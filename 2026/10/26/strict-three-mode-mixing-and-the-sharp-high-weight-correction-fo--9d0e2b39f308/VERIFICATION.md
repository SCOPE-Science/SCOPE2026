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

# Reproducibility

From this directory, execute `python verify.py` with SymPy, NumPy, and SciPy installed. The script verifies exact radial-moment ratios, the angular fourth-moment algebraic identity, the strict boundary directional derivative decomposition, the limiting sum-of-squares identity, and the unique completed-square maximum of the scaled correction. It independently cross-checks complex-coefficient fourth moments by angular Fourier expansion. Six multi-start numerical optimizations are diagnostic and **not** evidence that a finite range settles the all-weight theorem.

The reference output is embedded as `verification_output.txt`. The mathematical proof of the all-weight assertions is in `RESULT.md`. No external independent audit has been performed.
