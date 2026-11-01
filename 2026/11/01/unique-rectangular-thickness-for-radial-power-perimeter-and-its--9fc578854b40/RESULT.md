# Unique rectangular thickness for radial power perimeter and its essential-singularity law

## Finding

For \(a>0\), \(b>0\), and \(p\in\mathbb R\), let \(R_{a,b}=[-a,a]\times[-b,b]\), and let
\[F_p(a,b)=\int_{\partial R_{a,b}}\lVert x\rVert_2^p\,d\mathcal H^1(x).\]
For every \(p\geq0\), the function \(b\mapsto F_p(a,b)\) is strictly increasing. For every \(p<0\), it is strictly decreasing up to exactly one global minimizer \(b_*(a,p)\), and strictly increasing thereafter.

Put \(q=-p>0\). The minimizer is \(b_*(a,-q)=a/t_q\), where \(t_q\) is the **unique positive solution** of
\[q\int_0^{t_q}\left(\frac{1+t_q^2}{1+u^2}\right)^{q/2}\frac{du}{1+u^2}=1.\]
The normalized optimal thickness \(b_*(a,-q)/a\) increases strictly with \(q>0\), crosses one precisely at \(q=1\), and obeys both sharp endpoint laws
\[\lim_{q\downarrow0}\frac{(b_*(a,-q)/a)^q}{q}=\frac\pi2,\qquad
\lim_{q\to\infty}\frac{b_*(a,-q)}{aq}=1.\]
In particular, \(q\log(a/b_*)+\log q\to\log(2/\pi)\) as \(q\downarrow0\): the optimal thickness collapses essentially singularly, much faster than every power of \(q\). At \(p=-1\), the unique optimum is exactly the square \(b=a\).

## Assumptions and scope

The body is a nondegenerate centered axis-aligned rectangle of fixed horizontal half-width \(a>0\), and the variable is its vertical half-width \(b>0\). The radial weight is \(\lVert x\rVert_2^p\). The boundary stays a positive distance from the origin for every such rectangle, so the integral is finite for all real exponents, including exponents outside the integrability range used for limits to degenerate convex bodies in the motivating literature. There is no area or ordinary-perimeter constraint. Rotation of the entire family about the origin leaves all statements unchanged.

## Proof

**Exact boundary reduction.** Pair the four sides to obtain
\[\frac14F_p(a,b)=\int_0^a(x^2+b^2)^{p/2}\,dx+
\int_0^b(a^2+y^2)^{p/2}\,dy.\]
This is differentiable in \(b>0\) for every real exponent. For \(p\ge0\), its derivative is
\[\frac14\partial_b F_p(a,b)=p b\int_0^a(x^2+b^2)^{(p-2)/2}\,dx+(a^2+b^2)^{p/2}>0,\]
including \(p=0\), for which the first term is zero.

**Negative-exponent shape derivative.** Fix \(q=-p>0\) and set \(t=a/b\). Differentiation, followed by \(x=bu\), gives
\[\frac14\partial_bF_{-q}(a,b)=b^{-q}\left[(1+t^2)^{-q/2}-q\int_0^t(1+u^2)^{-1-q/2}\,du\right].\]
Factor the positive first term and define
\[\mathcal R_q(t)=q(1+t^2)^{q/2}\int_0^t(1+u^2)^{-1-q/2}\,du.\]
Thus \(\operatorname{sgn}(\partial_bF_{-q})=\operatorname{sgn}(1-\mathcal R_q(a/b))\). For each fixed \(q>0\), \(\mathcal R_q(t)\) is continuous and strictly increasing in \(t>0\): the prefactor and the integration interval both increase strictly. Moreover \(\mathcal R_q(0)=0\), while \(\mathcal R_q(t)\to\infty\) because the integral tends to a strictly positive finite limit. Consequently there is exactly one root \(t_q>0\) of \(\mathcal R_q(t)=1\). Since \(a/b\) strictly decreases with \(b\), the derivative of \(F_{-q}\) is negative for \(b<a/t_q\) and positive for \(b>a/t_q\), proving the unique global minimum for every \(a>0\) and every negative exponent.

