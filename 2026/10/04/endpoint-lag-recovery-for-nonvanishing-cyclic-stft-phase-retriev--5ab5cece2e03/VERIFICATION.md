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

The proof uses only discrete Fourier orthogonality and a cyclic recurrence. For each time shift \(k\), the \(L\)-th Fourier coefficient of the measured sequence \(|V_gf(k,\ell)|^2\) is expanded directly. Because the window is supported in \(\{0,\ldots,L\}\) and \(d>2L\), exactly one overlap pair contributes, giving
\[
\frac1d\sum_{\ell}|V_gf(k,\ell)|^2e^{2\pi iL\ell/d}
=f_{k+L}\overline{f_k}\overline{g_L}g_0.
\]
For two nonvanishing signals with equal measurements, the ratios therefore satisfy \(r_{k+L}\overline{r_k}=1\) and hence \(r_{k+2L}=r_k\). Since \(\gcd(d,2L)=1\), all ratios coincide and have modulus one.

The packaged `verify.py` independently constructs STFT data and checks the endpoint formula and explicit reconstruction for all \(106\) admissible pairs with odd \(3\le d\le31\). Test windows deliberately include zero interior samples where possible. The script prints `VERIFY_OK 106`.

The finite replay is not an exhaustive proof over all dimensions or signals and is not used as such. The universal claim rests on the analytic derivation above.
