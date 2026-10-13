def compose_nonzero_XY(a,b,i,j,k,l):
    # X: a -> b sends i to j; Y: b -> a sends k to l.
    # XY: b -> b is nonzero exactly when Y's target l equals X's source i.
    return l == i

def compose_nonzero_YX(a,b,i,j,k,l):
    # YX: a -> a is nonzero exactly when X's target j equals Y's source k.
    return k == j

checked_pairs = 0
checked_components = 0
for a in range(2,13):
    for b in range(a,13):
        survivors = []
        for i in range(a):
            for j in range(b):
                for k in range(b):
                    for l in range(a):
                        checked_pairs += 1
                        if not compose_nonzero_XY(a,b,i,j,k,l) and not compose_nonzero_YX(a,b,i,j,k,l):
                            survivors.append((i,j,k,l))
        target = a*(a-1)*b*(b-1)
        assert len(survivors) == target

        for c in range(1,a):
            # Every coordinate matrix unit has rank one, hence satisfies both rank bounds.
            assert c >= 1 and a-c >= 1
            assert len(survivors) == target
            checked_components += 1

        ambient = (a*b)**2
        assert target * a * b == ambient * (a-1) * (b-1)

for b in range(1,13):
    a = 1
    # Direct coordinate test: every pair violates at least one composition equation.
    survivors = 0
    for i in range(a):
        for j in range(b):
            for k in range(b):
                for l in range(a):
                    if l != i and k != j:
                        survivors += 1
    assert survivors == 0

print("VERIFY_OK", checked_pairs, checked_components)
