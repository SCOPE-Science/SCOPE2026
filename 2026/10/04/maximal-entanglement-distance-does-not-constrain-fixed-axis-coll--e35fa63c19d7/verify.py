#!/usr/bin/env python3
import cmath
import math

# Small dense linear-algebra helpers for pure states.
def kron(a, b):
    return [x*y for x in a for y in b]

def norm2(v):
    return sum((abs(x)**2 for x in v))

def qfi_jz(state, n):
    mean = 0.0
    mean2 = 0.0
    for idx, amp in enumerate(state):
        ones = idx.bit_count()
        eig = (n - 2*ones)/2.0
        p = abs(amp)**2
        mean += p*eig
        mean2 += p*eig*eig
    return 4.0*(mean2 - mean*mean)

def one_qubit_purity(state, n, q):
    rho00 = rho11 = 0.0
    rho01 = 0j
    mask = 1 << (n-1-q)
    for idx in range(1 << n):
        if idx & mask:
            continue
        j = idx | mask
        a, b = state[idx], state[j]
        rho00 += abs(a)**2
        rho11 += abs(b)**2
        rho01 += a*b.conjugate()
    return rho00*rho00 + rho11*rho11 + 2.0*abs(rho01)**2

def ed(state, n):
    return 2.0*sum(1.0-one_qubit_purity(state,n,q) for q in range(n))

def bell_rot(theta):
    c = math.cos(theta/2.0)
    s = math.sin(theta/2.0)
    # (I tensor R_y(theta)) |Phi+>, computational order 00,01,10,11.
    return [c/math.sqrt(2), s/math.sqrt(2), -s/math.sqrt(2), c/math.sqrt(2)]

def singlet():
    return [0j, 1/math.sqrt(2), -1/math.sqrt(2), 0j]

def ghz(n):
    v = [0j]*(1 << n)
    v[0] = 1/math.sqrt(2)
    v[-1] = 1/math.sqrt(2)
    return v

def tensor_power(v, k):
    out = [1+0j]
    for _ in range(k):
        out = kron(out, v)
    return out

for theta in [0.0, 0.37, math.pi/2, 2.2, math.pi]:
    v = bell_rot(theta)
    assert abs(norm2(v)-1.0) < 1e-12
    assert abs(ed(v,2)-2.0) < 1e-12
    got = qfi_jz(v,2)
    want = 2.0*(1.0+math.cos(theta))
    assert abs(got-want) < 1e-12, (theta, got, want)

for n in [2,4,6,8]:
    s = tensor_power(singlet(), n//2)
    g = ghz(n)
    assert abs(ed(s,n)-n) < 1e-11
    assert abs(qfi_jz(s,n)) < 1e-11
    assert abs(ed(g,n)-n) < 1e-11
    assert abs(qfi_jz(g,n)-n*n) < 1e-11

print('VERIFY_OK')
