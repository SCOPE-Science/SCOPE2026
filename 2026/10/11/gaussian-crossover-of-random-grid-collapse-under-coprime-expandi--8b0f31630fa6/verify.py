"""Exact rational checks and finite-size diagnostics for integer expanding circle maps."""
from fractions import Fraction
from itertools import product
from math import comb, erf, exp, lgamma, log, sqrt


def image_weights(n, word, a=2, b=3):
    N = (a * b) ** n
    counts = [0] * N
    for start in range(N):
        z = start
        for digit in word:
            z = (a if digit == 0 else b) * z % N
        counts[z] += 1
    return [Fraction(v, N) for v in counts]


def cramer_square(weights):
    N = len(weights)
    integral_h = Fraction(0)
    integral_h2 = Fraction(0)
    cumulative = Fraction(0)
    for j, w in enumerate(weights):
        cumulative += w
        b = cumulative - Fraction(j, N)
        integral_h += b / N - Fraction(1, 2 * N * N)
        integral_h2 += b * b / N - b / (N * N) + Fraction(1, 3 * N**3)
    return integral_h2 - integral_h * integral_h


def exact_cramer_square(n, count_a, count_b, a=2, b=3):
    N = (a * b)**n
    M = N // (a**min(n,count_a)*b**min(n,count_b))
    return Fraction(1, 12*M*M)


def exact_cdf(n, t, p=Fraction(1,2)):
    if t < 2*n:
        return Fraction(0)
    return sum((Fraction(comb(t,k))*p**k*(1-p)**(t-k) for k in range(n,t-n+1)),Fraction(0))


def gaussian_cdf(s, beta):
    if s < 0: return 0.0
    normal = lambda x: (1.0+erf(x/sqrt(2.0)))/2.0
    return normal((s-4*beta)/sqrt(2)) - normal((-s-4*beta)/sqrt(2))


def numeric_cdf(n, t, beta):
    if t < 2*n: return 0.0
    p = 0.5 + beta/sqrt(n)
    out=0.0
    for k in range(n,t-n+1):
        out += exp(lgamma(t+1)-lgamma(k+1)-lgamma(t-k+1)+k*log(p)+(t-k)*log(1-p))
    return out


def main():
    tests=0
    for n in (1,2,3):
        for t in range(0,7):
            for word in product((0,1), repeat=t):
                weights=image_weights(n, word)
                k=word.count(0)
                assert cramer_square(weights)==exact_cramer_square(n,k,t-k)
                assert sum(weights)==1
                tests+=1
    for n in (1,2,3):
        for t in range(0,10):
            observed=Fraction(sum(1 for word in product((0,1),repeat=t) if word.count(0)>=n and word.count(1)>=n),2**t)
            assert observed==exact_cdf(n,t)
    for s,beta in ((1.0,0.0),(2.0,0.0),(1.0,0.5),(3.0,-0.7)):
        pred=gaussian_cdf(s,beta)
        for n in (400,1600):
            t=int(2*n+s*sqrt(n))
            measured=numeric_cdf(n,t,beta)
            assert abs(pred-measured)<0.06, (n,s,beta,pred,measured)
        print(f'n={n}, s={s}, beta={beta}: predicted={pred:.6f}, observed={measured:.6f}')
    print('CHECK_OK', tests)

if __name__=='__main__': main()
