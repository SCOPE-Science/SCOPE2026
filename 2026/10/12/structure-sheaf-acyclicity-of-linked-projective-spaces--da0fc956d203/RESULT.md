# Structure-sheaf acyclicity of linked projective spaces
## Finding
Let \(\mathfrak V\) be a nontrivial exact finitely generated linked net of complex vector spaces of dimension \(r+1\) over a \(\mathbb Z^n\)-quiver, and let
\[
X=\mathbb{LP}(\mathfrak V)
\]
be its linked projective space. Then
\[
H^0(X,\mathcal O_X)\cong\mathbb C,
\qquad
H^i(X,\mathcal O_X)=0
\quad\text{for every }i>0.
\]
Moreover, the dual complex \(\mathcal D(X)\) of the simple-normal-crossings scheme \(X\) is contractible.

Thus \(X\) has the same structure-sheaf cohomology as the small diagonal \(\mathbb P^r\), even though it is not known whether every linked projective space is a flat degeneration of that diagonal.

## Assumptions and scope
The ground field is \(\mathbb C\). The linked net is nontrivial, exact, and finitely generated in the sense of De León--Esteves--Vital, and all its vertex spaces have dimension \(r+1\).

Let \(H\) be the minimum set of generators. The irreducible components of \(X\) are indexed by \(H\). For each nonempty subset \(\Delta\subseteq H\), write
\[
X_\Delta=\bigcap_{v\in\Delta}X_v
\]
for the scheme-theoretic component intersection when it is nonempty.

The result is about coherent structure-sheaf cohomology and the homotopy type of the dual complex. It does not construct a flat family from \(X\) to the diagonal and does not determine the multigraded coordinate ring or a minimal free resolution.

## Proof
De León--Esteves--Vital prove that \(X\) is simple normal crossings. Hence every nonempty stratum \(X_\Delta\) is smooth projective.

They also identify each nonempty \(X_\Delta\) as the scheme-theoretic image of a rational map
\[
\mathbb P(W_\Delta)\dashrightarrow \prod_{v\in H}\mathbb P(V_v)
\]
for an explicitly associated vector space \(W_\Delta\). Therefore \(X_\Delta\) is integral and unirational.

We first show
\[
H^q(X_\Delta,\mathcal O_{X_\Delta})=0
\quad\text{for every }q>0.
\]
Indeed, a smooth projective unirational complex variety has no nonzero holomorphic differential forms of positive degree. One way to see this is to restrict a dominant rational map from projective space to a general linear subspace of the same dimension as \(X_\Delta\), obtaining a generically finite dominant rational map. Resolve its indeterminacy. Pullback along the resulting generically finite morphism injects holomorphic differential forms, while the smooth projective source is birational to projective space and therefore has none in positive degree. Hodge symmetry then gives
\[
H^q(X_\Delta,\mathcal O_{X_\Delta})
=
H^{0,q}(X_\Delta)
=
0
\]
for \(q>0\). Since \(X_\Delta\) is integral and projective,
\[
H^0(X_\Delta,\mathcal O_{X_\Delta})=\mathbb C.
\]

For a simple-normal-crossings scheme, the Mayer--Vietoris simplicial resolution is exact:
\[
0\longrightarrow\mathcal O_X
\longrightarrow
\bigoplus_{|\Delta|=1}\mathcal O_{X_\Delta}
\longrightarrow
\bigoplus_{|\Delta|=2}\mathcal O_{X_\Delta}
\longrightarrow\cdots .
\]
Taking hypercohomology, all rows with positive sheaf-cohomological degree vanish by the preceding paragraph. Consequently
\[
H^i(X,\mathcal O_X)
\cong
H^i(\mathcal D(X),\mathbb C),
\]
where \(\mathcal D(X)\) is the simplicial complex whose nonempty faces are precisely the nonempty component intersections.

