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

# Exact checks and proof limits

Run `python3 artifacts/verify.py` using Python 3 standard library from the directory containing this document. The checker enumerates all Lagrangian subspaces of the standard four-dimensional symplectic space over \(\mathbb F_p\), with \(p\in\{3,5,7\}\). It confirms total plane counts \(40,156,400\), oriented surface-label dimensions \(40,312,1200\), transvection traces \(4,12,24\), involution traces \(-16,-72,-192\), and cyclic transvection invariant dimensions \(16,72,192\). It checks rank-two isotropy by a direct finite-field bilinear pairing, computes transformations and determinants in reduced row echelon bases, and verifies the determinant-minus-one parity on the tetrahedral \(p=3\) surface. The actual program completed with `VERIFY_OK`.

The universal proof uses closed oriented surface components and disjoint edge sets from Assaf et al., an orientation computation on symmetric-square cones, symplectic linear-algebra counting, and rational character theory. The finite enumeration is corroboration only; it does not validate every prime, establish originality, compute an entire irreducible character table, or constitute an independent audit.
