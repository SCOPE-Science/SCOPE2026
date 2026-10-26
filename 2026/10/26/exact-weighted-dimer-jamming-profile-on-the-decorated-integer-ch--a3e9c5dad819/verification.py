from fractions import Fraction as F
from functools import lru_cache
from math import factorial

def formula(L,i,A,B):
    a=F(B,A+B);g=F(A,A+B);s=F(0)
    for j in range(i):
     for k in range(L-i+1):
      z=j+k
      poch=F(1)
      for t in range(1,z+1):poch*=a+t
      s+=(-g)**z*F(factorial(z),factorial(j)*factorial(k))/poch
    return s

def direct(L,i,A,B):
    ed=[(u,u+1,A,False) for u in range(L-1)]+[(u,L+u,B,u==i-1) for u in range(L)]
    @lru_cache(None)
    def dp(mask):
     choices=[(u,v,w,target) for u,v,w,target in ed if not ((mask>>u)&1 or (mask>>v)&1)]
     total=sum(w for u,v,w,tar in choices)
     if not total: return F(0)
     return sum((F(w,total)*(1 if tar else dp(mask|(1<<u)|(1<<v))) for u,v,w,tar in choices),F(0))
    return dp(0),dp.cache_info()


def exponential_series(x, n):
    p=1.0;s=1.0
    for j in range(1,n+1):
        p *= -x/j
        s += p
    return s

def integrate_exp(fn):
    # Adaptive Simpson on [0,45]; the omitted tail is at most exp(-45).
    from math import exp
    def sim(a,b,fa,fm,fb):return (b-a)*(fa+4*fm+fb)/6
    def rec(a,b,fa,fm,fb,s,eps,depth):
        m=(a+b)/2;lm=(a+m)/2;rm=(m+b)/2
        fl=fn(lm);fr=fn(rm)
        x=sim(a,m,fa,fl,fm);y=sim(m,b,fm,fr,fb)
        if depth==0 or abs(x+y-s)<=15*eps:
            return x+y+(x+y-s)/15
        return rec(a,m,fa,fl,fm,x,eps/2,depth-1)+rec(m,b,fm,fr,fb,y,eps/2,depth-1)
    a=0;b=45;m=(a+b)/2
    fa=fn(a);fm=fn(m);fb=fn(b)
    return rec(a,b,fa,fm,fb,sim(a,b,fa,fm,fb),1e-13,35)

def bulk_prob(b):
    from math import exp
    c=2/(1+b);ratio=1+1/b
    return integrate_exp(lambda y:exp(-y-c*(1-exp(-ratio*y))))

def verify():
    from math import exp, factorial
    tested=0
    for L in range(1,8):
      for alpha,beta in [(1,1),(1,2),(2,1),(3,5)]:
       for i in range(1,L+1):
        a=formula(L,i,alpha,beta);b,_=direct(L,i,alpha,beta)
        assert a==b,(L,i,alpha,beta,a,b)
        tested+=1
    for b in [0.03,0.1,0.5,1.,3.,30.]:
      p=bulk_prob(b)
      assert 0<p<1
      gam=1/(1+b)
      for L in [7,13,21]:
        i=(L+1)//2
        # independent finite-cavity integration with truncated exponential
        from math import exp
        a=b/(1+b)
        def integrand(y):
            u=1-exp(-(1+1/b)*y)
            return exp(-y)*exponential_series(gam*u,i-1)*exponential_series(gam*u,L-i)
        pf=integrate_exp(integrand)
        bound=gam**i/factorial(i)+gam**(L-i+1)/factorial(L-i+1)
        assert abs(pf-p)<bound+1e-11,(L,b,pf,p,bound)
    assert abs(bulk_prob(0.0001)-exp(-2))<.0002
    assert abs(bulk_prob(300)-(1-1/300))<.00003
    pvals=[bulk_prob(x) for x in [.05,.2,1,4,50]]
    assert pvals==sorted(pvals)
    print('PASS',tested,'exact rational comb configurations; 54 finite-volume bounds; weak/strong-rate limits; monotonic sample')

if __name__=='__main__':
    verify()
