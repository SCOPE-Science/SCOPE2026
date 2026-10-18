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

# Reproducibility and verification

Analytical steps independently reconstructable from the statements are the strictly positive discriminant completion, the uniform derivative inequality \(4d(1+d x^2+r x)-(2dx+r)^2=4d-r^2>0\), pullback convergence at contraction factor \(q=\sqrt{d/(1+d)}\), conditional sign cancellation, and the centered-square AR identity. The exact mixed covariances and inversion of the two-lag moment map follow algebraically. Stationary even moments use the displayed finite multinomial recurrence.

Run `python3 verify.py` in the same directory. The included program executed successfully: 210 exact rational identities and 20 finite-sample diagnostics covering four admissible parameter pairs. The finite-sample diagnostics use deterministic seeds and tolerances and only guard against gross algebraic transcription mistakes; they do not prove infinite-time limits, statistical estimation error bounds, or scientific priority. No outside data, packages or network services are required to run the verifier.

The published source's equation is used at the anti-integrable limit only. Continuation to a finite-parameter three-dimensional map and independent audit have not been performed.
