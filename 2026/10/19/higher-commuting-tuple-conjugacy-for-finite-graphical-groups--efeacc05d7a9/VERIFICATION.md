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

# Verification and limitations

The argument in RESULT.md is a universal algebraic proof. The two supplemental scripts provide independently organized finite tests, not a substitute for that proof.

`python check_graphical.py` verifies the claimed orbit-size histogram for all 75 labeled graphs with at most four vertices over \(\mathbf F_2\) and two entries; it also exercises three entries and selected larger graphs and \(\mathbf F_3\) examples. Its matrix-rank path independently constructs edge commutator equations and conjugation maps.

`python check_group_orbits.py` enumerates complete finite groups for the two witness graphs over \(\mathbf F_2\), checks multiplication and inverses, enumerates all 5632 ordered commuting pairs in each, and computes actual conjugation orbits. The observed totals are 2272 versus 1600, with size profiles \(\{1:64,2:2016,8:192\}\) versus \(\{1:256,4:1344\}\).

All tests completed successfully. Results for infinitely many graphs, tuple lengths, and finite fields follow from the proof only. This is not an independently audited result.
