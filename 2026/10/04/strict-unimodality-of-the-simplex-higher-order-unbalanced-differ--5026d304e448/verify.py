from math import comb, sqrt, exp


def deltas(n):
    a = [comb(n,j) for j in range(n+1)] + [0]
    return [a[j+1]-a[j] for j in range(n+1)]


def q_coeffs(n,p):
    m=n*p
    ds=deltas(n)
    return [ds[j]*(comb(m-1,j) if j <= m-1 else 0) for j in range(n+1)]


def sign_changes(xs):
    s=[]
    for x in xs:
        if x>0:s.append(1)
        elif x<0:s.append(-1)
    return sum(s[i]!=s[i-1] for i in range(1,len(s)))

# Exact integer sanity checks for representative dimensions/orders.
for n in range(2,15):
    ds=deltas(n)
    assert sign_changes(ds)==1
    for p in range(1,10):
        qc=q_coeffs(n,p)
        assert sign_changes(qc)==1
        assert qc[0]==n-1
        # Last nonzero coefficient is negative.
        assert [c for c in qc if c][-1] < 0

# Planar formula: derivative-in-x coefficients are exactly
# 1, -(2p-1), -(2p-1)(p-1).
for p in range(1,20):
    assert q_coeffs(2,p) == [1, -(2*p-1), -(2*p-1)*(p-1)]
    disc=(2*p-1)*(6*p-5)
    t=2.0/(2*p+1+sqrt(disc))
    x=t/(1-t)
    q=1-(2*p-1)*x-(2*p-1)*(p-1)*x*x
    assert abs(q) < 1e-12
    F=(1-t)**(2*p)+4*p*t*(1-t)**(2*p-1)+p*(2*p-1)*t*t*(1-t)**(2*p-2)
    M=(2+(2*p-3)*t)*(1-t)**(2*p-2)
    assert abs(F-M) < 1e-12

# Asymptotic numerical sanity check (the proof uses direct limits).
p=10**6
t=2.0/(2*p+1+sqrt((2*p-1)*(6*p-5)))
assert abs(p*t-(sqrt(3)-1)/2) < 2e-6
M=(2+(2*p-3)*t)*(1-t)**(2*p-2)
L=(1+sqrt(3))*exp(1-sqrt(3))
assert abs(M-L) < 2e-6

print('VERIFY_OK')
