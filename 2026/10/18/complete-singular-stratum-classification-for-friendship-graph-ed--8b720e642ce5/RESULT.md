# Complete singular-stratum classification for friendship-graph edge toric varieties

## Finding
For each integer \(m\ge3\), let \(F_m\) be the friendship graph: \(m\) triangles \(\{o,a_i,b_i\}\), indexed by \(1\le i\le m\), sharing precisely their central vertex \(o\). Let \(P_m\) be its *edge polytope*, the convex hull of the vectors \(e_u+e_v\) for graph edges \(\{u,v\}\). The integral affine hyperplane containing \(P_m\) is \(\sum x_v=2\). Let \(X_m\) be the normal projective toric variety defined by its normal fan, over an algebraically closed field of arbitrary characteristic.

Delete the central coordinate from the affine lattice. Write \(A_i=e_{i,a}\), \(B_i=e_{i,b}\), and \(C_i=e_{i,a}+e_{i,b}\) in \(\mathbb Z^{2m}\). Then
\[
P_m=\operatorname{conv}\{A_i,B_i,C_i:1\le i\le m\},\qquad \dim P_m=2m.
\]
For a bit \(\epsilon_i\in\{a,b\}\), put \(E_i^{\epsilon_i}=A_i\) or \(B_i\), as indicated. Three families of *faces* determine the complete reduced singular locus.

**Square family.** Given \(1\le i<j\le m\) and \(\epsilon\in\{a,b\}^{[m]\setminus\{i,j\}}\), let
\[
F^{\square}_{ij,\epsilon}=\operatorname{conv}\bigl(\{C_i,C_j\}\cup\{C_k,E_k^{\epsilon_k}:k\notin\{i,j\}\}\bigr).
\]
There are \(\binom m2 2^{m-2}\) such faces. Each has dimension \(2m-3\).

**Flip-zero family.** Given \(1\le j\le m\) and \(\epsilon\in\{a,b\}^{[m]\setminus\{j\}}\), let
\[
F^{\mathrm{flip}}_{j,\epsilon}=\operatorname{conv}\{C_k,E_k^{\epsilon_k}:k\ne j\}.
\]
There are \(m2^{m-1}\) such faces, each of dimension \(2m-3\).

**Total-choice family.** Given \(\epsilon\in\{a,b\}^m\), let
\[
F^{\mathrm{Seg}}_{\epsilon}=\operatorname{conv}\{E_i^{\epsilon_i}:1\le i\le m\}.
\]
There are \(2^m\) such simplex faces, each of dimension \(m-1\).

For any face \(F\), let \(\sigma_F\) be its normal cone and \(Y_F=V(\sigma_F)\) its torus-orbit closure in \(X_m\). Then, as reduced closed subsets,
\[
\operatorname{Sing}(X_m)_{\mathrm{red}}=
\bigcup_{i<j,\epsilon}Y_{F^\square_{ij,\epsilon}}
\ \cup\ \bigcup_{j,\epsilon}Y_{F^{\mathrm{flip}}_{j,\epsilon}}
\ \cup\ \bigcup_{\epsilon}Y_{F^{\mathrm{Seg}}_{\epsilon}}.
\]
The displayed orbit closures are pairwise distinct and are exactly the irreducible components. The total number is
\[
\boxed{\binom m2 2^{m-2}+m2^{m-1}+2^m
=2^{m-3}(m^2+3m+8)}.
\]
The first two families have codimension three and generic transverse ordinary threefold nodes \(uv-wz=0\), of Hilbert--Samuel multiplicity two. The third has codimension \(m+1\) and generic transverse rank-one \(2\times m\) matrix variety, defined by all \(2\times2\) minors, of multiplicity \(m\). Its generic points are not \(\mathbb Q\)-Gorenstein when \(m\ge3\); the two conifold families are Gorenstein at their generic points. Thus the reduced singular locus is not equidimensional for \(m\ge3\).

All simplicial normal cones are unimodular. In particular the singular support equals the non-\(\mathbb Q\)-factorial support. Every one of the \(3m\) torus-fixed points is singular.

## Assumptions and scope
The toric variety here is the **normal-fan variety** of the edge polytope, not the affine homogeneous graph-edge cone. The projection deleting \(o\)'s coordinate is an integral affine lattice isomorphism because \(\sum x_v=2\). The base field is algebraically closed but its characteristic is unrestricted. The statement classifies the reduced singular support and generic transverse models along its irreducible components; it makes no claim about the embedded/nonreduced singular scheme or analytic singularities at every intersection point. The case \(m=2\) is used below only as a consistency check; the new all-parameter classification is stated for \(m\ge3\).

