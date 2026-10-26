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

The file `verify_extrema.py` requires Python 3 and the standard library only. Run `python verify_extrema.py` in a directory containing that file. Its expected console output is embedded in `verification_output.txt`.

It independently forms transitive closures from all subsets of forward-order pairs under one fixed linear-extension labelling, discards repeated closures, and computes all nonalgebraic one-point types via finite ideal/filter masks and a subset-zeta transform. It verifies the sharp minimum, sharp maximum, second-minimum bound, and exact equality classifications for every such relation with two through six elements. Expected relation totals by size are 2, 7, 40, 357, and 4824. The run terminates with `ALL_CHECKS_PASS`.

This test covers every finite poset up to six points up to isomorphism (each finite poset admits a linear-extension relabelling), but does not prove any statement about larger sizes. The proof in `RESULT.md` establishes the unrestricted identities and classifications by an independent maximal-element argument. No independent scientific audit has been performed.
