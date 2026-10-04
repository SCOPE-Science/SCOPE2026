from math import sqrt

def cubic(s):
    return s**3 - 2*s**2 - 4*s + 4

def threshold():
    lo, hi = 0.0, 1.0
    for _ in range(120):
        mid = (lo + hi)/2
        if cubic(mid) > 0:
            lo = mid
        else:
            hi = mid
    s0 = (lo + hi)/2
    h0 = sqrt(1-s0*s0)
    return s0, h0

S0, H0 = threshold()

def source_formula(d,h):
    s=sqrt(max(0.0,1-h*h))
    return max(1/(1-d+s), sqrt(d*d+h*h), 1-d)

def profile(h):
    s=sqrt(max(0.0,1-h*h))
    if s >= S0:
        F=(sqrt(5-h*h)-s)/2
        d=1-F
    else:
        F=(1+h*h)/2
        d=(1-h*h)/2
    return F,d

assert abs(S0-0.8060634335253696) < 2e-15
assert abs(H0-0.5918291486005840) < 2e-15

# Check branch equality and dominance at the claimed unique optimizer.
for j in range(1,1000):
    h=j/1000
    F,d=profile(h)
    s=sqrt(1-h*h)
    assert 0 <= d <= s + 2e-15
    A=1/(1-d+s)
    B=sqrt(d*d+h*h)
    C=1-d
    assert abs(max(A,B,C)-F) < 3e-13
    if h < H0-1e-10:
        assert abs(A-C) < 3e-13 and B <= C+3e-13
    elif h > H0+1e-10:
        assert abs(B-C) < 3e-13 and A <= C+3e-13

# At the phase transition all three mechanisms agree.
F0,d0=profile(H0)
s0=sqrt(1-H0*H0)
A0=1/(1-d0+s0); B0=sqrt(d0*d0+H0*H0); C0=1-d0
assert max(abs(A0-B0),abs(B0-C0),abs(C0-A0)) < 3e-14

# Exhaustive fine grids at representative heights verify the optimizer against
# the published three-term formula; this is a finite consistency check only.
for h in (0.03,0.10,0.25,0.45,H0,0.65,0.80,0.95,1.0):
    F,dstar=profile(h)
    s=sqrt(max(0.0,1-h*h))
    N=100000
    best=10.0
    for k in range(N+1):
        d=s*k/N if N else 0.0
        best=min(best,source_formula(d,h))
    # Grid error is first order in mesh because the objective has a cusp.
    assert best >= F-2e-12
    assert best-F < 3e-5

# Strict increase of the exact profile.
vals=[profile(j/10000)[0] for j in range(1,10001)]
assert all(vals[i+1] > vals[i] for i in range(len(vals)-1))

# Sharp quadratic coefficient at the degenerate golden-ratio limit.
phi=(1+sqrt(5))/2
c=(5-sqrt(5))/20
for h in (1e-2,5e-3,2e-3):
    F,_=profile(h)
    ratio=(F-1/phi)/(h*h)
    assert abs(ratio-c) < 2e-5

print("VERIFY_OK parallelogram folding height profile")
