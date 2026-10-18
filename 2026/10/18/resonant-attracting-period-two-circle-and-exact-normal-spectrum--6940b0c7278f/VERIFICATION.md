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

# Verification record

The proof is self-contained in `RESULT.md`: normalized synchronized restriction; exact weighted-attention derivative cancellation; orthogonal common/zero-sum tangent decomposition; two-step spectral values; and uniform normal contraction with an asymptotic phase.

Execute `python3 verify.py` with Python 3 and NumPy installed. The checker directly evaluates the full nonlinear normalized multihead softmax map. It checks 135 configurations (three dimensions, three token counts, three head counts, and five phases), including random non-symmetric per-head matrices with their effective sum constrained to a randomly rotated symmetric spectral example. Each case checks the exact two-step return and all intrinsic eigenvalues by centered finite differences. In the saved package it reported a maximum Floquet eigenvalue residual of `1.46e-09` and passed three exact rational checks. All test cases are finite; they corroborate the calculations but do not certify the all-parameter theorem.

Analytically, the only strict inequalities needed are \(r>1\) and \(|1+\eta_c\lambda_j|<r\) for each interior eigenvalue. Both follow from the simple endpoint spectral hypotheses. Normalization is locally well-defined because its unperturbed norm is the constant \(r>0\). The proof's convergence assertion is local and has no claim of finite-time synchronization or universal attraction from distant initial states.

Independent audit has not been performed.
