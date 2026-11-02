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

The functional weak-convergence proof is written out in `RESULT.md`. In the supplementary file `checks/moment_checker.py`, the first block independently enumerates all finite signed-step paths up to length 12 for exponent one and checks the exact second-/fourth-moment and signed mixed-moment recurrences. The second block verifies Beta moments at several rational switching rates by exact rational arithmetic. The third block uses the same independently checked recurrence for finite \(N\) and compares the resulting normalized moments with the predicted analytic finite-window targets at three real window parameters.

To reproduce with Python 3 and no external libraries:

```sh
python3 checks/moment_checker.py
```

Expected stdout is embedded as `checks/moment_checker_output.txt`. It finishes with `PASSED 131 finite assertions`. The computational cases test finite algebra and trends; they do not certify the Poisson point-process limit, asymptotic independence at positive times, global universality, or novelty.

The proof's noncomputational verification consists of: (1) the independent-flip Laplace-functional limit; (2) local sign-process convergence from a fair sign and continuity of integrated paths; (3) a deterministic \(2\delta\) near-origin approximation; (4) compact-support moment identification from the stationary telegraph generator; and (5) double integration of its exact parity correlation. The result claims convergence of laws for each bounded finite parameter and does not claim error bounds, formal third-party certification, or a uniform limit for unbounded exponent parameters.
