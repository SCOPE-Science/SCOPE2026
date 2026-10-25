# Sharp planar lattice-width real-rootedness and the unique width-three exception

## Finding

For every full-dimensional lattice polygon \(P\subset\mathbb R^2\) of lattice width \(w(P)\ge3\), its Ehrhart \(h^*\)-polynomial has degree exactly two. Exactly one of the following holds:

1. \(h^*_P(t)\) has two distinct, strictly negative real roots.
2. \(P\) is affine-unimodularly equivalent to
\[
T=\operatorname{conv}\{(0,0),(1,0),(3,7)\},
\]
whose width is exactly three and whose Ehrhart numerator is
\[
h^*_T(t)=1+3t+3t^2.
\]
The exceptional polynomial has two nonreal conjugate roots \(-\tfrac12\pm\tfrac{\sqrt3}{6}i\).

Consequently **four is the smallest integer lattice width that uniformly guarantees two distinct negative real zeros** for planar lattice polygons. At width three the nonreal-rooted exception is unique up to affine-unimodular equivalence; there are no multiple-root exceptions.

## Assumptions and scope

A lattice polygon is a compact, full-dimensional convex polygon whose vertices lie in \(\mathbb Z^2\). Its lattice width is
\[
w(P)=\min_{u\in\mathbb Z^2\setminus\{0\}}
\bigl(\max_{x\in P}\langle u,x\rangle-\min_{x\in P}\langle u,x\rangle\bigr).
\]
For a lattice polygon this is a positive integer. Affine-unimodular equivalence means a transformation \(x\mapsto Ux+z\) with \(U\in\mathrm{GL}_2(\mathbb Z)\) and \(z\in\mathbb Z^2\). The Ehrhart numerator is defined by
\[
\sum_{k\ge0}\#(kP\cap\mathbb Z^2)t^k=\frac{h^*_P(t)}{(1-t)^3}.
\]
The conclusion concerns \(h^*\), **not** the roots of the Ehrhart counting polynomial. It uses the established planar Fejes-Tóth–Makai isominwidth inequality and the established bound for the lattice width of hollow planar convex bodies.

## Proof

