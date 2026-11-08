---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

One-block symmetry gives alpha_n=E[X_i sgn(sum X)]=E|sum X|/n=4^{-floor(n/2)} binom(2floor(n/2),floor(n/2)). For F=Q+R with higher Walsh degree, orthogonality fixes E(QF)=E(Q^2)=product n_j, while |E QF|<=||F||∞ E|Q|; independence produces lower bound product 1/alpha_nj. Each block-sign has only odd-degree characters, first-level coefficient alpha_n; their product has only degree>=r and exactly the Q degree-r coefficients after multiplying C, attaining bound. Equality forces F=C sgn(Q) where Q!=0, giving unique optimum when each block odd; positive- and negative-deviation identity under |Q|-tilted measure yields stability <=2eps C E|Q|. Stirling gives parity correction (-1)^n/(4n) for fixed r. A fresh exact Fraction Walsh-Hadamard verification independently checked 36 nontrivial block tuples, including even zeros and odd blocks. All-block-size claim follows from Fourier proof, not finite tests.

## originality

PASS

Defant et al. Theorem 3.1 establishes a projection constant in a Walsh spectral subspace expressible as E|character sum|, a different operator invariant, not a specific affine coset quotient norm or uniqueness/stability. Eskenazis–Zhang treats approximation by Walsh tails, largely L1 and general comparison inequalities, but no inspected theorem yields the product formula for these disjoint-block chaoses. Direct duality and sign-products are elementary, so similar tensor-product extremal constructions may exist historically.

## value

PASS

The exact coset norm and sharp optimizer characterize a natural rank-one multipartite Walsh chaos where the degree-r polynomial has very large supnorm but a much smaller minimum representative. Rigidity, stability, and parity correction add useful structure, beyond a bare known Khinchine estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
