#!/usr/bin/env python3
import math


def A_closed(m,N,M):
    if m % 2:
        s=(m-1)//2
        return M-s+sum(math.sin((2*M+1)*r*math.pi/N)/math.sin(r*math.pi/N) for r in range(1,s+1))
    s=m//2
    return -s+sum(math.sin((2*M+1)*(2*r-1)*math.pi/(2*N))/math.sin((2*r-1)*math.pi/(2*N)) for r in range(1,s+1))


def lam_closed(m,N):
    v=(-1)**(m-1)*A_closed(m,N,N)
    for k in range(1,m):
        v += 2*(-1)**(k-1)*A_closed(m,N,(k*N)//m)
    return v/N


def lam_direct(m,N):
    total=float(m)
    for j in range(1,N):
        total += abs(math.sin(math.pi*m*j/N)/math.sin(math.pi*j/N))
    return total/N


def Q(m,x):
    if m%2:
        s=(m-1)//2
        return x+sum(math.sin(2*math.pi*r*x)/(math.pi*r) for r in range(1,s+1))
    s=m//2
    return sum(2*math.sin((2*r-1)*math.pi*x)/((2*r-1)*math.pi) for r in range(1,s+1))


def lam_cont(m):
    return sum((-1)**k*(Q(m,(k+1)/m)-Q(m,k/m)) for k in range(m))


def B2(x):
    return x*x-x+1/6


def second_order_coeff(m,N):
    return -m*math.pi*sum(B2(((N*k)%m)/m)/math.sin(math.pi*k/m) for k in range(1,m))


cases=0
max_exact_err=0.0
for N in range(2,161):
    for m in range(2,min(N,30)+1):
        a=lam_closed(m,N)
        b=lam_direct(m,N)
        err=abs(a-b)
        max_exact_err=max(max_exact_err,err)
        if err>2e-11:
            raise SystemExit(f'FAIL exact m={m} N={N} err={err}')
        cases+=1

# The m=4 residue coefficients recover the independently derived closed values.
s2=math.sqrt(2.0)
expected={0:-2*math.pi*(2*s2+1)/3,1:math.pi*(s2+2)/6,2:2*math.pi*(s2-1)/3,3:math.pi*(s2+2)/6}
for r,c in expected.items():
    got=second_order_coeff(4,400+r)
    if abs(got-c)>2e-13:
        raise SystemExit(f'FAIL m4 residue r={r} got={got} expected={c}')

# Numerical remainder check for the third-order law on every residue class through length ten.
max_scaled=0.0
asym_cases=0
for m in range(2,11):
    L=lam_cont(m)
    for r in range(m):
        N=4000+((r-4000)%m)
        approx=L+second_order_coeff(m,N)/(N*N)
        scaled=abs(lam_closed(m,N)-approx)*N**3
        max_scaled=max(max_scaled,scaled)
        if scaled>100.0:
            raise SystemExit(f'FAIL asym m={m} r={r} scaled={scaled}')
        asym_cases+=1

print(f'VERIFY_OK exact_cases={cases} max_exact_err={max_exact_err:.3e} asymptotic_residues={asym_cases} max_N3_remainder={max_scaled:.6f}')
