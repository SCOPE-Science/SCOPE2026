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
# Verification instructions
Run `python verify.py` with Python 3. The script uses only standard-library modules. It constructs every admissible ordered pair of distinct vertices directly for six bipartite networks and solves full rational backward equations, comparing the results against the three-state formulas at three transform parameters. It also verifies analytic eigen-residue sign predictions and hazard derivative signs in 18 representative unequal-rate classifications.

Observed execution: `PASS: 426 full-state exact-rational Laplace identities; 18 spectral hazard classifications`.

The exact rational checks are finite comparisons and are not claimed as a proof for all sizes or rates. The analytical reduction, strict eigenvalue placement, coefficient signs, and derivative factorization in RESULT.md establish the infinite-parameter statement. No independent review has been performed.
