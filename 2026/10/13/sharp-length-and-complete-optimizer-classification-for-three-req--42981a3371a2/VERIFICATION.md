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

# Reproducible verification

Execute `python3 verify.py` with `verify.py` and `witnesses.json` in the same directory. The program uses only Python's standard library, exhausts every nonzero-column binary three-row generator-column multiset at lengths \(7\) and \(8\), and computes its maximal exchange-closed family of disjoint complete histories.

The program verifies: no seven-column asynchronous encoder; exactly 79 eight-column encoders; literal minimal recovery masks and every zero-, one- and two-set history of each of 79 witness choices; 17 orbits under permuting the three message labels; multiplicity signatures 48, 24, and 7.

Actual packaged-file execution returned:

`VERIFY_OK: n=7 none; n=8 exactly 79 in 17 message-permutation classes; all 79 strong witnesses; profiles 48+24+7`

No completion beyond length eight is asserted. The claim that shorter lengths are excluded uses monotonicity under appending unused columns; the implemented exhaustive search alone does not inspect lengths below seven.
