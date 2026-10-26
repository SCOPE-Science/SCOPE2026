"""Finite sanity checks for x -> x^3+1 on Z_5; not an infinite proof."""

def f(x, modulus):
    return (x*x*x + 1) % modulus


def cycle_decomposition(modulus):
    done = set()
    cycles = []
    for start in range(modulus):
        if start in done:
            continue
        path = []
        index = {}
        x = start
        while x not in index and x not in done:
            index[x] = len(path)
            path.append(x)
            x = f(x, modulus)
        if x in index:
            cyc = path[index[x]:]
            # canonical rotation makes cycle comparisons deterministic
            j = cyc.index(min(cyc))
            cyc = tuple(cyc[j:] + cyc[:j])
            cycles.append(cyc)
        done.update(path)
    return cycles


def fixed_point_residue_3(modulus):
    roots = [x for x in range(modulus) if x % 5 == 3 and (x*x*x - x + 1) % modulus == 0]
    assert len(roots) == 1, (modulus, roots)
    return roots[0]


def main():
    for n in range(1, 6):
        modulus = 5**n
        alpha = fixed_point_residue_3(modulus)
        cycles = cycle_decomposition(modulus)
        b_cycles = [c for c in cycles if c[0] % 5 == 3]
        c_cycles = [c for c in cycles if c[0] % 5 != 3]
        expected_b = sorted([1] + [4 * 5**(n-k-1) for k in range(1, n)])
        got_b = sorted(len(c) for c in b_cycles)
        assert got_b == expected_b, (n, got_b, expected_b)
        assert len(c_cycles) == 1 and len(c_cycles[0]) == 4, (n, [len(c) for c in c_cycles])
        # Every residue outside B must eventually enter the unique 4-cycle.
        cycle_set = set(c_cycles[0])
        for x in range(modulus):
            if x % 5 == 3:
                continue
            y = x
            for _ in range(4 * (n + 2)):
                if y in cycle_set:
                    break
                y = f(y, modulus)
            assert y in cycle_set, (n, x, y)
        print(f"n={n}, modulus={modulus}, fixed_point={alpha}, B_cycle_lengths={got_b}, other_cycle_length=4")
    print("VERIFY_OK (finite checks n=1..5 only; proof covers all n)")

if __name__ == '__main__':
    main()
