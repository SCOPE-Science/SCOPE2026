"""Independent finite checks for permutation-invariant preconditionals.

Use: python3 checker.py. Standard library only. Mathematical definitions
P1--P5, conditional identity, semicomplementation and double-negation
inflation are tested directly; finite checks do not replace the proof.
"""
from itertools import product, combinations_with_replacement
from collections import defaultdict


def recurrence_count(m):
    """Independent dynamic programming count of compatible ternary rows."""
    # State = (previous zero prefix, lowest prior two suffix for a row with ones).
    states = {(0, m): 1}  # sentinel m means no previous middle-type row
    for k in range(2, m):
        nxt = defaultdict(int)
        for (old_z, cap), count in states.items():
            for z in range(old_z, k):
                for c in range(k-z):
                    if c > cap:
                        continue
                    b = k - 1 - z - c
                    nxt[(z, min(cap, c) if b else cap)] += count
        states = nxt
    return sum(states.values()) + 1


def arrays(m):
    """Enumerate proposed ternary normal forms on m-atom Boolean algebras."""
    states = [((),)]  # rank 1 has no interior arguments
    for k in range(2, m):
        next_states = []
        for old in states:
            preceding = old[-1]
            for row in combinations_with_replacement((0, 1, 2), k-1):
                if all((v != 0 or row[j-1] == 0) and
                           (v != 1 or row[k-d+j-1] <= 1)
                           for d, preceding in enumerate(old, 1)
                           for j, v in enumerate(preceding, 1)):
                # all earlier ranks are needed for type-1 constraints
                    next_states.append(old+(row,))
        states = next_states
    return states


def operation(m, options):
    """Build an equivariant operation from full orbit options by rank.

    option 0: D, 1: A, 2: D union A-complement, 3: universe.
    """
    full = (1 << m)-1
    out = []
    for a in range(1 << m):
        k = a.bit_count()
        row = []
        for b in range(1 << m):
            d = a & b
            j = d.bit_count()
            if k == 0:
                v = full
            elif k == m:
                v = b
            elif j == 0:
                v = 0 if options[k][0] == 0 else full ^ a
            elif j == k:
                v = full
            else:
                typ = options[k][j]
                v = (d, a, d | (full ^ a), full)[typ]
            row.append(v)
        out.append(tuple(row))
    return tuple(out)


def check_axioms(m, f):
    full = (1 << m)-1
    B = range(full+1)
    if any(f[full][a] & ~a for a in B): return False
    for a in B:
        if f[a][a] != full: return False
        if (a & f[a][0]): return False
        if a & ~f[f[a][0]][0]: return False
        for b in B:
            if (a & b) & ~f[a][b]: return False
            if f[a][b] & ~f[a][a & b]: return False
            for c in B:
                if f[a][b & c] & ~f[a][b]: return False
                d = a & b
                if f[a][f[d][c]] & ~f[d][c]: return False
    return True


def all_orbit_options(m):
    keys = [(k,j) for k in range(1,m) for j in range(k)]
    opts = [range(2) if j == 0 else range(4) for k,j in keys]
    for tpl in product(*opts):
        choices = {k: [None]*k for k in range(1,m)}
        for (k,j),v in zip(keys,tpl): choices[k][j] = v
        yield choices


def forms_as_operations(m):
    out=set()
    for t in arrays(m):
        opts={k:[0]+[dict(enumerate((0,2,3)))[x] for x in t[k-1]]
              for k in range(1,m)}
        out.add(operation(m,opts))
    full=(1<<m)-1
    out.add(tuple(tuple((full^a)|b for b in range(full+1))
                  for a in range(full+1)))
    return out


def main():
    for m in range(2,9):
        count=len(arrays(m))
        expected={2:1, 3:3, 4:12, 5:54, 6:260, 7:1309, 8:6801}[m]
        assert count==expected,(m,count,expected)
        print(f'NORMAL_FORMS atoms={m}: minimal_negation={count}, all={count+1}')
    for m in range(2,9):
        assert recurrence_count(m)==len(arrays(m))+1
    print('INDEPENDENT_DP_CROSSCHECK atoms=2..8 EXACT_MATCH')
    for m in (2,3,4):
        actual={operation(m,opts) for opts in all_orbit_options(m)
                if check_axioms(m, operation(m,opts))}
        predicted=forms_as_operations(m)
        assert actual==predicted,(m,len(actual),len(predicted),len(actual^predicted))
        print(f'BRUTE_ALL_EQUIVARIANT atoms={m}: count={len(actual)}, EXACT_MATCH')
    print('ALL_CHECKS_OK')

if __name__=='__main__':
    main()
