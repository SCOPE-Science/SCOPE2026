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

# Verification protocol

The scientific argument is in `RESULT.md`, especially its multiplication equation, kernel-coordinate identity, and conditional counting proof. The numerical verifier is `CHECKER.py`, requiring standard Python 3 only. Run `python3 CHECKER.py` in a directory containing that file and compare its final line with `CHECK_OUTPUT.txt`:

`ALL_QUIVER_ANNIHILATOR_CHECKS_PASSED 37 26595`

The checker constructs a matrix for the map \(b\mapsto ab\) from the algebra's multiplication table for every examined element; it then computes the matrix rank by modular row reduction. It separately computes the predicted annihilator-dimension polynomial from subsets of vertex labels and compares every coefficient. Test cases cover loops, parallel arrows, opposite arrows, short cycles, isolated vertices, stars and paths, and prime fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). Direct enumeration does not establish the theorem in arbitrary dimensions, for nonprime finite fields, or for all quivers; these rely on the characteristic-independent coordinate proof.

To reproduce the strict star/path nullity difference, the verifier implements the independent height-two zero-product pair formula and checks the polynomial identity at eleven distinct integers. Both sides are polynomials in the field-size indeterminate of degree at most \(10\), so agreement at eleven points is an exact symbolic identity, not merely a sample extrapolation. The checker also verifies that reversing the star changes its right-annihilator spectrum while preserving its scalar zero-product count.

No independent audit has been performed.
