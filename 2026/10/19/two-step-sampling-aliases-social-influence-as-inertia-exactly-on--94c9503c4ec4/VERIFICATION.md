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

# Reproducible exact checks

Execute `python verify.py` using Python 3.10 or later. The program uses only `fractions.Fraction` and `itertools`; it has no external data dependency.

At \(\beta=\log9\), a node of degree one or two with unit edge weights has rational logistic update probabilities. The checker enumerates every binary configuration and exactly multiplies the transition kernels. It verifies the 16 two-step entries for a one-edge graph and the 256 entries for two disjoint edges against the independent-inertia formula; it also verifies strict positive pair covariance for all 8 starts of the three-vertex path and all 16 starts of the four-cycle. On the path it independently evaluates the closed-form covariance at every start. Expected output begins with `PASS:` and reports exact covariance intervals.

These are complete finite checks for the *tested networks*, not an exhaustive enumeration of all finite graphs. The general if-and-only-if result and strict inequalities are established by the analytic proof in `RESULT.md`. Historic novelty is provisional, and independent audit has not been performed.
