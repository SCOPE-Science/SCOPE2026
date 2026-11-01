# Sharp finite-sample perimeter isoperimetry and fourth-order curvature memory for random boundary polygons

## Finding
Let \(K\subset\mathbb R^2\) be a compact convex body with nonempty interior and perimeter \(L\). Let \(Z_1,\ldots,Z_m\), independently for every integer \(m\ge3\), be uniformly distributed with respect to normalized boundary arclength, and put \(P_m=\operatorname{conv}\{Z_1,\ldots,Z_m\}\). The exact all-sample-size inequality is
\[
\mathbb E\operatorname{Area}(P_m)\le \frac{m b_{m,1}}{8\pi^2}L^2,
\qquad
b_{m,k}=(m-1)\int_0^1(1-u)^{m-2}\sin(2\pi k u)\,du.
\]
Equality holds if and only if \(K\) is a Euclidean disk (up to translation). Every \(b_{m,k}\) is strictly positive for integers \(m\ge3\) and \(k\ge1\). This improves the ordinary isoperimetric upper bound on the expected random-polygon area for every finite sample size, with the sharp constant attained by the disk.

More precisely, identify the plane with \(\mathbb C\), parametrize \(\partial K\) counterclockwise by unit-speed arclength \(\gamma(s)\) of period \(L\), and define Fourier coefficients
\[
c_n=\frac1L\int_0^L \gamma(s)e^{-2\pi i ns/L}\,ds\quad(n\in\mathbb Z).
\]
Then the following series converge absolutely:
\[
\mathbb E\operatorname{Area}(P_m)
=\frac m2\sum_{k=1}^\infty b_{m,k}\bigl(|c_k|^2-|c_{-k}|^2\bigr),
\]
and, crucially, the isoperimetric deficit has the **exact nonnegative spectral decomposition**
\[
\frac{m b_{m,1}}{8\pi^2}L^2-\mathbb E\operatorname{Area}(P_m)
=\frac m2\sum_{k=1}^\infty\bigl[(k^2b_{m,1}-b_{m,k})|c_k|^2
+(k^2b_{m,1}+b_{m,k})|c_{-k}|^2\bigr].
\]
Every displayed coefficient is nonnegative, and all except the positive first-frequency coefficient are strictly positive. For example, the sharp expected areas at perimeter \(L\) are \(3L^2/(8\pi^3)\) when \(m=3\) and \(3L^2/(4\pi^3)\) when \(m=4\).

For a counterclockwise **\(C^4\)** unit-speed boundary with curvature \(\kappa(s)\ge0\), the expected missed area has the following further **shape-sensitive fourth-order expansion**:
\[
\begin{aligned}
\operatorname{Area}(K)-\mathbb E\operatorname{Area}(P_m)
={}&\frac{\pi L^2}{(m+1)(m+2)}\\
&-\frac{L^4\int_0^L\kappa(s)^3\,ds}{2(m+1)(m+2)(m+3)(m+4)}+O_K(m^{-6}).
\end{aligned}
\]
The first coefficient depends only on perimeter, whereas the first curvature-sensitive coefficient depends on the curvature-cube integral. In this smooth convex class,
\[
\int_0^L\kappa(s)^3\,ds\ge\frac{8\pi^3}{L^2},
\]
with equality precisely for disks. The equality/range claims are in the indicated classes and do not require strictly positive curvature.

## Assumptions and scope
The main finite-sample results apply to every compact planar convex body with nonempty interior: no smoothness, strict convexity, or curvature hypothesis is imposed. Its positively oriented unit-speed boundary parametrization is Lipschitz and defined uniquely up to arclength origin. The Fourier series is understood in \(H^1\), and all area assertions concern ordinary Euclidean area, with samples uniform by arclength rather than by angular parameter or interior area. The asymptotic expansion needs a \(C^4\) periodic unit-speed parametrization; these assumptions imply \(\gamma^{(4)}\in L^2\). Here \(m\to\infty\) with a fixed body \(K\), so the implicit error constant may depend on \(K\).

