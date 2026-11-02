# Exact maximal shattering of closed neighborhoods in uniform-incidence graphs

## Finding

Let \(n\) and \(k\) be integers satisfying \(2\le k<n\). Define the **uniform-incidence graph** \(I(n,k)\) with vertex set \(P\sqcup\mathcal B\), where \(P=[n]\), \(\mathcal B=\binom{P}{k}\), and a point \(p\in P\) is adjacent to a block \(B\in\mathcal B\) precisely when \(p\in B\). Let \(\mathscr N(n,k)=\{N_{I(n,k)}[v]:v\in V(I(n,k))\}\) be the family of **closed** vertex neighborhoods. A support is shattered when every subset of it is a trace of a member of \(\mathscr N(n,k)\).

**Theorem.** For all such \(n,k\), put
\[
d=\min\{k,n-k+2\}.
\]
Then
\[
\operatorname{VCdim}(\mathscr N(n,k))=d.
\]
More strongly, the number \(E(n,k)\) of shattered supports of maximum cardinality \(d\) is exactly
\[
E(n,k)=
\begin{cases}
3\binom{n}{2}+n\binom{n-1}{2},&k=2,\\
4\binom{n}{3}+2\binom{n}{2}\binom{n-2}{2}+4\binom{n}{4},&k=3,\\
8\binom{n}{3},&k=n-1\ge4,\\
\binom{n}{d},&d\ge4.
\end{cases}
\]
The cases are disjoint and exhaustive; \(k=3,n=4\) belongs to the second case, and the second and third expressions agree there if both are evaluated.

For \(d\ge4\), **every** maximum shattered support consists entirely of point vertices, and **every** \(d\)-subset of \(P\) is maximum shattered. For \(d=2\), the maximum supports are exactly: any two points; any point and an incident block; any two blocks with a common point. For \(d=3\), the triple types are described explicitly in the proof.

There is also a sharp rank-two adaptive separation:
\[
\operatorname{Ldim}(\mathscr N(n,2))=
\begin{cases}
2,&n=3,\\
3,&n\ge4.
\end{cases}
\]
Hence for every \(n\ge4\), rank two has \(\operatorname{VCdim}=2\) but \(\operatorname{Ldim}=3\). No all-rank formula for Littlestone dimension is claimed.

For comparison, the corresponding **open** neighborhoods of the same graph have VC dimension \(\min\{k,n-k\}\). Thus adding the center to each neighborhood can raise VC dimension by two: for example whenever \(k=n-1\ge3\), it changes from one to three.

## Assumptions and scope

All graphs are finite, simple and undirected, and all binomial coefficients have their usual combinatorial interpretation, including zero when the lower index exceeds the upper one. The two bipartition classes \(P\) and \(\mathcal B\) are disjoint vertex types even when a block happens to be represented by a singleton set. The actual theorem assumes \(2\le k<n\), not \(k=1\) or \(k=n\). The concept family uses inclusive **closed** graph neighborhoods, not open neighborhoods and not geodesically convex subsets.

The Littlestone dimension is the largest depth of a full binary tree whose internal nodes are labeled by vertices, such that every root-to-leaf sequence of requested membership labels is realized by at least one neighborhood hypothesis. The standard inequality \(\operatorname{VCdim}\le\operatorname{Ldim}\) follows by asking a shattered support in one fixed order.

## Proof

**1. Neighborhood structure.** Each point \(p\) determines
\[
H_p=\{p\}\cup\{B\in\mathcal B:p\in B\},
\]
and each block \(B\) determines
\[
H_B=\{B\}\cup B.
\]
Thus a point-centered hypothesis contains exactly one point vertex, while a block-centered hypothesis contains exactly one block vertex. This two-sided singleton property controls the support types.

**2. All point-only supports.** Let \(S\subseteq P\) have size \(s\ge2\). A trace of size at least two can only come from a block-centered hypothesis, whose trace on \(S\) is \(B\cap S\). Each singleton trace comes from \(H_p\), \(p\in S\), and the empty trace comes from \(H_q\) for any \(q\in P\setminus S\), whenever \(s<n\). For a prescribed trace \(T\subseteq S\) with \(2\le |T|\le s\), a suitable block exists if and only if
\[
|T|\le k\quad\text{and}\quad k-|T|\le n-s.
\]
Consequently every point support of cardinality \(2\le s\le d\) is shattered. Conversely, if \(s\ge3\) is shattered, realizing the full trace requires \(s\le k\), while realizing any fixed two-point trace requires \(k-2\le n-s\). Hence \(s\le d\). The bound also rules out point-only supports larger than \(d\); the case \(s=2\) follows directly from \(2\le k<n\). In particular every \(d\)-subset of points is shattered.

**3. Mixed supports.** Let a support contain \(a\) point vertices and \(b\) block vertices, both positive. If \(a,b\ge2\), no hypothesis contains all the support, by the singleton property. If \(a\ge3,b=1\), any hypothesis containing the whole support must be the selected block-centered hypothesis; no hypothesis can then realize a trace containing that block vertex together with exactly two selected point vertices. Dually, if \(a=1,b\ge3\), the only possible hypothesis containing all selected block vertices is the chosen point-centered one, and a trace with that point and exactly two selected block vertices cannot be realized. Therefore a shattered mixed support has size at most three.

