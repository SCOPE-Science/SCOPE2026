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

# Reproducible exact checks

The complete argument is in `RESULT.md`. Execute `python3 verify_symbolic.py` and `python3 verify_fields.py` in the directory containing these files. The first script uses SymPy; the second uses only Python's standard library.

The symbolic checker independently expands the required powers, extracts six Cartier coefficients, reconstructs the correctly twisted scalar, checks the discriminant and its disjointness from the exceptional roots, and gives exact irreducibility and separability checks. Expected marker: `SYMBOLIC_CERTIFICATE_OK`.

The finite-field checker separately implements arithmetic in \(\mathbb F_{11}\), \(\mathbb F_{11^5}\), and \(\mathbb F_{11^{20}}\). It builds the dual Hasse–Witt matrix, applies entrywise Frobenius twists, and performs exact Gaussian elimination on the successive products. The two exceptional generators give rank sequences \((2,1,0,0,0)\); all eleven base-field parameters give \((2,2,2,2,2)\). Expected marker: `INDEPENDENT_FIELD_CERTIFICATE_OK`.

These are reproducibility checks, not external or independent expert certification. A finite sample does not establish algebraic-closure exhaustiveness; the theorem's complete enumeration follows instead from the symbolic factorization, Kummer irreducibility, and separability argument. No independent external audit or validation has been performed.
