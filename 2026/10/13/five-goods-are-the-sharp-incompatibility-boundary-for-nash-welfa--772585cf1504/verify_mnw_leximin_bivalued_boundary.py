from itertools import product
from collections import Counter, defaultdict
from math import factorial

VALUES=(1,2)
TYPES=((1,1),(1,2),(2,1),(2,2))


def mnw_key(u):
    pos=sum(x>0 for x in u)
    prodv=1
    for x in u:
        if x>0: prodv*=x
    return (pos,prodv)


def lex_key(u):
    return tuple(sorted(u))


def alloc_utils(v1,v2,bits):
    # bit 0 -> agent 1; bit 1 -> agent 2
    u1=sum(v1[g] for g,b in enumerate(bits) if b==0)
    u2=sum(v2[g] for g,b in enumerate(bits) if b==1)
    return (u1,u2)


def direct_profile(v1,v2):
    m=len(v1)
    alls=[]
    for bits in product((0,1), repeat=m):
        u=alloc_utils(v1,v2,bits)
        alls.append((bits,u))
    mk=max(mnw_key(u) for _,u in alls)
    lk=max(lex_key(u) for _,u in alls)
    M={bits for bits,u in alls if mnw_key(u)==mk}
    L={bits for bits,u in alls if lex_key(u)==lk}
    return M,L,tuple(sorted(next(u for bits,u in alls if bits in M))),tuple(sorted(next(u for bits,u in alls if bits in L)))


def comp_counts(n,k):
    if k==1:
        yield (n,); return
    for x in range(n+1):
        for rest in comp_counts(n-x,k-1):
            yield (x,)+rest


def multinomial(c):
    m=sum(c); z=factorial(m)
    for x in c: z//=factorial(x)
    return z


def count_profile(c):
    # independent route: choose x_t goods of each type to agent 1, weighted by combinations only for optimizer multiplicities
    a,b,c2,d=c
    entries=[]
    from math import comb
    for xa in range(a+1):
      for xb in range(b+1):
       for xc in range(c2+1):
        for xd in range(d+1):
          u1=xa + xb + 2*xc + 2*xd
          u2=(a-xa) + 2*(b-xb) + (c2-xc) + 2*(d-xd)
          mult=comb(a,xa)*comb(b,xb)*comb(c2,xc)*comb(d,xd)
          entries.append(((xa,xb,xc,xd),(u1,u2),mult))
    mk=max(mnw_key(u) for _,u,_ in entries)
    lk=max(lex_key(u) for _,u,_ in entries)
    M=[e for e in entries if mnw_key(e[1])==mk]
    L=[e for e in entries if lex_key(e[1])==lk]
    Mstates={x for x,_,_ in M}; Lstates={x for x,_,_ in L}
    return {
        'disjoint': Mstates.isdisjoint(Lstates),
        'mnw_utility': tuple(sorted(M[0][1])),
        'lex_utility': tuple(sorted(L[0][1])),
        'mnw_allocs': sum(mult for _,_,mult in M),
        'lex_allocs': sum(mult for _,_,mult in L),
    }


def swap_agents(c):
    a,b,c2,d=c
    return (a,c2,b,d)


def canonical(c):
    return min(c,swap_agents(c))

# Route A: all labeled profiles.
direct_counts={}
relation_counts={}
direct_m5=[]
for m in range(1,6):
    bad=0
    relation=Counter()
    mnw_hist=Counter(); lex_hist=Counter(); util_hist=Counter(); type_hist=Counter()
    for flat in product(VALUES, repeat=2*m):
        v1=flat[:m]; v2=flat[m:]
        M,L,mu,lu=direct_profile(v1,v2)
        if M==L:
            relation['equal']+=1
        elif M < L:
            relation['MNW_proper_subset_leximin']+=1
        elif L < M:
            relation['leximin_proper_subset_MNW']+=1
        elif M & L:
            relation['nonnested_overlap']+=1
        else:
            relation['disjoint']+=1
        if M.isdisjoint(L):
            bad+=1
            if m==5:
                mnw_hist[len(M)]+=1; lex_hist[len(L)]+=1; util_hist[(mu,lu)]+=1
                c=tuple(Counter(zip(v1,v2))[t] for t in TYPES)
                type_hist[c]+=1
                direct_m5.append((v1,v2,M,L,mu,lu,c))
    direct_counts[m]=bad
    relation_counts[m]=relation
    if m==5:
        direct_m5_stats=(mnw_hist,lex_hist,util_hist,type_hist)

