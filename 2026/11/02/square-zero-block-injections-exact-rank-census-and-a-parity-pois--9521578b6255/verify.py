#!/usr/bin/env python3
"""Independent finite-model and asymptotic checks for square-zero block injections."""
from itertools import combinations, permutations, product
from math import factorial, comb, sqrt, cosh, sinh, exp, lgamma

def maps(k,m):
    blocks=[tuple(range(i*m,(i+1)*m)) for i in range(k)]
    yield (-1,)*(k*m),0
    for t in range(1,k+1):
        for dom in combinations(range(k),t):
            for im in combinations(range(k),t):
                for perms in product(permutations(range(m)),repeat=t):
                    arr=[-1]*(k*m)
                    for h,(di,ii) in enumerate(zip(dom,im)):
                        for x,y in enumerate(perms[h]):
                            arr[di*m+x]=ii*m+y
                    yield tuple(arr),t

def squares_to_zero(f):
    return all(y<0 or f[y]<0 for y in f)

def pred(k,m,t):
    if 2*t>k:return 0
    return factorial(k)*factorial(m)**t//(factorial(k-2*t)*factorial(t)**2)

def check_exact():
    tests=[(k,m) for m,top in ((1,7),(2,6),(3,4)) for k in range(1,top+1)]
    for k,m in tests:
        got=[0]*(k+1)
        total=0
        for f,t in maps(k,m):
            total+=1
            if squares_to_zero(f):got[t]+=1
        expect=[pred(k,m,t) for t in range(k+1)]
        total_expect=sum(comb(k,t)**2 * factorial(m)**t for t in range(k+1))
        assert got==expect,(k,m,got,expect)
        assert total==total_expect,(k,m,total,total_expect)
    print('DIRECT_ENUMERATION_OK',len(tests))

def conditional_law(k,m):
    a=factorial(m)
    ws=[]
    for h in range(k%2,k+1,2):
        t=(k-h)//2
        ws.append((h,lgamma(k+1)-2*lgamma(t+1)-lgamma(h+1)+t*__import__('math').log(a)))
    maxi=max(v for _,v in ws)
    v=[(h,exp(x-maxi)) for h,x in ws]
    s=sum(x for _,x in v)
    return [(h,x/s) for h,x in v]

def check_asymptotic():
    # Critical lambda=k/(2*sqrt(m!)) matched along k to successive factorial sizes.
    for m in (5,6,7,8):
        base=round(2.0*sqrt(factorial(m)))
        for k in (base,base+1):
            par=k%2
            lam=k/(2*sqrt(factorial(m)))
            law=conditional_law(k,m)
            norm=cosh(lam) if par==0 else sinh(lam)
            target={h:lam**h/factorial(h)/norm for h in range(par, min(k+100,151),2)}
            tv=.5*(sum(abs(p-target.get(h,0.0)) for h,p in law)
                     +sum(q for h,q in target.items() if h>k))
            # Remaining far-Poisson tail is negligible at lambda about 1.
            print('CRITICAL',m,k,round(lam,6),round(tv,7))
            assert tv < .1,(m,k,tv)
    for m in (1,2,3):
        p0=1/(1+2*sqrt(factorial(m)))
        for k in (200,800):
            law=conditional_law(k,m)
            mean=sum(h*p for h,p in law)/k
            var=sum((h-k*p0)**2*p for h,p in law)/k
            print('FIXED_M',m,k,round(mean,6),round(var,6))
            assert abs(mean-p0)<.02
            assert abs(var-p0*(1-p0))<.02

def main():
    check_exact()
    check_asymptotic()
    print('VERIFY_OK')
if __name__=='__main__':main()
