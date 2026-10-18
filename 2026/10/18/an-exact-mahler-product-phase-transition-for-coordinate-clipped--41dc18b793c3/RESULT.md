# An exact Mahler-product phase transition for coordinate-clipped \(\ell_p\) balls

## Finding
For each integer \(d\ge2\), exponent \(1<p<\infty\), and clipping depth \(0<a\le1\), let
\[
B_p^d=\bigl\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|^p\le1\bigr\},\qquad
K_{d,p,a}=B_p^d\cap\{|x_1|\le a\}.
\]
Write \(K^\circ=\{y:\langle x,y\rangle\le1\text{ for every }x\in K\}\) and \(\mathcal M_{d,p}(a)=\operatorname{vol}_d(K_{d,p,a})\operatorname{vol}_d(K_{d,p,a}^\circ)\).
Let \(m=d-1\), \(q=p/(p-1)\), \(v=1-a^p\), and
\[
\kappa_{r,j}=\frac{2^j\Gamma(1+1/r)^j}{\Gamma(1+j/r)},\quad
F(a)=\int_0^a(1-s^p)^{m/p}\,ds,\quad
G(a)=\int_0^{a^{p-1}}(1-s^q)^{m/q}\,ds,\quad
H(a)=G(a)+\frac{v^{1+m/q}}{da}.
\]
The exact volume-product identity is
\[
\boxed{\mathcal M_{d,p}(a)=4\kappa_{p,m}\kappa_{q,m}F(a)H(a).}
\]
If \(p\ge2\), \(\mathcal M_{d,p}\) is strictly increasing on \((0,1)\), so the unique maximizing depth is \(a=1\) (no clipping). If \(1<p<2\), there is exactly one maximizing depth \(a_*(d,p)\in(0,1)\); the product increases strictly for \(a<a_*\) and decreases strictly for \(a>a_*\), and \(a_*\) is the unique solution of
\[
\boxed{d a^2(1-a^p)^{m(2-p)/p}H(a)=F(a).}
\]
The result holds uniformly in every stated dimension and exponent, not just at sampled parameter values. The limiting endpoint is \(\lim_{a\downarrow0}\mathcal M_{d,p}(a)=4\kappa_{p,m}\kappa_{q,m}/d\); the uncut endpoint is \(\mathcal M_{d,p}(1)=\kappa_{p,d}\kappa_{q,d}\).

## Assumptions and scope
All bodies are full-dimensional, origin-symmetric, and have the ordinary Euclidean scalar-product polar. The given norm is the coordinate \(\ell_p\) norm, not an arbitrarily rotated or translated slab. The parameters are precisely \(d\in\{2,3,\dots\}\), \(1<p<\infty\), and \(0<a\le1\). No claim is made for the nonsmooth endpoint exponents \(p=1,\infty\), or for uncentered clipping.