Write \(I=\#(\operatorname{int}P\cap\mathbb Z^2)\), \(B=\#(\partial P\cap\mathbb Z^2)\), and \(A=\operatorname{area}(P)\). Pick's theorem gives \(A=I+B/2-1\). Ehrhart's planar counting formula, followed by the generating-series identity, yields
\[
 h^*_P(t)=1+(I+B-3)t+It^2.
\]
Because \(w(P)\ge3\), Hurkens' sharp planar hollow-body flatness theorem \(w(P)\le1+2/\sqrt3<3\) for \(I=0\) forces \(I\ge1\). Thus this polynomial has degree two and strictly positive coefficients.

Its discriminant is \(\Delta=(I+B-3)^2-4I\). Since \(B\ge3\), direct algebra gives
\[
\begin{array}{c|c}
B&\Delta\\\hline
3&I(I-4)\\
4&(I-1)^2\\
B\ge5&\Delta\ge I^2+4>0.
\end{array}
\]
For \(I\ge1\), therefore, \(\Delta\le0\) is possible only for the five pairs
\[
(I,B)\in\{(1,3),(2,3),(3,3),(4,3),(1,4)\}.
\]
The first three pairs with area below three, namely \((1,3),(2,3),(1,4)\), all have \(A\le5/2\). The sharp Fejes-Tóth–Makai inequality \(w(P)^2\le(8/3)A\) then gives \(w(P)^2\le20/3<9\), contradicting \(w(P)\ge3\).

It remains to analyze \((I,B)=(3,3)\) or \((4,3)\). Because \(B=3\), the polygon must be a triangle with three primitive edges. Its normalized area \(D=2A=2I+1\) is respectively seven or nine. By choosing a primitive edge and applying an affine-unimodular transformation, every such triangle can be represented as
\[
T_{D,a}=\operatorname{conv}\{(0,0),(1,0),(a,D)\},
\quad 0\le a<D,
\]
where \(\gcd(a,D)=\gcd(a-1,D)=1\). Thus \(D=7\) permits exactly \(a=2,3,4,5,6\); \(D=9\) permits exactly \(a=2,5,8\).

The following exact width comparisons complete the small classification. For \(D=7\), the triangles with \(a=2,4,6\) admit directions of width two: respectively \((1,0),(2,-1),(1,-1)\). The triangle \(T_{7,3}\) has width three. Indeed direction \((1,0)\) gives width three. Conversely any integer direction \((p,q)\) of width at most two would have \(|p|\le2\) and its three projected vertex values \(0,p,3p+7q\) within a common interval of length at most two. For \(p=0\), nonzero \(q\) gives span at least seven. For \(|p|=1\), the least span over integral \(q\) is three. For \(|p|=2\), the least span is again three. Thus no such direction exists. The remaining triangle \(T_{7,5}\) is equivalent to \(T_{7,3}\): the unimodular matrix
\[
U=\begin{pmatrix}5&-2\\7&-3\end{pmatrix}
\]
has determinant \(-1\) and maps the vertices \((0,0),(3,7),(1,0)\) to \((0,0),(1,0),(5,7)\).

For \(D=9\), the triangles \(T_{9,2}\), \(T_{9,5}\), and \(T_{9,8}\) each have a direction of width two, respectively \((1,0),(2,-1),(1,-1)\). Thus no double-root case survives at width three.

For \(T=T_{7,3}\), Pick's theorem gives \(I=3,B=3\); therefore \(h^*_T(t)=1+3t+3t^2\), with discriminant \(-3\). Its width-three property shows the threshold cannot be lowered. For every other \(P\) of width at least three, the preceding classification forces \(\Delta>0\). Since the degree-two polynomial has positive coefficients and constant term one, both real roots are strictly negative and distinct. This proves all assertions.

## Verification

Run the standalone script `verify_planar_width_roots.py` using Python 3. It independently enumerates the primitive Hermite-normal-form triangles of normalized areas seven and nine; searches primitive integral width directions using explicit finite bounds; checks the relevant discriminants; verifies the affine-unimodular matrix; and compares the first four lattice-point counts against Pick–Ehrhart predictions by direct enumeration. Expected terminal line:

`PLANAR_WIDTH_ROOTS_OK det7=5 det9=3 low_discriminant_pairs=5`

The unbounded part of the proof is the algebraic discriminant classification plus the cited universal isominwidth and flatness bounds. Finite enumeration only establishes the eight small Hermite-normal-form cases; it is not an enumeration of all lattice polygons.

## Relationship to prior work

Nill (2026, arXiv:2608.03635, Theorem 1.1) proved that in every fixed dimension sufficiently large lattice width forces distinct negative real \(h^*\)-roots, while noting his constants are probably far from optimal. The exact two-dimensional cutoff and the width-three exceptional orbit are **not** supplied by that theorem.

Averkov–Codenotti–Freyer–Huang (2026, arXiv:2604.27260, Theorem 1.1 and Eq. (1.2)) provide the sharp one-point flatness theorem and summarize the classical Fejes-Tóth–Makai lattice isominwidth bound; these are explicitly used as prior lemmas. Hofscheier–Nill–Öberg (2016/2018, arXiv:1609.09526) study lattice-triangle Ehrhart pairs, use Hermite normal forms and lattice width, and discuss the prime-area classification, but their stated conclusions do not classify \(h^*\)-root discriminants by lattice width. Ferroni–Higashitani (2023/2024, arXiv:2307.10852) survey \(h^*\)-real-rootedness and related families without giving this planar width-three rigidity.

## Limitations

This is an exact planar statement only. It does not estimate the optimal threshold in dimensions at least three or for local/box \(h^*\)-polynomials. The elementary form of the proof makes historical priority uncertain: a sharp planar cutoff or equivalent small-triangle classification could have been observed in unindexed literature. Its universal conclusion relies on two published geometric inequalities rather than on an independent reproof of those inequalities. No independent external audit has been performed.

## References

1. Benjamin Nill, *Lattice polytopes of large width have real-rooted Ehrhart \(h^*\)-polynomials*, arXiv:2608.03635, first public 4 August 2026, Theorem 1.1 and remarks on constants.
2. Gennadiy Averkov, Giulia Codenotti, Ansgar Freyer, Kyle Huang, *Exact Flatness Constant for One-Point Convex Bodies and the Discrete Isominwidth Problem: The Planar Case*, arXiv:2604.27260, first public 29 April 2026, Theorem 1.1, Theorem A, and Eq. (1.2), which cites Fejes-Tóth and Makai.
3. Johannes Hofscheier, Benjamin Nill, Dennis Öberg, *On Ehrhart polynomials of lattice triangles*, arXiv:1609.09526 (2016), *Electronic Journal of Combinatorics* 25(1), article P1.3 (2018), especially Section 1, Remark 1.4 and Section 2.
4. Luis Ferroni, Akihiro Higashitani, *Examples and counterexamples in Ehrhart theory*, arXiv:2307.10852 (2023), survey version published 2024, Sections 1 and 4.
