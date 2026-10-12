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

# Exact verification and its limits

The independent-coefficient ensemble is encoded directly in the standalone `verify.py` file. Running `python3 verify.py` prints a summary and exits with status zero only if every exact equality holds. No nonstandard Python package is needed.

Verified by exhaustive enumeration of coefficient vectors in ten configurations: affine and quadratic univariate models over moduli \(2,4,6,8,9\), affine and quadratic bivariate models over moduli \(4,6\), and one affine trivariate model over modulus \(3\). Across these ensembles, the program enumerates \(5{,}998\) polynomials and checks \(2{,}754\) ordered point pairs, their joint-zero probabilities, all one-point marginals, complete-grid expectations and variances, and selected proper-subset moments. An additional \(116\) exact divisor-function checks cover moduli \(2\) through \(30\) and dimensions \(1\) through \(4\).

The computation uses exact integer and `Fraction` arithmetic, without numerical approximations. Finite checks cannot establish universal identities; those follow from the surjective uniform-linear-map argument and the totient divisor identity in the proof. No independent review or independent validation was performed.
