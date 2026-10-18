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

# Verification of the new Gaussian-reset KL theorem

## Reproduction
Run `python check.py` with dependencies in `requirements.txt`. The script evaluates both renewal forms by independent quadratures, validates the Gaussian Jeffreys identity and its derivative, and performs independent numerical optimizations. It completed 230 assertions successfully across eleven parameter settings including large temperature ratios; the output explicitly displays the optimized frequencies and rates.

## Direct mathematical checks
The exact OU variance and centered-Gaussian KL identity supply the observable. The periodic elasticity is a product of two strictly decreasing positive factors. The Poisson kernel's logarithmic-time derivative has concave log because the maps \(u\mapsto\log(1-e^{-e^u})\) and \(v\mapsto\log g(ae^v)\) are concave with the second increasing; Prékopa marginalization and analyticity establish uniqueness. The auxiliary expectation obeys \(0\le qJ_a'(q)\le J_a(q)\) and is \(O(a^{-1/2}\log a)\) when \(q\asymp\sqrt a\). These are analytical statements, not extrapolations from tests.

## Quantitative comparisons and limits
At \(a=10^6\), the checker reports \(q_{\mathrm{pois}}/\sqrt a\approx1.004917\), \(q_{\mathrm{per}}/\sqrt a\approx0.707274\), and \((M_{\mathrm{per}}-M_{\mathrm{pois}})/\sqrt a\approx0.289629\). The corresponding proved limits are \(1\), \(1/\sqrt2\), and \(1-1/\sqrt2\). Numerical tolerance and finite grids do not prove any uniqueness claim or asymptotic formula; those conclusions depend on the preceding analytic argument.

No independent scientific audit has been performed. The physical interpretation is restricted to the symmetrized endpoint KL component, not the total entropy production of a hardware realization.
