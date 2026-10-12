# Exact perimeter–area second moments of a random cyclic quadrilateral

## Finding

Choose four independent uniform points on the unit circle in the Euclidean plane and join them in counterclockwise order. Denote the perimeter by \(P\) and unsigned enclosed area by \(A\). Then the **complete bivariate first- and second-moment matrix** is

\[
\begin{aligned}
\mathbb E P&=\frac{24(\pi^2-4)}{\pi^3}, &\mathbb E A&=\frac3\pi,\\
\mathbb E P^2&=8+\frac{132}{\pi^2}, &\mathbb E A^2&=\frac12+\frac{105}{16\pi^2},\\
\mathbb E(PA)&=\frac{140}{3\pi^2}.
\end{aligned}
\]

In particular,

\[
\boxed{\operatorname{Cov}(P,A)=\frac{4(216-19\pi^2)}{3\pi^4}>0.}
\]

Moreover,

\[
\begin{aligned}
\operatorname{Var}(P)&=8-\frac{444}{\pi^2}+\frac{4608}{\pi^4}-\frac{9216}{\pi^6},\\
\operatorname{Var}(A)&=\frac{8\pi^2-39}{16\pi^2}.
\end{aligned}
\]

Thus \(\operatorname{Cov}(P,A)\approx0.3897995704\) and \(\operatorname{Corr}(P,A)\approx0.9051688467\). The displayed second area moment supplies an unconditional derivation of the value previously obtained from a conjectured angle-density formula in [1].

## Assumptions and scope

The four points are independent, each has uniform angular distribution, the circumradius is exactly one, and all random quantities are defined from the resulting convex hull. Coincident points have probability zero. The claim pertains only to four vertices and to raw area (not the area deficit relative to the disk); the asserted correlation and covariance are exact population parameters, not numerical estimates. For radius \(R>0\), covariance scales as \(R^3\), because perimeter scales as \(R\) and area as \(R^2\).

## Proof

Choose one of the four sampled vertices as angular origin. Conditional on its angle, the other three relative angles are independent uniform variables on \([0,2\pi)\). Let \(D_1,D_2,D_3,D_4\) be the four consecutive counterclockwise gaps in units of one revolution. Ordering the other three relative angles shows directly that

\[
(D_1,D_2,D_3,D_4)\sim\operatorname{Dirichlet}(1,1,1,1).
\]

This cyclic anchoring avoids using the nonexchangeable endpoint gap that occurs when ordering four angles on a fixed absolute interval. The polygon invariants are unchanged by the anchoring. Each gap has density \(3(1-x)^2\) for \(0<x<1\); any two distinct gaps have density \(6(1-x-y)\) on the open triangle \(x>0,y>0,x+y<1\).

The chord formula and the oriented shoelace formula give, with \(f(x)=\sin(\pi x)\) and \(g(x)=\sin(2\pi x)\),

\[
P=2\sum_{i=1}^4f(D_i),\qquad A=\frac12\sum_{i=1}^4g(D_i).
\]

The shoelace sum is the *positive* polygon area, including configurations with a gap exceeding a semicircle. The expression is the sum of signed cross-products of successive unit vectors; the entire convex polygon's counterclockwise orientation makes it nonnegative.

Write \(\langle h\rangle=3\int_0^1(1-x)^2h(x)\,dx\) and

\[
\langle h,k\rangle=6\int_0^1\int_0^{1-x}(1-x-y)h(x)k(y)\,dy\,dx.
\]

Elementary integrations, with boundary terms at \(0\) and \(1\), yield the following exhaustive table of terms required for the five moments:

\[
\begin{array}{c|c}
\text{integrand or pair}&\text{expected value}\\ \hline
f&3/\pi-12/\pi^3\\
g&3/(2\pi)\\
f^2&1/2-3/(4\pi^2)\\
g^2&1/2-3/(16\pi^2)\\
fg&8/(3\pi^2)\\
f(D_1)f(D_2)&3/\pi^2\\
g(D_1)g(D_2)&9/(4\pi^2)\\
f(D_1)g(D_2)&3/\pi^2
\end{array}
\]

