# Self-review

## Correctness
PASS. The proof reduces a late color split to a rooted-branch discrepancy. A coarse match through depth \(s-2\) but fine mismatch at depth \(s-1\) either occurs in two disjoint outward branches, which alone force \(2s-1\) branch vertices plus the two roots, or is carried uniquely inward along the geodesic. Each inward step consumes two permanent geodesic vertices and lowers the remaining depth by one, preserving the invariant needed for the same count. The fronts cannot cross without exposing an outward mismatch; the terminal depth-one case needs one extra neighbor and also totals \(2s+1\). Applying this to the last strict refinement gives the half-order upper bound. The path calculation supplies equality. An exhaustive implementation independently checks all 81,136 unlabeled trees through order 17.

## Originality
PASS with residual literature risk. Semantic literature searches for exact tree/forest iteration-number bounds, 1-WL stabilization on trees, and the half-order formula produced no matching finding. The primary archive-era source of Krebs--Verbitsky gives the general universal-cover/color-refinement correspondence and near-linear unrestricted lower bounds, not the tree extremum. Kiefer--McKay explicitly gives the path value and unrestricted extremal theory; targeted full-text searches of their 19-page paper return no occurrence of “tree” or “forest”. Ito's title *The Weisfeiler-Leman stability: the case of trees* was inspected as a high-risk collision; its subject is algebraic WL stability/coherent configurations rather than the 1-WL iteration count. No exact database/table entry for the tree maximum was found.

## Value
PASS. This upgrades a family-level exact calculation to a sharp class-wide extremal theorem: the unrestricted \(n-1\) worst case collapses to exactly half order on trees. The two-front lemma also isolates the structural reason: without cycles, a refinement event at depth \(s\) needs two simultaneously surviving information fronts, costing at least \(2s+1\) vertices. The result is simple to state, sharp for every order, and directly relevant to the iteration-number viewpoint in finite model theory and graph isomorphism.

Self-review: passed. Independent audit: not yet performed.
