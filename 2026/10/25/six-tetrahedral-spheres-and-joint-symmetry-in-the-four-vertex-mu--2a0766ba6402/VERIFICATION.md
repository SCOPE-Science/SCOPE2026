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

# Reproducible verification

Run `python3 check_omega4.py` using Python 3 without additional packages. The checker enumerates the complete finite family of faces, validates the decomposition into six tetrahedron boundaries, constructs the connected incidence graph, and confirms both \(S_4\times C_2\) character rows in each of two homological degrees. It verifies the exact Specht multiplicities by integer inner products with the ordinary \(S_4\) character table. The proof of the integral wedge type is conceptual and appears in `RESULT.md`; the checker validates its finite combinatorial hypotheses rather than asserting an unverified homotopy computation. No larger \(n\) cases or independent audit are claimed.
