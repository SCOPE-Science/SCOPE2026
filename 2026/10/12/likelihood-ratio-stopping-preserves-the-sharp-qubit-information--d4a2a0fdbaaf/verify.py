from fractions import Fraction


def solve(A, b):
    n = len(b)
    A = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if A[i][col] != 0)
        A[col], A[pivot] = A[pivot], A[col]
        z = A[col][col]
        A[col] = [v / z for v in A[col]]
        for i in range(n):
            if i == col:
                continue
            z = A[i][col]
            if z:
                A[i] = [a - z*c for a, c in zip(A[i], A[col])]
    return [A[i][-1] for i in range(n)]


def recurrence(p, m, kind, sqrt_pq=None):
    q = 1 - p
    states = list(range(-m + 1, m))
    pos = {s:i for i,s in enumerate(states)}
    n = len(states)
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    b = [Fraction(0) for _ in range(n)]
    for s in states:
        i = pos[s]
        A[i][i] = Fraction(1)
        if kind == 'hit_lower':
            # h_s = q h_{s+1} + p h_{s-1}; h_{-m}=1, h_m=0
            for ns, w in ((s+1, q), (s-1, p)):
                if ns == -m:
                    b[i] += w
                elif ns == m:
                    pass
                else:
                    A[i][pos[ns]] -= w
        elif kind == 'time':
            # e_s = 1 + q e_{s+1} + p e_{s-1}; e_{+-m}=0
            b[i] = Fraction(1)
            for ns, w in ((s+1, q), (s-1, p)):
                if -m < ns < m:
                    A[i][pos[ns]] -= w
        elif kind == 'coherence':
            # f_s = sqrt(pq)(f_{s+1}+f_{s-1}); f_{+-m}=1
            w = sqrt_pq
            for ns in (s+1, s-1):
                if abs(ns) == m:
                    b[i] += w
                else:
                    A[i][pos[ns]] -= w
        else:
            raise ValueError(kind)
    return solve(A,b)[pos[0]]


def main():
    cases = [
        (Fraction(1,10), Fraction(3,10)),
        (Fraction(1,5), Fraction(2,5)),
        (Fraction(9,25), Fraction(12,25)),
    ]
    checks = 0
    for p, s in cases:
        q = 1-p
        assert s*s == p*q
        for m in range(1,8):
            pm = p**m / (p**m + q**m)
            h = recurrence(p,m,'hit_lower')
            assert h == pm
            checks += 1

            et = recurrence(p,m,'time')
            et_formula = Fraction(m,1) * (q**m-p**m) / ((q-p)*(q**m+p**m))
            assert et == et_formula
            checks += 1

            coh = recurrence(p,m,'coherence',s)
            coh_formula = 2*(s**m)/(p**m+q**m)
            assert coh == coh_formula
            # Frontier identity: coherence multiplier / 2 = sqrt(pm(1-pm)).
            assert (coh*coh)/4 == pm*(1-pm)
            # Maximal disturbance of the dephasing channel.
            disturbance = (1-coh)/2
            assert disturbance + coh/2 == Fraction(1,2)
            checks += 2

    print('VERIFY_OK')
    print('exact_rational_checks =', checks)
    print('parameter_threshold_cases =', len(cases)*7)


if __name__ == '__main__':
    main()
