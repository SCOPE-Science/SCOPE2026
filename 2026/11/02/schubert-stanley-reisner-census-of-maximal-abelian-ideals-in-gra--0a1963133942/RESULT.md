# Schubert–Stanley–Reisner census of maximal abelian ideals in graphical Lie algebras

## Finding

Let \(G\) be any finite simple graph with ordered vertex set \(\{1,\ldots,n\}\), \(n\ge1\), and \(m=|E(G)|\) edges. Over an arbitrary field \(k\), form the graphical Lie algebra \(L_G\), with vertex generators \(x_i\), central edge generators \(z_{ij}\), and brackets \([x_i,x_j]=z_{ij}\) for \(\{i,j\}\in E(G)\), oriented by \(i<j\). Set \(\alpha=\alpha(G)\), the maximum cardinality of an independent vertex set. The variety \(\mathcal A_G\) of abelian subalgebras of largest possible dimension is canonically the variety of abelian \(\alpha\)-planes in the vertex space; **every such subalgebra is an ideal**, and its dimension is \(m+\alpha\).

Fix the vertex order. For a maximum independent set \(S\), every vertex outside \(S\) has a neighbor in \(S\). Let
\[
F_S=\{v\notin S:N_G(v)\cap S=\{s(v)\}\text{ and }s(v)<v\}.
\]
Define a graph \(H_S\) on \(F_S\), where distinct \(u,v\in F_S\) are adjacent precisely when \(\{u,v\}\in E(G)\) and \(s(u)\ne s(v)\). Let \(I_H(t)=\sum_{T\subseteq V(H)\,\mathrm{independent}}t^{|T|}\) denote the graph independence polynomial.

**Theorem (all fields and all finite simple graphs).** The intersection of \(\mathcal A_G\) with the reduced-row-echelon Schubert cell whose pivot set is \(S\) is, as an affine scheme,
\[
\mathcal A_G\cap\Omega_S\;\cong\;\operatorname{Spec}k[(t_v)_{v\in F_S}]/(t_ut_v:\{u,v\}\in E(H_S)).
\]
Thus every such stratum is a reduced coordinate-subspace arrangement, with irreducible components indexed by the inclusion-maximal independent sets of \(H_S\). Over any finite field \(\mathbb F_q\), the **complete exact count** of maximum-dimensional abelian ideals is
\[
\boxed{|\mathcal A_G(\mathbb F_q)|=\sum_{\substack{S\subseteq V(G)\\ |S|=\alpha,\ S\text{ independent}}} I_{H_S}(q-1).}
\]
The right side is a polynomial in \(q\), valid for every prime power, including characteristic two; its formula uses any fixed vertex order but its value is order independent.

The census is **strictly finer than the ordinary graph independence polynomial**. For \(G_1=K_3\sqcup K_1\) and \(G_2=P_4\), both have
\[
I_{G_1}(t)=I_{G_2}(t)=1+4t+3t^2
\]
and both associated Lie algebras have dimension seven and maximum abelian-ideal dimension five. Nevertheless,
\[
\mathcal A_{G_1}\cong\mathbb P_k^2,\quad
\mathcal A_{G_2}\cong\mathbb P_k^1\cup_{\mathbb P_k^0}\mathbb P_k^1,
\]
so their numbers of maximum-dimensional abelian ideals are, respectively,
\[
\boxed{q^2+q+1\quad\text{and}\quad 2q+1.}
\]

## Assumptions and scope

The graph is finite, simple and may have isolated vertices or no edges. The field \(k\) is arbitrary for the geometric and dimension statements. For the point-count formula, \(k=\mathbb F_q\) with \(q\) any prime power. The bracket is defined as an alternating Lie bracket, so the construction applies in characteristic two as well. The variety \(\mathcal A_G\) parameterizes distinct vector subspaces/ideals, not bases of subspaces, automorphism orbits or conjugacy classes. The above geometric scheme claim is made **on each Schubert stratum**, not a claim of a global irreducible-component decomposition.

