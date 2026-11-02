# Exact intrinsic mean distance and sharp balancing law for three-path theta graphs

## Finding
Let \(\Theta(a,b,c)\) be the compact metric graph consisting of three different intervals with their two endpoints identified in common. Give the graph its shortest-path metric and its arclength measure. For all real lengths \(0<a\le b\le c\), let \(T=a+b+c\), and choose \(X,Y\) independently uniformly with respect to normalized arclength. Then the entire length-dependent mean geodesic distance is
\[
\mathbb E[d(X,Y)]=\frac{2a^3+a^2(b+c)+3a(b^2+c^2)+4abc+b^3+2b^2c+2bc^2+c^3}{4T^2}.
\]
It has the **sharp global lower bound at fixed total length**
\[
\mathbb E[d(X,Y)]\ge \frac{5T}{27},
\]
with equality if and only if \(a=b=c=T/3\). The mean is **neither Schur-convex nor Schur-concave** in the three edge lengths at fixed sum. In particular, for \(T=3\), the isosceles family \(a=x\), \(b=c=(3-x)/2\), \(0<x\le1\), has
\[
\mathbb E[d(X,Y)]=\frac{11x^3-21x^2+9x+81}{144}.
\]
This family has its unique interior maximum at \(x=3/11\), with mean \(5/9+16/1089\); balancing the lengths from \(x<3/11\) towards \(3/11\) thus *increases* the mean.

## Assumptions and scope
The three intervals are *metrically distinct edges* of positive real lengths, joined only at the two common endpoints. The intrinsic distance is the minimum total arclength over all graph paths. The two random points are independent; each point has probability proportional to edge length of lying on a given edge. No Euclidean embedding or uniform edge-label sampling is assumed. Formulas use sorted edge lengths, but permutation of the three edges does not affect the invariant. Boundary lengths tending to zero are considered only as limits, never as equality cases.

## Proof
Orient all edges from their first common endpoint \(A\) to their second \(B\), and let \(x,y\) be arclength coordinates.

**1. Same-edge pairs.** For an edge of length \(L\) whose shorter *other* edge has length \(s\), the only simple competing paths are the internal segment and the complementary segment going around the shortest other edge. Therefore
\[
d_{L,L}(x,y)=\min\{|x-y|,L+s-|x-y|\}.
\]
Since the set of pairs with \(|x-y|=t\) has area density \(2(L-t)\), elementary integration yields
\[
I(L,s):=\int_0^L\!\int_0^L d_{L,L}(x,y)\,dx\,dy
=\frac{L^3}{3}-\frac{(L-s)_+^3}{12}.
\]
For sorted lengths, the same-edge contributions are \(I(a,b)+I(b,a)+I(c,a)\).

**2. Distinct-edge pairs.** For lengths \(r\le s\), the routes through either common endpoint have minimum \(\min(x+y,r+s-x-y)\). Its rectangle integral is
\[
J_0(r,s)=\frac{r^2s}{2}+\frac{rs^2}{4}-\frac{r^3}{12}.
\]
For the pairs \((a,b)\) and \((a,c)\), routing through the third edge cannot improve this minimum, because that third edge is at least as long as \(a\). For the pair \((b,c)\), routing through the shorter unused edge of length \(a\) can improve the minimum in two opposite corner rectangles, and nowhere else. In corner coordinates, put \(B=(b-a)/2\), \(C=(c-a)/2\), so \(0\le B\le C\). On each rectangle \([0,B]\times[0,C]\), the pointwise improvement is \(2\min\{B-x,C-y\}\). Thus the total correction across both corners is
\[
J_{\mathrm{corr}}=2\int_0^B\!\int_0^C2\min\{B-x,C-y\}\,dy\,dx
=\frac{(c-a)(b-a)^2}{4}-\frac{(b-a)^3}{12}.
\]
Here all paths are simple and the four candidate distinct-edge path lengths are explicitly
\[
x+y,\quad b+c-x-y,\quad x+a+c-y,\quad b-x+a+y.
\]
Hence the integral for the \((b,c)\) pair is \(J_0(b,c)-J_{\mathrm{corr}}\).

