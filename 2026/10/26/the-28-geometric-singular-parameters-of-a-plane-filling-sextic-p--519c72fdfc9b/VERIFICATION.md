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

Exact reproduction: run `python3 verify.py` using Python 3.8 or later. The executable checks the finite-field polynomial identities and irreducibility certificates, parameter orbit minimal polynomials, and \(\mathbb F_3\)-rational checks for all three rational parameters. Its successful final line is `VERIFY_OK`. A separately implemented SymPy script, `check_symbolic.py`, verifies the elimination, finite-field minimal polynomials, Hessian and cusp local expansion; its final line is `SYMBOLIC_VERIFY_OK`.

Geometric statements for all algebraic parameters follow from the affine critical equations and factorization proved in `RESULT.md`, together with the local Hessian and cusp calculation. Enumeration of rational points is not presented as proof over the algebraic closure. The scheme-theoretic discriminant multiplicities, the infinite parameter, and characteristics other than three are outside scope. No independent audit has been performed.
