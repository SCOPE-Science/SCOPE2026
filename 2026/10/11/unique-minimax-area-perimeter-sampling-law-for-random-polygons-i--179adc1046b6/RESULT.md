# Unique minimax area–perimeter sampling law for random polygons in ellipses

## Finding

Let \(K_{a,b}\) be the ellipse parametrized by \(x(\theta)=(a\cos\theta,b\sin\theta)\), where \(a\ge b>0\). Sample \(N\) independent boundary points using a strictly positive continuous arclength density, and take their convex hull. Compare the leading \(N^{-2}\) expected deficits in area and perimeter **after separately dividing each leading coefficient by its own minimum over sampling densities**.

Write \(\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f(\theta)\,d\theta\), and define
\[
E(\theta)=a^2\sin^2\theta+b^2\cos^2\theta,\qquad
C=\langle E^{-1/2}\rangle,\qquad
W(\theta)=\frac{E(\theta)^{-3/2}}{C^3}.
\]
For a boundary density \(\rho\) with respect to arclength, set \(q(\theta)=2\pi\rho(x(\theta))\sqrt{E(\theta)}\). Then \(q>0\) and \(\langle q\rangle=1\), and the two normalized leading coefficients are exactly
\[
R_A(q)=\langle q^{-2}\rangle,\qquad R_P(q)=\langle Wq^{-2}\rangle.
\]
Their separate minima both equal \(1\), attained uniquely at \(q_A=1\) and \(q_P=W^{1/3}\), respectively. Define the balanced minimax price
\[
\mathcal M(a,b)=\min_{q>0,\,\langle q\rangle=1}\max\{R_A(q),R_P(q)\},
\]
where the minimum ranges over strictly positive continuous periodic densities.

**Theorem.** If \(a>b\), put
\[
H(\lambda)=\left\langle[\lambda+(1-\lambda)W]^{1/3}\right\rangle
\quad(0\le\lambda\le1).
\]
There exists exactly one \(\lambda_*\in(0,1)\) satisfying
\[
\left\langle (1-W)[\lambda_*+(1-\lambda_*)W]^{-2/3}\right\rangle=0.
\]
The **unique** balanced minimax density and the **exact** minimax value are
\[
\boxed{q_*(\theta)=\frac{[\lambda_*+(1-\lambda_*)W(\theta)]^{1/3}}{H(\lambda_*)}},
\qquad
\boxed{\mathcal M(a,b)=H(\lambda_*)^3>1}.
\]
Moreover \(R_A(q_*)=R_P(q_*)=\mathcal M(a,b)\). If \(a=b\), the unique optimum is the uniform angular density \(q_*=1\), with \(\mathcal M(a,a)=1\).

For the dimensionless ellipticity \(\varepsilon=(a-b)/(a+b)\), the sharp near-circle expansion is
\[
\boxed{\mathcal M(a,b)=1+\tfrac38\varepsilon^2+O(\varepsilon^3)},
\qquad
\lambda_* =\tfrac12+O(\varepsilon),\quad
q_*(\theta)=1+\tfrac12\varepsilon\cos(2\theta)+O(\varepsilon^2).
\]
Here the last error is uniform in \(\theta\). These assertions concern the leading asymptotic random-polytope coefficients, not optimal expected deficits for any fixed finite \(N\).

## Assumptions and scope

The ellipse is nondegenerate and the admissible sampling densities are continuous and strictly positive, normalized with respect to Euclidean arclength. The expected intrinsic-volume asymptotics used below hold for each *fixed* admissible density as \(N\to\infty\). The all-eccentricity minimax formula is an exact one-dimensional integral/root characterization, not an elementary closed form for \(\lambda_*\). The notion of perimeter is Euclidean perimeter; intrinsic volume \(V_1\) differs from it by a dimension-dependent constant that disappears after normalization.

## Proof

**Reduction from geometric asymptotics.** In the planar case of the random-polytope intrinsic-volume formula, the leading unnormalized area and perimeter coefficient functionals, apart from positive density-independent constants, are
\[
I_A(\rho)=\int_{\partial K}\kappa\rho^{-2}\,ds,\qquad
I_P(\rho)=\int_{\partial K}\kappa^2\rho^{-2}\,ds.
\]
For an ellipse \(ds=\sqrt E\,d\theta\) and \(\kappa=abE^{-3/2}\). Substituting \(\rho=q/(2\pi\sqrt E)\) gives, with no unrecorded angular normalization factors,
\[
I_A=(2\pi)^3ab\,\langle q^{-2}\rangle,
\qquad
I_P=(2\pi)^3(ab)^2\,\langle E^{-3/2}q^{-2}\rangle.
\]
For every positive integrable weight \(F\), Hölder's inequality and \(\langle q\rangle=1\) give
\[
\langle Fq^{-2}\rangle\ge\langle F^{1/3}\rangle^3,
\]
with equality exactly when \(q=F^{1/3}/\langle F^{1/3}\rangle\), almost everywhere (hence everywhere for continuous densities). Thus the first minimum is \(1\), and the second is \(C^3\). Dividing each coefficient by its own optimum gives precisely \(R_A,R_P\) stated above, since \(\langle W^{1/3}\rangle=1\).

