"""Exact integer regression tests for the shift-three Euler totient map."""
from math import isqrt

LIMIT = 200_000
PHI_LIMIT = LIMIT + 10
phi = list(range(PHI_LIMIT + 1))
for p in range(2, PHI_LIMIT + 1):
    if phi[p] == p:
        for j in range(p, PHI_LIMIT + 1, p):
            phi[j] -= phi[j] // p

def f(n):
    assert 1 <= n <= PHI_LIMIT
    return phi[n] + 3

transition = {5: 7, 7: 9, 9: 9, 11: 13, 13: 15, 15: 11,
              17: 19, 19: 21, 21: 15, 23: 25, 25: 23}
for x, y in transition.items():
    assert f(x) == y, (x, y, f(x))
assert f(1) == f(2) == 4 and f(4) == 5

# A composite value is determined by the presence of a proper factor.
def composite(n):
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return True
    return False

# Check every local descent assertion in the proof over a finite range.
prime_checks = 0
composite_checks = 0
for n in range(27, 50_000, 2):
    if composite(n):
        assert f(n) < n
        composite_checks += 1
    else:
        prime_checks += 1
        assert f(n) == n + 2
        if composite(n + 2):
            assert f(f(n)) < n
        else:
            assert (n + 4) % 3 == 0
            assert f(f(f(n))) < n

# Exhaustively check each small starting state reaches one of three cycles.
cycles = {(9,), (11, 13, 15), (23, 25)}
visited = [False] * (LIMIT + 1)
max_path_length = 0
for n in range(1, LIMIT + 1):
    seen = {}
    path = []
    v = n
    for _ in range(LIMIT + 1):
        if v in seen:
            cycle = tuple(path[seen[v]:])
            rotations = {cycle[i:] + cycle[:i] for i in range(len(cycle))}
            assert rotations & cycles, (n, cycle)
            max_path_length = max(max_path_length, len(path))
            break
        assert 1 <= v <= PHI_LIMIT, (n, v)
        seen[v] = len(path)
        path.append(v)
        v = f(v)
    else:
        raise AssertionError(('No cycle', n))
print('VERIFY_OK')
print(f'exhaustive_starting_values=1..{LIMIT}=PASS')
print(f'composite_descent_checks={composite_checks}=PASS')
print(f'prime_two_or_three_step_descent_checks={prime_checks}=PASS')
print(f'finite_transition_table_states={len(transition)}=PASS')
print(f'max_path_length_within_test={max_path_length}')
print('all_detected_cycles=(9);(11,13,15);(23,25)')
print('finite_tests_supplement_unrestricted_symbolic_proof')
