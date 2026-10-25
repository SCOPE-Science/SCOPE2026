"""Exact rational test vectors for the capped weighted-network witness.
The infinite-size theorem is established algebraically in RESULT.md.
"""
from fractions import Fraction as F


def validate(k):
    assert isinstance(k, int) and k >= 4
    alpha = F(1) - F(1, 8*k)
    e = F(1, 200*k**3)
    eps = 2*e
    denominator = 1-alpha**2-F(k,2)*e**2
    numerator = alpha+alpha**2+e*(1+F(k,2))+F(k,2)*e**2
    c0 = numerator/denominator
    c1 = alpha*(1+c0)
    cb = F(k,2)*(1+e*(1+c0))
    cl = e*(1+c0)
    assert denominator > F(1,8*k)
    assert 0 < numerator < 3
    assert c0 < 24*k
    assert cb < k
    assert cl < 1
    assert c0 >= 8*k-1 and c1 >= 8*k-1
    assert c0 == alpha*(1+c1)+e*(1+cb)
    assert c1 == alpha*(1+c0)
    assert cb == F(k,2)*(1+cl)
    assert cl == e*(1+c0)
    assert 1-alpha**2-F(k,2)*e**2 > 0
    # Exact iteration verifies convergence of clipped discounted influence
    # from below, but only the symbolic bounds certify all times.
    def score(seed, T=48):
        x = [F(0)]*(k+3)
        x[seed] = F(1)
        W = [[] for _ in x]
        w = F(2)-F(1,4*k)
        W[0] = [(1,w),(2,eps)]
        W[1] = [(0,w)]
        W[2] = [(3+j,F(1)) for j in range(k)]
        for j in range(k):
            W[3+j] = [(0,eps)]
        total=F(0)
        for t in range(1,T+1):
            y = [F(0)]*len(x)
            for i, rows in enumerate(W):
                for j, weight in rows:
                    y[j] += weight*x[i]
            x = [min(F(1), z) for z in y]
            total += F(1,2**t)*sum(x)
        return total
    score_a0=score(0)
    score_a1=score(1)
    score_b=score(2)
    assert score_a0 <= 2+(k+1)*eps
    assert score_a1 <= 2+(k+1)*eps
    assert score_b >= F(k,2)
    bound=F(4,k)+F(k+1, 50*k**4)
    assert max(score_a0, score_a1)/score_b <= bound
    return (k, round(float(c0),5),round(float(c1),5),round(float(cb),5),
            round(float(score_a0),5),round(float(score_b),5),round(float(bound),5))


if __name__ == "__main__":
    for k in (4, 8, 16, 32):
        print(validate(k))
    print("Exact finite-instance checks passed; asymptotic claim follows the proof.")
