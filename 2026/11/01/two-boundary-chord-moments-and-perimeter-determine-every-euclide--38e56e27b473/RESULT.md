# Two boundary chord moments and perimeter determine every Euclidean triangle

## Finding
Let \(T\) be any nondegenerate Euclidean triangle with side lengths \(a,b,c>0\), perimeter \(P=a+b+c\), and area \(A>0\). Let \(X,Y\) be independent points distributed uniformly by arclength along the three sides, and put
\[
M_2=\mathbb E\|X-Y\|^2,\qquad M_4=\mathbb E\|X-Y\|^4.
\]
Then the three scalar measurements \(P,M_2,M_4\) uniquely determine the unordered triple of side lengths, hence \(T\) up to Euclidean congruence. Explicitly,
\[
A^2=\frac{P^4}{48}-\frac{P^2M_2}{2}>0,
\qquad Q:=ab+bc+ca=\frac{9P^2}{4A^2}\left(M_4-\frac{P^2M_2}{2}+\frac{P^4}{60}\right),
\]
\[
U:=abc=P\left(M_2-\frac{P^2}{6}+\frac Q2\right).
\]
The three side lengths are precisely the roots, counted with multiplicity, of
\[
z^3-Pz^2+Qz-U=0.
\]
In particular, no genericity, non-isosceles, acute-angle or distinct-side assumption is needed.

The second moment alone, even together with the perimeter, does **not** determine the triangle: it only determines its area. The fourth moment is a strictly discriminating coordinate along each positive-area, fixed-perimeter, fixed-area family. Indeed, whenever \(T_1,T_2\) share \(P,A\), writing \(Q_i=a_ib_i+b_ic_i+c_ia_i\),
\[
M_4(T_1)-M_4(T_2)=\frac{4A^2}{9P^2}(Q_1-Q_2).
\]
Thus the coefficient of discrimination vanishes at precisely the zero-area boundary; this equality is an exact conditioning identity, not merely an asymptotic estimate.

## Assumptions and scope
Here uniform boundary sampling means normalized one-dimensional Hausdorff/arclength measure on the three **Euclidean straight sides**, not area-uniform interior sampling, uniform vertices, kinematic random-line chords, or shortest-path distance along the perimeter. The random distance is the ordinary Euclidean norm of the point difference. The triangle is nondegenerate (strict triangle inequalities), \(P>0\), and both moments are exact population moments; the result includes scalene, isosceles, and equilateral cases.

The formula gives a complete effective feasibility criterion for candidate \((P,M_2,M_4)\): calculate \(A^2,Q,U\) by the displayed expressions; the data are attainable precisely when \(P>0\), \(A^2>0\), and the displayed cubic has three real positive roots, counted with multiplicity, satisfying the strict triangle inequalities. The necessity and sufficiency follow because these reconstructed roots have exactly the specified moments by the identities below. No claim is made for degenerate triangles or noisy measurements.

## Proof
Write \(Q=ab+bc+ca\), \(U=abc\). Condition on the two edges containing \(X\) and \(Y\). Edge \(e\) of length \(\ell_e\) is selected with probability \(\ell_e/P\), and conditional coordinates on the segment are independent uniform parameters on \([0,1]\).

For both points on one edge of length \(\ell\), direct integration yields
\[
\mathbb E(\|X-Y\|^2\mid e,e)=\frac{\ell^2}{6},\qquad
\mathbb E(\|X-Y\|^4\mid e,e)=\frac{\ell^4}{15}.
\]
For different edges of lengths \(u,v\) sharing a vertex and with opposite triangle side of length \(w\), their angular cosine is \(\eta=(u^2+v^2-w^2)/(2uv)\). For independent uniform parameters \(S,T\), their squared Euclidean separation is \(u^2S^2+v^2T^2-2uv\eta ST\). Direct polynomial integration gives
\[
\begin{aligned}
\mathbb E(D^2\mid u,v)&=\frac{u^2+v^2}{3}-\frac{uv\eta}{2},\\
\mathbb E(D^4\mid u,v)&=\frac{u^4+v^4}{5}
+\frac{2u^2v^2(1+2\eta^2)}9
-\frac{uv\eta(u^2+v^2)}2.
\end{aligned}
\]
In the unconditional mixture, same-edge pairs have weights \(a^2/P^2,b^2/P^2,c^2/P^2\), while each unordered distinct-edge pair of lengths \(u,v\) has weight \(2uv/P^2\). Summing the displayed integrals, using the cosine law, and collecting symmetric terms yields the exact identities
\[
M_2=\frac1P\left(\frac{P^3}{6}-\frac{PQ}{2}+U\right),
\]
\[
M_4=\frac1P\left(\frac{P^5}{15}-\frac{5P^3Q}{18}
+\frac{P^2U}{2}+\frac{PQ^2}{9}-\frac{2QU}{9}\right).
\]
These identities are verified by the standalone exact symbolic integrator, but follow solely from the elementary integrals and hold for all positive side triples satisfying the triangle inequalities.

