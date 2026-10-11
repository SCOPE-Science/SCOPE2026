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

For the trapezoid
\[
\Omega
=
\{(\xi,\eta):
0\le\xi\le2,\ |\eta|\le1+\xi/2\},
\]
the base area is \(6\) and a cone of height \(h\) has volume
\[
2h.
\]

For an apex \((x,y,h)\), direct edge-to-apex distance calculations give
\[
\begin{aligned}
A(x,y,h)
={}&6+\sqrt{h^2+x^2}
+2\sqrt{h^2+(2-x)^2}\\
&+\frac12\sqrt{5h^2+(x+2-2y)^2}\\
&+\frac12\sqrt{5h^2+(x+2+2y)^2}.
\end{aligned}
\]
The final pair is an even strictly convex function of \(y\), so every optimum has \(y=0\).

On \(y=0\),
\[
\Phi(x,h)=A(x,h)h^{-2/3}
\]
has exactly one stationary point because every stationary point minimizes the convex function
\[
A(x,h)-\Phi(x,h)h^{2/3}
\]
globally, while strict sublevel convexity excludes two global minimizers.

The packaged checker differentiates the explicit formula and solves
\[
A_x=0,
\qquad
3hA_h=2A
\]
at high precision. It also reproduces the four fixed-height numerical center values quoted by the source.

The numerical calculations only evaluate the uniquely characterized solution. Existence and uniqueness over the whole domain
\[
\mathbb R\times(0,\infty)
\]
come from the analytic coercivity and convexity argument, not from bounded search or finite sampling.

No closed form by radicals for the optimizer is claimed.
