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
`artifacts/verify.py` reconstructs the field \(\mathbb F_9=\mathbb F_3[\omega]/(\omega^2-\omega-1)\) and the exact Example 6.1 generator matrix.

It first enumerates all \(9^5\) messages and checks the published ordinary weight enumerator. It then enumerates every message subspace in dimensions \(1\) through \(5\) by a unique reduced-row-echelon basis and checks the complete support-size spectra in the finding. The subspace totals are independently checked against the Gaussian binomial coefficients.

Because the source specifies only that \(\omega\) is primitive, the same computation is repeated with \(\omega^e\) for \(e\in\{1,3,5,7\}\), which are all primitive elements of this field model. All four choices give the same spectra.

The computation is finite and exhaustive for the displayed code. It does not certify an equivalence classification of all \([11,5,6]_9\) codes and does not establish a family-wide EGRL formula.

Successful replay ends with `VERIFY_OK`.
