# Independent mathematical audit

## correctness

PASS

PASS: Two independent descriptions of Kendall tau as pair-order disagreement and adjacent-swap distance agree on all unordered permutation pairs. Every code with 20 elements maps by a symbol relabeling to one containing identity; thus normalized size-20 equality enumeration and no normalized size-21 clique suffice. Reviewed exact color-bounded clique enumeration over 120 permutations and independently replayed a fresh bitset/color-capped clique search: exactly 532 normalized 20-cliques, no 21-clique. Double count (code, selected word) yields N=532*120/20=3192; expansion under all 120 relabelings and reversal gives orbit profile 1*6+3*30+2*48+4*60+5*120+9*240=3192 and 24 orbits. Claimed symmetry is only the explicit 240 group; finite search is exhaustive for its fully specified 120-vertex graph.

## originality

PASS

PASS best-of-knowledge for complete equality-code census and natural-group orbit classification, not for known optimum P(5,3)=20 or the published explicit construction. Vijayakumaran (2016) provides the optimum and one code; Buzaglo--Etzion general bounds, and Jany--Ravagnani t-balanced structure at min distance>=4 do not mathematically imply distance-3 equality cases. Full Vijayakumaran article inaccessible due an explicit access/safety block, a residual priority risk.

## value

PASS

PASS: Enumerating all equality cases at the smallest substantial Kendall metric parameter reveals precise multiplicity, nontrivial stabilizer variation and 24 symmetry classes beyond a known cardinality bound; this is a motivated complete finite extremizer classification useful for comparing permutation-code constructions and orbit-search benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