assert direct_counts=={1:0,2:0,3:0,4:0,5:100}
assert relation_counts=={
  1:Counter({'equal':4}),
  2:Counter({'equal':16}),
  3:Counter({'equal':56,'leximin_proper_subset_MNW':8}),
  4:Counter({'equal':240,'leximin_proper_subset_MNW':16}),
  5:Counter({'equal':892,'leximin_proper_subset_MNW':32,'disjoint':100}),
}

# Route B: independent count-vector reduction and multinomial reconstruction.
count_counts={}
count_bad_vectors={}
for m in range(1,6):
    total=0; badvec=[]
    for c in comp_counts(m,4):
        r=count_profile(c)
        if r['disjoint']:
            total += multinomial(c)
            badvec.append((c,r))
    count_counts[m]=total
    count_bad_vectors[m]=badvec
assert count_counts==direct_counts

expected_vectors=[
    (0,0,4,1),(0,1,4,0),(0,4,0,1),(0,4,1,0),
    (1,0,3,1),(1,1,3,0),(1,3,0,1),(1,3,1,0),
]
assert [c for c,_ in count_bad_vectors[5]]==expected_vectors

# Every labeled profile maps to one of those vectors with the correct multinomial count.
_,_,util_hist,type_hist=direct_m5_stats
assert set(type_hist)==set(expected_vectors)
for c in expected_vectors:
    assert type_hist[c]==multinomial(c)

# Four classes up to agent swap and good relabeling.
classes=Counter()
for c in expected_vectors:
    classes[canonical(c)] += multinomial(c)
assert classes==Counter({(1,0,3,1):40,(1,1,3,0):40,(0,0,4,1):10,(0,1,4,0):10})
assert sum(classes.values())==100

# All utility profiles and optimizer multiplicities.
assert util_hist==Counter({((3,6),(4,4)):100})
mnw_hist,lex_hist,_,_=direct_m5_stats
assert mnw_hist==Counter({1:80,4:20})
assert lex_hist==Counter({3:80,6:20})

# Structural formula for canonical classes: (a,b,4-a,1-b), a,b in {0,1}.
assert set(classes)=={(a,b,4-a,1-b) for a in (0,1) for b in (0,1)}
for c in classes:
    r=count_profile(c)
    assert r['mnw_utility']==(3,6)
    assert r['lex_utility']==(4,4)

# Explicit canonical witness.
v1=(1,1,1,1,2)
v2=(1,2,2,2,1)
M,L,mu,lu=direct_profile(v1,v2)
assert mu==(3,6) and lu==(4,4) and M.isdisjoint(L)
assert M=={(0,1,1,1,0)}
assert L=={
    (0,0,1,1,0),
    (0,1,0,1,0),
    (0,1,1,0,0),
}

print('VERIFY_OK')
print('disjoint_counts_m1_to_m5', direct_counts)
print('relation_counts_m1_to_m5', {k:dict(v) for k,v in relation_counts.items()})
print('total_profiles_m5', 4**5)
print('m5_incidence', '25/256')
print('bad_type_vectors', expected_vectors)
print('canonical_classes', dict(sorted(classes.items())))
print('utility_profile_pair', 'MNW=(3,6), leximin=(4,4)')
print('mnw_optimizer_count_hist', dict(sorted(mnw_hist.items())))
print('leximin_optimizer_count_hist', dict(sorted(lex_hist.items())))
print('witness_MNW', sorted(M))
print('witness_leximin', sorted(L))
