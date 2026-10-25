# Independent mathematical audit

## correctness

PASS

For C_n, n>=3, one root, p in (0,1), each nonroot vaccine subset: edge-disjoint complementary paths give P(root connects k)=p^k+p^(n-k)-p^n. After a vaccine the remaining root arms have lengths i-1 and n-i-1; after two vaccines i<j they have lengths i-1 and n-j-1. Signed B second difference equals (n-1)p^n-sum_{k=n-i}^{n-1}p^k-sum_{k=j}^{n-1}p^k and is <=p^(n-1)((n-1)p-2), equality only at root neighbors. For nonempty background deletion leaves a rooted forest with nonnegative weighted path coverage, hence all additional second differences <=0. Continuity/monotone p^{-h} argument yields unique pair-specific crossing only for separation >=2. n=3 boundary is outside 0<p<1; C4 neighbors give p^3(3p-2). Independent exact live-edge enumeration checked all n=3..6, p=1/4,3/4, vaccine backgrounds and pairs, matched formulas. Finite checks are not the proof.

## originality

PASS

The sharp all-subsets on-cycle if-and-only-if threshold, individual pair switching and minimum graph size are compared against tree immunization submodularity and general epidemic optimization/reliability. No inspected exact statement implied the cycle threshold; novelty limited to this special stochastic model and not proven by unsuccessful search.

## value

PASS

The usual greedy guarantee for a monotone vaccination benefit depends on submodularity. A uniform exact threshold on a natural unicyclic graph, all pair-switching thresholds and minimum four-vertex counterexample identify precisely where that structural prerequisite holds. This is an infinite family with explicit boundary, not a routine substitution or isolated tiny check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
