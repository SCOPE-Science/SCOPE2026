# Exact fourth-power point-evaluation constant for quadratic circle polynomials

## Finding
Let \(dm\) be normalized arc measure on \(\mathbb T\). The exact norm of point evaluation on \(\operatorname{span}\{1,t,t^2\}\subset L^4(\mathbb T)\), maximized also over the evaluation point, is
\[
\|P\|_\infty^4\le C_{2,4}\int_\mathbb T|P(t)|^4\,dm(t),\qquad C_{2,4}=\frac1{Q(\rho)}=4.3856726428319838539\ldots,
\]
where \(Q(x)=70x^4-80x^3+36x^2-8x+1\), and \(\rho=0.37343884190325123748\ldots\) is the **unique real root** of \(35x^3-30x^2+9x-1=0\). All nonzero equality cases are \(P(t)=\lambda[\rho+(1-2\rho)\xi t+\rho\xi^2t^2]\), where \(\lambda\ne0\), \(|\xi|=1\).

Equivalently, for each homogeneous quadratic \(F(z,w)=a z^2+b zw+c w^2\), Rudin's diagonal map \(DF(u)=F(u,u)\) satisfies the **sharp** restricted norm inequality
\[
\|DF\|_{A^4(\mathbb D)}\le\kappa\|F\|_{H^4(\mathbb D^2)},\qquad\kappa=\bigl(5Q(\rho)\bigr)^{-1/4}=0.967757513648982739\ldots.
\]
In particular the whole homogeneous quadratic subspace has a uniform strict contraction gap, in contrast with the general norm-one estimate.

## Assumptions and scope
Polynomials have complex coefficients and degree at most two. The \(L^4\) norm uses probability Haar measure on the unit circle; \(H^4\) uses product probability Haar measure on the torus, and \(A^4\) normalized planar area measure. The exact coefficient result is for this three-dimensional space only, not for all degrees or other exponents.

## Proof
Fix any \(P\) and a point of maximum modulus \(\tau\in\mathbb T\). The polynomial \(P(\tau t)/P(\tau)\) has value \(1\) at \(t=1\), so the sharp fourth-power point-evaluation constant is the inverse of
\[
\min_{a+b+c=1}\int_\mathbb T|a+bt+ct^2|^4\,dm(t).
\]
The convolution of the coefficient vector \((a,b,c)\) with itself is \((a^2,2ab,b^2+2ac,2bc,c^2)\). Parseval applied to \(P^2\) gives the exact identity
\[
\int_\mathbb T|P(t)|^4\,dm(t)=|a|^4+4|ab|^2+|b^2+2ac|^2+4|bc|^2+|c|^4.
\]
This is a strictly convex coercive function of the coefficient vector: the map \(P\mapsto\|P\|_4^4\) is strictly convex since \(u\mapsto|u|^4\) is strictly convex on \(\mathbb C\), and distinct polynomials differ away from a null set. Hence on \(a+b+c=1\) there is one and only one minimizer.

Reversing coefficients \((a,b,c)\mapsto(c,b,a)\) preserves the affine constraint and the \(L^4\) norm, by substituting \(t\mapsto\bar t\). Conjugating all coefficients also preserves both. Uniqueness forces \(a=c=x\in\mathbb R\) and \(b=1-2x\in\mathbb R\). Therefore the minimized integral equals the minimum over \(x\in\mathbb R\) of
\[
Q(x)=2x^4+8x^2(1-2x)^2+\bigl((1-2x)^2+2x^2\bigr)^2
=70x^4-80x^3+36x^2-8x+1.
\]
Here \(Q'(x)=8(35x^3-30x^2+9x-1)\), and \(Q''(x)=840(x-2/7)^2+24/7>0\) for every real \(x\). Thus the cubic has exactly one real zero \(\rho\), the unique global minimizer. Undoing the evaluation-point rotation and scalar normalization gives exactly the listed extremizers.

The strict gap from the universal fourth-power bound \(5\) also has a rational certificate. Strong convexity with lower Hessian \(24/7\), evaluated at \(x=3/8\), yields
\[
Q(\rho)\ge Q(3/8)-\frac{Q'(3/8)^2}{2(24/7)}
=\frac{44825}{196608}>\frac15.
\]
Finally, for \(F(z,w)=a z^2+bzw+c w^2\), the torus modulus agrees with \(|a+bt+ct^2|\) up to rotation, while \(DF(u)=(a+b+c)u^2\) and \(\int_{\mathbb D}|u|^8dA(u)=1/5\). Hence \(\|DF\|_{A^4}^4/\|F\|_{H^4}^4\le C_{2,4}/5=1/(5Q(\rho))\), with equality from the coefficient extremizer.

## Verification
The standalone `checker.py` recomputes the fourth-moment polynomial by exact rational convolution for eight rational test inputs; checks strict root enclosure \(373438841903251/10^{15}<\rho<373438841903252/10^{15}\); checks \(Q''\)'s global lower bound and the exact rational contraction certificate. The universal proof uses strict convexity and algebra, not a finite numerical enumeration. The checker returned PASS. These computations independently support algebra and numerical bounds but are not substitutes for the analytic strict-convexity proof.

## Relationship to prior work
Instanes, *Point evaluation for polynomials on the circle* (public preprint arXiv:2509.22035v1, September 26, 2025; published 2026), defines the same sharp constant \(\mathscr C_{d,p}\), proves the existence and uniqueness of the normalized minimizer and upper bounds for small degrees, and gives estimates rather than the exact \(d=2,p=4\) algebraic constant and extremizer in the inspected full text (Theorems 1, 14, 16; Sections 2, 5, 7). Brevig, Gómez-Serrano, Ortega-Cerdà, Seip, *Contractivity of Rudin's diagonal restriction operator for \(H^p\) of the polydisc* (arXiv:2610.16227v1, October 12, 2026; Theorem 1.1 and Corollary 4.1), establishes the general norm-one bound and associated polynomial point-evaluation inequality, but does not compute this exact restricted norm. The earlier global inequality yields only \(C_{2,4}\le5\); the new exact constant is strictly smaller.

## Limitations
No formula is claimed for arbitrary polynomial degree or for non-even exponents. General strict contractivity at \(p=4\) does not imply the numerical constant proved here. Priority beyond the inspected primary literature and indexed comparisons is not independently certified; unindexed classical trigonometric extremal results may overlap. No independent external audit has been performed.

## References
1. S. M. Instanes, *Point evaluation for polynomials on the circle*, arXiv:2509.22035v1 (2025); Collectanea Mathematica (2026), DOI: 10.1007/s13348-026-00516-z.
2. O. F. Brevig, J. Gómez-Serrano, J. Ortega-Cerdà, K. Seip, *Contractivity of Rudin's diagonal restriction operator for \(H^p\) of the polydisc*, arXiv:2610.16227v1 (2026).
