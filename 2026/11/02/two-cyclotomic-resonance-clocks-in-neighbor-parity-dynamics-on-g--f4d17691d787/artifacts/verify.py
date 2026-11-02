"""Exact GF(2) verification of transient shells for generalized Petersen GP(n,2)."""
from math import gcd

def rank(rows, dim):
    basis={}
    for z in rows:
        while z:
            p=z.bit_length()-1
            if p not in basis:
                basis[p]=z
                break
            z^=basis[p]
    return len(basis)

def mul(X,Y,size):
    return [sumxor(X[i],Y,size) for i in range(size)]

def sumxor(row,Y,size):
    w=0
    while row:
        bit=row&-row
        j=bit.bit_length()-1
        w^=Y[j]
        row^=bit
    return w

def adjacency(n):
    s=2*n
    rows=[]
    for i in range(n):
        row= (1 << ((i-1)%n)) ^(1<<((i+1)%n)) ^ (1<<(n+i))
        rows.append(row)
    for i in range(n):
        row= (1 << (n+(i-2)%n)) ^(1 << (n+(i+2)%n)) ^ (1<<i)
        rows.append(row)
    return rows

def predicted(n,t):
    e=n&-n
    return (2*min(t,2*e) if n%3==0 else 0) + (4*min(t,e) if n%5==0 else 0)

def verify():
    cases=0
    for n in range(5,101):
        A=adjacency(n)
        size=2*n
        X=[1<<i for i in range(size)]
        e=n&-n
        # check all steps to max possible threshold, plus one stable check
        for t in range(1,min(2*e+2, 66)):
            X=mul(X,A,size)
            null=size-rank(X,size)
            want=predicted(n,t)
            assert null==want,(n,t,null,want)
            cases+=1
        # Some cases with large e need bounded extrapolation using powering
        if 2*e+1>66:
            for t in [2*e-1,2*e,2*e+1]:
                Z=[1<<i for i in range(size)]
                B=A
                k=t
                while k:
                    if k&1: Z=mul(Z,B,size)
                    k//=2
                    if k: B=mul(B,B,size)
                assert size-rank(Z,size)==predicted(n,t),(n,t)
                cases+=1
    # Exhaustively verify first-entry counts for small n with state enumeration
    enumerated=0
    for n in range(5,9):
        N=2*n
        A=adjacency(n)
        e=n&-n
        timebound=2*e if n%3==0 else (e if n%5==0 else 0)
        P=(1 << (N-predicted(n,timebound)))
        counts=[0]*(timebound+1)
        # membership in stable image = image of A^timebound; via stabilized kernel criterion
        # x periodic iff A^T x = x under invertible factor? Instead use rank decomposition:
        # Periodic iff x in image(A^timebound), constructed using bit-basis.
        Q=[1<<i for i in range(N)]
        for _ in range(timebound): Q=mul(Q,A,N)
        base={}
        for row in Q:
            v=row
            while v:
                k=v.bit_length()-1
                if k not in base:
                    base[k]=v;break
                v ^= base[k]
        def belongs(v):
            while v:
                k=v.bit_length()-1
                if k not in base:return False
                v ^= base[k]
            return True
        assert (1<<len(base))==P
        for x in range(1<<N):
            y=x
            for t in range(timebound+1):
                if belongs(y):
                    counts[t]+=1
                    break
                y=sumxor(y,A,N)
        expect=[P]
        for t in range(1,timebound+1):
            expect.append((1<<(N-predicted(n,timebound)+predicted(n,t)))-(1<<(N-predicted(n,timebound)+predicted(n,t-1))))
        assert counts==expect,(n,counts,expect)
        enumerated+=1<<N
    print('OK GF2 generalized Petersen GP(n,2): matrix-kernel tests',cases,'state checks',enumerated)
    for n in [5,6,9,10,15,30]:
        e=n&-n
        delta=(n%3==0,n%5==0)
        deficiency=4*e*sum(delta)
        first_time=2*e if delta[0] else e if delta[1] else 0
        print('n',n,'periodic dimension',2*n-deficiency,'max entry',first_time)
if __name__=='__main__':verify()
