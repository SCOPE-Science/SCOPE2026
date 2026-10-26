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

The accompanying standalone script `johnson_edge_verify.py` builds the full binary adjacency matrices, removes the selected single edge, and computes exact binary ranks and orbit dynamics. Its recorded output is `verification_output.txt`, ending with `JOHNSON_EDGE_DEFECT_VERIFY_OK`.

The exhaustive checks cover all configurations for \((n,k)=(4,2),(6,2),(6,4)\), with non-exhaustive exact matrix checks through \((10,6)\). Matrix identities and rank checks use arbitrary-precision binary vectors. No finite enumeration is treated as a proof of the quantified infinite family; the algebraic argument is in `RESULT.md`.
