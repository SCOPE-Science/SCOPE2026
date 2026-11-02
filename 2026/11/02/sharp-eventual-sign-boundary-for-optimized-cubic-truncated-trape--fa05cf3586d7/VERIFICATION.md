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

# Verification notes

To reproduce, run \(\texttt{python verify.py}\) with SymPy and mpmath installed (tested using SymPy 1.14.0 and mpmath 1.3.0). The verifier reconstructs the optimized \(J=2\) cubic from its defining symbol and runs exact-arithmetic assertions for the crossing parameter, boundary factorization, three roots, residue ratio, recurrence and BDF2/trapezoidal comparison. It also compares separately computed complex-pole partial fractions against directly generated scalar-CQ coefficients at several parameters using high-precision arithmetic.

The exact real-pole uniqueness, the asymptotic dominance, the irrational-angle boundary and infinite sign changes are proved in \(\texttt{RESULT.md}\). No finite enumeration can prove those infinite assertions. The program supplies supporting checks and examples, not an independent certificate of novelty or proof validation.
