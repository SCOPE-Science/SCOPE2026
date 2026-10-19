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

Run `python3 verify.py` from the directory holding the included script. It uses only the Python standard library and exact rational arithmetic to compute cosine moments, the Rayleigh test for \(v=Q^2\), minimum carrying capacities, the resident weighted balance, and the Neumann corrector. The exact claims checked are \(\Lambda(1)\ge1/35\), positive invasion lower bound \(13/700\), positive minimum invader capacity \(61/150\), and corrector constant \(C=1/32\).

The analytic proof, not script output, establishes the strict spectral positivity for arbitrary smooth domains and finite mobility, continuous/strict monotonicity, both diffusion endpoints, the unique inverse parameter cutoff, and its large-mobility scaling. An independent scientific audit has not been performed.
