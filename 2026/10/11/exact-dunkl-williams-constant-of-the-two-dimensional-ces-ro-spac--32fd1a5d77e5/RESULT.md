# Exact Dunkl--Williams constant of the two-dimensional Cesàro space
## Finding
Let \(X=\mathrm{ces}_2^{(2)}\) be the real plane with
\[
\|(x,y)\|_X
=
\left(
x^2+\left(\frac{|x|+|y|}{2}\right)^2
\right)^{1/2}.
\]
Then its Dunkl--Williams constant is
\[
DW(X)=\sqrt{\frac{32}{5}}=\frac{8}{\sqrt{10}}.
\]
After the linear normalization
\[
M(s,t)=\sqrt{s^2+t^2+\frac{2}{\sqrt5}|st|},
\]
the smooth points of the unit sphere contribute at most \(\sqrt5\) to \(DW\), while the sharp value is generated at a coordinate-axis point by Birkhoff--James directions \((r,1)\) with \(r\downarrow0\).

The sharp value is a supremum phenomenon at the nonsmooth coordinate axes of the normalized unit sphere. It is not produced by the smooth elliptical arcs.

## Assumptions and scope
The scalar field is real and the space is exactly the two-dimensional Cesàro space at exponent \(2\). The Dunkl--Williams constant is
\[
DW(X)
=
\sup_{x,y\in X\setminus\{0\},\,x\ne y}
\frac{\|x\|+\|y\|}{\|x-y\|}
\left\|
\frac{x}{\|x\|}-\frac{y}{\|y\|}
\right\|.
\]
Only this finite-dimensional Cesàro norm is treated. No claim is made for infinite-dimensional Cesàro spaces or for \(\mathrm{ces}_p^{(2)}\) with \(p\ne2\).

## Proof
Put
\[
c=\frac1{\sqrt5}.
\]
Since
\[
4\|(x,y)\|_X^2=5x^2+2|xy|+y^2,
\]
the linear change \((x,y)\mapsto(\sqrt5\,x,y)\), followed by a constant rescaling, reduces the problem to
\[
M(s,t)=\sqrt{s^2+t^2+2c|st|}.
\]
Thus \(DW(X)=DW(\mathbb R^2,M)\).

Define
\[
H_\pm(s,t)^2=s^2+t^2\pm2cst.
\]
Then
\[
M(s,t)^2=\max\{H_+(s,t)^2,H_-(s,t)^2\}.
\]

For a unit vector \(x\), let \(V(x)=\{y:x\perp_B y\}\). For \(y\in V(x)\), set
\[
\Gamma(x,y)=
\left\{
\frac{\lambda+\mu}{2}:
\lambda\le0\le\mu,\ 
M(x+\lambda y)=M(x+\mu y)
\right\},
\]
\[
m(x,y)=\sup_{\gamma\in\Gamma(x,y)}M(x+\gamma y),
\qquad
\mathcal M(x)=\sup_{y\in V(x)}m(x,y).
\]
The standard characterization gives
\[
DW(\mathbb R^2,M)=2\sup_{x\in S_M}\mathcal M(x).
\]

First consider a smooth point. Rotate by
\[
\xi=\frac{s+t}{\sqrt2},
\qquad
\eta=\frac{s-t}{\sqrt2}.
\]
Then
\[
H_+^2=(1+c)\xi^2+(1-c)\eta^2,
\qquad
H_-^2=(1-c)\xi^2+(1+c)\eta^2.
\]
By signed-coordinate and permutation symmetries, a smooth unit point may be written
\[
P(\theta)=
\left(
\frac{\cos\theta}{\sqrt{1+c}},
\frac{\sin\theta}{\sqrt{1-c}}
\right),
\qquad
0\le\theta<\theta_0,
\]
where
\[
\tan\theta_0
=
k
=
\sqrt{\frac{1-c}{1+c}}
=
\frac{\sqrt5-1}{2}.
\]
Its Birkhoff--James directions form the tangent line spanned by
\[
S(\theta)=
\left(
-\frac{\sin\theta}{\sqrt{1+c}},
\frac{\cos\theta}{\sqrt{1-c}}
\right).
\]
Along that line,
\[
M(P+\tau S)^2=\max\{1+\tau^2,Q(\tau)\},
\]
with \(Q\) quadratic and centered at \(\gamma_0<0\). Writing \(z=\tan\theta\),
\[
|\gamma_0|
=
\frac{z(1-k^4)}{1+k^4z^2}.
\]
For each norm level, the sublevel interval is the intersection of one interval centered at \(0\) and one centered at \(\gamma_0\). Hence every equal-level midpoint lies in \([\gamma_0,0]\). Convexity gives
\[
m(P,S)\le
\max\{M(P),M(P+\gamma_0S)\}
=
\sqrt{1+\gamma_0^2}.
\]
The displayed function of \(z\) is increasing on \(0\le z\le k\); using \(k^2+k=1\), its endpoint value is \(1/2\). Therefore every smooth unit point satisfies
\[
\mathcal M(P)\le\frac{\sqrt5}{2}.
\]

