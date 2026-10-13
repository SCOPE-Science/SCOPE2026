from itertools import product

ZERO = -1
VALUES = (ZERO, 0, 1)
PAIRS = ((0,0),(0,1),(1,0),(1,1))

def q(table, a, b):
    if a == ZERO or b == ZERO:
        return ZERO
    return table[2*a+b]

def self_distributive(table):
    for a,b,c in product((0,1), repeat=3):
        lhs = q(table, q(table,a,b), c)
        rhs = q(table, q(table,a,c), q(table,b,c))
        if lhs != rhs:
            return False
    return True

def swap_value(v):
    return ZERO if v == ZERO else 1-v

def swap_table(table):
    out=[]
    for a,b in PAIRS:
        sa,sb=1-a,1-b
        out.append(swap_value(q(table,sa,sb)))
    return tuple(out)

solutions=[t for t in product(VALUES, repeat=4) if self_distributive(t)]
assert len(solutions)==21
assert all(swap_table(t) in solutions for t in solutions)

seen=set(); split_orbits=[]
for t in solutions:
    if t in seen:
        continue
    orb={t,swap_table(t)}
    seen |= orb
    split_orbits.append(orb)
assert len(split_orbits)==13

split_counit=[orb for orb in split_orbits if all(ZERO not in t for t in orb)]
assert len(split_counit)==6

fixed=[t for t in solutions if swap_table(t)==t]
assert len(fixed)==5
nonsplit_counit=[t for t in fixed if ZERO not in t]
assert len(nonsplit_counit)==3

print(f"split_labeled={len(solutions)}")
print(f"split_isomorphism_classes={len(split_orbits)}")
print(f"split_counit_multiplicative_classes={len(split_counit)}")
print(f"nonsplit_descent_classes={len(fixed)}")
print(f"nonsplit_counit_multiplicative_classes={len(nonsplit_counit)}")
print(f"etale_total={len(split_orbits)+len(fixed)}")
print(f"etale_counit_multiplicative_total={len(split_counit)+len(nonsplit_counit)}")
print("CHECK_OK")
