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

The statement and proof were checked against the stated hypotheses.

- Measurability: a Haar-measurable set is replaced by a Borel representative modulo a null set for the product-measure argument; every countable family of translates changes only on a countable union of null sets.
- Measure normalization: \(\mu(G)=1\) and \(\mu(gA)=\alpha\) for every left translate.
- Lower bound: every admissible countable mixture has integral \(\alpha\), so Jensen's inequality gives cost at least \(-\log_2\alpha\).
- Positive baseline: the first-hit index of independent Haar translates is geometric with mean \(1/\alpha\); Tonelli's theorem gives a realization with finite integral of \(-\log_2 a_0\) and \(a_0>0\) almost everywhere.
- Approximation: for fixed \(\delta\in(0,\alpha)\), Hoeffding's inequality bounds the expected exceptional-set measure by \(\exp(-2N\delta^2)\); the chosen exceptional sets therefore have measures tending to zero.
- Logarithmic control: mixing the finite averages with the integrable baseline bounds the cost on the exceptional set, and the limits \(N\to\infty\), then \(\delta,\varepsilon\downarrow0\), give the upper bound.
- Boundary case: \(\alpha=1\) gives entropy zero directly.
- Limits: the proof does not establish attainment, a deterministic efficient construction, or the general conjecture for arbitrary set systems.
