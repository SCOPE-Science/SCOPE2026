# Double-domination polynomials of subdivisions of complete bipartite graphs

## Finding

For integers \(2\le p\le q\), let \(H_{p,q}=S(K_{p,q})\) be the graph obtained by replacing each edge of the complete bipartite graph with a two-edge path. A double dominating set \(D\subseteq V(H_{p,q})\) satisfies \(|N[v]\cap D|\ge2\) for every vertex \(v\), including selected vertices. Define the full cardinality enumerator

\[\mathcal D_{p,q}(z)=\sum_{D\text{ double dominating}}z^{|D|}.\]

Write

\[U_r(z)=(1+z)^r-1\]

and let the ordinary edge-cover polynomial of the underlying complete bipartite graph be

\[E_{p,q}(z)=\sum_{i=0}^{p}\sum_{j=0}^{q}(-1)^{i+j}\binom pi\binom qj(1+z)^{(p-i)(q-j)}.\]

Then the exact double-domination polynomial is

\[\boxed{\begin{aligned}
\mathcal D_{p,q}(z)=z^{p+q}\bigl[&E_{p,q}(z)
 +(U_q(z)+z^{q-1})^p-U_q(z)^p\\
 &+(U_p(z)+z^{p-1})^q-U_p(z)^q\bigr].
\end{aligned}}\]

In particular, the minimum cardinality is the previously established value

\[\gamma_{\times2}(H_{p,q})=p+2q.\]

The *new multiplicity refinement* is

\[\boxed{[z^{p+2q}]\mathcal D_{p,q}(z)=
\begin{cases}
12,&p=q=2,\\
3^q+2q-2,&p=2<q,\\
\displaystyle\sum_{j=0}^{p}(-1)^j\binom pj(p-j)^q,&3\le p\le q.
\end{cases}}\]

For \(p\ge3\), every minimum double dominating set includes all original vertices, and its selected subdivision vertices correspond to a surjection from the \(q\)-vertex part to the \(p\)-vertex part. For \(p=2\), additional minimum configurations omit original vertices; these cause the distinct exponential multiplicity formula.

## Assumptions and scope

All graphs are finite, simple, and undirected. The parts \(A=\{a_1,\ldots,a_p\}\) and \(B=\{b_1,\ldots,b_q\}\) have \(p,q\ge2\). Each original edge \(a_ib_j\) is replaced by \(a_iw_{ij}b_j\), with one new subdivision vertex \(w_{ij}\); there are no other edges. The closed neighborhood \(N[v]\) contains \(v\) itself. Counts distinguish labeled vertex subsets, not graph-automorphism classes. The formula concerns ordinary double domination (at least two), *not* exact/efficient double domination (exactly two). Polynomial coefficients outside the graph's possible cardinality range are zero.

## Proof

**1. Separation of omitted original vertices.** For each subdivision vertex, \(N[w_{ij}]=\{a_i,b_j,w_{ij}\}\). If both \(a_i\) and \(b_j\) were omitted from a double dominating set \(D\), this closed neighborhood would contain at most one member of \(D\). Hence the omitted original vertices lie in at most one bipartition class. There are three mutually exclusive cases: no original omitted, a nonempty subset of \(A\) omitted, or a nonempty subset of \(B\) omitted.

**2. All originals selected.** If \(A\cup B\subseteq D\), then each subdivision vertex is already doubly dominated by its two original endpoints, regardless of its own selection. Each original vertex has no original-vertex neighbors, so, besides itself, it needs at least one selected incident subdivision vertex. Thus the chosen subdivision vertices form precisely an edge cover of \(K_{p,q}\). The case contributes \(z^{p+q}E_{p,q}(z)\). Inclusion-exclusion over uncovered original vertices yields the displayed double sum for \(E_{p,q}\): excluding \(i\) vertices of \(A\) and \(j\) of \(B\) leaves \((p-i)(q-j)\) available edges, each optionally selected.

**3. Omission only from the first part.** Fix a nonempty set \(U\subseteq A\), of cardinality \(u\). Each edge subdivision vertex incident to an omitted \(a_i\) must belong to \(D\), since its closed neighborhood must contain both remaining eligible vertices. Hence exactly \(uq\) subdivision vertices are forced. Every omitted \(a_i\) then has \(q\ge2\) selected neighbors. Every selected original \(b_j\) has at least one of the forced neighbors (because \(u\ge1\)). For each of the remaining \(p-u\) original vertices of \(A\), the selected subdivisions along its row must form an arbitrary *nonempty* subset of the \(q\) incident vertices; these choices are independent. There are \(p+q-u\) selected original vertices. Summing the resulting monomials over the \(\binom pu\) possibilities gives

\[\sum_{u=1}^{p}\binom pu z^{p+q-u+uq}U_q(z)^{p-u}
=z^{p+q}\bigl[(U_q(z)+z^{q-1})^p-U_q(z)^p\bigr].\]

Conversely, all these configurations satisfy each closed-neighborhood requirement, including those of selected and unselected subdivision vertices. The case with nonempty omissions from \(B\) is symmetric, contributing

\[z^{p+q}\bigl[(U_p(z)+z^{p-1})^q-U_p(z)^q\bigr].\]

The three cases are disjoint and exhaustive, proving the polynomial identity for all \(p,q\ge2\).

