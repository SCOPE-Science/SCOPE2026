# A Kanter-type lower bound for the generalized Bessel sum at every real order

## Statement

For \(\nu\ge -\tfrac12\) and \(x>0\), define
\[
\Phi_\nu(x)=e^{-x}x^{-\nu}\bigl(I_\nu(x)+I_{\nu+1}(x)\bigr),
\]
where \(I_\nu\) is the modified Bessel function of the first kind. Baricz and
Pogány (2014) proved Kanter's inequality for \(\Phi_0\) and ended their paper
with the open problem of finding a generalization for \(\Phi_\nu\).

The following gives such a generalization for the full real-order range in
which their integral representation is available.

**Theorem.** For every \(r\ge0\) and \(\nu\ge-\tfrac12\),
\[
\boxed{
\Phi_\nu(2r)\ge
2^{-2r-\nu}
\frac{\Gamma(2r+1)}{\Gamma(r+1)\Gamma(r+\nu+1)}.}
\tag{1}
\]
Equality holds for every \(\nu\ge-\tfrac12\) when \(r=0\), and for every
\(r\ge0\) when \(\nu=-\tfrac12\). For \(r>0\) and \(\nu>-\tfrac12\), the
inequality is strict.

At \(\nu=0\), (1) is exactly the real-variable Kanter inequality proved by
Baricz and Pogány:
\[
 e^{-2r}\bigl(I_0(2r)+I_1(2r)\bigr)
 \ge 2^{-2r}\frac{\Gamma(2r+1)}{\Gamma(r+1)^2}.
\]
The constant in (1) is also asymptotically sharp for every fixed \(\nu\):
both sides are
\[
\frac{2^{-\nu}}{\sqrt\pi}\,r^{-\nu-1/2}(1+o(1))
\qquad(r\to\infty).
\]

Equivalently, with \(a=\nu+\tfrac12\ge0\),
\[
{}_1F_1(a;2a+1;-4r)
\ge
\frac{\Gamma(r+\tfrac12)\Gamma(a+\tfrac12)}
     {\sqrt\pi\,\Gamma(r+a+\tfrac12)}.
\tag{2}
\]

## Integral reduction

For \(\nu>-\tfrac12\), the Baricz--Pogány integral representation can be
written as
\[
\sqrt\pi\,2^\nu\Gamma\!\left(\nu+\tfrac12\right)\Phi_\nu(x)
=
\int_0^\pi e^{-x(1-\cos\theta)}(1+\cos\theta)
\sin^{2\nu}\!\theta\,d\theta.
\tag{3}
\]
Put \(x=2r\). Pairing \(\theta\) and \(\pi-\theta\) shows that replacing the
exponential in (3) by \(|\cos\theta|^{2r}\) gives
\[
\int_0^\pi |\cos\theta|^{2r}(1+\cos\theta)
\sin^{2\nu}\!\theta\,d\theta
=B\!\left(r+\tfrac12,\nu+\tfrac12\right).
\tag{4}
\]
Thus (1) is equivalent, for \(r>0\) and \(\nu>-\tfrac12\), to positivity of
\[
A_\nu(r)=2\int_0^1 G_r(c)(1-c^2)^{\nu-1/2}\,dc,
\tag{5}
\]
where
\[
G_r(c)=e^{-2r}\bigl(\cosh(2rc)+c\sinh(2rc)\bigr)-c^{2r}.
\tag{6}
\]

## One-sign-change lemma

**Lemma 1.** For each \(r>0\), there is a unique \(c_r\in(0,1)\) such that
\[
G_r(c)>0\quad(0<c<c_r),\qquad
G_r(c)<0\quad(c_r<c<1).
\tag{7}
\]
Also \(G_r(1)=0\).

