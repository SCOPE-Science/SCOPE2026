"""Finite regression checks for the divisor-sum GCD density theorem.

The proof of the density limit uses CRT and prime harmonic divergence,
not these finite computations.
"""
from math import gcd

N=1_000_000
spf=list(range(N+1))
for p in range(2,int(N**.5)+1):
    if spf[p]==p:
        for j in range(p*p,N+1,p):
            if spf[j]==j: spf[j]=p

def sigma_of_square(n):
    t=n
    result=1
    while t>1:
        p=spf[t]
        e=0
        while t%p==0:
            e+=1
            t//=p
        result *= (pow(p,2*e+1)-1)//(p-1)
    return result

checkpoints={10:10,100:99,1000:974,10000:9561,100000:93845,1000000:923464}
count=0
for m in range(1,N+1):
    s=sigma_of_square(m)
    good=gcd(m,s)==gcd(m*m,s)
    count += good
    if m in checkpoints:
        assert count==checkpoints[m],(m,count,checkpoints[m])
for p,u,v in [(7,2,11),(13,3,61)]:
    assert (u*u+u+1)%p==0
    assert (v*v+v+1)%p==0
    m=p*u*v
    assert m%(p*p)!=0
    assert gcd(m,sigma_of_square(m))!=gcd(m*m,sigma_of_square(m))
    assert sigma_of_square(m)%(p*p)==0
# Finite CRT identity: for each modulus q^2, exactly q-1 residues satisfy q||n.
for q in (2,3,5,7,11,13,17,19,31):
    residues=sum(1 for a in range(q*q) if a%q==0 and a%(q*q)!=0)
    assert residues==q-1
print('VERIFIED: 1,000,000 GCD classifications; 6 published checkpoints; 2 local witnesses; 9 CRT residue counts.')
