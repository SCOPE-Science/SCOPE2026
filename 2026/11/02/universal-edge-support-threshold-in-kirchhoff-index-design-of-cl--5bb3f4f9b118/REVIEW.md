# Review of the clique-windmill conductance-design theorem

**Correctness: PASS.** The weighted objective is strictly convex over the connected feasible budget simplex because the restricted Laplacian is an injective positive-definite affine function of individual edge weights. Automorphism invariance then forces the unique optimum to be uniform within each edge class. The direct Laplacian spectral factorization reduces the problem to \(C/a+A/(a+rb)\); the price-constrained Cauchy--Schwarz bound establishes the interior optimum and the exact right-boundary derivative establishes when the graph design abandons every internal clique edge. The calculation includes the equality threshold and strict uniqueness. Exact-rational inverses and unrestricted numerical searches corroborate the proof but do not establish the general theorem independently.

**Originality: PASS, subject to explicitly acknowledged historical search limits.** The 2006 and 2008 Ghosh--Boyd--Saberi works provide the foundational convex effective-resistance design and solved special topologies, but do not state the class-dependent clique-windmill threshold. The same-graph 2024 Sardar--Xu Kirchhoff-index study addresses fixed unit resistances in its accessible abstract; its full text is not available, so whole-document noncoverage is not asserted. The available published mathematical-result searches identified no equivalent support law. Potential unlocated specialist prior work remains a risk and absolute priority is unproved.

**Mathematical value: PASS.** A natural model of priced hub versus community connections is solved for every \(s,r\ge2\), globally against independent edge weights, not only among assumed symmetric designs. Its complete price-threshold support diagram reveals a universal dependence on total peripheral size despite nontrivial spectral dependence on the individual community sizes.

The theorem requires equal prices within each edge class and minimizes total effective resistance, not maximum resistance or mixing time. Reproduced finite computations are not an independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
