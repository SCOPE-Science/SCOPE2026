# A logarithmic acute-triangle law for the boundary of a thin rectangle

## Finding

For every real \(L\ge2\), let \(Q_L=[0,L]\times[0,1]\). Independently sample three points from \(\partial Q_L\) by normalized Euclidean arclength. Let \(p(L)\) be the probability that their triangle has all three angles strictly less than \(\pi/2\). Define
\[
J(L)=\int_0^L (L-r)w(r)\,dr,\qquad
w(r)=\begin{cases}r,&0\le r\le2,\\r-\sqrt{r^2-4},&r>2.\end{cases}
\]
Then, with \(p_{\mathrm{opp}}(L)=3J(L)/(2(L+1)^3)\),
\[
0\le p(L)-p_{\mathrm{opp}}(L)
\le\frac{12(2+4\log L)+8+48/L}{8(L+1)^3}.
\]
In particular the *two-term sharp asymptotic* is
\[
\boxed{p(L)=\frac{3\log L-3/2}{L^2}
+O\!\left(\frac{\log L}{L^3}\right),\qquad L\longrightarrow\infty.}
\]
Both coefficients are exact: \(L^2p(L)/\log L\to3\) and \(L^2p(L)-3\log L\to-3/2\). The contribution \(p_{\mathrm{opp}}\) has the closed form
\[
\frac{3}{2(L+1)^3}\left\{L\left[\frac{L^2-L\sqrt{L^2-4}}2
+2\log\left(\frac{L+\sqrt{L^2-4}}2\right)\right]
-\frac{L^3-(L^2-4)^{3/2}}3\right\}.
\]
Here \(p_{\mathrm{opp}}\) is precisely the probability of an acute triangle with two sampled points on one long horizontal edge and the third on the opposite horizontal edge. No other edge allocation changes either of the two leading asymptotic terms.

## Assumptions and scope

Rectangles are Euclidean, with short side length one; scale invariance gives the same result for any positive short side length and aspect ratio \(L\). Sampling is independent and uniform over the entire *boundary* of perimeter \(P=2(L+1)\), not uniform in the rectangle's interior. Three points on a common edge yield a degenerate triangle and are not counted as acute. Endpoint and right-angle coincidences outside such degenerate edge events have probability zero. The theorem concerns all real \(L\ge2\), not only integer ratios.

## Proof

**1. The event on opposite long edges.** Select a bottom-edge pair \((x_1,0),(x_2,0)\) with \(x_1<x_2\), put \(r=x_2-x_1\), and select a top-edge point \((z,1)\). The angles at the first two points are acute exactly if \(x_1<z<x_2\). The remaining angle is acute exactly if
\[
1>(z-x_1)(x_2-z).
\]
The permissible length of \(z\) is \(r\) for \(r\le2\) and \(r-\sqrt{r^2-4}\) for \(r>2\), precisely \(w(r)\). There are two choices of the doubly occupied long edge and three assignments of the labeled sample points; all have joint arclength density \(P^{-3}\). As
\[
\int_{[0,L]^2}w(|x-y|)\,dx\,dy
=2\int_0^L(L-r)w(r)\,dr,
\]
the total probability from this allocation is \(12J(L)/P^3=3J(L)/(2(L+1)^3)\).

**2. Exact integration.** For \(L\ge2\), integration separately over \([0,2]\) and \([2,L]\) gives
\[
A(L):=\int_0^Lw(r)\,dr=\frac{L^2-L\sqrt{L^2-4}}2
+2\log\left(\frac{L+\sqrt{L^2-4}}2\right),
\]
\[
B(L):=\int_0^Lrw(r)\,dr=
\frac{L^3-(L^2-4)^{3/2}}3.
\]
The formulas hold continuously at \(L=2\), where \(A(2)=2\) and \(B(2)=8/3\). Since \(J(L)=LA(L)-B(L)\), the closed expression follows. Expansion of the radicals and logarithm gives
\[
A(L)=2\log L+1+O(L^{-2}),\qquad
B(L)=2L+O(L^{-1}),
\]
so \(J(L)=2L\log L-L+O(L^{-1})\), whence
\[
p_{\mathrm{opp}}(L)=\frac{3\log L-3/2}{L^2}
+O\!\left(\frac{\log L}{L^3}\right).
\]

