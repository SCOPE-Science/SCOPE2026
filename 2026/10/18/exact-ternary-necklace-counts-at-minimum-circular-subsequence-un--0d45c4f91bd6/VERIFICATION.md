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

The mathematical proof is in `RESULT.md`. It establishes all assertions for every positive integer \(k\); finite experiments do not replace that proof.

Run `python3 verify/check.py` with a standard Python 3 interpreter. The checker enumerates all ternary words of length \(3k\) for \(k=1,2,3,4\), tests every phase directly, constructs rotation classes directly, and compares with the closed formulas. At \(k\le3\), it also tests each possible cyclic rotation for all \(3^k\) scattered target words without using the phase lemma. It checks primitive periods and phase-layer numbers.

Expected final line: `TERNARY_CIRCULAR_EXTREMAL_PASS`. Observed labeled counts: 6, 78, 582, 3750; necklaces: 2, 14, 66, 320; primitive necklaces: 2, 12, 64, 306. No external files or software packages are needed.

This checker does not certify all infinitely many \(k\) or the absence of equivalent prior results. Independent audit status remains unperformed.
