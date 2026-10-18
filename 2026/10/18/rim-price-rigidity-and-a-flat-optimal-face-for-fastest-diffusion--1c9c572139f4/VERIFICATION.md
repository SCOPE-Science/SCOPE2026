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

The proof uses two global Rayleigh bounds, an exact Fourier spectrum for symmetric allocations, and a complex first-Fourier eigenvector to force symmetry of **every** optimizer. For finite replay, execute `python verify_wheel_gap.py` with NumPy and SymPy installed. The script passed 2141 exact-rational, symbolic, and numerical assertions during replay, including independently varied conductance vectors and critical-price boundary samples. Finite tests corroborate, but do not replace, the analytical proof for every integer \(n\ge3\) and real \(B,t>0\). No independent scientific audit has been performed.
