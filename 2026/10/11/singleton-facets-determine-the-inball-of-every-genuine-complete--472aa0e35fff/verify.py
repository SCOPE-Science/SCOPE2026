#!/usr/bin/env python3
from fractions import Fraction

checks=0
for p in range(2,36):
    for q in range(2,36):
        N=p+q
        M=(2**p-1)*(2**q-1)
        r2=Fraction(M*M,N*(N-1))

        facet_count=N+M-1
        assert facet_count==N+((2**p-1)*(2**q-1)-1)

        for a in range(1,p+1):
            for b in range(1,q+1):
                if a==p and b==q:
                    continue
                k=a+b
                z=(2**a-1)*(2**b-1)

                small=Fraction(z,k*(k-1))
                big=Fraction(M,N*(N-1))
                assert small<big,(p,q,a,b,small,big)

                slack=Fraction(k*M,N)-z
                norm2=Fraction(k*(N-k),N)
                d2=slack*slack/norm2
                assert d2>r2,(p,q,a,b,d2,r2)
                checks+=1

        mu=Fraction(M,N)
        singleton_d2=mu*mu*Fraction(N,N-1)
        assert singleton_d2==r2

print(f"VERIFY_OK complete-bipartite-graph-associahedron cases={checks} p,q=2..35")
