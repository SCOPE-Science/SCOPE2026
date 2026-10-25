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

The reproducible finite proof certificate is `verify.py` (Python standard library). Execute `python3 verify.py` in the directory containing this file. It checks integer discriminants by fraction-free Sylvester determinants, Rabin finite-field irreducibility, modular cycle factorization, primality and exact valuation of discriminant witnesses, reciprocity, and the explicit exceptional cubic factorization.

The independently reconstructed n=8 inputs are the reciprocal representatives \(k=1,3\) with integer discriminants \(-5390272,-1205696\); their irreducibility primes are \(7,3\), and simple ramification primes are \(84223,18839\). Transitivity in degree seven together with a transposition forces \(S_7\). The script returned:

`CERTIFICATE_OK representative_pairs= 10  n8_modular_cases=2  cubic_discriminants=-31,-23  lower_degree_exception=(7,2),(7,5)`

This finite certificate is not a verification of Garmi's infinite theorem; the \(n\ge9\) step explicitly depends on that published theorem. A separate independent mathematical audit was not performed.
