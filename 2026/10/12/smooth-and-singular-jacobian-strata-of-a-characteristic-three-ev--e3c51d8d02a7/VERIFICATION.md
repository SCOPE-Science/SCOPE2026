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

The characteristic-three identities are confirmed by executing `python check.py` in an environment with SymPy installed. This independently constructs the derivative, boundary factorization, genus-three and genus-two Cartier–Manin coefficient matrices, the even quartic normalization, and the distinction between the two four-point boundary polynomials. The expected exact output is `VERIFY_OK`.

The global proof further requires the standard hyperelliptic genus formula, Cartier–Manin theory with semilinear stable rank, the prime-to-characteristic two-involution Jacobian decomposition, ordinary cusp local-completion classification, and the Rosenlicht–Serre exact sequence. These are written explicitly in `RESULT.md`; they are not verified by finite-field enumeration or by program output alone.

Limitations: algebraically closed base, characteristic \(3\), reduced complete curves only; extension classes and simultaneous normalization are not computed. No external independent audit has been performed.
