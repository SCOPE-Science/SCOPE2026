#!/usr/bin/env python3
"""Exact Weierstrass-gap certificate for the genus-17 multiquadratic curve.

Usage: python3 verify_semigroup.py CERTIFICATE.json
Requires only Python's standard library. Arithmetic is in F_11[alpha]/(alpha^2+1).
"""
import json
import sys

P = 11
ZERO = (0, 0)
ONE = (1, 0)
ALPHA = (0, 1)

def elt(a):
    return (a % P, 0) if isinstance(a, int) else tuple(a)

def add(a, b):
    a, b = elt(a), elt(b)
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)

def neg(a):
    a = elt(a)
    return ((-a[0]) % P, (-a[1]) % P)

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    a, b = elt(a), elt(b)
    return ((a[0]*b[0] - a[1]*b[1]) % P,
            (a[0]*b[1] + a[1]*b[0]) % P)

def inverse(a):
    a = elt(a)
    den = (a[0]*a[0] + a[1]*a[1]) % P
    assert den != 0
    v = pow(den, -1, P)
    return (a[0]*v % P, -a[1]*v % P)

def divide(a, b):
    return mul(a, inverse(b))

def sumfield(seq):
    total = ZERO
    for a in seq:
        total = add(total, a)
    return total

def poly_plus(a, b):
    return [add(a[i] if i < len(a) else ZERO,
                b[i] if i < len(b) else ZERO)
            for i in range(max(len(a), len(b)))]

def poly_scale(a, c):
    return [mul(x, c) for x in a]

def poly_times(a, b):
    out = [ZERO] * (len(a)+len(b)-1)
    for i, aa in enumerate(a):
        for j, bb in enumerate(b):
            out[i+j] = add(out[i+j], mul(aa,bb))
    return out

def poly_shift(a, point):
    """Coefficients of a(point+s), in increasing powers of s."""
    out = [ZERO]
    for c in reversed(a):
        out = poly_plus(poly_times(out, [elt(point),ONE]), [c])
    return out

def power(a, n):
    val = ONE
    while n:
        if n & 1:
            val = mul(val, a)
        a = mul(a,a)
        n >>= 1
    return val

def rank_pivots(mat):
    """Deterministic, complete Gaussian elimination over F_121."""
    rows = [list(map(elt,r)) for r in mat]
    nrows, ncols = len(rows), len(rows[0])
    assert all(len(r) == ncols for r in rows)
    pivots, row = [], 0
    for col in range(ncols):
        lead = next((r for r in range(row,nrows) if rows[r][col] != ZERO), None)
        if lead is None:
            continue
        rows[row], rows[lead] = rows[lead], rows[row]
        factor = inverse(rows[row][col])
        rows[row] = [mul(v,factor) for v in rows[row]]
        for i in range(nrows):
            if i != row and rows[i][col] != ZERO:
                coeff = rows[i][col]
                rows[i] = [sub(v,mul(coeff,w)) for v,w in zip(rows[i],rows[row])]
        pivots.append(col)
        row += 1
        if row == nrows:
            break
    return pivots

def normalized_sqrt_ratio(numer, denom, precision):
    """sqrt( (num/den)/(num(0)/den(0)) ) in F_121[[s]]."""
    assert numer[0] != ZERO and denom[0] != ZERO
    quotient = [ZERO] * precision
    for n in range(precision):
        residue = sub(numer[n] if n < len(numer) else ZERO,
                      sumfield(mul(denom[j],quotient[n-j])
                               for j in range(1,min(n+1,len(denom)))))
        quotient[n] = divide(residue, denom[0])
    quotient = [divide(v, quotient[0]) for v in quotient]
    assert quotient[0] == ONE
    sqrt = [ONE] + [ZERO]*(precision-1)
    for n in range(1,precision):
        remainder = sub(quotient[n], sumfield(mul(sqrt[j],sqrt[n-j])
                                                for j in range(1,n)))
        sqrt[n] = divide(remainder, 2)
    # Independent coefficient-by-coefficient square check.
    for n in range(precision):
        assert sumfield(mul(sqrt[j],sqrt[n-j]) for j in range(n+1)) == quotient[n]
    return sqrt

