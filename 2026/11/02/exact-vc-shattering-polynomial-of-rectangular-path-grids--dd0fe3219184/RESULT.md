# Exact VC-shattering polynomial of rectangular path grids

## Finding

Let \(m,n\ge 1\) be integers, and let \(G_{m,n}=P_m\square P_n\) be the unweighted Cartesian product of two vertex paths, on vertex set \([m]\times[n]\). Let \(\mathcal C_{m,n}\) comprise every geodesically convex vertex subset, including \(\varnothing\). A set \(S\subseteq V(G_{m,n})\) is **shattered** when every \(T\subseteq S\) is a trace \(C\cap S\) for some \(C\in\mathcal C_{m,n}\). Write \(\Phi_{m,n}(z)=\sum_{S\text{ shattered}}z^{|S|}\).

**Theorem (complete exact profile).** For all positive integers \(m,n\),
\[
\boxed{\begin{aligned}
\Phi_{m,n}(z)={}&1+mnz+\binom{mn}{2}z^2\\
&+\frac{mn(m-1)(n-1)(2mn-m-n-4)}{18}\,z^3\\
&+\frac{m(m-1)^2(m-2)n(n-1)^2(n-2)}{144}\,z^4.
\end{aligned}}
\]
All higher coefficients vanish; all displayed rational expressions are integers. The two nontrivial coefficients count *all individual shattered supports*, not traces on one chosen support.

The VC dimension is \(1\) if \(m=n=1\), is \(2\) if \(\min(m,n)=1<\max(m,n)\) or \((m,n)=(2,2)\), is \(3\) if \(\min(m,n)=2<\max(m,n)\), and is \(4\) if \(m,n\ge3\).

**Exact geometric criterion.** Every nonempty convex set is an axis-aligned grid rectangle. Every singleton or two-point support is shattered. A support with at least two elements is shattered exactly when each of its vertices is the *unique strict minimum or strict maximum in at least one coordinate* among its support. This criterion determines every shattered support, including non-maximal supports and coordinate-tie cases.

For a uniformly random unordered triple from the grid, the shattering probability is the displayed cubic coefficient divided by \(\binom{mn}{3}\) (when the denominator is nonzero); for a random four-point support, it is the quartic coefficient divided by \(\binom{mn}{4}\). When both \(m,n\to\infty\), these probabilities converge to \(2/3\) and \(1/6\), respectively. The finite formulas quantify the exact effect of lattice-coordinate ties.

## Assumptions and scope

The paths are finite, unweighted and simple; both lengths count **vertices** rather than edges. Graph geodesic convexity requires containing **every** shortest path between any two vertices of a convex set. Rectangles include degenerate one-row, one-column and single-vertex rectangles. The empty convex set is included. The polynomial counts **subsets of the fixed labeled grid vertex set**; no quotient by graph automorphisms is taken. No result is claimed for graph products other than two paths, nor for online/Littlestone dimension.

## Proof

**1. Convex sets are rectangles.** The distance on the Cartesian path grid is
\[d((i,j),(i',j'))=|i-i'|+|j-j'|.\]
Its geodesic interval is the Cartesian product of the two coordinate intervals. Thus every product of coordinate intervals is convex. Conversely, let \(C\ne\varnothing\) be geodesically convex. For any \((i,j),(i',j')\in C\), its geodesic interval contains both crossed corners \((i,j')\) and \((i',j)\). Hence \(C\) is the product of its two projections. Both projections are intervals, because all coordinate values between two values occurring in a projection occur on geodesics between corresponding points of \(C\). Therefore \(C\) is a rectangle.

**2. Criterion for shattering.** For nonempty \(T\subseteq V\), let \(B(T)\) be its smallest coordinate rectangle. For a support \(S\) with at least two points, shattering implies that for each \(p\in S\) some rectangle contains \(S\setminus\{p\}\) but not \(p\); hence \(p\notin B(S\setminus\{p\})\). Conversely, for \(|S|\ge2\) assume this exclusion for every \(p\in S\). For every nonempty \(T\subseteq S\), any \(p\in S\setminus T\) is excluded from \(B(T)\subseteq B(S\setminus\{p\})\); hence \(B(T)\cap S=T\). The empty trace is obtained by the empty rectangle. The condition \(p\notin B(S\setminus\{p\})\) says precisely that \(p\) is a strictly unique coordinate minimum or maximum. For distinct pairs it always holds. For supports of size \(k\ge3\), there are at most four different strict coordinate extrema, giving \(k\le4\).

**3. Count shattered triples.** A three-point support fails the criterion if and only if one of its points lies in the rectangle spanned by the other two. Such a point is unique: if distinct \(p\) and \(q\) were each coordinatewise between the other point and a third point, then in both coordinates \(p\) and \(q\) would have to agree, a contradiction.

