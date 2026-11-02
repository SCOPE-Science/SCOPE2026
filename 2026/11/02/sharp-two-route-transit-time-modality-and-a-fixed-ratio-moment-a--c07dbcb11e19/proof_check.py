"""Reproducible exact and numerical checks for the two-route transit-time theorem.

The proof is analytical. These checks test algebraic identities and samples;
finite sampling is not a proof of universal modality classification.
"""
from fractions import Fraction as F
from math import exp, factorial, sqrt


def moments(weight, a, b, k):
    return (weight / a + (1 - weight) * k / b,
            2 * weight / (a * a) + (1 - weight) * k * (k + 1) / (b * b))


def phi(k, R, s):
    return s ** (k - 2) * (k - 1 - s) * exp((R - 1) * s)


def critical(k, R):
    if k == 2:
        if R <= 2:
            return 1 / (1 + R * R), 0.0
        star = (R - 2) / (R - 1)
    else:
        lo, hi = 0.0, float(k - 1)
        for _ in range(80):
            mid = (lo + hi) / 2
            score = (k - 2) / mid - 1 / (k - 1 - mid) + (R - 1)
            if score > 0: lo = mid
            else: hi = mid
        star = (lo + hi) / 2
    H = phi(k, R, star)
    return H / (H + factorial(k - 1) * R * R), star


def predicted_modes(k, R, w):
    if k == 1: return (1, 'boundary')
    threshold, star = critical(k, R)
    if k == 2:
        zero_threshold = 1 / (1 + R * R)
        if R > 2 and zero_threshold < w < threshold:
            return (2, 'boundary_and_interior')
        if w < zero_threshold or (R > 2 and w == zero_threshold):
            return (1, 'interior')
        return (1, 'boundary')
    return (2, 'boundary_and_interior') if w < threshold else (1, 'boundary')


def derivative_sign_scaled(k, R, w, s):
    # Sign of f'(t)/[b^2 exp(-at)] with s=bt.
    if k == 1:
        return -w * R * R - (1-w) * exp((R - 1) * s)
    return -w * R * R + ((1-w) / factorial(k-1)) * s**(k-2) * (k-1-s) * exp((R-1)*s)


def count_pos_to_neg_crossings(k, R, w):
    # Numerical root counts strictly within (0,k-1); classifications
    # near the critical boundary are deliberately not sampled.
    upper = max(4.0, k + 1.0)
    vals = [derivative_sign_scaled(k,R,w,upper*j/5000) for j in range(5001)]
    crossings = [(x < 0 < y, x > 0 > y) for x,y in zip(vals,vals[1:])]
    local_maxima = sum(b for a,b in crossings)
    boundary_max = vals[0] < 0
    return local_maxima + int(boundary_max), (local_maxima, boundary_max)


def main():
    # Exact rational moment identities, fixed rate ratio, different modes.
    A = (F(7,16), F(11,2), F(11,6))
    B = (F(1971,1972), F(495,493), F(165,493))
    for w,a,b in (A,B):
        assert a / b == 3
        assert moments(w,a,b,3) == (F(1),F(493,242))
        assert moments(w,a,b,3)[1] - F(1) == F(251,242)
    # Exact lower bound exp(16/5) > 70/3 and hence H3>14:
    lower = sum((F(16,5)**j / factorial(j) for j in range(7)), F(0))
    assert lower > F(70,3), lower
    # s*=(1+sqrt5)/2: 8/5<s*<5/3, giving H*>14.
    assert F(8,5) < (1+sqrt(5))/2 < F(5,3)
    # Upper bound H*<e^4<3^4=81, yielding w* < 81/99.
    assert exp(4) < 81
    thr,star = critical(3,3)
    assert F(7,16) < thr < F(1971,1972)
    assert abs(star-(1+sqrt(5))/2)<1e-12
    assert predicted_modes(3,3,float(A[0])) == (2,'boundary_and_interior')
    assert predicted_modes(3,3,float(B[0])) == (1,'boundary')
    print('PASS exact rational moments, both cases; threshold bounds H*>14 and H*<81')

    checks = 0
    for k in range(1,9):
        for R in (0.3,0.7,1.0,1.2,1.8,2.0,2.4,3.0,5.0,10.0):
            for w in (0.005,0.018,0.06,0.15,0.27,0.42,0.62,0.81,0.95,0.995):
                pred = predicted_modes(k,R,w)
                if k >=2:
                    th,_ = critical(k,R)
                    if abs(w-th)<1e-4 or (k==2 and abs(w-1/(1+R*R))<1e-4):
                        continue
                actual,details = count_pos_to_neg_crossings(k,R,w)
                assert actual==pred[0], (k,R,w,pred,actual,details)
                checks+=1
    print(f'PASS {checks} sampled full-density derivative sign-change/mode comparisons')
    print('PASS no external data or dependency; numerical samples do not establish general theorem')

if __name__ == '__main__':
    main()
