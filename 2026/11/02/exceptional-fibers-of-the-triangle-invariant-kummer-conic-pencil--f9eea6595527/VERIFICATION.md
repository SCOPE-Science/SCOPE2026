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

The exact verifier is `verify_triangle_pencil.py`. Run `python3 verify_triangle_pencil.py` in a Python 3 environment with SymPy installed. It checks the conic determinant \((3\lambda+1)/4\), the axis discriminant \(4\lambda+1\), the cyclotomic split-conic identity, the Heron four-factor identity, and the arithmetic-genus identities for several positive exponents. It enumerates projective singular rational supports over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_9,\mathbb F_{25}\) with explicit field arithmetic and compares the counts to geometric predictions in cases where all supports are rational.

Successful completion prints `TRIANGLE_PENCIL_CONIC_DISCRIMINANT_HERON_FACTORIZATION_GENUS_AND_FINITE_FIELDS_PASS`. The finite instances and finite exponents are checks, not an infinite-family proof. Completeness follows from the conic pullback proof in `RESULT.md`; the ordinary-singularity and intersection-order assertions are established there, not inferred from a vanishing-gradient census. Independent audit: not performed.
