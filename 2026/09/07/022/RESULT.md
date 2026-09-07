# Finite-mutation census of connected 5-vertex quivers with arrow multiplicity at most 2

## Context
Rank-2 quiver mutation is Markov dynamics (textbook). General finite-mutation
classification of Felikson–Shapiro–Tumarkin (FST) is existential: rank 2,
surface triangulations, plus 11 exceptionals (smallest rank 6), with a
criterion but no vertex-and-arrow-bounded enumeration, diameters, or
replayable certificates. Rank-3 censuses (Seven; Felikson–Tumarkin geometry
via Markov constant) do not imply rank-5 global equivalence. Small bounded
catalogs are citable benchmarks for cluster-algebra software and Seiberg-duality
quiver work.

## Definitions
Let S(5,2) be connected skew-symmetric 5x5 integer matrices B with
max|B_ij|<=2, up to simultaneous permutation (unlabeled quivers).
Mutation mu_k (Fomin–Zelevinsky, exact integers):
mu_k(B)_ij=-B_ij if i=k or j=k, else
B_ij+(|B_ik|B_kj+B_ik|B_kj|)/2.
Labeled quivers are 25-tuples; canonical form is S5-minimum row-major tuple
(equivalently minimal base-5 code on 10 upper entries in order
01,02,03,04,12,13,14,23,24,34 with digits +2).
Labeled exchange graph: vertices distinct matrices, edges mu_k (involutive,
unweighted undirected). Diameter is max shortest labeled-mutation distance
by exact all-pairs BFS.
For a 3-vertex triple write p=|B_ij|,q=|B_jk|,r=|B_ki|; if all three edges
present and signs of B_ij,B_jk,B_ki agree (cyclic),
C=p^2+q^2+r^2-pqr is invariant under (p,q,r)->(p,q,pq-r).

## Result
S(5,2) meets exactly F=7 finite-mutation classes. One lex-min upper-10
representative per class with labeled order N and diameter d:

- 31 [-2,1,1,1,-1,-1,-1,0,0,0] N=270 d=7 affine tilde D4 (contains K1,4 star)
- 13 [-2,0,1,1,0,-1,-1,-1,-1,0] N=600 d=8 finite-mutation (surface)
- 0 [-2,0,0,1,0,0,-1,-2,1,-1] N=720 d=9 finite-mutation (surface)
- 15 [-2,0,1,1,0,-1,-1,-1,0,0] N=1440 d=11 finite-mutation (surface)
- 2 [-2,0,0,1,0,0,-1,-1,-1,0] N=1680 d=11 affine tilde A (contains acyclic C5)
- 415 [-1,-1,0,0,0,-1,0,0,-1,0] N=1980 d=11 type A5 (lex-min is 3-1-0-2-4 path)
- 199 [-1,-1,-1,0,0,0,-1,0,0,0] N=2184 d=11 type D5 (lex-min D5 tree arms 1,1,2)

Enumeration: 5^10=9765625 labeled, 9684224 connected (99.17%),
63709 passing triple filter, 58488 connected passing, 567 unlabeled passing.
Labeled BFS max<=2 from all 567: 97 close, 470 exhibit frontier needing 3
(hence infinite); canonical sets of the 97 collapse to 7 disjoint classes.

Witness W_fin (D5, id 199): rep upper [-1,-1,-1,0,0,0,-1,0,0,0]
(0<-1,2,3 and 1<-4 on D5 tree). Labeled BFS closes at 2184 nodes all max<=2,
eccentricity 11, diameter 11, per-node shortest path log and adjacency stored.

Witness W_inf: seed B0 [[0,2,-1,1,0],[-2,0,2,0,1],[1,-2,0,0,0],[-1,0,0,0,0],[0,-1,0,0,0]],
triple 012 cyclic (2,2,1) C=5. Mutate only 012 in repeating order 1,0,2 for
12 steps: maxima 2,3,4,10,37,366,13532,4952675,67019597734,
331926286207224918,22245566178948766568816183137,
7383888166355511098764350563784314022618210032,
164258772862618181462691390833789348539465093269150451212405503507035405466
strictly increasing, triple stays cyclic C=5. Hence unbounded and infinite;
lifting preserves triple dynamics. B0 is connected max 2, so in S(5,2).

## Proof / evidence
Hereditary: mutating inside V' uses only V' entries, so finite implies
induced subquivers finite. Rank-3 cyclic C invariance by direct check.
Needed C=5 case proved directly: sorted x<=y<=z with z>x and y>=2 gives
yz-x>z since yz>=2z>x+z, new strict maximum, stays positive cyclic,
minima rotate forever (round-robin 1,0,2 grows forever).
Rank-3 acyclic doubles: 112 connected labeled triples (125-13 disconnected);
10 cyclic C<=4 close in <=14 nodes; 78 acyclic with a 2 reach cyclic C>4 in
<=2 mutations (triple_bridge.csv, each step re-verified). Hence connected
triple with a 2 finite iff cyclic (2,1,1) or (2,2,2); acyclic finite iff
max<=1; disconnected triples with <=1 edge always finite. Filter is sound.
Bound 2 sharp for rank>=3 finite mutation (FST Theorem 2.6: no weight>2 in
class; 11 exceptionals rank>=6, rank 5 exceptional-free), connectivity
preserved (deleted edge (a,b) requires a-k,b-k edges, rerouted via k), so
bounded BFS max<=2 decides finiteness: closed=>finite, frontier needing
3=>infinite. Exhaustive vectorized enumeration plus S5-minimum plus labeled
BFS with union-find gives F=7 as above; independent audit replayed all
counts, closures, disjointness, diameters, paths, growth, and bridges.

## Limitations
Finiteness uses cited FST max<=2 and general cyclic C>4 infiniteness
(C=5 self-contained). Orders/diameters are exact-BFS computed evidence
replayed by independent formula, not hand proofs. Type labels beyond
A5/D5/affine-star/C5 are educated: 3 classes proven finite-mutation and
distinct by closure/disjointness/orders but explicit surface-block tilings
not machine-verified (labeled surface, conjectural); no exceptional possible
in rank 5. No claim beyond S(5,2).

## Reproducibility
artifacts/recheck.py (stdlib+numpy) replays lex-min (7), closure+orders (7),
disjointness, Wfin 2184 paths+closure, Winf 12 steps, 78 bridges in <2min.
Enumeration vectors and 5^9-weighted canonical documented in code.
Deterministic, fixed seed. Timing in timing.txt.

## References
- A. Felikson, M. Shapiro, P. Tumarkin, Skew-symmetric cluster algebras of finite mutation type, arXiv:0811.1703 (JEMS 14 (2012) 1135-1180). https://arxiv.org/abs/0811.1703 https://doi.org/10.4171/jems/329
- A. Seven, Mutation classes of skew-symmetrizable 3x3 matrices, arXiv:1012.3318. https://arxiv.org/abs/1012.3318
- A. Felikson, P. Tumarkin, Geometry of mutation classes of rank 3 quivers, arXiv:1609.08828. https://arxiv.org/abs/1609.08828
