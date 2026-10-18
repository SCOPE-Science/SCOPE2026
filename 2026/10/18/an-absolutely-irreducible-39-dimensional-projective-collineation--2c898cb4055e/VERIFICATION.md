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

# Reproducible checks and scope

Use Python 3 with no third-party dependencies. `python noncover_morse_check.py 3` reconstructs thirteen projective points and thirteen lines, all 3862 faces including the empty face, the full 1910-pair matching, its complete acyclicity and the signed integral critical-cell boundary. The output confirms one vertex, 39 four-cells and one five-cell, and a zero boundary.

Run `python noncover_character_check.py` to enumerate all 5616 projective collineations, their actions on thirteen points, the fixed-face signed simplicial Lefschetz numbers and the complete eight-row character table. The program checks the exact integer identities \(\sum_g\chi_4(g)=0\) and \(\sum_g\chi_4(g)^2=5616\); the second identity proves absolute irreducibility once the independent theoretical proof of the trivial top-degree character is applied.

The associated text output is `verification_output.txt`. All generated enumerations are finite and exact. The character result is over rational homology and does not certify integral lattice structure or equivariant homotopy equivalence. Independent mathematical audit has not been performed.
