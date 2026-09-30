# Independent audit — 2026-09-30

**Record:** `2026/09/20/schur-concavity-basmajian-seam-mass-hyperbolic-pants--05f60851034b`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `38edfe33002241d086c78e471aa485c882923411`  
**Disposition:** **PASSED**

## Correctness — PASS

The right-angled-hexagon cosine law and tanh half-angle identity yield the stated product formula and both closed forms. For fixed L, sum_i cosh(ell_i-L/4) is strictly Schur-convex, so the logarithm of its reciprocal is strictly Schur-concave. The equal-cuff maximum, zero boundary infimum, full interval by continuity, and sharp B_seam<L/2 bound follow. The displayed small-L expansion was independently re-expanded and agrees.

## Originality — PASS (literature-bounded)

The ingredients are classical and the result could exist as orthospectral folklore, but targeted comparison with the Basmajian identity literature, Doan–Parlier–Tan's Luo–Tan pants-measure work, and Basmajian–Parlier–Tan's prime-orthogeodesic framework did not locate the exact three-seam closed formula together with strict majorization, complete fixed-L range, and sharp one-half bound.

## Scientific value — PASS

The record converts a classical seam formula into a concise extremal theorem with a global sharp constant and a complete fixed-perimeter range. The strict Schur-concavity gives a useful structural statement beyond a one-point extremum.

## Evidence and literature

- Basmajian, The Orthogonal Spectrum of a Hyperbolic Manifold: https://doi.org/10.2307/2375068
- Doan–Parlier–Tan, Measuring pants: https://arxiv.org/abs/2002.02738
- Basmajian–Parlier–Tan, Prime orthogeodesics, concave cores and families of identities: https://arxiv.org/abs/2006.04872

## Limitations

- The quantity is only the contribution of the three inter-cuff seams, not the full Basmajian sum.
- Because the proof is elementary hyperbolic trigonometry, equivalent older formulations remain a real but unlocated originality risk.
