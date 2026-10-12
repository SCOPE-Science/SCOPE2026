#!/usr/bin/env python3
"""Independent finite checks for the strict weak-order modal term spectrum.

Frames are finite nonempty ordinal sums of antichains, with i R j iff
level(i) < level(j), never self-accessibility. Ordinary existential diamond.
This checks small finite instances, not the unrestricted theorem.
"""
from itertools import product
from math import comb
from fractions import Fraction


def s(m, q):
    return sum(comb(q, k) for k in range(1, min(m, q) + 1))


def expected_E(widths, q):
    ans = 0
    suffix = 1
    for m in reversed(widths):
        ans += q * suffix
        suffix *= s(m, q)
    return ans


def vertices(widths):
    lev = tuple(i for i, a in enumerate(widths) for _ in range(a))
    successors = tuple(tuple(v for v in range(len(lev)) if lev[v] > lev[w]) for w in range(len(lev)))
    return lev, successors


def canonical_type(color, w, succ, cache):
    if w not in cache:
        cache[w] = (color[w], frozenset(canonical_type(color, v, succ, cache) for v in succ[w]))
    return cache[w]


def check_pointed_types(widths, q):
    lev, succ = vertices(widths)
    n = len(lev)
    type_to_signature, signature_to_type = {}, {}
    count = 0
    for color in product(range(q), repeat=n):
        cache = {}
        palettes = tuple(frozenset(color[w] for w in range(n) if lev[w] == i) for i in range(len(widths)))
        for w in range(n):
            typ = canonical_type(color, w, succ, cache)
            sig = (lev[w], color[w], palettes[lev[w] + 1:])
            if typ in type_to_signature:
                assert type_to_signature[typ] == sig
            else:
                type_to_signature[typ] = sig
            if sig in signature_to_type:
                assert signature_to_type[sig] == typ
            else:
                signature_to_type[sig] = typ
            count += 1
    assert len(type_to_signature) == len(signature_to_type) == expected_E(widths, q), (widths,q, len(type_to_signature), expected_E(widths,q))
    return count


def check_clone(widths, r=1):
    """Construct the full term-operation closure independently, for small frames."""
    lev, succ = vertices(widths)
    n = len(lev)
    assignments = list(product(range(2**n),repeat=r))
    nbits = n*len(assignments)
    full = (1 << nbits)-1

    def lift_projection(j):
        acc = 0
        for vindex, values in enumerate(assignments):
            acc |= values[j] << (n*vindex)
        return acc

    def modal(t):
        ans=0
        for vindex in range(len(assignments)):
            block=(t >> (n*vindex)) & ((1<<n)-1)
            out = 0
            for w in range(n):
                if any((block>>v)&1 for v in succ[w]):
                    out |= 1<<w
            ans |= out << (n*vindex)
        return ans

    seen = {0,full}
    todo = [0,full]
    for j in range(r):
        x=lift_projection(j)
        if x not in seen:
            seen.add(x);todo.append(x)
    while todo:
        a=todo.pop()
        candidates = {a^full,modal(a)}
        for b in tuple(seen):
            candidates.add(a&b)
            candidates.add(a|b)
        for c in candidates:
            if c not in seen:
                seen.add(c);todo.append(c)
    assert len(seen)==2**expected_E(widths,2**r),(widths,r,len(seen),2**expected_E(widths,2**r))
    return len(seen)


def poly_mul(a,b):
    r=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return r


def poly_add(a,b):
    r=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): r[i]+=x
    for i,x in enumerate(b): r[i]+=x
    return r


def polynomial_S(m):
    res=[Fraction(0)]
    prod=[Fraction(1)]
    for k in range(1,m+1):
        prod=poly_mul(prod,[Fraction(1-k,k),Fraction(1,k)])
        res=poly_add(res,prod)
    return res


def polynomial_E_over_q(widths):
    value=[Fraction(0)]
    suffix=[Fraction(1)]
    for m in reversed(widths):
        value=poly_add(value,suffix)
        suffix=poly_mul(suffix,polynomial_S(m))
    return value


def poly_div_exact(a,b):
    if not b or b[-1]==0: raise ValueError('zero denominator')
    a=list(a)
    quo=[Fraction(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        d=len(a)-len(b)
        c=a[-1]/b[-1]
        quo[d]=c
        for i,x in enumerate(b): a[d+i]-=c*x
        while a and a[-1]==0: a.pop()
    assert not any(a),(a,b,quo)
    while len(quo)>1 and not quo[-1]:quo.pop()
    return quo


def reconstruct_tail(F,h,maxwidth=15):
    # F=P(q)/q, full polynomial; widths are identified from the bottom up.
    widths=[]
    for _ in range(h-1):
        assert F[0]==1
        slopes=[polynomial_S(m)[1] for m in range(1,maxwidth+1)]
        assert len(set(slopes))==len(slopes)
        t=F[1] if len(F)>1 else Fraction(0)
        assert t in slopes, (t,slopes)
        m=slopes.index(t)+1
        widths.append(m)
        F=poly_div_exact([F[0]-1]+F[1:],polynomial_S(m))
    assert F==[Fraction(1)],F
    return tuple(reversed(widths))


def all_vectors(limit_n=6,max_h=4):
    def make(h,remaining):
        if h==0:
            if remaining==0:yield ()
            return
        for v in range(1,remaining-h+2):
            for other in make(h-1,remaining-v): yield (v,)+other
    for n in range(1,limit_n+1):
        for h in range(1,min(max_h,n)+1): yield from make(h,n)


def main():
    vector_count=0; tests=0; valuations=0; inverse_tests=0
    for widths in all_vectors():
        vector_count+=1
        for q in (1,2,4):
            if q**sum(widths) > 50000:continue
            valuations+=check_pointed_types(widths,q)
            tests+=1
        F=polynomial_E_over_q(widths)
        for q in (1,2,4,7):
            assert sum(a*q**i for i,a in enumerate(F))*q==expected_E(widths,q), (widths,q,F)
        assert reconstruct_tail(F,len(widths))==widths[1:]
        inverse_tests+=1
    clone_tests=0; total_operations=0
    for widths in all_vectors(limit_n=4):
        got=check_clone(widths,0)
        clone_tests+=1; total_operations+=got
    for widths in all_vectors(limit_n=3):
        got=check_clone(widths,1)
        clone_tests+=1; total_operations+=got
    # Width of the first antichain is intentionally not identifiable.
    for tail in ((1,), (2,), (1,2), (2,1), (2,3,1)):
        Fs=[polynomial_E_over_q((first,)+tail) for first in (1,2,4,7)]
        assert Fs.count(Fs[0]) == len(Fs)
    print('VERIFY_OK', 'vectors', vector_count, 'type_tests',tests,
          'pointed_valuation_samples',valuations,'inverse_polynomials',inverse_tests,
          'direct_clone_tests',clone_tests,'direct_term_operations_total',total_operations,
          'root_invariance_families',5)

if __name__ == '__main__':main()
