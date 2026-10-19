"""Reproduce absorbing configurations in the ANNNI Glauber chain by independent direct Hamiltonian enumerations."""
from collections import Counter
from fractions import Fraction
from math import comb

def energy(s,J,K,h):
    n=len(s)
    return -J*sum(s[i]*s[(i+1)%n] for i in range(n)) + K*sum(s[i]*s[(i+2)%n] for i in range(n)) - h*sum(s)

def direct(n,J,K,h):
    counts=Counter()
    for m in range(1<<n):
        s=tuple(1 if m&(1<<i) else -1 for i in range(n))
        E=energy(s,J,K,h)
        blocked=True
        for i in range(n):
            t=list(s);t[i]=-t[i]
            if energy(t,J,K,h)<=E:
                blocked=False
                break
        if blocked: counts[s.count(-1)]+=1
    return counts

def trace_formula(n):
    c=Counter({0:1,n:1})
    for k in range(1,n//4+1):
        c[2*k]+= n*comb(n-3*k-1,k-1)//k
    return c

def predicted(n,J,K,h):
    if h==0: return Counter({0:1,n:1,n//2:4}) if n%4==0 else Counter({0:1,n:1})
    if 0<h<2*K:return trace_formula(n)
    if 2*K<=h<2*(J-K):return Counter({0:1,n:1})
    return Counter({0:1})

def run():
    tested=0
    for J,K in [(10,1),(10,3),(10,4),(11,5)]:
        for h in sorted(set([0,1,K,2*K-1,2*K,2*K+1,2*(J-K)-1,2*(J-K),2*(J-K)+1])):
            if h<0:continue
            for n in range(5,15):
                got=direct(n,J,K,h)
                want=predicted(n,J,K,h)
                if got!=want:raise AssertionError((J,K,h,n,got,want))
                tested+=1
    print('PASS',tested,'complete finite-state parameter checks; independent full Hamiltonian, no transfer simplification')
    for n in [5,6,8,10,12,14]:
        print('N',n, 'low-field total',sum(trace_formula(n).values()),'polynomial',sorted(trace_formula(n).items()))
if __name__=='__main__':run()
