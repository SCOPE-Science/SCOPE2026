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

The mathematical proof rests on a nested coupling of detected-species richness among non-tagged species. Given tagged sample count \(y\), observed richness has distribution \(\mathbf 1_{\{y>0\}}+R_{m-y}\). The coupling has increments in \(\{0,1\}\), so conditioning on tagged count one maximizes richness in first-order stochastic order among all feasible tagged counts. Averaging and testing all upper-tail indicators yields the asserted covariance and size-biased laws.

Reproduce the finite checks using `python3 verify.py` (only Python standard library is required). This verifier performs exact enumeration of every labeled subset in 96 positive-integer profiles of population size up to nine and of all categorical sequences for three nonuniform iid laws with sample sizes up to seven. It tests the dominance conditional on every feasible tag count, checks covariance signs with exact rational arithmetic, and verifies the positive and negative higher-frequency examples for \(r=2,\ldots,7\). Its completed execution reported 12,127 successful exact stochastic-order comparisons.

Computational checks are supplementary. No finite enumeration certifies the unrestricted theorem; the coupling argument and explicit analytic witness families provide that proof. The tests do not cover clustered surveys or heterogeneous individual selection weights in finite-census sampling.
