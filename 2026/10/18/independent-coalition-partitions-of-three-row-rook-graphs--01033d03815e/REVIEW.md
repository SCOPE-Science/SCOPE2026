# Independent mathematical audit

## correctness

PASS

The rook graph is L(K_{3,n}); independent dominating sets are maximal matchings and hence precisely three nonattacking cells, since any smaller matching leaves an unused row and column. There is no universal vertex. Every block must participate and therefore has size one or two. With t pairs the block count is 3n−t; t≤2 leaves a singleton in every row, demanding three distinct missing-row pair types. The two-column witness uses every cell of two columns, so any singleton in the missing row completes its pair. At t=3 and n≥4 each row still has a singleton, forcing one pair per missing row. In the notation B₀=(a,b), B₁=(c,d), B₂=(e,f) with row positions as in the Finding proof, each pair’s two columns must both be used by paired cells in its missing row. Thus {a,b}={c,e}, {c,d}={a,f}, {e,f}={b,d}. If c=b then e=a, d=a and f=b; if c=a then e=b and d=f∉{a,b}. These are sufficient, and B₀ fixes (a,b) while B₁ recovers d, so counts are n(n−1) and n(n−1)(n−2) without ordering blocks. For n=3, singleton counts are the missing-row counts: (1,1,1) repeats the two families for 12; (0,0,3) uses the two column derangements for each of the three singleton rows, for 6, and every pair and singleton has its complementary column partner. For (0,1,2) there are 6 row assignments and 6 choices (c,d) of the pair missing the middle row; its singleton at the third column z forces row 1's paired columns c,d and then the two other pairs (d,c),(z,d), each with an available row-2 complementary cell. This gives 36 and total 54. Inspected verify.py and frozen transcript, without executing that script. Independent replay: python3 -I /workspace/independent_reproductions.py uses closed-neighborhood bitmasks and a restricted-growth enumeration of all 21,147 partitions for n=3; finds exactly {6:54}, split 6,36,12 for the three sorted profiles. For n=4 it checks all 2863 disjoint at-most-three-pair candidates and finds 36 valid with 9 blocks. The support's checks for n=5 through 8 are recorded finite evidence, not independently rerun or used to infer the theorem.

## originality

PASS

The supported distinct claim is the sharp optimum and complete maximizing census for the width-three Cartesian product with its exceptional square case. The strongest accessible comparisons concern different graphs, different coalition definitions, or loose bounds. A likely relevant counting preprint could not be independently retrieved; the verdict does not rely on the frozen account of its contents or treat the access failure as evidence.

## value

PASS

The exact optimum and number of optimal labeled partitions are natural coefficient data for the independent-coalition polynomial of a graph product. The solution determines two entire optimizer families and explains three distinct boundary profiles giving 54, rather than extrapolating or selecting an arbitrary cutoff. The width-three restriction is motivated by the first product case in which maximal matchings have three cells and hence impose pair/singleton compatibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
