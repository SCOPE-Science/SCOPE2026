"""Independent finite checks of prescribed-target sum-product avoidance."""
from collections import Counter
from math import isqrt


def primes_below(bound):
    out = []
    for p in range(5, bound):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            out.append(p)
    return out


def order_projective(p, target):
    # h(x) = target - target/x; None represents projective infinity.
    x = None
    for j in range(1, p + 2):
        if x is None:
            x = target
        elif x == 0:
            x = None
        else:
            x = (target - target * pow(x, -1, p)) % p
        if x is None:
            return j
    raise AssertionError((p, target, "no projective return"))


def graph(p, target):
    nbr = [set() for _ in range(p)]
    loops = set()
    for x in range(p):
        y = (target - x) % p
        if x == y:
            loops.add(x)
        else:
            nbr[x].add(y)
            nbr[y].add(x)
        if x:
            y = (target * pow(x, -1, p)) % p
            if y == x:
                loops.add(x)
            else:
                nbr[x].add(y)
                nbr[y].add(x)
    return nbr, loops


def max_independent_path(seq, cyclic, loops):
    best = -10**9
    for first in (0, 1):
        if first and seq[0] in loops:
            continue
        dp = {first: first}
        for x in seq[1:]:
            new = {}
            for prior, value in dp.items():
                new[0] = max(value, new.get(0, -10**9))
                if prior == 0 and x not in loops:
                    new[1] = max(value + 1, new.get(1, -10**9))
            dp = new
        for last, value in dp.items():
            if not (cyclic and first and last):
                best = max(best, value)
    return best


def graph_independence(p, target):
    nbr, loops = graph(p, target)
    visited = set()
    result = 0
    for root in range(p):
        if root in visited:
            continue
        todo = [root]
        component = set()
        while todo:
            x = todo.pop()
            if x in component:
                continue
            component.add(x)
            todo.extend(nbr[x] - component)
        visited.update(component)
        starts = sorted(x for x in component if len(nbr[x]) < 2)
        cyclic = not starts
        x = starts[0] if starts else root
        path = []
        while x not in path:
            path.append(x)
            nexts = sorted(y for y in nbr[x] if y not in path)
            if not nexts:
                break
            x = nexts[0]
        assert len(path) == len(component), (p, target, component, path)
        result += max_independent_path(path, cyclic, loops)
    return result


def brute_independence(p, target):
    nbr, loops = graph(p, target)
    best = 0
    for bits in range(1 << p):
        pop = bits.bit_count()
        if pop <= best or any(bits & (1 << v) for v in loops):
            continue
        if all(not (bits & (1 << i)) or all(not (bits & (1 << j)) for j in nbr[i]) for i in range(p)):
            best = pop
    return best


def theorem(p, target):
    d = order_projective(p, target)
    square = pow(target, (p - 1) // 2, p) == 1
    return (p - 3) // 2 if square and d % 2 == 0 else (p - 1) // 2


def exceptional_count(p):
    L = p - (1 if p % 4 == 1 else -1)
    odd = L
    while odd % 2 == 0:
        odd //= 2
    return (L // 2 - odd - 1) // 2


def main():
    checked = 0
    brute_checked = 0
    for p in primes_below(200):
        spectrum = Counter()
        for target in range(1, p):
            value = graph_independence(p, target)
            expected = theorem(p, target)
            assert value == expected, (p, target, value, expected)
            assert order_projective(p, target) > 1
            spectrum[value] += 1
            if p <= 17:
                assert brute_independence(p, target) == value
                brute_checked += 1
            checked += 1
        assert spectrum[(p - 3) // 2] == exceptional_count(p), (p, spectrum)
        assert spectrum[(p - 1) // 2] == p - 1 - exceptional_count(p)
    print(f"VERIFY_OK prime_fields={len(primes_below(200))} target_cases={checked} exhaustive_bitmasks={brute_checked}")


if __name__ == "__main__":
    main()
