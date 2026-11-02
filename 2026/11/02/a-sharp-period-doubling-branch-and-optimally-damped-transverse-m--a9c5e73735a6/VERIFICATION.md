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

# Reproducibility and mathematical limits

The standalone `checker.py` requires Python 3 and no third-party packages. Running `python checker.py` computes 20 alternating two-step return examples at even ring sizes \(n=4,6,8,12,20\), with interaction strengths \(h=0.51,0.60,0.73,\pi/4-0.001\). It compares direct iterates of the original full vertex map to the exact two-cycle, computes the full quotient cycle-Laplacian Floquet spectrum, and checks closed-form optimal two-step spectral radii and nonoptimal nearby strengths for each tested ring.

Results are recorded in `checker_output.txt` and are finite corroboration only. The all-even-ring and all-parameter existence/attraction theorem, analytic local uniqueness, and large-ring asymptotics follow from the five analytic steps in `RESULT.md`, not from the checker. No independent audit has been performed, and no global basin was computed or claimed.
