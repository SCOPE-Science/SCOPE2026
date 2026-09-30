# Independent Audit — 2026/09/12/021

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `1d5025d595599e091ab59b7881787bbb7a4de555`  
**Disposition:** **REPAIRED**

## Correctness

The current package uses the wrong Fourier exponent on the root edge rc: it uses g1+g2, whereas for a consistent four-leaf pattern the rooted edge carries g1+g2+g3=g4 in G=Z2xZ2. The current verifier therefore certifies the wrong polynomial map. Recomputing the corrected map exactly nevertheless preserves the decisive conclusion: the 64x19 Jacobian has rank 13, with a nonzero 13x13 minor of determinant 160576479/4194304; the displayed-tree monomial exponent matrix has rank 10. The result is repairable, but the uncorrected research files are not internally correct.

## Originality

Recent dimension theory leaves the even-order 3-cycle case open. Cox, Gross, and Martin prove their 3-sunlet dimension formula for odd-order abelian groups and explicitly explain that even-order groups remain unresolved under their method. K2P uses the even-order group Z2xZ2, so an exact certified lower bound for this concrete triangle-network model is not mechanically implied by that theorem.

## Scientific value

After correcting the root-edge exponent, the rank-13 certificate rigorously refutes the proposed dimension 7 in a genuinely delicate 3-cycle/even-order regime and also fixes the displayed-tree dimension at 10. This is useful algebraic-statistical information for identifiability and parameter-count questions even though the exact network dimension is not yet proved.

## Limitations

- The repaired result proves only dimension at least 13 for the network, not exact dimension 13.
- The correction is tied to the stated K2P Fourier normalization and topology.
- The current package's original verifier is invalid for the phylogenetic map until the guarded replacement supplied by this audit is applied.

## Evidence

- [Gross–Krone–Martin, Dimensions of Level-1 Group-Based Phylogenetic Networks](https://arxiv.org/abs/2307.15166): Provides level-1 dimension formulas but the difficult 3-cycle case motivates later work; it does not settle this K2P four-state triangle instance.
- [Cox–Gross–Martin, Group-based phylogenetic models on 3-sunlet networks](https://doi.org/10.1007/s11538-025-01506-1): Proves a dimension formula for odd-order abelian groups and states that even-order cases remain open under the paper's method; K2P is based on Z2xZ2.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `1d5025d595599e091ab59b7881787bbb7a4de555`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
