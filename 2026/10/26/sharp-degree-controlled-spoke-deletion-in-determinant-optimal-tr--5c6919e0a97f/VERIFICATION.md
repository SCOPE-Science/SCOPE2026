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

## Reproduction
Run `python verify.py` with Python 3, NumPy and SymPy. The script uses a fixed pseudorandom seed and is independent of the construction of the document. The recorded standard output is included in `verification_output.txt`.

## Scientific checks performed
The checker reconstructs the grounded reduced Laplacian, computes its inverse and determinant numerically for 836 valid combinations of path, star and other tree topologies and cost parameters, verifies the explicit tree-distance covariance and marginal conditions, and compares 3,344 randomly sampled feasible conductance allocations. Nine selected rational configurations are verified in exact arithmetic using SymPy, including the precision-covariance matrix identity, determinant and budget. In 232 parameter combinations below the degree threshold it confirms that the analytically continued formula has negative spoke weight and is not a feasible design.

## Limits
Random comparisons do not establish global optimality, and below-threshold infeasibility of the closed formula does not establish that no other optimal design exists. The analytic convexity/KKT proof establishes global optimality of the displayed feasible allocations, while the Gaussian tree-separation argument proves that at least one spoke must vanish below the threshold. No general formula for that low-cost regime is asserted. No independent external audit was performed.
