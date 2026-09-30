# Independent Audit — 2026/09/19/arbitrary-state-completeness-compact-and-commutative-cstar--6852917bfb68

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `95a75aa7d1a853808b2a6521f4a734a646d5c7b8`
- Disposition: **PASSED**

## Correctness

**PASS** — The classification is mathematically sound. For the standard module over A=c0-direct-sum K(H_lambda), the state seminorm is exactly the l2 Hilbert-Schmidt norm of a_lambda rho_lambda^{1/2}; finite spectral truncations show the image is dense in the claimed l2-sum. Surjectivity holds exactly when the support projection has finitely many nonzero finite-rank blocks, equivalently p lies in A. If p is not in A, rho^{1/2} is a completion vector that cannot equal a rho^{1/2} for any a in A. When p lies in A, N_tau^E={x:xp=0}, and the quotient identifies with the closed finite-corner module Ep with an equivalent scalar norm. In the commutative case the standard quotient is the C0(X) image in L2(mu); closedness forces finite support by the bounded-inverse argument and localized bump functions, while finite support gives a finite direct sum of fibers for every module. The explicit faithful mixed state on K(l2) independently disproves unrestricted arbitrary-state completeness.

## Originality

**PASS** — The current Abedi-Moslehian preprint explicitly defines localization for arbitrary states and its abstract states completeness in the compact-operator and commutative classes, while its title and main Schatten-norm framework center pure states. The audited theorem supplies a sharp arbitrary-state boundary that is not present in the source abstract: finite-rank finite-block support in the compact-operator case and finite measure support in the commutative case. Targeted searches of Hilbert C*-module, GNS, compact-operator, finite-support and Hilbert-Schmidt formulations did not locate these two exact criteria or the explicit completion model. Classical GNS/localization and compact-operator-module results are background rather than coverage of the stated classification.

## Scientific value

**PASS** — The result repairs a materially overbroad recent completeness statement, identifies precisely which mixed states still work, and supplies explicit counterexamples for all infinite-support states already on the standard module. The Hilbert-Schmidt completion model also makes the failure mechanism transparent. This is a useful structural correction and extension rather than a merely cosmetic observation.

## Sources

- Schatten norms on Hilbert C*-modules via pure states (Sajjad Abedi; Mohammad Sal Moslehian): https://arxiv.org/abs/2609.13944 — Primary 2026 source defining the localization for states and stating the broad completeness claim in its abstract.
- Hilbert C*-modules over C*-algebras of compact operators (Damir Bakić; Boris Guljaš): https://www.researchgate.net/publication/238771838_Hilbert_C_-modules_over_C_-algebras_of_compact_operators — Classical structural background for Hilbert modules over compact-operator algebras; it does not state the audited arbitrary-state completeness boundary.

## Limitations

- The result classifies only the compact-operator and commutative algebra classes highlighted by the recent source, not arbitrary C*-algebras.
- It classifies the universal every-module property; individual modules can behave differently when the universal property fails.
- Originality remains subject to older GNS/localization literature that may encode closedness in different terminology, although no equivalent theorem was located.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "explicit_Kl2_counterexample_checked": true,
  "commutative_closed_image_argument_checked": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence; no repository write was performed. Open-access and preprint sources were checked first. No current assigned record required Oxford Download.