Heron's formula is equivalently
\[
16A^2=-P^4+4P^2Q-8PU.
\]
Combining this identity with the formula for \(M_2\) eliminates \(Q,U\) to give
\[
M_2=\frac{P^2}{24}-\frac{2A^2}{P^2}.
\]
Next eliminate \(U=P(M_2-P^2/6+Q/2)\) from \(M_4\). The terms quadratic in \(Q\) cancel, leaving
\[
M_4=\frac{P^2M_2}{2}-\frac{P^4}{60}
+\frac{4A^2Q}{9P^2}.
\]
For every nondegenerate triangle \(A^2>0\), so this equation solves uniquely for \(Q\), then the second-moment equation solves uniquely for \(U\). The monic polynomial \((z-a)(z-b)(z-c)=z^3-Pz^2+Qz-U\) therefore recovers the full side multiset. Side-side-side congruence proves the inverse theorem, including repeated roots. Substituting the recovered side lengths into the identities proves the feasibility criterion.

To show that the fourth moment contributes genuinely new information, compare \(T_1\) with sides \((3,4,5)\) and \(T_2\) with sides
\[
\left(\frac92,\frac{15-\sqrt{17}}4,\frac{15+\sqrt{17}}4\right).
\]
Both have \(P=12\), \(A=6\), and \(M_2=11/2\), yet their side multisets are different. Exact substitution yields respectively \(M_4=2503/45\) and \(M_4=10007/180\), differing by \(1/36\). The common-perimeter common-area equality for \(M_2\) is therefore insufficient, while \(M_4\) separates these examples.

At \(A=0\) the underlying boundary measure degenerates to uniform measure on a segment, independently of the position of the intermediate collinear vertex, and the coefficient \(4A^2/(9P^2)\) tends to zero. Thus the restriction to nondegenerate triangles is essential for this reconstruction mechanism.

## Verification
Run `python verify.py` with SymPy available. The script independently integrates each ordered edge pair in a coordinate-free Gram representation, verifies both symmetric moment polynomials and Heron's identity by exact symbolic simplification, verifies the inverse algebra identically, and checks the explicit two-triangle example with exact algebraic numbers. The completed execution printed:

`VERIFY_OK symbolic_2nd_and_4th_moments, Heron, inversion, exact_equal_area_example`

These are exact polynomial identity checks supplementing the displayed proof, not a substitute for the general argument; there is no finite enumeration standing in for a universal assertion. The three moment inputs have respective physical dimensions length, squared length, and fourth power of length, and every reconstruction formula respects those dimensions.

## Relationship to prior work
The established boundary second-moment formula for triangles ("Exact second-moment boundary gap for arbitrary Euclidean triangles," public research record, 2026) agrees with the formula for \(M_2\) above. It determines area from perimeter and the second moment, **not** the remaining side-shape parameter. The fourth-moment identity and the two-moment inverse classification are the distinct results retained here.

Tong, Ahmadi and Pan (arXiv:1312.2498v1, 2013) analyze two *area-uniform interior* points in arbitrary triangles and adjacent triangles, using chord length distributions. Their measure is different from arclength-uniform endpoint sampling and their results do not assert this finite-statistic boundary inverse.

Gates (1982) recognizes triangles from odd moments of a *kinematic random-line chord-length distribution*. Gasparyan and Ohanyan (2013) recognize triangles using orientation-dependent covariograms/chord distributions. The geometric object is the same, but neither source's cited statement concerns the second and fourth moments of a chord defined by two independent arclength-uniform boundary points. A richer invariant for a different sampling law is not an implication of the explicit two-moment formula here. The complete Gates article and Gasparyan--Ohanyan manuscript were not available for full inspection; these remain historical-priority risks rather than evidence of novelty.

An earlier complete three-even-moment inverse result for *area-uniform interior* points of triangles also has different premises, and does not yield the boundary calculation merely by changing labels. Search and record comparisons did not identify matching coverage; that does not certify historical priority.

## Limitations
This is a two-moment inverse theorem **conditional on knowing the perimeter**, not a claim that two moments alone identify all three metric scale/shape parameters. The inversion becomes poorly conditioned as the area tends to zero, as indicated by its exact coefficient, and no noise amplification bounds for individual roots, sampling-error rates, or extensions to general polygons are proved. The formal checks are reproducible but not independent mathematical validation. Historical originality is provisional pending fuller coverage of inaccessible sources.

## References
1. F. Tong, M. Ahmadi, J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498v1, first posted 2013-11-29. https://arxiv.org/abs/1312.2498
2. J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873–879. DOI:10.2307/3213843.
3. A. Gasparyan, V. K. Ohanyan, *Recognition of triangles by covariogram*, Journal of Contemporary Mathematical Analysis 48 (2013), 110–122. DOI:10.3103/S1068362313030023.
4. *Exact second-moment boundary gap for arbitrary Euclidean triangles*, published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-second-moment-boundary-gap-for-arbitrary-euclidean-triangl--d886b40f95a8.
