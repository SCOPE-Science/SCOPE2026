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

# Reproduction and verification

Run `python verify.py` using Python 3.9 or later, with no third-party packages. The program independently enumerates labelled irreversible adsorption paths and computes the exact scalar vacancy recursion on small complete graphs. It tests normalization, count parity, conditional label-uniformity, and an independent product formula for the all-dimer event. Larger-size scalar recurrences are compared against the stated parity-repaired Poisson limiting distribution.

The local execution produced `PASS: 294 exact/numerical assertions across finite graph and large-N tests`. The finite comparisons do not establish the limiting theorem. In the proof, the crucial infinite-size controls are the pairwise predictable Bernoulli coupling with summed discrepancy of order \(\varepsilon\), the bounded second-visit rate, Le Cam's Poisson bound, and harmonic-number asymptotics. The explicit \(5\varepsilon\) bound is proved in `RESULT.md` and applies to all \(n\ge4\) and \(0<\varepsilon\le1/4\).

The entire analytical domain and the unproved extensions are described in `RESULT.md`. This documentation records a self-review and does not constitute an independent audit.
