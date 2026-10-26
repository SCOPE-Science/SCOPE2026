"""Finite exact checks for bounded integral square-zero 2-by-2 matrices.

The infinite counting and distribution limits require the accompanying proof.
"""
from math import gcd, isqrt

def phi_sieve(n):
    ph = list(range(n + 1))
    for p in range(2, n + 1):
        if ph[p] == p:
            for j in range(p, n + 1, p):
                ph[j] -= ph[j] // p
    return ph

def formula(T, ph):
    return 1 + 8 * sum(ph[m] * (T // (m*m)) for m in range(1, isqrt(T) + 1))

def all_direct(T):
    ans = set()
    for a in range(-T, T+1):
        for b in range(-T, T+1):
            if b == 0:
                if a == 0:
                    for c in range(-T, T+1):
                        ans.add((a,b,c,-a))
                continue
            if a*a % b: continue
            c = -(a*a // b)
            if -T <= c <= T:
                ans.add((a,b,c,-a))
    return ans

def parameterized(T):
    ans = {(0,0,0,0)}
    for u in range(0, isqrt(T)+1):
        for v in range(-isqrt(T),isqrt(T)+1):
            if (u == 0 and v != 1) or (u,v)==(0,0):continue
            if gcd(u, v) != 1:continue
            m=max(u,abs(v))
            for t in range(-T//(m*m),T//(m*m)+1):
                if t == 0 or abs(t)*m*m > T:continue
                ans.add((-t*u*v,t*u*u,-t*v*v,t*u*v))
    return ans

def run():
    ph=phi_sieve(300)
    tests= [1,2,3,4,5,6,7,8,9,10,11,12,13,16,20,25,30,40,50]
    for T in tests:
        direct=all_direct(T)
        param=parameterized(T)
        assert direct==param, (T,len(direct),len(param),list(direct-param)[:4],list(param-direct)[:4])
        assert len(direct)==formula(T,ph),(T,len(direct),formula(T,ph))
        for a,b,c,d in direct:
            assert a+d==0 and a*d==b*c
    sector_checks=0
    for T in [1,2,3,4,5,7,9,12,16,21,30,40,50]:
        direct=all_direct(T)
        for H in {1,2,3,5,T}:
            for radius in {T, T//2, T//3}:
                a=0
                for x,b,c,d in direct:
                    if (x,b,c,d)==(0,0,0,0):continue
                    content=gcd(gcd(abs(x),abs(b)),abs(c))
                    # Kernel vector (b,-x), except when b=x=0 (vertical line).
                    u,v=(b,-x) if (b,x)!=(0,0) else (0,1)
                    if content<=H and u!=0 and abs(v)<=abs(u) and max(abs(x),abs(b),abs(c))<=radius:a+=1
                b=2*sum((3 if m==1 else 2*ph[m])*min(H,radius//(m*m)) for m in range(1,isqrt(radius)+1))
                assert a==b,(T,H,radius,a,b)
                sector_checks+=1
    for T in range(1,300):
        # alternate exact count from summing over matrix contents
        alt=1+2*sum(4*sum(ph[m] for m in range(1,isqrt(T//t)+1)) for t in range(1,T+1))
        assert alt == formula(T,ph),(T,alt,formula(T,ph))
    print(f'VERIFY_OK direct_and_parameter_sets=19 max_T=50 sector_content_checks={sector_checks} alternate_content_counts=299 all_exact=PASS')
if __name__=='__main__':run()
