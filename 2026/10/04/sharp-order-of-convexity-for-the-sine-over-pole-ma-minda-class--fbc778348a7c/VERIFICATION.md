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

For
\[
\xi(z)=1+\frac{\sin z}{1-z},
\]
the boundary real-part function is
\[
F(t)=\operatorname{Re}\xi(e^{it}).
\]
The exact derivative formula used by the checker is
\[
F'(t)
=
\operatorname{Re}\!\left(
 i e^{it}
 \frac{(1-e^{it})\cos(e^{it})+\sin(e^{it})}{(1-e^{it})^2}
\right).
\]

The included interval-arithmetic replay certifies
\[
F'<0\quad\text{on }[0.1,1.8086448],
\]
\[
F'>0\quad\text{on }[1.8086449,\pi-0.1],
\]
and
\[
0.7302132125\ldots<F''<0.7302151004\ldots
\]
on \([1.8086448,1.8086449]\). Hence that bracket contains exactly one critical point. High-precision evaluation inside the certified bracket gives
\[
t_*=1.808644860488715898679582852398313963676602879316\ldots
\]
and
\[
\mu_*=F(t_*)=0.39072298833669261703444293158667137888774859706022\ldots .
\]

The intervals near \(0\) and \(\pi\) are controlled analytically in `RESULT.md`; they stay above \(0.87\) and \(0.57\), respectively. The boundary singularity at \(z=1\) has lower limiting real part at least
\[
1+\frac{\sin1}2-\cos1=0.8804331865\ldots .
\]
Thus none of the omitted endpoint neighborhoods can compete with \(\mu_*\).

Sharpness uses the canonical solution of
\[
1+\frac{zf_*''}{f_*'}=\xi(z),
\]
so no numerical experiment is used to infer extremality. The computation only certifies the one-variable critical-point location and sign pattern.
