"""Independent direct-vertex EF-type recursion and comparison with gap recursion."""
from functools import lru_cache
from verify_symbolic import typ

_ids = {}
def intern(key):
    if key not in _ids:
        _ids[key] = len(_ids) + 1
    return _ids[key]

@lru_cache(None)
def direct_type(order, distance, choices, depth):
    labels = (0, distance) + choices
    atomic = tuple((a == b, (a + 1) % order == b)
                   for a in labels for b in labels)
    if depth == 0:
        return intern((0, atomic))
    successors = frozenset(direct_type(order, distance, choices + (x,), depth - 1)
                          for x in range(order))
    return intern((depth, atomic, successors))

for depth, maximum_order in [(0, 12), (1, 14), (2, 14), (3, 20), (4, 12)]:
    actual_to_symbolic = {}
    symbolic_to_actual = {}
    cases = 0
    for order in range(2, maximum_order + 1):
        for distance in range(1, order):
            actual = direct_type(order, distance, (), depth)
            symbolic = typ(((0,), (1,)), (distance, order - distance), depth)
            if actual in actual_to_symbolic:
                assert actual_to_symbolic[actual] == symbolic
            else:
                actual_to_symbolic[actual] = symbolic
            if symbolic in symbolic_to_actual:
                assert symbolic_to_actual[symbolic] == actual
            else:
                symbolic_to_actual[symbolic] = actual
            cases += 1
    print(f'DIRECT_CROSSCHECK_OK rank={depth} orders=2..{maximum_order} cases={cases}')
print('INDEPENDENT_DIRECT_CHECKS_OK')