def matrices():
    # F(x)=(x+1)(x^2+x+1), and four disjoint cubic branch factors.
    A = [ONE,elt(2),elt(2),ONE]
    B = [mul(c,(-1)**i) for i,c in enumerate(A)]
    C = [mul(c,power(ALPHA,i)) for i,c in enumerate(A)]
    D = [mul(c,(-1)**i) for i,c in enumerate(C)]
    product = poly_times(poly_times(A,B),poly_times(C,D))
    assert product == [ONE]+[ZERO]*11+[elt(-1)]  # 1-x^12
    factors = {
       't': poly_scale(poly_times(C,D), 2),
       'u': poly_scale(poly_times(A,B), 2),
       'z': poly_scale(poly_times(A,C), add(ONE,ALPHA)),
       'tu': poly_scale(product,4),
       'tz': poly_scale(poly_times(A,D), mul(2,add(ONE,ALPHA))),
       'uz': poly_scale(poly_times(B,C), mul(2,add(ONE,ALPHA))),
       'tuz': poly_scale(poly_times(B,D),mul(4,add(ONE,ALPHA)))
    }
    moved = {key:poly_shift(poly, -1) for key,poly in factors.items()}
    for key in ('u','z','tu','tz'):
        assert moved[key][0] == ZERO and moved[key][1] != ZERO
    for key in ('t','uz','tuz'):
        assert moved[key][0] != ZERO
    # Four rational places above x=-1; a local uniformizer is u.
    assert moved['t'][0] == elt(4)
    ratio = divide(moved['z'][1], moved['u'][1])
    assert power(ratio,60) == ONE   # z/u specializes in F_121
    assert power(moved['t'][0],60) == ONE
    assert moved['z'][1] == mul(moved['u'][1],mul(sub(ONE,ALPHA),sub(ONE,ALPHA)))
    # All twelve tame branch values are defined over the base field.
    field = [(a,b) for a in range(11) for b in range(11)]
    roots = {v for v in field if power(v,12) == ONE}
    assert len(roots) == 12
    def inverse_x(x):
        return inverse(x)
    def mobius(x):
        numer = add(x,add(7,mul(7,ALPHA)))
        denom = add(mul(add(7,mul(4,ALPHA)),x),ONE)
        return divide(numer,denom)
    seen = {elt(-1)}
    frontier = [elt(-1)]
    while frontier:
        point=frontier.pop()
        for action in (inverse_x,mobius):
            image=action(point)
            assert image in roots
            if image not in seen:
                seen.add(image)
                frontier.append(image)
    assert seen == roots
    configs = {
        'even': ('u', [('u',2),('z',2),('tu',5),('tz',2)],14),
        'odd': ('t', [('t',2),('uz',2),('tuz',2)],8)
    }
    result = {}
    for parity,(ref,blocks,precision) in configs.items():
        rows=[]
        for char,dim in blocks:
            nr = moved[ref]
            dr = moved[char]
            if parity == 'even':
                nr,dr=nr[1:],dr[1:]  # cancel their common simple zero
            sq = normalized_sqrt_ratio(nr,dr,precision)
            for j in range(dim):
                rows.append([ZERO]*j+sq[:precision-j])
        expected = 11 if parity == 'even' else 6
        assert len(rows)==expected
        result[parity] = [[[x[0],x[1]] for x in r] for r in rows]
    return result

def determinant(square):
    a = [list(map(elt, row)) for row in square]
    n = len(a)
    assert all(len(row) == n for row in a)
    out = ONE
    for col in range(n):
        pivot = next((i for i in range(col,n) if a[i][col] != ZERO),None)
        if pivot is None:
            return ZERO
        if pivot != col:
            a[pivot],a[col] = a[col],a[pivot]
            out = neg(out)
        t = a[col][col]
        out = mul(out, t)
        for row in range(col+1,n):
            f = divide(a[row][col], t)
            for j in range(col+1,n):
                a[row][j] = sub(a[row][j],mul(f,a[col][j]))
            a[row][col] = ZERO
    return out

def semigroup_gaps():
    M=matrices()
    even=rank_pivots(M['even'])
    odd=rank_pivots(M['odd'])
    assert even==[0,1,2,3,4,6,7,8,9,12,13]
    assert odd==[0,1,2,3,6,7]
    even_minor=determinant([[r[i] for i in even] for r in M['even']])
    odd_minor=determinant([[r[i] for i in odd] for r in M['odd']])
    assert even_minor==ONE and odd_minor==elt(4)
    vanishing=sorted([2*j for j in even]+[2*j+1 for j in odd])
    gaps=[j+1 for j in vanishing]
    assert len(gaps)==17 and len(set(gaps))==17
    assert gaps==[1,2,3,4,5,6,7,8,9,13,14,15,16,17,19,25,27]
    gens=[10,11,12,18,26]
    nongaps={0}
    for v in range(1,100):
        if any(v-m in nongaps for m in gens):
            nongaps.add(v)
    assert [v for v in range(1,100) if v not in nongaps]==gaps
    assert 27 not in nongaps and all(v in nongaps for v in range(28,38))
    # Ten consecutive nongaps and 10 in the semigroup prove the conductor.
    assert all((g==10 or g not in nongaps or
                all(g-h not in nongaps for h in gens if h!=g)) for g in gens)
    return {'even_pivots':even,'odd_pivots':odd,
            'pivot_minors':{'even':[1,0],'odd':[4,0]},
            'canonical_orders':vanishing,'gaps':gaps,'minimal_generators':gens,
            'multiplicity':10,'conductor':28, 'l_18P':sum(1 for i in range(19) if i in nongaps)}

def main():
    cert = {'field': 'GF(11)[a]/(a^2+1)',
            'point': 'x=-1, one of four rational points of the smooth model',
            'quadratic_character_factors': ['t','u','z','tu','tz','uz','tuz'],
            'matrices':matrices(),
            'results':semigroup_gaps()}
    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf-8') as infile:
            given = json.load(infile)
        assert given == cert, 'independent certificate mismatch'
        print('VERIFY_OK')
    else:
        print(json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