The pair rows hold for any distinct gap indices by exchangeability. Expanding the two sums and separating diagonal from off-diagonal terms gives

\[
\begin{aligned}
\mathbb EP&=8\langle f\rangle,& \mathbb EA&=2\langle g\rangle,\\
\mathbb EP^2&=16\langle f^2\rangle+48\langle f,f\rangle,&
\mathbb EA^2&=\langle g^2\rangle+3\langle g,g\rangle,\\
\mathbb E(PA)&=4\langle fg\rangle+12\langle f,g\rangle.
\end{aligned}
\]

Substitution proves all five formulas. Subtracting products of means yields the stated covariance matrix. Strict positivity follows from \(\pi^2<10\): indeed \(216-19\pi^2>26>0\). Positive marginal variances follow either from the explicit formulas or from the fact that the two geometric functionals vary over open subsets of the three-dimensional gap simplex. No asymptotic or unproved geometric density formula is needed.

## Verification

Run `python verify_quadrilateral.py` using Python 3 and SymPy. The program evaluates the one-gap and two-gap integrals independently, checks sixteen claimed symbolic identities by simplification, and compares direct Cartesian shoelace/perimeter computations with the gap identities for 150,000 seeded independent point sets. That Monte Carlo comparison is a numerical diagnostic only; it is neither used to prove the formulas nor a finite certificate of originality. In the recorded execution, all symbolic identities and Cartesian consistency checks passed; the simulated covariance was approximately \(0.388434453\) against the exact \(0.389799570\).

## Relationship to prior work

Finch [1], a 2016 primary-MSC 60D05 analysis of random cyclic quadrilaterals, explicitly leaves joint perimeter/area analysis unresolved and reports \(\mathbb E A^2=1/2+105/(16\pi^2)\) under a conjectured three-angle density (section 5). Our gap-based derivation proves this numerical identity without that conjecture and additionally evaluates the previously unreported mixed moment \(\mathbb E(PA)\), thereby closing the fixed-four bivariate second-moment question. It does **not** resolve the joint distribution or any density of area. Wang, Li, and Xu [2] develop the general symmetric-Dirichlet polygon representation and the large-vertex asymptotic theory of perimeter, area and related extrapolations; our claim is a finite-four exact evaluation rather than an extension of their asymptotic results. General Dirichlet integral identities are classical ingredients and not themselves novel. The possibility of a previously implicit equivalent evaluation in broader random-polygon moment literature remains a priority limitation.

## Limitations

No formula for the complete joint density of \((P,A)\) is asserted. The exact formulas do not cover general nonuniform angular samples, random circumradii, or higher-sided polygons. The mathematical derivation is elementary after a correct cyclic Dirichlet representation; the asserted contribution is the explicitly evaluated natural bivariate second-moment matrix and the unconditional confirmation of the previously conjecture-dependent area moment. No independent review or comprehensive historical priority certification is claimed.

## References

[1] S. R. Finch, *Random Cyclic Quadrilaterals*, arXiv:1610.00510 (first publicly submitted 3 October 2016), especially introductory discussion and section 5. https://arxiv.org/abs/1610.00510

[2] S. Wang, Z. Li, W.-Q. Xu, *Nonlinear Random Extrapolation Estimates of π Under Dirichlet Distributions*, Journal of Numerical Analysis and Approximation Theory 52 (2023), 273–294, doi:10.33993/jnaat522-1360, sections 2–3 and Appendix. https://doi.org/10.33993/jnaat522-1360

[3] N. Koroleva and Y. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (2013). This concerns maxima among polygonal subsamples, not the four-point mixed moment. https://arxiv.org/abs/1301.1360
