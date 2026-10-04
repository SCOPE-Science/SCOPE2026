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

The symbolic proof uses only the explicitly displayed transformations. Its critical points are: each letter has exactly one collision pair; after any nonempty word the last letter forces omission of one state needed for an effective \(b\); effective \(a\)'s must be separated; equality forces \((ba)^{s-1}\); and the explicit hole induction determines exactly how long that word keeps reducing rank.

`verify.py` reconstructs the automata independently. Exhaustive power-automaton breadth-first search for every \(4\le n\le18\) verifies the target-rank distances through the claimed range, counts shortest words, checks uniqueness for \(s\ge2\), and verifies the strict next-deficiency boundary. Direct replay verifies the hole formula and saturation for every \(4\le n\le200\).

The actual archived run produced `VERIFY_OK`; its complete standard output is stored in `verification_output.txt`.

The finite computations do not prove the theorem for all \(n\); they are consistency checks for the separate symbolic proof. No claim is made for later target ranks beyond the first strict boundary.
