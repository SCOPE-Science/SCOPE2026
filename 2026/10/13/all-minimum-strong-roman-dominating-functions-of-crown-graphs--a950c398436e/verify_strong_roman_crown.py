#!/usr/bin/env python3
from itertools import product
from math import ceil


def is_strong_roman(n, vals):
    assert len(vals) == 2*n
    for z, val in enumerate(vals):
        if val != 0:
            continue
        if z < n:
            i = z
            ok = False
            for j in range(n):
                if j == i:
                    continue
                w = n + j
                if vals[w] < 2:
                    continue
                zero_neighbors = sum(vals[k] == 0 for k in range(n) if k != j)
                if vals[w] >= 1 + ceil(zero_neighbors / 2):
                    ok = True
                    break
        else:
            i = z - n
            ok = False
            for j in range(n):
                if j == i:
                    continue
                w = j
                if vals[w] < 2:
                    continue
                zero_neighbors = sum(vals[n+k] == 0 for k in range(n) if k != j)
                if vals[w] >= 1 + ceil(zero_neighbors / 2):
                    ok = True
                    break
        if not ok:
            return False
    return True


def exhaustive(n):
    max_label = ceil((n-1)/2) + 1
    best = 10**9
    minima = []
    checked = 0
    for vals in product(range(max_label+1), repeat=2*n):
        w = sum(vals)
        if w > best:
            continue
        checked += 1
        if is_strong_roman(n, vals):
            if w < best:
                best = w
                minima = [vals]
            elif w == best:
                minima.append(vals)
    return best, minima, checked


def side_excess(z, common_positive, positive_inside_zero):
    if z == 0:
        return 0
    choices = []
    if common_positive >= 1:
        choices.append(ceil(z/2))
    if positive_inside_zero >= 2:
        choices.append(2*ceil((z-1)/2))
    return min(choices) if choices else None


def fixed_zero_min_weight(n, p, q, c):
    if c < max(0, p+q-n) or c > min(p, q):
        return None
    r = n-p-q+c
    ea = side_excess(q, r, q-c)
    eb = side_excess(p, r, p-c)
    if ea is None or eb is None:
        return None
    return 2*n-p-q+ea+eb


def optimal_patterns(n):
    best = 10**9
    pats = []
    for p in range(n+1):
        for q in range(n+1):
            for c in range(max(0,p+q-n), min(p,q)+1):
                w = fixed_zero_min_weight(n,p,q,c)
                if w is None:
                    continue
                r = n-p-q+c
                tup = (p,q,c,r)
                if w < best:
                    best = w
                    pats = [tup]
                elif w == best:
                    pats.append(tup)
    return best, sorted(pats)


def classified_minima(n):
    out=set()
    if n % 2:
        m=(n-1)//2
        for k in range(n):
            vals=[0]*(2*n)
            vals[k]=m+1
            vals[n+k]=m+1
            out.add(tuple(vals))
        return out
    m=n//2
    # (i) common singleton support.
    for k in range(n):
        vals=[0]*(2*n)
        vals[k]=m+1; vals[n+k]=m+1
        out.add(tuple(vals))
    # (ii) A support {k,u}, B support {k}; (iii) symmetric.
    for k in range(n):
        for u in range(n):
            if u==k: continue
            vals=[0]*(2*n)
            vals[k]=m+1; vals[u]=1; vals[n+k]=m
            out.add(tuple(vals))
            vals=[0]*(2*n)
            vals[k]=m; vals[n+k]=m+1; vals[n+u]=1
            out.add(tuple(vals))
    # (iv) two 2-supports meeting in exactly one index.
    for k in range(n):
        for u in range(n):
            if u==k: continue
            for v in range(n):
                if v==k or v==u: continue
                vals=[0]*(2*n)
                vals[k]=m; vals[u]=1; vals[n+k]=m; vals[n+v]=1
                out.add(tuple(vals))
    # (v) identical 2-supports, independently choose the strong index on each side.
    for k in range(n):
        for ell in range(k+1,n):
            for ha in (k,ell):
                for hb in (k,ell):
                    vals=[0]*(2*n)
                    vals[k]=1; vals[ell]=1; vals[ha]=m
                    vals[n+k]=1; vals[n+ell]=1; vals[n+hb]=m
                    out.add(tuple(vals))
    return out


def expected_patterns(n):
    if n % 2:
        return [(n-1,n-1,n-1,1)]
    return sorted([
        (n-2,n-2,n-3,1),
        (n-2,n-2,n-2,2),
        (n-2,n-1,n-2,1),
        (n-1,n-2,n-2,1),
        (n-1,n-1,n-1,1),
    ])


def expected_count(n):
    return n if n % 2 else n*(n*n+n-1)


def main():
    exhaustive_checked=0
    for n in (3,4,5):
        best, minima, checked=exhaustive(n)
        exhaustive_checked += checked
        target=n+1 if n%2 else n+2
        assert best==target, (n,best,target)
        classified=classified_minima(n)
        assert set(minima)==classified, (n,len(minima),len(classified),len(set(minima)^classified))
        assert len(minima)==expected_count(n), (n,len(minima),expected_count(n))
    pattern_checks=0
    for n in range(3,51):
        best,pats=optimal_patterns(n)
        target=n+1 if n%2 else n+2
        assert best==target, (n,best,target)
        assert pats==expected_patterns(n), (n,pats,expected_patterns(n))
        pattern_checks += sum(1 for p in range(n+1) for q in range(n+1) for c in range(max(0,p+q-n),min(p,q)+1))
    generated=0
    for n in range(3,21):
        fam=classified_minima(n)
        assert len(fam)==expected_count(n), (n,len(fam),expected_count(n))
        target=n+1 if n%2 else n+2
        for vals in fam:
            assert sum(vals)==target
            assert is_strong_roman(n,vals)
            generated += 1
    print(f"VERIFY_OK exhaustive_n=3..5 filtered_labelings={exhaustive_checked} pattern_n=3..50 pattern_checks={pattern_checks} classified_n=3..20 generated_minima={generated}")

if __name__=='__main__':
    main()
