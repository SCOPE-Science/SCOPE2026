---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Proposition 2, Eq. (6) uses Aθ=1+(3−2q)θ; Theorem 1, Eq. (9) instead defines A=4−2q and specifies the real lower branch. With b=(2−q)θ, z=−bx and q′=1/(2−q), the true inverse satisfies (z−Aθ)exp_q′(z)=−Aθ(1−u). Setting κ=1+(1−q′)A, substitution w=(z−A)/κ verifies that the printed expression solves this equation with A=4−2q rather than Aθ: the two positive bases factor as 1+(1−q′)z=κ[1+(1−q′)w]. When κ>0 and A>1, z<0 implies w<−A/κ<−1/(2−q′), the decreasing (lower) branch, whose endpoint value at z=0 corresponds to u=0 and whose other endpoint to u=1. The printed κ is positive throughout the admissible q intervals. Subtraction gives the stated exact residual, strictly signed as θ−1 for 0<u<1. As an exact check, for (θ,q)=(2,4/3) the printed inverse at u=3/8 gives x=3/2 but the true CDF there is 9/20. With the corrected Aθ, κ=(3−2q)[1−(q−1)θ]/(2−q); the shift divides by zero at κ=0 and loses its positive base at κ<0. Neither prevents monotone numerical CDF inversion: for s=1+(q−1)θx and p=(2−q)/(q−1)>1 on the unbounded side, the survival derivative in s has the sign of (1−p)s−(Aθ−p)<0 for s≥1, regardless of κ. On the bounded side, s=1−(1−q)θx decreases from 1 to 0, and s^p[1+(p/Aθ)(1−s)] for p=(2−q)/(1−q)>1 is strictly increasing in s on (0,1). The four reported medians were independently reproduced by bisection (python /workspace/checks/independent_formula_checks.py); supplied checker inspected without execution. No inference is made about private simulation code.

## originality

PASS

No checked distinct result covers the source-specific wrong constant, the resulting exact coverage error across the admissible parameters, or the limitation of the shifted remedy. The Lambert–Tsallis inversion device is prior and not credited as new. This is a best-of-evidence determination, not a comprehensive priority claim.

## value

PASS

This identifies the law that the published sampler actually generates if implemented literally, rather than just correcting notation. All four simulation designs are affected; for example the nominal median in the fourth design has actual coverage approximately 0.379. The exact residual and the real-domain boundary tell implementers both when the error occurs and when a simple constant replacement must be replaced by a different inversion method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
