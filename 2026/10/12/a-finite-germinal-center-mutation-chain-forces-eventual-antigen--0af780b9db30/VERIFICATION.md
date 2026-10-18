---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The analytic proof in `RESULT.md` applies for every finite \(n\ge2\), the domain where the distinct \(B_1\) and terminal \(B_n\) equations are unambiguous. For those lengths, the weighted quantity
\[
Q=B_0+\sum_{i=1}^n\alpha^{-i}B_i+\alpha^{-n}P
\]
has derivative
\[
\dot Q=-d\left(B_0+\sum_{i=1}^n\alpha^{-i}B_i\right)\le0.
\]
Direct summation gives \(\dot{(N+H+G)}\le s_N-m(N+H+G)\). The positive variations-of-constants through \(H,G,B_1,\ldots,B_n\) establish \(B_n(t)>0\) and \(P(t)>0\) for \(t>0\). The exact antigen equation then provides exponential decay after each \(t_0>0\). The original packaged numerical/algebraic verifier can corroborate cancellation identities at sampled chain lengths, but neither a finite test nor a `VERIFY_OK` flag establishes the universal long-time limit. No assertion is made for the undefined \(n=1\) degeneration without a further model convention.
