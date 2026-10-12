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

# Reproducibility and verification

Running `python3 verify.py` uses the Python standard library only. It reports 951 exact-rational checks: all binary trajectories through 12 attempted updates at five rational transmission probabilities; exact matching of the renewal and cubic recurrences through 15 updates; the two-success absorbing-state identity; the critical factorization and limiting residue; and a rational isolating interval for the growing root at \(p=1/2\).

The asymptotic classification is proved analytically by the positive renewal kernel, strict dominant simple pole and rational coefficient asymptotics. The finite verification does not establish asymptotic uniqueness or exhaustive validity for all real \(p\); those statements follow from the proof in `RESULT.md`. This is a self-review, not independent validation.
