# Exact Pareto-two tail for randomized heavy-ball momentum coefficients
## Finding

Consider either anytime construction in *Heavy-Ball Method under Randomized Schedules*. For a fixed
\[
k\ge1,
\]
condition on four successive boundaries
\[
A_{k-1}<A_k<A_{k+1}<A_{k+2}.
\]
Write
\[
h_-=A_k-A_{k-1},
\qquad
h_+=A_{k+1}-A_k,
\qquad
h_{++}=A_{k+2}-A_{k+1}.
\]

The evaluation times are conditionally independent with
\[
u_{k-1}\sim\mathrm{Unif}[A_{k-1},A_k],
\]
\[
u_k\sim\mathrm{Unif}[A_k,A_{k+1}],
\]
and
\[
u_{k+1}\sim\mathrm{Unif}[A_{k+1},A_{k+2}].
\]
The momentum coefficient is
\[
\beta_k=
\frac{u_k^{-2}-u_{k+1}^{-2}}
     {u_{k-1}^{-2}-u_k^{-2}}.
\]

Its conditional tail is exactly Pareto of exponent two in the asymptotic sense
\[
\mathbb P(\beta_k>t\mid A)
=
\frac{C_k(A)}{t^2}+o(t^{-2}),
\qquad
t\to\infty,
\]
where
\[
C_k(A)=
\frac{A_k^6}{8h_-h_+h_{++}}
\int_{A_{k+1}}^{A_{k+2}}
\left(A_k^{-2}-v^{-2}\right)^2\,dv.
\]
The constant is strictly positive.

Equivalently,
\[
C_k(A)=
\frac{A_k^6}{8h_-h_+h_{++}}
\left[
\frac{h_{++}}{A_k^4}
+
\frac{2}{A_k^2}
\left(
\frac1{A_{k+2}}-\frac1{A_{k+1}}
\right)
+
\frac13
\left(
\frac1{A_{k+1}^3}-\frac1{A_{k+2}^3}
\right)
\right].
\]

Therefore the exact conditional moment frontier is
\[
\mathbb E[\beta_k^p\mid A]<\infty
\quad\Longleftrightarrow\quad
0<p<2.
\]
In particular,
\[
\mathbb E[\beta_k\mid A]<\infty
\]
but
\[
\mathbb E[\beta_k^2\mid A]=\infty.
\]

For the deterministic-boundary anytime schedule, these are unconditional statements because the boundaries are fixed. For the randomized-boundary anytime schedule, the same frontier holds unconditionally for every fixed \\(k\\): conditioning already gives divergence for \\(p\ge2\\), while for \\(p<2\\) the finitely many random boundaries lie in a compact positive range with gaps bounded away from zero.

Thus the source statement that the random momentum coefficients may become arbitrarily large has a sharper distributional form: each fixed-time momentum coefficient has a \\(t^{-2}\\) upper tail, finite mean, and infinite variance.

## Assumptions and scope

The result concerns the two anytime schedules in the source, both of which use
\[
\beta_k=
\frac{u_k^{-2}-u_{k+1}^{-2}}
     {u_{k-1}^{-2}-u_k^{-2}},
\qquad
k\ge1.
\]

For deterministic boundaries, the source uses
\[
A_k=\left(1+\frac{k}{12}\right)^{4/3}
\]
and samples each \\(u_k\\) independently and uniformly from its interval.

For randomized boundaries, the source first samples the increasing boundary process and then sets
\[
u_k=A_k+(A_{k+1}-A_k)U_k,
\qquad
U_k\sim\mathrm{Unif}[0,1],
\]
with independent \\(U_k\\). Hence the same conditional independent-uniform structure holds after conditioning on the realized boundaries.

No property of the objective function or of the heavy-ball iterates is used in the tail calculation. The result is a property of the randomized schedule itself.

The fixed-time construction is not claimed here because its terminal evaluation time is treated differently. Interior coefficients with three independently uniform evaluation times obey the same proof.

## Proof

Set
\[
a=A_{k-1},
\qquad
A=A_k,
\qquad
B=A_{k+1},
\qquad
C=A_{k+2}.
\]
Introduce nonnegative local coordinates
\[
x=A-u_{k-1},
\qquad
y=u_k-A,
\qquad
z=u_{k+1}-B.
\]
They are independent uniforms on
\[
[0,A-a],
\qquad
[0,B-A],
\qquad
[0,C-B].
\]

Write
\[
D(x,y)=(A-x)^{-2}-(A+y)^{-2},
\]
and
\[
N(y,z)=(A+y)^{-2}-(B+z)^{-2}.
\]
Then
\[
\beta_k=\frac{N(y,z)}{D(x,y)}.
\]

