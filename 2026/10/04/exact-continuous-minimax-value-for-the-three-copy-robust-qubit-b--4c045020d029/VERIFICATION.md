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

The proof has two independent analytic certificates.

First, the least-favorable prior
\[
w_*=\frac5{13}\delta_{-\pi/3}+\frac3{13}\delta_0+\frac5{13}\delta_{\pi/3}
\]
produces an averaged Helstrom difference with nonzero eigenvalues \(\pm\sqrt{2114}/104\). Therefore every fixed measurement has worst-case success at most
\[
V=\frac12+\frac{\sqrt{2114}}{208}.
\]

Second, the displayed kernel-corrected observable \(B_*\) has spectrum \(\{-1,-4/39,4/39,1\}\), so it defines a valid binary POVM. Its exact profile obeys
\[
P_*(\theta)-V
=
\frac{\sqrt{2114}}{219856}(1-\cos\theta)(2\cos\theta-1)(246\cos\theta+713).
\]
For \(|\theta|\le\pi/3\), all factors on the right are nonnegative. This proves the continuum lower bound without sampling.

`artifacts/verify.py` reconstructs the four-dimensional symmetric-subspace matrices from the defining states and checks the spectra, active-point equalization, and closed-form profile against direct matrix evaluation. It uses only the Python standard library and deterministic arithmetic at double precision. Its grid test is a regression check for the formulas, not the proof of the continuum inequality.

Limits: the verification and theorem concern only three copies with \(\alpha=\pi/4\), \(\theta_{\max}=\pi/3\), and equal label priors.
