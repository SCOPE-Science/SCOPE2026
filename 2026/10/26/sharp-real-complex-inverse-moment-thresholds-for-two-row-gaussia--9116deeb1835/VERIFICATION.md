---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The convolution map from m+1 Gaussian coordinates to a fixed row combination has all nonzero singular values uniformly bounded below: its Toeplitz Gram eigenvalues are 1+2|ab|cos(kπ/(m+1)), so the lower bound is 1−cos(π/(m+1))>0. Spherical small-ball probability for a fixed row direction is O(t^{βm}); a projective β-dimensional t-net yields O(t^{β(m−1)}). A geometric-progression rank-one locus has residual coordinates with triangular Jacobian one and a bounded-density chart giving matching lower power. The independent Gaussian radius has the required negative moments. Layer-cake gives E||H†||^p,Eκ^p finite exactly p<β(m−1), divergent including equality. Verified algebraic rank and covariance bounds independently; 808 finite exact/numeric checks do not prove probability asymptotics.

## originality

PASS

Independent statement/implication comparison including direct mathematical object parameters and available primary material: Rank deficiency equals a geometric progression; column reversal is a Toeplitz alias, and projective tube probabilities rephrase the claim. Rudelson–Vershynin (arXiv:0802.3956, Theorem 1.1) requires independent matrix entries, violated by overlapping Hankel rows. No matching structured fixed-two-row moment theorem identified. Schmitz et al. arXiv:2402.13090 concerns data Hankel conditioning and computational control; Coulson–van Waarde–Dörfler arXiv:2205.06636 concerns robust persistent excitation; Lawrence et al. arXiv:2310.14098 considers increasing samples. Almost-sure full row rank does not imply integrable inverse singular values; none of the inspected theorem scopes mathematically implies the finite-m cutoff.

## value

PASS

A finite-column, dependence-aware exact inverse-moment frontier for the smallest nontrivial Hankel input design; the real versus complex transition matters for quantitative conditioning, rather than merely almost-sure rank. Does not directly imply a closed-loop control bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
