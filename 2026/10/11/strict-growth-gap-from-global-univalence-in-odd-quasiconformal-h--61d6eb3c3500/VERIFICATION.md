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

The candidate equality map can be reconstructed without external code:
\[
\psi(z)=\frac{z}{1-z^2},\quad
H_k'(z)=\frac{1+z^2}{(1-z^2)^2(1-kz^2)},\quad
G_k'(z)=kz^2 H_k'(z).
\]
The primitives vanish at the origin. The normalized harmonic map \(F_k=H_k+\overline{G_k}\) obeys
\[
\frac{G_k'}{H_k'}=kz^2,
\quad J_{F_k}=|H_k'|^2(1-k^2|z|^4)>0,
\quad H_k-G_k=\psi.
\]
On the positive real diameter, \(F_k(r)=\int_0^r(1+ks^2)U(s)/(1-ks^2)\,ds=T(k,r)\).

On the boundary right upper quadrant \(z=e^{it}\), the exact derivative
\[
\frac{d}{dt}\operatorname{Re}G_k(e^{it})=
\frac{k\cos t\sin(2t)}{2\sin^2t(1-2k\cos(2t)+k^2)}>0,
\qquad0<t<\pi/2
\]
with \(\operatorname{Re}G_k(i)=0\) gives a negative real part on that arc. The reflected boundary arc has the opposite real value. On the two horizontal components above each slit of \(\psi(\mathbb D)\), the exact coordinate derivative is
\[
\frac{\partial}{\partial x}\operatorname{Re}F_k(\psi^{-1}(x+iy))
=\frac{1-k^2|\psi^{-1}(x+iy)|^4}{|1-k\psi^{-1}(x+iy)^2|^2}>0.
\]
The two coordinate ranges overlap, providing distinct preimages of \(iy\) for every \(y>1/2\). This exact sign-and-intermediate-value proof establishes noninjectivity for all \(0<k<1\).

Any equality case for the upper bound forces \(\phi=h+\varepsilon g=\psi\) by the normalized second-coefficient equality case and forces \(\omega=kz^2\) by Schwarz-phase equality. It is therefore a normalized rotation of \(F_k\). Compactness follows from locally uniform derivative bounds, analytic schlicht compactness, and preservation of local topological degree, so the positive strict gap holds for each fixed \(k,r\).

For numerical consistency only, with \(k=1/2\), solving on \(y=1\) gives two approximate preimages \(\pm0.7552608658+0.3671083730i\), both sent near \(i\). The analytic proof is independent of this finite check.

Limitations: The exact optimal value \(M(k,r)\), the gap's magnitude and its endpoint behavior are not determined for positive \(k\). No other harmonic class is classified here.
