from itertools import product


def pair_pass(a,b,c,e):
    # Exact two-generator criterion for (x^a y^b, z^c y^e).
    d, f = a+b, c+e
    if d < f:
        return a == 1 and b <= e
    if f < d:
        return c == 1 and e <= b
    # equal degrees: the lcm must have degree d+1
    return a + c + max(b,e) == d + 1


def invariant_pass(data):
    # data is [(a_i,b_i),...]
    exc = [i for i,(a,b) in enumerate(data) if a > 1]
    if len(exc) > 1:
        return False
    if not exc:
        return True
    e = exc[0]
    return all(data[e][1] >= b for i,(a,b) in enumerate(data) if i != e)


def all_pairs_pass(data):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            a,b = data[i]
            c,e = data[j]
            if not pair_pass(a,b,c,e):
                return False
    return True


def canonical_order(data):
    exc = [i for i,(a,b) in enumerate(data) if a > 1]
    if not exc:
        return sorted(range(len(data)), key=lambda i: data[i][1])
    e = exc[0]
    rest = sorted((i for i in range(len(data)) if i != e), key=lambda i: data[i][1])
    return rest + [e]


def quotient_exponents(ui, uj):
    # u_i=x_i^a y^b and u_j=x_j^c y^e, distinct leaves.
    a,b = ui
    c,e = uj
    return a, max(b-e,0)


def linear_quotients_replay(data):
    if not invariant_pass(data):
        return False
    order = canonical_order(data)
    prev=[]
    last_degree=-1
    for j in order:
        a,b=data[j]
        deg=a+b
        assert deg >= last_degree
        last_degree=deg
        for i in prev:
            qa,qy=quotient_exponents(data[i],data[j])
            # Each quotient is exactly the distinct leaf variable x_i.
            assert (qa,qy)==(1,0)
        prev.append(j)
    return True

# Exhaust every two-generator exponent choice in a useful box and compare
# the lcm/intersection criterion with the invariant statement specialized to s=2.
pair_cases=0
for a,b,c,e in product(range(1,7), repeat=4):
    pair_cases += 1
    assert pair_pass(a,b,c,e) == invariant_pass([(a,b),(c,e)])

# Exhaust star exponent data up to four leaves.  The global invariant is
# equivalent to all exact two-leaf restrictions, and every passing case has
# the asserted nondecreasing-degree linear-quotient order.
star_cases=0
for s in range(1,5):
    choices=list(product(range(1,4), repeat=2))
    for data in product(choices, repeat=s):
        star_cases += 1
        assert invariant_pass(data) == all_pairs_pass(data)
        if invariant_pass(data):
            assert linear_quotients_replay(data)

# Boundary witnesses.
assert invariant_pass([(1,1),(1,7),(1,3)])
assert invariant_pass([(1,2),(2,5),(1,4)])
assert not invariant_pass([(2,1),(1,5)])
assert not invariant_pass([(2,5),(3,5)])

print(f"PAIR_CASES={pair_cases}")
print(f"STAR_CASES={star_cases}")
print("CHECK_OK")
