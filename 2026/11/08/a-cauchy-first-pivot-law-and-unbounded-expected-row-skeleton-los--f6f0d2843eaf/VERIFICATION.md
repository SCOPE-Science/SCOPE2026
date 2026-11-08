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

The proof is analytic and requires no numerical certificate: the spectrum of \(A_t^\mathsf{T}A_t\) is \(\{1+2t^2,1\}\), selected-row projection errors are exactly \(1\) and \(1+t^2\), and independent Gaussian sum/difference coordinates give a Cauchy ratio. The exact first-pivot law follows for all \(t>0\), and a reciprocal-arctangent identity proves the large-\(t\) asymptotics.

`CHECK.py` was executed directly using standard Python and returned `PASS: exact rational projection identities, angular counts, and extra-column invariance`. It independently evaluates rational row-projection identities for five parameters, angular Gaussian direction counts for seven parameters at 120,000 angles each, and invariance of the first pivot under appended columns. Numeric discretizations do not constitute proofs of the Cauchy law or asymptotic limit.

The result concerns only the first pivot and the best rank-one row reconstruction after that pivot. The certificate does not validate complete multi-pivot or adaptive algorithms, nor publication precedence beyond the enumerated source comparisons.
