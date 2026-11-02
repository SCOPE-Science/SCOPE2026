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

Run `python verify.py` with Python 3.10 or later, NumPy and SciPy. It tests the closed variance and fourth-cumulant rates for 10 parameter sets against a separately implemented Taylor eigenvector recursion for the eleven-separation tilted generator. It also tests strict large-field positivity across rate and hopping grids, the unique subcritical crossing for 15 parameter combinations, and independently evolves a finite-volume density matrix to check the opposite signs on either side of the threshold.

Result on the supplied code: `PASS 251 deterministic independent numerical checks`. Example finite-time fourth cumulants from the separate density-matrix propagation at time 10 with pure-dephasing rate 0.6, each-direction incoherent hop rate 0.2, and coherent hopping strength 1.2: about −60.4480 for zero field and +9.45746 for field 2.5. The program also checks normalization and negligible sampled finite-chain boundary mass.

The long-time infinite-chain theorem is proved in `RESULT.md`: the decisive steps are the isolated analytic branch, exact four-step Schur expansion in coherence separation, and the sign argument for the dimensionless quartic. Numerical checks are finite and do not replace this proof. The program requires standard scientific Python packages and does not access the internet.
