# Fifth-chord-moment law for acute triangles in thin convex bodies

## Finding

Let \(K\) be any full-dimensional compact convex subset of \(\mathbb R^2\). Write \(A=|K|>0\), let \([a,b]\) be its orthogonal projection on the first coordinate, write \(L=b-a>0\), and define the length of its vertical section by
\[
w(x)=\mathcal H^1\bigl(K\cap(\{x\}\times\mathbb R)\bigr),\quad a\le x\le b.
\]
For \(0<\varepsilon<1\) define the anisotropic compression
\[
K_\varepsilon=\{(x,\varepsilon y):(x,y)\in K\}.
\]
Let \(P_K(\varepsilon)\) be the probability that three independent, area-uniform points of \(K_\varepsilon\) form a **strictly acute** Euclidean triangle. Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{P_K(\varepsilon)}{\varepsilon^2\log(1/\varepsilon)}=C(K):=\frac{1}{A^3}\int_a^b w(x)^5\,dx.}
\]
Furthermore the coefficient lies in the sharp interval
\[
\boxed{\frac{A^2}{L^4}\le C(K)\le\frac{16A^2}{3L^4}.}
\]
The first constant is attained by rectangles and the second by nondegenerate triangles with the indicated vertical fiber direction. Neither the fifth-chord-moment formula nor its shape bounds assert a finite-\(\varepsilon\) inequality or a rate uniform across different bodies.

## Assumptions and scope

The body is compact and convex with nonempty planar interior. Its sections are vertical closed intervals \(I(x)=[\ell(x),u(x)]\), with \(w(x)=u(x)-\ell(x)\) at interior projection points; on \((a,b)\), both endpoints are continuous. Brunn--Minkowski in one dimension makes \(w\) nonnegative and concave. All logarithms are natural; probabilities use planar Lebesgue measure divided by \(\varepsilon A\). Translations and horizontal/vertical shears of \(K\) are allowed; only a fixed \(K\) is sent to the thin limit. Acute means that all three strict Euclidean angle tests are satisfied; degenerate/right events have probability zero.

## Proof

**Step 1: Exact acute-angle test after sorting.** Pull the three uniform points back to \(K\), and sort their first coordinates as \(x_1=x\), \(x_2=x+s\), \(x_3=x+s+t\), with \(s,t>0\). Because ties have measure zero, sorting gives density factor \(6/A^3\). Write the corresponding ordinate differences as \(\alpha=y_2-y_1\), \(\beta=y_3-y_2\). The three strict angle conditions in \(K_\varepsilon\), at left, middle and right, are exactly
\[
\begin{aligned}
 s(s+t)+\varepsilon^2\alpha(\alpha+\beta)&>0,\\
 -st-\varepsilon^2\alpha\beta&>0,\\
 t(s+t)+\varepsilon^2\beta(\alpha+\beta)&>0.
\end{aligned}
\]
Consequently \(\alpha\beta<0\) and \(st<\varepsilon^2|\alpha\beta|\) are necessary. Let \(D>0\) be the total vertical diameter of \(K\). Then \(|\alpha|,|\beta|,|\alpha+\beta|\le D\).

**Step 2: One logarithmic gap regime.** Split the sorted configurations into the two disjoint regimes \(s\le t\) and \(t<s\), ignoring their null separating set. In the first, configurations with \(0<t\le D\varepsilon\) contribute at most \(O_K(\varepsilon^2)\) to the probability: their allowed \((s,t)\) triangle has area \(O(D^2\varepsilon^2)\), and the three vertical integrals are uniformly bounded.

For \(t>D\varepsilon\), introduce \(z=st/\varepsilon^2\), so \(s=\varepsilon^2 z/t\), \(ds=\varepsilon^2\,dz/t\). The necessary middle-angle condition bounds \(0<z<D^2\). It also forces \(s<t\), since \(s/t\le D^2\varepsilon^2/t^2<1\). The right-angle test is automatically strict because \(t(t+s)>\varepsilon^2D^2\). The middle-angle test is \(0<z<-\alpha\beta\); the left-angle test reduces exactly to
\[
z\left(1+\frac{\varepsilon^2z}{t^2}\right)+\alpha(\alpha+\beta)>0.
\]
The remaining ordered-coordinate domain requires \(x+s+t\le b\). Everything has a bound independent of \(\varepsilon\) after factoring out \(\varepsilon^2\,dt/t\).

