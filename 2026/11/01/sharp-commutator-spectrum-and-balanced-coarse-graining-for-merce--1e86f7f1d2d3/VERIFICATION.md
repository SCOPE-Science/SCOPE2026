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

# Reproducible checks
Execute `python3 scripts/check_mercedes_commutators.py` using Python 3.10+ and only the standard library. The script constructs rational matrix entries from the stated Gram projection, multiplies the effect matrices without using the proposed commutator formula, and checks the resulting commutators against the derived closed identity. It independently enumerates all cardinality profiles for each \(3\le k\le21\) and checks all maximizing profiles. On replay, **6,779 exact rational/integer assertions passed**, with no probabilistic tolerance or floating-point approximation.

The mathematical proof of the all-\(k\) theorem is in `RESULT.md`; computations cover finitely many dimensions and do not certify infinite quantifiers or establish publication priority. The classification is confined to the stated complex Parseval frame family and deterministic binary effects. No independent audit is claimed.
