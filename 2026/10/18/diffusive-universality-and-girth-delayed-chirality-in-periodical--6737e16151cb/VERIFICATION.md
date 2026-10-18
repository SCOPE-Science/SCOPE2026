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

# Mathematical verification

The proof in `RESULT.md` gives a uniform factorial winding-tail estimate with constant \(B_xT_n+T_n^2\), a Fourier inversion/dominated-convergence argument for the full circle heat-kernel total-variation profile, and the path-interference computation at odd girth. They imply the infinite-size and all-time conclusions; a finite computation would not suffice.

The standalone script `verify.py` requires NumPy and SciPy, as specified by `requirements.txt`. Run from the extracted directory with `python verify.py`. It directly constructs \(H\) and \(e^{-i\tau H}\) for multiple sizes, fluxes, and time intervals; reconstructs the Bessel periodization; checks the coarse analytic error inequalities and parity; tests the leading odd-girth coefficient; and compares selected diffusive-time distances to a numerical circle heat-kernel integral. Observed output: `VERIFY_OK 702 finite identities and mixing comparisons`.

These are finitely many floating-point checks, not formal or exhaustive certificates, and they make no claim to verify all fluxes, all sizes, or the infinitely long mixing limit. The scientific priority judgment is similarly not an independent audit. No claim is made about experimental validation.