**3. Assemble the ordered double integral.** The same-edge squares occur once, and distinct-edge rectangles occur twice. Consequently
\[
T^2\mathbb E[d(X,Y)]
=I(a,b)+I(b,a)+I(c,a)
+2\bigl(J_0(a,b)+J_0(a,c)+J_0(b,c)-J_{\mathrm{corr}}\bigr).
\]
Expanding gives the stated homogeneous cubic numerator and proves the formula for all positive real lengths, including equality between lengths by continuity.

**4. Sharp inequality and equality.** Set \(u=b-a\ge0\) and \(v=c-b\ge0\). Exact expansion gives the nonnegative certificate
\[
108T^2\left(\mathbb E[d(X,Y)]-\frac{5T}{27}\right)
=36au^2+36auv+36av^2+2u^3+3u^2v+15uv^2+7v^3.
\]
All coefficients are positive, and \(a>0\). The right-hand side vanishes exactly for \(u=v=0\); this proves the sharp bound and uniqueness of the equilateral optimizer.

**5. Majorization obstruction.** On the fixed-total-length isosceles family, direct substitution and differentiation give
\[
\frac{d}{dx}\mathbb E[d(X,Y)]=\frac{(x-1)(11x-3)}{48}.
\]
The derivative is positive for \(0<x<3/11\) and negative for \(3/11<x<1\). Increasing \(x\) towards \(3/11\) balances the sorted triple but increases the mean, contradicting Schur-convexity. Since equality of lengths is the strict global minimum, Schur-concavity fails as well. At \(x=3/11\), the exact excess over the equilateral value is \(16/1089\).

## Verification
Run `python3 verify.py` in the same directory as this file. The standalone verifier checks two independently organized exact integral expressions for 64 rational triples, the nonnegative gap identity and equality criterion, the exact isosceles critical value, and shortest-path Monte Carlo comparisons in five additional geometries (750,000 pairs). It reported `PASS: 330 exact assertions and 750000 independently sampled point-pairs`. This is finite computational corroboration only: the infinite-parameter proof is the integration and coefficientwise inequality above. The direct path enumeration in the verifier uses the four possible simple routes independently of the integrated cubic.

## Relationship to prior work
Doyle and Graver introduced mean distances for graph-shaped domains and studied, among other configurations, three edges connecting two common vertices for *constrained edge lengths*. Their original 1982 full-length article could not be examined in full for this assessment; a later comprehensive review explicitly describes its restricted cases. Garijo, Márquez, and Silveira (first available preprint 2021) prove a general algorithm computing the continuous mean distance of any weighted graph, which therefore computes this example algorithmically, but do not present the all-positive-length cubic, the sharp \(5/27\) fixed-length inequality, or the failure of length majorization. Baptista, Kennedy, and Mugnolo (2023 preprint) prove general graph lower and upper bounds, including the \(T/4\) upper bound for doubly connected graphs. That **general upper bound is prior work**, not claimed here. Published related results about theta-graph algebraic gnarledness and metric Vietoris–Rips persistence concern different invariants, and neither implies the exact mean or sharp optimizer. The sharp fixed-topology result lies strictly between general bounds for three-edge graphs.

## Limitations
Only theta graphs with three parallel metric edges are treated; the result is not an arbitrary network formula, not a discrete-vertex Wiener-index theorem, and not an assertion of a sharp lower bound among all graphs with three edges. Unseen or unindexed prior treatments of unrestricted three-edge theta lengths remain possible, particularly because the relevant full 1982 article was not accessible. No independent external audit has been performed.

## References
1. J. K. Doyle and J. E. Graver, *A Summary of Results on Mean Distance in Shapes*, Environment and Planning B 9 (1982), 177–179. DOI: 10.1068/b090177.
2. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471. DOI: 10.1002/jgt.3190060410.
3. D. Garijo, A. Márquez, R. I. Silveira, *Continuous mean distance of a weighted graph*, arXiv:2103.11676 (2021); Results in Mathematics 78 (2023), 139. DOI: 10.1007/s00025-023-01902-w.
4. L. N. Baptista, J. B. Kennedy, D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952 (2023), Theorem 3.2.
