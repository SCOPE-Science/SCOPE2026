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

# Verification details

The proof in `RESULT.md` covers every length and every four-tuple of nonnegative zero gaps. `verify.py` is an independently formulated direct factor-composition enumeration using only the Python standard library. Run `python3 verify.py` in the directory containing the package files. It computes the **sets of factor Parikh vectors** directly from substrings and groups all weight-three words of every length 3 through 24. It asserts equality of every computed reconstruction fiber with the claimed gap-swap class and of every fiber-size count with the stated formula.

Recorded output: `PASS: all 12650 three-one words at lengths 3..24, all 5927 Parikh-set classes; every fiber and three class-size counts match.`

This finite check does not establish the theorem for arbitrary word lengths; that conclusion follows from the proof using exact threshold formulas for all nonnegative gaps. Public-literature searches cannot eliminate all unindexed equivalent results. Independent audit and independent mathematical validation have not been performed.
