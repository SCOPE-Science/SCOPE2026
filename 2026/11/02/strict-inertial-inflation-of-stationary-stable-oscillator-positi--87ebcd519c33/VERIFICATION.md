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

# Reproducibility and evidence

Run `python3 check.py` from this directory using only the Python standard library. The saved output in `check_output.txt` reports 197 assertions passing. These include: 90 gamma/beta identity evaluations, 30 direct-kernel numerical quadratures, mass-monotonicity and endpoint comparisons, small-mass coefficient cross-checks, and Gaussian controls. Quadrature uses a quadratic time map and Simpson integration with a truncated exponentially decaying kernel.

The proof of the claim, including the all-real-parameter strict derivative inequality and its positive small-mass coefficient, is in `RESULT.md`; the numerical checks cannot certify it. The stationary representation is a classical stable-integral result, and its prior use in harmonic oscillators is cited. No independent audit or external experimental certification has been performed.
