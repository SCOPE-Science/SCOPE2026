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

# Reproducible mathematical checks

The analytical proof is in `RESULT.md`. Execute the standalone `verify.py` using Python 3 with `sympy`, `numpy` and `scipy` installed:

```sh
python verify.py
```

The exact-algebra section checks the two drift zeros, the two linearization coefficients, the powers, both thresholds and the reciprocal sum and difference. It also checks an exact rational instance in which the lower and upper integrated powers are respectively \(2/3\) and \(4/3\).

The independent diagnostic builds a conservative upwind continuous-time Markov generator for three active velocity modes on 4000 finite-volume cells. It solves the stationary linear system and fits log-log endpoint *tail masses* (not density bins) over eight mesoscopic widths. On the rational example \(\mu=v=\gamma=1\), \(g=4\), the fitted powers are approximately \(0.68818\) at the lower edge and \(1.32923\) at the upper edge, against theoretical \(2/3\) and \(4/3\). The separately fitted conditional zero-to-attractor density ratios divided by boundary distance are approximately \(1.56413\) and \(0.80485\), against exact limiting values \(1.5\) and \(0.75\). The exact-algebra section reports 14 identities and the finite-volume section 6 assertions.

The finite grid is not a proof of endpoint asymptotics. Its discretization biases near-edge slopes by a few percent; positivity and the infinite-parameter-range conclusions follow solely from the analytical conservative-flux argument. No independent scientific validation has been conducted.
