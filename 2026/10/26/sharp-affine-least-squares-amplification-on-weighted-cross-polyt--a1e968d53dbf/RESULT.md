# Sharp affine least-squares amplification on weighted cross-polytopes

## Finding
Let \(d\ge1\), \(\alpha>-1\), and let the positive axis lengths \(a_1,\ldots,a_d\) be arbitrary. On the stretched cross-polytope
\[
B_a=\left\{x\in\mathbb R^d:\sum_{i=1}^d\frac{|x_i|}{a_i}\le1\right\},
\]
put the probability measure \(d\mu_\alpha(x)=Z^{-1}(1-\sum_i |x_i|/a_i)^\alpha\,dx\). Denote by \(P\) the \(L^2(\mu_\alpha)\)-orthogonal projection onto all affine functions and let \(m=d+\alpha>0\). Its sharp induced norms are
\[
\boxed{\|P\|_{L^\infty\to L^\infty}=\|P\|_{L^1\to L^1}=1+\frac{m(m+3)}{2(m+1)}\left(\frac{m(m+3)}{(m+1)(m+2)}\right)^m.}
\]
The continuous Lebesgue function \(\Lambda(x)=\int_{B_a}|K(x,y)|\,d\mu_\alpha(y)\) is maximized *exactly* at the \(2d\) vertices \(\pm a_i e_i\); the formula is independent of the axis lengths. For each vertex \(v\), the sign input \(f_v(y)=\operatorname{sgn} K(v,y)\) realizes the \(L^\infty\) operator norm. The optimal downward excursion for nonnegative inputs \(0\le f\le1\) is \(-(\|P\|_\infty-1)/2\), attained at each vertex by the indicator of \(\{K(v,\cdot)<0\}\).

The norm is strictly increasing in the real effective dimension \(m\). Moreover,
\[
\|P\|=\frac m2+1+\frac1m+O(m^{-2}),\qquad m\longrightarrow\infty.
\]
For fixed \(d\) and axis lengths, the measures \(\mu_\alpha\) converge weakly to the point mass at the origin as \(\alpha\to\infty\), yet these sharp norms diverge linearly. Some unweighted examples are \(\frac53\) for \(d=1\), \(\frac{233}{108}\) for \(d=2\), and \(\frac{10561}{4000}\) for \(d=3\).

## Assumptions and scope
All dimensions are integers \(d\ge1\), all \(\alpha>-1\) are real, and all axes are strictly positive. Boundary points have zero \(\mu_\alpha\)-measure, but the projected output has a continuous affine representative. Thus the maximum of its continuous Lebesgue function on the closed polytope equals its essential supremum on \(B_a\). Both operator norms refer to the same probability measure; the \(L^1\) equality is an operator-norm identity, not a claim of an attained \(L^1\) extremizer.

The result concerns a local weighted least-squares polynomial projector, not nearest-point projection of vectors onto the convex body, and not interpolation or globally coupled finite-element projections.

## Proof
Scale \(x_i=a_i u_i\). For \(U=Y/a\), independent symmetric coordinate signs and the nonnegative absolute values together with the slack \(1-\sum_i|U_i|\) have the Dirichlet density with parameters \((1,\ldots,1,\alpha+1)\). In particular each \(|U_i|\) has beta density
\[
p_m(t)=m(1-t)^{m-1},\qquad 0<t<1,
\]
and its moments are \(\mathbb E|U_i|=1/(m+1)\), \(\mathbb E U_i^2=2/((m+1)(m+2))\). Symmetry gives \(\mathbb E U_i=0\) and \(\mathbb E U_iU_j=0\) for distinct coordinates. Put \(c=(m+1)(m+2)/2>1\). The affine Gram matrix and its inverse therefore yield the exact reproducing kernel
\[
K(x,y)=1+c\sum_{i=1}^d\frac{x_i y_i}{a_i^2},\qquad (Pf)(x)=\int K(x,y)f(y)\,d\mu_\alpha(y).
\]
It is symmetric, has unit mass in either variable, and reproduces all affine functions. In particular,
\[
\|P\|_{L^\infty\to L^\infty}=\max_{x\in B_a}\Lambda(x),\quad \Lambda(x)=\mathbb E|K(x,Y)|.
\]
Since \(K(x,Y)\) is affine in \(x\), \(\Lambda\) is convex. Every point is a convex combination of the vertices, hence some vertex maximizes \(\Lambda\). Coordinate sign changes and permutations after normalizing by the \(a_i\) make all vertex values equal. More strongly, any two distinct vertices \(v,w\) give kernels having strictly opposite signs on a set of positive measure: near the vertex \(-v\), \(K(v,\cdot)<0\), whereas \(K(w,\cdot)>0\) for \(w\ne-v\); for \(w=-v\), choose points close to \(-v\) again. Because \(c>1\), these inequalities persist on an interior neighborhood. Therefore strict convexity of absolute value *at such sign-crossings* makes \(\Lambda(x)\) strictly below the common vertex value whenever \(x\) is a nontrivial convex combination of distinct vertices. Exactly the vertices maximize.

