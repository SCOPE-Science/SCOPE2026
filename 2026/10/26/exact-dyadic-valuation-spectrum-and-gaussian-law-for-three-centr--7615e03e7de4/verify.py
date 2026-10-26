"""Reproducibility checks for dyadic valuation statistics of 3-central binomial coefficients."""
from collections import Counter
from fractions import Fraction

def v2(n):
    assert n>0
    return (n & -n).bit_length()-1

def value_by_floor(n):
    # Use modular inverse separately of carry matrices.
    total=0
    alpha=1
    while (1<<alpha) <= 4*(n+1):
        q=1<<alpha
        inv=pow(3,-1,q)
        total += (n+inv-1)//q-n//q
        alpha+=1
    return total

def polys(L):
    # Integer polynomials represented as dict exponent -> coefficient.
    counts=[[1],[]] # carry 0,1; 1 initial empty prefix
    for j in range(L):
        b=j&1
        nxt=[[0]*(L+2) for _ in range(2)]
        for carry in (0,1):
            for exp,ways in enumerate(counts[carry]):
                if not ways:continue
                for digit in (0,1):
                    cout=int(digit+b+carry>=2)
                    nxt[cout][exp+cout]+=ways
        counts=nxt
    result=[0]*(L+3)
    for exp,ways in enumerate(counts[0]):result[exp]+=ways
    for exp,ways in enumerate(counts[1]):
        # Carry surviving odd-length prefix meets b=1, hence one final carry.
        result[exp+(L&1)]+=ways
    while result and not result[-1]:result.pop()
    return result

def exact_c(N):
    c=1
    v=[]
    for n in range(N):
        v.append(v2(c))
        numerator=c*3*(3*n+1)
        assert numerator%(n+1)==0
        c=numerator//(n+1)
    return v

def check():
    vals=exact_c(4096)
    for n,a in enumerate(vals):
        b=value_by_floor(n)
        assert a==b,(n,a,b)
    for L in range(13):
        h=Counter(vals[:1<<L])
        p=polys(L)
        assert all(h.get(i,0)==p[i] for i in range(len(p)))
        assert sum(p)==1<<L
        if L%2==0:
            assert p[0]==1<<(L//2)
            if L:
                assert p[-1]==1<<(L//2) and len(p)-1==L-1
        else:
            assert p[0]==1<<((L+1)//2)
            if L>=3:
                assert p[-1]==1<<(L//2) and len(p)-1==L
        print('L',L,'N',1<<L,'mean',sum(i*c for i,c in enumerate(p))/(1<<L))
    # Check the closed second-order recurrence for valuation polynomials,
    # without fitting coefficients from numerical samples.
    def shift_add(P, Q, shift, mul):
        for i,v in enumerate(Q):
            P[i+shift]+=mul*v
    for parity in (0,1):
        for m in range(2,15):
            X=polys(2*m+parity)
            A=polys(2*(m-1)+parity)
            B=polys(2*(m-2)+parity)
            Z=[0]*max(len(X),len(A)+2,len(B)+2)
            shift_add(Z,A,0,2);shift_add(Z,A,1,1);shift_add(Z,A,2,2)
            shift_add(Z,B,2,-4)
            while Z and not Z[-1]: Z.pop()
            assert X==Z,(parity,m,X,Z)
    print('VERIFY_OK: 4096 exact-integer coefficient valuations and separate modular-inverse floor checks; 13 dyadic histograms; 26 symbolic-polynomial recurrence checks; boundary extrema.')
if __name__=='__main__':check()
