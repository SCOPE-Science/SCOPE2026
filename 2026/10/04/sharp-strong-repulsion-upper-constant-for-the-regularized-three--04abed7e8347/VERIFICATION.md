---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The load-bearing multiplier is exactly the published homogeneous s-wave symbol. At \(\gamma_0=52/27\), setting \(t=\pi|k|/6\) reduces \(S_{\gamma_0}(k)\le S_{\gamma_0}(0)\) to \(F(t)=3t\cosh(3t)-\frac{13}{4}\sinh(3t)+\frac{27}{4}\sinh t\ge0\). Its power-series coefficient of \(t^{2n+1}\) is \([3^{2n+1}(8n-9)+27]/[4(2n+1)!]\): the first two vanish and every coefficient for \(n\ge2\) is positive, so the inequality is strict for \(t>0\). For \(\gamma>\gamma_0\), affine dependence on \(\gamma\) and \(\tanh x<x\) give strict decrease away from zero. The Taylor coefficient \(\pi^3(52-27\gamma)k^2/648\) makes zero fail even local maximality below the threshold. Since the quadratic form is multiplication by this continuous symbol, its optimal upper constant is its essential supremum. Independent direct evaluations reproduced the threshold behavior.

## originality

PASS

Basti et al. publish the exact Mellin multiplier and use it for the lower-boundedness mechanism at \(\gamma>\gamma_c\); full-text inspection of the relevant Section 3 formulas did not state the separate strong-repulsion threshold \(52/27\) or the exact upper norm constant. Ferretti--Teta use the same model and zero-frequency value in stability/instability analysis but the accessible material likewise does not identify the global-maximum transition. Current Resultary and exact-number searches did not locate an independent \(52/27\) theorem. The audited result is therefore a best-of-knowledge new spectral optimization of a published symbol.

## value

PASS

The exact norm of a load-bearing homogeneous multiplier is a natural spectral invariant of the regularized three-boson model. The theorem identifies a genuine maximizing-frequency phase transition and upgrades prior nonsharp upper control to an exact constant in the strong-repulsion regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
