# Scientific review

## Correctness
**PASS.** The general proof reconstructs the exact DP-Nash definition: every provider must offer precisely \(k\) distinct other-side free recipients and every free recipient must be covered. The one-sided case supplies \(n\); the mixed case gives the necessary and sufficient integer region \(1\le p,q\le n-k\), \(kp+q\ge n\), \(p+kq\ge n\). A cyclic nomination map constructs every feasible point, including boundary equalities. Balancing proves the all-cardinality interval, and the capacity \(k=n\) case is separate. A direct subset-enumeration checker agrees for \(35\) parameter pairs; the proof, not the finite checks, establishes the all-size claim.

## Originality
**PASS, subject to bibliographic risk.** Gerke et al. introduce DP-Nash sets, general bounds and complete-graph extrema, while Gutin–Neary–Yeo analyze uniqueness complexity. A later matching result already covers the minimum when capacity is one, which is not claimed as novel in isolation. Related released-packing and limited-domination statements on bicliques have materially different feasibility restrictions. No inspected result implies the entire biclique spectrum or its \(\{2,n\}\) capacity boundary. An equivalent result in unindexed literature remains a possibility.

## Mathematical value
**PASS.** The attainable count spectrum, rather than just an extreme, determines which participation burdens can occur in equilibrium selection. Its arbitrarily large forbidden interval at capacity \(n-1\) and the abrupt \(2\)-to-\(n\) jump at full capacity exhibit a strong structural nonmonotonicity even in vertex-transitive-in-each-side regular networks. This gives a complete natural graph-family benchmark for exact capacitated domination.

## Scope and limitations
Only uniform \(K_{n,n}\), positive integer capacity, and specialised Nash equilibria are covered. Neither heterogeneous networks nor nonspecialised effort profiles are classified. The finite computation is confirmatory and does not certify a universal formula by enumeration.

Self-review: passed. Independent audit: not yet performed.
