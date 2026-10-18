# Independent mathematical audit

## correctness

PASS

In generalized theta graph Theta(ell_1,...,ell_d) with d>=3 paths ell_i>=2, the branch vertices have equal round colors by the graph involution and are distinguished from degree-2 internal vertices at round 1. For internal position i on a length ell path, equality of round-r colors is exactly equality of unordered clipped distances {min(i,r),min(ell-i,r)}, proved inductively using the two neighbor colors plus branch marker. Within a longest length L, positions unresolved after round r force r>=floor(L/2). Across distinct lengths a<b, the shorter path tip first differs at round a; the largest such shorter length is second-largest DISTINCT path length S, requiring r>=S. These conditions jointly suffice: each path position is distinguished up to its reversal and shorter-length distance sums differ from every longer clipped pair. Hence Stab=max(floor(L/2),S). At fixed d and n=sum ell_i-d+2, L<=n-d and distinct second length S<=floor((n-d+1)/2); d-2 paths of length 2 and two balanced lengths attain upper bound. Independent direct refinement for 2,958 nondecreasing length tuples d=3..6, ell=2..9 matched the depth formula, corroborating but not proving its infinite quantification.

## originality

PASS

Generalized theta graphs are subdivisions of K_{2,d}; published square-coloring computations on theta graphs study proper coloring of square graph, not iterative 1-WL color refinement. Krebs–Verbitsky and Kiefer–McKay upper bounds for all n-vertex graphs apply but are not sharp equality for every theta path tuple and do not give max(floor(L/2),S). The general n−1 iterative upper bound, even if tight elsewhere, does not imply a lower bound tied to the second-largest DISTINCT arm length S nor the exact maximum at fixed d and n. Primary text inspections and Resultary cross-checks found no exact or dominating theorem for the complete claim; this is a best-of-knowledge PASS with the listed explicit literature and accessibility risks, not proof of absolute novelty.

## value

PASS

Subdivisions of K_{2,d} constitute a natural graph family with two high-degree symmetric hubs; the result gives the full refinement partition evolution, identifies the exact bottleneck from path length diversity, and solves a sharp fixed-order extremum within the whole family. It supplies precise algorithmic iteration behavior not provided by generic worst-case 1-WL bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
