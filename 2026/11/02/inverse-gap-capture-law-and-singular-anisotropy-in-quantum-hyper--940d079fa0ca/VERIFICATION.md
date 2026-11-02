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

# Reproducible verification

The analytical argument in `RESULT.md` establishes the statement for all specified dimensions and real parameters. The standalone `verify.py` uses Python 3 standard-library exact rational arithmetic. It checks the candidate integrated density matrix, including *every* real and imaginary Lyapunov equation entry, across seven different simple rational energy spectra with sizes 3, 4, 5, 6, 4, 8 and 16. In three separate cases an exact Gaussian elimination of the full Lyapunov system reproduces its trace independently of the candidate closed form. It verifies the binary-cube weighted spectra and exact rational coefficients of the first three nontrivial cube dimensions, together with representative exact small-anisotropy gap bounds for dimensions 2 through 5.

Run `python3 verify.py` in the package directory. Recorded checker standard output is included in `CHECK_OUTPUT.txt`; it is not used to certify universal identities by finite sampling. Critical proof steps include negativity of all dynamical eigenvalue real parts, a pairwise energy-gap identity obtained by cancellation of triple partial fractions, the strictly convex loss optimization, binary uniqueness of anisotropic Walsh energies, and the equal-Hamming-cardinality gap contribution. No external validation has been performed.

Known limits: no general nonflat absorber weights, no competing quantum noise or recombination, no finite-time probability distribution, no joint large-dimension/vanishing-anisotropy asymptotics, and no independently certified historical priority.
