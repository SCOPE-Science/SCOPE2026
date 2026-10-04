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

Run `python3 verify_d63.py` in the directory containing this file and the verifier. The script is standard-library only and performs the following checks from definitions rather than loading a precomputed face table:

1. Enumerates all \(2^{15}=32768\) simple graphs on six labeled vertices.
2. Computes the domination condition both by exhaustive dominating-set search and by the logically equivalent direct exclusion of dominating sets of sizes one and two; it requires agreement on every graph.
3. Reconstructs exactly \(4502\) nonempty simplices and checks the face vector \((15,105,455,1185,1647,915,180)\), downward closure, and the canonical face-list SHA-256 digest.
4. Constructs each simplicial boundary map over \(\mathbb F_2\), checks boundary-of-boundary is zero, and performs exact binary Gaussian elimination.
5. Requires boundary ranks \((14,91,364,821,711,180)\), Betti vector \((1,0,0,0,115,24,0)\), and Euler characteristic \(92\).

A successful replay terminates with `VERIFY_OK`.

The verification is finite and exhaustive for the stated mod-2 claim. It does not compute integral Smith normal forms, attaching maps, or the full homotopy type.
