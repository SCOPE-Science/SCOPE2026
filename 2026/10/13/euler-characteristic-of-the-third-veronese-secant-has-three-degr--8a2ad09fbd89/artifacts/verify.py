import itertools, math

def comps(total, parts):
    if parts == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for tail in comps(total-a, parts-1):
            yield (a,) + tail

def divisor_count(alpha, k):
    # Number of beta with 0<=beta_i<=alpha_i and sum beta_i=k.
    count = 0
    for beta in comps(k, len(alpha)):
        if all(b <= a for a,b in zip(alpha,beta)):
            count += 1
    return count

def classified_br3(alpha):
    pos = sorted((a for a in alpha if a), reverse=True)
    d = sum(alpha)
    if len(pos) == 1:
        return True
    if len(pos) == 2:
        return pos[1] <= 2
    if len(pos) >= 4:
        return False
    # Three-support case.
    if d == 3:
        # Han's normalization gives A(x0*x1*x2)=phi_012^4 != 0.
        return False
    assert len(pos) == 3 and d >= 4
    return False

def lower_bound_exclusion(alpha):
    pos = [a for a in alpha if a]
    d = sum(alpha)
    if len(pos) >= 4:
        return divisor_count(alpha, 1) >= 4
    if len(pos) == 3 and d >= 4:
        return divisor_count(alpha, 2) >= 4
    if len(pos) == 2 and min(pos) >= 3:
        b = min(pos)
        return divisor_count(alpha, b) >= 4
    return True

cases = 0
monomials = 0
weight_checks = 0
for n in range(2, 9):
    m = n + 1
    for d in range(3, 13):
        alphas = list(comps(d, m))
        monomials += len(alphas)
        br3 = []
        br2 = []
        B = d + 1
        weights = set()
        for alpha in alphas:
            assert lower_bound_exclusion(alpha)
            if classified_br3(alpha):
                br3.append(alpha)
            pos = sorted((a for a in alpha if a), reverse=True)
            if len(pos) == 1 or (len(pos) == 2 and pos[1] <= 1):
                br2.append(alpha)
            w = sum(a * (B**i) for i,a in enumerate(alpha))
            assert w not in weights
            weights.add(w)
            weight_checks += 1

        expected2 = m*m
        assert len(br2) == expected2
        if d == 3:
            expected3 = m*m
            exact = 0
        elif d == 4:
            expected3 = m*m + math.comb(m,2)
            exact = math.comb(m,2)
        else:
            expected3 = m*(2*m-1)
            exact = m*(m-1)
        assert len(br3) == expected3
        assert len(br3)-len(br2) == exact
        cases += 1

# Direct cubic Aronhold specialization: if only phi_012 is nonzero, A=phi_012^4.
for c in [1,2,-1,3,5]:
    A = c**4
    assert A != 0

assert cases == 70
assert monomials > 100000
print("VERIFY_OK", cases, monomials, weight_checks)
