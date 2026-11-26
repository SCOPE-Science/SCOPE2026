---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The small-time law follows by substituting \(1-e^{-\theta y}\sim\theta y\) in the exact density and taking \(1-G(y)\to1\). At large \(y\), the leading terms of \(1-G(y)\) and \(g(y)\) are, respectively, \(\gamma\alpha e^{-\theta y}/(1+\alpha)\) and \(\gamma\alpha\theta e^{-\theta y}/(1+\alpha)\), giving the limit \(\theta\).

The bundled `verify_notexp_endpoints.py` uses `mpmath` to numerically differentiate the CDF at selected points, compare the hazard to its small-time asymptotic, and check the far-tail limit for the four triples assigned shapes in the prose of §2. It does not verify the figure legend or test every parameter triple. The alternate triples in the hazard-panel legend with \(\gamma>1\) fall under the symbolic exclusion of an initial decline; no plotting code is needed for this exclusion. For the prose and legend see DOI `10.3390/math14071182`, §2, p. 5, and Figure 1, p. 6.
