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

# Verification of the modular rank formulas

The proof reduces the bilinear operation to a free module over a product of local truncated polynomial rings and counts all valuation strata including the zero stratum. The coefficient-space verifier `verify.py` directly constructs the multiplication tensor and computes Gaussian-elimination ranks for **all** coefficient vectors in four small prime-field examples. It prints `VERIFY_OK` when each left and right rank distribution and ordered zero-product count matches the theorem.

The cases are \((C_3,\mathbb F_3,-1)\) with \(Z=81\); \((C_4,\mathbb F_2,-1)\) with \(Z=88\); \((C_6,\mathbb F_3,-1)\) with \(Z=26001\); and \((C_{12},\mathbb F_2,-1)\) with \(Z=444928\). These cases exercise Latin, non-Latin, cyclic modular valuation, and nonsplitting separable factors. These finite checks cannot establish the result in general; the proof is the source of the universal quantifiers.

No independent audit or external certification was performed. The theorem does not assert noncyclic modular displacement cases.
