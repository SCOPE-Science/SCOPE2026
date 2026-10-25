# A sharp dimension-free Mahler envelope for one-axis cross-polytope extrusions

## Finding
For each integer \(d\ge2\) and \(h>0\), let \(B_1^d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\) and let
\[
K_{d,h}=B_1^d+[-h,h]e_1.
\]
Write \(\mathcal P(K)=\operatorname{vol}_d(K)\operatorname{vol}_d(K^\circ)\), where the polar is taken about the origin. Then the complete Mahler-volume profile is
\[
\boxed{M_d(h):=\frac{\mathcal P(K_{d,h})}{4^d/d!}=
\frac{1+dh}{dh}\left(1-(1+h)^{-d}\right).}
\]
For every fixed dimension \(d\ge2\), this profile exceeds \(1\) at each finite positive \(h\), tends to \(1\) at both ends, and has **exactly one** maximizer. If \(t_d\in(0,1)\) is the unique root of
\[
\sum_{j=1}^{d-1}j\,t^{j-1}=d(d-1)t^{d-1},
\]
then its maximizing parameter is exactly \(h_d=t_d^{-1}-1\).

There is a *sharp, dimension-independent* strict upper bound:
\[
\boxed{1<M_d(h)<C_*:=\frac{(1+\alpha_*)^2}{1+\alpha_*+\alpha_*^2}
=1.298425607525639\ldots,}
\]
where \(\alpha_*>1\) is the unique positive solution of \(e^{\alpha}=1+\alpha+\alpha^2\) (numerically \(\alpha_*=1.793282132900761\ldots\)).
Let \(\mu_d=M_d(h_d)\). Then \(\mu_d\) increases **strictly** with dimension, \(\mu_d\uparrow C_*\), and \(dh_d\to\alpha_*\). Hence the constant \(C_*\) cannot be decreased, although equality never holds in a finite dimension. For \(d=2\), \(h_2=1\) and \(\mu_2=9/8\).

## Assumptions and scope
All bodies are in ordinary Euclidean \(\mathbb R^d\), with Lebesgue volume. Minkowski addition and centered polarity are used. The body \(K_{d,h}\) is centrally symmetric and full-dimensional, so the origin is its Santaló center. The normalization \(4^d/d!\) equals the Mahler product of the cross-polytope and of the Cartesian product of a line segment with a lower-dimensional cross-polytope. Claims about strict inequalities require finite \(d\ge2\) and \(0<h<\infty\); the asymptotic statement takes \(d\to\infty\) through integers.

The structural motivation is a one-axis Minkowski deformation between two Hanner-type equality geometries. The theorem characterizes its entire all-dimensional volume-product excursion, rather than claiming a universal extremum over all convex bodies.

## Proof
**1. Primal volume.** Write \(x=(s,y)\) with \(y\in\mathbb R^{d-1}\). On the base \(B_1^{d-1}\), the fiber of \(B_1^d\) has length \(2(1-\|y\|_1)\), while the fiber of \(K_{d,h}\) has length \(2(1-\|y\|_1+h)\). Therefore
\[
\operatorname{vol}_d(K_{d,h})=\frac{2^d}{d!}+2h\frac{2^{d-1}}{(d-1)!}
=\frac{2^d}{d!}(1+dh).
\]
This argument proves the identity for every positive real \(h\), not merely rational examples.

**2. Polar volume.** Minkowski support functions add and the support of \(B_1^d\) is \(\|u\|_\infty\). Hence
\[
K_{d,h}^{\circ}=\left\{u:\max_{1\le j\le d}|u_j|+h|u_1|\le1\right\}.
\]
Equivalently, \(|u_1|\le(1+h)^{-1}\) and, for every \(j\ge2\), \(|u_j|\le1-h|u_1|\). These bounds are simultaneous: the first ensures that the first coordinate also satisfies the maximum constraint. Integration of the remaining \(d-1\) independent coordinates gives
\[
\operatorname{vol}_d(K_{d,h}^{\circ})=
2^d\int_{0}^{1/(1+h)}(1-hs)^{d-1}\,ds
=\frac{2^d}{dh}\left(1-(1+h)^{-d}\right).
\]
Multiplication with the primal volume yields the asserted exact formula.

**3. Strict positivity and a unique finite-dimensional peak.** Put \(t=(1+h)^{-1}\in(0,1)\). A finite geometric sum rearranges the profile as
\[
M_d(h)=1+\frac1d\left(\sum_{j=1}^{d-1}t^j-(d-1)t^d\right).
\]
Every summand \(t^j-t^d\) for \(j<d\) is positive, so \(M_d(h)>1\). Both endpoint limits are \(1\). The derivative with respect to \(t\) has the sign of
\[
Q_d(t)=\sum_{j=1}^{d-1}j\,t^{j-1}-d(d-1)t^{d-1}.
\]
After dividing by \(t^{d-1}\), its zero equation becomes
\[
\sum_{j=1}^{d-1}j\,t^{j-d}=d(d-1).
\]
The left-hand side strictly decreases from \(+\infty\) as \(t\downarrow0\) to \(d(d-1)/2\) at \(t=1\). Exactly one root exists, with derivative changing from positive to negative. Since \(h\mapsto t\) is bijective, this gives the unique global maximizing \(h_d\).

