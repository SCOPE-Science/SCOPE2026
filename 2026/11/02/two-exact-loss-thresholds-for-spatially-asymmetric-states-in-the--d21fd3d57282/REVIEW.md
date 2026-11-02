# Review of the balanced two-patch Allee phase diagram

## Correctness
The equilibria are fully enumerated by the factored mean/difference equations, without squaring away sign restrictions. The two asymmetric algebraic families satisfy distinct and exhaustive conditions, yielding nine, five and three equilibria in the stated regimes. Explicit Jacobian eigenvalues and determinant give their types; the nonhyperbolic \(m=1/12\) points are independently handled by a repelling cubic center-manifold drift. The exact gradient energy and a finite stationary set imply convergence of all orbits in the biological square. SymPy checks the factorizations, rational examples and critical cubic coefficient; sampled tests are not used to infer the infinite claim.

## Originality
The 2010 Kang–Lanchier article is the same underlying ODE and the decisive comparison. It states qualitative attractor loss and the high-coupling sufficient boundary \(m>1/8\) at balanced threshold, but does not provide the explicit sharp earlier stability loss at \(m=1/12\), nine–five–three equilibrium phase diagram, or the saddle interval \(1/12<m<1/8\). The 1999 Gyllenberg et al. work concerns biparental reproduction; its abstract does not establish the same cubic formula. Other two-patch Allee models differ in their local birth/death functions and coupling. No exact equivalent was identified in mathematical-record and literature comparisons. General coupled bistable-potential theories might imply the special calculation; this is a priority risk, not proof of uniqueness.

## Value
This is a natural complete sharp classification of the canonical symmetry-balanced threshold in an established ecological model. The two critical rates answer different ecological modeling questions: the destruction of stable source–sink imbalance versus the disappearance of all stationary imbalance. Between them a numerical solver can still find asymmetric states, but they cannot be long-term attractors. The full transition classification is more informative than either a high-dispersal sufficient bound or numerical phase plots. No field-level applicability or extension to arbitrary Allee thresholds is asserted.

## Closest literature and limitations
Same-model source: Kang–Lanchier (2010), arXiv:1003.0121, equations (4)–(5), Theorems 2.3–2.4 and related proofs; full relevant arXiv HTML sections inspected. Older prior: Gyllenberg–Hemminki–Tammaru (1999), DOI 10.1006/tpbi.1999.1430, accessible abstract; full text not inspected. Alternative formulation: the two-site discrete Allen–Cahn or coupled double-well gradient flow after an affine state change, which could host an earlier exact threshold classification. More general dispersal/Allee literature gives qualitative attractor loss. The mathematical result concerns deterministic local stability, not stochastic extinction.

Self-review: passed. Independent audit: not yet performed.
