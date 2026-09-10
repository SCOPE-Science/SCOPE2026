# Certified cross-ratio distortion on an explicit genus-2 SL(3,R) Goldman-bulging line

## Context
Hitchin-component entropy rigidity (Potrie–Sambarino: topological/first-simple-root
entropy maximized only at the Fuchsian locus), Liouville pressure metrics
(Bridgeman–Canary–Labourie–Sambarino), and Labourie cross-ratio dynamics form a
recognized program. The qualitative maximum is known; quantitative distortion
numbers for named bending cells were missing. This record is the admitted preset
fallback of that target investigation: one exact certified distortion datum on a
canonical cell, explicitly not an entropy-gap proof.

## Definitions
- Base: closed genus-2 Fuchsian group via two tr(3.2) blocks A,B in SL(2,R)
  doubled through the commutator involution j (relation error 6.2e-15 in SL(2)),
  lifted by the symmetric-square irreducible representation Sym^2:
  SL(2,R) → SL(3,R) (homomorphism error 1.8e-13; SL(3) relation error 9.2e-13).
  Named generators: A1, B1 (Block 1, fixed side), A2, B2 (Block 2, bent side).
- Bending curve: γ = [A1,B1], hyperbolic length ≈ 2.6614.
- Bulge: B(t) = V diag(e^t, 1, e^{−t}) V^{−1} / det^{1/3}, V diagonalizing
  γ in SL(3,R) (centralizer error |B(t)γ − γB(t)| = 3.4e-15);
  ρ_t = (G(A1), G(B1), B(t)G(A2)B(t)^{−1}, B(t)G(B2)B(t)^{−1}).
- Parameter: t* = 1/4 (fixed interior Fuchsian-nearby point).
- Quadruple: Q0 = (a+, a−, b+, b−) with a = A1, b = A2. Flags are transverse
  line+covector pairs with crossed attracting/repelling pairing:
  a+ = (attracting line of ρ(A1), repelling covector of ρ(A1)),
  a− = (repelling line of ρ(A1), attracting covector of ρ(A1)), likewise for b.
- Labourie cross-ratio: B(x,y,z,w) = ⟨x|z⟩⟨y|w⟩ / (⟨x|w⟩⟨y|z⟩),
  ⟨x|z⟩ = n_z · p_x (covector of z dotted with line of x).

## Result
For the explicit ρ_{1/4} defined above, on Q0 = (a+, a−, b+, b−) with a = A1,
b = A2:

**B(ρ_{1/4})(Q0) = 674.3355365450 ≥ 1.02 — binary check PASS (margin +673.32).**

Pairings: ⟨a+|b+⟩ = −1.339290, ⟨a−|b−⟩ = −0.665985,
⟨a+|b−⟩ = −0.032507, ⟨a−|b+⟩ = −0.040689;
smallest |pairing| = 0.0325 (bounded from degeneracy).
Bending-driven table on this Q0 convention:
B = 17.15 (t=0), 116.18 (0.15), 258.90 (0.20), 674.34 (0.25),
2271.53 (0.30), 12457.02 (0.35).

## Proof / evidence
Numerical certificate (float64 + perturbation stability), honestly not an
interval enclosure (mpmath interval attempt blew up; logged as failed).
- One-command replay `output/artifacts/replay_fallback.py` recomputes
  B = 674.3355365450072 from stored matrices and prints PASS; independently
  re-executed at audit with identical value.
- All four ρ generators loxodromic with real distinct eigenvalues
  (≈ 0.123, 1, 8.117); eigen-residuals |Mv − λv|, |wM − λw| ≈ 1e-14–1e-16;
  biorthogonality W^T V = I exact; eigengaps (7.12, 0.88); condition ≤ 22.
- SL(2)/SL(3) dets = 1 to ~1e-12; ρ relation error 9.2e-13 (audit recompute
  1.04e-12); bulge centralizes γ to 3.4e-15.
- Stability: 200 perturbations at 1e-9 produce spread 1.6e-4, ~4M× below the
  673.32 margin, so rounding cannot flip the binary inequality.

## Limitations
- Numerical certificate only; exact digits beyond ~1e-4 are not certified.
- Distortion only: implies no entropy bound h ≤ 0.999 by itself; the target
  pressure-zero derivative inequality was not proved (pressure route capped:
  length-8 relator forces kernel words at N ≥ 8).
- The bare threshold 1.02 is already exceeded at the Fuchsian base
  (B0 ≈ 17.148 on this Q0 convention); Fuchsian departure is witnessed by the
  full logged value 674.34 and the monotone bending table, not by the
  threshold alone.

## Reproducibility
`python3 output/artifacts/replay_fallback.py` → PASS.
`output/artifacts/build_matrices.py` rebuilds base, Sym², bulge, B-table,
length-stretch and dominated-splitting checks. Matrices:
`genus2_SL2.npy`, `genus2_SL3.npy`, `rho_t025.npy`, `block_AB.npy`.

## References
- R. Potrie, A. Sambarino, Eigenvalues and Entropy of a Hitchin representation,
  arXiv:1411.5405.
- M. Bridgeman, R. Canary, F. Labourie, A. Sambarino, The pressure metric for
  Anosov representations, arXiv:1301.7459.
- M. Bridgeman, R. Canary, F. Labourie, A. Sambarino, Simple root flows for
  Hitchin representations, arXiv:1708.01675.
- J. Beyrer, O. Guichard, F. Labourie, B. Pozzetti, A. Wienhard, Positivity,
  cross-ratios and the Collar Lemma, arXiv:2409.06294.
- R. Canary, T. Zhang, A. Zimmer, Entropy rigidity for cusped Hitchin
  representations, arXiv:2201.04859.
