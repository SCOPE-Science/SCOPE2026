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

# Reproducibility and proof-scope verification

Execute `python verify.py` from the directory containing this file, with NumPy, SciPy, SymPy and mpmath installed. The included program is standalone and requires no web access or files from another item.

At the time of packaging it completed: (i) exact symbolic substitution of the persistent-orientation first-harmonic solution and orientationally averaged second-order solution into their radial differential equations; (ii) 25 comparisons between the modified-Bessel coefficient and an independently shot four-dimensional radial Dirichlet boundary-value problem; (iii) 60 high-precision derivative-sign spot-checks for orders zero through four; and (iv) small- and large-rotational-diffusion limit checks. All checks passed.

These finite calculations do not establish analyticity of the full solution or prove complete monotonicity for every derivative and every real parameter. Those claims rely on the elliptic Dirichlet perturbation argument and the exact four-dimensional killed-diffusion resolvent shown in `RESULT.md`. The prescribed expansion fixes positive angular diffusivity before taking the small-propulsion limit. An independent audit has not been performed.
