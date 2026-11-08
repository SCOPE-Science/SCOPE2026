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

Reconstructed exact identity E||e+||²= eᵀ(I-Aᵀdiag(p)A)e and equivalence diag(p)≽λ(AAᵀ)^-1 for 4×4 invertible A. Reduction to min trace diagonal PSD majorant of C and dual max trace(CX), X PSD diag 1, valid by Slater. For t≤1/3 provided q and X=all-ones and reversal blocks B+=(1,-1;-1,1), B-=(1-2t,-1;-1,3) with determinant 2-6t≥0. For t≥1/3 planar correlation Xij=cos((i-j)θ), cosθ=sqrt((t+1)/(4t)), q pair values 2twc/2wc, dual slack reversal blocks determinant 0 and nonnegative diagonal. Exact complementary slackness and dual equality; uniqueness follows from SX=0 and diagonal entries of X. Independently checked symbolic PSD certificates, matching primal/dual and five rational t including boundary and high t; inspected verify_signed_cycle.py. Existence of normalized rows given by IFT for small w, explicit t=1 example. Distinguishes one-step minimax from long horizon.

## originality

PASS

Best-of-knowledge qualified PASS after comparing mathematical implications, high-relevance primary material and related Resultary records; no decisive prior domination identified. Residual risks explicit.

## value

PASS

Determines the exact optimal row sampling distribution in a nontrivial, motivated signed-frustrated inverse Gram regime, with a sharp universal rank-change threshold and uniqueness. This is useful when designing static randomized Kaczmarz steps, not merely generic SDP duality or a numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
