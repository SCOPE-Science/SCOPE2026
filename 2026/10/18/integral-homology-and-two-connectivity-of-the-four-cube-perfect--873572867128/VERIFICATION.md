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

# Verification of the four-cube perfect-matching result

Execute `python3 q4_verifier.py` in a directory containing that file; it needs Python 3 standard library only and no downloads. `CHECK_OUTPUT.txt` reproduces the complete output from the script's actual execution.

The script independently implements (i) exhaustive enumeration of the 272 perfect matchings, their 30,561 faces and dimension counts, (ii) an explicit face-poset matching and a complete directed Hasse acyclicity test, (iii) certified elementary free-face collapses, and (iv) alternating-sign **integer** boundary matrices followed by exact unit-pivot chain contractions. The observed critical cells occur only in degrees zero, three, four and five, so \(\pi_1=\pi_2=0\). The signed integral reductions leave ranks 54 and 21 in degrees three and four, with **identically zero** residual boundaries.

All assertions completed successfully. The enumerated example is finite and all computations are exact integers; no infinite-family generalization, integral equivariant action or sphere-wedge homotopy type has been checked. The code is reproducibility evidence, not an independent external mathematical audit.
