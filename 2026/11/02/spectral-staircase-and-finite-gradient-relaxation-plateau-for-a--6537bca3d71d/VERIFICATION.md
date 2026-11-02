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

# Verification of the finite-gradient relaxation spectrum

The analytic conjugation is verified as a symbolic identity with independent expressions on both sides. The finite-difference Schrödinger discretization then compares the lowest spatial eigenvalues against the exact formula for gradients \(g=0.2,0.3,0.65\), taking \(v=1\), \(\gamma_1=0.5\), and \(\gamma_0=0.8\). These choices respectively realize two, one, and zero nonstationary bound levels. The code also checks the sign and exact forms of the slow temporal rates, threshold plateau, and bound-level counts.

Run `python verify_spectrum.py`. This test uses `numpy`, `scipy`, and `sympy`. It checks a finite sample and a finite spatial box; it does **not** verify the complete infinite-line spectrum, which follows from the separate factorization and essential-spectrum proof. There is no independent audit evidence.
