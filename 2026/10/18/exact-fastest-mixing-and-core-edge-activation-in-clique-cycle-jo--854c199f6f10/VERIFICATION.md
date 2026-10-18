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

Run `python verify.py` after installing the packages in `requirements.txt`. With Python, NumPy and SciPy installed, it produced `VERIFY_OK 3929 checks`.

The code checks the exact closed formulas for all pairs \(2\le k\le11\), \(4\le m\le40\), independently solves each associated symmetry-reduced linear program, directly diagonalizes all constructed stochastic matrices having at most 29 states, and verifies exact fraction arithmetic for cycle orders four and six. It also checks positivity feasibility and the two support-phase inequalities.

This is not an exhaustive search over all asymmetric stochastic matrices. That unrestricted optimality is established analytically by convexity and automorphism averaging. Finite numerical and rational examples cannot prove the infinite-family assertions or establish originality; the mathematical proof and prior-work comparisons are essential. No independent audit has been performed.
