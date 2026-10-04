from itertools import product


def has_sdr(family, right):
    family=[set(s) for s in family]
    used=set()
    order=sorted(range(len(family)), key=lambda i: len(family[i]))
    def rec(j):
        if j==len(order):
            return True
        i=order[j]
        for y in family[i]:
            if y in right and y not in used:
                used.add(y)
                if rec(j+1):
                    return True
                used.remove(y)
        return False
    return rec(0)


def hall_ok(family):
    m=len(family)
    for mask in range(1,1<<m):
        U=set()
        k=0
        for i in range(m):
            if mask>>i & 1:
                k+=1
                U.update(family[i])
        if len(U)<k:
            return False
    return True

# Exhaustive finite Hall replay for all families with at most three left
# vertices and at most four right vertices.
for m in range(1,4):
    for n in range(1,5):
        right=tuple(range(n))
        subsets=[{y for y in right if mask>>y & 1} for mask in range(1<<n)]
        for choice in product(range(len(subsets)), repeat=m):
            fam=[subsets[i] for i in choice]
            assert has_sdr(fam,set(right)) == hall_ok(fam)

# Finite truncations of the infinite-row boundary example.
# D={0,...,N}; R(0)={1,...,N}, R(i)={i} for i>0.
# After deletion of b=0, all proper subsets satisfy Hall, while the full
# left set is deficient by one. As N grows, this sole witness escapes to
# infinity, matching the infinite counterexample in the proof.
for N in range(2,9):
    D=set(range(N+1))
    rows={0:set(range(1,N+1))}
    for i in range(1,N+1):
        rows[i]={i}
    for mask in range(1,1<<(N+1)):
        S={i for i in D if mask>>i & 1}
        neigh=set().union(*(rows[i]-{0} for i in S)) if S else set()
        deficient=len(neigh)<len(S)
        assert deficient == (S==D)

print("VERIFY_OK")