## Proof
**Step 1: exact random-gap representation.** Ordering the \(m\) almost surely distinct samples counterclockwise produces a convex polygon. Its area equals one half the sum of the positive cross products of successive vertices, including the wrap-around edge. Choose one of the \(m\) ordered sample vertices uniformly by index, and write \(U\) for its forward cyclic arclength gap divided by \(L\). By rotation invariance of independent uniform arclength coordinates, its starting arclength \(S\) is uniform on \([0,L)\), independent of \(U\), and \(U\) has the \(\operatorname{Beta}(1,m-1)\) law with density \((m-1)(1-u)^{m-2}\). Consequently
\[
\mathbb E\operatorname{Area}(P_m)
=\frac m2\mathbb E\operatorname{Im}\bigl(\overline{\gamma(S)}\gamma(S+LU)\bigr).
\]
The shift-correlation identity for Fourier series, valid first for smooth trigonometric approximants and then by \(L^2\)-continuity, yields
\[
\frac1L\int_0^L\operatorname{Im}\bigl(\overline{\gamma(s)}\gamma(s+Lu)\bigr)\,ds
=\sum_{n\in\mathbb Z}|c_n|^2\sin(2\pi nu).
\]
Integrating over \(U\) and pairing opposite integers gives the exact spectral expectation formula in the Finding.

**Step 2: strict spectral comparison.** Integration by parts, using the vanishing of \(\sin(2\pi ku)\) at both endpoints, gives for \(m\ge3\)
\[
b_{m,k}=\frac{(m-1)(m-2)}{2\pi k}
\int_0^1(1-u)^{m-3}(1-\cos(2\pi k u))\,du>0.
\]
For integer \(k\ge2\), the pointwise inequality \(1-\cos(k\theta)\le k^2(1-\cos\theta)\), strict except on a set of zero measure, implies \(0<b_{m,k}<k b_{m,1}\le k^2b_{m,1}\). Since \(|\gamma'(s)|=1\) almost everywhere, Parseval implies
\[
\sum_{n\in\mathbb Z}n^2|c_n|^2=\frac{L^2}{4\pi^2}.
\]
Subtracting the exact expected area from \(m b_{m,1}L^2/(8\pi^2)\) gives the nonnegative series written above. A zero deficit forces \(c_n=0\) except possibly \(n=0,1\), because every other coefficient has a strictly positive multiplier. Thus \(\gamma(s)=c_0+c_1e^{2\pi i s/L}\) in \(H^1\). Unit speed forces \(|c_1|=L/(2\pi)\), hence \(K\) is a disk. Conversely a disk has exactly those two modes and attains equality. The absolute convergence of every series follows from \(H^1\) and \(b_{m,k}\le k b_{m,1}\).

**Step 3: curvature-cube expansion with an actual remainder bound.** Taylor's formula for the sine function, with global seventh-order remainder, and the beta moments
\[
\mathbb E U^r=\frac{r!}{m(m+1)\cdots(m+r-1)}
\]
give for every integer \(n\), with sign retained for negative \(n\),
\[
\begin{aligned}
\mathbb E\sin(2\pi nU)
={}&\frac{2\pi n}{m}-\frac{(2\pi n)^3}{m(m+1)(m+2)}\\
&+\frac{(2\pi n)^5}{m(m+1)(m+2)(m+3)(m+4)}+R_{m,n},\\
|R_{m,n}|\le{}&\frac{(2\pi|n|)^7}{m(m+1)\cdots(m+6)}.
\end{aligned}
\]
Because \(\gamma\in C^4\), Parseval for its fourth derivative gives \(\sum_n|n|^8|c_n|^2<\infty\), which dominates the remainder series and proves an aggregate \(O_K(m^{-6})\) error after multiplication by \(m/2\). The classical Fourier signed-area identity is
\[
\operatorname{Area}(K)=\pi\sum_n n|c_n|^2.
\]
The positive unit tangent \(T=\gamma'\) satisfies the planar Frenet formulas \(T'=i\kappa T\) and \(\gamma'''=(i\kappa'-\kappa^2)T\). Taking imaginary parts of periodic inner products and using Fourier orthogonality yields
\[
\left(\frac{2\pi}{L}\right)^3\sum_n n^3|c_n|^2
=\frac1L\int_0^L\kappa(s)\,ds=\frac{2\pi}{L},
\]
\[
\left(\frac{2\pi}{L}\right)^5\sum_n n^5|c_n|^2
=\frac1L\int_0^L\kappa(s)^3\,ds.
\]
The first is the total turning theorem and the second follows by taking \(\operatorname{Im}(\overline{\gamma''}\gamma''')=\kappa^3\). Inserting them into the beta-sine expansion proves the claimed area-deficit asymptotics, with all coefficients and the stated remainder. Finally Jensen's inequality for nonnegative curvature and \(\int_0^L\kappa=2\pi\) gives the sharp cubic lower bound. Equality requires constant curvature; periodic unit-speed convexity then forces a circle.

