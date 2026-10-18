# Unique-matching census of minimum zero-forcing sets in subdivided helms

## Finding

For every integer \(m\ge3\), form a graph \(G_m\) from a wheel on \(m\) rim vertices by subdividing each rim edge once and attaching one private pendant leaf to each original rim vertex. More precisely, with cyclic indices \(i\in\mathbb Z/m\mathbb Z\), its vertices are \(h,v_i,x_i,p_i\), and its edges are exactly \(hv_i\), \(v_ix_i\), \(x_iv_{i+1}\), and \(v_ip_i\). Thus \(|V(G_m)|=3m+1\).

Let \(Z(G_m)\) be the ordinary zero-forcing number and let \(N_m\) count labeled minimum zero-forcing vertex subsets. Then

\[
Z(G_m)=m+1,
\qquad
\sum_{m\ge3}N_m t^m=
\frac{t^3(24-92t+101t^2-42t^3+6t^4)}{(1-t)(1-3t+t^2)^2}.
\]

In particular, \((N_3,N_4,N_5,N_6,N_7,N_8)=(24,76,225,649,1848,5220)\). For \(m\ge8\), these numbers obey the exact order-five recurrence

\[
N_m=7N_{m-1}-17N_{m-2}+17N_{m-3}-7N_{m-4}+N_{m-5}.
\]

All minimum zero-forcing sets are characterized by the unique-perfect-matching criterion below. This supplies a static certificate for every optimum, not just its total number.

## Assumptions and scope

The graphs are finite, simple and undirected, with ordinary zero forcing: initially chosen vertices are blue; a blue vertex with exactly one white neighbor may color that neighbor blue. A zero-forcing set colors every vertex blue after finitely many such steps. All vertices and leaves are distinguished by their cyclic indices. The theorem holds for every \(m\ge3\) without any parity restriction. The generating function uses formal power series over \(\mathbb Q\).

Set \(U=\{v_i:i\in\mathbb Z/m\mathbb Z\}\) and \(W=\{h\}\cup\{x_i,p_i:i\in\mathbb Z/m\mathbb Z\}\). Every minimum set is contained in \(W\). For \(B\subseteq W\) with \(|B|=m+1\), define

\[
T=\{i:p_i\in B\},\qquad
Q=(\{h\}\cup\{x_i:i\in\mathbb Z/m\mathbb Z\})\setminus B.
\]

These sets have equal cardinality \(|T|=|Q|\). Let \(J(T,Q)\) be the bipartite graph with shores \(T,Q\); an index \(i\in T\) is adjacent to \(h\) (if present), and to \(x_i,x_{i-1}\) whenever those vertices belong to \(Q\). Then \(B\) is a minimum zero-forcing set **if and only if** \(T\ne\varnothing\) and \(J(T,Q)\) has a unique perfect matching. The perfect matching condition automatically excludes \(T=\mathbb Z/m\mathbb Z\).

For any nonempty proper \(T\subset\mathbb Z/m\mathbb Z\), let \(\ell_1,\ldots,\ell_k\) be lengths of its maximal cyclic runs of consecutive indices. The number of minimum forcing sets with precisely those pendant leaves initially blue equals

\[
\prod_{j=1}^k(\ell_j+1)
+\sum_{j=1}^k \ell_j\prod_{r\ne j}(\ell_r+1).
\]

The first term counts sets with initially blue hub, and the second those with initially white hub.

## Proof

**Lower bound and forced shore.** The adjacency matrix in the bipartition \(U\cup W\) is \(A=\begin{psmallmatrix}0&M\\M^{\mathsf T}&0\end{psmallmatrix}\), with \(M\) of size \(m\times(2m+1)\). The columns corresponding to the private leaves form an identity matrix, hence \(\operatorname{rank}M=m\) and \(\dim\ker A=(3m+1)-2m=m+1\). In fact every kernel vector vanishes on \(U\). For any zero-forcing set \(B\), restriction of vectors in \(\ker A\) to the coordinates in \(B\) is injective: if a kernel vector vanishes on the initially blue vertices, the equation at a forcing vertex forces it to vanish also on the unique white neighbor, inductively. Consequently \(|B\cap W|\ge m+1\), and \(|B|\ge m+1\). Equality requires \(B\subseteq W\).

