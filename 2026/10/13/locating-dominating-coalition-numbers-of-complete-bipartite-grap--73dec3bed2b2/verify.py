from functools import lru_cache

def vertices(m,n):
    return tuple(range(m+n))

def neigh(m,n,v):
    return set(range(m,m+n)) if v < m else set(range(m))

def is_ld(m,n,S):
    S=set(S); V=set(vertices(m,n)); outside=V-S
    traces=[]
    for v in outside:
        t=neigh(m,n,v)&S
        if not t:
            return False
        traces.append(frozenset(t))
    return len(traces)==len(set(traces))

def partitions(seq):
    seq=tuple(seq)
    if not seq:
        yield ()
        return
    first=seq[0]
    for rest in partitions(seq[1:]):
        yield (frozenset((first,)),)+rest
        for i in range(len(rest)):
            yield rest[:i]+(rest[i]|{first},)+rest[i+1:]

def is_ldc_partition(m,n,P):
    if any(is_ld(m,n,B) for B in P):
        return False
    for i,A in enumerate(P):
        if not any(i!=j and is_ld(m,n,A|B) for j,B in enumerate(P)):
            return False
    return True

def exact_CL(m,n):
    best=0
    for P in partitions(vertices(m,n)):
        if len(P)>best and is_ldc_partition(m,n,P):
            best=len(P)
    return best

def predicted(m,n):
    if (m,n)==(1,1):
        return 0
    if (m,n)==(2,2):
        return 4
    return 3

def construction(m,n):
    V=set(vertices(m,n))
    if (m,n)==(1,1):
        return None
    if (m,n)==(2,2):
        return tuple(frozenset((v,)) for v in sorted(V))
    if (m,n)==(1,2):
        return tuple(frozenset((v,)) for v in sorted(V))
    # choose two vertices from a shore of size at least 3
    if n>=3:
        y1,y2=m,m+1
    else:
        y1,y2=0,1
    return (frozenset(V-{y1,y2}),frozenset((y1,)),frozenset((y2,)))

profiles=0
for total in range(2,10):
    for m in range(1,total):
        n=total-m
        if m>n:
            continue
        got=exact_CL(m,n)
        exp=predicted(m,n)
        assert got==exp,(m,n,got,exp)
        profiles+=1

construction_profiles=0
for m in range(1,41):
    for n in range(m,41):
        P=construction(m,n)
        if P is None:
            assert (m,n)==(1,1)
        else:
            assert is_ldc_partition(m,n,P),(m,n,P)
            assert len(P)==predicted(m,n)
        construction_profiles+=1

# Directly verify the structural LD characterization used in the proof.
ld_characterization_checks=0
for m in range(2,8):
    for n in range(m,8):
        V=vertices(m,n)
        for mask in range(1<<(m+n)):
            S={v for v in V if mask>>v&1}
            omitted_x=sum(v<m and v not in S for v in V)
            omitted_y=sum(v>=m and v not in S for v in V)
            expected=(omitted_x<=1 and omitted_y<=1)
            assert is_ld(m,n,S)==expected,(m,n,S)
            ld_characterization_checks+=1

print('ALL CHECKS PASSED')
print(f'exhaustive_biclique_profiles_order_le_9={profiles}')
print(f'construction_profiles_m_n_le_40={construction_profiles}')
print(f'ld_characterization_subset_checks={ld_characterization_checks}')