For \(k\ge3\), the two possible three-point mixed forms admit exact criteria:

* A support consisting of distinct points \(p,q\) and block \(B\) is shattered exactly when \(p,q\in B\). Necessity follows from the all-positive trace. For sufficiency, obtain \(\{p,q,B\}\) with \(H_B\), \(\{p,q\}\) with any other block containing the pair, \(\{p,B\}\) and \(\{q,B\}\) with \(H_p,H_q\), \(\{B\}\) with \(H_r\) for \(r\in B\setminus\{p,q\}\), each singleton point with a block containing it but not the other, and the empty trace with a point outside \(B\). These choices exist because \(3\le k<n\).
* A support consisting of point \(p\) and distinct blocks \(B,C\) is shattered exactly when \(p\in B\cap C\) and \(|B\cap C|\ge2\). The traces \(\{p,B,C\}\) and \(\{B,C\}\) force respectively the first and second conditions. Conversely use \(H_p\) for the full trace, \(H_q\) with \(q\in(B\cap C)\setminus\{p\}\) for the two-block trace, \(H_B,H_C\) for \(\{p,B\}\) and \(\{p,C\}\), points of the nonempty differences \(B\setminus C,C\setminus B\) for individual blocks, a third block containing \(p\) for \(\{p\}\), and a block not containing \(p\) for the empty trace. Existence of the third block follows from \(\binom{n-1}{k-1}\ge3\).

For \(k=2\) both mixed triple types are impossible: a pair of selected point vertices determines a unique containing block, and two distinct two-element blocks have intersection of size at most one. The necessary conditions just given therefore cannot both hold.

**4. Block-only supports.** Let \(S=\{B_1,\ldots,B_s\}\subseteq\mathcal B\) be a shattered support of size \(s\ge3\). A block-centered hypothesis produces a trace of size at most one on \(S\). Therefore each trace indexed by a subset \(A\subseteq[s]\) with \(|A|\ge2\) must arise from a distinct point vertex \(p_A\) whose incidence signature is
\[
\{i:p_A\in B_i\}=A.
\]
Fixing one index \(i\), there are \(2^{s-1}-1\) required non-singleton signatures containing \(i\), and \(2^{s-1}-s\) required signatures avoiding \(i\). Hence
\[
k\ge2^{s-1}-1,\qquad n-k\ge2^{s-1}-s.
\]
For every \(s\ge3\) these bounds imply \(s\le k\) and \(s\le n-k+2\), proving \(s\le d\). For \(s\ge4\), they are both strict: \(k>s\) and \(n-k+2>s\). Thus a block-only support can never have maximum size \(d\ge4\). Together with steps 2 and 3 this proves the VC formula and the complete maximum-support classification when \(d\ge4\).

For \(s=3\), shattering is equivalent to the following four Venn regions being nonempty:
\[
B_1\cap B_2\cap B_3,\quad
(B_1\cap B_2)\setminus B_3,\quad
(B_1\cap B_3)\setminus B_2,\quad
(B_2\cap B_3)\setminus B_1.
\]
Necessity is the signature argument. For sufficiency those four point-centered hypotheses realize all traces of size at least two; the three block-centered hypotheses realize the singletons, and any block-centered hypothesis outside the support realizes the empty trace. Such an outside block exists because \(\binom{n}{k}\ge4\) for \(3\le k<n\). This proves the entire triple classification.

**5. Counting maximum supports.** If \(d=2\), necessarily \(k=2\). All pairs of points are shattered (\(\binom{n}{2}\) choices); a mixed point-block pair is shattered if and only if it is incident (\(2\binom{n}{2}\) choices); and a pair of blocks is shattered if and only if they intersect (\(n\binom{n-1}{2}\) choices). This yields the first formula.

If \(d=3\), then either \(k=3\) or \(k=n-1\). In every case all \(\binom{n}{3}\) point triples are shattered.

For \(k=3\), the two-point-one-block triples contribute \(3\binom{n}{3}\). The one-point-two-block triples have a two-point block intersection and contribute \(2\binom{n}{2}\binom{n-2}{2}\): first choose the shared pair and then the two distinct external points of the two blocks. A shattered triple of blocks is uniquely obtained by choosing four distinct ground points and designating one as the common triple intersection; the other three are the pair-only points. This contributes \(4\binom{n}{4}\). Summation gives the second formula.

For \(k=n-1\ge4\), identify each block with the unique point it omits. All three-block supports satisfy the four-region criterion, contributing \(\binom{n}{3}\). Two-point-one-block triples contribute \(n\binom{n-1}{2}=3\binom{n}{3}\). Every pair of distinct blocks has intersection of size \(n-2\), so one-point-two-block triples contribute \((n-2)\binom{n}{2}=3\binom{n}{3}\). Adding the point triples gives \(8\binom{n}{3}\). For \(n=4,k=3\) the two counts coincide. All cases are exhausted by the support-type split.

