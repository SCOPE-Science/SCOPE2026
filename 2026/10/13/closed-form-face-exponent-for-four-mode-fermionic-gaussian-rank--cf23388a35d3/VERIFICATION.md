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

The proof is analytic. On the face \(w_3=0\), diagonalizing each two-by-two Gram block yields the same internal binary entropy \(h(\theta_t)\). The Gibbs variational inequality then bounds the face objective by
\[
\Phi_t(r)=\log\frac{1+4N_t r+3N_t r^2}{(1+r)^4}.
\]
The unique positive stationary point solves
\[
r(1+r)=\frac{2(N_t-1)}{3N_t},
\]
and the Gibbs weights at this point satisfy the exact mean-degree self-consistency relation, proving attainability rather than merely an upper bound.

The packaged script `artifacts/verify.py` checks the closed form, stationary equation, self-consistency, entropy equality, and strict positivity for several values of \(t\); it also compares against a dense grid of face weights and checks convergence of \(\log\widehat B_t/h(\theta_t)^2\) toward \(4/3\).

The finite grid and numerical asymptotic checks are not used as proofs. They are regression tests for the symbolic derivation. The checker does not assess the full four-weight maximization and does not establish that \(\widehat B_t=B_t\).
