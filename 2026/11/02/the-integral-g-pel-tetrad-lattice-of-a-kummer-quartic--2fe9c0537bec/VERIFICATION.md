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
# Verification record

The supplied `verify_gopel.py` is self-contained Python 3 code requiring no third-party dependencies. It enumerates exactly the 15 two-dimensional maximal isotropic vector subspaces of the standard symplectic `F2^4`, their 60 affine translates, and the resulting 16-by-60 matrix in deterministic lexicographic order. Every one of the 60 columns satisfies the six stated congruences; all column sums are 4 and all row sums 15.

The certificate columns (zero-based indices `11,1,39,49,36,7,43,45,23,51,31,37,3,12,9,17`) have determinant `-128` by a signed, exact integer Bareiss algorithm. The program also gives binary row rank 10. The mathematical proof in `RESULT.md` independently shows that the congruence lattice has index 128; together these facts establish equality of lattices, not merely approximate membership or a rank estimate.

The checker was run on the included source and returned `VERIFY_OK`. The source is finite and does not establish any claim about higher genus, geometric divisor-class equivalence, or complete Picard lattices. Independent scientific audit remains unperformed.
