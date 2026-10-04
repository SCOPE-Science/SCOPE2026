#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

# Gaussian rationals are pairs (real, imag) of Fractions.
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def conj(z): return (z[0],-z[1])
def scale(q,z): return (q*z[0],q*z[1])
def abs2(z): return z[0]*z[0]+z[1]*z[1]
ZERO=(Fraction(0),Fraction(0))
UNITS=[(Fraction(1),Fraction(0)),(Fraction(0),Fraction(1)),(Fraction(-1),Fraction(0)),(Fraction(0),Fraction(-1))]

def cycles(N,a):
    seen=set(); out=[]
    for s in range(N):
        if s in seen: continue
        C=[]; x=s
        while x not in seen:
            seen.add(x); C.append(x); x=(x+a)%N
        out.append(C)
    return out

def intensity_coeffs(f,N,a,x):
    # |f_x + f_{x+a} t^{-a}|^2 as a character polynomial in t.
    y=(x+a)%N
    d={}
    def put(k,z): d[k%N]=add(d.get(k%N,ZERO),z)
    put(0,(abs2(f[x])+abs2(f[y]),Fraction(0)))
    put(a,mul(f[x],conj(f[y])))
    put(-a,conj(mul(f[x],conj(f[y]))))
    return {k:v for k,v in d.items() if v!=ZERO}

def swap_cycle(f,C):
    A2=abs2(f[C[0]]); B2=abs2(f[C[1]])
    # Require rational positive square ratio with chosen constructions.
    # Our constructed alternating examples use integer magnitudes A,B.
    A=int(A2.numerator**0.5); B=int(B2.numerator**0.5)
    assert Fraction(A*A)==A2 and Fraction(B*B)==B2 and A>0 and B>0
    out=list(f)
    for k,x in enumerate(C):
        out[x]=scale(Fraction(B,A) if k%2==0 else Fraction(A,B),f[x])
    return out

def classify_modulus_fiber(m2):
    # m2 are squared magnitudes around one even cycle. Return admissible r^2 values.
    L=len(m2); assert L%2==0 and L>=4
    vals={Fraction(1)}
    cand=m2[1]/m2[0]
    ok=True
    for k in range(L):
        r2=cand if k%2==0 else 1/cand
        # Equality r_k^2 m_k + r_{k+1}^2 m_{k+1}=m_k+m_{k+1},
        # with r_{k+1}^2 reciprocal to r_k^2.
        if r2*m2[k] + (1/r2)*m2[(k+1)%L] != m2[k]+m2[(k+1)%L]:
            ok=False; break
    if ok and cand != 1: vals.add(cand)
    return vals

checks=0; swaps=0; generic=0
for N in range(4,121):
    for a in range(1,N):
        L=N//gcd(N,a)
        if L<4 or L%2: continue
        Cs=cycles(N,a)
        assert len(Cs)==gcd(N,a) and all(len(C)==L for C in Cs)
        assert (2*a)%N != 0
        # Verify the character polynomial has three distinct coefficients.
        f=[UNITS[(3*x+N+a)%4] for x in range(N)]
        for x in range(N):
            co=intensity_coeffs(f,N,a,x)
            assert set(co)=={0,a%N,(-a)%N}
            checks += 1

        # On each cycle construct a two-level alternating full-support signal,
        # swap the two levels, and verify every slice intensity polynomial exactly.
        f=[ZERO for _ in range(N)]
        for ci,C in enumerate(Cs):
            A=2+(ci%3); B=5+(ci%4)
            if A==B: B+=1
            for k,x in enumerate(C):
                mag=A if k%2==0 else B
                f[x]=scale(Fraction(mag),UNITS[(x+2*k+ci)%4])
        g=list(f)
        for C in Cs:
            g=swap_cycle(g,C)
        for x in range(N):
            assert intensity_coeffs(f,N,a,x)==intensity_coeffs(g,N,a,x)
            checks += 1
        swaps += len(Cs)

        # Exact modulus-fiber classification: alternating data admit exactly
        # r^2=1 and the level ratio; a one-site perturbation removes the swap.
        for ci,C in enumerate(Cs):
            A=Fraction((2+ci%3)**2); B=Fraction((5+ci%4)**2)
            m2=[A if k%2==0 else B for k in range(L)]
            vals=classify_modulus_fiber(m2)
            assert vals=={Fraction(1),B/A}
            checks += 1
            m2[2] += 1
            vals=classify_modulus_fiber(m2)
            assert vals=={Fraction(1)}
            checks += 1; generic += 1

print(f"N_MAX=120 checks={checks} swap_cycles={swaps} perturbed_cycles={generic}")
print("VERIFY_OK")
