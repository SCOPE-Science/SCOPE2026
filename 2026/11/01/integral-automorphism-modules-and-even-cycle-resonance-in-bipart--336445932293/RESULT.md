# Integral automorphism modules and even-cycle resonance in bipartite flex homology

## Finding
For every integer \(n\ge3\), let \(G=K_{2,n}\) have hubs \(u,v\) and labeled leaves \(w_1,\ldots,w_n\), and let \(F=\operatorname{Flex}(G)\) be the cubical complex of source/sink flips of edge orientations. Its natural automorphism group is \(\Gamma=S_n\times C_2\), with \(S_n\) permuting leaves and \(\tau\) exchanging the hubs. Denote by \(\mathcal S\) the set of all nonempty subsets of \([n]\), and by \(e_S\) its integral permutation basis. There is a natural \(\Gamma\)-module isomorphism
\[
H_1(F;\mathbb Z)\cong\mathbb Z[\mathcal S],\qquad
\pi e_S=e_{\pi S},\quad
\tau e_S=\begin{cases}
e_{[n]\setminus S},&\varnothing\ne S\ne[n],\\
e_{[n]},&S=[n].
\end{cases}
\]
In particular this module is free abelian of rank \(2^n-1\); the hub exchange acts by **unsigned** transpositions on all proper nonempty subsets, fixing the full subset.

If \(\pi\in S_n\) has \(c\) cycles of lengths \(\ell_1,\ldots,\ell_c\), the complete rational first-homology character is
\[
\operatorname{tr}(\pi\mid H_1(F;\mathbb Q))=2^c-1,\qquad
\operatorname{tr}(\pi\tau\mid H_1(F;\mathbb Q))
=1+\begin{cases}2^c,&2\mid\ell_j\text{ for every }j,\\0,&\text{otherwise}.\end{cases}
\]
Thus the hub-exchange eigenspaces have dimensions \(2^{n-1}\) and \(2^{n-1}-1\), while the subspace fixed by the entire group \(\Gamma\) has dimension \(\lfloor n/2\rfloor+1\). The parity condition for fixed points of a hub exchange combined with a leaf permutation is sharp.

## Assumptions and scope
The graph is the undirected simple complete bipartite graph with two distinguishable hubs and \(n\ge3\) leaves. An orientation chooses one direction per edge. A flex is permitted precisely at a source or a sink, and reverses all incident edges. Independent nonadjacent flexes span the higher-dimensional cubical cells of \(F\). Homology is ordinary integral singular or cubical homology of \(F\), equipped with the natural action of graph automorphisms on orientations and cells; no orientation local system is inserted.

For \(S\subseteq[n]\), define the orientation \(O_S\) by \(w_i\to u\) for every \(i\), together with \(v\to w_i\) for \(i\in S\) and \(w_i\to v\) for \(i\notin S\). Only nonempty \(S\) are used to index homology basis elements. These labels are canonical relative to the chosen hub names and leaf labels.

## Proof
**1. Construct a nontrivial circle in each labeled component.** Fix nonempty \(S\). In \(O_S\), first flex the sink \(u\), then each of the \(w_i\) with \(i\in S\), then the sink \(v\), and finally each leaf with \(i\notin S\). At each stage the vertex being flexed is a sink: after the first flip the leaves in \(S\) receive both incident arrows; after those flips \(v\) receives all incident arrows; after its flip the remaining leaves receive both incident arrows. All \(n+2\) vertices have been flexed exactly once, so every graph edge has reversed twice and the final orientation is again \(O_S\).

Orient each edge of the cubical flex complex from the state where its labeled vertex is a sink to the state where that vertex is a source. Let \(\omega\) be the integer one-cochain evaluating \(+1\) on every such directed edge. The cochain is closed: in any square from two nonadjacent simultaneous flexes, the sink/source status of one vertex is unaffected by the other flip, so the signed contributions on opposite sides cancel. The displayed loop integrates \(\omega\) to \(n+2\ne0\). It therefore represents a nonzero integral first-homology class.

**2. Distinguish the circle components.** The integral edge-orientation signature on any closed walk in the underlying graph is unchanged by a flex: reversing all arcs incident to a single vertex changes the orientation cochain by an integral vertex coboundary. For the oriented graph four-cycle \(u\to w_i\to v\to w_j\to u\), its evaluation at \(O_S\) is \(2(\mathbf1_{j\in S}-\mathbf1_{i\in S})\). These values for all \(i,j\) determine a binary membership vector up to adding a constant. Among nonempty binary subsets they determine \(S\) uniquely: the only two distinct binary vectors differing by a constant are the empty and full vectors, and the empty set has been excluded. Hence the \(2^n-1\) orientations \(O_S\) lie in different connected components of \(F\).

Kozlov's theorem on flex complexes of connected graphs states that every component is either collapsible or collapses onto a circle. The same paper, in its complete-bipartite calculation, establishes that \(\operatorname{Flex}(K_{2,n})\) has exactly \(2^n-1\) circle components (and \(3^n-2^{n+1}+1\) contractible components). Since each \(O_S\) is in a noncontractible component and their number equals the total number of such components, they label **all** the first-homology summands. Every one contributes exactly one integral generator.

