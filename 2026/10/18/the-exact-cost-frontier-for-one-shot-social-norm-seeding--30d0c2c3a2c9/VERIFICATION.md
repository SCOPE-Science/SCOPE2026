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
# Verification notes

The analytic proof in `RESULT.md` establishes the all-parameter theorem. To check computational examples, install requirements from `requirements.txt` and run `python check_social_campaign.py`.

Observed result: `PASS: 48 exact-form/numeric minimizer comparisons; 6 trajectory outcomes; omega-constant check`.

The cost frontier was compared with independently located one-dimensional numerical minima across eight dynamical parameter pairs and six cost ratios. Six trajectories were integrated on either side of the separatrix. The Lambert-W specialization at \(\beta=1\), \(r=1/2\) was checked numerically. These are finite consistency checks, not an exhaustive proof of a universal assertion, and they do not constitute independent mathematical auditing.

The correctness argument uses a conserved quantity, compact invariance, monotone state limits, and strict convexity. The original dynamical phase classification belongs to the cited source. The novel mathematical objective is the one-time two-cost choice of initial supporter and advocate fractions. Potentially equivalent previous intervention literature remains an originality risk; independent validation is not claimed.
