# Sharp oscillation threshold for exponentially damped geodesic covariance on hyperbolic three-space

## Finding
Let \(\mathbb H^3\) be real hyperbolic three-space of constant sectional curvature \(-1\), with geodesic distance \(r=d(x,y)\). For any \(a>1\) and \(\omega\ge0\), define
\[
K_{a,\omega}(x,y)=e^{-ar}\cos(\omega r).
\]
Then \(K_{a,\omega}\) is positive semidefinite on every finite collection of points of \(\mathbb H^3\) **if and only if**
\[
3\omega^4+2(a^2+1)\omega^2\le (a^2-1)^2.
\]
Equivalently, the sharp oscillation allowance is
\[
0\le\omega^2\le\Omega(a)^2,
\qquad \Omega(a)^2=\frac{2\sqrt{a^4-a^2+1}-(a^2+1)}{3}.
\]
Equality is included. At the threshold the continuous spherical transform vanishes at spectral parameter \(\lambda=0\), and is strictly positive for \(\lambda>0\); beyond it the transform is negative on an interval adjacent to zero.

## Assumptions and scope
The curvature normalization is exactly \(-1\); \(a>1\) and \(\omega\ge0\) are real, with no further restrictions. Positive semidefinite means that for every integer \(m\ge1\), all points \(x_1,\ldots,x_m\in\mathbb H^3\), and all coefficients \(c_1,\ldots,c_m\in\mathbb C\), one has \(\sum_{i,j=1}^m\overline{c_i}c_j K_{a,\omega}(x_i,x_j)\ge0\). Repeated points are permitted. No assertion about other dimensions, other curvature normalizations without rescaling, or \(a\le1\) is made.

## Proof
Fix an origin. Polar integration on \(\mathbb H^3\) uses \(4\pi\sinh^2r\,dr\); the principal-series spherical function is
\[
\varphi_\lambda(r)=\frac{\sin(\lambda r)}{\lambda\sinh r},\qquad
\varphi_0(r)=\frac r{\sinh r}.
\]
For \(a>1\), the radial function \(f(r)=e^{-ar}\cos(\omega r)\) is in \(L^2(\mathbb H^3)\) and admits an absolutely convergent real-axis spherical transform
\[
\widehat f(\lambda)=\frac{4\pi}{\lambda}\int_0^\infty e^{-ar}\cos(\omega r)\sinh r\sin(\lambda r)\,dr.
\]
All formulas at \(\lambda=0\) are understood by continuity. For \(c>0\) and \(u=\lambda^2\ge0\), set
\[
D_c(u)=[c^2+(\lambda-\omega)^2][c^2+(\lambda+\omega)^2]
=(c^2+u+\omega^2)^2-4u\omega^2>0,
\quad G_c(u)=\frac{c^2+u-\omega^2}{D_c(u)}.
\]
The elementary Laplace sine integral \(\int_0^\infty e^{-cr}\sin(tr)\,dr=t/(c^2+t^2)\), together with the product-to-sum formula and \(2\sinh r=e^r-e^{-r}\), gives
\[
\widehat f(\lambda)=2\pi\bigl(G_{a-1}(u)-G_{a+1}(u)\bigr).
\]
Expansion over the positive denominator gives the exact rational form
\[
\widehat f(\lambda)=\frac{8\pi a\,P_{a,\omega}(u)}{D_{a-1}(u)D_{a+1}(u)},
\quad
P_{a,\omega}(u)=u^2+2(a^2+\omega^2+1)u+(a^2-1)^2-2(a^2+1)\omega^2-3\omega^4.
\]
Since \(P_{a,\omega}'(u)=2u+2(a^2+\omega^2+1)>0\) on \([0,\infty)\), nonnegativity of \(\widehat f\) for every real spectral parameter is **equivalent** to \(P_{a,\omega}(0)\ge0\). Solving this quadratic inequality in \(\omega^2\ge0\) gives the displayed sharp threshold, including equality.

To turn spectral sign into kernel positivity without assuming any unproved finite-grid criterion, use radial spherical inversion. With the above normalization,
\[
f(r)=\frac1{2\pi^2}\int_0^\infty\widehat f(\lambda)\varphi_\lambda(r)\lambda^2\,d\lambda.
\]
Here the integrand is absolutely integrable even at \(r=0\), because \(\widehat f(\lambda)=O(\lambda^{-4})\) as \(\lambda\to\infty\) and is bounded near zero. Each real-parameter \(\varphi_\lambda(d(x,y))\) is a normalized positive-semidefinite spherical kernel on \(\mathbb H^3\). Thus \(\widehat f\ge0\) yields the required positive-semidefinite Gram matrices by integration against the positive measure \(\lambda^2d\lambda/(2\pi^2)\).

Conversely, suppose the distance kernel is positive semidefinite. In particular its radial convolution form is nonnegative against \(h*h^*\) for every compactly supported smooth radial test function \(h\). Radial Plancherel and convolution convert this form (up to the fixed positive transform-normalization constant) into \(\int_0^\infty\widehat f(\lambda)|\widehat h(\lambda)|^2\lambda^2d\lambda\ge0\). Since \(a>1\) gives \(f\in L^2\), its spherical transform is defined in \(L^2\); here the explicitly computed transform is continuous and bounded, so the associated multiplier form extends continuously to the radial \(L^2\) transform space. Density and surjectivity of the spherical Plancherel transform force \(\widehat f\ge0\) almost everywhere, hence everywhere by continuity. If \(P_{a,\omega}(0)<0\), continuity makes \(\widehat f\) negative on an open interval of positive \(\lambda\), a contradiction. This establishes both directions.

## Verification
The included `check_spherical_symbolics.py` independently expands the rational numerator and checks its equality to the stated polynomial using exact symbolic algebra. It also checks the threshold equation algebraically and evaluates interior, boundary, and exterior parameter examples. The proof itself is analytic and does not depend on sampling spectral frequencies. The spectral inversion normalization and the spectral positivity criterion follow from standard spherical Plancherel theory; the algebraic factorization is the only special calculation.

## Relationship to prior work
Pusti (2011, arXiv:1111.3157), particularly Sections 2–3, supplies the relevant general spherical-transform and Bochner-type context; it does not state the two-parameter damped-cosine threshold. Feragen, Lauze and Hauberg (2014, arXiv:1411.0296), especially its discussion of geodesic Laplacian kernels, establishes the motivation for the unmodulated \(\omega=0\) geodesic exponential but does not classify oscillatory modulation. This result concerns \(\mathbb H^3\), not the Euclidean or spherical cases, and derives an exact curvature-dependent region that is not implied by Euclidean radial covariance calculations.

## Limitations
The \(a>1\) hypothesis ensures the required square integrability and direct real-axis spherical transform; the region \(0<a\le1\) is not classified here. No assertion of independent verification, priority over all unindexed literature, or strict positive definiteness is made. Exact priority remains subject to comparison with literature beyond the inspected sources. The normalization assumes sectional curvature \(-1\).

## References
1. Sanjoy Pusti, *An analogue of Bochner's theorem for Damek–Ricci spaces*, arXiv:1111.3157 (first publicly submitted 2011-11-14), especially Sections 2–3. https://arxiv.org/html/1111.3157v1
2. Aasa Feragen, François Lauze, and Søren Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (first publicly submitted 2014-11-02), especially the geodesic Laplacian kernel discussion. https://arxiv.org/html/1411.0296v2
