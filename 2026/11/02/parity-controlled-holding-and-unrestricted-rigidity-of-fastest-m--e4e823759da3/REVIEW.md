# Scientific review

## Correctness — PASS

The exact Fourier eigenvalue interval gives the SLEM lower bound \(\max\{1-t,Et-1\}\) and forces \(t=\min\{2/(E+1),1/H\}\). Symmetry averaging establishes unrestricted attainability. The upper semidefinite eigenvalue equality for all first coordinate Fourier characters then forces every individual edge weight, ruling out nonsymmetric ties. The holding criterion follows from an exact trigonometric odd-cycle deficit. No computation is substituted for the infinite proof. The standalone verifier independently confirmed 3,138 finite consistency assertions on 28 cases.

## Originality — PASS, qualified

The 2004 convex-SDP framework and 2007 symmetry/product results are acknowledged. Section 3.2 of the 2007 paper explicitly solves a two-factor **equal-side** torus, while Section 3.3 covers homogeneous Hamming products. The current general statement is not an equal-side example or an edge-transitive direct specialization: products with distinct cycle lengths have independent edge-direction parameters, and the proof adds an edge-by-edge rigidity argument. Actual published-record and full-text searches did not identify the arbitrary-dimensional odd-factor holding criterion. General older optimization techniques make the spectral part approachable, but do not by themselves state or establish the joint classification. An unindexed earlier equivalent classification remains a residual risk.

## Mathematical value — PASS

This is a complete infinite-family optimization classification, not an isolated example: the rule works for arbitrarily shaped and high-dimensional discrete tori and for unrestricted stochastic weights. The phase boundary collapses from all numerical side lengths to the count of odd factors, apart from one sharp triple-triangle equality case. That is a structural, usable support/holding design criterion for uniform-stationary lattice random walks.

## Closest literature and limits

Boyd, Diaconis and Xiao (2004), DOI 10.1137/S0036144503423264, establish the general convex objective. Boyd, Diaconis, Parrilo and Xiao (2007), arXiv:0709.0955v1, §§2–3, prove averaging and treat equal two-dimensional cycle products and homogeneous Hamming graphs; their generic product-spectrum identity is retained as established groundwork. The theorem here assumes symmetric nearest-neighbor/self-loop kernels and does not compare nonreversible or lifted chains. Earliest precise-date release directly verified for the focal arXiv version is 2007-09-06; a precursor MSR technical report is catalogued with month-only May 2007 dating.

Self-review: passed. Independent audit: not yet performed.
