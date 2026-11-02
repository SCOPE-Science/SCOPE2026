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

# Verification of the finite tests

Run `python3 checker.py` with standard-library Python 3. This tests complete binary target sets for the two canonical witnesses at parameters up to nine, every binary target of critical lengths in substitution ranks one through five, and greedily computed shortest-absence counts for ranks one through eleven. It independently checks the claimed three exceptional strings at odd ranks and the unique exceptional string at even ranks. Observed result: all checks passed.

The infinite-rank theorem is mathematical, not an inference from the finite tests. The proof explicitly handles the base rank, both parities, all binary target strings of the critical length, and the defining recurrence. No separate independent audit or formal machine certification has been carried out.
