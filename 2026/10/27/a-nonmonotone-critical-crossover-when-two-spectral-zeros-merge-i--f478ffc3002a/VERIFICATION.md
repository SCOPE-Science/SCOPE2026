---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The frozen proof stated a false complex square-root equality in §3 (already false at q=0); its real-part version and the theorem are correct. The complete replacement RESULT.md under repairs/4 uses i/sqrt(−q+2i)=conj((q+2i)^(−1/2)) on the principal branch. Independent recheck: summing the two covariance lags yields the stated positive diagonal variance. The factorization by s=r/(v+W), with |s|<1 since Re(v conj W)>0 and (v+W)(v−W)=r², gives angular log-mean 2 log|v+W|. Differentiation at fixed epsilon gives the exact formula with rv'−v=−c−i/(2δ). The scaled radicands remain uniformly in a compact neighborhood in the upper half-plane for bounded lambda; analyticity of the inverse square root gives the asserted absolute remainder. The conjugation identity preserves the real-part profile. Its derivative in q=lambda² is proportional to −cos(3 arg(q+2i)/2), crossing from positive to negative at q=2/sqrt(3). Direct evaluation gives the correct height and endpoint/tail constants. The repaired theorem makes no finite-radius or global moving-parameter optimization claim. The unmodified finite checker is diagnostic and was not executed.

## originality

PASS

Credit the published exact integral machinery and both fixed-parameter regimes. The supported distinct claim is the uniform joint-merger profile including its strict nonzero-separation maximum. The repaired branch argument leaves this claim unchanged.

## value

PASS

The competing length scales arise intrinsically from this degeneration, not from an arbitrary parameter slice. The profile, uniform error and exact positive optimizer quantify an unexpected effect: separating the double zeros on the critical scale can produce a stronger leading deficit than exact collision. The endpoint asymptotics alone do not answer it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
