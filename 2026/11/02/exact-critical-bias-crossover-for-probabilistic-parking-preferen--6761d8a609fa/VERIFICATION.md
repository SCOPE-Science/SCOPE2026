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

# Reproducibility checks

Execute `python verify_parking_crossover.py` with Python, NumPy and SciPy installed. On successful execution it prints `PASS: 43 exact and asymptotic reproducibility checks`. The exact-rational enumeration implements both potential search directions on each occupied preference and weights both successful and unsuccessful branches. Comparisons cover five probability values for each size 2, 3, 4 and 5, and symmetry and total-mass checks. The numerical component computes stable log-gamma coefficient sums at sizes 500, 2000 and 10000, then verifies that the absolute discrepancy from the claimed critical coefficient decreases with size for five fixed scaled biases.

The formulas (1)–(8) and the uniform boundary estimates in RESULT.md are the actual infinite-sample mathematical proof. No finite collection of checks certifies weak convergence, asymptotic originality, or an independent audit.
