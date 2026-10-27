# Symmetric expanding evolution algebras with a simple socle and an exact ideal lattice

## Finding

There is a uniform construction associating to every finite connected simple \(d\)-regular graph \(G\) with \(d\geq1\) a symmetric evolution algebra \(E(G)\) over \(\mathbb Q\) whose undirected support graph is the two-clique blow-up \(G[K_2]\). The graph is connected, and along any fixed-degree graph expander family it remains a fixed-degree expander family. Nevertheless \(E(G)\) is not simple: its square \(I=E(G)^2\) is a simple ideal of dimension \(|V(G)|\) in the \(2|V(G)|\)-dimensional algebra. Every nonzero ideal contains \(I\); all subspaces containing \(I\) are ideals. Thus its entire ideal lattice is obtained by adjoining one new least element to the ordinary vector-subspace lattice of \(\mathbb Q^{|V(G)|}\).

For the unnormalized graph Laplacian, the exact spectral formula is
\[
\operatorname{Spec} L_{G[K_2]}=2\operatorname{Spec}L_G\ \uplus\ \{2(d+1)\}^{[|V(G)|]}.
\]
In particular its positive spectral gap is exactly twice that of \(G\). Finite-field specializations yield explicit Gaussian-binomial enumerations of every ideal, not merely maximal ideals.

## Assumptions and scope

Let \(K\) be a field with \(\operatorname{char}K\neq2\). Let \(G\) be any finite connected simple undirected \(d\)-regular graph on \(n\ge2\) vertices, where \(d\ge1\); write \(A\) for its symmetric adjacency matrix. Choose a nonzero scalar \(\lambda\in K\) such that \(B=A+\lambda\,\mathrm{Id}_n\) is invertible. Over \(\mathbb Q\), \(\lambda=d+1\) always works: each eigenvalue of \(A\) lies in \([-d,d]\), so every eigenvalue of \(B\) is at least one.

Define the \(2n\)-dimensional commutative nonassociative \(K\)-algebra \(E=E(G,\lambda)\) with natural basis \(x_{v,+},x_{v,-}\) (\(v\in V(G)\)), pairwise distinct basis products zero, and
\[
 x_{v,\pm}^{\,2}=\sum_{w\in V(G)}B_{vw}(x_{w,+}+x_{w,-}).
\]
The matrix relative to the displayed natural basis is \(B\otimes J_2\), where \(J_2\) is the all-ones matrix. The term *simple* means having no nonzero proper two-sided algebra ideal. An *evolution ideal* means an ideal admitting a natural basis; the square ideal below is also an evolution ideal whose natural basis extends to a natural basis of \(E\).

## Proof

**Simple square ideal.** Define \(f_v=x_{v,+}+x_{v,-}\) and \(g_v=x_{v,+}-x_{v,-}\). The vectors \(\{f_v,g_v:v\in V(G)\}\) form a natural basis because \(2\) is invertible. Direct expansion gives, for each vertex \(v\),
\[
 f_v^2=g_v^2=2\sum_w B_{vw}f_w,
 \qquad f_vg_v=0,
\]
and products of basis vectors with different subscripts vanish. Let \(I=\operatorname{span}_K\{f_v\}\). Every product in \(E\) belongs to \(I\); invertibility of \(B\) implies that \(\{f_v^2:v\in V(G)\}\) spans \(I\). Hence \(E^2=I\) and \(\dim I=n\), while \(E/I\) is square-zero of dimension \(n\).

To show that \(I\) is simple, take a nonzero ideal \(H\) of the algebra \(I\) and an element \(u=\sum_v a_v f_v\in H\) with \(a_v\neq0\). The product \(uf_v=a_v f_v^2\) places \(f_v^2\) in \(H\). Whenever \(w\) is a neighbor of \(v\), multiplying \(f_v^2\) by \(f_w\) yields \(2B_{vw}f_w^2=2f_w^2\in H\). Connectivity propagates membership to every \(f_w^2\), which span \(I\). Therefore \(H=I\).

**All ideals.** Let \(J\subset E\) be a nonzero ideal. Choose a nonzero \(u=\sum_v(a_v f_v+b_vg_v)\in J\). Some coefficient is nonzero. Multiplication by the corresponding \(f_v\) or \(g_v\) yields a nonzero multiple of \(f_v^2=g_v^2\) in \(J\cap I\). Since \(I\) is simple, \(J\cap I=I\). Conversely, if \(I\subseteq J\subseteq E\) is any linear subspace, then \(JE\subseteq E^2=I\subseteq J\), so \(J\) is an ideal. The ideal poset is therefore exactly
\[
 \{0_E\}\ \oplus\ \mathcal L_K(E/I),
\]
where \(\mathcal L_K(E/I)\) is the full vector-subspace lattice, including its zero subspace corresponding to \(I\), and the prefixed \(0_E\) is an additional bottom element. This also proves uniqueness of the minimal nonzero ideal \(I\). Its extending natural basis is the set of \(f_v\) inside \(\{f_v,g_v\}\).

