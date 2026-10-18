# Review of cograph-induced-subgraph profiles of matching-deleted bicliques

## Correctness — PASS

The claim is for finite labeled \(G_{a,b,t}=K_{a,b}-M_t\), with \(a,b\ge1\) and \(0\le t\le\min(a,b)\); coefficientwise monotonicity is only for \(a,b\ge3\), and the maximal-set enumeration is only for the full crown \(n\ge3\). The proof establishes an iff classification using the absent cross-edge that must close any induced four-vertex path, with no assumptions about unspecified edges. The three resulting configuration types are disjoint. Their weights produce the bivariate formula without overcounting. The difference formula is algebraically exact; all mixed coefficients except the first are visibly nonnegative, while the first is \((a-1)(b-1)-2t\ge0\), with the stipulated unique equality case. All maximal crown sets are captured by a one-vertex extension argument. These are proofs for all claimed integers, not extrapolations from finite tests.

The standalone verifier constructs adjacency and detects induced four-vertex paths, checks the entire face polynomial directly for 129 parameter triples (169304 subsets), and checks all maximal crown subsets for orders 3–8. Symbolic finite comparison checks cover 9282 further triples; they do not establish the infinite theorem. Python 3 standard library is sufficient.

## Originality — PASS, subject to residual priority risks

Oxley and Singh, *Generalizing Cographs to 2-Cographs* (arXiv:2103.00403), and Singh, *Cographs and 1-sums* (arXiv:2210.04139), state the classical forbidden-induced-\(P_4\) description and study structural extensions. Neither inspected full text treats the bivariate count of induced cograph vertex subsets of \(K_{a,b}-M_t\), its coefficientwise comparison under matching deletion, or its crown inclusion-maximal facet polynomial. Nastos and Gao, *Bounded Search Tree Algorithms for Parameterized Cograph Deletion* (arXiv:1006.3020, Section 4), explicitly reduce cograph vertex deletion to four-path hitting sets and give algorithms; an existence decision procedure does not state or imply the formulas for numbers of **all** solutions or all inclusion-minimal solutions. Closest publicly indexed results on deleted-matching bicliques concern non-CIS pairs or geodesic subpaths, and a complete-multipartite result concerns dissociation polynomials, not induced cographs.

The relationship to induced-forest and dissociation counts is not mere parameter renaming: induced \(C_4\) is a cograph but not a forest; induced \(P_4\) is a forest but not a cograph. Dissociation configurations form a proper subclass. There is no claim that the cograph definition, recognition, general deletion problem, or existence of facet-size gaps in other graph properties is new. Bibliographic searching and full-text reading are not a proof of priority; exact priority remains a risk.

## Value — PASS

Cograph vertex deletion is a natural hereditary graph-modification problem. The result gives the *entire* cardinality and bipartition-occupancy distribution of feasible induced cographs for every matching-deleted biclique, not merely a maximum size. The coefficientwise matching-deletion comparison is a global invariant inequality despite an edge deletion being able to both create and destroy induced paths; it includes an exact boundary equality. On the crown subfamily, a complete classification of irredundant vertex-deletion solutions gives arbitrarily long gaps in their cardinality spectrum, a structural obstruction to naïve interpolation among minimal solutions. The general polynomial and exact deletion-spectrum consequences are mathematically motivated, with no unproven downstream application asserted.

## Scope and limitations

This review considers exactly the theorem in `RESULT.md`, not any graph-polynomial claims in other families. The general formula applies down to one vertex per side; the monotonicity claim is deliberately limited to both sides at least three, and no general maximality theorem is claimed for partial matching deletion. A prior formula in unindexed work under *induced four-path transversal*, *P4-free deletion*, or *hereditarily well-colored induced subgraphs* could supersede part of the contribution. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
