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

Fix
\[
\beta>1,
\qquad
\alpha=\sqrt{\beta^2-1},
\qquad
\phi=\arccos(1/\beta).
\]
For
\[
a_n
=
\frac{(i\alpha)^n-(-i\alpha)^n}{2i},
\]
the binomial theorem gives exactly
\[
b_n
=
\frac{(1+i\alpha)^n-(1-i\alpha)^n}{2i}
=
\beta^n\sin(n\phi)
\]
and
\[
c_n
=
\frac{(-1+i\alpha)^n-(-1-i\alpha)^n}{2i}
=
(-1)^{n+1}\beta^n\sin(n\phi).
\]
Also,
\[
\limsup_{n\to\infty}\frac{|a_n|}{\alpha^n}=1.
\]
Therefore the witness ratio is exactly
\[
\left(
\limsup_{n\to\infty}|\sin(n\phi)|
\right)^{-1}.
\]

If
\[
\phi/\pi
\]
is irrational, density modulo \(\pi\) makes this limsup equal to \(1\).

If
\[
\phi/\pi=p/q
\]
in lowest terms, multiplication by \(p\) permutes residues modulo \(q\). Hence
\[
\max_n|\sin(n\phi)|
=
\begin{cases}
1,&q\text{ even},\\[3pt]
\cos(\pi/(2q)),&q\text{ odd}.
\end{cases}
\]
This proves the lower formula.

The inspected 2026 theorem supplies
\[
\kappa(\beta)\le2/\sqrt3
\]
for every \(\beta>1\). At the shortest admissible odd resonance
\[
q=3,
\]
one has
\[
\phi=\pi/3,
\qquad
\beta=2,
\]
and the lower formula is
\[
\sec(\pi/6)=2/\sqrt3.
\]
Thus the fixed-parameter constant is exactly known at \(\beta=2\).

No finite numerical experiment or asymptotic extrapolation is used.
