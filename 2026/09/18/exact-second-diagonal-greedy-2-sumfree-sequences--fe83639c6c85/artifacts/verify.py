from itertools import combinations

def claimed_member(f, n):
    m = 9*f - 1
    r = n % m
    in_residues = (
        r in (f, f+1, 8*f-2, 8*f-1)
        or 3*f <= r <= 4*f-2
        or 5*f+1 <= r <= 6*f-1
    )
    return n in (4*f-1, 5*f) or (in_residues and n != f+1)

def greedy(f, count):
    seq = [f, 3*f]
    pair_sums = {4*f}
    x = 3*f + 1
    while len(seq) < count:
        if x not in pair_sums:
            for a in seq:
                pair_sums.add(a + x)
            seq.append(x)
        x += 1
    return seq

def residue_set(f):
    R = {f, f+1, 8*f-2, 8*f-1}
    R.update(range(3*f, 4*f-1))
    R.update(range(5*f+1, 6*f))
    return R

def difference_word(f):
    prefix = [2*f] + [1]*(f-1) + [f+1, 1]
    period = (
        [1]*(f-2)
        + [2*f-1, 1, 2*f, 1, 2*f-1]
        + [1]*(f-2)
        + [f+3]
    )
    return prefix, period

def check_residue_sumfree(f):
    m = 9*f - 1
    R = residue_set(f)
    for a in R:
        for b in R:
            if (a+b) % m in R:
                return False, ("periodic", a, b, (a+b) % m)
    for e in (4*f-1, 5*f):
        for a in R:
            if (e+a) % m in R:
                return False, ("exception", e, a, (e+a) % m)
    if ((4*f-1)+(5*f)) % m in R:
        return False, ("exception-pair",)
    return True, None

def witness_base(f, r):
    m = 9*f - 1
    if r == 0:
        return (f, 8*f-1, 1, 0)
    if 1 <= r <= f-1:
        return (4*f-1, 5*f+r, 1, 1)
    if f+2 <= r <= 2*f:
        return (5*f, 4*f-1+r, 1, 1)
    if 2*f+1 <= r <= 3*f-2:
        return (f+1+r, 8*f-2, 1, 1)
    if r == 3*f-1:
        return (4*f-1, 8*f-1, 1, 1)
    if r == 4*f-1:
        return (5*f, 8*f-2, 1, 1)
    if 4*f <= r <= 5*f-1:
        return (f, r-f, 0, 0)
    if r == 5*f:
        return (4*f-1, f+1, 0, 1)
    if r == 6*f:
        return (5*f, f, 0, 1)
    if 6*f+1 <= r <= 7*f-1:
        return (f, r-f, 0, 0)
    if r == 7*f:
        return (f+1, 6*f-1, 0, 0)
    if 7*f+1 <= r <= 8*f-3:
        return (4*f-1, r-(4*f-1), 0, 1)
    if 8*f <= r <= 9*f-2:
        return (5*f, r-5*f, 0, 1)
    return None

def check_saturation_witnesses(f):
    m = 9*f - 1
    R = residue_set(f)
    excluded = [r for r in range(m) if r not in R]
    for r in excluded:
        w = witness_base(f, r)
        if w is None:
            return False, ("missing", r)
        a, b, eps, shift_second = w
        if a == b or a + b != r + eps*m:
            return False, ("bad-base", r, w)
        q = 2
        if eps == 1:
            shift = (q-1)*m
        else:
            shift = q*m
        if shift_second:
            aa, bb = a, b + shift
        else:
            aa, bb = a + shift, b
        x = q*m + r
        if aa == bb or aa + bb != x:
            return False, ("bad-shift", r, w, aa, bb, x)
        if not (claimed_member(f, aa) and claimed_member(f, bb)):
            return False, ("nonmember", r, w, aa, bb)
        if not (aa < x and bb < x):
            return False, ("not-earlier", r, w, aa, bb, x)
    return True, None

def check_formula(f, count=700):
    seq = greedy(f, count)
    upto = seq[-1]
    claimed = [n for n in range(1, upto+1) if claimed_member(f, n)]
    if claimed[:count] != seq:
        return False
    diffs = [b-a for a,b in zip(seq, seq[1:])]
    prefix, period = difference_word(f)
    if diffs[:len(prefix)] != prefix:
        return False
    for i, d in enumerate(diffs[len(prefix):]):
        if d != period[i % len(period)]:
            return False
    if sum(period) != 9*f-1 or len(period) != 2*f+2:
        return False
    if period.count(2*f) != 1:
        return False
    return True

def main():
    for f in range(4, 81):
        assert check_formula(f, 700)
    for f in range(4, 201):
        ok, detail = check_residue_sumfree(f)
        assert ok, (f, detail)
        ok, detail = check_saturation_witnesses(f)
        assert ok, (f, detail)

    f = 4
    seq = greedy(f, 30)
    prefix, period = difference_word(f)
    print("verified exact greedy formula for f=4..80 (700 terms each)")
    print("verified modular sum-free and saturation certificates for f=4..200")
    print("f=4 first 30 terms:", seq)
    print("f=4 preperiod:", prefix)
    print("f=4 period:", period)
    print("f=4 period length:", len(period), "period sum:", sum(period))
    print("all checks passed")

if __name__ == "__main__":
    main()