**Dual scalar minimax solution.** For \(0\le\lambda\le1\), set \(F_\lambda=\lambda+(1-\lambda)W\). For any admissible \(q\),
\[
\max\{R_A(q),R_P(q)\}\ge\lambda R_A(q)+(1-\lambda)R_P(q)
=\langle F_\lambda q^{-2}\rangle\ge H(\lambda)^3.
\]
If \(a>b\), \(W\) is continuous, positive, and nonconstant. The second derivative exists and satisfies
\[
H''(\lambda)=-\frac29\left\langle(1-W)^2F_\lambda^{-5/3}\right\rangle<0
\quad(0\le\lambda\le1).
\]
Since \(H(0)=\langle W^{1/3}\rangle=1=H(1)\), strict concavity forces a unique interior maximum \(\lambda_*\), with \(H(\lambda_*)>1\) and \(H'(\lambda_*)=0\). Differentiation yields the displayed scalar root equation. Define \(q_*=F_{\lambda_*}^{1/3}/H(\lambda_*)\). It has mean one; direct substitution gives
\[
R_A(q_*)-R_P(q_*)
=H(\lambda_*)^2\langle(1-W)F_{\lambda_*}^{-2/3}\rangle=0.
\]
Consequently their common value equals the weighted average \(\langle F_{\lambda_*}q_*^{-2}\rangle=H(\lambda_*)^3\), attaining the universal lower bound. Any other minimizer must saturate Hölder for the same fixed interior \(\lambda_*\), forcing \(q=q_*\). When \(a=b\), \(W\equiv1\) and Hölder gives the unique optimizer \(q=1\).

**Small-eccentricity coefficient.** By similarity invariance, put \(a=1+\varepsilon\), \(b=1-\varepsilon\), and \(c=\cos(2\theta)\). Then
\[
E=1-2\varepsilon c+\varepsilon^2,\quad
C=1+\frac14\varepsilon^2+O(\varepsilon^3),\quad
W=1+3\varepsilon c+\varepsilon^2\left(\frac{15}{2}c^2-\frac94\right)+O(\varepsilon^3).
\]
Here \(\langle c\rangle=0\), \(\langle c^2\rangle=1/2\); all expansions hold uniformly in the angle and uniformly in \(\lambda\in[0,1]\). Taylor expansion yields
\[
H(\lambda)=1+\frac12\lambda(1-\lambda)\varepsilon^2+O(\varepsilon^3),\qquad
H'(\lambda)=\frac12(1-2\lambda)\varepsilon^2+O(\varepsilon^3).
\]
The unique maximizer therefore satisfies \(\lambda_*=1/2+O(\varepsilon)\). Cubing its maximal value proves \(\mathcal M=1+3\varepsilon^2/8+O(\varepsilon^3)\); substituting \(\lambda_*\) into \(q_*\) gives the stated uniform first-order angular sampling density.

## Verification

The standalone `verify_ellipse_minimax.py` uses only the Python standard library and midpoint quadrature on 32,768 angles, combined with bisection for the scalar root. It checks the endpoint normalization, interior root sign, exact balance of the two normalized objectives at the proposed density, and numerical convergence to the coefficient \(3/8\), over ten ellipticities from zero through \(0.95\). Run `python verify_ellipse_minimax.py`; the expected final marker is `ELLIPSE_MINIMAX_STANDARD_LIBRARY_CHECKS_OK`. This finite numerical check corroborates, but does not replace, the continuous-parameter Hölder proof and uniform Taylor argument.

## Relationship to prior work

Hoehner's *One polytope fits all* (arXiv:2602.18547v1, 2026), Section 3.1, states the separate asymptotic functionals and their individual optimal densities, and Section 3.2 proves that simultaneous individual optimality forces a Euclidean ball. Böröczky–Fodor–Hug (arXiv:1103.4978) develops the underlying intrinsic-volume boundary-sampling asymptotics. Besau–Hoehner–Kur (arXiv:1905.08862) analyzes simultaneous approximations mainly for Euclidean balls. The new statement concerns the **minimum possible worst relative asymptotic loss** on each ellipse, identifying a unique compromise sampler and the exact \(3/8\) near-circle cost. Mere mismatch between individually optimal curvature laws does not determine this minimax value or its optimizer.

## Limitations

This theorem neither supplies optimal finite-\(N\) samplers nor asserts a uniform-in-density \(N^{-2}\) remainder or an all-convex-body minimax theorem. The numerical verifier does not certify inequalities for an uncountable family of ellipses. The literature comparison cannot rule out equivalent results in unindexed or uninspected sources; no independent scientific audit has been performed.

## References

1. S. Hoehner, *One polytope fits all: Characterization of the Euclidean ball via simultaneous intrinsic volume approximation*, arXiv:2602.18547v1 (first submitted 20 February 2026), Sections 3.1–3.2; https://arxiv.org/html/2602.18547v1.
2. K. J. Böröczky, F. Fodor, and D. Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body*, arXiv:1103.4978 (2011); https://arxiv.org/abs/1103.4978.
3. F. Besau, S. Hoehner, and G. Kur, *Intrinsic and Dual Volume Deviations of Convex Bodies and Polytopes*, arXiv:1905.08862 (2019); https://arxiv.org/html/1905.08862v2.
