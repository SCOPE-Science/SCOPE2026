# Finite–tame–wild trichotomy and affine-factor census for acyclic face algebras

## Finding

Let \(k\) be an algebraically closed field of arbitrary characteristic, and let \(Q\) be a nonempty finite acyclic quiver, possibly with multiple arrows. Its Hayashi face algebra \(\mathfrak H(Q)\) has a sharp classification by the **connected components of the original quiver**:

1. It is of **finite representation type** precisely when every component is a coherently oriented directed path (an isolated vertex is allowed).
2. It is of **tame infinite representation type** precisely when every component is a directed path or a two-arrow, three-vertex fork, and at least one component is a fork. A fork has either two arrows directed out of its central vertex or two arrows directed into it.
3. In every other acyclic case, the algebra is **wild**.

Write \(f_+\) and \(f_-\) for the numbers of outward and inward forks in the tame case. The associated Kronecker-square quiver has exactly
\[
  f_+^2+f_-^2\quad\text{affine }\widetilde D_4\text{ components},
  \qquad 2f_+f_-\quad\text{affine }\widetilde A_3\text{ components}.
\]
Every remaining connected component has underlying Dynkin type \(A\). Thus the number of tame connected factors is exactly \((f_++f_-)^2\), and their Euclidean types are completely specified.

In the finite-type case, suppose the directed paths have respectively \(n_1,\ldots,n_s\ge1\) vertices. Then the **number of indecomposable finite-dimensional modules up to isomorphism** is
\[
  \sum_{\ell\ge0}\left(\sum_{i=1}^{s}\max\{n_i-\ell,0\}\right)^2
  =\dim_k\mathfrak H(Q).
\]
This is an equality of two natural invariants, not a claim that the corresponding modules and path-basis elements are canonically identified.

## Assumptions and scope

The base field is algebraically closed; no characteristic restriction is imposed. The quiver has finitely many vertices and arrows and no oriented cycles. Connected means connected after forgetting arrow directions. Parallel arrows are permitted and always place the face algebra in the wild case. A directed path means a connected quiver isomorphic to \(1\to2\to\cdots\to n\) for some \(n\ge1\), up to reversal and relabeling. A fork means the outward quiver \(1\leftarrow0\to2\) or its reversal \(1\to0\leftarrow2\), with no extra arrows.

The Kronecker-square quiver \(\widehat Q\) has vertex set \(Q_0\times Q_0\) and an arrow \((a,b)\) from \((s(a),s(b))\) to \((t(a),t(b))\) for every ordered pair of arrows of \(Q\). Calderón and Walton established the isomorphism \(\mathfrak H(Q)\cong k\widehat Q\). For acyclic \(Q\), this is the path algebra of a finite acyclic quiver; its representation type is governed by Gabriel's finite-type theorem and the affine-Dynkin tame classification.

## Proof

**1. Reduction to a graph criterion.** The cited face-algebra identification gives \(\mathfrak H(Q)\cong k\widehat Q\). Every directed cycle of \(\widehat Q\) would project to one in \(Q\), hence \(\widehat Q\) is acyclic. The classification of hereditary path algebras says that a connected component is representation-finite exactly when its underlying graph is Dynkin, tame infinite exactly when it is extended Dynkin, and wild otherwise. The representation type of a finite disjoint union is controlled by its most complicated component.

**2. Local branching obstruction.** If \(Q\) has two parallel arrows from \(u\) to \(v\), the four ordered arrow pairs give four parallel arrows from \((u,u)\) to \((v,v)\) in \(\widehat Q\). The resulting four-arrow Kronecker subquiver is wild, hence so is \(\widehat Q\). We may therefore assume that \(Q\) has no parallel arrows. At any vertex \(v\), write \(a=\deg^-(v)\) and \(b=\deg^+(v)\). The vertex \((v,v)\) of \(\widehat Q\) has \(a^2\) distinct incoming and \(b^2\) distinct outgoing neighbors, with disjoint sets because \(Q\) is acyclic. If \(\max(a,b)\ge3\), or if \(\max(a,b)\ge2\) and \(\min(a,b)\ge1\), the underlying graph contains a star with at least five leaves. Such a connected quiver is wild: its adjacency spectral radius exceeds two, whereas Dynkin and extended Dynkin diagrams have spectral radius below or equal to two. Thus a nonwild \(Q\) has \(\deg^-(v),\deg^+(v)\le1\) everywhere except possibly a vertex with degree pattern \((2,0)\) or \((0,2)\).