**Attainment.** Initially color every \(x_i\) and one leaf \(p_0\) blue. The leaf forces \(v_0\); blue subdivision vertices successively force all other rim vertices around the cycle; the blue rim vertex \(v_0\), whose remaining white neighbor is \(h\), forces the hub; and then each other rim vertex forces its private pendant leaf. Hence \(Z(G_m)=m+1\).

**Unique-matching equivalence.** Assume \(B\subseteq W\) and \(|B|=m+1\). If \(T=\varnothing\), no initially blue vertex can force: each blue subdivision vertex has two white rim neighbors and the blue hub has \(m\ge3\) white rim neighbors. Thus \(T\ne\varnothing\) is necessary. The blue leaves immediately force all \(v_i\) with \(i\in T\). The initially white vertices of \(W\) consist of \(Q\) and the pendant leaves with indices outside \(T\). An initially white pendant leaf \(p_j\), \(j\notin T\), can only be colored by \(v_j\), and that coloring must happen after all \(v_j\)'s neighbors in \(Q\) have become blue. Hence no rim vertex with index outside \(T\) can ever force a vertex of \(Q\). Every vertex of \(Q\) must therefore be forced by a distinct rim vertex indexed in \(T\), because each forcing vertex can force at most once. These forces give a perfect matching of \(J(T,Q)\). At the time a matched rim vertex forces its partner, all its other neighbors in \(Q\) are already blue. A second perfect matching would create an alternating cycle, on which these strict chronological inequalities form an impossible directed cycle. The matching is unique.

Conversely, suppose \(T\ne\varnothing\) and \(J(T,Q)\) has a unique perfect matching. A bipartite graph with a unique perfect matching has a degree-one vertex in the \(T\)-shore: orient every nonmatching incidence from its \(T\)-vertex toward the \(T\)-vertex matched to its other endpoint; an oriented cycle would give an alternating cycle and another matching, so this directed graph has a sink. That sink is adjacent to only its own matched vertex of \(Q\). Since its rim vertex was colored by its blue pendant leaf, it may force its partner in \(Q\). Delete the matched pair from the bookkeeping graph and repeat. This colors all of \(Q\) blue. Now the hub and every \(x_i\) are blue. Starting from any blue \(v_i\) with \(i\in T\), the blue subdivision vertices sequentially color every rim vertex along the cycle. Each remaining rim vertex then forces its sole white neighbor, its pendant leaf. Thus \(B\) is zero forcing.

**Counting the unique matchings.** For proper nonempty \(T\), consider a maximal run of \(\ell\) consecutive selected-leaf indices. Exactly \(\ell+1\) subdivision vertices touch its rim vertices: the two boundary subdivision vertices and the \(\ell-1\) internal ones. Different runs have disjoint sets of incident subdivision vertices. An element of \(Q\) must meet \(T\) to participate in a perfect matching.

If \(h\notin Q\), every run must contribute exactly \(\ell\) subdivision vertices to \(Q\). Any one of its \(\ell+1\) possible omissions leaves a path-like incidence graph with a unique perfect matching, producing \(\prod(\ell_j+1)\) possibilities.

If \(h\in Q\), exactly one run of length \(\ell_j\) contributes \(\ell_j-1\) subdivision vertices, and every other run contributes its full length. Within the deficient run, two of the \(\ell_j+1\) subdivision vertices are omitted. If their positions are nonconsecutive, the rim interval between them has at least two vertices, each of which can be matched to \(h\), producing at least two perfect matchings. If the omissions are consecutive, their unique common rim vertex is isolated from the selected subdivision vertices and must match \(h\); all remaining incidence paths have uniquely forced matchings. There are exactly \(\ell_j\) consecutive omission pairs. Summing over the deficient run gives the stated second term.

