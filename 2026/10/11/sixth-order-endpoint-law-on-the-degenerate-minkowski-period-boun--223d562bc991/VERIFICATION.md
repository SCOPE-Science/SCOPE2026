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

The packaged checker begins only with
\[
U'(y)=\frac{e^y-1}{qe^y-p},
\qquad d=q-p,
\qquad s=p+q,
\]
and the source convolution
\[
\Theta(E)=\frac1d\int_0^E\frac{W'(x)}{\sqrt{e^{2(E-x)}-1}}\,dx.
\]
It expands \(U\), solves \(U(y(t))=t^2\) recursively through the coefficient of \(t^7\), and forms
\[
W(x)=y(\sqrt x)-y(-\sqrt x).
\]
It then expands the kernel and performs the convolution using exact beta values.

The replay verifies
\[
[ E ]\Theta
=
\frac{\pi(3d^2-12d+s^2)}{48d^{3/2}},
\]
\[
[ E^2 ]\Theta
=
\frac{\pi(3d^2-12d+s^2)^2}{9216d^{5/2}},
\]
and, after imposing \(s^2=12d-3d^2\),
\[
[ E^3 ]\Theta
=
\frac{\pi(d-4)(d-1)^2}{720\sqrt d}.
\]

It also checks the consistency identity
\[
\frac d8[ E ]\Theta
=
\frac{\pi A}{96\sqrt d},
\]
which is the published quadratic coefficient after using \(\log r\sim r-1\).

Finally it verifies
\[
\frac{d^3}{512}[E^3]\Theta
=
\frac{\pi d^{5/2}(d-4)(d-1)^2}{368640}.
\]

The proof uses exact symbolic algebra and analytic series identities; finite numerical sampling is not used as evidence for the asymptotic theorem.
