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

# Verification of the covariance-positive band theorem

The exact argument in `RESULT.md` proves all integer sizes and frequency pairs without relying on a finite computation. Its essential checks are: normalization of uniform weak-composition probabilities; exact one- and two-coordinate stars-and-bars probabilities; the separate two-category boundary; factorial simplification; the derivative identity and strict monotonicity of its auxiliary function; the strictly subunit limit; and conversion of a one-peaked real curve to a single integer superlevel interval.

The standalone Python 3 script `check.py` independently generates weak compositions and compares all three moments and the normalized ratio against the closed formulas for \(3\le n\le10\) and \(2\le k\le7\), for every admissible distinct positive pair \(r<s\). It also checks the discrete one-peaked and superlevel interval properties for \(3\le n\le50\), with category counts through \(40\), and the six exact values at \((n,r,s)=(10,1,6)\).

Reproduction: execute `python3 check.py` in the directory containing this file. The run returned `PASS 21041 exact assertions` using standard-library rational arithmetic. These tests are finite corroboration, not independent confirmation of originality or a substitute for the symbolic proof. No external independent scientific audit has been performed.
