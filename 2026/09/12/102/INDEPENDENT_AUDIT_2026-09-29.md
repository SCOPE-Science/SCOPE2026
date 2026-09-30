# Independent audit — 2026-09-29

Record: `2026/09/12/102`  
Audited source tree: `ab788e3afdcc5a5cc6abd0d1b03afc4cb52f342a`  
Disposition: **repaired**

## Correctness

The exact balanced-block computation is supported. Independent inspection of the supplied data and scripts confirms nine minimal balanced blocks, the listed Phi images, N^8>0 (minimum entry 1), M^4>0, prolongability, and the exact Q(beta) stationary-frequency calculation with diagonal-letter density (-3-9 beta+7 beta^2)/32≈0.350051. The polynomial x^3-2x^2-1 has one real Pisot root beta≈2.20556943, with the conjugate moduli below one. However, the original RESULT/SLOGAN promoted finite balanced-block closure plus coincidences directly to 'regular model set with pure-point diffraction'. The open literature located for common Rauzy-fractal dynamics states extra geometric hypotheses (for example interior/tiling or strong-coincidence conditions) around such conclusions. Those hypotheses were not established in the record, so the staged repair retains the exact nine-block/common-dynamics theorem and removes the unsupported spectral corollary.

## Originality

Balanced-block methods for same-matrix Pisot substitutions are established by Sellami and later work. The record contributes an exact decision and explicit finite closure for this concrete pair; a focused search did not surface this exact nine-block instance, but search absence is not a priority proof.

## Scientific value

The exact finite closure, primitive block substitution and frequency data are a useful concrete common-dynamics certificate even after removing the overextended diffraction conclusion.

## Limitations

- The repaired record does not claim that finite balanced-block closure alone proves a regular model set or pure-point diffraction.
- Any spectral/model-set corollary requires separately verifying the hypotheses of the applicable Rauzy-fractal or overlap theorem.
- The intersection matrix N itself is not Pisot; the exact computation concerns the common-block substitution built from the Pisot pair.

## Evidence and literature

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/12/102
- https://arxiv.org/abs/1002.3559
- https://doi.org/10.3906/mat-1407-3
- https://doi.org/10.1007/s00605-021-01515-x
- https://arxiv.org/abs/1711.10167
