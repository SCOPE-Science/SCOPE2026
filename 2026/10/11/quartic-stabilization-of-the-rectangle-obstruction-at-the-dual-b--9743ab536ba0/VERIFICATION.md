---
{
  "expert_attestation": {
    "status": "not_performed",
    "evidence": null
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "status": "not_performed",
    "evidence": null
  },
  "schema_version": 1
}
---

# Exact endpoint calculation and verification limits

Let \(a=1+t\), \(b=1-t\), and \(R_t=[-a,a]\times[-b,b]\), where \(|t|<1\). Exact Fubini integration gives
\[
\int_{R_t}(x^2+y^2)\,dx\,dy
=\frac43ab(a^2+b^2)=\frac83(1-t^4).
\]
Consequently \(\widetilde V_4(R_t)=16(1-t^4)/3\) and the normalized deficit is
\[
1-(1-t^4)^{1/4}=\frac14t^4+O(t^8).
\]

For \(n\ge2\), put \(d=n-2\) and \(K_{t,\varepsilon}=R_t\times[-\varepsilon,\varepsilon]^d\). At exponent \(q=n+2\), the exact identity \(\widetilde V_q(K)=q\int_K|x|^2dx/n\) and Fubini's theorem yield
\[
\widetilde V_{n+2}(K_{t,\varepsilon})=\frac{n+2}{n}(2\varepsilon)^d
\left(\frac83(1-t^4)+\frac{4d}{3}\varepsilon^2(1-t^2)\right).
\]
It follows algebraically that the finite-thickness ratio is
\[
\frac{1-t^4+\frac d2\varepsilon^2(1-t^2)}{1+\frac d2\varepsilon^2}.
\]
Taking \(\varepsilon\downarrow0\) proves the stated limiting deficit in every fixed dimension. This is an identity-based proof, not an extrapolation from sampled dimensions.

For cross-check against the published dimensional-reduction argument, its correct coefficient is \(2q/(nQ)\), where \(Q=q-n+2\); the coefficient \(2^q/(nQ)\) in the original source package was a transcription error and has been corrected here. The normalization constants cancel in the final ratio, but accurate quotation matters for reproducibility.

The existing standalone `verify.py` reconstructs the exact planar polynomial and leading coefficient with rational arithmetic. It does not perform the independent literature comparison or prove general endpoint stability. The modified scientific files do not assert external expert or formal certification.
