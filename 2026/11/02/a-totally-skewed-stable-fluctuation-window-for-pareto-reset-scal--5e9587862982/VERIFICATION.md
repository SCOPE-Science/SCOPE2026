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

Run `python verify.py` with SciPy. The actual replay returned `PASS 25 deterministic independent numerical identities; stable convergence is analytic`. The program independently compares Pareto moments with numerical quadrature, checks Brownian-area means, rates, regular-variation ratios, and admissible stable exponents. Neither these finite checks nor the numerical quadrature certify the distributional limit: the proof uses the Gaussian scaling identity, regularly varying product tails, the stable limit theorem for independent cycle rewards, a renewal-time random change, and tightness of the final unfinished cycle. This is a self-reviewed analytical finding; independent audit has not been performed.
