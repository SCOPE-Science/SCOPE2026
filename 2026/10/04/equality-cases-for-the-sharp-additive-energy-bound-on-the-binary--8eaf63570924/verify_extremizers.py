from collections import Counter
from itertools import product
from math import log2


def add(u, v):
    return tuple(a+b for a,b in zip(u,v))

def sub(u, v):
    return tuple(a-b for a,b in zip(u,v))

def energy(A):
    c = Counter(add(x,y) for x in A for y in A)
    return sum(v*v for v in c.values())

def diff_mult(A):
    return Counter(sub(x,y) for x in A for y in A)

def is_power_two(n):
    return n > 0 and (n & (n-1)) == 0

def is_affine_boolean_cube(A):
    A = set(A)
    n = len(A)
    if not is_power_two(n):
        return False
    if n == 1:
        return True
    m = n.bit_length()-1
    r = diff_mult(A)
    # In a rank-m proper Boolean cube, the exactly-one-generator
    # differences are precisely the nonzero differences with multiplicity n/2.
    cand = [z for z,c in r.items() if any(z) and c == n//2]
    reps = []
    seen = set()
    for z in cand:
        if z in seen:
            continue
        nz = tuple(-a for a in z)
        seen.add(z); seen.add(nz)
        reps.append(z)
    if len(reps) != m:
        return False
    # Sign choices can be absorbed into the base point. Test all signs and bases.
    for signs in product((-1,1), repeat=m):
        gs = [tuple(s*a for a in g) for s,g in zip(signs,reps)]
        sums = []
        for bits in product((0,1), repeat=m):
            v = tuple(sum(bits[j]*gs[j][k] for j in range(m)) for k in range(len(gs[0])))
            sums.append(v)
        if len(set(sums)) != n:
            continue
        for b in A:
            gen = {add(b,s) for s in sums}
            if gen == A:
                return True
    return False

def main():
    p = log2(6)
    all_stats = {}
    for d in range(1,5):
        pts = list(product((0,1), repeat=d))
        eq_by_size = Counter()
        affine_by_size = Counter()
        mismatches = []
        for mask in range(1, 1 << len(pts)):
            A = [pts[i] for i in range(len(pts)) if (mask >> i) & 1]
            n = len(A)
            e = energy(A)
            # Equality is exact iff n^p = 6^m for n=2^m. For non-powers of 2,
            # compare numerically only as a diagnostic; the theorem predicts strictness.
            if is_power_two(n):
                m = n.bit_length()-1
                eq = (e == 6**m)
            else:
                eq = abs(e - n**p) < 1e-10
            cube = is_affine_boolean_cube(A)
            if eq:
                eq_by_size[n] += 1
            if cube:
                affine_by_size[n] += 1
            if eq != cube:
                mismatches.append((A,e,n**p,cube))
                if len(mismatches) >= 5:
                    break
        if mismatches:
            print(f"d={d} MISMATCHES={mismatches}")
            raise SystemExit(1)
        all_stats[d] = (dict(sorted(eq_by_size.items())), dict(sorted(affine_by_size.items())))
        print(f"d={d} equality_counts={dict(sorted(eq_by_size.items()))} affine_cube_counts={dict(sorted(affine_by_size.items()))}")
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