*Proof.* Write \(k=2r\) and
\[
Q(c)=\log\!\left(
\frac{e^{-k}(\cosh(kc)+c\sinh(kc))}{c^k}
\right),\qquad 0<c\le1.
\]
The sign of \(Q\) is the sign of \(G_r\). A direct differentiation gives
\[
\operatorname{sgn}Q'(c)
=
\operatorname{sgn}\left[c\tanh(kc)-k(1-c^2)\right].
\]
The bracket has derivative
\[
\tanh(kc)+kc\,\operatorname{sech}^2(kc)+2kc>0,
\]
starts at \(-k\), and ends at \(\tanh k>0\). Hence \(Q\) decreases and then
increases, with exactly one critical point. Moreover
\(Q(c)\to+\infty\) as \(c\downarrow0\), while \(Q(1)=0\) and
\(Q'(1)>0\), so \(Q<0\) immediately to the left of \(1\). Therefore there
is exactly one interior zero, with the sign pattern (7). \(\square\)

## A boundary-weight integral

The sign-change lemma reduces all orders to a single limiting weight. Define
\[
F(r)=2\int_0^1\frac{G_r(c)}{1-c^2}\,dc.
\tag{8}
\]
The integral is finite: \(G_r(1)=0\) and \(G_r\) has a finite derivative at
\(1\).

**Lemma 2.** \(F(r)>0\) for every \(r>0\).

*Proof.* Put \(c=1-2v\) in (8). Then
\[
F(r)=\int_0^{1/2}
\frac{(1-v)e^{-4rv}+ve^{-4r(1-v)}-(1-2v)^{2r}}
     {v(1-v)}\,dv.
\tag{9}
\]
Using a common cutoff at \(v=\varepsilon\), the first two exponential terms
combine into
\(\int_\varepsilon^{1-\varepsilon}e^{-4ru}\,du/u\), while the power term,
after \(y=(1-2v)^2\), becomes
\(\int_0^{(1-2\varepsilon)^2}y^{r-1/2}\,dy/(1-y)\). Letting
\(\varepsilon\downarrow0\) and using the standard integral formula for the
digamma function yields
\[
F(r)=\psi\!\left(r+\tfrac12\right)-\log r+\operatorname{Ei}(-4r).
\tag{10}
\]

It remains to prove that the right side is positive. Its derivative is
\[
F'(r)=\psi_1\!\left(r+\tfrac12\right)-\frac{1-e^{-4r}}r
=
\int_0^\infty e^{-rt}K(t)\,dt,
\tag{11}
\]
where
\[
K(t)=\frac{t}{2\sinh(t/2)}-\mathbf 1_{(0,4)}(t).
\tag{12}
\]
Thus \(K(t)<0\) on \((0,4)\) and \(K(t)>0\) on \((4,\infty)\): it has one
sign change, from negative to positive. Consequently \(F'\) has at most one
zero. Indeed, if \(F'(r_0)=0\), then for \(r>r_0\), multiplication by the
strictly decreasing function \(e^{-(r-r_0)t}\) gives strictly more relative
weight to the negative part \(t<4\), hence \(F'(r)<0\).

Furthermore
\[
F'(0+)=\int_0^\infty K(t)\,dt
=\psi_1\!\left(\tfrac12\right)-4
=\frac{\pi^2}{2}-4>0.
\]
The standard endpoint expansions
\(\psi(\tfrac12)=-\gamma-2\log2\),
\(\operatorname{Ei}(-4r)=\gamma+\log(4r)+O(r)\) at zero and the usual
large-argument expansions of \(\psi\) and \(\operatorname{Ei}\) give
\[
F(0+)=0,\qquad F(\infty)=0.
\]
Since \(F'\) starts positive, can cross zero at most once, and \(F\) returns
to zero at infinity, it follows that \(F(r)>0\) for every \(r>0\). \(\square\)

## Completion of the proof

Let
\[
a=\nu+\tfrac12>0,
\qquad h_a(c)=(1-c^2)^a.
\]
Then (5) is
\[
A_\nu(r)=2\int_0^1
\frac{G_r(c)}{1-c^2}\,h_a(c)\,dc.
\tag{13}
\]
The function \(h_a\) is strictly decreasing. Let \(c_r\) be the unique sign
change from Lemma 1. Because \(G_r\) is positive before \(c_r\) and negative
after it,
\[
\begin{aligned}
\frac12 A_\nu(r)
&-h_a(c_r)\frac12F(r)\\
&=\int_0^1\frac{G_r(c)}{1-c^2}
\bigl(h_a(c)-h_a(c_r)\bigr)\,dc>0.
\end{aligned}
\]
Lemma 2 gives \(F(r)>0\), hence \(A_\nu(r)>0\). Equations (3)--(5) now give
(1), strictly for \(r>0\) and \(\nu>-\tfrac12\).

At \(r=0\), both sides of (1) equal \(2^{-\nu}/\Gamma(\nu+1)\). At
\(\nu=-\tfrac12\), the elementary half-order formulas
\[
I_{-1/2}(x)=\sqrt{\frac{2}{\pi x}}\cosh x,
\qquad
I_{1/2}(x)=\sqrt{\frac{2}{\pi x}}\sinh x
\]
give \(\Phi_{-1/2}(x)=\sqrt{2/\pi}\); the right side of (1) has the same
value by Legendre duplication. This completes the proof for the full stated
range.

## Context and originality

Baricz and Pogány proved the \(\nu=0\) real-variable inequality and explicitly
ended their 2014 paper with the problem of finding a generalization for
\(\Phi_\nu\). Their full paper, including the relevant integral representation,
existing bounds, order-convexity results, Theorem 3, and the stated open problem,
was inspected.

The literature check covered the paper title and DOI, the open-problem wording,
Kanter inequalities combined with \(\Phi_\nu\), the exact gamma-factor pattern in
(1), the equivalent confluent-hypergeometric inequality (2), and combinations
with modified Bessel sums, digamma functions, and exponential integrals. A 2026
paper by Veestraeten revisits the same generalized expression \(\Phi_\nu\) and
rewrites it in terms of a single \({}_1F_1\), but does not state the lower bound
(1); it refers back to Baricz--Pogány for the properties of \(\Phi_\nu\).
No source located through the publication date states (1), (2), or a full
real-order solution of the 2014 open problem.

Accordingly, originality is claimed **to the best of our knowledge**. A prior
result under a substantially different special-function formulation, or an
unindexed/unpublished source, remains a residual possibility.

## Limitations

The theorem gives a sharp-asymptotic lower bound but does not claim that the
right side is the largest possible pointwise lower bound at finite \(r\). It does
not derive a probabilistic concentration theorem corresponding to arbitrary real
\(\nu\); the result is an analytic inequality for the generalized Bessel sum.
The originality search cannot exclude differently phrased or poorly indexed prior
coverage. 

## References

1. Á. Baricz and T. K. Pogány, *On a Sum of Modified Bessel Functions*,
   Mediterranean Journal of Mathematics **11** (2014), 349--360.
   https://doi.org/10.1007/s00009-013-0365-y

2. L. Mattner and B. Roos, *A shorter proof of Kanter's Bessel function
   concentration bound*, Probability Theory and Related Fields **139** (2007),
   191--205. https://doi.org/10.1007/s00440-006-0043-0

3. D. Veestraeten, *On Finite and Infinite Sums of the Modified Bessel Function
   of the First Kind*, Mediterranean Journal of Mathematics **23** (2026),
   Article 53. https://doi.org/10.1007/s00009-026-03050-1
