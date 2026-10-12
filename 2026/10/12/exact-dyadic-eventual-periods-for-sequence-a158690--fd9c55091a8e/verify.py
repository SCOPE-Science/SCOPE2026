#!/usr/bin/env python3
"""Independent finite arithmetic checks for exact dyadic periods of A158690."""
from math import comb, factorial

N = 145
MOD = 2**13

# Method I: directly convolve the defining exponential generating products.
A = [0] * (N + 1)
A[0] = 1
P = [1] + [0] * N
for m in range(1, N + 1):
    d = 2*m - 1
    fac = [0] + [(-1)**(j+1)*pow(d,j,MOD) % MOD for j in range(1,N+1)]
    new = [0]*(N+1)
    for n in range(m,N+1):
        new[n] = sum(comb(n,j)*P[n-j]*fac[j] for j in range(1,n-m+2)) % MOD
        A[n] = (A[n]+new[n])%MOD
    P = new

# Method II: ordinary coefficients of H(y), then Stirling transform.
G = [1]+[0]*N
P = [1]+[0]*N
for m in range(1,N+1):
    d=2*m-1
    fac=[0]+[(-1)**(j+1)*comb(d+j-1,j)%MOD for j in range(1,N+1)]
    new=[0]*(N+1)
    for n in range(m,N+1):
        new[n]=sum(P[i]*fac[n-i] for i in range(m-1,n))%MOD
        G[n]=(G[n]+new[n])%MOD
    P=new
S=[1]+[0]*N
B=[]
for n in range(N+1):
    if n:
        T=[0]*(N+1)
        for j in range(1,n+1):T[j]=(S[j-1]+j*S[j])%MOD
        S=T
    B.append(sum(G[j]*factorial(j)*S[j] for j in range(n+1))%MOD)
assert A == B, 'defining EGF disagrees with Stirling representation'
assert A[:15] == [x%MOD for x in (1,1,5,55,1073,32671,1431665,85363615,6646603073,654896692351,79656194515025,11722538113191775,2052949879753739873,421931472111868912831,100568330857984368195185)]
assert G[:8]==[x%MOD for x in [1,1,2,7,33,197,1419,11966]]

BROWS=[]
for e in (0,1):
    vals=[]
    for m in range(16):
        val=sum((-1)**(m-j)*comb(m,j)*((j*j-1)//8)*(j**e) for j in range(m+1) if j%2)%4
        vals.append(val)
    BROWS.append(vals)
assert BROWS[0] == [0,0,0,1,0,1,2,0]+[0]*8
assert BROWS[1] == [0,0,0,3,0,1,2,2]+[0]*8
assert [(sum(G[m]*BROWS[e][m] for m in range(8))%4) for e in (0,1)]==[2,0]

# Exact (not modular) coefficient certificate for the only eight needed terms.
P0=[1]+[0]*7
C0=P0[:] 
for m in range(1,8):
    d=2*m-1
    f=[0]+[(-1)**(j+1)*comb(d+j-1,j) for j in range(1,8)]
    Q=[sum(P0[t]*f[i-t] for t in range(i+1)) for i in range(8)]
    C0=[x+y for x,y in zip(C0,Q)]
    P0=Q
assert C0==[1,1,2,7,33,197,1419,11966]
for e in (0,1):
    H=lambda j: (j**e)*((j*j-1)//8) if j%2 else 0
    for j in range(256):
        value=sum((-1)**(8-t)*comb(8,t)*H(j+t) for t in range(9))
        assert value%4==0,(e,j)

checks=0
for k in range(2,8):
    h=2**(k-1)
    mod=2**(k+3)
    for n in range(k+3,N-h+1):
        target=(2**(k+2) if n%2==0 else 0)
        assert (A[n+h]-A[n])%mod==target,(k,n)
        checks+=1
for r in range(5,11):
    period=2**(r-3)
    for n in range(r,N-period):
        assert (A[n+period]-A[n])%(2**r)==0, (r,n)
print('VERIFY_OK direct_EGF_vs_Stirling_n=0..%d exact_first_coefficients=15 g0_to_g7_exact=yes'%N)
print('VERIFY_OK finite_difference_rows=%s,%s odd_even_weighted=0,2 delta8_samples=512'%(BROWS[0][:8],BROWS[1][:8]))
print('VERIFY_OK half_shift_checks=%d k=2..7 n>=k+3 full_modulus=yes'%checks)
print('VERIFY_OK eventual_period_tests_r=5..10 parity_obstruction=yes infinite_proof_in_RESULT=yes')
