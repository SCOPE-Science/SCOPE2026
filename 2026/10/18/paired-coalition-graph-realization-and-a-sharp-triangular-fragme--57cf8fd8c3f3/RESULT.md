# Paired-coalition graph realization and a sharp triangular fragmentation law for bicliques

## Finding
Let \(G=K_{m,n}\) be a complete bipartite graph with labeled bipartition \(A\sqcup B\), where \(m=|A|\ge1\) and \(n=|B|\ge1\). A **paired-coalition partition** \(\pi\) is a partition of its vertices into nonempty blocks, none of which is paired-dominating, but every block has a different block with which it forms a paired-dominating union. The associated **paired-coalition graph** \(\operatorname{PCG}(G,\pi)\) has the blocks as its vertices and joins partners.

**Realization theorem.** The graph \(H\) is isomorphic to \(\operatorname{PCG}(G,\pi)\) for some paired-coalition partition of \(K_{m,n}\) if and only if \(H\) is a nonempty disjoint union of complete bipartite graphs,
\[
H\cong\bigsqcup_{j=1}^{c}K_{p_j,q_j},\qquad p_j,q_j\ge1,
\]
and there exist pairwise distinct positive integers \(d_1,\ldots,d_c\), choices of which side of each component corresponds to positive imbalance (so \(p_j\) and \(q_j\) may be swapped independently), and a nonnegative integer \(t\) satisfying
\[
m=t+\sum_{j=1}^c d_jp_j,\qquad
n=t+\sum_{j=1}^c d_jq_j.
\]

**Sharp fragmentation.** If \(\kappa(\pi)\) denotes the number of connected components of \(\operatorname{PCG}(G,\pi)\), then
\[
\max_{\pi}\kappa(\pi)=
\left\lfloor\frac{\sqrt{8\min\{m,n\}+1}-1}{2}\right\rfloor.
\]
Indeed the attained component-count spectrum is every integer from \(1\) to this maximum. If \(m=n=T_c=c(c+1)/2\), the number of paired-coalition partitions with \(c\) components is exactly
\[
\left(\frac{T_c!}{\prod_{j=1}^{c}j!}\right)^2.
\]
These are partitions of labeled vertices with **unlabeled** blocks, not merely isomorphism classes of coalition graphs.

**Enumeration theorem.** The following finite-coefficient formula records all these partitions jointly by number of connected components and number of blocks. For \(d\ge1\), set
\[
B_d(x,y)=\sum_{r\ge0}\frac{x^{d+r}y^r}{(d+r)!r!}.
\]
Let \(N_{m,n}(c,k)\) be the number of paired-coalition partitions \(\pi\) of \(K_{m,n}\) with exactly \(c\) coalition-graph components and \(k\) blocks. Then
\[
\boxed{\quad N_{m,n}(c,k)=m!n!\,[x^my^nu^cz^k]
\prod_{d\ge1}\bigl(1+u(e^{zB_d(x,y)}-1)
(e^{zB_d(y,x)}-1)\bigr).\quad}
\]
The infinite product is formal: only indices \(d\le\min\{m,n\}\) can contribute to this coefficient.

## Assumptions and scope
All graphs are finite, simple, and undirected. The two color classes \(A,B\) of \(K_{m,n}\) consist of distinguishable vertices; the graph family includes stars and \(K_{1,1}\). A paired-dominating set is a dominating vertex set whose induced subgraph has a perfect matching. Neither blocks nor components are ordered. A paired-coalition graph is not the same notion as the original graph's ordinary coalition graph, which uses domination without a matching condition. Each maximizing partition in the theorem refers to the number of **coalition-graph connected components**, not the paired-coalition number (maximum number of blocks).

