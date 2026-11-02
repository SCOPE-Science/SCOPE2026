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

# Reproduction and limits

Run `python thermal_dimer_check.py` with Python 3, NumPy, SciPy and SymPy. The program independently constructs the four-dimensional Ornstein–Uhlenbeck drift matrix, solves its stationary Lyapunov equation, and compares its measured left-bath heat injection with the closed flux identity. It also solves a representative covariance system over exact rational numbers, compares the analytic joint optimizer to an independently optimized clipped one-dimensional objective for 180 random budget triples, and verifies a closed radical witness.

At creation, the checker reported exact rational covariance PASS, 600 random Lyapunov comparisons PASS, 180 optimizer comparisons PASS, and the \(k=1\), \(P=3\), \(\Gamma=4\) witness PASS. These are finite diagnostics; the universal theorem is proved analytically in RESULT.md. The external literature comparison is necessarily nonexhaustive, and no independent scientific audit has occurred.
