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

# Evidence and reproducibility
The critical state is the prey-only equilibrium with \(u\equiv1\) and \(v\equiv0\). The exact predator integral balance is \(z'=-(\alpha/a)\int_0^a(1-u)v\,dx\). The proof identifies the positive Neumann resolvent \(\psi_a\) from the stable prey linearization, and proves \(v/z\to1\) and \((1-u)/z\to\beta\psi_a\) uniformly before evaluating the limiting quadratic drift. This gives the stated \(1/t\) laws without assuming that the dynamics is spatially homogeneous.

Run `python3 verify.py` with a Python 3 standard-library interpreter. The script solves the piecewise-forced Neumann elliptic equation by a finite-volume tridiagonal method for five independent geometric/physical parameter choices on two spatial meshes each, checks the reconstructed residuals, compares all cell values and the integrated response against the exact formula, and checks six thin-zone asymptotic ratios. It reports 16 successful cases. A separate symbolic calculation checked continuity and derivative matching at the patch boundary and the small-patch limit.

The finite mesh computations verify the **elliptic formula to numerical tolerances**, not the PDE theorem; the infinite-time conclusions rest on the comparison, heat-kernel, spectral-gap, and Duhamel proof. No exhaustive computational certification is claimed. The initial perturbation must be small, the predator diffusivity must be positive, and the limits \(t\to\infty\) and \(a\downarrow0\) are in the given order.
