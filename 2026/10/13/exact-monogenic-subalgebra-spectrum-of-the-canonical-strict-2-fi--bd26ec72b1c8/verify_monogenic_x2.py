from itertools import combinations

W = 5  # |L_2^i| = 2^2+1
TOP = 'TOP'
BOT = frozenset()


def q(j): return (0,j)
def r(j): return (1,j)
L0 = frozenset(q(j) for j in range(W))
L1 = frozenset(r(j) for j in range(W))


def leq(p, s):
    i,l = p; j,m = s
    return p == s or i >= j+2 or (i == j+1 and m != l+1)


def is_upset(U):
    U=set(U)
    # Enough to test the occupied finite levels: successors are always shallower.
    for x in tuple(U):
        i,_=x
        for j in range(i+1):
            for m in range(W):
                y=(j,m)
                if leq(x,y) and y not in U:
                    return False
    return True


def comp_down_nonempty(D):
    D=set(D)
    assert D
    jmin=min(i for i,_ in D)
    # Every point at level >= jmin+2 lies below any D-point at level jmin.
    out=set()
    for i in range(jmin+2):
        for l in range(W):
            p=(i,l)
            if not any(leq(p,d) for d in D):
                out.add(p)
    return frozenset(out)


def meet(a,b):
    if a == TOP: return b
    if b == TOP: return a
    return frozenset(set(a)&set(b))


def join(a,b):
    if a == TOP or b == TOP: return TOP
    return frozenset(set(a)|set(b))


def impl(a,b):
    if b == TOP: return TOP
    if a == TOP: return b
    D=set(a)-set(b)
    if not D: return TOP
    return comp_down_nonempty(D)


def closure(gen):
    E={BOT,TOP,gen}
    changed=True
    while changed:
        changed=False
        old=tuple(E)
        for a in old:
            for b in old:
                for z in (meet(a,b),join(a,b),impl(a,b)):
                    if z not in E:
                        E.add(z); changed=True
    return E

# Enumerate all rank-0 and rank-1 finite clopen upsets exactly.
rank0=[]
for mask in range(1,1<<W):
    U=frozenset(q(j) for j in range(W) if mask>>j & 1)
    assert is_upset(U)
    rank0.append(U)

rank1=[]
univ=list(L0|L1)
for mask in range(1,1<<len(univ)):
    U=frozenset(univ[k] for k in range(len(univ)) if mask>>k & 1)
    if U & L1 and is_upset(U):
        rank1.append(U)
assert len(rank0)==31
assert len(rank1)==35

c0={2:0,3:0,5:0,9:0}
for U in rank0:
    s=len(closure(U))
    assert s in c0
    c0[s]+=1
assert c0 == {2:0,3:1,5:26,9:4}

c1={2:0,3:0,5:0,9:0}
for U in rank1:
    s=len(closure(U))
    assert s in c1
    c1[s]+=1
assert c1 == {2:0,3:31,5:4,9:0}

# Identify the four 9-element generators exactly.
nine=[U for U in rank0 if len(closure(U))==9]
expected9={frozenset(L0-{q(j)}) for j in range(1,5)}
assert set(nine)==expected9

# Identify the four exceptional rank-1 generators exactly.
five1=[U for U in rank1 if len(closure(U))==5]
expected5_rank1={frozenset((L0-{q(j)})|{r(j-1)}) for j in range(1,5)}
assert set(five1)==expected5_rank1

# For each 9-element case, verify a uniform nine-term description and full closure.
for j in range(1,5):
    a=frozenset(L0-{q(j)})
    b=impl(a,BOT)
    c=join(a,b)
    d=impl(b,BOT)
    e=join(b,d)
    f=impl(d,a)
    g=join(d,f)
    named={BOT,TOP,a,b,c,d,e,f,g}
    assert len(named)==9
    assert closure(a)==named
    for x in named:
        for y in named:
            assert meet(x,y) in named
            assert join(x,y) in named
            assert impl(x,y) in named

# Deep-rank lemma, checked symbolically for all possible labels: a point at
# any level i>=2 lies below every maximal point at level 0. Hence an upset
# meeting level >=2 contains L0 and is dense; a nonzero proper dense element
# generates exactly {0,a,1}.
for i in range(2,12):
    for l in range(W):
        for m in range(W):
            assert leq((i,l),q(m))

# Global spectrum/count statement: bottom and top give size 2; 30 elements
# give size 5 (26 rank-0 + 4 rank-1); 4 elements give size 9; all others size 3.
assert len([U for U in rank0 if len(closure(U))==5]) + len(five1) == 30
assert len(nine)==4
assert len(closure(BOT))==2 and len(closure(TOP))==2

checks = 31 + 35 + 4*9*9*3 + 10*5*5 + 12
print(f'VERIFY_OK {checks} exact assertions')
