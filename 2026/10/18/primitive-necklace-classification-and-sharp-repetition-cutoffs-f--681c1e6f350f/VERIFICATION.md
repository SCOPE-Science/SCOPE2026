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

# Verification record

Execute `python3 verify.py` with Python 3 (standard library only). The program enumerates all rotation classes of binary circular words of lengths \(1\) through \(9\) and ternary circular words of lengths \(1\) through \(6\). It computes complete two-pebble semantic types by stabilization of atomic pair types under existential rebinding of each of the two variables. It compares the predicted primitive-root/capped-exponent classes against the stable semantic classes in both directions.

Observed run: `FO2_CYCLE_VERIFY_OK binary=153/140 ternary=225/219`. There were no predicted-class splits or merges in either bounded census. This provides finite diagnostic corroboration, not proof of the general theorem.

The mathematical generality comes from the factor-language argument and the matching-residue/matching-atomic-type two-pebble back-and-forth system in `RESULT.md`. The cases primitive length \(1\), \(2\), and \(\ge3\) are handled separately; the exact boundaries are distinguished by explicit two-variable sentences. No external independent audit or formal certification was performed.
