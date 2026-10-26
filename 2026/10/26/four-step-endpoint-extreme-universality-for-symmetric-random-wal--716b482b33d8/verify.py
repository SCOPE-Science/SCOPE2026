"""Independent finite exact-arithmetic checks for four-step random-walk endpoint extrema."""
from fractions import Fraction
from itertools import permutations, product, combinations

PATTERNS = ('----', '-+--', '--+-', '-++-')

def general_position(aa):
    # Distinct nonzero values and no vanishing signed sub-sum.
    if len(set(aa)) != 4 or min(aa) <= 0:
        return False
    for n in range(1, 5):
        for ss in combinations(aa, n):
            for signs in product((-1, 1), repeat=n):
                if sum(s*x for s,x in zip(signs, ss)) == 0:
                    return False
    return True

def direct_counts(aa):
    counts = {}
    for signs in product('+-', repeat=4):
        pat = ''.join(signs)
        count = 0
        for z in permutations(aa):
            s = Fraction(0)
            vals = [s]
            for sign,x in zip(signs,z):
                s += x if sign == '+' else -x
                vals.append(s)
            count += vals[0] > max(vals[1:]) and vals[-1] < min(vals[:-1])
        if count:
            counts[pat] = count
    return counts

def theoretical_counts(aa):
    u,v,w,z = sorted(aa)
    I = int(w<u+v)
    return {'----':24, '-+--':10+2*I, '--+-':10+2*I, '-++-':4*(1-I)} if not I else {'----':24, '-+--':12, '--+-':12}

# All tuples below have rational entries and no nonempty signed zero sub-sum.
EXAMPLES=[(1,3,7,20),(1,2,4,9),(1,4,6,25),(13,17,19,24),(100,115,135,160),(11,17,23,31), (5,8,12,30), (101,103,109,127)]
checks=0
for ints in EXAMPLES:
    aa=tuple(map(Fraction,ints))
    assert general_position(aa), f'Not generic: {ints}'
    a=direct_counts(aa)
    b={k:v for k,v in theoretical_counts(aa).items() if v}
    assert a==b, (ints,a,b)
    assert sum(a.values())==48
    checks+= len(PATTERNS) + 2
print(f'PASS: {checks} exact-rational assertions across {len(EXAMPLES)} magnitude configurations; each of 384 signed orders directly enumerated.')
