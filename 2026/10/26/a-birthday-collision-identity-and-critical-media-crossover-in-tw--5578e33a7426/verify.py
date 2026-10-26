"""Independent finite-chain and asymptotic checks for the two-panel media voter rule.

Only Python's standard library is needed. The exact proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations
from math import sqrt, exp, erf, pi, fsum


def transitions(N, k, p):
    """Direct combinatorial probabilities from the microscopic update rule."""
    assert N >= 3 and 0 <= k <= N and 0 <= p <= 1
    if k == 0 or k == N:
        return Fraction(0), Fraction(0)
    den = N * (N - 1) * (N - 2)
    up = Fraction((N-k) * (k*(k-1) + 2*p*k*(N-k-1)), den)
    down = Fraction(k * (N-k)*(N-k-1), den)
    return up, down


def enumerate_transitions(N, k, p):
    """Enumerate all ordered voter, panel-member triples, without replacement."""
    labels = [1] * k + [0] * (N-k)
    up = down = Fraction(0)
    triples = N*(N-1)*(N-2)
    for voter in range(N):
        for i in range(N):
            if i == voter:
                continue
            for j in range(N):
                if j == voter or j == i:
                    continue
                panel = (labels[i], labels[j])
                before = labels[voter]
                if panel[0] == panel[1]:
                    after_one = Fraction(panel[0])
                else:
                    after_one = (Fraction(p) if before == 0 else Fraction(1))
                if before == 0:
                    up += after_one / triples
                else:
                    down += (1-after_one) / triples
    return up, down


def fixation_weights_exact(N, p):
    """Closed birth-death increment weights from the theorem."""
    p = Fraction(p)
    weights = [Fraction(1)]
    for j in range(1, N-1):
        numerator = N-j-1
        denominator = j-1 + 2*p*(N-j-1)
        weights.append(weights[-1] * Fraction(numerator, 1) / denominator)
    return weights


def solve_gauss(matrix, rhs):
    """Independent exact rational solution of the absorbing-chain linear equations."""
    n = len(rhs)
    A = [[Fraction(x) for x in row] + [Fraction(rhs[i])] for i,row in enumerate(matrix)]
    for c in range(n):
        r = next(r for r in range(c,n) if A[r][c])
        A[c],A[r] = A[r],A[c]
        pivot=A[c][c]
        A[c] = [x/pivot for x in A[c]]
        for r in range(n):
            if r != c and A[r][c]:
                fac=A[r][c]
                A[r] = [A[r][i]-fac*A[c][i] for i in range(n+1)]
    return [row[n] for row in A]


def fixation_exact(N, p):
    w=fixation_weights_exact(N,p)
    denominator=sum(w)
    return [Fraction(0)] + [sum(w[:k])/denominator for k in range(1,N)] + [Fraction(1)]


def numerical_fixation(N, p, k):
    """Log-normalized weights: stable when N is large."""
    logs=[0.0]
    for i in range(1,N-1):
        a=N-i-1
        b=i-1+2*p*a
        logs.append(logs[-1] + __import__('math').log(a/b))
    mx=max(logs)
    den=fsum(exp(z-mx) for z in logs)
    num=fsum(exp(z-mx) for z in logs[:k])
    return num/den


def crossover(lam, x):
    # Integrals of exp(-t*t/2 - 2*lam*t).
    from math import erfc
    return 1-erfc((x+2*lam)/sqrt(2))/erfc(sqrt(2)*lam)


def one_seed_scale(lam):
    from math import erfc
    I=exp(2*lam*lam)*sqrt(pi/2)*erfc(sqrt(2)*lam)
    return 1/I


def main():
    count=0
    for N in range(3,10):
        for p in [Fraction(1,4),Fraction(1,2),Fraction(2,3),Fraction(3,4)]:
            for k in range(1,N):
                assert transitions(N,k,p) == enumerate_transitions(N,k,p)
                count+=1
            # Cross-check exact finite fixation against an independently solved linear system.
            A=[]; b=[]
            for k in range(1,N):
                a,down=enumerate_transitions(N,k,p)
                row=[Fraction(0)]*(N-1)
                row[k-1]=a+down
                if k>1: row[k-2]=-down
                if k<N-1: row[k]=-a
                A.append(row); b.append(a if k==N-1 else Fraction(0))
            sol=solve_gauss(A,b)
            vals=fixation_exact(N,p)
            assert sol==vals[1:N]
            count += N-1
            if p==Fraction(1,2):
                # Exact birthday law, M=N-2 birthdays.
                M=N-2
                w=[Fraction(1)]
                for j in range(1,M+1): w.append(w[-1]*Fraction(M-j+1,M))
                assert w==fixation_weights_exact(N,p)
                count += 1
    # Explicit critical illustrations.
    assert fixation_exact(4,Fraction(1,2)) == [Fraction(0),Fraction(2,5),Fraction(4,5),Fraction(1),Fraction(1)]
    count+=1
    # Check the moving media parameter and moving initial-seed Gaussian profiles.
    for N in (1000,4000,16000,64000):
        for lam in (-1.,0.,1.):
            p=.5+lam/sqrt(N)
            for x in (.5,1.,2.):
                k=int(x*sqrt(N))
                actual=numerical_fixation(N,p,k)
                target=crossover(lam,x)
                tol=0.085 if N==1000 else 0.055 if N==4000 else 0.028 if N==16000 else 0.015
                assert abs(actual-target)<tol,(N,lam,x,actual,target)
                count+=1
            scaled=sqrt(N)*numerical_fixation(N,p,1)
            target=one_seed_scale(lam)
            tol=.3 if N==1000 else .15 if N==4000 else .08 if N==16000 else .04
            assert abs(scaled-target)<tol,(N,lam,scaled,target)
            count+=1
    print(f'PASS {count} independent finite-chain and critical-window checks')
    print('Critical one-seed prefactor:',one_seed_scale(0.))
    for lam in (-1.,0.,1.):
        print('lambda',lam,'F_lambda(1)',crossover(lam,1.),'one-seed coefficient',one_seed_scale(lam))

if __name__=='__main__':
    main()
