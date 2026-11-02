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

# Verification and reproducibility

The attached `verify_spectral.py` uses exact rational arithmetic and only the Python standard library. It evaluates the explicit rational kernels for finite mixtures of independent OU speed modes and independently computes the first four orders of the tilted planar Fourier–Hermite generator. Comparing the second and fourth cumulant eigenvalue derivatives gives four exact identities, including unequal colored relaxation rates and a zero-mean process. It checks off-diagonal mixed spectral kernels rather than just a single OU rate.

Run: `python verify_spectral.py`. A successful run prints `True` for each exact comparison and exits with no exception. The test reports values at unit rotational diffusivity and unit colored-noise intensity. General \(D_r\) factors are obtained by rescaling ordered time gaps.

The proof of the arbitrary positive finite spectrum uses Wick's identity, the explicit angular four-point function, an elementary integrated connected cumulant and the spectral-gap dominated-convergence argument; its mathematical validity cannot be inferred from four examples. A non-gapped spectrum, correlated angular and propulsion noise, or non-Gaussian signed speed is outside scope. Long-time cumulant sign is not finite-time sign. Independent audit has not been performed.
