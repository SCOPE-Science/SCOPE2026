#!/usr/bin/env python3
"""Exact finite-lag regression for a Fibonacci cat-map correlation theorem.

Finite enumeration checks examples; the mathematical proof covers every integer lag.
"""

def fib(m):
    f=[0,1]
    for _ in range(m):f.append(f[-1]+f[-2])
    return f

def matmul(x,y):
    return ((x[0][0]*y[0][0]+x[0][1]*y[1][0], x[0][0]*y[0][1]+x[0][1]*y[1][1]),
            (x[1][0]*y[0][0]+x[1][1]*y[1][0], x[1][0]*y[0][1]+x[1][1]*y[1][1]))

def action(M,v):
    return (M[0][0]*v[0]+M[0][1]*v[1], M[1][0]*v[0]+M[1][1]*v[1])

def neg(v):return (-v[0],-v[1])

def norm(v):return max(abs(v[0]),abs(v[1]))

def main():
    a=((2,1),(1,1))
    power=((1,0),(0,1))
    f=fib(15)
    for n in range(1,13):
        power=matmul(power,a)
        v=(f[n],-f[n+1]);w=(f[n-1],-f[n]); c=f[n+1]
        assert v[0]*w[1]-v[1]*w[0]==(-1)**n
        assert action(power,v)==tuple((-1)**(n+1)*x for x in (f[n],f[n-1]))
        assert action(power,w)==tuple((-1)**n*x for x in (f[n+1],f[n]))
        assert norm(v)<=c and norm(action(power,v))<=c
        assert norm(w)<=c and norm(action(power,w))<=c
        if n<=9:
            found=set()
            for x in range(-c,c+1):
                for y in range(-c,c+1):
                    k=(x,y)
                    if k!=(0,0) and norm(action(power,k))<=c:
                        found.add(k)
            assert found=={v,neg(v),w,neg(w)},(n,found)
    print('PASS: exact matrix identities for lags 1..12; complete square-band minimizers for lags 1..9.')

if __name__=='__main__':main()
