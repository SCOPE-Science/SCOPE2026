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
The universal proof uses two exact ingredients. First, the uniform permutation average of \(T_\pi^{\mathsf T}T_\pi\) commutes with every simplex symmetry, hence is scalar on the standard simplex representation. Second, for one fixed ordering, projecting a simplex vertex through the preceding hyperplanes multiplies its common remaining inner product by \(1+1/n\) after each projection. Summing the resulting exact squared-norm losses gives the displayed formula for \(c_n\).

The embedded `verify.py` reconstructs the ambient rational simplex projectors and enumerates every order for \(1\le n\le5\). It checks the full averaged Gram matrix, not only selected test vectors, and verifies the summation and closed forms for \(c_n\) and the with-replacement factors. A successful finite replay corroborates the theorem but is not the proof for arbitrary \(n\).

Unproved limits include non-simplex equiangular frames, noisy or inconsistent systems, relaxation parameters different from one, block projections, adaptive row choice, single-shuffle reuse, and finite-precision stability.
