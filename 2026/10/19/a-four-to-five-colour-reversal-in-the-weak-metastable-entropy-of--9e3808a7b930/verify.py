# Reproduce finite checks of weakly blocked q=4 and q=5 clock chains.
# All spin positions are labelled; only strictly energy-decreasing recolourings are forbidden.
import itertools, math
from functools import lru_cache

def weakly_blocked_by_direct_energy(q,word):
    n=len(word); val=[math.cos(2*math.pi*i/q) for i in range(q)]
    for i in range(n):
        a,b=word[i-1],word[(i+1)%n]; old=val[(word[i]-a)%q]+val[(word[i]-b)%q]
        for k in range(q):
            if val[(k-a)%q]+val[(k-b)%q]>old+1e-9: return False
    return True

def enumeration(q,n):
    count=0
    for w in itertools.product(range(q),repeat=n): count+=weakly_blocked_by_direct_energy(q,w)
    return count

def trace_mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(A))) for j in range(len(B[0]))] for i in range(len(A))]
def trace_power(A,n):
    M=[[int(i==j) for j in range(len(A))] for i in range(len(A))]
    for _ in range(n): M=trace_mul(M,A)
    return sum(M[i][i] for i in range(len(A)))

def analytic4(n):
    # signed hard core matrix walls parity, trace integer
    m1=[[1,1],[1,0]]; m2=[[1,1],[-1,0]]
    return (trace_power(m1,n)+trace_power(m2,n))**2

def analytic5(n):
    # integer DP over three step-types and residue mod 5, cyclic trace
    T=((1,1,1),(1,1,0),(1,0,1)); d=(0,1,-1)
    total=0
    for a in range(3):
        dp={(a,0):1}
        for _ in range(n):
            nxt={}
            for (last,res),ways in dp.items():
                for b in range(3):
                    if T[last][b]:
                        key=(b,(res+d[last])%5)
                        nxt[key]=nxt.get(key,0)+ways
            dp=nxt
        total+=dp.get((a,0),0)
    return 5*total

if __name__=='__main__':
    for n in range(3,8):
        a,b=enumeration(4,n),enumeration(5,n)
        x,y=analytic4(n),analytic5(n)
        assert (a,b)==(x,y),(n,a,b,x,y)
        print(n,a,b)
    for n in range(8,17):
        a,b=analytic4(n),analytic5(n)
        assert a>b, (n,a,b)
    print('PASS direct recoloring enumeration q=4,5 n=3..7; transfer comparisons n=3..16')
