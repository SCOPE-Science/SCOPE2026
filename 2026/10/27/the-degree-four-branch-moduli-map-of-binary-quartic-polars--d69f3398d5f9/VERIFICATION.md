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

Execute `python verify.py` with SymPy. The checker builds the universal squarefree binary quartic in one parameter, constructs its polar cubic pencil, computes its discriminant, and checks the precise invariant identities and consequent degree-four rational transformation. It also checks the branch fiber factorization, derivative critical equation and classical level-three modular expression. Successful execution produces `VERIFY_OK: quartic invariants, branch invariants, discriminants, degree-four Belyi map and modular identity`.

The algebraic identities are exact symbolic computations over \(\mathbb Q[a]\), not a finite sampled enumeration. The proof separately explains why the normal form covers all smooth binary quartics, why the cubic discriminant gives the polar branch quartic, and why the exceptional harmonic case is a square. The conclusion concerns equal rational covers, not a naturally given isogeny. Neither independent mathematical audit nor external validation has been performed.
