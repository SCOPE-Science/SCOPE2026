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

The manuscript proves the theorem directly; its exhaustive computations are supporting checks, not a source of inference from finite to infinite cases.

Run `python3 verify_rectangle_invariants.py` to check all ordered factor pairs with side lengths from one to eighteen, directly compute order ranks and incomparable rank spectra, reconstruct both factor lengths, and verify a separate maximal-rank-gap formula. The recorded output reports 324 cases and 1,877,922 ordered incomparable pairs with all assertions passing.

Run `python3 verify_fo2_types.py` to perform an independent global two-variable, noncounting refinement across 45 unlabelled rectangles with side lengths at most nine. The exact theory counts at depths one through six are 4, 8, 17, 32, 44, 45. The recurrence uses sets of neighbor-type pairs, not multiplicity counts.

Both scripts are standalone Python 3 without third-party dependencies. Their text outputs are embedded as `invariants_output.txt` and `fo2_types_output.txt`; rerunning each script produces these texts byte-for-byte in the tested environment.

No independent audit or external formal verification was performed. The argument does not claim depth optimality, identification among arbitrary posets, or a theorem for three or more chain factors. The current published-literature comparison is bounded and cannot certify exhaustive priority.