For \(T\) equal to the whole cycle, the no-hub case gives the cyclic incidence graph with two perfect matchings; with hub, exactly one subdivision vertex is omitted, leaving a path whose rim vertices offer \(m\) possible hub partners. Neither case has a unique perfect matching. Together with the empty-set obstruction this completes the classification and enumeration.

**Generating function.** A nonempty proper cyclic binary selection decomposes into \(k\ge1\) alternating positive-length one-runs and zero-runs. Define

\[
a(t)=\sum_{\ell\ge1}(\ell+1)t^\ell=\frac{t(2-t)}{(1-t)^2},\quad
b(t)=\sum_{\ell\ge1}\ell t^\ell=\frac{t}{(1-t)^2},\quad
g(t)=\frac{t}{1-t}.
\]

For fixed run and gap lengths summing to \(m\), there are \(m/k\) labeled cyclic placements (each word has exactly \(k\) designated starts of one-runs). Therefore the hub-blue contribution is encoded by \(t\frac{d}{dt}[-\log(1-ag)]\), while the hub-white contribution is encoded by \(t\frac{d}{dt}[bg/(1-ag)]\). Since

\[
1-ag=\frac{1-3t+t^2}{(1-t)^3},\qquad \frac{bg}{1-ag}=\frac{t^2}{1-3t+t^2},
\]

the sum simplifies to

\[
\frac{t^2(6-18t+10t^2-t^3)}{(1-t)(1-3t+t^2)^2}.
\]

This formal cyclic construction has an artificial \(6t^2\) term at length two, where no simple wheel exists. Removing that term yields exactly the asserted generating function for \(m\ge3\). Multiplication by its denominator proves the recurrence and stated initial counts.

## Verification

A standalone independent enumerator, `hybrid_forcing_verify.py`, uses the ordinary forcing rule on the actual graph, enumerates every potential initial set of size \(m+1\) for \(3\le m\le7\), and compares feasibility with the matching characterization. It checks \(379663\) such labeled subsets, independently counts the resulting optima, and compares the run formula with the rational generating function through \(m=15\). The recorded output is provided as `hybrid_forcing_verify_output.txt`.

The proof, including the all-parameter lower bound, does not depend on extrapolating these finite checks.

## Relationship to prior work

Anderton et al., arXiv:2310.18513 (first public preprint 2023-10-27), determine zero-forcing numbers and propagation times for gear graphs and helm graphs separately. Their conclusion explicitly proposes studying the combination obtained by adding both intermediate rim vertices and pendant leaves to a wheel. The present graph is the smallest uniform such combination, with one inserted vertex per rim edge and one pendant leaf per spoke. Their zero-forcing formulas for either separate family do not provide this graph's minimum-set enumeration. Geneson, Haas and Hogben, arXiv:2009.00220 (2020), introduce zero-forcing reconfiguration graphs; no assertion about the complete minimum-set census of this hybrid family is used. The kernel-injectivity argument is standard background, not claimed as new. The contribution here is the complete static classification, cyclic run census, and rational generating function for the hybrid family.

## Limitations

This theorem treats one subdivision per original rim edge and one pendant leaf at each original rim vertex. It does not address arbitrary numbers of subdivisions or leaves, propagation times, the token-jumping reconfiguration graph, or all zero-forcing sets of nonminimum sizes. Novelty was compared against accessible primary literature and research records; unindexed or inaccessible equivalent results remain a priority risk. Independent expert validation has not been performed.

## References

1. S. Anderton et al., *The zero forcing numbers and propagation times of gear graphs and helm graphs*, arXiv:2310.18513v1 (2023-10-27), https://arxiv.org/abs/2310.18513; revised version 2024-04-14, https://arxiv.org/html/2310.18513.
2. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (2020-09-01), https://arxiv.org/abs/2009.00220.
3. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648.
