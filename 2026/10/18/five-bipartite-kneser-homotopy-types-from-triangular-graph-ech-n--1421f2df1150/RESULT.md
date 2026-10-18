# Five bipartite Kneser homotopy types from triangular-graph Čech nerves

## Finding
Let \(n\) be **one of the five integers \(6,7,8,9,10\)**. Let \(T_n=L(K_n)\) be the triangular graph, whose vertices are the two-element subsets of \([n]\), with two vertices adjacent when their subsets intersect. Equip its geometric realization with unit-length edges, and write \(X_n=\mathcal N(T_n,2)\) for the intrinsic graph Čech nerve of *closed radius-one* balls centered at vertices of \(T_n\). Then
\[
X_n\simeq\bigvee^{\binom{n-1}{4}} S^3\;\vee\;\bigvee^{\binom n4}S^4.
\]
In particular, its only nonzero reduced integral homology groups are free of ranks \(\binom{n-1}{4}\) in degree three and \(\binom n4\) in degree four.

Let \(H(n,2)\) be the bipartite Kneser graph, with one part indexed by the two-subsets of \([n]\), the other by the \((n-2)\)-subsets, and edges corresponding to containment. The same classification yields, by the closed-neighborhood suspension equivalence,
\[
\operatorname{Ind}(H(n,2))\simeq
\bigvee^{\binom{n-1}{4}}S^4\;\vee\;\bigvee^{\binom n4}S^5.
\]
These are five **finite** homotopy classifications, not a theorem for arbitrary \(n\).

## Assumptions and scope
The graph \(K_n\) is simple and complete, and its line graph has \(\binom n2\) vertices. In the graph Čech convention of Adams–Shukla–Singh, scale \(r=2\) means geometric balls of radius \(r/2=1\); it is not the Vietoris–Rips complex and not a radius-two ball nerve.

Identify a simplicial vertex of \(X_n\) with an edge of \(K_n\). The closed neighborhood in \(T_n\) of the vertex corresponding to an edge \(e=\{a,b\}\) consists exactly of the edges of \(K_n\) that meet \(e\). Lemma 2.2 of Adams–Shukla–Singh therefore identifies \(X_n\) with the simplicial complex of edge sets admitting a vertex cover of size at most two: its generating simplices are
\[
F_e=\{f\in E(K_n): f\cap e\neq\varnothing\},\qquad e\in E(K_n).
\]
The empty simplex is included when constructing its augmented face poset.

## Proof
The proof is a finite, exactly reproducible acyclic discrete-Morse certificate; the five integer values form the entire proved domain.

**(1) Exhaustive complex.** Order the \(m=\binom n2\) edges of \(K_n\) lexicographically as \(e_0,\ldots,e_{m-1}\). Encode each face \(\sigma\subseteq E(K_n)\) as the integer with bit \(j\) set iff \(e_j\in\sigma\). Form the union of **all** subfaces of all \(m\) generator sets \(F_e\), including the empty simplex. This is exactly \(X_n\) by the cited even-scale Čech lemma, not a sampling of its faces.

**(2) The matching.** Initially mark every face as unmatched. For \(j=0,\ldots,m-1\), simultaneously pair every still-unmatched \(\sigma\) that does not contain \(e_j\) with \(\sigma\cup\{e_j\}\) provided both faces remain unmatched; remove both from later pairing stages. At a fixed stage these pairs are disjoint. This standard ordered-coordinate matching is acyclic (Goyal–Shukla–Singh, Proposition 3.1); the standalone verification additionally constructs and exhaustively topologically sorts the **entire** directed graph of possible nontrivial Forman gradient steps at each of the five values of \(n\). The directed graph has one node per matched lower face and an arrow \(\sigma\to\tau\) exactly when \(\tau\neq\sigma\) is a codimension-one face of the matched upper face of \(\sigma\) and \(\tau\) is itself matched lower. No such graph contains a directed cycle.

**(3) Exhaustive critical-face counts.** All faces are paired except the critical faces below. The full face counts, pairing counts, and unmatched dimensions are:

| \(n\) | All faces, including empty | Matched pairs | Critical three-faces | Critical four-faces |
|---:|---:|---:|---:|---:|
| 6 | 5,142 | 2,561 | 5 | 15 |
| 7 | 34,308 | 17,129 | 15 | 35 |
| 8 | 202,141 | 101,018 | 35 | 70 |
| 9 | 1,099,624 | 549,714 | 70 | 126 |
| 10 | 5,673,836 | 2,836,750 | 126 | 210 |

The equality between each row's total face count and twice its matched-pair count plus its critical-face count checks exhaustiveness. In all five rows the empty face is paired; no critical simplices of any other dimensions remain. The critical counts agree, at each listed integer, with \(\binom{n-1}{4}\) and \(\binom n4\).

