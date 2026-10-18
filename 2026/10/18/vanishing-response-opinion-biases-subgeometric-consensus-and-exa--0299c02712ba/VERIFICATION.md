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
# Verification and reproducibility

The standalone script `verify.py` uses only the Python standard library. Run with `python3 verify.py`. In the packaged preparation it printed successful exact-rational checks for a heterogeneous four-node directed influence cycle (three synchronous transitions), successful finite scalar recurrences for the flat two-agent biases at \(\alpha=1\) (20,000 steps) and \(\alpha=2\) (2,000 steps), and two rational transitions each for the analytic responses of degrees \(1\), \(3\), and \(5\). The finite scalar output includes the monitored ratio \(H(d_t^{-\alpha})/(2\alpha t)\); it is far from the asymptotic limit for some parameters, consistent with strong preasymptotic slowing and not a failed test.

The unlimited-time mathematical verification instead consists of (i) the positive self-weight convex-combination argument; (ii) the strong-connectivity propagation of a strict decrease from the old maximum; (iii) continuity and compactness forcing consensus; (iv) the lower diameter inequality and flatness at zero; (v) the exact two-agent recurrence and asymptotically constant increment of \(H\); and (vi) the Taylor leading-order inverse-power recurrence in the analytic contrast. These are derived in `RESULT.md` and do not depend on simulation.

The script does not constitute exhaustive graph enumeration, numerical proof of the infinite-time limits, or independent validation. All claims are restricted to the hypotheses and domains stated in the result.
