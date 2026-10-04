# Inscribed-quadrilateral collapse in strictly convex normed planes
## Finding
Let \(X\) be a real two-dimensional strictly convex normed space. Define
\[
J_{\mathrm{in}}(X)
=
\sup\left\{\sum_{1\le i<j\le4}\|x_i-x_j\|^2:
x_1,x_2,x_3,x_4\in S_X,\ \sum_{i=1}^4x_i=0\right\}
\]
and
\[
C'_{\mathrm{NJ}}(X)
=
\sup_{x,y\in S_X}
\frac{\|x+y\|^2+\|x-y\|^2}{4}.
\]
Then
\[
J_{\mathrm{in}}(X)=8+8C'_{\mathrm{NJ}}(X).
\]
Consequently, for every \(1\le p\le\infty\),
\[
J_{\mathrm{in}}(\ell_p^2)
=
8\left(1+2^{|2/p-1|}\right),
\]
where \(2/\infty=0\).

## Assumptions and scope
All spaces are real. The structural identity assumes that \(X\) is two-dimensional and strictly convex. The family \(\ell_p^2\) is strictly convex for \(1<p<\infty\); the two non-strict endpoints are handled separately. No assertion is made that the same reduction holds in dimension at least three.

## Proof
Write \(B_X\) for the unit ball and \(S_X=\partial B_X\).

First, a planar translate lemma is needed. If \(K\subset\mathbb R^2\) is a strictly convex compact convex body and \(t\ne0\), then \(\partial K\) and \(t+\partial K\) meet in at most two points. Choose affine coordinates in which \(t=(a,0)\) with \(a>0\). For an ordinate \(r\), write the horizontal section as
\[
K_r=[L(r),R(r)]
\]
whenever it is nonempty, and put \(w(r)=R(r)-L(r)\). Convexity gives that \(L\) is convex, \(R\) is concave, and hence \(w\) is concave. Away from the extreme ordinates, a common boundary point of \(K\) and \(t+K\) must be the right endpoint of \(K_r\) and the left endpoint of \((t+K)_r\); therefore it exists exactly when
\[
w(r)=a.
\]
A horizontal level can meet the graph of a concave function in more than two points only if that level contains a nontrivial interval. Such an interval is impossible here: if \(w\) were constant on an interval, then \(R=L+\text{constant}\), so \(L\) would be both convex and concave there and hence affine; the two corresponding boundary arcs would be line segments, contradicting strict convexity. Thus there are at most two common boundary points.

Now take an admissible quadruple \(x_1,x_2,x_3,x_4\in S_X\) with
\[
x_1+x_2+x_3+x_4=0.
\]
Put \(s=x_1+x_2=-x_3-x_4\). If \(s=0\), then \(x_2=-x_1\) and \(x_4=-x_3\), so the quadruple is already a union of two antipodal pairs.

Assume \(s\ne0\). A vector \(u\in S_X\) can occur in a unit pair with sum \(s\) exactly when
\[
u\in S_X\cap(s+S_X),
\]
because \(s-u\in S_X\) is equivalent, by central symmetry, to \(u-s\in S_X\). By the translate lemma this intersection has at most two points. If \(x_1\ne x_2\), the two points \(x_1,x_2\) exhaust it, so
\[
\{-x_3,-x_4\}=\{x_1,x_2\}.
\]
If \(x_1=x_2\), then \(s=2x_1\); strict convexity applied to the midpoint of any other unit pair with sum \(s\) forces that pair also to equal \(x_1,x_1\). Hence every admissible quadruple is, after relabelling,
\[
x,-x,y,-y
\]
with \(x,y\in S_X\).

For such a quadruple, the six squared pairwise distances sum to
\[
8+2\|x+y\|^2+2\|x-y\|^2.
\]
Taking the supremum over \(x,y\in S_X\) yields
\[
J_{\mathrm{in}}(X)=8+8C'_{\mathrm{NJ}}(X).
\]

For \(1<p<\infty\), Ciesielski and Płuciennik's exact formula for the upper modified \(n\)-th von Neumann--Jordan constant, specialized to \(n=2\) and dimension \(2\), gives
\[
C'_{\mathrm{NJ}}(\ell_p^2)
=
\begin{cases}
2^{2/p-1},&1<p\le2,\\
2^{1-2/p},&2\le p<\infty.
\end{cases}
\]
Substitution gives
\[
J_{\mathrm{in}}(\ell_p^2)
=
8\left(1+2^{|2/p-1|}\right).
\]

For \(p=1\), the four unit vectors \(\pm e_1,\pm e_2\) have all six mutual distances equal to \(2\), so the value is at least \(24\). For \(p=\infty\), the four vertices \((\pm1,\pm1)\) likewise have all six mutual distances equal to \(2\). Ahmad--Liu--Li prove the universal bound \(J_{\mathrm{in}}(X)\le24\), so both endpoint values are exactly \(24\), agreeing with the displayed formula.

## Verification
The planar translate lemma was reconstructed from horizontal sections rather than assumed. The reduction covers \(s=0\), \(s\ne0\) with distinct pair members, and the repeated-point case. The published modified von Neumann--Jordan formula was recomputed at \(n=2\). As a non-proof stress test, constrained numerical maximization in \(\ell_p^2\) over twenty deterministic starting points for each of \(p=3/2,3,4\) returned the predicted values to within \(10^{-12}\) or better. The infinite statement rests on the analytic proof, not on that finite computation.

## Relationship to prior work
Ahmad, Liu and Li introduced \(J_{\mathrm{in}}\), proved
\[
J_{\mathrm{in}}(X)\ge8C'_{\mathrm{NJ}}(X)+8,
\]
proved \(16\le J_{\mathrm{in}}(X)\le24\), and computed the two polygonal endpoint examples \(\ell_1^2\) and \(\ell_\infty^2\). Their paper does not identify a class on which the lower bound is always an equality and does not give the full \(\ell_p^2\) profile. Ciesielski and Płuciennik independently computed modified \(n\)-th von Neumann--Jordan constants for \(L^p\) and \(\ell_p\); their \(n=2\) theorem supplies the two-variable constant used after the planar reduction, but it does not concern \(J_{\mathrm{in}}\).

## Limitations
The collapse to antipodal pairs is essentially planar. In dimensions at least three, distinct centered chords of a strictly convex sphere can have the same midpoint, so the argument does not extend. The result does not determine \(J_{\mathrm{in}}(\ell_p^d)\) for \(d\ge3\). Literature searches cannot logically prove novelty; the remaining risk is an unindexed later source containing the same planar identity.

## References
1. A. Ahmad, Q. Liu, Y. Li, “Geometric Constants in Banach Spaces Related to the Inscribed Quadrilateral of Unit Balls,” *Symmetry* 13 (2021), 1294. DOI: 10.3390/sym13071294.
2. M. Ciesielski, R. Płuciennik, “On some modifications of n-th von Neumann--Jordan constant for Banach spaces,” *Banach Journal of Mathematical Analysis* 14 (2020), 650--673. DOI: 10.1007/s43037-019-00033-1; arXiv:1811.01652.
