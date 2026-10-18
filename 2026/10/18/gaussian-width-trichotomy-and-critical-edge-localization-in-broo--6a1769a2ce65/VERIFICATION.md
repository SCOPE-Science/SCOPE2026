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

The exact identities are checked by `VERIFY.py` against direct root-vertex linear-functional maxima, with a fixed pseudorandom seed. The same code verifies the Gaussian path increment covariance matrix symbolically in floating-point arrays with integral entries. A successful run prints `VERIFY_OK` and test counts. All tests are finite; they cannot establish the infinite limiting laws.

The analytic verification consists of: (i) independent Gaussian radial normalization, including fourth inverse-chi moments; (ii) two one-sided normal maxima producing a persistent half-normal hub term; (iii) a locally dependent Poisson exceedance theorem with adjacent-pair probability \(O(q^{-4/3}(\log q)^C)\); (iv) an independent-even/odd decomposition proving coarse path maximum concentration; and (v) continuous mapping and \(L^2\) estimates for the critical width and exposed-branch selection. The exact bridge edge is retained and proved asymptotically negligible.

No computer calculation is offered as a proof of the asymptotic regime classification, of bibliographic independence, or of any external certification. Independent audit: not yet performed.
