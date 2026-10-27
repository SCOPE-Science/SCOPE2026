# Exact endpoint norm and nonattainment for a two-cell quadratic spline projector

## Finding

Let \(S\subset C[0,1]\) be the five-dimensional space of continuous functions that restrict to polynomials of degree at most two on each of the intervals \([0,1/2]\) and \([1/2,1]\). Let \(P\) be the orthogonal projection in unweighted \(L^2[0,1]\) onto \(S\). Its extension to bounded measurable inputs and its restriction to continuous inputs have the same sharp supremum-norm constant:

\[
\boxed{\|P\|_{L^\infty\to L^\infty}=\|P\|_{C\to C}
=1+\frac{58\sqrt{174}}{625}+\frac{2\sqrt6}{25}=2.420075252350\ldots.}
\]

With \(K\) the real reproducing kernel, the Lebesgue function \(\Lambda(x)=\int_0^1 |K(x,t)|\,dt\) has exactly the two maximizers \(x=0,1\). The norm is attained for bounded measurable inputs, but **not** for any continuous input of unit supremum norm. The result holds equally for real or complex scalar inputs.

## Assumptions and scope

The spline has one fixed midpoint knot and requires only continuity there; its first derivative may jump. The measure is ordinary Lebesgue measure, with no mass weighting. The result makes no assertion about variable knot positions, multiple interior knots, or continuously differentiable quadratic splines.

Define the basis \(b(t)=(1,t,t^2,(t-1/2)_+,(t-1/2)_+^2)^{\mathsf T}\), where \((u)_+=\max(u,0)\). The Gram matrix \(G=\int_0^1 b(t)b(t)^{\mathsf T}\,dt\) is nonsingular, and \(K(x,t)=b(x)^{\mathsf T}G^{-1}b(t)\).

## Proof

**Exact kernel.** Direct integration and rational matrix inversion yield

\[
G^{-1}=\begin{pmatrix}
17&-128&200&-96&-160\\
-128&1280&-2240&1344&1600\\
200&-2240&4160&-2880&-2560\\
-96&1344&-2880&3072&0\\
-160&1600&-2560&0&5120
\end{pmatrix}.
\]

For \(0\le x\le 1/2\), the kernel is a quadratic polynomial in \(t\) on each half-interval:

\[
K(x,t)=\begin{cases}
(4160x^2-2240x+200)t^2+(-2240x^2+1280x-128)t+200x^2-128x+17,&0\le t\le1/2,\\
(1600x^2-640x+40)t^2+(-2560x^2+1024x-64)t+1000x^2-400x+25,&1/2\le t\le1.
\end{cases}
\]

Reflection invariance gives \(K(1-x,1-t)=K(x,t)\). At \(x=0\) the two pieces are \(200t^2-128t+17\) and \(40t^2-64t+25\), respectively; each has two simple roots strictly inside its half-interval. Their discriminants are \(2784\) and \(96\). For a positive-leading-coefficient quadratic \(q\) with discriminant \(\Delta>0\), the negative integral between its roots equals \(\Delta^{3/2}/(6a^2)\), where \(a\) is the leading coefficient. Since \(P1=1\), \(\int_0^1K(0,t)\,dt=1\), so

\[
\Lambda(0)=1+2\left(\frac{2784^{3/2}}{6(200)^2}+\frac{96^{3/2}}{6(40)^2}\right)
=1+\frac{58\sqrt{174}}{625}+\frac{2\sqrt6}{25}.
\]

