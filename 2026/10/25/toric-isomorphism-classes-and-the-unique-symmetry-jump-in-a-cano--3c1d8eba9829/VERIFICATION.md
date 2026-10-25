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
Run `python verify_fan_isomorphism.py` in an environment with SymPy. The program enumerates all \(40320\) permutations of eight rays, obtains exactly eight cone-preserving permutations, forms the unique candidate lattice map for each, computes Gröbner bases of all ray-coordinate constraints, and asserts the two non-unit ideals \((a-b)\) and \((a+b+4)\), with unit ideals for the other six. It also checks determinant one and the inverse composition of the explicit reflection. A successful run prints `VERIFY_OK`.

This finite enumeration is exhaustive over the finite combinatorial automorphism group, while the polynomial identities prove the asserted parameter conditions for every integer pair. It does not verify abstract non-toric isomorphism classifications, nor the source's separate tensor-generation theorem.
