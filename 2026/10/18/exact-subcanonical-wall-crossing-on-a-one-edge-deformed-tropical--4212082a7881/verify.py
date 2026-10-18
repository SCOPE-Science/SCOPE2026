"""Exact rational checks for the subcanonical points of a one-edge metric K4.

No third-party dependencies. The finite-grid tests supplement, not replace,
the all-real-parameter mathematical proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations

EDGES=list(combinations(range(4),2))

def solve(M,b):
    n=len(b)
    a=[list(map(F,row))+[F(x)] for row,x in zip(M,b)]
    for j in range(n):
        i=next(i for i in range(j,n) if a[i][j]!=0)
        a[j],a[i]=a[i],a[j]
        h=a[j][j]
        a[j]=[x/h for x in a[j]]
        for i in range(n):
            if i!=j:
                t=a[i][j]
                if t: a[i]=[u-t*v for u,v in zip(a[i],a[j])]
    return [row[-1] for row in a]

def slopes(L, edge, t):
    # Node 4 is p; ground v_2. Positive Laplacian equals 4 at p and -4 at v_2.
    e=[(a,b,L if (a,b)==(0,1) else F(1)) for a,b in EDGES if (a,b)!=edge]
    ell=L if edge==(0,1) else F(1)
    assert 0<t<ell
    e += [(edge[0],4,t),(4,edge[1],ell-t)]
    A=[[F(0) for _ in range(5)] for _ in range(5)]
    for a,b,l in e:
        c=1/l
        A[a][a]+=c;A[b][b]+=c;A[a][b]-=c;A[b][a]-=c
    nodes=[0,1,3,4]
    rhs={0:F(0),1:F(0),3:F(0),4:F(4)}
    sol=solve([[A[i][j] for j in nodes] for i in nodes],[rhs[i] for i in nodes])
    pot={2:F(0),**dict(zip(nodes,sol))}
    return {(a,b):(pot[b]-pot[a])/ell for a,b,ell in e}

def integral_all(ss): return all(z.denominator==1 for z in ss.values())


def check():
    for L in [F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(2),F(3),F(5)]:
        found=[]
        for edge in EDGES:
            ell=L if edge==(0,1) else F(1)
            for n in range(1,int(ell*16)):
                t=F(n,16)
                if integral_all(slopes(L,edge,t)):
                    found.append((edge,t))
        predicted=[] if L<=1 else [((0,1),(L-1)/4),((0,1),(3*L+1)/4)]
        assert set(found)==set(predicted),(L,found,predicted)
        print('lambda=',L,'interior subcanonical=',found)
    print('PASS: exact rational Laplacian checks at all sampled points')

if __name__=='__main__':check()
