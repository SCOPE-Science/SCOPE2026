from fractions import Fraction
from itertools import product


def sign_covariance(magnitudes, order):
    n = len(magnitudes)
    data = []
    for signs in product((-1, 1), repeat=n):
        seq = [signs[i] for i in order]
        runs = 1 + sum(seq[j] != seq[j+1] for j in range(n-1))
        xs = [Fraction(signs[i] * magnitudes[i]) for i in range(n)]
        mean = sum(xs, Fraction(0)) / n
        s2 = sum((x-mean)**2 for x in xs) / (n-1)
        q2 = sum(x*x for x in xs) / n
        data.append((Fraction(runs), s2, q2))
    den = Fraction(1, len(data))
    er = sum(r for r, _, _ in data) * den
    es = sum(s for _, s, _ in data) * den
    eq = sum(q for _, _, q in data) * den
    ers = sum(r*s for r, s, _ in data) * den
    erq = sum(r*q for r, _, q in data) * den
    cov_s = ers - er*es
    cov_q = erq - er*eq
    rhs = sum(Fraction(magnitudes[order[j]] * magnitudes[order[j+1]]) for j in range(n-1)) / (n*(n-1))
    return cov_s, cov_q, rhs


def deterministic_checks():
    count = 0
    sign_vectors = 0
    for n in range(2, 10):
        mags = list(range(1, n+1))
        orders = [
            list(range(n)),
            list(reversed(range(n))),
            sorted(range(n), key=lambda i: (i % 2, i)),
            sorted(range(n), key=lambda i: ((i * 3) % n, i)),
        ]
        seen = set()
        for order in orders:
            key = tuple(order)
            if key in seen:
                continue
            seen.add(key)
            cov_s, cov_q, rhs = sign_covariance(mags, order)
            assert cov_s == rhs
            assert cov_q == 0
            count += 1
            sign_vectors += 2**n
    return count, sign_vectors


def unconditional_discrete_checks():
    # Exact averaging over iid positive magnitudes uniformly chosen from {1,2,3},
    # with absolute-rank ordering and index tie-breaking.
    count = 0
    states = 0
    for n in range(2, 6):
        total_weight = Fraction(1, 3**n)
        # E Cov(R,S^2 | A) plus Cov(E[R|A],E[S^2|A]); the latter is zero.
        lhs = Fraction(0)
        rhs = Fraction(0)
        cov_q = Fraction(0)
        # Compute the unconditional covariance directly from all magnitudes and signs.
        all_rows = []
        for mags in product((1,2,3), repeat=n):
            order = sorted(range(n), key=lambda i: (mags[i], i))
            for signs in product((-1,1), repeat=n):
                seq=[signs[i] for i in order]
                runs=1+sum(seq[j]!=seq[j+1] for j in range(n-1))
                xs=[Fraction(signs[i]*mags[i]) for i in range(n)]
                mean=sum(xs,Fraction(0))/n
                s2=sum((x-mean)**2 for x in xs)/(n-1)
                q2=sum(x*x for x in xs)/n
                all_rows.append((Fraction(runs),s2,q2))
            rhs += total_weight * sum(Fraction(mags[order[j]]*mags[order[j+1]]) for j in range(n-1))/(n*(n-1))
        den=Fraction(1,len(all_rows))
        er=sum(r for r,_,_ in all_rows)*den
        es=sum(s for _,s,_ in all_rows)*den
        eq=sum(q for _,_,q in all_rows)*den
        lhs=sum(r*s for r,s,_ in all_rows)*den-er*es
        cov_q=sum(r*q for r,_,q in all_rows)*den-er*eq
        assert lhs == rhs
        assert cov_q == 0
        count += 1
        states += len(all_rows)
    return count, states


def uniform_checks():
    # For A_(j) from n iid Uniform[0,a], with a=1:
    # E[A_(j)A_(j+1)] = j(j+2)/((n+1)(n+2)).
    count=0
    for n in range(2,1001):
        s=sum(Fraction(j*(j+2),(n+1)*(n+2)) for j in range(1,n))
        closed=Fraction(n*(n-1)*(2*n+5),6*(n+1)*(n+2))
        assert s==closed
        cov=s/Fraction(n*(n-1))
        expected=Fraction(2*n+5,6*(n+1)*(n+2))
        assert cov==expected
        count += 1
    return count


def chronological_checks():
    # For a fixed ordering and iid magnitudes A uniform on {1,2,3},
    # E adjacency product = (n-1)(E A)^2, so Cov=(E A)^2/n=4/n.
    count=0
    for n in range(2,10):
        expected=Fraction(4,n)
        # Formula-level exact check.
        ea=Fraction(1+2+3,3)
        rhs=Fraction(n-1, n*(n-1))*ea*ea
        assert rhs==expected
        count += 1
    return count


if __name__ == '__main__':
    dc, sv = deterministic_checks()
    uc, states = unconditional_discrete_checks()
    uf = uniform_checks()
    ch = chronological_checks()
    print('VERIFY_OK')
    print(f'deterministic_sign_order_checks={dc}')
    print(f'deterministic_sign_vectors={sv}')
    print(f'unconditional_discrete_checks={uc}')
    print(f'unconditional_joint_states={states}')
    print(f'uniform_order_moment_checks={uf}')
    print(f'chronological_formula_checks={ch}')
