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
For \(u\in(0,1)\), set \(p=e/(e-1)\) and \(z=1+\log(1-u/p)\). Then \(0<z<1\), and the target CDF equation is equivalent to
\[
(1-w)^w=z,\qquad w=G(x).
\]
Taking logarithms and substituting \(t=\log(1-w)<0\) gives
\[
t e^t-t=-\log z.
\]
On the negative half-line,
\[
\frac{d}{dt}\{t(e^t-1)\}=e^t(1+t)-1<0,
\]
and the function ranges from \(+\infty\) to \(0\). Therefore the admissible negative root is unique.

The embedded checker reconstructs \(w=1-e^t\), evaluates the original FEx-G CDF, and verifies the requested probability level. It separately checks the Kumaraswamy composition
\[
Q_F(u)=\left[1-\exp(t/b)\right]^{1/a}.
\]
The checker is a replayable consistency test, not the proof of the infinite-domain claim. No speed comparison with Newton–Raphson is asserted.
