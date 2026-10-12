from itertools import combinations

def intervals(vertex_count):
    return [(p,q) for p in range(vertex_count) for q in range(p, vertex_count)]

def rank_data(vertex_count, chosen):
    d = [0]*vertex_count
    for p,q in chosen:
        for v in range(p,q+1):
            d[v] += 1
    r = {}
    for i in range(vertex_count):
        for j in range(i+1, vertex_count):
            r[i,j] = sum(1 for p,q in chosen if p <= i and q >= j)
    return d,r

def arrow_coordinate_satisfies(vertex_count, r, arrow):
    # Coordinate representation has rank 1 on this direct arrow and zero on all other arrows.
    for i in range(vertex_count):
        for j in range(i+1, vertex_count):
            actual = 1 if (j == i+1 and i == arrow) else 0
            if actual > r[i,j]:
                return False
    return True

representations = arrow_type_checks = rank_condition_checks = 0
weighted_coordinate_points = 0

for vertex_count in range(2, 6):
    ints = intervals(vertex_count)
    # Exhaust every 0/1 interval-multiplicity representation.
    for mask in range(1, 1 << len(ints)):
        chosen = [ints[k] for k in range(len(ints)) if (mask >> k) & 1]
        d,r = rank_data(vertex_count, chosen)
        # Ignore zero-dimensional vertices only to keep projective arrow spaces meaningful.
        if any(x == 0 for x in d):
            continue
        direct = 0
        formula = 0
        for a in range(vertex_count-1):
            ok = arrow_coordinate_satisfies(vertex_count, r, a)
            arrow_type_checks += 1
            rank_condition_checks += vertex_count*(vertex_count-1)//2
            assert ok == (r[a,a+1] > 0)
            if ok:
                direct += d[a]*d[a+1]
            if r[a,a+1] > 0:
                formula += d[a]*d[a+1]
        assert direct == formula
        weighted_coordinate_points += direct
        representations += 1

# Explicit examples.
d,r = rank_data(3, [(0,2)])
assert d == [1,1,1]
assert r[0,1] == r[1,2] == r[0,2] == 1
assert sum(d[i]*d[i+1] for i in range(2) if r[i,i+1] > 0) == 2

d,r = rank_data(3, [(0,1),(1,2)])
assert r[0,1] == r[1,2] == 1 and r[0,2] == 0
assert sum(d[i]*d[i+1] for i in range(2) if r[i,i+1] > 0) == 4

print('VERIFY_OK', representations, arrow_type_checks, rank_condition_checks, weighted_coordinate_points)
