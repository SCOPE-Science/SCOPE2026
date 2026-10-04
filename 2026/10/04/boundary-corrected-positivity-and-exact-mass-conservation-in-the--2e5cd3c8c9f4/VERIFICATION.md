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

The algebraic proof in `RESULT.md` is primary. The accompanying `verify.py` uses exact rational arithmetic to replay equation (3.1) on deterministic representative states. It checks componentwise nonnegativity, exact conservation of \(S+E+I+R+D\), monotonicity of \(D\), and the boundary counterexample in which the disease-free state remains unchanged.

The replay is finite and therefore is not used as an infinite proof. The universal statement follows from the displayed transfer decomposition in `RESULT.md`. The replay checks transcription and implementation consistency.