Write \(V=k^n\) for the vertex-generator span and \(Z=k^m\) for the central edge span. The bracket on \(L_G=V\oplus Z\) is obtained by projecting \(\bigwedge^2V\) to the span of the edge coordinates. The scheme \(\mathcal A_G\) is the closed subvariety of \(\operatorname{Gr}(\alpha,V)\) cut out by the equations \([W,W]=0\). The graph \(H_S\) is defined intrinsically from \(G\), \(S\) and the chosen order.

## Proof

**1. Maximal dimension and ideals.** Every abelian subalgebra \(B\le L_G\) of maximum dimension contains \(Z\): otherwise \(B+Z\) would be a strictly larger abelian subalgebra. Hence \(B=W\oplus Z\) for a unique subspace \(W\le V\), and \([W,W]=0\). Any subalgebra containing \(Z\) is automatically an ideal because \([L_G,L_G]\subseteq Z\). Choose a reduced-row-echelon basis of \(W\), with pivot vertex columns \(S\) of size \(d=\dim W\). If two pivot vertices \(i,j\in S\) were adjacent, the coefficient of the edge basis vector \(z_{ij}\) in the bracket of the two corresponding rows would be the nonzero determinant \(1\). Thus \(S\) is independent and \(d\le\alpha\). Conversely the span of the vertex vectors indexed by a maximum independent set is abelian and has dimension \(\alpha\). This gives \(\dim B=m+\alpha\) and identifies all such \(B\) with \(\mathcal A_G\).

**2. Explicit cell equations.** Fix \(S=\{s_1<\cdots<s_\alpha\}\) maximum independent and let \(C_v\in k^\alpha\) be column \(v\) of the unique reduced-row-echelon matrix representing \(W\) in \(\Omega_S\). For a pivot vertex \(s_i\), \(C_{s_i}=e_i\). For an edge \(\{s_i,v\}\), the bracket-zero condition is \(e_i\wedge C_v=0\), so \(C_v\) is a scalar multiple of \(e_i\). If \(v\) has two distinct neighbors in \(S\), these conditions force \(C_v=0\). A vertex \(v\notin S\) always has at least one neighbor in \(S\), because otherwise \(S\cup\{v\}\) would be a larger independent set. Therefore a nonzero \(C_v\) is possible only when there is a unique neighbor \(s(v)\in S\); in that case \(C_v=t_ve_{s(v)}\). The echelon condition further forces \(t_v=0\) whenever \(v<s(v)\). Exactly the vertices \(v\in F_S\) can carry free scalar parameters.

For an edge \(\{u,v\}\) with both endpoints in \(F_S\), the corresponding bracket coefficient is the \(2\)-form \(t_ut_v e_{s(u)}\wedge e_{s(v)}\). This is zero automatically when \(s(u)=s(v)\), and is zero precisely when \(t_ut_v=0\) when \(s(u)\ne s(v)\). All other edge constraints were already satisfied. Thus the defining ideal in the echelon coordinates is generated by the squarefree monomials \(t_ut_v\) indexed by \(E(H_S)\). A squarefree monomial ideal is radical. Its minimal primes correspond to complements of the maximal independent vertex sets of \(H_S\), proving the claimed coordinate-subspace description of every stratum.

**3. Point count.** For a choice of parameters \((t_v)_{v\in F_S}\in\mathbb F_q^{F_S}\), the equations hold if and only if its support \(T=\{v:t_v\ne0\}\) is an independent set of \(H_S\). Each fixed support admits \((q-1)^{|T|}\) assignments. Distinct echelon pivot sets define disjoint Schubert cells, so summing over all maximum independent sets \(S\) proves the formula. Uniqueness of reduced-row-echelon form proves there is no overcounting.

