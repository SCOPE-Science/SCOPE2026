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

Run `python3 verify.py` with Python 3.8+ (standard library only). The program checks eighteen field, weight, and dimension combinations: characteristic three, five, and seven; weight zero and one; and unequal/equal radical dimensions. It constructs the full unital tensor-product multiplication and both oriented operators, checks every basis-pair Rota–Baxter identity and the normalized quadratic relation, and calculates ranks by modular Gaussian elimination.

For the nontrivial unequal-dimension examples, the full algebra has dimension \(15\) and both orientations have rank \(7\). For nonzero weight with scalar operators, it checks the rank-balanced flip-compatible case of dimension \(6\). The expected final output is `VERIFY_OK`; the program was executed successfully on the packaged source before packaging.

The finite-field enumeration does not prove the all-field theorem, does not enumerate all automorphisms in dimension \(15\), and does not independently certify novelty. Nonisomorphism for unequal radical dimensions follows from the radical-square argument in the mathematical proof.
