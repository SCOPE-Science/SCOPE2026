from itertools import combinations_with_replacement, permutations


def extension_signatures(m, second_order, t):
    # The first order is 0<...<m-1. second_order lists the same labels in
    # increasing second-order position. t_i is the first second-order column
    # related to row i; t_i=m means an empty final segment.
    colpos = {a:j for j,a in enumerate(second_order)}
    assert all(t[i] <= t[i+1] for i in range(m-1))
    assert all(colpos[i] < t[i] for i in range(m))  # irreflexivity
    sigs=set()
    for c in range(m+1):
        block=[i for i,x in enumerate(t) if x==c]
        for q in range(len(block)+1):
            true_block=set(block[:q])
            T=[]
            old_to_x=[]
            for i,x in enumerate(t):
                if x<c:
                    T.append(x); old_to_x.append(1)
                elif x>c:
                    T.append(x+1); old_to_x.append(0)
                else:
                    if i in true_block:
                        T.append(c); old_to_x.append(1)
                    else:
                        T.append(c+1); old_to_x.append(0)
            assert all(T[i] <= T[i+1] for i in range(m-1))
            for z in range(c+1,m+2):  # R(x,x) is false
                # R(x,a) for old labels a.
                x_to_old=[]
                for a in range(m):
                    j=colpos[a]
                    j2=j if j<c else j+1
                    x_to_old.append(int(j2>=z))
                for r in range(m+1):
                    seq=T[:r]+[z]+T[r:]
                    if all(seq[i] <= seq[i+1] for i in range(m)):
                        sig=(r,c,tuple(old_to_x),tuple(x_to_old))
                        sigs.add(sig)
    return sigs


def threshold_count(t):
    m=len(t)
    total=0
    for c in range(m+1):
        b=sum(x==c for x in t)
        l=sum(x<c for x in t)
        for q in range(b+1):
            total += 2*m-c-l+1-q
    return total


def closed_distinct(m):
    return (m+1)*(2*m+1)


def closed_total(m):
    return 2*(m+1)*(m+1)-1

# Algebraic/threshold replay: the count is independent of the threshold shape.
for m in range(0,9):
    vals=set()
    for t in combinations_with_replacement(range(m+1),m):
        vals.add(threshold_count(t))
    assert vals=={closed_distinct(m)}, (m,vals)

# Exhaustive replay over every valid finite base through five parameters.
base_counts=[]
for m in range(0,6):
    if m==0:
        bases=[((),())]
    else:
        bases=[]
        for second in permutations(range(m)):
            colpos={a:j for j,a in enumerate(second)}
            for t in combinations_with_replacement(range(m+1),m):
                if all(colpos[i] < t[i] for i in range(m)):
                    bases.append((second,t))
    target=closed_distinct(m)
    for second,t in bases:
        sigs=extension_signatures(m,second,t)
        assert len(sigs)==target, (m,second,t,len(sigs),target)
    base_counts.append(len(bases))

expected_distinct=[closed_distinct(m) for m in range(6)]
expected_total=[closed_total(m) for m in range(6)]
assert expected_distinct == [1,6,15,28,45,66]
assert expected_total == [1,7,17,31,49,71]
print('valid_bases_m0_to_m5=',base_counts)
print('distinct_point_types_m0_to_m5=',expected_distinct)
print('all_1_types_m0_to_m5=',expected_total)
print('VERIFY_OK')