## Proof
**1. Signed imbalance gives the exact partner relation.** For any nonempty vertex set \(S\subseteq A\sqcup B\), put
\[
a(S)=|S\cap A|,\quad b(S)=|S\cap B|,\quad\delta(S)=a(S)-b(S).
\]
The induced subgraph of \(S\) is the complete bipartite graph with part sizes \(a(S)\) and \(b(S)\). It admits a perfect matching precisely when \(a(S)=b(S)>0\). In that case \(S\) also dominates the entire graph, as it meets both partite classes; therefore
\[
S\text{ is paired-dominating}\quad\Longleftrightarrow\quad\delta(S)=0.
\]
(The possibility \(S=\varnothing\), also balanced, is excluded.) For two **disjoint nonempty** blocks \(X,Y\) which are not paired-dominating, their union is paired-dominating precisely when
\[
\delta(X)+\delta(Y)=0.
\]
In a paired-coalition partition every block has nonzero imbalance, and each imbalance \(d>0\) that appears must be accompanied by \(-d\). Conversely these conditions suffice to make every block have a partner. For each such \(d\), every positive-\(d\) block is adjacent to every negative-\(d\) block and to no other block. The coalition graph is consequently a disjoint union of complete bipartite graphs, with one component per distinct positive magnitude \(d\).

**2. The numerical realization criterion.** Write \(p_d\) for the number of blocks with imbalance \(d>0\) and \(q_d\) for those with imbalance \(-d\). Every positive-\(d\) block has exactly \(d\) more \(A\)-vertices than \(B\)-vertices, and each negative-\(d\) block has exactly \(d\) more \(B\)-vertices than \(A\)-vertices. Define its nonnegative **neutral count** as the smaller of these two populations, and put \(t\) equal to the sum of the neutral counts over all blocks. Summing the populations yields
\[
m=\sum_d d p_d+t,\qquad n=\sum_d d q_d+t.
\]
This proves necessity, including the possible exchange of which side of a component is the positive one. For sufficiency, given a solution of the numerical equations, form \(p_d\) disjoint monochromatic \(A\)-blocks each of size \(d\) and \(q_d\) disjoint monochromatic \(B\)-blocks each of size \(d\). The remaining \(t\) vertices from each partite class can be added together to any one block (or distributed in balanced pairs). This leaves all imbalances unchanged, gives a genuine partition of all vertices, and realizes exactly the required coalition graph.

**3. Sharp upper bound and existence at every count.** If there are \(c\) connected components, their positive magnitudes are distinct, say \(1\le d_1<\cdots<d_c\). Since each component contains at least one positive and one negative block, it consumes at least \(d_j\) vertices on **each** side. Hence
\[
\min\{m,n\}\ge\sum_{j=1}^{c}d_j\ge\sum_{j=1}^{c}j
=\frac{c(c+1)}2.
\]
Conversely let \(1\le c\) satisfy this inequality and put \(T_c=c(c+1)/2\). For each \(d=1,\ldots,c\), take one pure \(A\)-block and one pure \(B\)-block of size \(d\). Without loss of generality, suppose \(m\ge n\). Add \(m-n\) extra singleton \(A\)-blocks (all joining the \(d=1\) coalition component) and place the remaining \(n-T_c\) vertices of each partite class together into an existing block. The resulting coalition graph has exactly \(c\) components. This proves the sharp maximum and all smaller positive attainable counts.

**4. Triangular equality and its exact multiplicity.** If \(m=n=T_c\) and \(c\) components occur, equality must hold in each of the two nonnegative inequalities in Step 3. Therefore the distinct magnitudes are exactly \(1,2,\ldots,c\), and each one has precisely one positive and one negative block, no neutral vertices, and sizes \(d\) on their respective monochromatic sides. Conversely all partitions consisting of one monochromatic \(A\)-block and one monochromatic \(B\)-block of every size \(1,2,\ldots,c\) attain \(c\) components. Because these block sizes are all distinct, there is no symmetry divisor: for each of the labeled side sets there are \(T_c!/\prod_{j=1}^c j!\) ways to assign the blocks by size. Squaring gives the formula.

