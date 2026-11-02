"""Exact checks for excursion cover times of friendship graphs.

The walk is simple random walk started at the central vertex of n triangles
meeting only at their central vertex.  One excursion is a departure from the
center through the next return to the center.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial, exp, log, gamma


def multinomial(n, a, b):
    return comb(n, a) * comb(n-a, b)


def excursion_cdf_ie(n, m):
    total = Fraction(0)
    for a in range(n+1):
        for b in range(n-a+1):
            coeff = multinomial(n,a,b) * (-2)**a
            q = Fraction(4*n-3*a-4*b,4*n)
            total += coeff * q**m
    return total


def excursion_cdf_dp(n, m):
    # u: untouched blade pairs; v: pairs with one unseen leaf.
    d = {(n,0): Fraction(1)}
    for _ in range(m):
        nxt = {}
        def add(state, prob):
            nxt[state] = nxt.get(state,Fraction(0))+prob
        for (u,v),prob in d.items():
            if u:
                add((u-1,v+1), prob*Fraction(u,2*n))
                add((u-1,v),   prob*Fraction(u,2*n))
            if v:
                add((u,v-1),   prob*Fraction(3*v,4*n))
            add((u,v), prob*(1-Fraction(u,n)-Fraction(3*v,4*n)))
        d=nxt
    return d.get((0,0),Fraction(0))


def excursion_mean_ie(n):
    s=Fraction(0)
    for a in range(n+1):
        for b in range(n-a+1):
            if a+b==0: continue
            s += -multinomial(n,a,b)*(-2)**a*Fraction(4*n,3*a+4*b)
    return s


def excursion_mean_dp(n):
    @lru_cache(None)
    def e(u,v):
        if not (u or v):return Fraction(0)
        move=Fraction(u,n)+Fraction(3*v,4*n)
        total=Fraction(1)
        if u:
            total+=Fraction(u,2*n)*(e(u-1,v+1)+e(u-1,v))
        if v:
            total+=Fraction(3*v,4*n)*e(u,v-1)
        return total/move
    return e(n,0)


def walk_mean_markov(n):
    import sympy as sp
    N=2*n+1; allmask=(1<<N)-1
    neighbors={0:list(range(1,N))}
    for v in range(1,N):
        neighbors[v]=[0, v+1 if v%2 else v-1]
    dp={}
    for mask in range(allmask,-1,-1):
        if not (mask&1): continue
        verts=[v for v in range(N) if mask>>v&1]
        if mask==allmask:
            for v in verts:dp[mask,v]=sp.Rational(0)
            continue
        k=len(verts); A=sp.eye(k); rhs=sp.ones(k,1)
        lookup={v:i for i,v in enumerate(verts)}
        for i,v in enumerate(verts):
            for w in neighbors[v]:
                p=sp.Rational(1,len(neighbors[v]))
                if mask>>w&1:
                    A[i,lookup[w]]-=p
                else:
                    rhs[i]+=p*dp[mask|(1<<w),w]
        sol=A.inv()*rhs
        for i,v in enumerate(verts):dp[mask,v]=sol[i]
    return Fraction(dp[1,0])


def poisson_cdf(n,x):
    u=exp(-x)
    return (1-2*u/n+(u/n)**(4/3))**n


def run():
    count=0
    for n in range(1,7):
        for m in range(0,16):
            a=excursion_cdf_ie(n,m)
            b=excursion_cdf_dp(n,m)
            assert a==b and 0<=a<=1, (n,m,a,b)
            count+=1
        assert excursion_mean_ie(n)==excursion_mean_dp(n)
        count+=1
    for n in range(1,4):
        et=walk_mean_markov(n)
        rhs=3*excursion_mean_ie(n)-2
        assert et==rhs, (n,et,rhs)
        count+=1
    for x in (-0.5,0,0.5,1):
        for n in (10**3,10**4,10**5,10**6):
            g=poisson_cdf(n,x)
            g0=exp(-2*exp(-x))
            scaled=n**(1/3)*(g/g0-1)
            target=exp(-4*x/3)
            assert 0 <= g <= 1, (x,n,g)
            assert abs(scaled-target)<.2, (x,n,scaled,target)
            count+=2
    print('PASS',count,'exact identities / asymptotic numerical comparisons')
    for n in range(1,5):
        print('n=',n,'E[M]=',excursion_mean_ie(n),'E[T]=',3*excursion_mean_ie(n)-2)
    print('mean correction coefficient',4*gamma(4/3)/2**(4/3))

if __name__=='__main__':run()
