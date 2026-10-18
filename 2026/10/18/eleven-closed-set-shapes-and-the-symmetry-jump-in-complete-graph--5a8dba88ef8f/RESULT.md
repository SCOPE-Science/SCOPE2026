# Eleven closed-set shapes and the symmetry jump in complete-graph edge-overlap concept lattices

## Finding
Fix an integer \(n\ge4\), let \(V=[n]\), and let \(E=\binom V2\). Form the symmetric formal context with both objects and attributes indexed by \(E\), with incidence \(e\,I\,f\) if and only if \(e\cap f\ne\varnothing\). Incidence includes \(e\,I\,e\). Define the polarity
\[
P(B)=\{e\in E:\forall f\in B,\ e\cap f\ne\varnothing\},\qquad c(B)=P(P(B)).
\]
A closed intent means \(c(B)=B\). The complete list of closed intents, regarded as subgraphs of the complete graph on \(V\), is:

1. The empty edge set, any single edge, or any two-edge set (adjacent or disjoint).
2. Any three-edge path on four vertices; any four-cycle; or any triangle.
3. A full star \(S_v=\{\{v,w\}:w\in V\setminus\{v\}\}\).
4. A full star plus an edge between two leaves, \(S_v\cup\{\{a,b\}\}\) for distinct \(a,b\ne v\).
5. The union \(S_u\cup S_v\) of two distinct full stars.
6. The entire set \(E\).

These are distinct families for each \(n\ge4\). Their exact number, hence the number of formal concepts, is
\[
C_n=2+2\binom n2+\binom{\binom n2}{2}+\binom n3+15\binom n4+n+n\binom{n-1}{2}.
\]
In particular \(C_4=64\), \(C_5=187\), \(C_6=448\), and \(C_n=\tfrac34 n^4+O(n^3)\).

The entire order-preserving automorphism group is
\[
\operatorname{Aut}(\mathcal L_n)\cong
\begin{cases}
\mathfrak S_6,&n=4,\\
\mathfrak S_n,&n\ge5.
\end{cases}
\]
The lattice is distributive and modular at \(n=4\), and neither modular nor distributive for \(n\ge5\). At \(n=3\), every edge meets every edge, giving a one-element concept lattice.

## Assumptions and scope
The graph is the simple complete graph on the finite vertex set \(V\). The relation is **nonempty overlap**, including incidence of each edge with itself; the disjointness relation defines a different formal context. There are no vertex labels or order relations in the language of the concept lattice itself. An intent is a subset of the \(\binom n2\) attributes. The usual concept lattice is ordered by inclusion of extents, equivalently reverse inclusion of closed intents; reversing the order does not alter its order-automorphism group or the modularity/distributivity properties.

## Proof
**Polarity classification.** Because incidence is symmetric, \(P^3=P\); consequently the closed intents are precisely the sets \(P(B)\) for \(B\subseteq E\). If \(B=\varnothing\), then \(P(B)=E\). Suppose next that all pairs of edges in \(B\) intersect. Every family of pairwise intersecting two-element subsets is either contained in a vertex-star or contained in a triangle: indeed, if it contains \(\{a,b\}\) and \(\{a,c\}\), an edge avoiding \(a\) and meeting both must equal \(\{b,c\}\). Explicitly, a singleton family has polar \(S_a\cup S_b\); a family of two distinct adjacent edges \(\{a,b\},\{a,c\}\) has polar \(S_a\cup\{\{b,c\}\}\); a star-family with at least three distinct edges has polar \(S_a\); and the three edges of a triangle have polar that same triangle. This exhausts all pairwise-intersecting nonempty families.

If \(B\) contains two disjoint edges \(\{a,b\}\) and \(\{c,d\}\), every edge in \(P(B)\) joins one vertex of \(\{a,b\}\) to one vertex of \(\{c,d\}\). Thus \(P(B)\) is a subset of the four edges of a \(4\)-cycle. Conversely **every** subset of these four edges is a polar: start with the two disjoint edges, and for each cross edge to be excluded add its uniquely disjoint opposite cross edge to \(B\). Each chosen retained cross edge meets all these added edges, because opposite pairs are the only disjoint pairs within that \(4\)-cycle. Hence every subset of a \(4\)-cycle occurs as \(P(B)\). Subsets of four-cycle edge sets are exactly the empty set, singletons, arbitrary pairs, three-edge paths, and full four-cycles. Combining both cases proves the complete list.

**Counting.** Write \(m=\binom n2\). There is one empty set, \(m\) singletons, \(\binom m2\) two-edge sets, \(12\binom n4\) three-edge paths (choose four vertices and one of twelve labeled paths), \(3\binom n4\) four-cycles, \(\binom n3\) triangles, \(n\) full stars, \(n\binom{n-1}2\) full stars with a chord between two leaves, \(m\) unions of two full stars, and one full edge set. These families have distinct shapes, except for the two categories of two-edge sets which were counted together, giving the asserted formula.

