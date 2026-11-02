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

# Reproducibility and boundaries

Execute `python verify.py` with Python 3 (standard library only) from the folder containing this file. The script enumerates all matrices over the prime fields of sizes 2, 3, 5, 7 and the nonprime field with four elements using \(X^2+X+1\). It computes the homogeneous binary cubic discriminant exactly and recognizes the triple-root family separately. The expected (reduced, double-plus-simple, triple) counts are \((6,0,0)\), \((36,8,4)\), \((180,0,0)\), \((400,64,16)\), and \((1764,216,36)\). All were reproduced.

The universal claim for every finite field rests on the symbolic classification of repeated binary-cubic roots, not these enumerations. No independence claim or external audit is made.
