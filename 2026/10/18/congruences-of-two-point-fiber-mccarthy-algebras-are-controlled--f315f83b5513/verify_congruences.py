"""Independent exhaustive congruence census of two-fibre McCarthy algebras.
Run with Python 3; no external packages required.
"""
from itertools import product

def partitions(n):
    a=[0]*n
    def go(i,m):
        if i==n:
            yield tuple(a)
        else:
            for k in range(m+2):
                a[i]=k
                yield from go(i+1,max(m,k))
    if not n:
        yield ()
    else:
        yield from go(1,0)

def is_cong(part, joins):
    n=len(joins)
    return all(part[joins[i][k]]==part[joins[j][k]] for i in range(n) for j in range(n) if part[i]==part[j] for k in range(n))

def mccarthy_cong(part, joins):
    n=len(joins)
    # encode 2*i+b
    def mul(x,y):
        i,b=divmod(x,2);j,c=divmod(y,2)
        return (2*i) if b==0 else (2*joins[i][j]+c)
    for x in range(2*n):
        for y in range(2*n):
            if part[x]!=part[y]:continue
            if part[x^1]!=part[y^1]:return False
            for z in range(2*n):
                if part[mul(x,z)] != part[mul(y,z)]:return False
                if part[mul(z,x)] != part[mul(z,y)]:return False
    return True

def expected_congs(joins):
    n=len(joins)
    tops=set(range(n))
    top=0
    for i in range(n): top=joins[top][i]
    expected=[]
    for p in partitions(n):
        if not is_cong(p,joins):continue
        for flag in (0,1):
            cl=[0]*(2*n)
            reps={};nxt=0
            for i in range(n):
                for b in range(2):
                    key=(p[i],None if flag and p[i]==p[top] else b)
                    if key not in reps:reps[key]=nxt;nxt+=1
                    cl[2*i+b]=reps[key]
            expected.append(tuple(cl))
    return expected

def norm(part):
    seen={};a=[]
    for x in part:
        if x not in seen:seen[x]=len(seen)
        a.append(seen[x])
    return tuple(a)

def verify(name,join):
    nc=sum(is_cong(p,join) for p in partitions(len(join)))
    expected={norm(p) for p in expected_congs(join)}
    actual={norm(p) for p in partitions(2*len(join)) if mccarthy_cong(p,join)}
    assert expected==actual,(name, 'unexpected',actual-expected, 'missing',expected-actual)
    assert len(actual)==2*nc
    print(f'{name}: semilattice_congruences={nc}, McCarthy_congruences={len(actual)}, exact_pairs_checked={len(actual)}')

if __name__=='__main__':
    for n in range(1,5):
        join=[[max(i,j) for j in range(n)] for i in range(n)]
        verify(f'chain_{n}',join)
    # Four-element Boolean join semilattice (diamond).
    verify('Boolean_diamond_4',[[i|j for j in range(4)] for i in range(4)])
    # Five-element join semilattice with three incomparable atoms.
    fan=[]
    for i in range(5):
        fan.append([j if i==0 else i if j==0 or i==j else 4 for j in range(5)])
    verify('three_atom_fan_5',fan)
    print('MCCARTHY_SEMILATTICE_CONGRUENCE_PRODUCT_OK')