Because
\[
D(x,y)=\int_{A-x}^{A+y}2s^{-3}\,ds,
\]
we have
\[
D(x,y)=2A^{-3}(x+y)+o(x+y)
\]
uniformly as \\((x,y)\to(0,0)\\). For fixed \\(z\\),
\[
N(y,z)\longrightarrow n(z):=A^{-2}-(B+z)^{-2}
\]
as \\(y\downarrow0\\), and
\[
n(z)>0
\]
throughout \\(0\le z\le C-B\\).

Now scale
\[
x=\frac{X}{t},
\qquad
y=\frac{Y}{t}.
\]
For each fixed \\(z\\), the event \\(\beta_k>t\\) converges under this scaling to
\[
X+Y<\frac{A^3n(z)}2,
\qquad
X\ge0,
\quad
Y\ge0.
\]
The area of that triangle is
\[
\frac12\left(\frac{A^3n(z)}2\right)^2
=
\frac{A^6n(z)^2}{8}.
\]

Multiplying by the joint uniform density and integrating in \\(z\\) gives
\[
\lim_{t\to\infty}t^2\mathbb P(\beta_k>t\mid A)
=
\frac{A^6}{8(A-a)(B-A)(C-B)}
\int_0^{C-B}
\left(A^{-2}-(B+z)^{-2}\right)^2\,dz.
\]
Changing variables \\(v=B+z\\) gives the stated constant.

The closed form follows by integrating
\[
\left(A^{-2}-v^{-2}\right)^2
=A^{-4}-2A^{-2}v^{-2}+v^{-4}.
\]

For the moment frontier, the integral representation of \\(D\\) shows that it is comparable to \\(x+y\\) on the compact boundary interval. The numerator is bounded above. Hence
\[
\beta_k^p\le K(x+y)^{-p}
\]
for a finite constant \\(K\\), and
\[
\int_0^\varepsilon\int_0^\varepsilon(x+y)^{-p}\,dx\,dy
\]
is finite exactly when \\(p<2\\). This proves finiteness for \\(0<p<2\\).

Conversely, on a sufficiently small square near \\(x=y=0\\), the numerator is bounded below by a positive constant while the denominator is bounded above by a constant multiple of \\(x+y\\). Therefore
\[
\beta_k^p\ge K'(x+y)^{-p}
\]
there, and the same double integral diverges for \\(p\ge2\\).

For randomized boundaries, conditioning proves the divergence branch immediately. For fixed \\(k\\), the recurrence
\[
A_{j+1}=A_j+\frac{A_j^{1/3}}{512}V_j,
\qquad
V_j\in[1,2],
\]
keeps the finitely many relevant boundaries inside deterministic positive upper and lower bounds, with each gap bounded away from zero. The conditional estimates are therefore uniformly integrable for every \\(p<2\\), which yields the same unconditional moment frontier.

## Verification

The standalone script `artifacts/verify_momentum_tail.py` evaluates the exact tail constant for the first nontrivial coefficient of the deterministic-boundary anytime schedule and numerically integrates the exact three-uniform probability. It confirms convergence of
\[
t^2\mathbb P(\beta_1>t)
\]
to the analytic constant.

The numerical integration is supporting evidence only. The proof above establishes the tail limit and moment threshold for every admissible boundary quadruple.

## Relationship to prior work

The source introduces the randomized anytime schedules and explicitly remarks that their momentum coefficients can exceed one and can be arbitrarily large. It does not state a tail law, finite-moment threshold, or variance property for those coefficients.

The present calculation sharpens that qualitative observation to a complete fixed-\\(k\\) distributional boundary:
\[
\mathbb P(\beta_k>t)\asymp t^{-2},
\]
with an exact leading constant and a sharp moment cutoff at order two.

Related stochastic heavy-ball literature studies random gradients, randomized linear-system updates, and adaptive momentum, but the inspected records do not use this adjacent-uniform reciprocal-time ratio or derive the same coefficient-tail law.

## Limitations

The theorem is about each fixed momentum coefficient. It does not claim independence of the sequence \\((\beta_k)\\), because adjacent coefficients share evaluation times.

Infinite variance of \\(\beta_k\\) does not by itself imply instability of the heavy-ball iterates. The source convergence analysis couples the coefficients to its interpolation construction, and the present result does not contradict those convergence guarantees.

The tail constant depends on the local boundary geometry and therefore varies with \\(k\\) and, in the randomized-boundary construction, with the realized boundaries.

## References

1. C. He, S. Zhang, *Heavy-Ball Method under Randomized Schedules*, arXiv:2609.09743v1, 2026.
2. D. Han, Y. Su, J. Xie, *Randomized Douglas--Rachford Methods for Linear Systems: Improved Accuracy and Efficiency*, SIAM Journal on Optimization 34(1), 1045--1070, 2024. DOI: 10.1137/23M1567503.
