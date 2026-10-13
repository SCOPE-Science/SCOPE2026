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

# Verification and reproducibility

The mathematical proof is in `RESULT.md`; the following are bounded finite checks, not substitutes for that proof.

Run `python3 checker.py`: it generates every reduced-row-echelon subspace of the ambient algebra for the tested fields and numbers of leaves, checks closure under all products of basis vectors, and compares the resulting dimension distribution with the three-family formula. Tested parameter pairs were \((q,m)=(2,1),(2,3),(2,5),(3,1),(3,2),(3,4),(4,1),(4,3),(5,1),(5,2),(5,3),(7,1),(7,2)\). The script printed `VERIFY_OK`.

Run `python3 polar_check.py`: it reconstructs the product-formula isotropic Grassmannian counts, comparing them with direct reduced-row-echelon isotropic-subspace enumeration in odd characteristic and in characteristic two. It printed `POLAR_OK`.

For example, the independently enumerated dimension vectors were \((1,4,4,3,1)\) for \((q,m)=(2,3)\), \((1,8,16,5,1)\) for \((4,3)\), and \((1,0,1,1)\) for \((7,2)\). These are vector-space counts of distinct subalgebras by increasing dimension, with the zero subalgebra included.

No computations address fields or graph families outside the theorem's hypotheses, and no exhaustive finite run proves a universally quantified statement. The characteristic-dividing-\(m\) case is deliberately unclaimed.