## Verification
The self-contained standard-library program `checker.py` checks 184 finite diagnostics, including 72 beta-weight evaluations against direct quadrature, 99 positivity/strict Fourier-weight inequalities, exact rational unit-square geometry, truncated Fourier reconstructions of that square, seeded circular Monte Carlo, the exact circle expansion at three sample sizes, and Gauss--Bonnet/Jensen diagnostics for a noncircular ellipse. Its finite checks do **not** establish the infinite-series or universal statements; Steps 1--3 prove those analytically. As a completely independent basic benchmark, three arclength-uniform points on the unit square produce mean triangle area \(5/32\), whereas four produce \(5/16\); both match the Fourier formula.

## Relationship to prior work
Fodor and Papvári, *On generalized disc-polygons in plane convex bodies with a higher degree of smoothness* (arXiv:2509.11702, originally posted 2025-09-16), derive high-order expansions for **interior-sampled generalized \(L\)-convex hulls**, a different stochastic model and operation from arclength-uniform classical convex hulls. Reitzner, Schütt and Werner (arXiv:1911.05917) study random points on **boundaries of higher-dimensional simple polytopes** and leading missing-volume asymptotics; their conclusions do not supply this all-finite-sample planar sharp perimeter inequality or the curvature-cube correction. Nikitin and Polevaya (2020, DOI below) address expected **perimeter** of inscribed random polygons, not the stated mean-area spectral identity. Existing unit-circle expected-area formulas, including the circle cases displayed here, are background checks, not claimed as new results. Research on optimal sampling densities for ellipse approximation and on Hausdorff error addresses different loss functionals or sampling laws.

## Limitations
The spectral inequality concerns arclength-uniform **boundary** sampling, not uniform interior sampling, arbitrary boundary density, or randomly oriented circumscribed polygons. The curvature-cube term is proved for fixed \(C^4\) convex curves only; no statement about nonsmooth polygonal asymptotic curvature corrections, a uniform remainder over classes of bodies, or independent mathematical certification is made. Despite extensive comparison against accessible primary material and indexed mathematical statements, older or unindexed priority claims about finite-sample extremality or higher-order boundary sampling remain a residual historical risk.

## References
1. F. Fodor and D. I. Papvári, *On generalized disc-polygons in plane convex bodies with a higher degree of smoothness*, arXiv:2509.11702 (first public version 2025-09-16), https://arxiv.org/abs/2509.11702.
2. M. Reitzner, C. Schütt, and E. Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope*, arXiv:1911.05917, https://arxiv.org/abs/1911.05917.
3. A. Nikitin and E. Polevaya, *On the average perimeter of the inscribed random polygon* (2020), DOI: 10.21638/11701/spbu01.2020.108.
4. M. Sonnleitner, *A limit theorem for Hausdorff approximation by random inscribed polytopes*, arXiv:2508.16442 (2025), https://arxiv.org/abs/2508.16442.
5. M. Reitzner, M. Sonnleitner, *Central limit theorems for random boundary polytopes*, arXiv:2509.20058 (2025), https://arxiv.org/abs/2509.20058.