Now take the axis point \(e=(1,0)\). One-sided derivatives give
\[
e\perp_B(a,b)
\quad\Longleftrightarrow\quad
|a|\le c|b|.
\]
By symmetry and homogeneity, take
\[
y_r=(r,1),
\qquad
0\le r\le c.
\]
Along this line,
\[
M(e+\tau y_r)^2=\max\{q_+(\tau),q_-(\tau)\},
\]
where
\[
q_\pm(\tau)=1+2(r\pm c)\tau+A_\pm\tau^2,
\qquad
A_\pm=1+r^2\pm2cr.
\]
The two quadratic sublevel intervals are centered at
\[
\alpha_+=-\frac{r+c}{A_+},
\qquad
\alpha_-=\frac{c-r}{A_-}.
\]
Every equal-level midpoint lies between these centers, so
\[
m(e,y_r)\le
\max\{M(e+\alpha_+y_r),M(e+\alpha_-y_r)\}.
\]
At \(\alpha_+\), the \(q_-\)-branch dominates; at \(\alpha_-\), the \(q_+\)-branch dominates. With \(c=1/\sqrt5\),
\[
\frac85-q_-(\alpha_+)
=
\frac{8r^2(5r^2+4\sqrt5\,r+9)}
{25(1+r^2+2r/\sqrt5)^2}
\ge0,
\]
and
\[
\frac85-q_+(\alpha_-)
=
\frac{8r^2(5r^2-4\sqrt5\,r+9)}
{25(1+r^2-2r/\sqrt5)^2}
\ge0.
\]
The second numerator is positive because its quadratic discriminant is negative. Hence
\[
m(e,y_r)\le\sqrt{\frac85}.
\]

For \(r>0\), \(A_+>A_-\). At sufficiently large levels, the \(q_+\)-sublevel interval is strictly narrower and lies inside the \(q_-\)-sublevel interval. The equal-level midpoint is then exactly \(\alpha_+\), so
\[
m(e,y_r)\ge M(e+\alpha_+y_r).
\]
Letting \(r\downarrow0\) yields
\[
M(e+\alpha_+y_r)^2\longrightarrow\frac85.
\]
Therefore
\[
\mathcal M(e)=\sqrt{\frac85}.
\]

All nonsmooth sphere points are coordinate-axis images of \(e\), and every other sphere point is smooth. Since
\[
\frac{\sqrt5}{2}<\sqrt{\frac85},
\]
the global supremum is the axis value. Thus
\[
DW(X)
=
2\sqrt{\frac85}
=
\sqrt{\frac{32}{5}}
=
\frac8{\sqrt{10}}.
\]

## Verification
The normalized sphere consists of four smooth elliptical arcs meeting at four coordinate axes, so the smooth/axis split is exhaustive.

At a smooth point, the active quadratic norm is differentiable and the Birkhoff--James direction is its unique tangent. At an axis, the full Birkhoff cone is
\[
|a|\le\frac{|b|}{\sqrt5}.
\]
The two radical identities above verify the global axis upper bound. The lower bound is a genuine limiting argument using \(r>0\) and then \(r\downarrow0\). No numerical optimization, finite sampling, timeout, or external certificate is used as proof.

## Relationship to prior work
Maligranda, Petrot, and Suantai studied the same two-dimensional Cesàro space and calculated its James constant. Their paper establishes this plane as a natural geometric benchmark, but it does not discuss the Dunkl--Williams constant.

Mizuguchi, Saito, and Tanaka developed the Birkhoff--James midpoint characterization used here and applied it to the different Day--James plane \(\ell_2-\ell_\infty\). Their inspected full text contains no Cesàro-space calculation.

Recent work on Dunkl--Williams constants calculates several other two-dimensional spaces, including \(\ell_2-\ell_1\), but the checked statement does not include the two-dimensional Cesàro plane.

Targeted exact-value searches using the Cesàro notation, the normalized quadratic norm, and the candidate value \(\sqrt{32/5}\) did not locate an equivalent formula.

## Limitations
The result is specific to \(\mathrm{ces}_2^{(2)}\). It does not determine \(DW(\mathrm{ces}_p^{(2)})\) for general \(p\), nor any infinite-dimensional Cesàro-space Dunkl--Williams constant.

Search nonappearance is not treated as proof of originality. A differently notated or poorly indexed prior calculation remains a residual bibliographic risk.

## References
1. L. Maligranda, N. Petrot, and S. Suantai, “On the James constant and B-convexity of Cesàro and Cesàro--Orlicz sequence spaces,” *Journal of Mathematical Analysis and Applications* 326 (2007), 312--331, DOI 10.1016/j.jmaa.2006.02.085; available online 2006-04-17.
2. H. Mizuguchi, K.-S. Saito, and R. Tanaka, “On the calculation of the Dunkl--Williams constant of normed linear spaces,” *Open Mathematics* 11 (2013), 1212--1227, DOI 10.2478/s11533-013-0238-4; available online 2013-04-26.
3. J. Alonso and P. Martín, “Some results on the Dunkl--Williams constant,” arXiv:2604.02918, first posted 2026-04-03.