Use zero-based coordinates for this count. Fix the unique obstructing point \(b=(i,j)\), with \(0\le i<m\) and \(0\le j<n\). An unordered pair \(\{a,c\}\) spans \(b\) precisely when its endpoints lie in opposite weak quadrants: southwest/northeast, or northwest/southeast. Excluding \(b\), those two products contribute
\[
((i+1)(j+1)-1)((m-i)(n-j)-1)
\]
and
\[
((i+1)(n-j)-1)((m-i)(j+1)-1).
\]
Their intersection consists of pairs lying on the horizontal or vertical line through \(b\) with \(b\) strictly between the endpoints. Subtract exactly
\[i(m-1-i)+j(n-1-j).\]
Summing over \(i,j\), using
\[
\sum_{i=0}^{m-1}(i+1)(m-i)=\frac{m(m+1)(m+2)}6,
\qquad
\sum_{i=0}^{m-1}i(m-1-i)=\binom m3,
\]
and the corresponding identities for \(n\), yields the exact number of non-shattered triples
\[
2\frac{m(m+1)(m+2)}6\frac{n(n+1)(n+2)}6
-mn((m+1)(n+1)-2)-n\binom m3-m\binom n3.
\]
Subtracting from \(\binom{mn}{3}\) and simplifying gives
\[
[z^3]\Phi_{m,n}(z)=\frac{mn(m-1)(n-1)(2mn-m-n-4)}{18}.
\]
These identities remain valid for unit coordinate lengths, under the convention \(\binom{k}{3}=0\) when \(k<3\).

**4. Count shattered quadruples.** Each of four shattered points must have its own distinct one of the four strict extrema (left, right, bottom, top). Thus the support has uniquely named points \(L,R,B,T\), with \(x_L<x_B,x_T<x_R\) and \(y_B<y_L,y_R<y_T\). Fix the extreme coordinate values \(x_L=a<x_R=d\) and \(y_B=b<y_T=c\). There are exactly \((d-a-1)^2(c-b-1)^2\) choices for the two interior horizontal coordinates and two interior vertical coordinates. The points cannot coincide, and no support is counted twice since its four extreme labels and values are unique. Therefore
\[
[z^4]\Phi_{m,n}(z)=
\left(\sum_{0\le a<d<m}(d-a-1)^2\right)
\left(\sum_{0\le b<c<n}(c-b-1)^2\right).
\]
The first factor equals
\[\sum_{h=2}^{m-1}(m-h)(h-1)^2=\frac{m(m-1)^2(m-2)}{12},\]
and similarly for \(n\). Their product gives the displayed quartic coefficient. Its positivity is equivalent to \(m,n\ge3\). The cubic coefficient is positive precisely when \(m,n\ge2\) and \((m,n)\ne(2,2)\). The coefficient tests and the one-vertex boundary prove the VC-dimension cases.

**5. Limiting random-support probabilities.** As \(m,n\to\infty\), the cubic coefficient is asymptotic to \((mn)^3/9\), and the quartic coefficient to \((mn)^4/144\). Dividing by \(\binom{mn}{3}\sim(mn)^3/6\) and \(\binom{mn}{4}\sim(mn)^4/24\) gives \(2/3\) and \(1/6\).

## Verification

Run `python3 grid_shattering_check.py` with a standard Python 3 interpreter; no third-party libraries or network access are needed. The checker enumerates shortest-path convexity independently on small grids, computes every trace using all rectangles (not using the extrema criterion), compares those traces with the criterion, and verifies the coefficient formulas. Exhaustive trace comparisons include all supports of sizes one through four on ten grids up to \(5\times5\). It also separately enumerates all four-point supports on grids through \(8\times8\). The successfully replayed package returned `ALL_GRID_SHATTERING_CHECKS_PASS`. This finite verification is not used as the proof for unbounded \(m,n\).

For orientation, the exact coefficient vectors in degrees zero through four are \((1,6,15,2,0)\) for \(2\times3\), \((1,9,36,16,1)\) for \(3\times3\), \((1,16,120,160,36)\) for \(4\times4\), and \((1,25,300,800,400)\) for \(5\times5\).

## Relationship to prior work

The usual bound \(\operatorname{VCdim}=4\) for real planar axis-parallel rectangles, including the extremal-point obstruction, is classical; see Blum, Hopcroft and Kannan, *Foundations of Data Science*, Section 5.11.1 (2018). The Cartesian-product description of graph geodesic convexity is also already known; see Jiang, Pelayo and Pritikin (2004). Neither principle is claimed as new here. Thiessen and Gärtner's 2022 paper studies online learning of geodesically convex graph sets and provides general VC and mistake bounds; it also explicitly discusses a two-row grid, but does not state the present exact all-coefficient finite-grid census. The mathematical contribution assessed here is the explicit **full shattering enumerator**, including coordinate ties, narrow-grid transitions, and exact random-support proportions, rather than the textbook four-point upper bound.

## Limitations

The formulas count supports for the full convex-set concept class, **not** the growth function on an adversarially chosen support and **not** the Littlestone dimension. The global claim of historical priority cannot be certified by accessible literature search; equivalent enumerations in another terminology may exist. The 2004 Cartesian-product paper was available for abstract-level comparison, not complete-text verification. Independent scientific review has not been performed.

## References

1. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD (2022), DOI: 10.1007/978-3-031-26412-2_22. Full open-access conference preprint: https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2022/lncs13716/lncs13716354.pdf.
2. A. Blum, J. Hopcroft, and R. Kannan, *Foundations of Data Science* (2018), Section 5.11.1, pp. 149–150, https://www.cs.cornell.edu/jeh/book.
3. T. Jiang, I. M. Pelayo, and D. Pritikin, *Geodesic Convexity and Cartesian Products in Graphs* (2004), publicly accessible author abstract at https://www.researchgate.net/publication/249760576_Geodesic_Convexity_and_Cartesian_Products_in_Graphs.