**3. Normalize generators and calculate the group action.** On every circle component choose the unique first-homology generator \(e_S\) on which \(\omega\) has positive evaluation. This is well-defined because \(\omega\) is nonzero there. Every graph automorphism maps sinks to sinks and sources to sources, preserving \(\omega\), so it necessarily maps a positive generator to another positive generator, never to its negative.

Leaf relabeling clearly carries \(O_S\) to \(O_{\pi S}\). To track hub exchange, start with \(\tau O_S\), where \(v\) is a sink. Flex \(v\), then the now-sink leaves \(w_i\) for \(i\in S\); the resulting state is \(O_{[n]\setminus S}\) when \(S\ne[n]\). If \(S=[n]\), an additional legal flex at the sink \(v\) yields \(O_{[n]}\) again. Thus the stated complement-with-fixed-full-set action holds on components and, by the positive normalization, on the integral homology basis.

**4. Count fixed basis vectors.** A leaf permutation with \(c\) disjoint cycles preserves a nonempty subset if and only if that subset is a union of cycles. This gives \(2^c-1\) fixed basis elements. For a combined symmetry \(\pi\tau\), the full subset is always fixed. A proper nonempty subset is fixed if and only if its binary membership indicator alternates under \(\pi\). Such an alternating assignment exists precisely when every cycle length of \(\pi\) is even; then each of the \(c\) cycles has two choices, yielding \(2^c\) further fixed subsets. The rational trace equals the number of fixed basis elements because the action is unsigned.

The involution \(\tau\) has one fixed basis element and \(2^{n-1}-1\) swapped pairs, giving its two eigenspace dimensions. Finally, an \(S_n\)-orbit of a subset is determined by its cardinality. The hub exchange identifies cardinalities \(k\) and \(n-k\) for \(1\le k\le n-1\), while leaving the size-\(n\) class fixed. Hence the \(\Gamma\)-orbit count, which is the dimension of the invariant subspace of the permutation module, is \(\lfloor n/2\rfloor+1\).

## Verification
The Python standard-library checker `verify.py` exhaustively constructs the full graph of source/sink flips of all \(2^{2n}\) edge orientations, separately identifies its connected components, and checks the proposed labels and all \(2n!\) graph automorphisms for each \(n=3,4,5\). It separately generates every cubical cell, calculates signed fixed-cell Lefschetz numbers for the automorphisms, and verifies the predicted integral permutation-module characters against the resulting first-homology traces. The completed runs examined 142, 658, and 3,190 cells and respectively 12, 48, and 240 automorphisms. All assertions passed with final output `VERIFY_OK`.

These computations exhaust the displayed finite sizes only. Steps 1–4 above, together with the explicitly credited published component classification, prove the statements for every integer \(n\ge3\).

## Relationship to prior work
Kozlov introduced flex complexes and proved both their connected-component homotopy classification and the \(2^n-1\) number of circle components for \(K_{2,n}\). Those nonequivariant facts are **prior results**, not new claims here. The new content is the canonical positive integral symmetry module, the hub-exchange complement action including its distinguished full-set fixed point, the even-cycle trace resonance, and the invariant-space counts.

Earlier source/sink click-equivalence work of Macauley and Mortveit already establishes general acyclic-orientation equivalence counting and its Tutte-polynomial interpretation; that enumeration is not claimed as new. The published note *A complete cycle-anchor invariant and geodesic formula for graph flexes* gives stronger general connected-component tests and shortest flip distances, but its theorem is not an equivariant homology-module or character classification. The published note *Equivariant homology and symmetry quotients of complete-graph flex complexes* computes such representations for \(K_m\), whose automorphism action and circular-order indexing differ from the bipartite family treated here.

## Limitations
The theorem is for \(K_{2,n}\) with \(n\ge3\) and its particular automorphism group \(S_n\times C_2\); \(K_{2,2}\) has additional graph symmetries and is excluded. It does not compute the automorphism module of degree-zero homology, cover larger complete bipartite graphs \(K_{m,n}\) for \(m\ge3\), classify equivariant homotopy types or quotient spaces, or assert new nonequivariant homology ranks. The finite verifier alone is not a general proof. The possibility of an unindexed equivalent equivariant calculation remains an originality risk.

## References
1. Dmitry N. Kozlov, *Flex complexes of graphs*, Journal of Applied and Computational Topology **10** (2026), article 10; first verified online publication 23 May 2026. DOI: https://doi.org/10.1007/s41468-026-00235-1. In particular Theorem 6.1 and the \(K_{n,2}\) calculation in Section 6.2.
2. Matthew Macauley and Henning S. Mortveit, *Equivalences on Acyclic Orientations*, arXiv:0709.0291, first submitted 3 September 2007; see its source/sink click-equivalence framework.
3. *A complete cycle-anchor invariant and geodesic formula for graph flexes*, publicly available mathematical note, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-complete-cycle-anchor-invariant-and-geodesic-formula-for-graph--adc90e8a9935.
4. *Equivariant homology and symmetry quotients of complete-graph flex complexes*, publicly available mathematical note, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-equivariant-homology-and-symmetry-quotients-of-complete-graph-fl--d33423646847.
