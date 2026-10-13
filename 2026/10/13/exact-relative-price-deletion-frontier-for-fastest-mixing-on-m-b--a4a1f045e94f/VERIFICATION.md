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

# Verification

The analytical proof establishes the two harmonic Rayleigh upper bounds for all nonnegative individual rates, solves their one-dimensional envelope, checks exact Fourier attainment, and proves all optimizing assignments are uniform within each edge class by equality rigidity. The derived threshold and asymptotics are exact consequences of these steps.

Run `python check_mobius.py` with NumPy to reproduce the finite numerical tests. The checker constructs the full graph Laplacian from each candidate weight vector and compares eigenspectra and Fourier bounds. The fixed-seed checks cover 10 graph sizes, 90 optimized cases, 2,700 nonsymmetric feasible competitors, and 70 points along the critical optimal family. Numerical floating-point checks have tolerance and do not certify every real parameter, every size, or historical originality.

Self-review: passed. Independent audit: not yet performed.
