from functools import lru_cache
from itertools import combinations

def kab(a,b):
    n=a+b; E=set()
    for i in range(a):
        for j in range(a,n): E.add((i,j))
    return n,E

def adj(E,i,j):
    return (min(i,j),max(i,j)) in E if i!=j else False

def is_complete_bipartite(n,E):
    # direct recognition via all two-colorings induced by a nontrivial component pattern
    if not E: return False
    # relation R = equality or nonadjacency must be equivalence; and at most 2 classes
    for x in range(n):
      for y in range(n):
       for z in range(n):
        Rxy=(x==y or not adj(E,x,y)); Ryz=(y==z or not adj(E,y,z)); Rxz=(x==z or not adj(E,x,z))
        if Rxy and Ryz and not Rxz: return False
    # no triangle
    for x,y,z in combinations(range(n),3):
        if adj(E,x,y) and adj(E,x,z) and adj(E,y,z): return False
    return True

def beta(n,E):
    if not E: return False
    for x in range(n):
      for y in range(n):
       for z in range(n):
        Rxy=(x==y or not adj(E,x,y)); Ryz=(y==z or not adj(E,y,z)); Rxz=(x==z or not adj(E,x,z))
        if Rxy and Ryz and not Rxz: return False
    for x,y,z in combinations(range(n),3):
        if adj(E,x,y) and adj(E,x,z) and adj(E,y,z): return False
    return True

def dup_wins(n1,E1,n2,E2,q):
    @lru_cache(None)
    def rec(r,pairs):
        if r==0:return True
        d1=dict(pairs); d2={b:a for a,b in pairs}
        for side in (0,1):
            N=n1 if side==0 else n2
            for u in range(N):
                if (u in d1) if side==0 else (u in d2): continue
                ok=False
                M=n2 if side==0 else n1
                for v in range(M):
                    if (v in d2) if side==0 else (v in d1): continue
                    a,b=(u,v) if side==0 else (v,u)
                    good=True
                    for aa,bb in pairs:
                        if adj(E1,a,aa)!=adj(E2,b,bb): good=False;break
                    if good and rec(r-1,tuple(sorted(pairs+((a,b),)))):
                        ok=True;break
                if not ok:return False
        return True
    return rec(q,tuple())

# rank-3 class axiom exhaustive through 5 vertices
cases=0
for n in range(1,6):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        E={pairs[i] for i in range(len(pairs)) if mask>>i & 1}
        assert beta(n,E)==is_complete_bipartite(n,E)
        cases+=1
# lower-bound competitor: Duplicator survives b rounds on K_ab vs K_a,b+1
low=0
for a in range(1,5):
  for b in range(a,5):
    n1,E1=kab(a,b); n2,E2=kab(a,b+1)
    assert dup_wins(n1,E1,n2,E2,b)
    assert not dup_wins(n1,E1,n2,E2,b+1)
    low+=1
print(f'VERIFY_OK class_cases={cases} lower_pairs={low}')
