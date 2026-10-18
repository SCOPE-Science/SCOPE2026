"""Independent finite-state checks of the random transitive-delegation coverage formulas."""
from fractions import Fraction
from itertools import product
from math import factorial, exp, sqrt, erfc, pi

def one_guru_coverage(N,m):
    den=N-1
    alive=Fraction(1)
    result=Fraction(0)
    for k in range(N-m):
        result += Fraction(m,den)*alive
        alive *= Fraction(N-m-1-k,den)
    return result

def approx_one_guru_coverage(N,m):
    den=N-1
    alive=1.0
    result=0.0
    for k in range(N-m):
        result += m/den*alive
        alive *= (N-m-1-k)/den
        if alive<1e-16: break
    return result

def all_coverage(N,m):
    return Fraction(m*N**(N-m-1),(N-1)**(N-m)) if N-m else Fraction(1)

def direct_check(N,m):
    gurus=set(range(m))
    delegators=list(range(m,N))
    possible=[[j for j in range(N) if j!=i] for i in delegators]
    total=(N-1)**(N-m)
    all_good=0
    total_good=0
    total_non_guru_good=0
    for edges in product(*possible):
        f=dict(zip(delegators,edges))
        good=0
        for x in range(N):
            seen=set()
            v=x
            while v not in gurus and v not in seen:
                seen.add(v)
                v=f[v]
            if v in gurus:
                good+=1
        total_good+=good
        total_non_guru_good+=good-m
        if good==N: all_good+=1
    assert Fraction(total_non_guru_good,(N-m)*total)==one_guru_coverage(N,m)
    assert Fraction(all_good,total)==all_coverage(N,m)
    assert Fraction(total_good,N*total)==Fraction(m,N)+Fraction(N-m,N)*one_guru_coverage(N,m)
    return total

if __name__=='__main__':
    tested=0; profiles=0
    for N in range(2,8):
        for m in range(1,N+1):
            if m==N: continue
            profiles+=direct_check(N,m)
            tested+=1
    print('finite checks:',tested,'(N,m) pairs and',profiles,'profiles')
    for c in [0.5,1.0,2.0]:
        limit=c*sqrt(pi/2)*exp(c*c/2)*erfc(c/sqrt(2))
        for N in [10000,100000]:
            m=round(c*sqrt(N))
            p=approx_one_guru_coverage(N,m)
            assert abs(p-limit)<0.03, (N,m,p,limit)
        print('critical c',c,'limit',round(limit,9))
    for N,m in [(10000,10),(10000,1000),(10000,5000),(10000,9900)]:
        p=approx_one_guru_coverage(N,m); q=float(all_coverage(N,m))
        print('N,m,non-guru coverage,all-covered prob',N,m,round(p,8),round(q,8))
    print('VERIFY_OK')
