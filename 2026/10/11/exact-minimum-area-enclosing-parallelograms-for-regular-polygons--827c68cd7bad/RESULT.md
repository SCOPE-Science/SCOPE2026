# Exact minimum-area enclosing parallelograms for regular polygons
## Finding
Let \(P_n\subset\mathbb R^2\) be a regular \(n\)-gon of circumradius \(R\), with \(n\ge3\). Let \(M(P_n)\) denote the smallest area of a parallelogram containing \(P_n\). Then
\[
\boxed{
M(P_n)=
\begin{cases}
4R^2\cos^2(\pi/n),&n\equiv0\pmod4,\\[4pt]
4R^2\cos(\pi/n),&n\equiv2\pmod4,\\[4pt]
4R^2\cos^3(\pi/(2n)),&n\ \text{odd}.
\end{cases}}
\tag{1}
\]

A minimum is attained by taking the two adjacent side directions of the enclosing parallelogram from the side directions of \(P_n\), with their angle as close as possible to \(\pi/2\).

Thus the minimum-area enclosure has a genuine arithmetic split. In particular,
\[
\frac{M(P_n)}{4R^2}
=
\begin{cases}
1-\pi^2/n^2+O(n^{-4}),&n\equiv0\pmod4,\\
1-\pi^2/(2n^2)+O(n^{-4}),&n\equiv2\pmod4,\\
1-3\pi^2/(8n^2)+O(n^{-4}),&n\ \text{odd}.
\end{cases}
\tag{2}
\]

## Assumptions and scope
A minimum-area enclosing parallelogram means a Euclidean parallelogram containing the whole polygon; no restriction to rectangles, rhombi, or homothetic copies is imposed.

For a convex body \(K\), if two adjacent sides of an enclosing parallelogram have line directions making an angle \(\phi\in(0,\pi)\), and if the widths of \(K\) perpendicular to those sides are \(w_1,w_2\), then the unique smallest parallelogram with those two directions has area
\[
\frac{w_1w_2}{\sin\phi}.
\tag{3}
\]

The structural input is the classical edge-contact lemma for minimum enclosing parallelograms: for a convex polygon there is a minimum-area enclosing parallelogram such that one side from each opposite pair contains a whole edge of the polygon. Rote gives a proof and explicitly attributes the lemma to the earlier Schwarz--Teich--Welzl--Evans algorithm.

## Proof
Put
\[
a=\frac{\pi}{n}.
\]
The directions of consecutive sides of \(P_n\), considered modulo \(\pi\), differ by
\[
2a.
\tag{4}
\]

By the edge-contact lemma, at least one global minimum may be chosen so that its two adjacent side directions are side directions of \(P_n\). Hence it suffices to evaluate (3) on pairs of polygon-side directions.

First suppose \(n\) is even. Opposite sides of \(P_n\) are parallel, and the distance between the two supporting lines parallel to any side is twice the apothem:
\[
w=2R\cos a.
\tag{5}
\]
Thus every edge-aligned candidate with mutual angle \(\phi\) has area
\[
\frac{4R^2\cos^2 a}{\sin\phi}.
\tag{6}
\]
If \(4\mid n\), the side-direction lattice contains a right angle, so
\[
\max\sin\phi=1,
\]
and (6) gives
\[
M(P_n)=4R^2\cos^2 a.
\]

If
\[
n\equiv2\pmod4,
\]
the closest side-direction separations to \(\pi/2\) differ from it by \(a\). Therefore
\[
\max\sin\phi=\cos a,
\]
and (6) gives
\[
M(P_n)=4R^2\cos a.
\]

Now suppose \(n\) is odd. Take an outward unit normal to a side. In that direction the supporting value is the apothem
\[
R\cos a.
\]
Because \(n\) is odd, the opposite normal points exactly toward a vertex of \(P_n\), so the opposite supporting value is \(R\). Therefore the width perpendicular to every side is
\[
w=R(1+\cos a)
=2R\cos^2\frac a2.
\tag{7}
\]
Among multiples of the side-direction step \(2a\), the closest directions to a right angle differ from \(\pi/2\) by \(a/2\). Hence
\[
\max\sin\phi=\cos\frac a2.
\tag{8}
\]
Substituting (7)--(8) into (3) yields
\[
M(P_n)
=
\frac{4R^2\cos^4(a/2)}{\cos(a/2)}
=
4R^2\cos^3\frac a2.
\]
This proves (1).

Finally, the three expansions in (2) follow from the Taylor expansions of
\[
\cos^2 a,\qquad
\cos a,\qquad
\cos^3(a/2).
\]

## Verification
The bundled `verify.py` checks the complete finite reduction supplied by the edge-contact lemma.

For each \(3\le n\le300\), it computes the width perpendicular to a side directly from all vertices, enumerates every pair of side directions, and checks that the smallest area obtained from
\[
w_1w_2/\sin\phi
\]
agrees with (1).

It separately checks the claimed maximum-sine values in all three residue classes and compares the exact formulas with direct support-line computations.

The finite sweep is diagnostic only. The all-\(n\) theorem follows from the published edge-contact lemma and the exact width/angle calculation above.

## Relationship to prior work
Aggarwal, Chang and Yap gave an algorithm for the more general problem of a minimum-area convex \(k\)-gon circumscribing a convex polygon. That problem does not impose the parallelogram constraint.

Schwarz, Teich, Welzl and Evans later gave a linear-time algorithm specifically for a minimum-area enclosing parallelogram. A later complete treatment by Rote reproduces the crucial structural lemma: a minimum exists in which one side from each opposite pair contains an edge of the input polygon. This reduces the regular-polygon problem to a finite trigonometric optimization.

The inspected full treatment develops the general algorithm and its optimality certificate, but does not state the regular-\(n\) formula (1) or the three asymptotic residue regimes (2). Candidate-specific searches under minimum/smallest enclosing parallelogram, circumscribed parallelogram, regular polygon, pentagon, hexagon, and the cosine fingerprints in (1) did not locate an implication-equivalent closed form.

The general 1985 circumscribing-\(k\)-gon paper and the 1994--1995 minimum-parallelogram sources remain the closest historical literature. The latter primary report was not retrievable in full text during this check; the structural lemma used here was instead materially verified in Rote's later proof, where it is explicitly attributed to the original report.

## Limitations
The result concerns minimum area, not minimum perimeter.

It gives the sharp value and explicit optimal direction classes, but does not classify every minimum parallelogram in degenerate contact descriptions.

The key structural lemma is prior work; the new content is the all-\(n\) exact evaluation and its arithmetic asymptotics.

Because the remaining calculation is elementary after the edge-contact reduction, an unindexed regular-polygon specialization in older computational-geometry notes remains the main originality risk.

## References
1. A. Aggarwal, J.-S. Chang, and C. K. Yap, *Minimum area circumscribing polygons*, *The Visual Computer* 1 (1985), 112--117. DOI: 10.1007/BF01898354.
2. C. Schwarz, J. Teich, E. Welzl, and B. L. Evans, *On Finding a Minimal Enclosing Parallelogram*, International Computer Science Institute technical report TR-94-036, 1994; conference version with A. Vainshtein, *Minimal Enclosing Parallelogram with Application*, SCG 1995. DOI: 10.1145/220279.220338.
3. G. Rote, *The Largest Contained Quadrilateral and the Smallest Enclosing Parallelogram of a Convex Polygon*, arXiv:1905.11203.
4. M. Lassak, *Approximation of convex bodies by axially symmetric bodies*, *Proceedings of the American Mathematical Society* 130 (2002), 3075--3084. DOI: 10.1090/S0002-9939-02-06404-3.