**3. An isolated fork is the unique surviving branching case.** A vertex of pattern \((2,0)\) or \((0,2)\) gives an underlying four-leaf star centered at \((v,v)\) in \(\widehat Q\), namely affine \(\widetilde D_4\). If its connected component of \(Q\) contains any additional arrow beyond those of the three-vertex fork, the diagonal embedding \(u\mapsto(u,u)\) supplies additional edges or vertices in the same component of \(\widehat Q\). This is a proper connected enlargement of the affine star and is wild by strict spectral-radius monotonicity for connected nonnegative adjacency matrices. Therefore a tame nonwild branching component must be exactly one of the two forks. A connected acyclic quiver in which every vertex has at most one incoming and at most one outgoing arrow is a coherently oriented directed path, since no directed cycles are allowed. This exhausts the possible nonwild input components.

**4. Sufficiency and the Euclidean-factor census.** Decompose \(Q\) into its directed-path and fork components. The Kronecker-square arrows never connect vertices coming from different ordered pairs of these input components, so consider each ordered pair. A directed path paired with a directed path splits into oriented chains. A fork paired with a directed path, in either order, splits into three-vertex paths and isolated vertices. For two forks of the same orientation, the only nontrivial connected component is a four-leaf star \(\widetilde D_4\); for two forks of opposite orientations, it is a four-cycle \(\widetilde A_3\), oriented acyclically. In each ordered pair of forks exactly one affine component occurs, and all other components are isolated. Counting ordered fork pairs gives \(f_+^2+f_-^2\) instances of \(\widetilde D_4\) and \(2f_+f_-\) instances of \(\widetilde A_3\). Thus all permitted inputs have only Dynkin \(A\) and affine \(\widetilde A_3\)/\(\widetilde D_4\) components; having at least one fork yields tame infinite type, and having none yields finite type.

**5. Exact indecomposable count in finite type.** In an oriented chain of \(m\) vertices, indecomposables are interval representations, one for every oriented subpath (including length-zero paths). Each connected component of \(\widehat Q\) is such an oriented chain when the components of \(Q\) are directed paths. Hence the number of indecomposables equals the number of paths in \(\widehat Q\), which equals \(\dim_k k\widehat Q\). By the definition of the synchronous square, its length-\(\ell\) paths are ordered pairs of length-\(\ell\) paths of \(Q\). A directed chain with \(n_i\) vertices has \(\max\{n_i-\ell,0\}\) such paths. Summing their squared total counts over all \(\ell\ge0\) proves the displayed identity.

## Verification

The standalone `verify_face_types.py` constructs the synchronous-square adjacency matrix independently from input arrow lists, then classifies the symmetric Cartan matrix \(2I-A\) by numerical inertia. It checks every acyclic orientation of each simple graph on at most four labeled vertices, plus deterministic samples on five and six vertices, all four ordered products of the two fork orientations, and a doubled-arrow boundary case. The observed output is `VERIFY_OK 857 acyclic quivers; Cartan inertia, four affine fork products and parallel-arrow boundary`.

The numerical spectral tests check only finitely many quivers. The proof above, including the connected spectral-radius comparison and the classical representation-type classification, establishes the infinite statement. No numerical tolerance is invoked in the proof.

## Relationship to prior work

Calderón–Walton (2021, Theorem 3.5 and Proposition 3.4) established that the face algebra is a Kronecker-square path algebra and studied dimension, Hilbert series, Noetherian properties, homological dimensions and related invariants. Their Table 1 already explicitly illustrates several small square quivers, including a three-vertex fork; those examples and the structural isomorphism are prior results. Gabriel's theorem and the Donovan–Freislich–Nazarova classification are also established input theorems. The finding here is the complete, sharp criterion directly on the *original* acyclic quiver, including every wild obstruction, all affine-component multiplicities and the finite-type indecomposable-count equality.

Eckert (2023) gives a modern treatment recalling the Dynkin/extended-Dynkin representation-type classification of path algebras, which is applied here. The literature search did not locate a prior source stating the complete input-level trichotomy and affine-factor census. This is not proof of publication priority; a general quiver-product classification could imply the present result.

## Limitations

The classification is stated only for finite acyclic quivers over algebraically closed fields. It makes no assertion about infinite-dimensional face algebras from cyclic quivers, representation theory over nonclosed fields, geometric classifications within tame module families, or priority beyond the inspected literature. Finite checks cannot replace the graph-theoretic argument.

## References

1. F. Calderón and C. Walton, *Algebraic properties of face algebras*, arXiv:2105.12042 (first posted 2021-05-25); see Proposition 3.4, Theorem 3.5 and Table 1, https://arxiv.org/abs/2105.12042.
2. S. Eckert, *Tame hereditary path algebras and amenability*, *Bull. Lond. Math. Soc.* 55 (2023), 1837–1856, https://doi.org/10.1112/blms.12822; Introduction (Gabriel and affine-Dynkin trichotomy).
3. P. Gabriel, finite-type classification of quiver representations (classical theorem); Donovan–Freislich and Nazarova, tame extended-Dynkin classification (classical results), cited in Eckert's Introduction.
