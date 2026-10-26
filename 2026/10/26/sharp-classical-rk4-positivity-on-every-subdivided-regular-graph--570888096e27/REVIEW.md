# Scientific review

## Correctness — PASS
The entrywise polynomial is derived from the unoriented incidence-matrix block Laplacian. All off-diagonal pairs fall into six disjoint classes. Nonnegative classes are explicit monomials; two remaining quadratics have strictly negative discriminants and positive leading coefficients, and the incident original-to-edge cubic has the positive lower bound \(1-x+x^2/3\) on the required interval. The diagonal is positive because the scalar stability polynomial has an explicit sum-of-squares representation. A length-two path yields a negative distance-three entry at **every** timestep above \(2/(d+2)\). Perron–Frobenius applied to the signless Laplacian supplies the exact largest eigenvalue. The direct construction of 24 base graphs and 9,338 exact coefficient comparisons in `verify.py` corroborated the block formulas; enumeration is not used as infinite proof.

## Originality — PASS, residual risk
The 2001 full text by Gottlieb, Shu and Tadmor supplies general SSP theory, not the all-regular-base incidence-graph result. The accessible 2015 full text by Khalsaraei gives positivity conditions for upwind advection and Burgers discretizations, not for a graph's full edge subdivision. Steinerberger's 2018 work concerns true heat-semigroup asymptotics, not the fourth-degree RK4 polynomial. Mathematical research-record searches using “classical RK4 positivity ... full edge subdivisions”, “semiregular bipartite network ...”, and “Taylor polynomial ... regular bipartite ...” returned related methods but no covering theorem. Previously known special-family graph results include degree-at-most-two, complete multipartite, Hamming and crown graphs; those do not imply the arbitrary regular-base subdivision statement. General methods, unindexed graph-specific results, and one incompletely accessible 2003 paper remain originality risks. A failed search alone is not taken as proof of uniqueness.

## Value — PASS
Subdivision networks model coupled original sites and edge-mediated intermediate states. A degree-only, topology-independent, **sharp** completed-step positivity threshold over all connected regular underlying networks is a meaningful classification: it holds independently of size, girth and spectrum. It also quantifies exactly when completed RK4 extends the forward-Euler positivity horizon and when spectral stability ceases to ensure a nonnegative numerical solution. The result provides an exact network diffusion benchmark, not simply a calculation for one chosen finite graph.

## Limits
Only simple, connected, unweighted regular base graphs with one subdivision per edge, integer \(d\ge2\), and completed classical RK4 steps are covered. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
