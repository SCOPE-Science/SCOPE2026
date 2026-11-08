# Independent mathematical audit

## correctness

PASS

The all-n VC upper bound maps any shattered comparison-support edges to a forest: a cycle can be oriented cyclically in its queried pair answers but no total order can realize it. n-1 lower bound is a star comparing symbol 1 to all other symbols: for every partition before/after 1, Av(123) is witnessed by both sides descending, and Av(132) by left descending/right ascending; reversal/complement symmetries extend to all six forbidden length-three patterns. For Ldim only n<=8 is claimed. For each of tau=123 and tau=132, all n! permutations are screened by direct triple standardization; compared concepts' n-choose-2 comparison-column masks. The exact complete-depth recurrence F(B,d)=exists query q with both answer subsets satisfying F(.,d-1), and safe cardinality pruning <2^d, proves both feasible and infeasible depth decisions. I independently reimplemented the recurrence without relying on package upper-test results and reproduced the dimensions tau=123: (n=3..8) 2,3,4,6,7,9 and tau=132: 2,3,5,6,8,9, including upper negative decisions; class sizes 5,14,42,132,429,1430. Inspected the actual compute_dimensions.py, verify_certificates.py, and full Git-tree-listed SHATTERING_TREES.json 33,305-byte certificate and its documented leaf verifier. The source verifier checks all root-to-leaf answer traces; independent exhaustive upper recurrence also confirms both dimensions. Boundaries n=1 gives 0, n=2 gives 1. No general n>=9 Ldim formula or finite-to-infinite extrapolation is asserted.

## originality

PASS

The six avoidance classes are Catalan/Wilf-equivalent, as Janson documents, but prior pattern-occurrence, permutation-enumeration and constrained stack-sorting results do not calculate this exact online pairwise-comparison Littlestone table. General query-learning theorems and full-permutation VC/online dimensions give only universal bounds, not restricted-class sharp dimensions. A published 123-avoidance fp/exc/des finite census concerns a genuinely different observable. Originality qualified by potential older specialization in sorting/ranking learning literature.

## value

PASS

The question whether equinumerous Wilf classes and identical static VC dimensions can have different adaptive comparison complexity is mathematically natural. Exact separation first at n=5, renewed n=7, and a full two-symmetry-orbit finite census to n=8 give an independently useful boundary with explicit search/tree witnesses; no unjustified all-n claim. The result is not arbitrary isolated integer counting because it compares canonical Catalan pattern classes under a standard online learning dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