**Support graph and spectral gap.** Since \(\lambda\neq0\), the two basis elements over each vertex are adjacent in the symmetrized, loopless support graph; since \(B_{vw}=1\) precisely when \(v,w\) are adjacent in \(G\) (for distinct vertices), all four cross-fiber edges occur. Thus the support graph is \(G[K_2]\), of degree \(2d+1\), with adjacency matrix
\[
 C=(A+\mathrm{Id}_n)\otimes J_2-\mathrm{Id}_{2n}.
\]
Its Laplacian \(L=(2d+1)\mathrm{Id}_{2n}-C\) splits into the fiber-symmetric subspace \(\{(z_v,z_v)_v\}\), where it acts as \(2L_G\), and the fiber-antisymmetric subspace \(\{(z_v,-z_v)_v\}\), where it acts as scalar \(2(d+1)\). This proves the complete spectral formula. The nonzero eigenvalues of \(L_G\) have mean \(nd/(n-1)\le d+1\), so its least positive eigenvalue is at most \(d+1\). Hence the new least positive eigenvalue is exactly twice the old one. For any family of \(d\)-regular graphs whose least positive Laplacian eigenvalue is uniformly bounded below by \(\delta>0\), the lifted family is \((2d+1)\)-regular and has spectral gaps at least \(2\delta\). Standard regular-graph Cheeger inequalities therefore give uniform edge expansion. This is an infinite family over the fixed field \(\mathbb Q\).

**Finite-field counts.** If \(K=\mathbb F_q\), with \(q\) odd and \(q>n+1\), there exists a nonzero \(\lambda\in K\) for which \(A+\lambda\mathrm{Id}_n\) is invertible: the monic degree-\(n\) determinant polynomial excludes at most \(n\) values, and zero excludes one more. The preceding conclusions then hold. Since \(E/I\cong K^n\), the exact number of algebra ideals is
\[
 1+\sum_{j=0}^n {n\brack j}_q,
\]
where \({n\brack j}_q\) is the Gaussian binomial coefficient, counting \(j\)-dimensional linear subspaces. The leading \(1\) is the zero ideal of \(E\).

## Verification

The accompanying standalone `verify.py` checks the rank, support matrix, degree, and full Laplacian invariant-subspace decomposition on five connected regular graphs with \((n,d)=(2,1),(3,2),(4,3),(4,2),(8,3)\). Over \(\mathbb F_5\), for the graph \(K_2\) and \(\lambda=2\), it exhaustively enumerates all \(1120\) linear subspaces of \(\mathbb F_5^4\), tests actual ideal closure against the multiplication table, and finds exactly \(9\) ideals, precisely zero together with the subspaces containing \(I\). It prints `VERIFY_OK` on success. Finite tests corroborate but do not prove the all-graph/all-field statements; the proof above supplies the general argument.

## Relationship to prior work

Giacomelli, *Expander Evolution Algebras* (arXiv:2605.12672v1, first posted 12 May 2026), introduces the symmetrized graph and expander algebra framework. Its Theorem 3.8 asserts that positive expansion together with a symmetric structure matrix implies simplicity. The present symmetric positive-support construction gives counterexamples, strengthened by a complete ideal-lattice and graph-spectrum determination. Giacomelli's Section 9.2 already discusses tensor constructions; the fact that our matrix is a Kronecker product is not claimed as new. The stated source theorem does not provide this ideal-lattice classification or the displayed exact spectral decomposition.

Cabrera Casado, Siles Molina, and Velasco, *Evolution algebras of arbitrary dimension and their decompositions* (arXiv:1601.01832v2, first posted 8 January 2016), distinguish connectedness/irreducibility from simplicity and characterize simple finite-dimensional evolution algebras. Their structural criteria are used rather than claimed as new. Cabrera Casado, Martín Barquero, Martín González, and Tocino, *Connecting ideals in evolution algebras with hereditary subsets of its associated graph* (published online 14 March 2024, DOI below), already show that all subspaces containing the square are ideals and characterize maximal ideals, including a two-dimensional equal-square example. Neither result is claimed as new here. The contribution is the explicit uniform bounded-degree expander family with a **simple square ideal**, absence of every other nonzero ideal below the square, complete full ideal lattice, and exact normalized spectral behavior.

## Limitations

The construction is basis-dependent at the graph level, as is the notion of an expander evolution algebra for a chosen natural basis. The expansion implication is about support graphs, not invertibility or a dynamical spectral gap of the algebra's multiplication operator. The natural characteristic restriction is \(2\neq0\); a finite field must admit a nonzero parameter with invertible \(B\), as ensured by \(q>n+1\), but this bound is sufficient rather than necessary. Earlier general theory already establishes many component facts; an independently established broad ideal-lattice classification may implicitly encompass this specialized family. No independent audit has been performed.

## References

1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1 (2026), especially Definitions 3.1 and 3.5, Theorem 3.8, and Section 9.2. https://arxiv.org/html/2605.12672v1
2. Y. Cabrera Casado, M. Siles Molina and M. V. Velasco, *Evolution algebras of arbitrary dimension and their decompositions*, arXiv:1601.01832v2 (2016), Sections 4–5. https://arxiv.org/html/1601.01832v2
3. Y. Cabrera Casado, D. Martín Barquero, C. Martín González and A. Tocino, *Connecting ideals in evolution algebras with hereditary subsets of its associated graph*, Collectanea Mathematica, published online 14 March 2024, DOI:10.1007/s13348-024-00435-x, Proposition 3.9 and Remark 3.12. https://doi.org/10.1007/s13348-024-00435-x
