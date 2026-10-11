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

The mathematical proof is self-contained in `RESULT.md`. Its critical steps are:

1. every positive continuant of total weight \(c\) is generated from \((1,1)\) by \(c-1\) coordinate-sum steps;
2. keeping the larger previous coordinate is future-dominating and produces \((F_{c+1},F_c)\);
3. when \(c\equiv2\pmod3\), an odd numerator must deviate from that even extremum, and the first effective deviation loses at least \(F_{c-4}\);
4. explicit positive rational diagrams attain both formulas;
5. Kim--Morifuji's published Example 4.5 then gives \(\mathcal N\le16M_c^2\).

`verify_bound.py` exhausts all positive compositions only for \(3\le c\le18\). It verifies the claimed maxima and witnesses on that finite range and prints `VERIFY_OK c=3..18 exact_odd_continuant_max`. This finite computation does not certify the infinite theorem and is not used to replace the symbolic argument.

Scientific limits: the determinant extremum is for two-bridge knots; the monic-character corollary requires the stated component hypotheses; no attainment of the character-count upper bound is claimed.
