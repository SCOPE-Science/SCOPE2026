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

The proof uses two analytic comparison scales.

For
\[
B_n
=
\left((n-1)\frac{\omega_{n-1}}{\omega_{n-2}}-1\right)^{-1},
\]
strict gamma log-convexity gives
\[
\frac{\omega_{n-1}}{\omega_{n-2}}
>
\sqrt{\frac{2\pi}{n}}
>
\sqrt{\frac6n}.
\]
It follows analytically that
\[
B_n<\frac1{\sqrt n}
\quad(n\ge3),
\]
and
\[
B_n<\frac1{2\sqrt n}
\quad(n\ge14).
\]

For \(A_n\), the ball-volume recurrence and duplication formula give
\[
A_n
=
(2^{n-1}\pi n)^{1/n}
\left[
\frac1{\sqrt3\,2^n\pi^{n/2}\Gamma(n/2+1)}
\right]^{1/(n+1)}.
\]
The elementary parity estimate
\[
\Gamma\!\left(\frac n2+1\right)
\le
\sqrt{\frac{\pi n}{2}}
\left(\frac n2\right)^{n/2}
\]
then yields
\[
A_n>\frac1{2\sqrt n}
\]
for every \(n\ge2\).

Thus the infinite tail \(n\ge14\) is completely analytic.

The bundled checker addresses only \(3\le n\le13\). It uses
\[
3<\pi<\frac{22}{7},
\qquad
\sqrt3<\frac74,
\]
and the exact formulas
\[
\omega_{2k}=\frac{\pi^k}{k!},
\qquad
\omega_{2k+1}
=
\frac{2^{k+1}\pi^k}{(2k+1)!!}.
\]
After replacing constants in the direction that lowers \(A_n\), the assertion \(A_n>1/\sqrt n\) becomes a rational inequality after raising to \(n(n+1)\). All arithmetic in `verify.py` uses integers and `Fraction`; no floating point is used. The smallest finite normalized certificate is
\[
\frac{1944365472}{1771561}>1000.
\]

For \(n=2\),
\[
B_2=1,
\qquad
A_2^6=\frac{4\pi}{3}>1.
\]

The primary source's Lemma A.2 then converts \(A_n>B_n\) into
\[
\rho_n^*>\rho_n
\]
for every \(n\ge2\).
