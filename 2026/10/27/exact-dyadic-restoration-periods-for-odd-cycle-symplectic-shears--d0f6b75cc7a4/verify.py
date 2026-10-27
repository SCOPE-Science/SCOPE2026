#!/usr/bin/env python3
"""Independent integer-ring checks for odd-cycle symplectic shears.

Usage: python3 verify.py. No third-party packages are needed.
The analytic proof (not this bounded computation) establishes the theorem for all odd n.
"""

def mul(X,Y,q):
    n=len(X[0][0]); Z=[[[0]*n for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                a=X[i][k]; b=Y[k][j]
                for r in range(n):
                    if a[r]:
                        for t in range(n):
                            if b[t]: Z[i][j][(r+t)%n]=(Z[i][j][(r+t)%n]+a[r]*b[t])%q
    return Z

def identity(n):
    X=[[[0]*n for _ in range(2)] for _ in range(2)]
    X[0][0][0]=X[1][1][0]=1
    return X

def make(n):
    T=identity(n)
    T[0][1][1]=T[0][1][n-1]=1
    T[1][0][0]=1
    T[1][1][1]=T[1][1][n-1]=1
    return T

def mpow(X,e,q):
    Y=identity(len(X[0][0]))
    while e:
        if e&1:Y=mul(Y,X,q)
        X=mul(X,X,q);e//=2
    return Y

def same(X,Y,q):
    return all((X[i][j][r]-Y[i][j][r])%q==0 for i in range(2) for j in range(2) for r in range(len(X[0][0])))

def trial(n,s):
    q=1<<s;T=make(n);I=identity(n)
    predicted=(2*n if s==1 else 4*n*(1<<max(0,s-3)))
    assert same(mpow(T,predicted,q),I,q), (n,s,'upper')
    # order has only prime factors 2 and primes dividing odd n.
    def pf(x):
        out=[];p=2
        while p*p<=x:
            if x%p==0:
                out.append(p)
                while x%p==0:x//=p
            p+=1
        if x>1:out.append(x)
        return out
    for p in pf(predicted):
        assert not same(mpow(T,predicted//p,q),I,q), (n,s,p,'lower')
    return 1+len(pf(predicted))

def run():
    tests=0
    for n in range(3,26,2):
        T=make(n);I=identity(n)
        # Check the precise 2-adic intermediary identity in the Laurent quotient.
        A=mpow(T,2*n,4)
        target=identity(n)
        for j in range(n):
            target[0][0][j]=(target[0][0][j]+2)%4
            target[1][1][j]=(target[1][1][j]+2)%4
        assert same(A,target,4), ('congruence',n)
        assert same(mpow(T,4*n,8),I,8), ('plateau',n)
        assert not same(mpow(T,4*n,16),I,16), ('sharp-16',n)
        tests+=3
        for s in range(1,11):tests+=trial(n,s)
    print('VERIFY_OK odd_cycle_lengths=12 moduli=1..10 checks=',tests)

if __name__=='__main__':run()
