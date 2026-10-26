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

# Reproduction and boundaries

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy. The standalone script reconstructs the Gram matrix and unique proposed probability law, tests both exact spectral bottlenecks, checks independently generated asymmetric candidate allocations, runs generic simplex-constrained optimizations, and uses exact rational algebra to verify characteristic-polynomial factors. It also verifies the polynomial identity forming the two-dimensional global maximum certificate.

The actual execution produced the text in `verification_output.txt`: 270 spectral cases, 6,480 sampled feasible laws, 11 numerical optimizations, and six symbolic checks. Generic optimizations use a numerical tolerance because a multiple lowest eigenvalue makes the objective nonsmooth at the optimum; they are not an exhaustive search. The universal optimization and uniqueness conclusions depend on the analytic proof, not finite tests. The results concern one-step expected squared-error reduction for consistent square systems and do not assert a sharp multistep average exponent.
