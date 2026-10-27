"""Exact independent checks for marked inversion participation versus decreasing triples.

Run: python3 research32_degree_triangles_verifier.py
Only Python's standard library is required. The analytical result is not
established by finite enumeration; the checker tests its identities.
"""
from itertools import combinations, permutations
from fractions import Fraction as Q
from math import comb, factorial


def choose(m,k):
    return comb(m,k) if m >= k and k >= 0 else 0


def proposed_covariance(n,i):
    assert n>=3 and 1<=i<=n
    return Q((n-2)*(n-1)*(n+1),48)-Q((n-3)*(i-1)*(n-i),24)


def proposed_variance_degree(n,i):
    return Q(2*(n-1)+(n-2*i+1)**2,12)


def overlap_covariance(n,i):
    """Sum the rigorous 3- and 4-point overlap probabilities.

    Edge inside a decreasing triple: covariance 1/12. One shared index:
    +/-1/24 for an extremal entry and 0 for the middle entry.
    """
    a=choose(n-1,2)
    first=choose(n-i,2)*(n-2*i-1)
    last=choose(i-1,2)*(2*i-n-3)
    external=(i-1)*(n-i)*(n-3)
    return Q(a,6)+Q(first+last,24)+Q(external,24)


def exact_polynomial_integral_variance():
    """Integrate the squared first-order projection over [0,1]^2 exactly.

    A polynomial is a map (power of t, power of x) -> coefficient.
    """
    def add(*polys):
        out={}
        for p in polys:
            for k,v in p.items():out[k]=out.get(k,Q())+v
        return {k:v for k,v in out.items() if v}
    def mul(p,q):
        out={}
        for (a,b),c in p.items():
            for (d,e),f in q.items():
                key=(a+d,b+e)
                out[key]=out.get(key,Q())+c*f
        return {k:v for k,v in out.items() if v}
    def scale(p,k): return {a:b*k for a,b in p.items()}
    one={(0,0):Q(1)}; t={(1,0):Q(1)};x={(0,1):Q(1)}
    t2=mul(t,t);om_t=add(one,scale(t,-1));om_x=add(one,scale(x,-1))
    g=add(scale(mul(mul(om_t,om_t),mul(x,x)),Q(1,4)),
          mul(mul(t,om_t),mul(x,om_x)),
          scale(mul(t2,mul(om_x,om_x)),Q(1,4)),
          {(0,0):-Q(1,12)})
    for a in range(3):
        assert sum(c/Q(b+1) for (aa,b),c in g.items() if aa==a)==0
    var=sum(c/Q(a+1)/Q(b+1) for (a,b),c in mul(g,g).items())
    assert var==Q(13,7200),(var,Q(13,7200))
    return var


def enumerate_exact(n):
    pairs=list(combinations(range(n),2));triples=list(combinations(range(n),3))
    total=factorial(n);sum_d=[0]*n;sum_d2=[0]*n;sum_t=0;sum_dt=[0]*n
    for p in permutations(range(n)):
        d=[0]*n
        for i,j in pairs:
            if p[i]>p[j]:d[i]+=1;d[j]+=1
        tri=sum(p[i]>p[j]>p[k] for i,j,k in triples)
        sum_t+=tri
        for i in range(n):
            sum_d[i]+=d[i];sum_d2[i]+=d[i]*d[i]
            sum_dt[i]+=d[i]*tri
    assert Q(sum_t,total)==Q(choose(n,3),6)
    for i in range(1,n+1):
        cov=Q(sum_dt[i-1],total)-Q(sum_d[i-1]*sum_t,total*total)
        vd=Q(sum_d2[i-1],total)-Q(sum_d[i-1]**2,total*total)
        assert Q(sum_d[i-1],total)==Q(n-1,2)
        assert cov==proposed_covariance(n,i)==overlap_covariance(n,i),(n,i,cov)
        assert vd==proposed_variance_degree(n,i),(n,i,vd)
    print('EXHAUSTIVE_PASS',n,'permutations',total,'marked_positions',n)


def main():
    for n in range(3,9):enumerate_exact(n)
    for n in (3,4,5,6,8,13,50,101,250,1000):
        for i in range(1,n+1):
            assert overlap_covariance(n,i)==proposed_covariance(n,i)
            assert proposed_covariance(n,i)>0
            assert proposed_covariance(n,i)==proposed_covariance(n,n+1-i)
        assert proposed_covariance(n,1)==proposed_covariance(n,n)
        print('ALL_POSITION_OVERLAP_PASS',n)
    c=exact_polynomial_integral_variance()
    print('EXACT_PROJECTION_VARIANCE_CONSTANT_PASS',c)
    print('VERIFY_OK')

if __name__=='__main__':main()