At \(x=v=a_1e_1\), the kernel is \(1+cU_1\). Writing \(U_1=ST\) with \(S\in\{-1,1\}\) symmetric and \(T\) beta-distributed, one gets
\[
\begin{aligned}
\Lambda(v)&=\mathbb E\frac{|1+cT|+|1-cT|}{2}
=1+\mathbb E(cT-1)_+\\
&=1+m\int_{1/c}^1(ct-1)(1-t)^{m-1}\,dt\\
&=1+\frac{c-1}{m+1}\left(1-\frac1c\right)^m.
\end{aligned}
\]
Since \(c-1=m(m+3)/2\) and \(1-1/c=m(m+3)/((m+1)(m+2))\), this is the claimed formula. The bounded sign input \(f_v=\operatorname{sgn}K(v,\cdot)\) attains \((Pf_v)(v)=\Lambda(v)\), and continuity of the affine output makes the same value its essential supremum. Symmetry \(K(x,y)=K(y,x)\) and \(L^1\)-\(L^\infty\) duality give the identical \(L^1\)-operator norm.

As \(\int K(v,y)\,d\mu_\alpha=1\), its negative mass is \((\Lambda(v)-1)/2\). Choosing the indicator of the negative-kernel region gives the sharp downward excursion. The convexity argument rules out greater negativity at any other output point.

For strict monotonicity set \(b(m)=m(m+3)/((m+1)(m+2))\) and \(F(m)=\Lambda(v)-1=m(m+3)b(m)^m/[2(m+1)]\). For every \(m>0\), \(b\in(0,1)\). The elementary inequality \(\log(1-z)>-z/(1-z)\), applied to \(z=2/((m+1)(m+2))\), gives \(\log b>-2/[m(m+3)]\). Differentiating the explicit formula and substituting that bound yields
\[
\frac{d}{dm}\log F(m)>
\frac{m^2+5m+2}{m(m+2)(m+3)}>0.
\]
The large-\(m\) expansion \(b(m)^m=1-2/m+8/m^2+O(m^{-3})\) together with the rational prefactor gives \(F(m)=m/2+1/m+O(m^{-2})\). Finally \(\mathbb E|Y_i|/a_i=1/(m+1)\), so for fixed \(d\), \(\mathbb E\sum_i|Y_i|/a_i=d/(m+1)\to0\) as \(\alpha\to\infty\), proving weak concentration at the origin; the norm expansion simultaneously proves divergence.

## Verification
The accompanying `verify.py` performs exact rational beta-polynomial quadratures for every integer effective dimension \(1\le m\le32\), independently checks the first five beta moments in each such dimension, simplifies the logarithmic-derivative lower bound symbolically, evaluates seven noninteger parameter instances at 65-digit precision using an endpoint-regularized integral, and checks the large-parameter remainder in four instances. It returns `PASS 204 exact/symbolic/high-precision checks`. Those finite computations are verification aids; the formulas for all real \(m>0\), the unique maximizing vertices, and strict monotonicity are proved above analytically.

## Relationship to prior work
Aktas and Xu study Jacobi weights and orthogonal polynomials on a simplex, including weights containing a slack-coordinate power. Their framework accounts for the Dirichlet beta marginals on each signed orthant, but does not supply the maximum-coordinate operator norm of the affine projector on the signed union of orthants. Foucart studies the maximum norms of one-dimensional spline projectors with multiple knots; that is a different approximation subspace and support geometry. De Boor's bounds on spline least squares provide historical stability motivation.

A previously published simplex-projection calculation obtains a sharp affine norm on a *single* simplex by convexity of the reproducing-kernel row. In contrast, the present result is for a centrally symmetric cross-polytope with a free radial Jacobi weight; the Gram covariance, vertex kernel, beta sign mixture, exact formula, and concentration parameter are different. Known metric projections onto cross-polytopes concern the closest point in a convex set, not a weighted function-space orthogonal projector. These distinctions prevent the cited results from implying the stated formula without the separate derivation above.

## Limitations
The calculation relies on signed-coordinate symmetry and the Dirichlet slack weight. It does not establish sharp norms for general anisotropic nonradial densities, higher-degree polynomial projections, or other polytopes. Its linear large-\(\alpha\) behavior concerns a family of changing measures: it makes no statement about boundedness of projectors in one fixed measure space. Literature priority remains provisional because an equivalent formula might appear under different approximation-theoretic terminology; no independent external audit of the derivation or the bibliographic comparison has been performed.

## References
1. Rabia Aktas and Yuan Xu, *Sobolev orthogonal polynomials on a simplex*, arXiv:1111.2994v1, public 13 November 2011, https://arxiv.org/abs/1111.2994.
2. Simon Foucart, *On the Value of the Max-Norm of the Orthogonal Projector onto Splines with Multiple Knots*, Journal of Approximation Theory 140 (2006), 154–177, DOI 10.1016/j.jat.2005.12.004; accessible preprint https://foucart.github.io/publi/SplineProj2.pdf.
3. Carl de Boor, *A Bound on the L-Infinity-Norm of L2-Approximation by Splines in Terms of a Global Mesh Ratio*, Mathematics of Computation 30 (1976), 765–771, DOI 10.1090/S0025-5718-1976-0425432-1.
4. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34 (mathematically distinct domain).
