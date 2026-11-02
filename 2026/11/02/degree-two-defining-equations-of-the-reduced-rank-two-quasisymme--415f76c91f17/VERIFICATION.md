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

# Exact finite checks and limits

The separate Python 3 script `verify_quadrics.py` uses only standard-library rational arithmetic. It evaluates determinant coefficients for each of the \(n-2\) rank-two component matrices, forms quadratic products in Plücker variables, groups them by full \(\mathbb Z^n\) weight, and performs exact Gaussian elimination. For each \(n=4,5,6,7,8,9,10\), it independently checks rank-one squared-pair weights, the unique forbidden shared-middle-index weights, and rank one/two for four-distinct-index weights according to whether index \(1\) is present.

The observed quadratic coordinate dimensions are respectively \(19,45,90,161,266,414,615\), and the independent extra quadratic counts are respectively \(0,1,5,15,35,70,126\). The script exits with `VERIFY_OK` when all identities hold. These checks are finite and do not prove the arbitrary-\(n\) assertion, which follows from the multigraded component-restriction proof in RESULT.md.

Independent mathematical audit: not performed.
