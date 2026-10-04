# Normalization and boundary singular locus of a six-monomial toric surface
## Finding
Let
\[
A=\{{(0,0),(0,5),(1,2),(1,3),(5,0),(5,5)\}}
\]
be the support in Forsgård--de Wolff, Example 8.4, and let \(X_A\subset\mathbb P^5_{\mathbb C}\) be the projective closure of
\[
(x,y)\longmapsto [1:y^5:xy^2:xy^3:x^5:x^5y^5].
\]
Then the normalization of \(X_A\) is \(\mathbb P^1\times\mathbb P^1\). Its singular locus is exactly the toric boundary, a cycle of four projective lines. A generic point of each of those four lines has five distinct normalization preimages. Moreover, \(\deg(X_A)=50\).

## Assumptions and scope
All varieties are over \(\mathbb C\), and \(X_A\) means the reduced projective closure of the displayed torus image. Coordinates on the target are \([z_0:\dots:z_5]\). The claim concerns this projective toric surface associated to the exact six-point support of Example 8.4; it does not assert a new statement about the SONC equality proved in that source.

## Proof
Homogenizing the six monomials gives a morphism
\[
\nu:\mathbb P^1\times\mathbb P^1\longrightarrow\mathbb P^5
\]
with coordinates
\[
[X_0^5Y_0^5:X_0^5Y_1^5:X_0^4X_1Y_0^3Y_1^2:X_0^4X_1Y_0^2Y_1^3:X_1^5Y_0^5:X_1^5Y_1^5].
\]
There is no common zero, so this is everywhere defined. Its image is closed and contains the original torus image, hence it equals \(X_A\).

On the dense torus all six coordinates are nonzero, and the inverse is recovered by
\[
y=\frac{{z_3}}{{z_2}},\qquad x=\frac{{z_2^3}}{{z_0z_3^2}}.
\]
Thus \(\nu\) is birational and \(X_A\) is smooth on its dense torus.

The complement of the torus in \(\mathbb P^1\times\mathbb P^1\) consists of the four coordinate divisors. Their images are respectively
\[
L_{{x=0}}=V(z_2,z_3,z_4,z_5),\quad
L_{{x=\infty}}=V(z_0,z_1,z_2,z_3),
\]
\[
L_{{y=0}}=V(z_1,z_2,z_3,z_5),\quad
L_{{y=\infty}}=V(z_0,z_2,z_3,z_4).
\]
On each divisor only the two endpoint sections survive, and the restriction is \([u:v]\mapsto[u^5:v^5]\) onto the corresponding line. Therefore every fiber on the boundary is finite, while every torus fiber is a singleton. Since \(\nu\) is proper and quasi-finite, it is finite. The source \(\mathbb P^1\times\mathbb P^1\) is normal, so this finite birational morphism is the normalization of \(X_A\).

At a generic point of each boundary line, the fifth-power map has five distinct preimages. A regular local ring is normal, so such a point cannot be regular. The singular locus is closed, hence it contains all four boundary lines. Conversely the dense torus is smooth, so there are no other singular points. This proves that the singular locus is exactly the four-line cycle.

Finally \(\nu^*\mathcal O_{{X_A}}(1)=\mathcal O_{{\mathbb P^1\times\mathbb P^1}}(5,5)\). Birationality gives
\[
\deg(X_A)=(5H_1+5H_2)^2=50.
\]

## Verification
The included `artifacts/verify.py` checks the square Newton polytope and normalized area, that the exponent differences generate the full lattice, the exponent identities giving the torus inverse, the exact facet supports, lattice length five on every facet, and bidegree \((5,5)\) of all six homogenized sections. Its successful output is `VERIFY_OK`.

## Relationship to prior work
Forsgård--de Wolff introduce this exact support in Example 8.4 to show that its SONC cone equals its sparse nonnegativity cone; the displayed example and surrounding discussion describe the five possible SONC-support cells, not the normalization or singular locus of the associated projective toric surface. Targeted searches using the exact support matrix, the six-monomial map, “projective toric surface”, “normalization”, and “singular locus” located the source itself but no statement covering the result above. Standard facts about finite birational maps and normal varieties are used only as proof tools.

## Limitations
No scheme-theoretic conductor, local analytic equation, delta invariant, or singularity classification at the four line intersections is claimed. The five-preimage statement is generic along each line; at a corner of the four-line cycle the normalization fiber is a single point. The originality assessment is limited by the possibility of an obscure source indexed under a different description of this monomial surface.

## References
1. Jens Forsgård and Timo de Wolff, *The algebraic boundary of the SONC-cone*, arXiv:1905.04776, especially Theorem 8.1, Remark 8.2, and Example 8.4.