**4. Minimal cardinality and all minimizers.** In the all-original case, the fewest subdivisions form an edge cover of \(K_{p,q}\), whose minimum size is \(q\) when \(p\le q\). A size-\(q\) edge cover chooses precisely one edge incident with each vertex of \(B\), and all \(p\) vertices of \(A\) must occur; equivalently this is a surjection \(B\to A\). Its multiplicity is \(\sum_{j=0}^{p}(-1)^j\binom pj(p-j)^q\).

If \(u\ge1\) original vertices of \(A\) are omitted, the minimum size within that fixed-\(u\) class is

\[2p+q+u(q-2),\]

since each of the \(p-u\) remaining rows must contribute at least one subdivision. If \(v\ge1\) original vertices of \(B\) are omitted, the analogous minimum is

\[p+2q+v(p-2).\]

For \(p\ge3\), both omitted-original minima exceed \(p+2q\) by at least \(p-2>0\). Thus the only minimum sets are the surjection constructions.

For \(p=2<q\), the all-original case supplies \(2^q-2\) minima. Omitting exactly one original from \(A\) supplies \(2q\) additional minima. Omitting a nonempty set of \(v\) vertices from \(B\), for any \(1\le v\le q\), supplies \(\binom qv2^{q-v}\) minima. Their sum is

\[(2^q-2)+2q+(3^q-2^q)=3^q+2q-2.\]

Finally, when \(p=q=2\), omitting both vertices from either original part supplies one additional minimum configuration on each side, beyond the preceding count. This gives \(12\) minimum sets. The displayed case distinction follows and independently proves the minimum cardinality \(p+2q\).

## Verification

An independently coded brute-force enumerator constructs \(H_{p,q}\) from its edges and tests \(|N[v]\cap D|\ge2\) for every vertex and every subset. The standalone script `verify_double_subdivision.py` reconstructs the polynomial using inclusion-exclusion and the three-case formula, and compares its coefficients against the adjacency-based exhaustive oracle for \((p,q)\) equal to \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)\). These are \(1,755,392\) subsets across seven graphs. It also checks the minimum multiplicity for 52 further parameter pairs by independent integer calculations. All performed tests pass. Representative polynomials are

\[\mathcal D_{2,2}(z)=12z^6+8z^7+z^8,\]
\[\mathcal D_{2,3}(z)=31z^8+34z^9+11z^{10}+z^{11}.\]

Run `python3 verify_double_subdivision.py` with Python 3 and no third-party dependencies. The exhaustive tests prove the recorded finite cases only; the combinatorial argument above establishes the formula for all allowed parameters.

## Relationship to prior work

Behtoei and Zarifian (arXiv:2408.05783, first posted 11 August 2024, especially Section 2 and Theorem 5) characterize when subdivision graphs admit *exact* doubly dominating sets, where each closed neighborhood meets the set in exactly two vertices. The condition here is *at least* two, and the theorem counts all such sets by cardinality. Their exact-existence characterization cannot enumerate the non-exact double dominating sets.

Magima and Ragukumar (DOI:10.7546/nntdm.2024.30.3.640-653, online 25 October 2024, Section 2.6, Theorem 2.19) give \(\gamma_{\times2}(S(K_{p,q}))=p+2q\) for \(p\le q\). That scalar value is not claimed to be new. Their theorem does not supply the full polynomial, a classification of every double dominating set, or minimum-set counts.

Akbari and Oboudi's edge-cover polynomial is a known invariant. The term \(E_{p,q}(z)\) in this work is therefore not claimed as a new edge-cover identity. The new part is the precise three-case transfer from double domination to edge covers and forced-subdivision choices, together with the full distribution and sharp multiplicity transition at the smaller part of size two. The 2023 work on double domination of rooted products concerns a different graph operation and is not a general enumeration theorem for these subdivision graphs.

## Limitations

The formulas apply to one-step subdivisions of complete bipartite graphs with both parts of cardinality at least two. They do not address arbitrary subdivisions, complete multipartite graphs, more than one inserted vertex per edge, or exact doubly dominating sets. Some potentially equivalent terminology (closed-neighborhood two-fold covering; \(2\)-tuple domination) may index further literature. Searches and primary-text comparisons cannot certify global uniqueness or priority. Independent review is not yet performed.

## References

1. A. Behtoei and R. Zarifian, *Exact double domination in subdivision, Mycielskian and middle graphs*, arXiv:2408.05783v1, submitted 2024-08-11. https://arxiv.org/abs/2408.05783 and https://arxiv.org/pdf/2408.05783 .
2. M. Magima and P. Ragukumar, *Double domination number of graphs generated from unary products*, Notes on Number Theory and Discrete Mathematics 30 (2024), 640–653, DOI:10.7546/nntdm.2024.30.3.640-653, online 2024-10-25. https://nntdm.net/papers/nntdm-30/NNTDM-30-3-640-653.pdf .
3. A. Cabrera-Martínez and A. Estrada-Moreno, *Double domination in rooted product graphs*, Discrete Applied Mathematics 339 (2023), 127–135, DOI:10.1016/j.dam.2023.06.021; public conference exposition dated 2023-05-26: https://xiiieamd.uca.es/wp-content/uploads/2023/06/Alejandro-Estrada-Moreno.pdf .
4. S. Akbari and M. R. Oboudi, *On the edge cover polynomial of a graph*, edge-cover polynomial definition and results: https://janos.cs.technion.ac.il/COURSES/236603-11/oboudi.pdf .
