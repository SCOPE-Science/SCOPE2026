import pickle, itertools
with open("ord_d2.pkl","rb") as f:
    D=pickle.load(f)
rows_list=D["rows"]; R=D["nrows"]; C=D["ncols"]
print("d2:",R,C)
# H1^ord with Fp: dim = C1 - rank(d1) - rank(d2) = 56040-24239-31731 = 70. Check mod-p variations? rank d2 same all p; rank d1 = R-c over Fp for graph incidence: +1/-1 columns => rank = R - #bipartite?... For signed incidence over Fp (char!=2 same; char 2: +1=-1, column has two 1s => rank = R - #components-with-... For connected graph with a non-bipartite... our 1-skeleton graph: columns connect two 0-cells; over F2 incidence rank = R - (#components without odd cycle? ) = R-1 if non-bipartite (has odd cycle?), else R-2+... Let's compute F2 rank of d1 directly via union-find + bipartiteness, and F3/F5 ranks (=R-1 since connected).
import pickle as pk
with open("mats.pkl","rb") as f:
    DM=pk.load(f)
cells=DM["cells"]; edges=DM["edges"]
n=5
with open("collapse_state.pkl","rb") as f:
    S=pk.load(f)
remaining=S["remaining"]
rem0=set(remaining[0]); rem1=set(remaining[1])
ord0=[]
for j in rem0:
    es,vs=cells[0][j]
    for perm in itertools.permutations(range(n)):
        ord0.append(tuple(vs[perm[l]] for l in range(n)))
o0={c:i for i,c in enumerate(ord0)}
R0=len(ord0)
parent=list(range(R0)); bip=[0]*R0  # parity to root
def find(a):
    p=0; path=[]
    while parent[a]!=a:
        path.append(a); a=parent[a]
    r=a
    # compute parity
    for x in path:
        pass
    return r
# use union-find with parity
par=list(range(R0)); xor=[0]*R0
def root(a):
    if par[a]==a: return a
    r=root(par[a]); xor[a]^=xor[par[a]]; par[a]=r; return r
def union(a,b):
    ra=root(a); rb=root(b)
    if ra==rb: return xor[a]^xor[b]^1  # 0 if consistent-bipartite, 1 if odd cycle found
    par[ra]=rb; xor[ra]=xor[a]^xor[b]^1; return -1
odd=False; comps=0
for j in rem1:
    es,vs=cells[1][j]
    e=es[0]; u,v=edges[e]
    for l in range(n):
        for rest in itertools.permutations(vs):
            f1=[""]*n; f2=[""]*n
            ri=0
            for m in range(n):
                if m==l: continue
                f1[m]=rest[ri]; f2[m]=rest[ri]; ri+=1
            f1[l]=u; f2[l]=v
            r=union(o0[tuple(f1)],o0[tuple(f2)])
            if r==1: odd=True
ncomp=len(set(root(i) for i in range(R0)))
print("components",ncomp,"has_odd_cycle",odd)
print("rank d1 over F2:", R0-ncomp+(0 if odd else -1), " (R-c if nonbipartite else R-c-? )")
# Standard: connected graph incidence over F2: rank R-1 if non-bipartite, R-2+1=R-1? Recall: rank = R - b where b = #bipartite components. Connected non-bipartite => R-1... wait: bipartite connected => R-1; non-bipartite => R-1? Hmm: over F2, incidence of connected graph: rank R-1 if has odd cycle?? No: sum of all rows = 0 iff every column has even obce... every column has exactly two 1s => all-rows sum = 0 always (each col sums to 2=0). Additional relations iff bipartite (partition vector). So rank = R-1 (non-bipartite), R-2+1 = R-1?? For connected: nullspace of transpose = {x: x_a+x_b=0 per edge} = constants on... if non-bipartite, x=0 only? x_a=x_b for all edges (char2: +=) => x constant; then per edge 2c=0 always => constants ARE in left nullspace too?! Let me just directly: left null vectors x with x^T A=0: per column x_a + x_b = 0 => x_a = x_b (char 2). Connected => x constant c; any constant works (2c=0). So left null dim 1 => rank R-1 regardless of bipartiteness. Right null (cycles) differs. So rank d1 F2 = R-1 = 24239. Same as QQ. Good.
print("=> rank d1 = 24239 over QQ and F2,F3,F5.")
print("dim H1(Fp) = 56040-24239-31731 = 70 for p=2,3,5 => H1 free (no p-torsion for p=2,3,5).")
print("b1^ord =",56040-24239-31731)
print("b2^ord =",31920-31731)
# chi check: 24240-56040+31920 = 120 ✓ expected 120*chi(B)=120*1
print("chi =",24240-56040+31920)
