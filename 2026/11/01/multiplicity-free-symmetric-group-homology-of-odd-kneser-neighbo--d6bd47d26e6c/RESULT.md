# Multiplicity-free symmetric-group homology of odd Kneser neighborhood complexes

## Finding

For every integer \(k\ge2\), put \(n=2k+1\), let \(G_k=\mathrm{KG}(n,k)\) be the graph of \(k\)-element subsets of \([n]\), adjacent when disjoint, and let \(X_k=\mathcal N(G_k)\) be its ordinary open-neighborhood simplicial complex. The natural action of \(\mathfrak S_n\) on the ground set preserves \(X_k\).

**Theorem.** There is a \(\mathfrak S_n\)-equivariant **strong deformation retraction** of \(|X_k|\) onto the embedded middle-levels inclusion graph \(\Gamma_k\), whose bipartition consists of the \(k\)- and \((k+1)\)-subsets of \([n]\), with an edge for each inclusion. The first reduced rational homology is the following multiplicity-free module:

\[
\widetilde H_1(X_k;\mathbb Q)\cong_{\mathbb Q[\mathfrak S_n]}
\bigoplus_{i=1}^{k} S^{(2k-i,i,1)}.
\]

Here \(S^\lambda\) denotes the irreducible rational Specht representation labeled by the partition \(\lambda\) of \(n\). All other reduced rational homology groups vanish; integrally, \(X_k\) is homotopy equivalent to a wedge of

\[
\beta_k=(k-1)\binom{2k+1}{k}+1
\]

circles. The complete rational character is, for every \(g\in\mathfrak S_n\),

\[
\operatorname{tr}(g\mid\widetilde H_1)=F_k(g)-2U_k(g)+1,
\]

where \(U_k(g)\) is the number of invariant \(k\)-subsets and \(F_k(g)\) is the number of invariant inclusions \(A\subset B\) with \(|A|=k\), \(|B|=k+1\). The *new assertion* is the equivariant reduction and the full irreducible decomposition. The nonequivariant sphere-wedge type is already covered by the general Kneser-neighborhood literature and is not claimed as new.

## Assumptions and scope

All graphs are finite, simple, undirected, without loops; a face of the open-neighborhood complex is a nonempty vertex set admitting a common graph neighbor. The integer parameter is arbitrary \(k\ge2\), with \(n=2k+1\); no finite upper cutoff is assumed. The symmetric-group action is the literal ground-set relabeling action. The incidence graph \(\Gamma_k\) is realized *inside* \(|X_k|\): its \(k\)-subset nodes are the original vertices, and its \((k+1)\)-subset nodes are barycenters of maximal simplices.

## Proof

**1. Describe all facets and intersections.** Let \(B\subset[n]\) have cardinality \(k+1\), and let \(\Delta_B\) denote the full simplex on the \(k+1\) vertices given by the \(k\)-subsets of \(B\). For each \(k\)-subset \(A\), its graph neighborhood is the set of \(k\)-subsets of \([n]\setminus A\), which is precisely the vertex set of \(\Delta_{[n]\setminus A}\). Hence \(X_k\) is exactly the union of the \(\Delta_B\). These are its maximal simplices. For distinct \((k+1)\)-subsets \(B,C\), \(\Delta_B\cap\Delta_C\) contains as vertices the \(k\)-subsets of \(B\cap C\). Since \(|B\cap C|\le k\), the intersection is either empty or a *single original vertex*; in particular no edge belongs to two facets.

**2. Equivariant strong deformation retract.** In any one facet \(\Delta_B\) write a point in barycentric coordinates \(t=(t_1,\ldots,t_{k+1})\). Set \(b=(1/(k+1),\ldots,1/(k+1))\). Let \(M\) and \(M_2\) be the largest and second-largest coordinates of \(t\), counting multiplicity. If the maximum is unique, at index \(j\), put

\[
R(t)=b+(M-M_2)(e_j-b);
\]

if the maximum is tied, put \(R(t)=b\). This is continuous across maximum ties, because the gap \(M-M_2\) tends to zero, and is invariant under relabeling the simplex vertices. It fixes every point on the star \(Y_B=\bigcup_{j}[b,e_j]\): at \(b+s(e_j-b)\), the top-two gap equals \(s\). Moreover \(H_u(t)=(1-u)t+uR(t)\), for \(0\le u\le1\), remains in the convex simplex and fixes \(Y_B\). Thus it is a permutation-equivariant strong deformation retract onto \(Y_B\). Every overlap of two facets is empty or a vertex, and \(H_u\) fixes all vertices, so these local homotopies glue into a continuous global \(\mathfrak S_n\)-equivariant strong deformation retract. The union of the stars \(Y_B\) is exactly the middle-levels inclusion graph \(\Gamma_k\).

**3. Integral topology and connectedness.** Two \(k\)-subsets differing in one element are linked by a two-edge path through their \((k+1)\)-element union. Since any two \(k\)-subsets are related by such swaps, \(\Gamma_k\) is connected. It has \(2\binom{n}{k}\) vertices and \((k+1)\binom{n}{k}\) edges. Its cycle rank is \((k-1)\binom{n}{k}+1\). A connected graph is a wedge of that many circles up to homotopy. Hence \(\pi_1(X_k)\) is free of this rank; \(\widetilde H_1(X_k;\mathbb Z)\) is a free abelian group of this rank, and all other reduced integral homology groups vanish. These nonequivariant consequences are given for context rather than claimed as new.

