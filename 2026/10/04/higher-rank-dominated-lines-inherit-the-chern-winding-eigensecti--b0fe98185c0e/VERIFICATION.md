---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification
The verification is analytic and claim-specific.

1. **Domain and quantifiers.** The result is for every ambient rank \(n\ge3\), every strip-admissible analytic sewn cocycle over a Diophantine translation of \(\mathbb T^2\), and every specified invariant line \(L\) that is an extremal one-dimensional block of a two-block dominated splitting \(L\oplus H\). It is not a bundle-wide classification.
2. **Finite-time gap.** For the stable order, iteration gives \(a_r/b_r\le\kappa^r\). Min-max yields \(\sigma_{n-1}\ge b_r\) and \(\sigma_n\le a_r\), so the least singular line is simple for large \(r\) and approaches \(L\) uniformly.
3. **Uniform continuity.** Fixed-time block matrices are uniformly Lipschitz on the real lift by strip holomorphy and unitary sewing. Spectral projection onto the separated least singular line is uniformly continuous. Uniform convergence to \(L\) therefore gives a uniform modulus for the lifted line.
4. **Holomorphic extension.** In affine graph coordinates \(\operatorname{Hom}(L,H)\), the real backward graph transform has Lipschitz factor at most the domination ratio. On a sufficiently thin strip the complex transform remains a uniform contraction on a fixed graph ball. Fixed-center holomorphic iterates converge uniformly in a single projective chart, so the invariant line is holomorphic by Weierstrass convergence.
5. **Gauge and scalar equations.** Pullback of the tautological line over \(\mathbb{CP}^{n-1}\) is a holomorphic line bundle. The strip and its quotient have exactly the Stein properties used in the rank-two normalization, so a real-analytic charge gauge exists. The multiplier is real analytic and zero free; both \(\log|q|\) and the zero-winding phase are real analytic, and the Diophantine Fourier equation solves both.
6. **Final implication.** The Chern obstruction, charge-zero winding obstruction, and abstract existence theorem in arXiv:2609.29577v1 are line-resolved in arbitrary ambient rank. They give necessity and sufficiency after Step 5. For the exact spectrum, any second section on the same line is \(F=rF_0\); Poincaré recurrence on a finite positive level band forces the eigenvalue ratio to be unimodular, ergodicity makes \( |r|\) constant, and Fourier analysis of \(r/|r|\) makes it a single torus character. This yields the dense eigenvalue coset, carried geometric simplicity, and analytic representatives without any ambient-rank restriction.
7. **Reverse order.** If the line is the dominating block, the inverse cocycle over \(-\tau\) reverses the order and preserves the Diophantine condition; the same normalization is then read back for the forward multiplier.

No finite computation, enumeration, timeout, or numerical approximation is used. The unproved limit is only bibliographic: a general analytic invariant-bundle theorem may subsume the graph-transform regularity lemma, but no located source supplied the full higher-rank Chern–winding eigensection criterion.
