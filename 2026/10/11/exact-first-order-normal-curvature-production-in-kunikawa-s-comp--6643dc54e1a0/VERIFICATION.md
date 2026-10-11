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

The source formulas used as premises are:

\[
\partial_tK^\perp\big|_{t=0}
=
-2
\left\langle
\mathcal C(\nu,\xi)e_1,e_2
\right\rangle,
\]
and
\[
\mathcal C(\nu,\xi)
=
\frac{2\kappa'\sin\theta}{(2+\cos\theta)^4}
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]
The source's frames are orthonormal, so the relevant matrix entry gives
\[
\partial_tK^\perp(s,\theta,0)
=
-\frac{4\kappa'(s)\sin\theta}{(2+\cos\theta)^4}.
\]

The packaged checker differentiates
\[
h(\theta)=\frac{\sin\theta}{(2+\cos\theta)^4}
\]
and obtains numerator
\[
4+2\cos\theta-3\cos^2\theta.
\]
The unique root with cosine in \([-1,1]\) is
\[
\frac{1-\sqrt{13}}3.
\]
Substitution gives the exact maximum coefficient
\[
\frac{108\sqrt{2\sqrt{13}-5}}
{(7-\sqrt{13})^4}.
\]

For the global energy, the initial area form is
\[
d\mu_0=(2+\cos\theta)\,ds\,d\theta.
\]
Thus the quadratic coefficient is
\[
16
\int_0^{2\pi}
\frac{\sin^2\theta}{(2+\cos\theta)^7}\,d\theta.
\]
The checker generates
\[
J_{n+1}(a)
=
-\frac1n\frac{dJ_n}{da}
\]
from
\[
J_1(a)=\frac{2\pi}{\sqrt{a^2-1}}
\]
and verifies
\[
-J_5(2)+4J_6(2)-3J_7(2)
=
\frac{59\sqrt3\pi}{1944}.
\]
Consequently
\[
16I
=
\frac{118\sqrt3\pi}{243}.
\]

The source point \(\theta=\pi/2\) has absolute initial rate \(|\kappa'|/4\); the exact profile maximum is larger by
\[
4.8385048269546666\ldots.
\]

No finite sampling is used to establish the formulas, the maximizer, or the energy coefficient.
