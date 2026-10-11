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

The explicit constants are
\[
a_0=\frac{100}{81},
\qquad
b_0=1,
\qquad
q=\frac9{10},
\qquad
t_0=\frac{17}{10},
\]
\[
u=(1-q)t_0=\frac{17}{100},
\qquad
v=\frac{a_0}{t_0}-\frac1{q t_0}
=
\frac{100}{1377}.
\]
The two source radii at the contact point are
\[
t_0=\frac{17}{10},
\qquad
q t_0=\frac{153}{100},
\]
both in the interior of
\[
[3/2,2].
\]

For the graph difference
\[
F(x,y)
=
\frac1{\sqrt{(x-u)^2+y^2}}+v
-
\frac{a_0}{\sqrt{x^2+y^2}},
\]
direct substitution gives
\[
F(t_0,0)=0
\]
and
\[
\nabla F(t_0,0)=0.
\]
The Hessian is
\[
D^2F(t_0,0)
=
\begin{pmatrix}
2\lambda&0\\
0&-\lambda
\end{pmatrix},
\qquad
\lambda
=
\frac{1-q}{q^3t_0^3}>0.
\]
Thus the critical point is a nondegenerate saddle.

The Morse lemma gives a local product normal form. In a fixed square,
\[
\left|
\{|UV|\le\delta\}
\right|
=
4\delta
\left(1+\log\frac{\rho^2}{\delta}\right),
\]
so the planar base set on which the graph separation is at most \(\delta\) has area at least a constant multiple of
\[
\delta\log(1/\delta).
\]
The vertical \(\delta\)-slabs contained in the two Euclidean surface neighborhoods overlap by length at least \(\delta\) on that base set. Hence the intersection volume is at least a constant multiple of
\[
\delta^2\log(1/\delta).
\]

The source's Theorem 1.5(b), with
\[
|a_0-b_0|=19/81,
\]
gives the matching upper order.

For the source hypotheses,
\[
g_t=-a/t^2,
\qquad
g_{tt}=2a/t^3.
\]
The derivative-pair map has a smooth inverse on its compact image, so the cinematic-curvature constant is positive. The hyperbolic sign follows from
\[
D
=
\frac{2\bar a(a-\bar a)(\bar t-t)}{\bar t^3t^3},
\]
which makes the product in Definition 1.4 strictly negative whenever
\[
\bar a\ne a,
\qquad
\bar t>t.
\]

No finite numerical experiment is used in the proof. The only qualitative local theorem invoked is the Morse lemma for a nondegenerate critical point.