**3. Every other allocation is smaller.** Write a short-edge point on the left vertical edge as \((0,v)\), with \(v\in[0,1]\). If the two other points are \((x,0)\) and \((y,1)\) on distinct long edges, acuteness at those two points requires
\[
y<x+\frac vx\quad\text{if }y>x,\qquad
x<y+\frac{1-v}{y}\quad\text{if }x>y.
\]
In particular, for each \(v\) the allowable \((x,y)\) region has area at most
\[
2\int_0^L\min\{L-u,1/u\}\,du
\le 2+4\log L\qquad(L\ge2).
\]
There are two choices of short edge and six assignments of the three labeled points, so these events contribute at most \(12(2+4\log L)/P^3\). A short-edge point with two points on the *same* long edge cannot give an acute triangle: its horizontal projection falls outside the interval between those points.

If two points lie on one short edge and the remaining point on a long edge, an acute triangle is again impossible by vertical projection. If the two short-edge points lie on *opposite* vertical edges, the point \((x,0)\) or \((x,1)\) on a long edge can form an acute angle only if \(x(L-x)<1\). For \(L\ge2\) the set of such \(x\) has total length at most \(4/L\). There are twelve labeled assignments including the two choices of long edge, yielding probability at most \(48/(LP^3)\). Finally, all-three-short-edge allocations have probability at most \((2/P)^3=8/P^3\). Since these event classes are exhaustive and disjoint up to arclength-zero boundaries, adding their bounds gives the explicit theorem. The residual is \(O((\log L)/L^3)\), completing both sharp asymptotic limits. \(\square\)

## Verification

The accompanying `verify.py` differentiates the two antiderivative expressions symbolically and checks their endpoint values and Laurent expansions; it also compares the exact dominant-event formula with independent numerical quadratures at six aspect ratios. Execution uses `python verify.py` with `sympy` and `mpmath`. Observed output includes `VERIFY_OK primitive_derivatives=2 endpoint_values=2 symbolic_series=2 quadratures=6 asymptotic_checks=4`. These finite checks are diagnostics; the probability bound and asymptotic claims follow from the preceding proof.

## Relationship to prior work

Langford (1969) computed an obtuse-triangle probability for three **interior-coordinate-uniform** points in an arbitrary rectangle, a different probability measure. Hall (1982) likewise studied uniform points in an \(n\)-ball. An openly available 2012 derivation by Joriki evaluates the **boundary-uniform square** probability as \(23/96\), but does not give a thin-rectangle formula or its singular logarithmic scaling. The present theorem treats the entire one-parameter degenerating rectangular-boundary family and identifies the exact first two asymptotic terms with a finite-ratio error bound. Different sampling measures do not imply one another's probabilities. Historical priority has not been independently certified.

## Limitations

No explicit exact closed form is claimed here for the total acute probability at arbitrary finite aspect ratio; the theorem gives its exact dominant contribution and a proven remainder interval. Uniform sampling is by boundary arclength; conclusions do not apply to interior sampling or nonrectangular quadrilaterals. The formula is asymptotic as the aspect ratio tends to infinity, and the stated finite-ratio upper remainder is rigorous but not optimal. A full-text historical comparison with every older geometric-probability article was not possible.

## References

1. E. Langford, “The probability that a random triangle is obtuse,” *Biometrika* **56** (1969), 689–690. DOI: `10.1093/biomet/56.3.689` (interior-uniform rectangle; publisher abstract inspected).
2. G. R. Hall, “Acute triangles in the n-ball,” *Journal of Applied Probability* **19** (1982), 712–715. DOI: `10.2307/3213533` (interior-uniform ball; publisher abstract inspected).
3. Joriki, answer of 2012-04-09 to “What's the probability that three points determine an acute triangle?”, Mathematics Stack Exchange, `https://math.stackexchange.com/questions/126719` (complete relevant boundary-square derivation inspected).
4. S. Portnoy, “A Lewis Carroll pillow problem: Probability of an obtuse triangle,” *Statistical Science* **9** (1994), 279–284. DOI: `10.1214/ss/1177010497` (description and abstract inspected).
