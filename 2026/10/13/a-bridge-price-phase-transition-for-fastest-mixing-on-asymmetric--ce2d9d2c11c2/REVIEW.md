# Scientific review: double-star bridge-price threshold

## Correctness — PASS

The geometric upper bound is an exact sum of Rayleigh inequalities with all edge-price constraints tight. Each explicit primal–dual construction is centered, has squared norm equal to the stated inverse spectral gap, and satisfies the unscaled Laplacian eigenvalue-one equation. The low-price interlacing argument and high-price Schur inertia argument prove this eigenvalue is the second eigenvalue, not merely an arbitrary eigenvalue. Equality in the certificate and the leaf equations prove uniqueness even without assuming symmetric competing rates. The branches and equality boundary match algebraically. Exact-rational checker tests reproduce all structural identities for 299 cases but are not substituted for the proof. Risks: arithmetic transcription or unnoticed edge cases remain possible; no independent validation.

## Originality — PASS, narrowly bounded

Sun–Boyd–Xiao–Diaconis establish the optimization and embedding duality in the general positive edge-cost setting. Richter–Rocha give explicit double-broom uniform-price formulas and eigenvectors, covering the unit-price case here, and Fiedler establishes prior tree-level absolute connectivity theory. Wappler studies arbitrary edge lengths in general. The specific price-dependent optimizer for all real positive bridge prices, the explicit location of its threshold, and the eigenvalue-multiplicity change are not stated in the inspected primary full texts of Sun et al. or Richter–Rocha. This is a claim for that classification only, not for the known general method or the unit-price specialization. Residual risk: the 2013 Wappler thesis PDF and Fiedler's complete 1990 article were not available for full-text exclusion; an equivalent unpublished or poorly indexed specialized formula may exist. Abstract- or repository-level evidence is not represented as full-text inspection.

## Value — PASS

A two-hub network with asymmetric peripheral populations and a separately priced inter-hub link is a natural resource-constrained mixing model. Its exact price transition distinguishes two optimizer geometries, uniquely specifies all \(k+\ell+1\) edge rates, and determines a nontrivial spectral multiplicity boundary. General semidefinite optimization does not by itself display these sharp analytic price and dimension laws. The theorem does not assert a general graph-class improvement or an empirical application.

## Closest antecedents and limitations

The closest full-text predecessor is Richter–Rocha's double-broom analysis of the equal-price model. Sun et al. provide the same primal–dual principles for arbitrary prices but give examples of paths and cycles rather than the two-hub price transition. Fiedler (1990) and Wappler (2013) are relevant structural antecedents with incomplete full-text access. The nonuniform stationary-measure, arbitrary-tree, and discrete-time variants are outside scope.

Self-review: passed. Independent audit: not yet performed.