## Proof
**1. Exact polar sections.** By elementary polarity of intersections,
\[
K_{d,p,a}^\circ=\operatorname{conv}\bigl(B_q^d,\,e_1/a,\,-e_1/a\bigr).
\]
The \(x_1=s\) section of \(B_p^d\) has \((d-1)\)-volume \(\kappa_{p,m}(1-|s|^p)^{m/p}\), giving \(\operatorname{vol}_d(K)=2\kappa_{p,m}F(a)\).
For the polar, its positive-axis section radius agrees with \(\phi(s)=(1-s^q)^{1/q}\) until the tangent cone from \(e_1/a\) meets \(B_q^d\). The tangent-line axis intercept at \(s>0\) is \(s-\phi(s)/\phi'(s)=s^{-(q-1)}\). Thus the tangency section occurs exactly at \(s=a^{p-1}\), with transverse radius \(v^{1/q}\), after which the hull section radius decreases linearly to zero at \(s=1/a\). Fubini, using \(1/a-a^{p-1}=v/a\), gives
\[
\operatorname{vol}_d(K^\circ)=2\kappa_{q,m}\left[G(a)+\frac{(v^{1/q})^m}{d}\left(\frac1a-a^{p-1}\right)\right]=2\kappa_{q,m}H(a).
\]
Multiplication proves the stated exact identity, including the endpoints by continuity.

**2. Critical-point reduction.** Put \(f=v^{m/p}\), \(g=v^{m/q}\), and \(\eta=m(2-p)/p\). Direct differentiation of the integral and conical terms yields the unusually simple cancellation
\[
F'(a)=f,\qquad H'(a)=-\frac{g}{d a^2}.
\]
Indeed, differentiating \(G(a)\) contributes \((p-1)a^{p-2}g\); differentiating \(v^{1+m/q}/(da)\) cancels that contribution except for \(-g/(d a^2)\). Therefore the sign of \(\mathcal M_{d,p}'(a)\) is the sign of
\[
W(a)=d a^2v^\eta H(a)-F(a),\qquad
\mathcal M_{d,p}'(a)=\frac{4\kappa_{p,m}\kappa_{q,m}g}{d a^2}W(a).
\]

**3. A strictly decreasing auxiliary function.** Let \(t=a^p\), \(\beta=m/q\), and define
\[
J(t)=\int_0^1\left(\frac{1-ts^q}{1-t}\right)^\beta ds,\qquad
A(t)=dJ(t)-1,\qquad
T(t)=\frac{(1-t)A(t)}{1+tA(t)},\qquad c=\frac{m(2-p)}2.
\]
For \(0<t<1\), \(J(t)\ge1\) and hence \(A(t)\ge m>0\). Differentiation under the integral gives
\[
(1-t)J'(t)=\beta\int_0^1\left(\frac{1-ts^q}{1-t}\right)^\beta\frac{1-s^q}{1-ts^q}\,ds
\le\beta J(t).
\]
It follows that
\[
T'(t)=\frac{d(1-t)J'(t)-A(t)(1+A(t))}{(1+tA(t))^2}<0,
\]
because \(A(1+A)=(dJ-1)dJ\ge mdJ>\beta dJ\). Also \(T(0+)=m\) and \(T(1-)=0\). The last limit holds since \(J(t)=O((1-t)^{-\beta})\) and \((1-t)A/(1+tA)\le(1-t)/t\).
Since \(aG(a)/g=tJ(t)\), a substitution of \(H\) into the derivative of \(W\) simplifies **exactly** to
\[
\boxed{W'(a)=\frac{2f\,t(1+tA(t))}{1-t}\bigl[T(t)-c\bigr].}
\]
As \(a\downarrow0\), \(W(a)\to0\). If \(p\ge2\), then \(c\le0<T(t)\), and \(W'(a)>0\) throughout \((0,1)\); hence \(W>0\) and \(\mathcal M'_{d,p}>0\).
If \(1<p<2\), then \(0<c<m\), so strict monotonicity of \(T\) shows that \(W\) increases on one initial interval and decreases on its complement. Moreover \(W(1-)=-F(1)<0\) because \(\eta>0\). Since \(W(0+)=0\), there is precisely one zero \(a_*\in(0,1)\), necessarily with a positive-to-negative sign change. The sign formula for \(\mathcal M'\) proves the full phase law and strict uniqueness of the maximizer.

## Verification
The accompanying `mahler_checker.py` recomputes the integrals by adaptive quadrature, locates the sole stationary point for five parameter pairs with \(p<2\), checks the sign pattern for selected \(p\ge2\), and compares the planar polar-section area with an independent angular radial formula for five other pairs. It also confirms the exact algebraic specialization
\[
\mathcal M_{3,2}(a)=\frac{4\pi^2}{9}\left(3+2a^2-a^4\right).
\]
For example, the computed maximizers are \(a_*(2,1.5)\approx0.949020780328\), \(a_*(3,1.5)\approx0.905389178252\), and \(a_*(4,1.5)\approx0.861773876011\). These are reproducibility diagnostics; the infinite-parameter assertion rests on the preceding proof, not on a finite grid.

## Relationship to prior work
Böröczky–Makai–Meyer–Reisner (2013) establish sharp general planar Mahler lower bounds and stability, and supply the archival convex-geometric motivation; their main theorem is not a coordinate-cut product formula or an optimization over clipping depth. Reisner–Schütt–Werner (2010) discuss local behavior of the volume product under geometric perturbations but do not state this all-dimensional coordinate-cut transition. Barthe–Fradelizi (2013) treat invariant bodies with many reflection hyperplanes and general volume-product bounds, not this explicit cut-parameter optimization in the material accessible. The exact coefficient law and \(p=2\) transition are distinct from the volume-only plank bounds, cube–crosspolytope interpolation, simplex difference-body interpolation, and Ball's quadratic Santaló **moment** product.

## Limitations
Only centered, coordinate-aligned single-axis clipping of finite-exponent \(\ell_p\) balls is covered. The optimal depth for \(1<p<2\) is implicitly characterized, not generally elementary; no classification for arbitrary slabs, rotated slabs, or other convex bodies follows. Independent external validation has not been performed. The full text of Barthe–Fradelizi's paper was unavailable during the literature comparison, so an unrecognized earlier equivalent special case remains a residual priority risk.

## References
- K. J. Böröczky, E. Makai Jr., M. Meyer, S. Reisner, *On the volume product of planar polar convex bodies — Lower estimates with stability*, Studia Sci. Math. Hungar. 50 (2013), 159–198. DOI: 10.1556/SScMath.50.2013.2.1235. Public online 20 June 2013. Open text: https://arxiv.org/pdf/1507.01481.
- S. Reisner, C. Schütt, E. Werner, *A note on Mahler's conjecture*, International Mathematics Research Notices (2012), preprint https://arxiv.org/abs/1009.3583.
- F. Barthe, M. Fradelizi, *The volume product of convex bodies with many hyperplane symmetries*, American Journal of Mathematics 135 (2013), DOI: 10.1353/ajm.2013.0018.
