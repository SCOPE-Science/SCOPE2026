"""Independent finite checks of partial-inner-map classification for Rees zero-matrix semigroups.
No external dependencies; direct multiplication and domains, not the closed-form proof.
"""
from itertools import permutations, product


def cyclic_group(n):
    return list(range(n)), 0, lambda x,y: (x+y)%n

def sym3():
    elements = list(permutations(range(3)))
    e = (0,1,2)
    def mul(x,y):
        return tuple(x[y[i]] for i in range(3))
    return elements,e,mul


def check(P, group, label):
    G,e,gm = group
    I=len(P[0]); L=len(P)
    assert all(any(P[j][i] is not None for i in range(I)) for j in range(L))
    assert all(any(P[j][i] is not None for j in range(L)) for i in range(I))
    S=[None]+[(i,x,j) for i in range(I) for x in G for j in range(L)]
    ext=('IDENTITY',)
    def prod(a,b):
        if a==ext:return b
        if b==ext:return a
        if a is None or b is None: return None
        t=P[a[2]][b[0]]
        return None if t is None else (a[0],gm(gm(a[1],t),b[1]),b[2])
    def varphi(g,h):
        gh=prod(g,h)
        return tuple(sorted(((a,prod(prod(h,a),g)) for a in S if prod(gh,a)==a==prod(a,gh)),key=lambda x: S.index(x[0])))
    maps={varphi(g,h) for g in S+[ext] for h in S+[ext]}
    m=sum(v is not None for row in P for v in row)
    conjugation_maps={tuple((x,gm(gm(ginv,x),g)) for x in G) for g in G for ginv in G if gm(g,ginv)==e==gm(ginv,g)}
    expected=(m*m*len(conjugation_maps)+2 if m>1 else len(conjugation_maps)+1)
    if len(maps)!=expected:
        raise AssertionError((label,m,len(maps),expected))
    idS=tuple((a,a) for a in S)
    assert idS in maps
    zero=tuple(((None,None),))
    assert zero in maps
    def compose(f,g):
        dic=dict(g)
        return tuple((a,dic[b]) for a,b in f if b in dic)
    # Directly check closure and identity of the generated set.
    for f in maps:
        assert compose(f,idS)==f==compose(idS,f)
        for g in maps:
            assert compose(f,g) in maps, (label,'composition outside predicted generators')
    print(f'{label}: |S|={len(S)}, idempotents={m}, partial-inner maps={len(maps)}, predicted={expected}; closure verified')
    return len(maps)


def run():
    C1=cyclic_group(1)
    C2=cyclic_group(2)
    C3=cyclic_group(3)
    S3=sym3()
    for G,label in [(C1,'trivial'),(C2,'C2'),(C3,'C3'),(S3,'S3')]:
        e=G[1]
        check([[e]],G,f'{label}: 1x1')
        check([[e,None],[None,e]],G,f'{label}: 2x2 diagonal')
        check([[e,e],[None,e]],G,f'{label}: 2x2 triangle')
        check([[e,e],[e,e]],G,f'{label}: 2x2 full')
    e=C2[1]
    check([[e,1,None],[1,None,e]],C2,'C2: sparse 2x3 with nonidentity entries')
    check([[e,e,e],[1,None,None]],C2,'C2: distinct 2x3 zero pattern')
    print('VERIFY_OK')

if __name__=='__main__':run()