**Automorphisms.** At \(n=4\), the formula gives all \(2^{\binom42}=64\) subsets as closed intents; hence the concept lattice is the six-atom Boolean lattice and its automorphism group is \(\mathfrak S_6\). For \(n\ge5\), singletons are precisely the atoms in the inclusion-ordered closed-intent lattice, and every closed set is their join. Therefore an automorphism induces a permutation of the edge set \(E\). For two distinct edges \(e,f\), count third edges \(g\) for which the three-element edge set \(\{e,f,g\}\) is **itself closed** (not merely its closure). The classification shows that these are exactly triangles and three-edge paths. If \(e,f\) intersect, there are \(2(n-3)+1=2n-5\) choices; if they are disjoint, there are exactly four. Since \(2n-5\ne4\) for integral \(n\ge5\), the lattice recovers whether \(e\) and \(f\) intersect. Thus every lattice automorphism induces an automorphism of the line graph of the complete graph. In that line graph, any clique of at least four vertices is contained in a full vertex-star: a pairwise-intersecting family of at least four edges of a simple graph must share a common endpoint. The maximal cliques of size at least four are therefore precisely the \(n\) full stars. Their incidence recovers the original vertex set, forcing the edge permutation to arise from a permutation of \(V\). Conversely every permutation of \(V\) preserves incidence and induces a lattice automorphism. This proves \(\operatorname{Aut}(\mathcal L_n)\cong\mathfrak S_n\).

**Modularity.** For \(n\ge5\), choose five vertices \(0,1,2,3,4\). In the inclusion-ordered closed-intent lattice set \(X=\{\{0,1\},\{0,2\}\}\), \(Z=S_0\), and \(Y=\{\{3,4\}\}\). Then \(X\subseteq Z\), \(Y\wedge Z=\varnothing\), while
\[
X\vee Y=c(X\cup Y)=S_0\cup\{\{3,4\}\}.
\]
Therefore \(X\vee(Y\wedge Z)=X\), but \((X\vee Y)\wedge Z=S_0\ne X\). The modular identity fails, as does distributivity. At \(n=4\), the lattice is Boolean and hence both modular and distributive.

## Verification
The standalone standard-library script `verify_overlap_context.py` independently computes polarities from the complete incidence matrix and compares them to the claimed shapes for \(3\le n\le9\). It exhausts all \(2^{\binom n2}\) initial attribute sets through \(n=6\), recomputes closed sets from arbitrary neighborhood intersections through \(n=9\), and counts witness triples that distinguish intersecting from disjoint edges. Expected output ends with:

```
VERIFY_OK generated_concepts=6283 exhaustive_initial_sets=33864 line_graph_pair_witnesses=1368 n=3..9 direct_classification=PASS automorphism_invariants=PASS
```

The finite checks corroborate the enumerative and closure assertions; only the argument above proves all parameter values. The script is a standalone artifact in this package and does not require external datasets or libraries.

## Relationship to prior work
Standard formal concept analysis defines the polarity and closure used here. Zhang, Mi, Li and Liang (2019) study neighborhood-based attribute reduction in formal decision contexts, rather than this exact symmetric edge-overlap context. Rawson, Myers, Green, Robinson and Joslyn (2023) connect hypergraph intersection complexes with concept lattices and give general algorithms; their available abstract does not exhibit the present complete-graph edge-overlap count, the eleven-shape classification, or the exceptional automorphism group. Zhou et al. (2021) study general formal-concept enumeration algorithms rather than an exact family classification.

This context must be distinguished from the Kneser **disjointness** context on two-element subsets. The latter has a different Galois closure; results about its rank-band closed sets do not yield the present overlap context by a trivial complement of a closed intent. The novelty assessment concerns this precise classification and automorphism transition, not basic polarity or line-graph facts.

## Limitations
The classification applies to all two-element subsets of a complete graph and their reflexive overlap relation; it is not a formula for arbitrary line graphs, noncomplete base graphs, or disjointness contexts. The mathematical proof has not received independent external audit. The 2023 hypergraph/concept-lattice preprint was compared at abstract level only, not in full text, leaving residual publication-priority uncertainty. Search noncoverage is not a proof of priority.

## References
- Zhang, Mi, Li and Liang (2019), *Neighbourhood systems based attribute reduction in formal decision contexts*, DOI: 10.1049/trit.2019.0039. First public date used here: 2019-12-09. https://doi.org/10.1049/trit.2019.0039
- Rawson, Myers, Green, Robinson and Joslyn (2023), *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681, publicly posted 2023-07-21. https://arxiv.org/abs/2307.11681
- Zhou, Yang, Wang and Liu (2021), *A New Algorithm based on Extent Bit-array for Computing Formal Concepts*, arXiv:2111.00003, publicly posted 2021-10-29. https://arxiv.org/abs/2111.00003
