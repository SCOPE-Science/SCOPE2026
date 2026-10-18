# Indegree-parity rigidity and exact orientation spectra of cactus graphs

## Finding
Let \(G=(V,E)\) be a finite connected simple undirected graph. For an orientation \(D\), its *indegree-parity signature* is \(\sigma_D(v)=\deg_D^-(v)\bmod 2\). Two orientations have the same signature precisely when reversing the arcs on which they differ changes indegree parity at no vertex.

**Rigidity characterization.** The following are equivalent:

1. \(G\) is a cactus: every edge belongs to at most one undirected simple cycle.
2. For every feasible parity signature \(\tau\), either every orientation with signature \(\tau\) is acyclic or every such orientation contains a directed cycle.

**Complete signature spectrum.** If \(G\) is a cactus with \(b\) bridges and \(c\) (pairwise edge-disjoint) cycles of lengths \(\ell_1,\ldots,\ell_c\), then exactly \(2^{|V|-1}\) parity signatures are feasible. Every feasible signature has exactly \(2^c\) realizing orientations. For a feasible signature \(\tau\), let \(h_G(\tau)\) be the number of coherently directed simple cycles in any realizing orientation; the rigidity argument makes this independent of the realizing orientation. Then
\[
 P_G(z):=\sum_{\tau\;\mathrm{feasible}}z^{h_G(\tau)}
 =2^b\prod_{i=1}^c\bigl(2^{\ell_i-1}-1+z\bigr).
\]
In particular, the number of signatures admitting an acyclic orientation is
\[
 N_{\mathrm{acyc}}(G)=2^b\prod_{i=1}^c(2^{\ell_i-1}-1),
\]
and for each such signature all \(2^c\) realizing orientations are acyclic. Empty products equal one. The one-vertex graph and trees are included.

## Assumptions and scope
Graphs are finite, connected, undirected and simple, with at least one vertex. A directed cycle is an orientation of an undirected simple cycle with all its edges following one cyclic direction. A signature \(\tau:V\to\{0,1\}\) is *feasible* if some orientation realizes it; this holds exactly when \(\sum_{v\in V}\tau(v)\equiv |E|\pmod 2\). For a cactus, \(c=|E|-|V|+1\). The polynomial counts **signatures**, not individual orientations; multiplying its coefficients by \(2^c\) gives the corresponding orientation counts. The theorem does not assert rigidity for all graphs containing overlapping cycles: it proves the converse fails there.

## Proof
**Lemma 1 (parity fibres are cycle-space cosets).** Fix a reference orientation and encode another by a bit on each edge specifying reversal. Reversing an edge toggles indegree parity at both its endpoints. Hence two orientations have the same signature if and only if their reversal-edge set has even degree at every vertex, namely lies in the binary cycle space. The incidence matrix of a connected graph has rank \(|V|-1\) over \(\mathbf F_2\): a spanning-tree leaf elimination proves this, including the one-vertex case. Therefore precisely \(2^{|V|-1}\) signatures are feasible, characterized by the stated sum parity, and every fibre has \(2^{|E|-|V|+1}\) orientations.

**Lemma 2 (cactus fibres preserve directed cycles).** For a cactus its \(c\) simple cycles have disjoint edge sets and form a cycle-space basis: they are independent by disjointness and their number equals the cycle-space dimension. Consequently, two orientations in one signature fibre differ by reversing all edges of a subset of these cycles. On reversing every edge of one cycle, that cycle is coherently directed before the reversal if and only if it is coherently directed afterward; cycles not reversed are unchanged because their edge sets are disjoint. There are no other undirected simple cycles in a cactus. Thus the list of directed simple cycles, and in particular their number and existence, is constant throughout a fibre. This proves rigidity in the cactus direction.

