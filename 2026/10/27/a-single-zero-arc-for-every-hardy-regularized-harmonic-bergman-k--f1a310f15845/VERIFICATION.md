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

The result was checked through exact coefficient orthogonality, an independently derived Poisson-mixture integral, the strict derivative sign for the normalized Poisson ratio, and the unique negative-axis root equation. The angular and radial derivatives guarantee a regular zero arc; dominated convergence gives both endpoint asymptotics.

Run `python checker.py` using Python 3.10 or later. No additional packages are needed. The script compares 27 kernel values computed by two formulas, tests numerical sign changes and normalized angular monotonicity for five boundary weights, and prints limiting constants. `check_output.txt` records the output of the packaged source. Numerical integrals use a polynomial change of variables followed by composite Simpson quadrature; calculations are finite checks, not rigorous interval proofs. Infinite-degree and all-parameter assertions rest on the analytic proof in `RESULT.md`.

The first-zero radius is defined implicitly; no direct elementary closed form is asserted. Prior-publication priority is not independently certified. Independent audit has not been performed.
