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

The proof requires no computer-assisted infinite certificate. Derive the stroboscopic affine map and its unique fixed point, integrate the dark and light orbit to obtain the displayed formula for \(m(h)\), verify the monotonicity of \(h\coth(kh)\), and apply the finite-Fejér phase-mixing lemma to one- and two-time products. Autocorrelation, Parseval, and the Riemann–Lebesgue lemma establish the exact long-lag plateau.

The file `verify_photobioreactor.py` uses NumPy/SciPy, and can be executed as `python verify_photobioreactor.py`. It performed 78 successful checks spanning exact periodic closure, direct quadrature versus closed-form cycle means, monotonicity, and supplementary long-time/lag covariance quadrature. A representative uniform period example with \(a=1\), \(b=3\), \(c=1\), \(r=0.4\), and \(H\) uniform on \([0.6,2.2]\) has the predicted plateau approximately \(0.0001293906580\), with a finite-time/lags quadrature approximation of \(0.0001370678536\).

**Unproved by computation:** neither limiting covariance theorem nor parameter-universal strictness is inferred from finite grid calculations. They follow from the analytical proof. The model does not describe redraws of the period on every cycle. No independent external audit is represented.
