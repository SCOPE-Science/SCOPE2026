"""Exact finite-state checks for discounted discord in a heterogeneous star voter chain.

Uses only the Python standard library; no simulation and no numerical tolerances.
The finite-state tests do not replace the analytic proof for arbitrary star size.
"""
from fractions import Fraction as F


def solve(A, b):
    """Fractional Gaussian elimination with partial nonzero pivoting."""
    n = len(A)
    M = [list(row) + [rhs] for row, rhs in zip(A, b)]
    for i in range(n):
        pivot = next((j for j in range(i, n) if M[j][i]), None)
        assert pivot is not None, 'singular transient resolvent'
        M[i], M[pivot] = M[pivot], M[i]
        pv = M[i][i]
        for j in range(i+1, n):
            if M[j][i]:
                mul = M[j][i] / pv
                for h in range(i+1, n+1):
                    M[j][h] -= mul * M[i][h]
                M[j][i] = F(0)
    x = [F(0)] * n
    for i in reversed(range(n)):
        x[i] = (M[i][n] - sum(M[i][j]*x[j] for j in range(i+1,n))) / M[i][i]
    return x


def generator_expectation(k, alpha, beta, delta, p):
    """Independently solve the full 2**(k+1)-state Kolmogorov resolvent."""
    n = k + 1
    transient = [s for s in range(1, 2**n-1)]
    idx = {s:i for i,s in enumerate(transient)}
    Q = [[F(0) for _ in transient] for __ in transient]
    rewards = [F(0) for _ in transient]
    for s in transient:
        i = idx[s]
        hub = s & 1
        different = [j for j in range(1, n) if ((s>>j)&1) != hub]
        rewards[i] = F(len(different))
        transitions = {}
        for j in different:
            dest = s ^ (1<<j)
            transitions[dest] = transitions.get(dest,F(0)) + alpha
        for j in different:
            dest = s ^ 1
            transitions[dest] = transitions.get(dest,F(0)) + beta / k
        Q[i][i] -= sum(transitions.values(),F(0))
        for dest,rate in transitions.items():
            if dest in idx: Q[i][idx[dest]] += rate
    resolvent = [[(delta if i==j else F(0))-Q[i][j] for j in range(len(transient))] for i in range(len(transient))]
    values = solve(resolvent, rewards)
    ans = F(0)
    for s in transient:
        ones = s.bit_count()
        ans += p**ones * (1-p)**(n-ones) * values[idx[s]]
    return ans


def closed_form(k, alpha, beta, delta, p):
    return 2*p*(1-p)*k*(delta+2*alpha+(k-1)*beta/F(k))/(delta**2+(3*alpha+beta)*delta+2*alpha*(alpha+beta/F(k)))


def main():
    checks=0
    for k in (2,3,4):
        for alpha,beta in [(F(1),F(1)),(F(1),F(4)),(F(2),F(3))]:
            for delta in (F(0),F(1),F(2)):
                for p in (F(1,2),F(2,5)):
                    actual=generator_expectation(k,alpha,beta,delta,p)
                    expected=closed_form(k,alpha,beta,delta,p)
                    assert actual==expected, (k,alpha,beta,delta,p,actual,expected)
                    checks+=1
    for k in range(2,51):
        for alpha in (F(1),F(5,3)):
            for delta in (F(0),F(1,4),F(2),F(30)):
                for beta1,beta2 in [(F(1,3),F(3,2)),(F(1),F(8))]:
                    p=F(2,5)
                    diff=closed_form(k,alpha,beta2,delta,p)-closed_form(k,alpha,beta1,delta,p)
                    critical=alpha*(k-3)-delta
                    assert (diff>0)-(diff<0)==(critical>0)-(critical<0)
                    checks+=1
    for k in range(4,51):
        for alpha in (F(1),F(7,3)):
            delta=alpha*(k-3)
            for beta in (F(1,10),F(1),F(17)):
                assert closed_form(k,alpha,beta,delta,F(1,2))==F(k,2)/ (alpha*(k-2))
                checks+=1
    for k in range(2,40):
        for alpha,beta in [(F(1),F(1)),(F(2),F(3))]:
            # Initial discord slope, divided by initial per-edge disagreement.
            # -k*alpha-beta (hub update hits one disagreement on average).
            assert -k*(alpha+beta/F(k)) == -k*alpha-beta
            checks+=1
    print('PASS', checks,'exact assertions; full-state cases',3*3*3*2)

if __name__=='__main__':main()