**4. A strict refinement of independence polynomials.** For either four-vertex witness graph, \(\alpha=2\); for an abelian two-plane \(W\) let \(p_{ij}\) be its Plücker coordinates. The Grassmannian \(\operatorname{Gr}(2,4)\) is the quadric
\[
p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0
\]
in \(\mathbb P^5\). The bracket vanishes exactly when \(p_{ij}=0\) on every graph edge. For \(K_3\sqcup K_1\), edges \(12,13,23\) leave \(p_{14},p_{24},p_{34}\), so the Plücker equation vanishes identically and the locus is \(\mathbb P^2\). For the path with edges \(12,23,34\), the surviving coordinates are \(p_{13},p_{14},p_{24}\), constrained by \(p_{13}p_{24}=0\); this is two projective lines meeting at one rational point. Their finite-field point counts are therefore \(q^2+q+1\) and \(2(q+1)-1\). The two independence polynomials agree by direct inspection of their independent vertex sets.

## Verification

The standalone script `verify_abelian_ideal_schubert.py` independently enumerates reduced-row-echelon subspaces of dimension \(\alpha(G)\), checks every bracket directly, and compares with the independent-set support formula. It checks every labeled graph with one through four vertices over each of \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), plus four larger graphs over the first two fields and both four-vertex witnesses over \(\mathbb F_5\). Thus \(235\) graph-field configurations are directly compared. The quadratic extension field is implemented with \(a^2+a+1=0\). All agree: `GRAPH_MAXIMAL_ABELIAN_SCHUBERT_OK 235`.

Reproduce using `python3 verify_abelian_ideal_schubert.py`; it needs only Python's standard library. The general proof is the echelon argument above; checking a finite list of fields and graphs is not an infinite proof, and the script does not purport to exhaust larger graphs.

## Relationship to prior work

Burde and Ceballos (2009 preprint; 2012 journal publication) studied maximal dimensions of abelian subalgebras and ideals in solvable Lie algebras. Their general results supply context for the dimension problem; the dimension equality alone is **not** the novel point asserted here. Mainkar (2013 preprint; 2015 journal publication) proved graph-isomorphism rigidity for the two-step graphical construction, which is taken as established background. Aldi, Gabrielsen, Grandini, Harris and Kelley (2025 preprint) showed that the basic-cohomology independence polynomial of a Dani–Mainkar algebra recovers the ordinary graph independence polynomial, and proved a general bound on abelian-subalgebra dimensions (Proposition 24). The new contribution here is the **all-graph, all-characteristic Schubert-stratum classification and finite-field count**, with a specific witness that equal graph independence polynomials do not force equal maximum-abelian-ideal varieties or counts. No claim of global publication priority is made; equivalent presentations in older Lie-subalgebra or Grassmannian literature may exist.

## Limitations

The classification is specific to the Dani–Mainkar graphical two-step Lie algebras, not arbitrary two-step nilpotent Lie algebras or higher-step Lie algebras. It counts ideals of **maximum dimension**, not all inclusion-maximal abelian ideals, and does not classify their automorphism orbits. The individual Schubert cells are radical coordinate arrangements, but this analysis does not determine global singularities, irreducible components or cohomology of the entire variety for general graphs. The computation verifies small cases only. Independent external mathematical validation and exhaustive historical priority verification have not been performed.

## References

1. D. Burde and M. Ceballos, *Abelian ideals of maximal dimension for solvable Lie algebras*, arXiv:0911.2995v1, first posted 2009-11-16; *Journal of Lie Theory* **22** (2012), 741–756. https://arxiv.org/abs/0911.2995
2. M. G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, arXiv:1310.3414v1, first posted 2013-10-12; *Groups, Geometry, and Dynamics* **9** (2015), 55–65. https://arxiv.org/abs/1310.3414
3. M. Aldi, T. Gabrielsen, D. Grandini, J. Harris and K. Kelley, *Independence Polynomials of 2-step Nilpotent Lie Algebras*, arXiv:2504.19836v1, first posted 2025-04-28. https://arxiv.org/abs/2504.19836
