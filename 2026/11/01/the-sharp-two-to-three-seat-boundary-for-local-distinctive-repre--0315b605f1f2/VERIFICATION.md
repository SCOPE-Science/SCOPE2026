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

# Finite verification and analytical boundaries

Execute `python3 verify.py` with Python 3.9 or later. The program enumerates all election candidate-support subsets with nonempty, distinct supports on up to five labeled voters, at most five labeled candidates, and two committee seats. It independently tests the source's JR and local-exchange definitions and the theorem's feasibility criterion. It then tests seeded pseudorandom elections allowing duplicate supporter sets, and the explicit six-voter, five-candidate three-seat example.

Observed result:

`VERIFY_OK two_seat_unique_support_profiles=211380 random_profiles_including_duplicates=18000 three_seat_distinct_support_witness=6v_5c`

These tests are finite; the proof in RESULT.md establishes all finite electorate sizes. The source's numerical example with four seats is not replayed. No external certificate, formal proof assistant, or independent audit is claimed.
