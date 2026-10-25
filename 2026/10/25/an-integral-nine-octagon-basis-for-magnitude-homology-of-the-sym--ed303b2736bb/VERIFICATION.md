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

# Exact reproduction

Execute `python magnitude_gq3_checker.py` using Python 3.10+ with `sympy==1.14`. The code constructs all 40 points, 40 lines, and metric distances, then all endpoint chains in length five. It certifies the complete integer Smith invariant multisets (18,63) at incident endpoints and (28,50) at nonincident endpoints, each invariant one. The augmented nine-cycle matrix has 59 unit Smith factors. It verifies the two point–line automorphism orbits and their sizes, and the 25920 global rank.

# Limits

Smith normal forms certify the finite chain computations but do not establish a formula for arbitrary quadrangle order. The proof is computer-assisted and has not been independently audited.
