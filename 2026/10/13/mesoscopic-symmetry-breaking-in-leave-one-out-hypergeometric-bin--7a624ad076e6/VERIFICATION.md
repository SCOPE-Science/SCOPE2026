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

The exact reduction can be checked directly from the two possible leave-one-out counts. For \(p=K/N\) and \(q=1-p\), both relevant masses under \(\operatorname{Bin}(N-1,p)\) equal \(\binom NKp^Kq^{N-K}\), which gives
\[
D_N(K)=-\log\binom NK+(N-1)H(p).
\]

For the asymptotic proof, the critical symbolic checks are
\[
F(u)-F(0)=-\sum_{m=2}^{\infty}\frac{m-1}{m(2m-1)}(2u)^{2m}
=-\frac83u^4+O(u^6),
\]
and
\[
G(u)-G(0)=\frac{4u^2}{3(1-4u^2)}=\frac43u^2+O(u^4).
\]
Thus, after the independently justified localization \(u=O(N^{-1/2})\), the scaled objective converges uniformly on bounded sets to
\[
P(y)=\frac43y^2-\frac83y^4,
\]
whose only global maximizers are \(y=\pm1/2\), with \(P(\pm1/2)=1/6\).

The bundled `verify.py` performs direct finite-parameter checks of the exact KL identity and prints numerical maximizers for increasing \(N\). Those computations are not a certificate of the infinite asymptotic statement; the proof rests on the uniform Stirling expansion and analytic profile comparison.
