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

# Verification instructions and limits

Run `python3 check.py`, then compare its UTF-8 standard output byte-for-byte to `verification.json`. Both files are present in this package. The script uses only the Python standard library and its graph edges are constructed directly from the stated cyclic-index definition.

Checks performed: all 16,384 vertex masks, two independent component algorithms, all four complete vertex-toggle matchings, all 69,083 directed face incidences in aggregate, four acyclicity topological sorts, independent mod-two homology ranks, signed simplicial Lefschetz traces for all dihedral conjugacy classes, and full boundary-matrix persistence over the filtered 6,475 nonempty faces of cutoff four. The critical-cell distributions give full **integral** homotopy types by discrete Morse theory; mod-two calculations alone would not. The script asserts every numerical value in the result.

This verifies a finite, fully specified graph at precisely four cutoffs, not a family statement. The six degree-six persistent classes are survivors only **through** cutoff four, not infinite bars. The integral degree-five inclusion is known to be injective, but its index in an ambient direct summand has not been determined. Verification and this self-review are not independent mathematical auditing.