It remains to identify the topology of \(\mathcal D(X)\). In the proof of their Hilbert-polynomial theorem, De León--Esteves--Vital define, for each nonnegative lattice point \(a\), a simplicial complex \(K_a\) whose faces are the polygons \(\Delta\) satisfying \(a\in D_\Delta\), where \(D_\Delta\) is the independence polytope of \(X_\Delta\). Since every independence polytope contains \(0\),
\[
K_0=\mathcal D(X).
\]
Their convex-cover construction realizes every nonempty \(K_a\) with \(|a|\le r\) as the nerve of a cover of a simplex by closed convex subsets and proves it contractible. Taking \(a=0\) gives
\[
\mathcal D(X)\simeq *.
\]
Therefore its cohomology is \(\mathbb C\) in degree \(0\) and zero in all positive degrees. Substitution in the Mayer--Vietoris computation proves
\[
H^0(X,\mathcal O_X)\cong\mathbb C,
\qquad
H^i(X,\mathcal O_X)=0
\quad(i>0).
\]

## Verification
The proof was checked against the complete accessible text of arXiv:2609.37634v1 at the following structural points:

1. Proposition 2.4 records the exact Mayer--Vietoris simplicial resolution for a simple-normal-crossings scheme.
2. Theorem 3.3 proves that a linked projective space is simple normal crossings.
3. Proposition 4.1 identifies each nonempty stratum \(X_\Delta\) with the scheme-theoretic image of a rational map from a projective space.
4. In the proof of Theorem 4.4, the complexes \(K_a\) are shown contractible for \(|a|\le r\) by a convex-cover nerve argument.
5. At \(a=0\), every nonempty stratum contributes because \(0\) lies in every independence polytope, so \(K_0\) is exactly the dual complex.

The only additional input is the standard characteristic-zero fact that a smooth projective unirational complex variety has \(H^q(\mathcal O)=0\) for \(q>0\). The proof above includes a reduction through a generically finite rational parametrization, resolution of indeterminacy, and Hodge symmetry.

No finite experiment or enumeration is used to infer the universal statement.

## Relationship to prior work
De León--Esteves previously proved that linked projective spaces have the Chow class of the small diagonal. Their 2026 Bulletin of the London Mathematical Society article also describes the reduction complex through the polygonal tiling associated to the linked net. The full text inspected there does not state contractibility of that complex or structure-sheaf cohomology vanishing.

De León--Esteves--Vital strengthen the Chow-class result to equality of multivariate Hilbert polynomials and prove the simple-normal-crossings, stratum-image, and convex-nerve facts used here. Their paper does not state
\[
H^i(X,\mathcal O_X)=0
\quad(i>0).
\]
Equality of Hilbert polynomials alone would yield only the Euler characteristic
\[
\chi(X,\mathcal O_X)=1,
\]
not the individual vanishing groups.

A 2026 doctoral thesis by Felipe De León titled *On the geometry of linked projective spaces* is cited by the earlier paper and is highly relevant. Exact-title searches located its bibliographic citation but not an accessible full text, so it remains a residual originality risk.

## Limitations
The proof is over \(\mathbb C\). It uses Hodge theory in the step from unirationality of the smooth strata to vanishing of their higher structure-sheaf cohomology. A positive-characteristic analogue is not claimed.

The conclusion concerns only \(\mathcal O_X\). It does not give cohomology vanishing for arbitrary line bundles or coherent sheaves, nor does it identify the multigraded Betti table.

Contractibility is proved for the dual complex arising from the component-intersection stratification. No statement is made about the ordinary topological homotopy type of the whole linked projective space.

The inaccessible 2026 thesis remains the main literature-access risk.

## References
1. Felipe De León, Eduardo Esteves, and Eduardo Vital, *On the Hilbert polynomial of the linked projective space*, arXiv:2609.37634v1, 29 September 2026.
2. Felipe de Leon and Eduardo Esteves, *Polymatroidal tilings and the Chow class of linked projective spaces*, Bulletin of the London Mathematical Society 58 (2026), e70370, DOI 10.1112/blms.70370; arXiv:2508.14799v1, 20 August 2025.
3. Felipe De León, *On the geometry of linked projective spaces*, Ph.D. thesis, Instituto de Matemática Pura e Aplicada, 2026.
