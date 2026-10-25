---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Exact 3-by-3 multiplication gives S^2=SK=KS=K^2=S and KSK^2=K^2; the Drazin definition is met with k=2. For W=H, v=1, Λ=K*, energy is ||K*f||^2; at f=(1,0,-1), it equals 1 while ||S*f||^2=2 and ||S||=sqrt2. The printed A/||S|| bound would require sqrt2<=1. Idempotence and Drazin imply KS=S and S*=S*K*, giving ||S*f||^2<=||S||^2||K*f||^2 and the universal A/||S||^2 guarantee. For arbitrary f=(x,y,z), ratio (|x|^2+|x+z|^2)/(2|x|^2)>=1/2 with equality z=-x, proving sharpness. The positive upper frame bound is B=||K||^2 and is unchanged.

## originality

PASS

Best-of-knowledge: the exact published corollary is false. Its Theorem 3.9 proof implies the corrected inequality after idempotence but not the explicit counterexample or sharpness; the latter constitutes the surviving additional statement. Direct comparison with the full target source and another same-source published theorem found no prior full result. Residual priority risks noted.

## value

PASS

A concrete published quantitative frame-preservation corollary is invalid. The sharp explicit example and norm-level correction give the exact universal constant compatible with its idempotence hypotheses; this matters for interpreting the lower bound in this specialized frame class. Although the proof uses elementary operator estimates, it corrects a definite nontrivial claim rather than an arbitrary tiny computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
