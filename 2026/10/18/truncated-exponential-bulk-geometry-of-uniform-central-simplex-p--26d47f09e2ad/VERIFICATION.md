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

# Reproducibility

This report records ordinary analytical and numerical checks of the stated theorem. It does not supply an independent audit.

The pivotal identity is obtained by transforming \(e^{-(c-1)Y_{(1)}}\) under the exact conditional minimum density. The resulting beta mean is \(1/c\) and its variance is \((c-1)^2/[c^2(mc+c-1)]\). Conditional iid truncated exponentials yield the law of large numbers. The unconditioned independent gamma sum makes the normalization rigorous. The exact first two moments of the limiting truncated exponential are \(1\) and \(2-c(\log c)^2/(c-1)^2\).

Execute `python verify.py` from this extracted package. Tests include exact beta-moment algebra at rational parameters, numerical quadrature of limiting moments, an exact integral benchmark for the two-coordinate polytope, and simulated finite-dimensional radial quantities from the correct conditional law. Randomized checks are supporting diagnostics, not a proof of limiting assertions. The proof covers all fixed \(c>1\), while the sampler tests a finite set of ratios and dimensions.