**Lemma 3 (an overlapping-cycle graph has a mixed fibre).** A finite simple graph is not a cactus exactly when it contains a theta subgraph, consisting of three internally vertex-disjoint paths \(P_1,P_2,P_3\) joining distinct vertices \(u,v\). This follows, for example, by taking two distinct simple cycles sharing an edge and following their first divergence and reconvergence; conversely a theta visibly has edges in two cycles. Direct all three paths from \(u\) to \(v\). This directed theta is acyclic, and its partial orientation extends to an acyclic orientation \(D\) of all of \(G\): first take a topological ordering of the partial directed graph and orient every remaining edge forward in that order. Now reverse precisely the edges in \(P_1\cup P_2\), which form an undirected cycle. Their reversal preserves the indegree-parity signature, by Lemma 1. But the resulting orientation has a directed cycle following \(P_3\) from \(u\) to \(v\) and then \(P_1\) back from \(v\) to \(u\). Thus one parity fibre contains both a cyclic and an acyclic orientation. This proves the converse.

**Polynomial derivation.** For a cactus, every bridge direction is free, contributing a factor \(2\) to the sum over orientations. Each cycle of length \(\ell_i\) has \(2^{\ell_i}\) orientations of its edges. Exactly two are coherently directed; the remaining \(2^{\ell_i}-2\) contribute zero to the directed-cycle count. Since all bridge and cycle edge sets are disjoint, the orientation enumerator weighted by directed cycles is
\[
 \sum_D z^{\#\mathrm{directed\ cycles}(D)}
 =2^b\prod_{i=1}^c\bigl(2^{\ell_i}-2+2z\bigr).
\]
Lemma 2 makes this weight constant on each signature fibre, which has exactly \(2^c\) elements by Lemma 1. Dividing the displayed expression by \(2^c\) gives the asserted signature polynomial. Its constant term counts precisely the signatures whose whole fibre is acyclic. Substitution \(z=1\) recovers \(2^{|V|-1}\), providing an independent normalization check. This completes both the characterization and the census.

## Verification
The standalone standard-library program `verify_cactus.py` explicitly enumerates all orientations of several trees, single cycles, and multi-cycle cacti, checking both fibre sizes and every coefficient of the stated polynomial. It also explicitly enumerates **all 772 labeled connected simple graphs on at most five vertices**, determines cactus status by listing undirected cycles, and tests fibrewise acyclicity directly with a directed-graph topological-sort algorithm. It finds 399 cacti and 373 non-cacti, with the characterization holding in all cases. Execute `python3 verify_cactus.py` from the directory containing this document and the program. These finite tests are checks, not substitutes for the general proof.

## Relationship to prior work
The March 2026 paper of Gravier, Petiteau and Sivignon formulates acyclic orientations with prescribed indegree parities, gives necessary conditions and constructive solutions for certain graph families, particularly Cartesian products of paths and cycles. It motivates the present exact cactus-fibre problem; its inspected discussion of those families does not state the cactus rigidity equivalence or this full parity-signature spectrum. Király and Kisfaludi-Bak's 2012 treatment of dual-critical graphs provides earlier structural theory of parity-constrained acyclic orientations, including the special requirement that all but one indegree be odd. Neither that existential condition nor a generic feasible-signature condition implies the present equivalence for all signatures and all graphs. The elementary binary incidence-matrix identity used in Lemma 1 is classical and is not claimed as new.

## Limitations
The rigidity equivalence applies to connected simple graphs; no claim is made about the most useful formulation for loops or multigraphs. The product formula is for cacti, not all graphs with a small cycle rank. The result supplies a complete proof but has not undergone independent scientific assessment. An equivalent result under alternative terminology or in literature not indexed by the searches remains a bibliographic risk.

## References
1. S. Gravier, M. Petiteau, I. Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem*, arXiv:2603.09475v1, first posted 2026-03-10. https://arxiv.org/abs/2603.09475
2. Z. Király, S. Kisfaludi-Bak, *Dual-Critical Graphs — Notes on parity constrained acyclic orientations*, EGRES Technical Report 2012-07, 2012-07-04. https://egres.elte.hu/tr/egres-12-07.pdf
