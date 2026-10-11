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

Let
\[
\tau=2^{-2/p},\qquad
H_\tau(x,y)^2=(x+y)^2+\tau(x-y)^2.
\]
For \(2<p<\infty\), one has \(1/2<\tau<1\).

On \(xy\ge0\),
\[
1+\tau\le\frac{H_\tau^2}{\|\cdot\|_{X_p}^2}\le4\tau.
\]
On \(xy\le0\), with \(s=|x+y|/|x-y|\),
\[
\frac{H_\tau^2}{\|\cdot\|_{X_p}^2}
=
\frac{4(s^2+\tau)}{(1+s)^2},
\]
whose derivative is \(8(s-\tau)/(1+s)^3\). Hence its minimum is \(4\tau/(1+\tau)\) and its maximum is \(4\tau\).

Thus
\[
\sqrt{\frac{4\tau}{1+\tau}}\,\|w\|_{X_p}
\le H_\tau(w)\le
\sqrt{4\tau}\,\|w\|_{X_p},
\]
so Hilbert Ptolemy gives \(C_{\mathrm{Pt}}(X_p)\le1+\tau\).

For
\[
x=(-\tau,-\tau),\qquad
y=(1,-1),\qquad
z=(1-\tau,-1-\tau),
\]
the six required norms are
\[
\|x\|=\sqrt\tau,\quad
\|y\|=1,\quad
\|z\|=1+\tau,\quad
\|x-y\|=1+\tau,\quad
\|x-z\|=1,\quad
\|z-y\|=\sqrt\tau.
\]
Therefore the Ptolemy ratio is \(1+\tau\), proving equality. No finite enumeration is used. The unresolved scope is \(1\le p<2\), the infinite endpoint as part of the theorem, and general Day--James \(\ell_p-\ell_q\) families.