## Proof
**1. Exact irredundant facets.** Write a point in the affine lattice as nonnegative coordinates \((x_{i,a},x_{i,b})\). Its membership in \(P_m\) is equivalent to
\[
\begin{gathered}
x_{i,a}\ge0,\quad x_{i,b}\ge0\quad(1\le i\le m),\\
\sum_{i=1}^m(x_{i,a}+x_{i,b})\ge1,\\
\sum_{i=1}^m x_{i,\epsilon_i}\le1
\quad\text{for every }\epsilon\in\{a,b\}^m.
\end{gathered}
\]
Necessity follows by evaluating each inequality on \(A_i,B_i,C_i\). Conversely the choice inequalities say \(\sum_i\max(x_{i,a},x_{i,b})\le1\). Choose \(\lambda_i\) between \(\max(x_{i,a},x_{i,b})\) and \(x_{i,a}+x_{i,b}\), with \(\sum_i\lambda_i=1\), possible by the sum bounds. The block \((x_{i,a},x_{i,b})\) belongs to \(\lambda_i\operatorname{conv}\{(1,0),(0,1),(1,1)\}\), proving sufficiency. For \(m\ge2\), the equality vertices for each coordinate inequality, the total-sum inequality, and every choice inequality span affine hyperplanes of dimension \(2m-1\). More specifically, the total equality has all \(2m\) standard-basis vertices, each choice equality has the \(2m\) linearly independent vertices \(C_i,E_i^{\epsilon_i}\), and a coordinate-zero equality contains the corresponding other spoke vertex together with all vertices in the remaining \(m-1\) blades. Thus all \(2m+1+2^m\) displayed inequalities define distinct facets.

The primitive outer normals are
\[
Z_{i,a}=-e_{i,a}^{*},\quad Z_{i,b}=-e_{i,b}^{*},\quad
T=-\sum_i(e_{i,a}^{*}+e_{i,b}^{*}),\quad
Q_\epsilon=\sum_i e_{i,\epsilon_i}^{*}.
\]

**2. Exhaustion of nonunimodular cones.** For a nonempty face \(F\), \(Z_{i,s}\) is active iff the \(s\)-coordinate vanishes at every vertex of \(F\); \(T\) is active iff \(F\) has no \(C_i\) vertex. The active \(Q\)'s are either absent (when both \(A_i\) and \(B_i\) occur in a single blade) or constitute an entire Boolean subcube: each blade containing an \(A_i\) or \(B_i\) vertex fixes its choice, and each blade with no such vertex contributes one free bit. These conditions follow directly by testing the equality \(\sum_i x_{i,\epsilon_i}=1\) on the face vertices.

If there are at least two free bits, all four rays at a two-dimensional Boolean square occur. If there is one free bit \(j\) and blade \(j\) is unused, both \(Z_{j,a}\) and \(Z_{j,b}\) also occur along with the two \(Q\)-rays. If there are no free bits and \(T\) occurs, all blades contribute their single selected spoke and all complementary \(Z\)-rays occur. These give precisely the three dependence patterns below.

In every remaining case the active normal rays form part of an integral basis of their saturated linear span: zero-coordinate normals alone are coordinate unit vectors; adding only \(T\) or only one \(Q\) has a coefficient \(\pm1\) on a coordinate outside their span; and when exactly two \(Q\)-rays remain with their free blade containing \(C_j\), they give the identity matrix on the two \(j\)-coordinates, with all remaining active \(Z\)'s outside that block. In particular all simplicial normal cones are unimodular, and all nonsmooth cones contain one of the three displayed dependence patterns.

**3. Minimal singular cones.** Every square-family face has exactly four active \(Q\)-facets, varying on blades \(i,j\) and fixed elsewhere. Their primitive rays obey
\[
Q_{00}+Q_{11}=Q_{01}+Q_{10}.
\]
They have rank three and span a saturated rank-three sublattice (one may select a unimodular three-column minor). The flip-zero face has exactly four normal rays \(Q_0,Q_1,Z_{j,a},Z_{j,b}\), with
\[
Q_0+Z_{j,a}=Q_1+Z_{j,b}.
\]
Again their rank is three and the lattice span is saturated. The total-choice face has exactly \(m+2\) active rays \(T,Q_\epsilon,Z_{1,\bar\epsilon_1},\ldots,Z_{m,\bar\epsilon_m}\), with the primitive relation
\[
T+Q_\epsilon=\sum_{i=1}^{m}Z_{i,\bar\epsilon_i}.
\]
The span has rank \(m+1\) and is saturated: the \(m\) complementary-coordinate columns and any one selected-coordinate column give a determinant of absolute value one for the corresponding \(m+1\) independent rays.

