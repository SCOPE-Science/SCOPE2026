#!/usr/bin/env python3
import math


def laguerre(n, z):
    return sum(((-1)**k) * math.comb(n, k) * (z**k) / math.factorial(k) for k in range(n + 1))


def objective_ratio(n, t, z):
    p = ((-1)**n) * laguerre(n, z)
    return math.sqrt(math.factorial(n)) * (1.0 - t + t*p) / (2.0 * (z ** (n/2.0)) * math.sqrt(t))


def golden_min(n, t):
    A = math.factorial(n) ** (1.0/n)
    center = math.log(A * t ** (-1.0/n))
    a, b = center - 2.0, center + 2.0
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c = b - gr*(b-a)
    d = a + gr*(b-a)
    fc = objective_ratio(n,t,math.exp(c))
    fd = objective_ratio(n,t,math.exp(d))
    for _ in range(180):
        if fc < fd:
            b,d,fd = d,c,fc
            c = b - gr*(b-a)
            fc = objective_ratio(n,t,math.exp(c))
        else:
            a,c,fc = c,d,fd
            d = a + gr*(b-a)
            fd = objective_ratio(n,t,math.exp(d))
    x=(a+b)/2.0
    z=math.exp(x)
    return z, objective_ratio(n,t,z)


def pred(n,t):
    A = math.factorial(n)**(1.0/n)
    e=t**(1.0/n)
    r=1.0 - n*n/(2*A)*e + n*n*(n*n-2)/(8*A*A)*e*e
    z=A/e+(n-2)
    return z,r


def check_coeffs(n):
    # coefficients of P_n=(-1)^n L_n from the defining sum
    lead = 1.0/math.factorial(n)
    nextc = -n*n/math.factorial(n)
    third = n*n*(n-1)*(n-1)/(2.0*math.factorial(n))
    # direct combinatorial coefficients
    dlead = ((-1)**n)*((-1)**n)*math.comb(n,n)/math.factorial(n)
    dnext = ((-1)**n)*((-1)**(n-1))*math.comb(n,n-1)/math.factorial(n-1)
    dthird = ((-1)**n)*((-1)**(n-2))*math.comb(n,n-2)/math.factorial(n-2)
    assert abs(lead-dlead)<1e-15
    assert abs(nextc-dnext)<1e-15
    assert abs(third-dthird)<1e-15


def main():
    for n in (3,4,5,6):
        check_coeffs(n)
    cases=[(3,1e-9,5e-6,5e-3),(4,1e-12,2e-5,2e-2),(5,1e-15,3e-4,2e-1)]
    for n,t,tol_r,tol_z in cases:
        z,r=golden_min(n,t)
        zp,rp=pred(n,t)
        assert abs(r-rp) < tol_r, (n,t,r,rp)
        assert abs(z-zp) < tol_z, (n,t,z,zp)
        print(f"n={n} t={t:g} exact_ratio={r:.15g} predicted_ratio={rp:.15g} z={z:.15g} predicted_z={zp:.15g}")
    print('VERIFY_OK')

if __name__=='__main__':
    main()
