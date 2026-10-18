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

# Reproduction
Use Python 3.9 or later and run `python3 verify.py` from the directory containing the supplied file. No nonstandard dependencies or source downloads are required. The program must print `VERIFY_OK` followed by exact class-character and multiplicity vectors.

The tested complete cubical chain-group dimensions are \((455,1560,1650,520)\). The integer boundary-square test is exact. Sparse elimination modulo three produces boundary ranks \((454,1100,520)\), and an independent modulo-two cross-check yields \((454,1099,520)\). The homological rational upper-bound argument using the surjection onto graph-cycle homology is required in addition to those modular computations; modular elimination alone does not prove the characteristic-zero second-boundary rank. This upper bound is reconstructed in the proof and checked numerically against the finite rank certificate.

For the class order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), the program verifies the rational \(H_1\)-character \((6,0,-2,0,0,0,1)\), degree-two character \((30,0,-2,0,0,0,0)\), and seven Specht multiplicities \((0,1,1,2,1,1,0)\). It also checks the total Specht dimension of thirty.

The code is an exact finite verifier, not a complete automation of the cited graph-discretization theorem or of the topological naturality of the motion-to-graph homomorphism. No independent scientific review is asserted.
