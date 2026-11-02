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

# Mathematical verification and scope

The derivation begins with the stationary angular generator \(\mathcal L f=d f''+\omega f'+r(f(0)-f(	heta))\). Direct generator balance determines the two Fourier harmonics \(m_1\) and \(m_2\). The exact conditional first-harmonic semigroup determines a centered, exponentially integrable velocity correlation, and its symmetrized time integral yields the full stationary long-time diffusion tensor.

The complex traceless tensor component \(Z\) is reduced by an exact algebraic identity. The imaginary term in its numerator excludes zero for every nonzero angular drift; this is an all-parameter analytic proof, independent of finite numerical search. Differentiation at \((r,\omega)=(d/2,0)\) proves the first-order splitting law with a locally uniform quadratic Taylor remainder. No boundary at zero diffusivity or zero reset rate is included.

The included standalone `checker.py` performs exact symbolic identity and derivative tests with SymPy, numerical Green--Kubo integration for five parameter sets, and independent discretized angular Markov-generator Poisson-equation calculations at two mesh resolutions for three parameter sets. Refinement reduces finite-grid differences in each checked case. These finite checks are corroboration, not a substitute for infinite-dimensional or all-parameter arguments.

Reproduce with `python checker.py` and Python 3, SymPy, NumPy and SciPy. The source comparison covers the achiral source, a chiral relative-tumble model, passive shape-anisotropic diffusion and a shape-anisotropic active model without intrinsic rotation. An independent scientific audit and an exhaustive publication-priority search have not been performed.
