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

# Verification and scientific boundaries

Run `python check.py` using Python 3 and SymPy. A successful run prints `OCTAHEDRAL_K3_RAMIFICATION_EXACT_OK`. The test checks the quartic-discriminant expansion, degree-six repeated-root parametrization, exact residual quadratic factorization and degree-eight squarefree branch polynomial, all four double-double-root quartics, and distinctness of the six triple-root cusp images.

The proof of completeness of singularities uses the arithmetic genus of an irreducible plane sextic, not numerical plotting or finite enumeration. Its global K3 inputs (smoothness, equations, symplectic parity) come from Nukui's published construction; the quotient flatness follows from finite Cohen–Macaulay flatness. The model identifies reduced divisorial ramification only; no assertion is made about full non-reduced stack stabilizer schemes or exceptional quotient resolutions.

The six-cusp/four-node count is a previously known property of generic quartic discriminant sections (Tokunaga 2002); the novel geometric subject is the explicit special symmetric K3 quotient and its octahedral genus-three ramification curves. An equivalent unlocated classical description is a residual originality risk. Independent audit: not performed.