**Step 3: Extracting the logarithmic coefficient.** For any fixed \(0<\theta<1\), set \(t=\varepsilon^\theta\). Then \(t\to0\), \(\varepsilon/t\to0\), and \(s\le D^2\varepsilon^{2-\theta}\to0\). On almost every \(x\in(a,b)\), the three section intervals \(I(x)\), \(I(x+s)\), and \(I(x+s+t)\) converge to the same interval \(I(x)\); the coefficient \(\varepsilon^2z/t^2\to0\). Consequently the limiting allowed \(z\)-length for fixed ordinates is
\[
\mathbf1_{\alpha\beta<0}\left[(-\alpha\beta)-\max\{0,-\alpha(\alpha+\beta)\}\right]
=\mathbf1_{\alpha\beta<0}|\alpha|\min\{|\alpha|,|\beta|\}.
\]
Here the displayed bracket is nonnegative on the indicated event. Passing to the limit under the bounded quadruple integral is valid by dominated convergence, because the exceptional equality hypersurfaces have Lebesgue measure zero. Integrating in \(dt/t\) corresponds to integrating over \(\theta\in(0,1)\) with the factor \(\log(1/\varepsilon)\). Values of \(t\) outside this logarithmic window (a fixed multiplicative neighborhood of \(D\varepsilon\) or bounded away from zero) contribute only \(O_K(\varepsilon^2)\); equivalently one can first truncate \(\theta\) to \([\delta,1-\delta]\), apply dominated convergence, and let \(\delta\downarrow0\). Thus the coefficient from \(s<t\) is
\[
\frac{6}{A^3}\int_a^b\!\int_{I(x)^3}
\mathbf1_{\alpha\beta<0}|\alpha|\min(|\alpha|,|\beta|)
\,dy_1\,dy_2\,dy_3\,dx.
\]

**Step 4: Exact fiber integral and the other regime.** If \(I\) is any interval of length \(w\), splitting according as \(y_2\) is the maximum or the minimum gives
\[
\begin{aligned}
&\int_{I^3}\mathbf1_{\alpha\beta<0}|\alpha|\min(|\alpha|,|\beta|)\,d\boldsymbol y\\
&=2\int_0^w\!\int_0^r\!\int_0^r u\min(u,v)\,dv\,du\,dr
=2\cdot\frac{w^5}{5}\cdot\frac5{24}=\frac{w^5}{12}.
\end{aligned}
\]
Hence \(s<t\) contributes \(\int w^5/(2A^3)\). Reversing the labels of the two end points exchanges \(s<t\) with \(t<s\) and leaves all three angles invariant, giving an equal coefficient. Adding yields \(C(K)=A^{-3}\int w^5\), as claimed.

**Step 5: Sharp coefficient bounds.** Jensen's inequality, \(A=\int_a^b w\), and convexity of the fifth power yield
\[
\int_a^b w^5\,dx\ge L\left(\frac AL\right)^5=\frac{A^5}{L^4}.
\]
For a nonnegative concave function on an interval, the classical one-dimensional Berwald inequality between exponents one and five says
\[
\left(\frac6L\int_a^b w^5\,dx\right)^{1/5}\le\frac2L\int_a^b w\,dx=\frac{2A}{L}.
\]
Thus \(\int w^5\le16A^5/(3L^4)\). Divide by \(A^3\). Constant vertical chords attain the Jensen side (for instance rectangles); an affine decreasing chord function \(w(x)=h(1-(x-a)/L)\) yields equality in Berwald (for instance right triangles). Both bounds are therefore globally sharp.

## Verification

The fiber integral is independently evaluated by an exact rational polynomial identity in the attached executable `check_acute.py`. That program also verifies the area/chord-moment constants for a rectangle, a triangle and a trapezoid, and compares seeded Sobol gap-conditioned numerical integrations at multiple compression scales with the limiting coefficients. The finite computations are corroboration, **not** a replacement for the limiting argument or for Berwald's known inequality. In particular the convergence is logarithmically slow, and finite-width numerical values should not be mistaken for their limits.

## Relationship to prior work

The general random-obtuse-triangle question is classical. Langford (1969) gives the probability for each fixed rectangle; this includes the rectangular subcase and is expressly not claimed as new. Beck (first available January 20, 2025) provides a full analysis for the three-dimensional cube, including a review of Langford's two-dimensional formula and Crofton reduction. Drivas and Retakh (2025) give distribution-uniform probability constraints, a different type of result. The **new claim here** is the precise all-planar-convex-body *thin-direction* coefficient as a fifth parallel-chord moment, with sharp geometrically normalized range. Jensen's inequality and Berwald's reverse Hölder theorem are acknowledged tools, not new results. No inspected primary source or mathematical-result comparison yielded the same general coefficient; that absence is not a proof of historical priority.

## Limitations

The full two-page Langford (1969) text was inaccessible, notwithstanding open-access and institutional access attempts; its abstract and the complete later treatment by Beck were available for comparison. An unindexed earlier derivation, especially for slender rectangles or more general convex bodies, remains a priority risk. Neither a uniform error term, an optimal finite-compression shape, nor a higher-dimensional analogue is established. The result does not identify a finite positive compression threshold. Independent scientific validation has not been performed.

## References

1. D. Beck, *The Probability that a Random Triangle in a Cube is Obtuse*, first preprint 2025-01-20, arXiv:2501.11611; open full journal HTML: https://www.cambridge.org/core/journals/journal-of-applied-probability/article/probability-that-a-random-triangle-in-a-cube-is-obtuse/BB6E7ECA977E3BB6EEDFB478C90BAB60.
2. E. Langford, *The probability that a random triangle is obtuse*, Biometrika 56 (1969), 689–690, https://doi.org/10.1093/biomet/56.3.689 (abstract accessible, full text not obtained).
3. T. D. Drivas and M. Retakh, *How doth the random triangle*, first preprint 2025-08-25, arXiv:2508.18414 (abstract accessible).
4. *A discrete approach to Zhang's projection inequality*, Canadian Journal of Mathematics, 2025, https://doi.org/10.4153/S0008414X25101624, Section 2.3 (accessible full HTML statement of the classical Berwald inequality).