**(4) Exact integral Morse boundary.** Give simplicial faces the lexicographically increasing orientation. For a matched lower \(\tau\) with paired upper \(u\), eliminate the unit incidence coefficient \([u:\tau]=\pm1\) using the integral chain-substitution rule
\[
\pi(\tau)=-[u:\tau]^{-1}
\sum_{\substack{\rho\subset u\\|\rho|=|\tau|,\rho\ne\tau}}
[u:\rho] \pi(\rho).
\]
Set \(\pi(\rho)=0\) for matched upper faces and \(\pi(\rho)=\rho\) for critical faces. The already verified absence of closed gradient paths makes the substitution terminating. For **every** critical four-simplex \(\sigma\), form the integral signed Morse boundary \(\sum_{\tau\subset\sigma,\ |\tau|=4}[\sigma:\tau]\pi(\tau)\). All entries are *exactly zero integers* at all five values, as checked by the embedded `verify.py`; the algorithm does not reduce modulo a prime or approximate a rank. Thus the Morse complex has one zero-cell, \(\binom{n-1}{4}\) three-cells and \(\binom n4\) four-cells with zero attaching degrees into the three-cells.

**(5) Homotopy, not just homology.** Its three-skeleton is a wedge of three-spheres. Since this skeleton is two-connected, its Hurewicz map from \(\pi_3\) to \(H_3\) is an isomorphism. Consequently zero cellular attaching degrees for every four-cell imply nullhomotopic attaching maps. The Morse CW model is therefore the displayed wedge of three- and four-spheres. There is no reliance on the false inference that arbitrary spaces with free homology are wedges of spheres.

**(6) Bipartite Kneser interpretation.** The complement of \(T_n\) is the Kneser graph \(KG(n,2)\). Its canonical bipartite double cover \(K_2\times KG(n,2)\) is naturally isomorphic to \(H(n,2)\): the second copy of a two-subset \(B\) maps to its \((n-2)\)-element complement, and disjointness becomes containment. Matsushita's Theorem 1.2 gives \(\operatorname{Ind}(H(n,2))\simeq\Sigma X_n\), and suspending the proved wedge yields the asserted bipartite Kneser types.

## Verification
The accompanying **standalone standard-library** program `verify.py` reconstructs all generator simplices and **every face** for each \(n\in\{6,7,8,9,10\}\); constructs each matching pair; checks pair disjointness and the complete critical-face distribution; computes indegrees and performs a full topological sort of all Forman V-path candidate transitions; then evaluates **every** integer Morse incidence from critical degree four to critical degree three using oriented face boundaries. It prints `VERIFY_OK` if and only if all assertions pass. To reproduce: `python3 verify.py` from a directory containing that file. Its largest case contains 5,673,836 faces and is memory-intensive; do not treat an unsuccessful run due to resources as evidence against the theorem.

## Relationship to prior work
Adams–Shukla–Singh establish the graph Čech construction and the even-scale neighborhood lemma, and classify hypercube graphs rather than these triangular graphs. Goyal–Shukla–Singh establish the generic ordered-coordinate matching's acyclicity, not the critical cells or signed Morse boundary of this complex. Barmak's Theorem 4.11 classifies the independence complex of the **ordinary Kneser graph** \(KG(n,2)\); it does not classify that of its bipartite double cover. Nilakantan–Shukla classify **consecutive-neighbor circulant** regular bipartite graphs, not bipartite Kneser graphs. Matsushita establishes the suspension equivalence for general complement graphs; the theorem does not provide the five homotopy computations here. Its worked complete-graph-product example involves \(K_a\square K_b\), not \(L(K_n)\). Known computations for the smaller Desargues graph, corresponding to \(n=5\), are not included in the new claim.

## Limitations
Only the **five integers 6 through 10** are established. The binomial pattern is not asserted to hold for \(n\ge11\), despite its suggestive form. This is a finite exact homotopy classification based on complete enumerations and integral Morse calculations; it does not prove an infinite-family formula or a canonical equivalence between the associated CW models. Bibliographic searches and inspected sources do not establish uniqueness in the literature; unindexed equivalent results remain a risk. No independent validation has been performed.

## References
1. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, v1 first public December 12, 2022, especially Lemma 2.2, Theorems 4.1–4.2. https://arxiv.org/abs/2212.05871
2. S. Goyal, S. Shukla, A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, Proposition 3.1 and Proposition 3.2. https://arxiv.org/abs/1905.06926
3. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, Theorem 1.2 and Example 3.5. https://arxiv.org/abs/2511.12608
4. J. A. Barmak, *Star clusters in independence complexes of graphs*, Advances in Mathematics 241 (2013), 33–57, Theorem 4.11. https://doi.org/10.1016/j.aim.2013.03.016
5. N. Nilakantan, S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789, Theorem 1.2. https://arxiv.org/abs/1709.04789
6. A. Kumar, P. Singh, R. Verma, *Certain homological invariants of bipartite Kneser graphs*, Journal of Algebra and Its Applications, DOI:10.1142/S0219498822502061, arXiv:2105.06144 (linear-strand and edge-ideal invariants, a distinct object). https://arxiv.org/abs/2105.06144
