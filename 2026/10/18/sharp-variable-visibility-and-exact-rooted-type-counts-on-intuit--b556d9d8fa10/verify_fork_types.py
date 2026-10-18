"""Finite tests of rooted fork semantic types in intuitionistic propositional logic.

A fork has one least world (bit 0) and k incomparable maximal leaves
(bits 1..k). Formulas are interpreted on the corresponding upset algebra.
No tests here substitute for universal induction arguments.
"""
from itertools import combinations, product
from math import comb

BOT = ('bot',)

def atom(i):
    return ('atom', i)

def conj(a, b):
    return ('and', a, b)

def disj(a, b):
    return ('or', a, b)

def impl(a, b):
    return ('imp', a, b)

def neg(a):
    return impl(a, BOT)

def join(fs):
    result = BOT
    for f in fs:
        result = disj(result, f)
    return result

def meet(fs):
    result = neg(BOT)
    for f in fs:
        result = conj(result, f)
    return result

def beta(n, t):
    return meet([atom(i) if (t >> i) & 1 else neg(atom(i)) for i in range(n)])

def theta(n, k):
    universe = range(1 << n)
    return join([neg(join(beta(n, t) for t in universe if t not in A))
                 for A in combinations(universe, k)])

def evaluate(f, valuation, k, cache):
    if f in cache:
        return cache[f]
    mask = (1 << (k + 1)) - 1
    if f[0] == 'bot':
        ans = 0
    elif f[0] == 'atom':
        ans = valuation[f[1]]
    else:
        a = evaluate(f[1], valuation, k, cache)
        b = evaluate(f[2], valuation, k, cache)
        if f[0] == 'and':
            ans = a & b
        elif f[0] == 'or':
            ans = a | b
        else:
            local = (~a | b) & mask
            ans = (local & (mask ^ 1)) | (1 if local == mask else 0)
    cache[f] = ans
    return ans

def valid_atom_upsets(k):
    return list(range(0, 1 << (k + 1), 2)) + [(1 << (k + 1)) - 1]

def signature(valuation, n, k):
    a = sum(((valuation[i] & 1) << i) for i in range(n))
    colors = [sum((((valuation[i] >> (j + 1)) & 1) << i)
                  for i in range(n)) for j in range(k)]
    return a, frozenset(colors)

def count_formula(n, k):
    return sum(comb(n, j) * sum(comb(1 << (n-j), s)
                     for s in range(1, min(k, 1 << (n-j)) + 1))
               for j in range(n+1))

def test_type_counts():
    tested = 0
    for n in (1, 2, 3):
        for k in range(1, 6):
            vals = valid_atom_upsets(k)
            types = set(signature(v, n, k) for v in product(vals, repeat=n))
            predicted = count_formula(n, k)
            assert len(types) == predicted, (n, k, len(types), predicted)
            tested += len(vals)**n
            print('TYPES', n, k, len(types), 'valuations', len(vals)**n)
    return tested

def test_distinguishing_formulas():
    tested = 0
    for n in (1, 2, 3):
        for k in range(1, 4):
            vals = valid_atom_upsets(k)
            distinguishing = [atom(i) for i in range(n)] + [neg(beta(n, t)) for t in range(1<<n)]
            dict_sig = {}
            for val in product(vals, repeat=n):
                cache = {}
                vec = tuple(bool(evaluate(f, val, k, cache) & 1) for f in distinguishing)
                sig = signature(val, n, k)
                if vec in dict_sig:
                    assert dict_sig[vec] == sig
                else:
                    dict_sig[vec] = sig
                tested += 1
            assert len(dict_sig) == count_formula(n, k)
            print('SEPARATION', n, k, len(dict_sig))
    return tested

def test_sharp_validity():
    verified=0
    for n in (1, 2, 3):
        for k in range(1, min(3, (1<<n)-1)+1):
            f = theta(n, k)
            for val in product(valid_atom_upsets(k), repeat=n):
                truth = evaluate(f, val, k, {})
                assert truth == (1 << (k+1)) - 1, (n, k, val, truth)
                verified += 1
            # On k+1 leaves, assign k+1 distinct colors and the all-false root.
            colors = list(range(k+1))
            v = tuple(sum((1 << (j+1)) for j,c in enumerate(colors) if (c >> i) & 1)
                      for i in range(n))
            assert not (evaluate(f, v, k+1, {}) & 1), (n, k)
            print('SHARP', n, k, 'valid_and_counterexample')
    return verified

if __name__ == '__main__':
    a=test_type_counts()
    b=test_distinguishing_formulas()
    c=test_sharp_validity()
    print('PASS',a,'valuation-type checks;',b,'distinguishing checks;',c,'full formula validity checks')
