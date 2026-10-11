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

# Direct verification

Run `python verify.py` with a Python 3 standard-library interpreter. The checker constructs the finite fields with respective orders \(3\), \(9\), \(27\), \(81\) from explicit irreducible polynomials and uses no network access or third-party dependencies. It performs exhaustive ordered-pair and ordered-triple enumeration, confirming the cubic-fiber multiplicities, the identity \(M(\mathbf1)=q^4+q^3-q^2\), the two-point correlation \(K(0,1)=q^2\), diagonal/off-diagonal weighted-pair multiplicities, and both real and imaginary normalized Taylor coefficients on a mean-zero test direction.

Expected order-by-order constant moments are \(99\), \(7209\), \(550395\), and \(43571601\). These calculations are finite cross-checks, not an assertion that finite experiments prove the unrestricted all-field result. The proof in `RESULT.md` derives the necessary identities independently. The conclusion applies locally near nonzero constants and does not determine a global extension norm in characteristic three.
