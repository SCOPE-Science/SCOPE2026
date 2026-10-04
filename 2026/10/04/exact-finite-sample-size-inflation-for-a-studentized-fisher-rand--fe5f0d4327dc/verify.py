from fractions import Fraction as F
from itertools import combinations

N = 6
N1 = 3
Y0 = [F(-996,1000), F(-1004,1000), F(19,1000), F(-997,1000), F(-16,1000), F(-989,1000)]
Y1 = [F(1044,1000), F(1026,1000), F(2000,1000), F(967,1000), F(-33,1000), F(-8987,1000)]
A = list(combinations(range(N), N1))

def mean(x):
    return sum(x, F(0)) / len(x)

def svar(x):
    m = mean(x)
    return sum((v-m)**2 for v in x) / (len(x)-1)

def t2(y, a):
    s = set(a)
    yt = [y[i] for i in range(N) if i in s]
    yc = [y[i] for i in range(N) if i not in s]
    den = svar(yt)/N1 + svar(yc)/(N-N1)
    assert den > 0
    return (mean(yt)-mean(yc))**2 / den, den

assert sum(Y1[i]-Y0[i] for i in range(N)) == 0
ps = []
minimum_denominator = None
for observed_assignment in A:
    s = set(observed_assignment)
    y = [Y1[i] if i in s else Y0[i] for i in range(N)]
    observed_t2, observed_denominator = t2(y, observed_assignment)
    reference = []
    for reference_assignment in A:
        value, denominator = t2(y, reference_assignment)
        reference.append(value)
        if minimum_denominator is None or denominator < minimum_denominator:
            minimum_denominator = denominator
    tail_count = sum(value >= observed_t2 for value in reference)
    ps.append(F(tail_count, len(A)))

counts = {p: ps.count(p) for p in set(ps)}
assert counts == {F(1,10): 7, F(1,5): 3, F(9,10): 3, F(1): 7}
assert minimum_denominator == F(246719,2250000)
reject_count = sum(p <= F(1,10) for p in ps)
assert reject_count == 7
assert F(reject_count, len(A)) == F(7,20)
print('VERIFY_OK')
