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
# Reproduction and scope

Execute `python3 verify_ciani.py` (Python 3.11+; no third-party dependencies). The program works in the prime field with 1009 elements and the smooth specialization \(a=1\). It enumerates 35 distinct rational quotient coordinates, calculates the order-two and order-three Wronskians as determinants of exact Taylor-coefficient matrices, and checks exact interpolating polynomials.

The degree-three order-two quotient coefficients are `[353,959,322,857]`; the degree-eleven order-three quotient coefficients are `[879,326,508,141,914,387,343,133,815,401,47,498]`, in increasing powers of the quotient variable. The test checks a nonzero leading coefficient, vanishing polynomial gcd with the derivative, vanishing gcd with the second-order residual, and nonzero evaluations at every finite branch value (0,889,270). The expected last line is `VERIFY_OK`.

The program checks finite-field identities and nonvanishing conditions; it is not a stand-alone proof of the characteristic-zero theorem. The mathematical proof in `RESULT.md` establishes the invariant Wronskian factorization, a degree-24 quotient, the complete ramification, and the algebraic specialization implication. No independent review or external certification has been performed.
