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

Let
\[
F_m(r)
=
p\frac{1-r^m}{1+r^m}
-
\frac{2r^N}{1-r}.
\]
The derivative is
\[
F_m'(r)
=
-\frac{2pmr^{m-1}}{(1+r^m)^2}
-
\frac{2r^{N-1}(N-(N-1)r)}{(1-r)^2},
\]
so the root is unique and comparison in \(m\) is valid.

Let
\[
A=A_{p,N}
\]
satisfy
\[
p=\frac{2A^N}{1-A}.
\]
Then
\[
F_m(A)=-\frac{2pA^m}{1+A^m}<0,
\]
so
\[
R_{m,N}^{(p)}<A.
\]
The roots increase with \(m\), and their \(m\)-th powers are bounded by
\[
A^m\to0,
\]
which proves convergence to \(A\).

For a mean-value point
\[
\xi_m\in(R_{m,N}^{(p)},A),
\]
\[
A-R_{m,N}^{(p)}
=
\frac{2pA^m/(1+A^m)}{-F_m'(\xi_m)}.
\]
Because
\[
m\xi_m^{m-1}\le mA^{m-1}\to0,
\]
the denominator converges to
\[
\frac{2A^{N-1}(N-(N-1)A)}{(1-A)^2}.
\]
Using the equation for \(A\) gives
\[
A-R_{m,N}^{(p)}
\sim
\frac{2A(1-A)}{N-(N-1)A}A^m.
\]

At
\[
N=1,
\]
\[
A=\frac{p}{p+2},
\]
which yields
\[
\frac{p}{p+2}-R_{m,1}^{(p)}
\sim
\frac{4p}{(p+2)^2}
\left(\frac{p}{p+2}\right)^m.
\]

The proof is analytic. Numerical roots were used only as independent sanity checks, not as evidence for an infinite statement.