**6. Rank-two Littlestone dimension.** At \(n=3\) there are six distinct neighborhoods, so a full depth-three online tree (which needs eight distinct hypotheses) is impossible. The VC lower bound gives dimension two.

Suppose \(n\ge4\). An initial query at a block \(B=\{i,j\}\) has just three positive hypotheses, \(H_i,H_j,H_B\), so no depth-four online tree can start with that query. An initial point query at \(i\) has positive hypotheses exactly \(H_i\) and \(H_{\{i,j\}}\) for \(j\ne i\). Within this positive version space, querying another point gives at most one positive hypothesis, while querying a block gives at most two positive hypotheses. Hence this version space has Littlestone dimension at most two, and a full depth-four tree cannot start with a point query either. Therefore \(\operatorname{Ldim}\le3\).

For the matching lower bound, first query point \(i\). In the positive branch query the block \(\{i,j\}\): its positive branch contains \(H_i\) and \(H_{\{i,j\}}\), distinguished by querying point \(j\); its negative branch contains the \(n-2\ge2\) hypotheses \(H_{\{i,\ell\}}\) for \(\ell\notin\{i,j\}\), distinguished by a further point query. Thus the initial positive branch admits depth two. The initial negative branch contains, on the remaining point and block coordinates, precisely the closed neighborhoods of \(I(n-1,2)\). Since this smaller graph has VC dimension two by the established result, it also admits online depth two. Joining the branches gives depth three, as required.

**7. Open-neighborhood comparison.** Open neighborhoods of a bipartite graph lie entirely on the part opposite their centers, so a shattered support of size at least two lies in one part. For point supports of size \(s\), all traces are realized by \(k\)-blocks exactly when \(s\le\min\{k,n-k\}\). For block supports of size \(s\ge2\), every binary signature must occur among the \(n\) points. Each block and its complement must therefore contain at least \(2^{s-1}\) points; as \(2^{s-1}\ge s\), such a support cannot exceed \(\min\{k,n-k\}\). The point construction gives equality. This comparison does not use the closed-neighborhood theorem.

## Verification

The companion `verify_uniform_incidence_neighborhoods.py` constructs every graph from the incidence relation and computes traces of its literal closed neighborhoods, independently of the symbolic classification. It exhaustively checks maximum-support counts for all ranks at orders three through seven and selected additional ranks at orders eight and nine, including every size-three support and all size-\(d+1\) supports through order six. It separately evaluates the exact full binary online recurrence for rank two at orders three through eight. The printed success marker is `ALL_UNIFORM_INCIDENCE_NEIGHBORHOOD_CHECKS_PASS`.

These finite computations corroborate boundary and classification arithmetic; the proof above establishes the statements for every allowed parameter without extrapolation.

## Relationship to prior work

Adler, Benediktsson and Macpherson (arXiv:2007.16042, first posted July 31, 2020) study VC dimension and density of **open neighborhoods** of Johnson and Hamming graphs, also discussing boundedness for closed neighborhoods of those graph families. Their main families are not the bipartite point-to-uniform-block incidence graph \(I(n,k)\). Their Corollary 4.4 does explicitly identify the rank-two case \(I(n,2)\) as a graph induced by an open distance-two neighborhood of a binary Hamming graph; however, the paper derives no closed-neighborhood extremal-support count or Littlestone dimension for that induced graph, and its main open-neighborhood bounds for Hamming graphs do not imply the present formulas.

Axenovich and Zimmermann (arXiv:2401.11296, first posted January 20, 2024) define a hedgehog \(H(n,k,1)\) whose underlying graph is exactly \(I(n,k)\), and use it for induced Turán bounds and ordinary bipartite one-sided VC dimension. This is important **same-object prior art**. Their theorems concern forbidden induced graphs and extremal edge densities, not the closed-neighborhood concept class on both vertex types or its maximum-support counts. The open-neighborhood comparison is elementary background; it is not asserted to be novel.

The result's potential new content is the exact closed-neighborhood VC law, its coefficient at maximum size throughout all ranks, the structural extremal-support classification, and the rank-two online gap. Earlier uses of uniform-incidence graphs and the classical definitions themselves are explicitly acknowledged.

## Limitations

The stated scope excludes the degenerate ranks \(k=1\) and \(k=n\). No general all-rank Littlestone formula or all-coefficient shattered-support polynomial is established. Exhaustive computation covers only the stated finite orders. Independent mathematical validation has not been performed. Historical priority remains subject to comparison with literature using alternative terminology such as hedgehog graphs, complete-uniform hypergraph incidence, graph neighborhood traces and bipartite shattering; absence of a search hit does not prove novelty.

## References

1. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (initial public version 2020-07-31), https://arxiv.org/abs/2007.16042.
2. M. Axenovich, J. Zimmermann, *Induced Turán problem in bipartite graphs*, arXiv:2401.11296 (initial public version 2024-01-20), https://arxiv.org/abs/2401.11296.
