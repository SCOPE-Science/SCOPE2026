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

# Reproducible checks and limits

Execute `python verify.py` with SymPy available. The verification independently constructs the generator on the original four states, solves 144 exact-rational stationary systems, checks the joint and mean occupancy formulas against those solutions, checks both symbolic derivative factorizations, and evaluates three exact examples. All checks completed successfully on the packaged script.

The proof, not this finite arithmetic sample, establishes the universal result for all positive rates and every \(\rho\in[0,1]\). The stationary process assumes independent Poisson event clocks except that one shared catastrophe simultaneously affects both patches. No simulation, numerical root search, or external computational certificate is needed for the universal signs. Priority remains subject to independent literature review, especially the incompletely accessible correlated-disturbance papers.
