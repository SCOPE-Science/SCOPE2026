---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Exact scalar source reconstruction: H=C, K=I, W=H, ω=2 gives synthesis T_W=2I and minimum-norm X_w=I/2; θ=I/4 satisfies K=ω² θ and weighted square summability, but source Thm4.3 demands 1/4<=1/16 for nonzero f. Source Corollary4.4 inserts factor ω into (π_R(K)T_W)^dagger, giving I vs actual I/2. Repair norm follows T_W{ω_i θ_i f}=Kf and orthogonality of reduced solution to ker T_W. All exact, no numerical assumptions.

## originality

PASS

Exact weight-two counterexample falsifies a particular published K-fusion Theorem 4.3 and the derivative pseudoinverse Corollary 4.4. A separate later relay-fusion counterexample has a similar mechanism but concerns another source theorem and cannot substitute for this exact refutation. No covering prior source-specific correction located; generic Douglas orthogonal least-norm theorem only supplies the repair, not the error claim.

## value

PASS

An exact source-specific refutation of a published minimum-coefficient theorem and its Moore–Penrose corollary, with a fully justified corrected weight geometry, prevents incorrect Hilbert fusion reconstructions. The scalar dimension is minimal to isolate a substantive theorem defect, not a pointless tiny exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
