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

# Verification instructions and limits

Execute `python verify.py` using Python 3 and SymPy. The verifier is standalone and recomputes exact modular polynomial coefficients; `verify_output.txt` is its recorded successful execution and ends with `VERIFY_OK`. This checks the three-by-three Hasse--Witt matrix, its factorization, discriminant exclusions, the geometric root counts, the \(\mathbb F_{13}\)-parameter census, and the elliptic Hasse invariant pairs for \(p=5,7,11\).

The infinite-field conclusions use symbolic polynomial identities, the diagonal Frobenius action, and the prime-to-thirteen dihedral quotient isogeny proved in `RESULT.md`. Enumeration of the eleven base-field coefficients is corroboration, not an infinite proof. No separate formalization, independent audit, or all-prime calculation has been performed. The finite-field counts refer to marked coefficients, not isomorphism classes.
