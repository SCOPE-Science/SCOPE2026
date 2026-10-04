from fractions import Fraction
from itertools import product, combinations


def rank(mat):
    a=[list(map(Fraction,row)) for row in mat]
    if not a:return 0
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]
        a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c]
                a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def qval(d, a, s):
    out=Fraction(1)
    for (i,j),v in a.items(): out += v*s[i]*s[j]
    return out

for d in range(2,11):
    edges=list(combinations(range(d),2))
    target=d if d%2==0 else d+1
    ar=Fraction(2,d if d%2==0 else d-1)
    a={e:ar for e in edges}
    vals=[qval(d,a,s) for s in product((-1,1), repeat=d)]
    assert min(vals)==0 and all(v>=0 for v in vals)
    assert Fraction(1)+sum(a.values())==target
    if d%2:
        signs=[s for s in product((-1,1), repeat=d) if sum(s)==1]
        M=[[s[i]*s[j] for i,j in edges] for s in signs]
        assert rank(M)==len(edges)
    else:
        signs=[s for s in product((-1,1), repeat=d) if sum(s)==0]
        M=[[s[i]*s[j] for i,j in edges] for s in signs]
        # affine equations have same coefficient rank; expected edge-space rank E-(d-1)
        if d==2:
            assert rank(M)==1
        else:
            assert rank(M)==len(edges)-(d-1)
        if d>=4:
            # explicit nonradial interior example u_i=1/d+eps*(i-(d-1)/2), sum perturbation zero
            eps=Fraction(1, 20*d*d)
            center=Fraction(d-1,2)
            u=[Fraction(1,d)+eps*(Fraction(i)-center) for i in range(d)]
            assert sum(u)==1
            for r in range(d//2):
                for B in combinations(range(d),r):
                    assert sum(u[i] for i in B) <= Fraction(1,2)
            ae={(i,j):u[i]+u[j] for i,j in edges}
            vv=[qval(d,ae,s) for s in product((-1,1), repeat=d)]
            assert all(v>=0 for v in vv)
            assert Fraction(1)+sum(ae.values())==target
print('VERIFY_OK dimensions=2..10 radial_values=exact odd_unique_ranks=exact even_extremal_dimensions=exact nonradial_examples=exact')
