# Euler characteristic of toric Chow divisors depends only on ambient size and polytope vertices
## Finding
Let
\[
\mathcal A=\{a_1,\ldots,a_N\}\subset\mathbb Z^d
\]
be distinct lattice points whose affine span has dimension \(d\), and let
\[
P=\operatorname{conv}(\mathcal A).
\]
Write \(v\) for the number of vertices of \(P\). Let
\[
X_{\mathcal A}\subset\mathbb P^{N-1}
\]
be the closure of the monomial torus orbit determined by \(\mathcal A\), and assume
\[
d\le N-2.
\]
Its Chow divisor is
\[
Z_{\mathcal A}
=
\left\{
L\in\operatorname{Gr}(N-d-1,N):
\mathbb P(L)\cap X_{\mathcal A}\ne\varnothing
\right\}.
\]
Then
\[
\boxed{
\chi_{\mathrm{top}}(Z_{\mathcal A})
=
\binom{N}{d+1}
-
\binom{N-v}{N-d-1}.
}
\]
Equivalently,
\[
\boxed{
\chi_c\!\left(
\operatorname{Gr}(N-d-1,N)\setminus Z_{\mathcal A}
\right)
=
\binom{N-v}{N-d-1}.
}
\]
The binomial coefficient is interpreted as zero when its lower argument exceeds its upper argument.

Thus the Euler characteristic of the Chow divisor forgets the degree, normalized volume, triangulations, singularities, and all other lattice geometry of the toric embedding except the three integers \(N,d,v\).

Two standard families become especially simple. For the \(e\)-th Veronese embedding of \(\mathbb P^d\),
\[
N=\binom{d+e}{d},\qquad v=d+1,
\]
so
\[
\boxed{
\chi_{\mathrm{top}}(Z)=\binom{N}{d+1}-1.
}
\]
For a Segre embedding of a product of at least two positive-dimensional projective spaces, every monomial coordinate is a polytope vertex, so \(v=N\) and
\[
\boxed{
\chi_{\mathrm{top}}(Z)=\binom{N}{d+1},
}
\]
the Euler characteristic of the ambient Grassmannian.

## Assumptions and scope
The base field is \(\mathbb C\). The lattice points in \(\mathcal A\) are distinct, and \(X_{\mathcal A}\) is the projective torus-orbit closure in the coordinate embedding indexed by \(\mathcal A\). Normality and smoothness are not assumed.

The restriction \(d\le N-2\) excludes the degenerate case in which the Chow construction would parametrize projective spaces of negative dimension. The result concerns the ordinary topological Euler characteristic of the projective Chow divisor and the compactly supported Euler characteristic of its complement.

## Proof
Choose a one-parameter subgroup of the intrinsic algebraic torus of \(X_{\mathcal A}\) whose weights on the ambient homogeneous coordinates are pairwise distinct. This is possible because the points \(a_i\) are distinct: a generic integral linear functional separates them.

The induced action on
\[
G=\operatorname{Gr}(N-d-1,N)
\]
has isolated fixed points, namely the coordinate \((N-d-1)\)-planes. Hence
\[
\#G^{\mathbb C^*}=\binom{N}{N-d-1}=\binom{N}{d+1}.
\]

The fixed points of \(X_{\mathcal A}\) under the same generic one-parameter subgroup are exactly the coordinate points indexed by the vertices of \(P\). Indeed, the coordinate fixed points in the closure of a torus orbit are precisely the exposed extremal weights, equivalently the vertices of the weight polytope.

Let \(L_S\) be a coordinate fixed point of the Grassmannian, where
\[
S\subset\{1,\ldots,N\},
\qquad
|S|=N-d-1.
\]
Then
\[
L_S\in Z_{\mathcal A}
\]
if and only if \(S\) contains at least one vertex index of \(P\).

The forward implication uses projectivity. If
\[
\mathbb P(L_S)\cap X_{\mathcal A}\ne\varnothing,
\]
then this intersection is a nonempty closed \(\mathbb C^*\)-stable projective variety, so it contains a \(\mathbb C^*\)-fixed point. Every such fixed point of \(X_{\mathcal A}\) is a vertex coordinate point, and belonging to \(\mathbb P(L_S)\) means that its index lies in \(S\). The reverse implication is immediate because a vertex coordinate point indexed by \(S\) lies in both varieties.

