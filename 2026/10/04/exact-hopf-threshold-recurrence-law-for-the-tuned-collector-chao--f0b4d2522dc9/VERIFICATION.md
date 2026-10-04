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

The proof uses the published normalized vector field with \(y_{12}=y_{22}=0\). The critical algebraic checks are: \(\dot q=x\) for \(q=y-Mz\); the exact storage derivative \(\dot H=((\beta-MY)/(MY^2))z^2+(\alpha/(MY^4))z^4\); the characteristic-polynomial factorization at \(\beta=MY\); and the exact source-parameter value \(K=14574087/1000000\).

`verify.py` replays the numerical specialization with exact rational arithmetic and evaluates the differential identity at several exact rational states. Its output is `VERIFY_OK`. The general cancellation is proved symbolically in `RESULT.md`; finite state checks are only implementation checks and are not treated as an infinite proof.

The verification does not establish existence or uniqueness of a chaotic attractor for \(\beta>MY\), nor does it independently audit the source's numerical Lyapunov exponents or experiments. Independent audit is not performed.
