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

# Verification and limits

Run `python3 verify.py` using the standard-library Python interpreter. The script builds the full original associative algebra on the \(n+n^2\) basis vectors, computes actual anti-automorphism matrices, and checks the defining anti-multiplication identity and \(\sigma^2=I\) in exhaustive small-dimensional cases. A separate finite-field linear kernel test verifies the theoretically predicted parameter dimensions, with a genuine \(\mathbb F_4\) implementation. For \(n=2\) over \(\mathbb F_2\), a separate calculation constructs all identity-linear conjugations and recomputes their orbit sizes and number.

Expected summary: over \(\mathbb F_2\), \(112\) anti-involutions, with \(19\) identity-linear orbits; over \(\mathbb F_3\), \(1710\) anti-involutions. The output ends in `ANTI_INVOLUTION_CENSUS_AND_IA_ORBITS_OK`.

These checks do not exhaust arbitrary \(n,q\) and provide no independent proof of publication priority. The general proof uses the anti-automorphism normal form, elementary \(C_2\)-module calculations, exact centralizer orders and a linear group action. No independent mathematical audit has been performed.
