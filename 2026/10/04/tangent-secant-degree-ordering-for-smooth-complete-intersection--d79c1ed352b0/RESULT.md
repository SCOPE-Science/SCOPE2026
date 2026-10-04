# Tangent–secant degree ordering for smooth complete-intersection curves
## Finding
Let \(C\subset\mathbb P^N_{\mathbb C}\), \(N\ge4\), be a smooth complete-intersection curve of multidegree \((d_1,\ldots,d_{N-1})\), with every \(d_i\ge2\). Put
\[
D=\prod_i d_i,\qquad S=\sum_i d_i.
\]
Then
\[
\deg\operatorname{Tan}(C)=D(S-N+1)
\]
and
\[
\deg\operatorname{Sec}(C)=\frac D2(D-S+N-2).
\]
The complete ordering classification is
\[
\deg\operatorname{Sec}(C)\le \deg\operatorname{Tan}(C)
\]
if and only if \(N=4\) and, after reordering, the multidegree is one of
\[
(2,2,2),\quad (2,2,3),\quad (2,2,4).
\]
Equality occurs if and only if the multidegree is \((2,2,4)\). The corresponding degree pairs \((\deg\operatorname{Sec}(C),\deg\operatorname{Tan}(C))\) are respectively
\[
(16,24),\quad (42,48),\quad (80,80).
\]
Every other smooth complete-intersection curve in \(\mathbb P^N\) with \(N\ge4\) and all defining degrees at least two has
\[
\deg\operatorname{Sec}(C)>\deg\operatorname{Tan}(C).
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The curve is smooth, nondegenerate, and a complete intersection of \(N-1\) hypersurfaces in \(\mathbb P^N\), with \(N\ge4\) and \(d_i\ge2\). Here \(\operatorname{Tan}(C)\) is the tangent developable and \(\operatorname{Sec}(C)\) is the first secant variety. The statement compares their projective degrees; it does not assert an inclusion between the two varieties beyond the usual containment of tangent lines in the closure defining the secant variety.

## Proof
For a smooth non-plane curve of degree \(D\) and genus \(g\), the classical tangent-degree formula recorded by Achilles, Manaresi, and Schenzel is
\[
\deg\operatorname{Tan}(C)=2D+2g-2.
\]
For a smooth nondegenerate curve in \(\mathbb P^N\) with \(N\ge4\), their secant-degree formula specializes to
\[
\deg\operatorname{Sec}(C)=\binom{D-1}{2}-g.
\]
Adjunction for a smooth complete-intersection curve gives
\[
2g-2=D(S-N-1).
\]
Substitution yields
\[
\deg\operatorname{Tan}(C)=D(S-N+1)
\]
and
\[
\deg\operatorname{Sec}(C)
=\frac{(D-1)(D-2)}2-1-\frac D2(S-N-1)
=\frac D2(D-S+N-2).
\]

Since \(D>0\), the inequality \(\deg\operatorname{Sec}(C)\le\deg\operatorname{Tan}(C)\) is equivalent to
\[
D\le 3S-3N+4.
\]
Write \(m=N-1\) and \(y_i=d_i-1\). Then \(m\ge3\), each \(y_i\ge1\), and the inequality becomes
\[
\prod_{i=1}^m(y_i+1)\le 3\sum_{i=1}^m y_i+1.
\]
Let
\[
F(y_1,\ldots,y_m)=\prod_{i=1}^m(y_i+1)-3\sum_{i=1}^m y_i-1.
\]
Increasing one \(y_i\) by one changes \(F\) by
\[
\prod_{j\ne i}(y_j+1)-3.
\]
For \(m\ge4\), this increment is at least \(2^{m-1}-3>0\), so \(F\) is minimized at \((1,\ldots,1)\). There
\[
F(1,\ldots,1)=2^m-3m-1,
\]
which is positive at \(m=4\) and strictly increases thereafter. Hence no solution exists for \(m\ge4\).

It remains to take \(m=3\) and order \(1\le y_1\le y_2\le y_3\). The same increment is positive, so if \(y_1\ge2\), the minimum is at \((2,2,2)\), where \(F=8>0\). Thus \(y_1=1\). If \(y_2\ge2\), the minimum at \((1,2,2)\) has \(F=2>0\), so \(y_2=1\). The remaining inequality is
\[
4(y_3+1)\le3(y_3+2)+1,
\]
equivalently \(y_3\le3\). Therefore the only possibilities are \((y_1,y_2,y_3)=(1,1,1),(1,1,2),(1,1,3)\), giving multidegrees \((2,2,2),(2,2,3),(2,2,4)\). The final inequality is an equality exactly when \(y_3=3\), proving uniqueness of \((2,2,4)\).

## Verification
A standalone exact-integer checker recomputes the adjunction-specialized degree formulas and exhaustively tests all nondecreasing multidegrees with \(4\le N\le9\) and \(2\le d_i\le12\). It checks 75,504 tuples and finds exactly the three predicted cases with secant degree at most tangent degree, with equality only for \((2,2,4)\). This finite replay is regression evidence only; the proof above is uniform for all allowed \(N\) and multidegrees.

## Relationship to prior work
Achilles, Manaresi, and Schenzel give the general tangent- and secant-degree formulas for non-plane curves and prove the secant formula using the Stückrad–Vogel self-intersection cycle. Their full text was inspected at the theorem and proposition level. Their paper does not state the complete-intersection ordering classification above; its occurrences of complete intersections concern singular examples and local computations. Exact-statement and implication searches for a tangent-versus-secant degree classification of smooth complete-intersection curves did not locate a source covering the three exceptional multidegrees or the unique equality case.

The result is not implied by the previously recorded complete-intersection dual-degree collision result: projective dual degree in \(\mathbb P^3\) is a different invariant from the degrees of tangent and first secant varieties in \(\mathbb P^N\), and the present theorem ranges over every codimension \(N-1\ge3\).

## Limitations
The theorem is restricted to smooth complete-intersection curves over \(\mathbb C\), with all defining degrees at least two and ambient dimension at least four. Singular curves introduce local correction terms in both degree formulas. Curves in \(\mathbb P^3\) are excluded because their first secant variety fills the ambient space and the relevant invariant in the cited formula is instead the number of secants through a general point. The literature search cannot exclude an unindexed classical source that states the same ordering classification explicitly.

## References
R. Achilles, M. Manaresi, P. Schenzel, *A Degree Formula for Secant Varieties of Curves*, Proceedings of the Edinburgh Mathematical Society 57 (2014), 305–322. DOI: 10.1017/S0013091513000497. Published online 21 August 2013.

The adjunction formula for smooth complete intersections is used in its standard form.