Each set is a primitive circuit, and every proper face of each generated cone is smooth by the integral-basis argument of Step 2. Conversely any nonsmooth normal cone has one of these circuit groups of facet normals, so its underlying polytope face lies in the intersection of their corresponding facet equalities, namely one of the displayed faces. Thus these and only these cones are inclusion-minimal singular cones. The associated orbit closures are the distinct irreducible components of the reduced singular locus. Their codimensions equal the ranks of their normal cones, proving the counts and non-equidimensionality.

**4. Local affine transverse models.** For a saturated cone generated by \(r\) primitive rays with one primitive integral relation, its affine semigroup ring is the invariant subring of a polynomial ring on \(r\) variables under the one-dimensional torus whose weights are the coefficients of that relation. Both four-ray relations above have two positive and two negative unit coefficients. The degree-zero monomials are generated by the four products of two positive and two negative variables, subject to one \(2\times2\) minor, giving \(uv-wz=0\). The total-choice relation has weights \((1,1,-1,\ldots,-1)\) with \(m\) negative entries. Its degree-zero subring is generated by the \(2m\) products of the two positive-weight variables with the \(m\) negative-weight variables, subject to all \(2\times2\) minors: the rank-one \(2\times m\) determinantal cone. As cones over Segre varieties their Hilbert--Samuel multiplicities are respectively \(\deg(\mathbb P^1\times\mathbb P^1)=2\) and \(\deg(\mathbb P^1\times\mathbb P^{m-1})=m\).

A toric affine cone is \(\mathbb Q\)-Gorenstein precisely when a rational linear functional takes value one on every primitive ray. Applying such a functional to the total-choice relation would force \(2=m\); it cannot exist for \(m\ge3\). The conifold charts are Gorenstein. Toric \(\mathbb Q\)-factoriality is equivalent to simpliciality, which Step 2 shows is equivalent here to smoothness. All vertices are singular: the \(A_i,B_i\) vertices lie in flip-zero or square faces, and every \(C_i\) vertex lies in a square face. This completes the proof.

## Verification
The self-contained Python 3 program `verify.py` enumerates the facet incidences and all nonempty faces by intersections for \(m=2,3,4\). It computes exact rational face dimensions, verifies expected facet ranks, identifies the maximal nonsimple faces, and compares their full vertex masks against the three explicit index families. It also computes the gcd of full-rank integer minors for every simplicial cone when \(m=2,3\). Recorded outputs are: \(m=2\): 9 facets, 49 faces, 9 maximal nonsimple faces; \(m=3\): 15 facets, 289 faces, 26 maximal nonsimple faces; \(m=4\): 25 facets, 1645 faces, 72 maximal nonsimple faces. The program ends with `VERIFY_OK` when all assertions hold. These finite computations corroborate but do not replace the all-parameter symbolic argument in the proof.

## Relationship to prior work
Ohsugi and Hibi (2008, arXiv:0804.4287, Theorem 1.8) classify when edge polytopes are globally simple/smooth, but do not supply this family-wide singular-component basket. Tran and Ziegler (2014, Theorem 19) recount the general Ohsugi--Hibi facet criterion and give exponential-facet examples for windmills built from \(K_4\) blades, whereas the present graph has \(K_3\) blades. Their general facet framework is acknowledged as prior; no novelty is claimed for that framework. An earlier local chart calculation for the triangle-bouquet edge toric varieties treats base-edge torus-fixed points but does not classify the global singular locus. Likewise, the two-triangle wedge case \(m=2\) has prior global singular-locus coverage and is excluded from the new theorem. The present contribution is the exact all-\(m\ge3\) orbit-closure and transverse-type classification, not the general toric-cone or graph-edge-polytope machinery.

## Limitations
No scheme structure is asserted for the potentially nonreduced singular subscheme. Local determinantal types are generic transverse types of the specified components, not equations for every nongeneric or intersecting orbit. An equivalent prior classification under another toric presentation could remain unindexed; literature searching cannot establish uniqueness. No independent audit has been performed.

## References
1. H. Ohsugi and T. Hibi, *Simple polytopes arising from finite graphs*, arXiv:0804.4287, first publicly posted 2008-04-27; in particular Theorem 1.8.
2. T. Tran and G. M. Ziegler, *Extremal edge polytopes*, Electron. J. Combin. 21(2) (2014), P2.57, DOI: 10.37236/3633; in particular Theorem 19 and Section 5.
3. D. Cox, J. Little, and H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics 124, AMS, 2011, DOI: 10.1090/gsm/124.
