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
# Reproducibility and limits

The analytic calculation enumerates all index sequences of length two (two RR orders versus four independent-with-replacement orders) and derives their exact output values. With equal curvatures, the initial-state propagation is deterministic and identical across the sampling rules, and only the noise variance differs. The sharp uniform comparison uses positive curvatures bounded by \(L\) and an explicit equal-curvature witness with individually contracting gradient steps.

Run the included `verify.py` with Python 3 and no third-party packages. It carries out exact rational arithmetic on 1,000 parameter configurations at the finite-sum minimizer and 500 additional configurations with arbitrary rational initial points and equal curvatures. It checks the displayed formulas and a fixed witness. All checks are finite spot checks and do not certify the universal quantifiers; the proof is symbolic and self-contained. No external independent audit has been performed. The work does not address long-run rates, last-iterate distributional stochastic ordering, or floating-point effects.