**4. A sharp universal envelope.** Set \(\alpha=dh\). The strict inequality \(\log(1+\alpha/d)<\alpha/d\) gives
\[
M_d(\alpha/d)<g(\alpha):=
\left(1+\frac1\alpha\right)(1-e^{-\alpha}),\qquad\alpha>0.
\]
The derivative satisfies
\[
\alpha^2g'(\alpha)=e^{-\alpha}(1+\alpha+\alpha^2)-1.
\]
Thus its positive critical points solve \(e^\alpha=1+\alpha+\alpha^2\). The auxiliary function \(q(\alpha)=\alpha-\log(1+\alpha+\alpha^2)\) has derivative
\[
q'(\alpha)=\frac{\alpha(\alpha-1)}{1+\alpha+\alpha^2}.
\]
It starts at zero, decreases strictly until \(1\), then increases strictly toward infinity. There is consequently exactly one positive root \(\alpha_*>1\), and \(g\) increases before it and decreases after it. At this root,
\[
\max_{\alpha>0}g(\alpha)=g(\alpha_*)=
\frac{(1+\alpha_*)^2}{1+\alpha_*+\alpha_*^2}=C_*.
\]
Both endpoint limits of \(g\) are \(1\). This proves the strict all-dimensional bound.

**5. Dimension monotonicity and sharpness.** For every fixed \(\alpha>0\), the function \(x\mapsto x\log(1+\alpha/x)\) has positive derivative, because \(\log(1+z)>z/(1+z)\) for \(z>0\). Therefore \((1+\alpha/d)^d\) strictly increases with integer \(d\). As a result, \(M_d(\alpha/d)\) strictly increases with \(d\), with limit \(g(\alpha)\). Evaluating the \((d+1)\)-dimensional profile at \(\alpha=dh_d\) shows \(\mu_{d+1}>\mu_d\). The upper bound \(\mu_d<C_*\), together with \(\mu_d\ge M_d(\alpha_*/d)\to C_*\), implies \(\mu_d\uparrow C_*\). Finally, put \(\alpha_d=dh_d\). Since \(g(\alpha)\to1\) at both boundaries but \(\mu_d\to C_*>1\), the inequalities \(\mu_d<g(\alpha_d)\) force \(\alpha_d\) eventually into a common compact subinterval of \((0,\infty)\). On compact intervals \(M_d(\alpha/d)\to g(\alpha)\) uniformly. Every subsequential limit of \(\alpha_d\) must therefore maximize \(g\), and uniqueness forces \(dh_d\to\alpha_*\). This completes the proof.

## Verification
The accompanying standard-library script `verify.py` checks the polar-volume integral through an independently expanded polynomial antiderivative in exact rational arithmetic, compares the normalized product with the original volume product, computes unique finite-dimensional maximizers, and checks monotonicity and the sharp envelope numerically. Invoke `python3 verify.py` in the directory containing the script. The expected success prefix is `VERIFY_OK 1490` followed by root and bound values. Its tests are finite diagnostics, and the proof above independently handles every dimension and positive real parameter.

## Relationship to prior work
The Hanner-polytope literature supplies volume-product minimizers and local stability. In particular, Kim's *Minimal volume product near Hanner polytopes* (first publicly posted 2012-12-11, arXiv:1212.2544v1) proves local minimality of Hanner polytopes. Local lower-bound theory does not imply the exact positive-parameter formula, unique maximum, or dimension-uniform optimal upper bound here.

Two closely related but geometrically different complete mathematical treatments are *Exact Mahler products for cube–cross-polytope intersections and their three-dimensional phase diagram* and *Exponential Mahler growth along the cube–cross-polytope Minkowski interpolation*. Their full `RESULT.md` texts were compared. The former treats the intersection \([-1,1]^d\cap\{\|x\|_1\le t\}\), whose polar is a different body. The latter treats \([-1,1]^d+tB_1^d\), which adds an entire cross-polytope to a cube: its maximum normalized volume product grows exponentially in dimension, whereas the present *single-coordinate segment extrusion of the cross-polytope* has a bounded normalized product with one peak for each dimension. The same equation \(e^\alpha=1+\alpha+\alpha^2\) appears in the latter work's large-dimensional saddle; this coincidence of a scalar constant is explicitly acknowledged, but neither theorem is a specialization of the other. The profile and sharp dimension-free statement here are not claims about the full cube–cross-polytope interpolation.

## Limitations
The result concerns exactly this one-parameter unconditional convex family. It proves no universal upper bound for arbitrary unconditional bodies, no general Mahler conjecture, and no claim that a sharp constant for some other interpolation must coincide. The proof of the bound does not depend on a table lookup. Classical shadow-system or unconditional volume-product literature could contain an unrecognized equivalent form, so exhaustive historical-priority verification and independent validation remain outstanding. The script's finite checks are not a proof.

## References
1. J. Kim, *Minimal volume product near Hanner polytopes*, arXiv:1212.2544v1, first public posting 2012-12-11; https://arxiv.org/abs/1212.2544.
2. *Exact Mahler products for cube–cross-polytope intersections and their three-dimensional phase diagram*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mahler-products-for-cube-cross-polytope-intersections-and--afc1f44d4eb2.
3. *Exponential Mahler growth along the cube–cross-polytope Minkowski interpolation*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exponential-mahler-growth-along-the-cube-cross-polytope-minkowsk--237a7d354626.