**Monotonic dependence and exact square transition.** For fixed \(t>0\), write
\[\mathcal R_q(t)=q\int_0^t\left(\frac{1+t^2}{1+u^2}\right)^{q/2}\frac{du}{1+u^2}.\]
Its integrand is positive and the bracket is at least one, so \(q\mapsto\mathcal R_q(t)\) is strictly increasing on \((0,\infty)\). Together with strict increase in \(t\), this implies \(q\mapsto t_q\) is strictly decreasing, hence \(q\mapsto b_*(a,-q)/a\) strictly increasing. At \(q=1\), the elementary integral \(\int_0^t(1+u^2)^{-3/2}\,du=t/\sqrt{1+t^2}\) gives \(\mathcal R_1(t)=t\), so \(t_1=1\). The square is therefore optimal exactly at \(p=-1\).

**Singular limit as the exponent approaches zero.** As \(q\downarrow0\), each fixed \(t\) satisfies \(\mathcal R_q(t)\to0\), hence \(t_q\to\infty\). The root equation is
\[(1+t_q^2)^{-q/2}=q\int_0^{t_q}(1+u^2)^{-1-q/2}\,du.\]
The right-hand integral tends to \(\int_0^\infty(1+u^2)^{-1}du=\pi/2\) by dominated convergence: the integrand is bounded by \((1+u^2)^{-1}\), while its upper limit tends to infinity. Dividing by \(q\) and using \(t_q\to\infty\) gives \(t_q^{-q}/q\to\pi/2\). Since \(b_*/a=1/t_q\), the stated exact logarithmic and essential-singularity laws follow. In particular, \(t_q\) exceeds every fixed inverse power of \(q\), so the minimizer thickness is smaller than every fixed power of \(q\).

**Large negative-exponent limit.** For each fixed \(c>0\), substitute \(t=c/q\) and \(u=v/q\) in the definition of \(\mathcal R_q\). Uniform convergence of both factors on \(0\le v\le c\) shows \(\mathcal R_q(c/q)\to c\) as \(q\to\infty\). Since \(\mathcal R_q\) is strictly increasing in \(t\), comparison with any fixed \(c<1\) and \(c>1\) implies \(q t_q\to1\). Therefore \(b_*/(aq)=1/(qt_q)\to1\).

## Verification

The companion standalone program `rectangle_verify.py` evaluates the exact derivative and unique-root equation at ten exponents using arbitrary precision; checks derivative signs and strict local minimality; verifies the \(q=1\) square identity, both asymptotic regimes, and finite-difference derivatives. It passed 50 deterministic assertions on the delivered source code. These finite checks are diagnostics; the preceding integral arguments establish all quantified statements, including the singular limit and global uniqueness.

## Relationship to prior work

Csató and Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies* (arXiv:2610.11677v1, first public October 8, 2026), establish continuity and inclusion monotonicity conditions for radial weighted perimeter, not the complete fixed-width rectangular minimum or essential singularity. Csató, Giovagnoli, and Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces* (arXiv:2608.19851v1, August 20, 2026), study a different fixed-standard-perimeter optimization; their symmetric needle extremal concerns maximization for negative powers, rather than the fixed-side-width minimization considered here. Previous work on thin ellipses proves a negative thin-axis derivative and an interior minimum for some negative exponents, but does not imply a unique rectangular optimizer, strict exponent monotonicity, or the present essential-singularity rate. These distinctions are by hypotheses and logical implications, not by differing terminology.

## Limitations

Only centered rectangles of a **fixed** first half-width are optimized: there is no claim of global optimality over all convex bodies, ellipses, or all rectangles subject to another geometric constraint. The laws for exponents below the usual integrability threshold apply to nondegenerate rectangles only, not to boundary measures of lower-dimensional degenerate limits. Historical priority could be affected by an independently derived formula in older fixed-width weighted-curve literature. Independent verification by another researcher has not been performed.

## References

1. G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1 (2026-10-08), https://arxiv.org/html/2610.11677v1.
2. G. Csató, D. Giovagnoli, and P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1 (2026-08-20), https://arxiv.org/html/2608.19851v1.

