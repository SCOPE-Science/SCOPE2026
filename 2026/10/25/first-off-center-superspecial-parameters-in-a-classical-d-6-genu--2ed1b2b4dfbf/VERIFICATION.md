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

# Exact reproducibility and limitations

Run `python3 verify.py` with Python 3.8 or later. No external packages are needed. A normal execution checks all nine primes \(5,7,11,13,17,19,23,29,31\) and finishes with `VERIFY_OK`.

The calculation constructs the coefficients \(A_p,B_p\) of \((u^2-tu+1)^{(p-1)/2}\) exactly using integer multinomial coefficients, then computes the monic polynomial gcd over \(\mathbf F_p[t]\) with modular Euclidean division. It confirms \(\gcd(A_{31},B_{31})=t(t^2-20)\). A second computation raises the original polynomial \(x^7-tx^4+x\) to the relevant half exponent by ordinary polynomial convolution and compares every Cartier–Manin coefficient for each base-field parameter at all nine primes. The proof's geometric completeness comes from gcd in the polynomial ring, not from enumeration of finite-field parameter values.

Boundary checks: the three characteristic-\(31\) common zeros are \(0,12,-12\), all smooth since their squares differ from \(4\). The argument relies on the standard equivalence between zero Cartier operator and superspecial genus-three Jacobian. No assertion extends beyond the stated primes or establishes a global moduli-isomorphism classification. No independent audit has been performed.
