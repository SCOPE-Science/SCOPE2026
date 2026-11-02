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

# Reproducibility and verification

The curve is the smooth projective normalization of \((x^7+x)(z^4+z)=x^8+x^6+x^4+x^2+1\) over \(\mathbb F_2\). The arithmetic datum required for zeta reconstruction is the genus \(9\) and the full point counts for \(\mathbb F_{2^n}\), \(1\le n\le9\).

Run `python3 verify_zeta.py` from the directory containing this file. The script uses only Python's standard library. It checks all field moduli by exhaustive multiplicative inversion, enumerates every nonexceptional affine fiber of the plane equation, enumerates a second complete Artin–Schreier-over-elliptic description, handles the totally ramified points separately, checks the birational elimination identities, recovers the zeta numerator from Newton identities and Weil symmetry, and checks extension degrees \(10\), \(11\), \(12\) against the predicted numerator. It also checks the exact integral factor product and the Jacobian order. Expected final line: `VERIFY_OK`.

For the claimed simple-factor decomposition, run `python3 verify_simple_factors.py` (requires SymPy). It proves that the two higher-degree factors are irreducible over \(\mathbb Q\) by exact rational polynomial factorization. Expected final line: `SIMPLE_FACTOR_VERIFY_OK`.

Only degrees through \(9\) are required to determine this known genus-\(9\) zeta numerator. This finite exhaustive computation establishes infinitely many point counts **only together with** the independently known genus and Weil functional equation. There is no claim to an independently audited proof, explicit rational isogeny maps, or equations for the two higher-dimensional factors.
