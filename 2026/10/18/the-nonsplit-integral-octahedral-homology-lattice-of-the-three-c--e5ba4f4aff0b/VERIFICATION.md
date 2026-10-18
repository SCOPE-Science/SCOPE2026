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

# Reproduction of the three-cube matching-homology calculation

Run `python3 verify.py` with SymPy. The script independently constructs every cube edge and every matching face from binary adjacency, computes exact boundary ranks and both explicit integer unit minors, and constructs an integral quotient basis. It checks boundary compositions, evaluates all \(48\) graph automorphisms on oriented faces, compares the Lefschetz and quotient-basis character calculations, and verifies the integral antipodal eigenlattice index. The expected last line is `VERIFY_OK`.

The result is finite and exact. No floating-point arithmetic, random search, outside solver, or inaccessible saved certificate is needed. The complete finite calculation proves the stated assertions for this twelve-edge graph, not for all hypercubes. Bibliographic uniqueness cannot be established by computational verification alone. Independent scientific audit has not been performed.
