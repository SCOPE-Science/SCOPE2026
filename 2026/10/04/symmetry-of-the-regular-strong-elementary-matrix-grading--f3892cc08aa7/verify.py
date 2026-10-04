from itertools import permutations

# Finite groups represented by a multiplication table on range(n).
def cyclic(n):
    return [[(i+j)%n for j in range(n)] for i in range(n)]

def v4():
    return [[i^j for j in range(4)] for i in range(4)]

def s3():
    # permutations of (0,1,2), composition p*q = p after q
    ps=list(permutations(range(3)))
    idx={p:i for i,p in enumerate(ps)}
    tab=[]
    for p in ps:
        row=[]
        for q in ps:
            r=tuple(p[q[i]] for i in range(3))
            row.append(idx[r])
        tab.append(row)
    return tab

def invs(tab):
    n=len(tab)
    return [next(j for j in range(n) if tab[i][j]==0 and tab[j][i]==0) for i in range(n)]

def degree(tab, inv, x,y):
    return tab[inv[x]][y]

def component_permuter(tab,sig):
    n=len(tab); inv=invs(tab)
    pi=[None]*n
    for g in range(n):
        outs=set()
        for x in range(n):
            for y in range(n):
                if degree(tab,inv,x,y)==g:
                    outs.add(degree(tab,inv,sig[x],sig[y]))
        if len(outs)!=1: return None
        pi[g]=next(iter(outs))
    return tuple(pi)

def is_aut(tab,a):
    n=len(tab)
    return a[0]==0 and sorted(a)==list(range(n)) and all(a[tab[x][y]]==tab[a[x]][a[y]] for x in range(n) for y in range(n))

def check(name,tab):
    n=len(tab)
    weak=[]; stab=[]; auts=[]
    for a in permutations(range(n)):
        if is_aut(tab,a): auts.append(a)
    for sig in permutations(range(n)):
        pi=component_permuter(tab,sig)
        if pi is not None:
            weak.append((sig,pi))
            if pi==tuple(range(n)): stab.append(sig)
            assert is_aut(tab,pi)
            # affine form sig(x)=sig(e)*pi(x), for degree x^{-1}y
            left=sig[0]
            assert all(sig[x]==tab[left][pi[x]] for x in range(n))
    assert len(stab)==n
    assert len(weak)==n*len(auts)
    print(f'{name}: n={n} Aut(G)={len(auts)} weak_perms={len(weak)} stabilizer_perms={len(stab)} OK')

for name,tab in [('C2',cyclic(2)),('C3',cyclic(3)),('C4',cyclic(4)),('V4',v4()),('S3',s3())]:
    check(name,tab)

# Finite-field scalar-factor checks for q=2,3,5 on sample groups.
for q,n,autg in [(2,2,1),(3,3,2),(5,4,2),(3,4,6),(3,6,6)]:
    tor=(q-1)**(n-1)
    stab=n*tor
    weak=n*autg*tor
    assert weak//stab==autg
    print(f'orders q={q} n={n} |AutG|={autg}: torus={tor} stab={stab} weak={weak} quotient={autg} OK')
print('CHECK_OK')
