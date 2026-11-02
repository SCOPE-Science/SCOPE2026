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

# Reproducible numerical checks and mathematical boundaries

Run `OPENBLAS_NUM_THREADS=1 python verify.py` using Python 3.9+ and NumPy. Its deterministic random seed is embedded in the code; expected stdout appears in `verification_output.txt`.

The program checks 198 complete analytic parameter sets and stationary equations, 195 full-matrix versus Fourier spectral comparisons, 18,880 randomly selected feasible dihedrally symmetric transition matrices, and 1,200 randomly selected feasible asymmetric edge-weight transition matrices. It additionally checks the exact \(m=4\) rational example and four large-size asymptotic samples.

The comparisons use floating-point arithmetic with explicit numerical tolerances. Random tests and finite computations do not establish universal optimality. The rigorous proof uses convex averaging over graph automorphisms, a Fourier block decomposition, saturation of the exact spectral lower bound, and strict scalar convexity. These steps prove global optimality over **all** admissible symmetric stochastic matrices for every integer \(m\ge3\), and prove uniqueness only inside the dihedrally invariant family. The proof does not claim uniqueness of unrestricted minimizers.

The accompanying script and output are scientific reproducibility materials; no external certification is asserted.
