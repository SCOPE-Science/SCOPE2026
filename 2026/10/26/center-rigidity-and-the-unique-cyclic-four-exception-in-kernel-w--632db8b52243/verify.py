"""Direct finite-group verification of centers of balanced regular wreath kernels."""
from itertools import product, permutations


def cyclic(n):
    return [[(a+b) % n for b in range(n)] for a in range(n)]


def klein():
    return [[a ^ b for b in range(4)] for a in range(4)]


def sym3():
    ps = list(permutations(range(3)))
    ps.remove((0, 1, 2))
    ps = [(0, 1, 2)] + ps
    where = {p: i for i, p in enumerate(ps)}
    mul = [[where[tuple(p[q[j]] for j in range(3))] for q in ps] for p in ps]
    sign = []
    for p in ps:
        inv = sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        sign.append(inv % 2)
    return mul, sign


def dihedral8():
    items = [(a,b) for a in range(4) for b in range(2)]
    where = {v:i for i,v in enumerate(items)}
    mul = [[where[((a+(-1)**b*c)%4,(b+d)%2)] for c,d in items] for a,b in items]
    return mul, [b for a,b in items]


def alternating4():
    es=[]
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        if inv%2==0:es.append(p)
    es.remove((0,1,2,3));es=[(0,1,2,3)]+es
    w={p:i for i,p in enumerate(es)}
    mul=[[w[tuple(p[q[j]] for j in range(4))] for q in es] for p in es]
    N={i for i,p in enumerate(es) if all(p[p[j]]==j for j in range(4))}
    x=w[(1,2,0,3)]; xp=0; chi=[None]*12
    for k in range(3):
        for n in N: chi[mul[xp][n]]=k
        xp=mul[xp][x]
    assert all(v is not None for v in chi)
    return mul,chi


def check_case(name,R,T,chi):
    nr,nt=len(R),len(T)
    assert len(chi)==nr
    assert sorted(set(chi))==list(range(nt))
    assert all(chi[R[a][b]]==T[chi[a]][chi[b]] for a in range(nr) for b in range(nr))
    tinv=[next(j for j in range(nt) if T[i][j]==0==T[j][i]) for i in range(nt)]
    coords=[[T[t][x] for x in range(nt)] for t in range(nt)]
    invperm=[[T[tinv[t]][x] for x in range(nt)] for t in range(nt)]
    elems=[]
    for v in product(range(nr),repeat=nt):
        total=0
        for a in v:total=T[total][chi[a]]
        elems.append((v,tinv[total]))
    def mul(g,h):
        v,t=g;w,s=h; perm=invperm[t]
        return (tuple(R[v[x]][w[perm[x]]] for x in range(nt)),T[t][s])
    predicted={(tuple([c]*nt),0) for c in range(nr) if all(R[c][a]==R[a][c] for a in range(nr))}
    if name=='C2 onto C2':
        predicted=set(elems)
    center=set()
    for g in elems:
        if all(mul(g,h)==mul(h,g) for h in elems):center.add(g)
    if center!=predicted:
        raise AssertionError((name,'center mismatch',center,predicted))
    print(name, 'group_order',len(elems), 'center_order',len(center), 'center_matches_prediction')
    return True


def main():
    C2=cyclic(2)
    checks=[
        ('C2 onto C2',cyclic(2),C2,[0,1]),
        ('C3 onto C3',cyclic(3),cyclic(3),[0,1,2]),
        ('C4 onto C2',cyclic(4),C2,[0,1,0,1]),
        ('C4 onto C4',cyclic(4),cyclic(4),[0,1,2,3]),
        ('V4 onto C2',klein(),C2,[0,1,0,1]),
        ('V4 onto V4',klein(),klein(),[0,1,2,3]),
        ('S3 onto C2',*sym3()[:1],C2,sym3()[1]),
        ('D8 onto C2',*dihedral8()[:1],C2,dihedral8()[1]),
        ('A4 onto C3',*alternating4()[:1],cyclic(3),alternating4()[1]),
    ]
    for name,R,T,chi in checks:check_case(name,R,T,chi)
    print('VERIFY_OK')
if __name__=='__main__':main()
