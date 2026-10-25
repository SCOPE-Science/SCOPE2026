"""Exact finite checks for bridge--isolation covariance in unicyclic bond percolation.

Uses rational arithmetic; finite checks corroborate, but do not establish,
the all-cycle-length sign theorem proved analytically.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def connectivity_count(n, edges):
    parent = list(range(n))
    def root(a):
        while parent[a] != a:
            a=parent[a]
        return a
    for a,b in edges:
        x,y=root(a),root(b)
        if x!=y:parent[x]=y
    return len({root(i) for i in range(n)})


def brute(n,edges,p):
    m=len(edges)
    qb=1-p
    ez=Fraction(0);ei=Fraction(0);ebi=Fraction(0)
    for mask in range(1<<m):
        present=[edges[j] for j in range(m) if mask>>j&1]
        w=p**len(present)*qb**(m-len(present))
        c=connectivity_count(n,present)
        b=sum(connectivity_count(n,present[:j]+present[j+1:])>c for j in range(len(present)))
        deg=[0]*n
        for a,d in present:deg[a]+=1;deg[d]+=1
        i=sum(x==0 for x in deg)
        ez+=w*b;ei+=w*i;ebi+=w*b*i
    return ebi-ez*ei


def cycle(l):
    return [(i,(i+1)%l) for i in range(l)]


def identity(l,p,pendant):
    q=1-p
    if not pendant:
        return l*p*q*q*(l*p**(l-1)-2)
    return p*(-q-2*(l-1)*q*q-3*q**3+l*p**(l-1)*((l-1)*q*q+q**3))


def odds_coeffs(l):
    # F(u) = l u^(l-1)((l-1)u+l) - (1+u)^(l-1)(u^2+2lu+2(l+1))
    c=[0]*(l+2)
    c[l-1]+=l*l;c[l]+=l*(l-1)
    for j in range(l):
        v=comb(l-1,j)
        c[j]-=2*(l+1)*v
        c[j+1]-=2*l*v
        c[j+2]-=v
    return c


def run():
    checks=0
    for l in range(3,9):
        for pendant in [False,True]:
            n=l+int(pendant)
            if n>9:continue
            edges=cycle(l)+([(0,l)] if pendant else [])
            for p in [Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(19,20)]:
                lhs=brute(n,edges,p)
                rhs=identity(l,p,pendant)
                assert lhs==rhs, (l,pendant,p,lhs,rhs)
                checks+=1
    # A genuinely irregular unicyclic host checks the supporting identity.
    irregular=cycle(4)+[(0,4),(1,5)]
    degrees=[0]*6
    for a,b in irregular:degrees[a]+=1;degrees[b]+=1
    for p in [Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(19,20)]:
        q=1-p
        rhs=-p*sum(d*q**d for d in degrees)+4*p**4*sum(q**degrees[v] for v in range(4))
        assert brute(6,irregular,p)==rhs
        checks+=1
    for l in range(3,40):
        cs=odds_coeffs(l)
        assert cs[l+1]==-1
        assert cs[l]==l*l-4*l+1
        assert cs[l-1]==-3*(l*l-l+2)//2
        assert all(v<0 for v in cs[:l-1])
        checks+=4
    for l in range(3,7):
        cc=l*l-4*l+1;dd=3*(l*l-l+2)//2
        assert cc*cc-4*dd<0
        checks+=1
    for l in [7,8,9,10,12,20,40,100]:
        p=Fraction(2*l-1,2*l)
        assert identity(l,p,True)>0
        checks+=1
    print(f'PASS {checks} exact-rational checks, including exhaustive percolation states for cycles and single-leaf cycles of lengths 3-8.')
    print('l=7 witness normalized F:',identity(7,Fraction(13,14),True)/(Fraction(13,14)*Fraction(1,14)))

if __name__=='__main__':run()