**5. Enumerating every partition.** For a fixed magnitude \(d\), a positive-imbalance block may have \((d+r,r)\) vertices from \(A,B\), respectively, for any \(r\ge0\). By labeled exponential counting it has bivariate exponential weight \(B_d(x,y)\), with an additional factor \(z\) marking one block. An unordered *nonempty* collection of these blocks has weight \(e^{zB_d(x,y)}-1\). Independently, a nonempty collection of negative-imbalance blocks has weight \(e^{zB_d(y,x)}-1\). Either magnitude \(d\) is absent, contributing \(1\), or it is present with both signs, contributing the product of these two weights and a factor \(u\) for its single coalition-graph component. Different magnitudes form an unordered but canonically distinguished assembly indexed by \(d\), hence multiply. Coefficient extraction and multiplication by \(m!n!\) restore the assignments of the labeled \(A\)- and \(B\)-vertices and prove the stated formula, with no block-label overcount.

## Verification
The standalone `verify.py` does not assume the signed-imbalance characterization when generating its direct answers. It independently constructs each \(K_{m,n}\), tests domination against adjacency and existence of a perfect matching by recursive subset search, generates **every** unlabeled vertex partition for \(1\le m,n\le5\), and computes the resulting coalition graph and its components directly. It compares the complete count indexed by number of components and blocks against an independent rational-coefficient evaluation of the exponential generating product. The largest directly enumerated case, \(K_{5,5}\), has \(14{,}637\) paired-coalition partitions. It also checks sharp maxima and the triangular equality counts for \(T_c\le5\); the formal series calculation alone separately checks the \(K_{6,6}\) triangular coefficient \(3{,}600\). Run `python3 verify.py`; expected last line: `ALL_FINITE_CHECKS_PASSED`. These are finite checks, not proofs of the infinite formulas; Steps 1–5 supply the proof.

## Relationship to prior work
Samadzadeh, Mojdeh, and Nadimi introduced paired-coalition graphs and proved \(\operatorname{PC}(K_{n_1,\ldots,n_r})=\sum n_i\) for complete multipartite graphs (Observation 2.2 in their 2024 paper). That scalar result maximizes the **number of partition blocks**, rather than classifying their paired-coalition graph, which may have more than one connected component. Their main graph-structure classifications concern paths, cycles and trees, not the present biclique realization spectrum.

The publicly available paired-domination polynomial characterization for complete multipartite graphs yields the individual paired-dominating-set formula \(\sum_{q\ge1}\binom mq\binom nq x^{2q}\) for a biclique. This is used as known background, **not** claimed as new; it counts individual balanced sets and does not supply complete graph realization, the distinct-magnitude component bound, or the multipartition generating function. Likewise, ordinary coalition graph studies involve a different, matching-free notion of domination. Searches of these specific implications and possible equivalent imbalance formulations did not uncover the present combined structural/enumerative result.

## Limitations
The theorem addresses complete bipartite base graphs with both parts nonempty, not arbitrary complete multipartite graphs, non-complete bipartite graphs or other coalition notions. The exact realization condition includes existential integer choices; it is not itself a closed-form count of unlabeled **coalition-graph isomorphism types**. Finite verification covers at most ten base vertices by exhaustive partition enumeration. Literature retrieval cannot rule out poorly indexed publications or unpublished equivalences; originality is an evidence-based comparison and no independent scientific validation is asserted here.

## References
1. M. R. Samadzadeh, D. A. Mojdeh, and R. Nadimi, “Paired coalition in graphs,” arXiv:2402.10842 (first publicly posted 16 February 2024), subsequently *AKCE International Journal of Graphs and Combinatorics* 22 (2025), 43–54 (online 1 October 2024), DOI: 10.1080/09728600.2024.2389070. https://arxiv.org/pdf/2402.10842
2. “Paired-domination polynomial of complete multipartite graphs,” publicly accessible mathematical result (2026), available as a full text in the published-finding corpus/2026 public mathematical records. Its bipartite specialization is the paired-dominating-set polynomial, not a coalition partition enumerator.
