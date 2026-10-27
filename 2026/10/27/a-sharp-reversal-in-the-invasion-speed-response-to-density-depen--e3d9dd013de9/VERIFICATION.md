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
# Verification of the front-speed sensitivity

The displayed front-speed coefficient is established by the full analytic derivation in `RESULT.md`, not by numerical enumeration. The proof uses (i) the exact crowding-to-diffusivity identity, (ii) a wave-existence theorem with the zero-speed case covered by direct quadrature, (iii) a strictly positive adjoint transversality pairing, (iv) the parameter derivative of the traveling-wave equation, and (v) exact moments of a beta distribution. The polynomial resulting from step (v) is \(\sqrt{2}(1+2a)(4a^2-17a+9)/60\) in normalized speed units.

`verify_front.py` was executed with the packages named in `requirements.txt`. It passed an exact rational-coefficient polynomial check. It then solved separate two-tailed boundary-value problems with a midpoint phase at \(U=1/2\), using the physically correct flux \(P=d_b(U)U'\), linearized exponential Robin tail conditions, a residual tolerance of \(4\times10^{-9}\), and a cutoff at dimensionless distance 27. For symmetric \(b=\pm0.005\), the observed first differences were \(0.190070706\), \(0.070710969\), and \(-0.125016577\) at \(a=0.2,0.5,0.8\), compared with analytical slopes \(0.190070303\), \(0.070710678\), and \(-0.125016479\). It also checked that the computed speed has magnitude below \(5\times10^{-12}\) at \((b,a)=(-1/2,6/13)\) and \((1/2,14/27)\), the two exact weighted-area balance points.

These tests use a finite interval and finite numerical precision and do not verify exact wave dynamics for all parameters; the infinite-domain theorem relies on the explicit analysis. A self-review found correctness, novelty versus inspected sources, and mathematical value sufficient within the stated scope. Independent audit and independent validation have not been performed. Full texts for two older/related primary papers were unavailable, as described in `REVIEW.md`.