**Global maximality (finite exact certificate).** The following argument reduces the infinite optimization over \(x\) to finitely many *rational* comparisons. For each \(i=0,\ldots,9\), put \(a=i/20\), \(b=(i+1)/20\), \(m=(a+b)/2\) and
\[
C_{a,b}(t)=2K(m,t)-\frac{K(a,t)+K(b,t)}2.
\]
For \(a\le x\le b\), let \(u=(x-a)/(b-a)\). Quadratic Bernstein interpolation in the variable \(x\) gives the identity
\[
K(x,t)=(1-u)^2K(a,t)+2u(1-u)C_{a,b}(t)+u^2K(b,t).
\]
The coefficients are nonnegative and sum to one. The accompanying `verify_quadratic_spline.py` verifies, by exact rational arithmetic, that the \(L^1(dt)\)-norms of **all 29 control rows other than \(K(0,\cdot)\)** are *strictly below* \(9/4\), whereas \(\Lambda(0)>9/4\). For completeness, the exact integration upper bounds in that checker use a rational uniform subdivision: on a segment of width \(h\), the integral of the absolute value of a quadratic is bounded by the absolute integral of its affine endpoint interpolant plus \(|a_2|h^3/6\). Both terms are rational for rational polynomial coefficients and rational knots. The checker computes the original Gram matrix, verifies its inverse, verifies both kernel polynomials by exact identities, and checks all 29 strict comparisons.

By the triangle inequality and nonnegative Bernstein weights, \(\Lambda(x)\le\Lambda(0)\) on the left half. For every \(0<x\le1/2\), the coefficient of the first endpoint row is strictly less than one, so \(\Lambda(x)<\Lambda(0)\). Reflection gives exactly one other maximizing point, \(x=1\).

**Sharpness and nonattainment.** On measurable bounded inputs, \(f(t)=\operatorname{sgn}K(0,t)\) attains the norm at \(x=0\). The same norm on \(C[0,1]\) follows by smoothing this sign function in arbitrarily short neighborhoods of its four kernel zeros, yielding continuous functions of supremum norm at most one and approaching the endpoint integral. Suppose a continuous \(f\), \(\|f\|_\infty\le1\), attained the sharp norm. Since \(Pf\) is continuous, a maximizing evaluation point exists and must be \(0\) or \(1\). Equality in the integral triangle inequality would then force \(f\) (up to a common constant phase) to coincide almost everywhere with the sign of the corresponding kernel row. That sign changes four times across simple interior roots, so cannot agree almost everywhere with a continuous function. This contradiction establishes nonattainment on \(C[0,1]\).

## Verification

Run `python3 verify_quadratic_spline.py` with standard Python 3; no packages or internet are needed. It checks \(GG^{-1}=I\), the explicit kernel identities, 29 rational strict inequalities, and an exact rational lower bound for the claimed endpoint expression. The calculation is a finite algebraic **proof certificate**, not numerical sampling of a continuous optimization variable: the Bernstein identity covers every evaluation point.

## Relationship to prior work

Shadrin's 2001 de Boor-conjecture theorem supplies knot-independent boundedness for spline orthoprojectors; its multiple-knot corollary includes lower-continuity spline spaces. It does not provide the sharp constant for this specific midpoint, piecewise-quadratic projector. Sections 0.2, 4.1, 4.3, and 4.5 of that paper were compared, including its discussion of bounding constants and selected special cases. Kayumov's 2004 L-spline study discusses mesh-uniform norms and special linear/exponential/trigonometric spline families, rather than this finite quadratic case. Passenbrunner and Shadrin's 2013 paper derives maximal kernel estimates and almost-everywhere convergence on arbitrary meshes, not this exact two-cell value or nonattainment statement.

## Limitations

This result concerns only one midpoint knot and continuity across it. The projectors for arbitrary knots and higher spline dimensions may have different maximizers and constants. The certificate proves the stated finite case and does not assert an optimal universal bound. No independent audit has been performed; equivalently phrased or unindexed prior finite calculations remain possible.

## References

- A. Yu. Shadrin, *The \(L^\infty\)-norm of the \(L^2\)-spline projector is bounded independently of the knot sequence: A proof of de Boor's conjecture*, Acta Mathematica 187 (2001), 59–137, DOI: 10.1007/BF02392832. Open text: https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6612-11511_2006_Article_BF02392832.pdf
- A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, publicly posted 2004-08-30, https://arxiv.org/abs/math/0408418.
- M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824, publicly posted 2013-08-22, https://arxiv.org/abs/1308.4824.
