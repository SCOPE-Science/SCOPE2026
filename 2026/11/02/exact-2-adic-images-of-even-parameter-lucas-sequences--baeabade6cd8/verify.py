#!/usr/bin/env python3
"""Finite checks of an algebraic theorem on even-parameter Lucas sequences."""

def observed(P, N):
    mod = 1 << N
    a, b = 0, 1
    seen_states = set()
    out = set()
    while (a, b) not in seen_states:
        seen_states.add((a, b))
        out.add(a)
        a, b = b, (P * b + a) % mod
    return out, len(seen_states)

def expected(P, N):
    mod = 1 << N
    h = (abs(P) & -abs(P)).bit_length() - 1
    ev = {(P * k) % mod for k in range(1 << max(0, N-h))}
    od = {(1 + P*P*k) % mod for k in range(1 << max(0, N-2*h))}
    return ev | od

def seq(P, upto):
    u=[0,1]
    for _ in range(upto-1):
        u.append(P*u[-1] + u[-2])
    return u

def v2(x):
    assert x != 0
    return (abs(x) & -abs(x)).bit_length()-1

def check():
    modular_checks = 0
    states = 0
    for P in (-32,-16,-12,-10,-8,-6,-4,-2,2,4,6,8,10,12,16,24,32,40):
        for N in range(1, 13):
            actual, period = observed(P, N)
            wanted = expected(P,N)
            assert actual == wanted, (P,N,len(actual),len(wanted))
            assert len(actual) == 2**max(0,N-v2(P)) + 2**max(0,N-2*v2(P))
            modular_checks+=1
            states+=period
    valuation_checks=0
    doubling_checks=0
    for P in (-12,-8,-4,-2,2,4,6,8,12):
        U=seq(P,2*130+1)
        u=P*P
        f=[U[2*m]//P for m in range(131)]
        g=[U[2*m+1] for m in range(130)]
        H=[(x-1)//u for x in g]
        assert all(U[2*m] == P*f[m] for m in range(130))
        assert all((x-1)%u==0 for x in g)
        for m in range(1, 91):
            for n in range(m):
                assert v2(f[m]-f[n]) == v2(m-n), (P,m,n,'f')
                valuation_checks += 1
        for x in range(1, 63):
            for y in range(x):
                assert v2(H[2*x]-H[2*y]) == v2(x-y),(P,x,y,'H')
                valuation_checks += 1
        for t in range(0,60):
            assert g[2*t] == g[t]*g[t]+u*f[t]*f[t]
            assert f[2*t] == f[t]*(f[t+1]-f[t-1] if t>=1 else 2)
            doubling_checks +=2
    print('VERIFY_OK', 'modular_image_cases',modular_checks,
          'total_modular_states',states,'isometry_pairs',valuation_checks,
          'doubling_identities',doubling_checks)

if __name__=='__main__':check()
