---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

With deg Q=m>=1, all Q-roots on unit circle, deg P<=m, the m-reversal satisfies Q#=κQ with |κ|=1, hence on circle overline(P/Q) Q²=κ^{-1}QP#, a nonsingular polynomial. For F_j=z^jQ², the adjoint Toeplitz operator T_barφ maps it to κ^{-1}z^jQP#; this polynomial belongs to domain T_φ and maps further to κ^{-1}z^jPP#. The de Branges–Rovnyak norm identity <f,g>_H(b)=<f,g>_H²+<T_barφ f,T_barφ g> yields <F_j,z^k>=coefficient w_{k-j} of W=Q²+κ^{-1}PP#. In finite monomial Gram M_N, all rows j<=N-2m of Q(B_N)²M_N coincide with upper Toeplitz band T_N(W); last 2m rows differ and residual rank<=2m. Handles repeated poles, complex coefficients, P=0, N>=2m; no assumption that original M_N is banded.

## originality

PASS

Qualified PASS for explicit arbitrary boundary-pole and multiplicity all-order Gram transformation with constant band diagonals and a 2m-row correction. Dellepiane–Seco 2026 §§4.2–4.3 treat a second-order single pole and discuss an all-order generalization but do not establish the exact polynomial W or all boundary-pole sets. Hartmann–Lamberti multi-boundary-pole decompositions and higher local Dirichlet literature do not give this transformed finite Gram matrix identity in inspected material. Known Toeplitz adjoint identity remains foundational prior work.

## value

PASS

The exact finite-band symbol resolves a motivated higher-order Gram structure question raised by prior orthogonal-polynomial work, with all poles/multiplicities and uniform boundary rank. It provides concrete symbolic input for Gram–Schmidt/orthogonal polynomial computations and a structural lemma beyond a textbook adjoint identity. Does not claim explicit orthonormal polynomials or exact boundary rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