Therefore the coordinate Grassmannian fixed points outside the Chow divisor are exactly the subsets \(S\) chosen entirely from the \(N-v\) nonvertex coordinates. Their number is
\[
\binom{N-v}{N-d-1}.
\]
Thus
\[
\# Z_{\mathcal A}^{\mathbb C^*}
=
\binom{N}{d+1}
-
\binom{N-v}{N-d-1}.
\]

For a complex projective algebraic variety with an algebraic \(\mathbb C^*\)-action,
\[
\chi_{\mathrm{top}}(Y)=\chi_{\mathrm{top}}(Y^{\mathbb C^*}).
\]
Applying this to \(Z_{\mathcal A}\) proves the first formula. Additivity and
\[
\chi_{\mathrm{top}}(G)=\binom{N}{N-d-1}
\]
give the complement formula.

## Verification
The bundled checker exhaustively enumerates every coordinate Grassmannian fixed point for all triples
\[
2\le N\le16,
\qquad
1\le d\le N-2,
\qquad
1\le v\le N,
\]
subject to the obvious feasibility inequalities, and compares the direct count of subsets meeting a distinguished \(v\)-element vertex set with the closed binomial formula.

It separately constructs standard finite toric supports for rational normal curves, Veronese surfaces, and product-simplex Segre embeddings, computes their convex-hull vertices by an elementary hull routine, and checks the corresponding specializations.

These finite calculations are regression evidence only. The all-parameter theorem is proved by the fixed-locus argument above.

## Relationship to prior work
Kapranov, Sturmfels, and Zelevinsky developed the Chow form and Chow polytope of a projective toric variety and identified the toric setting in terms of the weight configuration \(\mathcal A\) and its convex hull. Their work emphasizes Chow polytopes, regular triangulations, secondary polytopes, and resultants.

The classical Chow construction identifies \(Z(X)\) as the Grassmannian hypersurface of linear spaces meeting \(X\). Later work on Chow forms and coisotropic hypersurfaces develops determinantal representations, tropicalizations, duality, and equations.

Targeted searches for “Euler characteristic,” “Poincaré,” “topology,” and “fixed point” in the inspected archival Chow-polytope source found no such calculation. Searches combining “toric Chow divisor,” “Chow hypersurface,” “Grassmannian,” “Euler characteristic,” “fixed points,” and “vertices” did not locate the displayed formula or a stronger statement implying it.

The result is not the Euler characteristic of a divisor on the toric variety itself. It is the Euler characteristic of the Chow hypersurface inside a Grassmannian, a different parameter space.

## Limitations
Euler characteristic is coarse: the theorem does not determine Betti numbers, Hodge numbers, singularity type, the Chow-form degree, or the Chow polytope.

The proof uses a complex-algebraic one-parameter subgroup and topological Euler localization. No positive-characteristic analogue is claimed.

Because the proof becomes short once the fixed-point criterion is isolated, an unindexed or folklore equivalent remains a residual originality risk.

The earliest exact public date verified to day precision for the foundational journal article is 1 July 1992. An inspected 1991 proceedings note cites an earlier January 1991 technical report but does not provide a day, so no exact day has been invented for that earlier report.

## References
M. M. Kapranov, B. Sturmfels, and A. V. Zelevinsky, *Chow polytopes and general resultants*, Duke Mathematical Journal 67 (1992), 189--218, DOI 10.1215/S0012-7094-92-06707-X.

A. V. Zelevinsky, *Chow Polytopes*, RIMS Kokyuroku 773 (1991), 106--111. The note cites Technical Report 91-2, MSI, Cornell University, January 1991.

D. Eisenbud, F.-O. Schreyer, and J. Weyman, *Resultants and Chow forms via exterior syzygies*, arXiv:math/0111040, first submitted November 2001; Journal of the American Mathematical Society 16 (2003), 537--579.
