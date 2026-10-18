#!/usr/bin/env python3
"""Independent finite checks for Fibonacci recurrence orbit spectra.
All arithmetic is exact; the accompanying proof establishes the infinite result.
"""
from collections import Counter

def orbit_spectrum(modulus):
    visited = bytearray(modulus * modulus)
    counts = Counter()
    for a in range(modulus):
        for b in range(modulus):
            idx = a*modulus+b
            if visited[idx]:
                continue
            u,v = a,b
            length=0
            while not visited[u*modulus+v]:
                visited[u*modulus+v]=1
                length+=1
                u,v = v,(u+v)%modulus
            assert (u,v)==(a,b), 'Bijectivity failed'
            counts[length]+=1
    assert sum(l*c for l,c in counts.items()) == modulus*modulus
    return counts

def predicted(k):
    assert k>=3
    c=Counter({1:1,3:1,6:2,8:1,12:4})
    if k==3:
        c[24]=21
    else:
        c[24]=93
        for j in range(5,k+1):
            c[3*(1<<(j-1))]=9*(1<<(j-1))
    return c

def main():
    for k in range(3,8):
        m=3*(1<<k)
        got=orbit_spectrum(m)
        want=predicted(k)
        assert got==want,(k,got,want)
        assert sum(got.values())==9*(1<<k)-42
        print(f'k={k} modulus={m} cycles={sum(got.values())} spectrum={dict(sorted(got.items()))}')
    # Independently enumerate the two prime-power strata used in the proof.
    for k in range(1,8):
        modulus=1<<k
        got=orbit_spectrum(modulus)
        want=Counter({1:1})
        for j in range(1,k+1):
            length={1:3,2:6}.get(j,3*(1<<(j-1)))
            want[length]+=1<<(j-1)
        assert got==want,(k,got,want)
        assert sum(got.values())==modulus
    assert orbit_spectrum(3)==Counter({1:1,8:1})
    # The 2-adic matrix-lifting base is exact.
    A3=((1,2),(2,3))
    A6=((5,8),(8,13))
    A12=((89,144),(144,233))
    for base,denom in ((A3,2),(A6,4),(A12,8)):
        B=[[(base[i][j]-(1 if i==j else 0))//denom for j in range(2)] for i in range(2)]
        assert all((base[i][j]-(1 if i==j else 0))%denom==0 for i in range(2) for j in range(2))
        assert (B[0][0]*B[1][1]-B[0][1]*B[1][0])%2==1
    print('VERIFY_OK')

if __name__=='__main__':
    main()
