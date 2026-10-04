from fractions import Fraction
from math import comb

def transition(M):
    P = [[Fraction(0) for _ in range(M+1)] for _ in range(M+1)]
    for k in range(M+1):
        if k > 0:
            P[k][k-1] = Fraction(k, M)
        if k < M:
            P[k][k+1] = Fraction(M-k, M)
    return P

def mul(v, P):
    return [sum(v[i]*P[i][j] for i in range(len(v))) for j in range(len(v))]

for M in range(1, 11):
    P = transition(M)
    pi = [Fraction(comb(M,k), 2**M) for k in range(M+1)]
    assert sum(pi) == 1
    assert mul(pi, P) == pi

    for k in range(M):
        assert pi[k]*Fraction(M-k,M) == pi[k+1]*Fraction(k+1,M)

    mean = sum(pi[k]*Fraction(2*k-M,2) for k in range(M+1))
    second = sum(pi[k]*Fraction((2*k-M)**2,4) for k in range(M+1))
    assert mean == 0
    assert second == Fraction(M,4)

    for k in range(M+1):
        y = Fraction(2*k-M,2)
        e1 = Fraction(0)
        e2 = Fraction(0)
        if k > 0:
            p = Fraction(k,M)
            e1 += p*(y-1)
            e2 += p*(y-1)**2
        if k < M:
            p = Fraction(M-k,M)
            e1 += p*(y+1)
            e2 += p*(y+1)**2
        assert e1 == (1-Fraction(2,M))*y
        assert e2 == (1-Fraction(4,M))*y*y + 1

# Exact M=2 second-moment oscillation from the central state.
M = 2
P = transition(M)
v = [Fraction(0), Fraction(1), Fraction(0)]
seconds = []
for _ in range(6):
    seconds.append(sum(v[k]*Fraction((2*k-M)**2,4) for k in range(M+1)))
    v = mul(v, P)
assert seconds == [0,1,0,1,0,1]

# Parity-conditioned convergence: after many two-step iterations, representative
# chains approach twice the invariant mass on the reachable parity class.
for M in (3,4,5,7):
    P = transition(M)
    pi = [Fraction(comb(M,k), 2**M) for k in range(M+1)]
    v = [Fraction(0) for _ in range(M+1)]
    v[0] = 1
    for _ in range(120):
        v = mul(mul(v,P),P)
    target = [2*pi[k] if k % 2 == 0 else Fraction(0) for k in range(M+1)]
    assert max(abs(float(v[k]-target[k])) for k in range(M+1)) < 1e-10

print("verification passed")
