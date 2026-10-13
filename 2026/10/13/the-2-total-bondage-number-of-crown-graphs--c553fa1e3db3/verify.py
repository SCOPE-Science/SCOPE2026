from itertools import combinations, product

def crown_edges(n):
    return [(i,j) for i in range(n) for j in range(n) if i != j]

def no_isolates(n,E):
    da=[0]*n; db=[0]*n
    for i,j in E:
        da[i]+=1; db[j]+=1
    return all(da) and all(db)

def shore_dom(n,E,side):
    target=[set() for _ in range(n)]
    if side=='A':
        for i,j in E: target[j].add(i)
    else:
        for i,j in E: target[i].add(j)
    for k in range(1,n+1):
        for S in combinations(range(n),k):
            S=set(S)
            if all(S & target[v] for v in range(n)):
                return k
    raise AssertionError('isolated target')

def gamma_t(n,E):
    return shore_dom(n,E,'A') + shore_dom(n,E,'B')

def construction(n,r=0,c=1):
    F={(r,j) for j in range(n) if j not in (r,c)}
    F |= {(i,c) for i in range(n) if i not in (r,c)}
    F.add((c,r))
    return F

def exhaustive_deletions():
    total=0
    by_n={}
    for n in range(3,5):
        E0=crown_edges(n); threshold=2*n-3; here=0
        assert gamma_t(n,E0)==4
        for k in range(threshold):
            for idx in combinations(range(len(E0)),k):
                I=set(idx); E=[e for z,e in enumerate(E0) if z not in I]
                if no_isolates(n,E):
                    here += 1
                    assert gamma_t(n,E)==4, (n,k,idx)
        by_n[n]=here; total += here
    return total,by_n

def exhaustive_pair_cover_lemma():
    total=0; minima={}
    for n in range(3,5):
        opts=[]
        for j in range(n):
            other=[x for x in range(n) if x!=j]
            cur=[]
            for mask in range(1<<(n-1)):
                S={j}
                for t,x in enumerate(other):
                    if (mask>>t)&1: S.add(x)
                if len(S)<n: cur.append(S)
            opts.append(cur)
        pairs=[set(p) for p in combinations(range(n),2)]
        mn=None; count=0
        for fam in product(*opts):
            if all(any(P<=S for S in fam) for P in pairs):
                count+=1
                d=sum(len(S)-1 for S in fam)
                assert d>=2*n-3, (n,d,fam)
                mn=d if mn is None else min(mn,d)
        total+=count; minima[n]=mn
    return total,minima

def construction_checks():
    for n in range(3,41):
        E0=crown_edges(n); F=construction(n)
        assert len(F)==2*n-3
        E=[e for e in E0 if e not in F]
        assert no_isolates(n,E)
        # Direct structural witness: both shore domination numbers are exactly three.
        r,c,x=0,1,2
        A={r,c,x}; B={c,r,x}
        assert all(any((i,j) in E for i in A) for j in range(n))
        assert all(any((i,j) in E for j in B) for i in range(n))
        # Every pair on A fails to dominate B; same on B by transpose symmetry.
        for p,q in combinations(range(n),2):
            assert any((p,j) not in E and (q,j) not in E for j in range(n))
            assert any((i,p) not in E and (i,q) not in E for i in range(n))
    return 38

def main():
    dtotal,by_n=exhaustive_deletions()
    ltotal,minima=exhaustive_pair_cover_lemma()
    crange=construction_checks()
    print('ALL CHECKS PASSED')
    print(f'exhaustive_noisolate_deletion_cases={dtotal}; by_n={by_n}')
    print(f'pair_cover_families={ltotal}; minima={minima}')
    print(f'construction_orders=3..40; count={crange}')

if __name__=='__main__': main()
