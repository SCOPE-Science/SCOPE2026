#!/usr/bin/env python3
import itertools, math

def criterion(n,k):
    return (k-1)*math.ceil(n/k) >= n

def has_bounded_coloring(n,k,perms):
    m=math.ceil(n/k)
    counts=[0]*k
    def leaves(i,center):
        if i==n-1:
            return True
        forbidden=perms[i][center]
        for color in range(k):
            if color==forbidden or counts[color]>=m:
                continue
            counts[color]+=1
            if leaves(i+1,center):
                return True
            counts[color]-=1
        return False
    for center in range(k):
        counts[:] = [0]*k
        counts[center]=1
        if counts[center] <= m and leaves(0,center):
            return True
    return False

cover_cases=0
parameter_cases=0
for n in range(2,5):
    for k in range(1,5):
        want=criterion(n,k)
        parameter_cases+=1
        if k==1:
            all_good=False
            cover_cases+=1
        else:
            perms=list(itertools.permutations(range(k)))
            all_good=True
            for cover in itertools.product(perms, repeat=n-1):
                got=has_bounded_coloring(n,k,cover)
                cover_cases+=1
                if not got:
                    all_good=False
        assert all_good==want,(n,k,all_good,want)

arith_cases=0
cyclic_bad=0
for n in range(2,201):
    for k in range(1,201):
        m=math.ceil(n/k)
        arith_cases+=1
        if criterion(n,k):
            assert m*(k-1)-1 >= n-1
        else:
            if k==1:
                continue
            leaf_capacity=m*(k-1)-1
            assert leaf_capacity < n-1
            cyclic_bad+=1

good9=[k for k in range(1,11) if criterion(9,k)]
assert good9 == [4,6,7,8,10], good9
print(f"ALL CHECKS PASSED; exhaustive_plain_full_covers={cover_cases}; exhaustive_parameter_cases={parameter_cases}; arithmetic_cases={arith_cases}; cyclic_bad_cases={cyclic_bad}; star_order_range_exhaustive=2..4; k_range_exhaustive=1..4; arithmetic_n_k_range=2..200,1..200; good_k_for_n9={good9}")