**4. The actual rational \(\mathfrak S_n\)-module.** Orient every edge of \(\Gamma_k\) from its \(k\)-subset endpoint to its \((k+1)\)-subset endpoint. Relabeling preserves this bipartite orientation. Thus, with rational coefficients, the cellular one-chains form the permutation representation on the flags \(A\subset B\), whose stabilizer is \(\mathfrak S_k\times\mathfrak S_1\times\mathfrak S_k\). The zero-chains are the two permutation representations on \(k\)- and \((k+1)\)-subsets, which are isomorphic under complementation. Since the graph is connected, the augmented sequence is an exact sequence of \(\mathbb Q[\mathfrak S_n]\)-modules:

\[
0\longrightarrow H_1(\Gamma_k;\mathbb Q)\longrightarrow C_1
\xrightarrow{\partial}C_0\longrightarrow\mathbb Q\longrightarrow0.
\]

Let \(h_a\) be the degree-\(a\) complete homogeneous symmetric function and \(s_\lambda\) a Schur function. By the characteristic map of ordinary symmetric-group representations, the Frobenius characteristics of \(C_1\) and \(C_0\) are \(h_kh_1h_k\) and \(2h_kh_{k+1}\), respectively. Complete reducibility over \(\mathbb Q\) gives

\[
\operatorname{ch}H_1=h_k^2h_1-2h_kh_{k+1}+s_{(2k+1)}.
\]

The Pieri rule yields

\[
h_kh_{k+1}=\sum_{i=0}^{k}s_{(2k+1-i,i)},
\]

and

\[
h_k^2h_1=
2\sum_{i=0}^{k}s_{(2k+1-i,i)}-s_{(2k+1)}
+\sum_{i=1}^{k}s_{(2k-i,i,1)}.
\]

Subtracting cancels every one- and two-row constituent exactly, leaving precisely the asserted \(k\) distinct three-row Specht constituents, each with multiplicity one. The chain action also gives \(\operatorname{tr}(g\mid H_1)=\#\operatorname{Fix}(g\mid C_1)-\#\operatorname{Fix}(g\mid C_0)+1=F_k(g)-2U_k(g)+1\), proving the character formula.

## Verification

The standalone script `verify.py` reconstructs the facet intersections and incidence graph, checks connectivity and Euler ranks, checks Specht dimensions by hook lengths, and independently evaluates the rational character via the Jacobi–Trudi power-sum formula. All \(120\) elements of \(\mathfrak S_5\) and all \(5040\) elements of \(\mathfrak S_7\) were checked, as well as numerical structural checks for \(k=4\). It also verifies that the simplex retraction fixes its star on exact rational sample points. Recorded output: `verify_output.txt`. The infinite theorem follows from the preceding algebraic and topological proof, **not** from these finite tests.

For \(k=2\), the module is \(S^{(3,1,1)}\oplus S^{(2,2,1)}\), with dimensions \(6+5=11\). For \(k=3\), the module is \(S^{(5,1,1)}\oplus S^{(4,2,1)}\oplus S^{(3,3,1)}\), with dimensions \(15+35+21=71\). For \(k=4\), the four dimensions are \(28,105,162,84\), totaling \(379\).

## Relationship to prior work

The Lovász neighborhood-complex construction and the topology of Kneser graphs are classical. Kozlov's general nonequivariant Kneser-neighborhood sphere-wedge theorem is explicitly cited in Nilakantan–Singh (2018). In particular, that paper's Theorem 1.3 covers the \(k=3\) ground-subset-size, one-extra-element specialization at a nonequivariant level. The numeric ranks and sphere-wedge statements here are not priority claims. Schultz (2010/2011) develops dihedrally equivariant topology for *stable* Kneser graphs and their box complexes; the present theorem concerns the ordinary odd Kneser graphs under the **full** symmetric group. The middle-levels graph was long studied for matchings and Hamiltonicity; its cycle-space Specht decomposition is the additional result here. A separate recorded computation for \(\mathcal N(\mathrm{KG}(6,2))\) concerns different graph parameters and homological degree, and does not entail the uniform odd-family formula.

## Limitations

The representation decomposition is over \(\mathbb Q\); no integral Specht-module direct-sum splitting is asserted. The integer homology rank and graph homotopy type are not new. The explicit equivariant strong deformation retraction does not assert an equivariant simplicial collapse. The statement does not extend to \(\mathrm{KG}(2k+s,k)\) for general slack \(s\ge2\). Literature-index coverage cannot establish definitive publication priority; equivalent unindexed treatments of middle-level cycle representations remain a residual risk. No independent mathematical audit is claimed.

## References

- C. Schultz, *The equivariant topology of stable Kneser graphs*, DMTCS Proceedings AO (2011), pp. 873–884, public journal metadata dated 2010-12-31, https://dmtcs.episciences.org/en/articles/2960.
- N. Nilakantan and A. Singh, *Neighborhood Complexes of Kneser Graphs, \(\mathrm{KG}_{3,k}\)*, arXiv:1807.11732 (first submitted 2018-07-31), especially Theorem 1.3 and Section 4, https://arxiv.org/abs/1807.11732.
- D. Kozlov, *Combinatorial Algebraic Topology*, Springer (2007), Proposition 17.28, cited in Nilakantan–Singh for the general nonequivariant sphere-wedge result.
- H. Kierstead and W. Trotter, *Explicit matchings in the middle levels of the Boolean lattice*, Order 5 (1988), pp. 163–171, https://doi.org/10.1007/BF00337621.
- T. Mütze, *Proof of the middle levels conjecture*, Proc. London Math. Soc. 112 (2016), pp. 677–713, https://doi.org/10.1112/plms/pdw004.
