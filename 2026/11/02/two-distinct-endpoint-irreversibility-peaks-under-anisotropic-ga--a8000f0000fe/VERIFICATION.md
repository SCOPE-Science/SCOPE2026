---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The OU variances conditioned on shared cycle age t are v_j=1−(1−q_j)e^(−k_j t); the conditional Gaussian Jeffreys divergence is additive, with each term (v/q+q/v−2)/2. Exponential cycle integration gives J(r)=F_(1/2)(r)+100 F_(9/10)(r/100); the prefactor 100 cancels when differentiating. In a separate exact calculation, expand q/v=q Σ_(n≥0) a^n e^(−ns), a=1−q, and differentiate u²/(u+n) to get 1−n²/(u+n)² per term. At cutoff 16 the discarded derivative tail is positive and less than a^17/2 per coordinate; rational comparisons give J′(1), J′(20)>10^−4 and J′(3), J′(200)<−10^−4. This independently establishes the critical signs from the stated Gaussian model. An extremum on each closed bracket is interior by the endpoint derivative signs. Since the Laplace formula is real analytic and nonconstant, zeros of J minus its attained extremal value are isolated locally, so these extrema are strict. No uploaded code was executed. The independent calculation is replayable in review_checks.py, ou().

## originality

PASS

Credit harmonic Gaussian endpoint and reset-cycle calculations as background. The supported distinct claim is the explicit two-scale non-unimodality witness for the Poisson-frequency objective, certified by alternating derivative signs. Do not credit a general theory of multiple modes or priority over unchecked work.

## value

PASS

A specific exact witness tests frequency tuning for a natural conditional endpoint objective. It shows that two ordinary Gaussian modes at distinct relaxation scales invalidate any blanket unique-peak assumption for this optimization, even with independent reset coordinates and a single global clock. The rational sign proof avoids mistaking numerical noise near the shallow second peak for a real extremum. This does not imply multimodality of physical entropy production.

The dated certificate retains the supplied scientific assessment, sources and limitations.
