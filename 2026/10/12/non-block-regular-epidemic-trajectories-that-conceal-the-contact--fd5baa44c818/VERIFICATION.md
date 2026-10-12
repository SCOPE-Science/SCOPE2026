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

# Reproduction and limits

Run `python3 verify.py` with a standard Python 3 interpreter in the same directory as this file. The script uses `fractions.Fraction`, has no nonstandard dependencies and prints `VERIFY_OK` if all assertions pass.

The exact rational tests independently substitute the stated all-dimension counterfamily into both polynomial vector fields on the proportional trajectory for \(n=2,3,4,7,11,25\), check admissible bounds, symmetry, nontrivial perturbation and the relation annihilating the contact-matrix difference. The two-community tests evaluate the first nonzero Gram determinant Taylor coefficients using exact derivatives of the vector field, obtaining \(1/7500\) at order \(T^4\) and \(4/703125\) at order \(T^6\).

These finite assertions are not proofs for arbitrary dimensions or parameters. The unrestricted conclusions are proved directly by invariant-subspace uniqueness, positivity and explicit Gram integral identities in `RESULT.md`. No noisy-data reconstruction, stochastic approximation or global classification for general \(n>2\) is asserted.
