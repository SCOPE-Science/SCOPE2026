# First maximal-independent-set shattering gap and its connected-cograph amplification

## Finding

For a finite simple graph \(G\), let \(\mathcal M(G)\) be its set of inclusion-maximal independent vertex sets, considered as Boolean functions on \(V(G)\) by membership. Write \(v(G)=\operatorname{VCdim}(\mathcal M(G))\) and \(\ell(G)=\operatorname{Ldim}(\mathcal M(G))\).

**First-order boundary.** Every graph on at most four vertices satisfies \(v(G)=\ell(G)\). Exactly two isomorphism types of five-vertex graphs have strict inequality, and both have \((v,\ell)=(1,2)\). They are: (a) a diamond (\(K_4\) minus one edge) with one pendant vertex attached to a degree-two diamond vertex; and (b) the cograph \(F=K_2\vee(K_2\sqcup K_1)\). Among the \(1024\) labeled graphs on five specified vertices, the former type occurs \(60\) times and the latter \(30\) times. The latter is the unique \(P_4\)-free five-vertex type with a gap.

**Infinite connected amplification.** For every integer \(m\ge1\), the graph
\[
G_m=K_1\vee\underbrace{(F\sqcup\cdots\sqcup F)}_{m\text{ copies}}
\]
is a connected \(P_4\)-free graph on \(5m+1\) vertices with exactly \(4^m+1\) maximal independent sets and
\[
\boxed{v(G_m)=m,\qquad \ell(G_m)=2m.}
\]
In particular, the adaptive-minus-static shattering gap is unbounded even among connected cographs.

## Assumptions and scope

Graphs are finite, loopless, undirected, and simple. An independent set is *maximal* when no new vertex can be adjoined while preserving independence; it need not have maximum cardinality. A support \(S\subseteq V(G)\) is VC-shattered if every subset of \(S\) equals \(I\cap S\) for some \(I\in\mathcal M(G)\). Littlestone dimension is the largest depth of a complete binary tree whose internal nodes query vertex membership and whose every root-to-leaf answer sequence is realized by a member of \(\mathcal M(G)\). A depth-zero tree is always shattered. The disjoint union \(\sqcup\) and complete join \(\vee\) have their usual graph-theoretic meanings. A cograph means a graph with no induced four-vertex path, equivalently a graph built from singletons by disjoint unions and joins.

## Proof

**1. The five-vertex cograph mechanism.** Label the vertices of \(F\) by \(a,b,c,d,e\). The pair \(a,b\) is an edge joined to all of \(c,d,e\), the pair \(c,d\) is an edge, and \(e\) is nonadjacent to \(c,d\). The four and only four maximal independent sets are
\[
\mathcal M(F)=\big\{\{a\},\{b\},\{c,e\},\{d,e\}\big\}.
\]
Every coordinate takes both values across these hypotheses, so \(v(F)\ge1\). If a two-coordinate support has an all-positive trace, it must be \(\{c,e\}\) or \(\{d,e\}\); on either such support the pattern with the non-\(e\) vertex present but \(e\) absent cannot occur. Every other two-coordinate support lacks the all-positive trace. Hence \(v(F)=1\). The query \(e\) divides the class into two two-hypothesis branches: \(\{c,e\},\{d,e\}\) and \(\{a\},\{b\}\). Querying \(c\) on the first branch and \(a\) on the second gives a fully shattered depth-two tree. Four hypotheses cannot shatter depth three (which requires eight distinct terminal witnesses); thus \(\ell(F)=2\). This construction is a cograph because its displayed graph expression uses only union and join.

**2. Connected amplification: hypothesis count and online dimension.** Let \(u\) denote the new universal vertex of \(G_m\), and let \(F_1,\ldots,F_m\) be the disjoint blocks. A maximal independent set either equals \(\{u\}\) or is a union of independently chosen members of \(\mathcal M(F_i)\), one from each block. Therefore
\[
|\mathcal M(G_m)|=1+4^m.
\]
On the product subfamily, concatenate the depth-two shattered trees in the \(m\) blocks: at the end of each block's two queries, the remaining blocks are unconstrained, so the next two queries can be made in the next block. This shatters depth \(2m\) and proves \(\ell(G_m)\ge2m\). Conversely a depth-\(d\) tree requires at least \(2^d\) distinct hypotheses. Since \(4^m+1<2^{2m+1}\) for every \(m\ge1\), \(\ell(G_m)\le2m\).

**3. Connected amplification: VC dimension.** For each \(i\), query its vertex \(e_i\). The product subfamily assigns the \(m\) answers independently, taking \(\{a_i\}\) for a zero and \(\{c_i,e_i\}\) for a one. Thus \(v(G_m)\ge m\). For the reverse direction, let \(S\) be shattered. If \(S\) contains \(u\) and any other vertex, its all-positive trace is impossible; hence such an \(S\) has size at most one. Assume \(S\) omits \(u\). If \(S\) meets at least two different blocks, fix an affirmative query in one block and range over all trace patterns in another block. The special hypothesis \(\{u\}\) cannot realize these affirmative patterns, so the projection of \(S\) to each block is itself VC-shattered by \(\mathcal M(F)\), and therefore contains at most one vertex. Hence \(|S|\le m\). If \(S\) lies within one block, all its **nonempty** traces must be supplied by \(\mathcal M(F)\). No two-coordinate support of \(F\) has all three nonempty traces: if the all-positive trace exists, the support is \(\{c,e\}\) or \(\{d,e\}\), and the single-positive trace at \(c\) or \(d\) is missing. Thus \(|S|\le1\). This completes \(v(G_m)=m\). Disjoint unions and adjoining a universal vertex preserve the cograph property, and the universal vertex makes \(G_m\) connected.

**4. Complete smallest-order classification.** Enumerate every graph on a fixed set of \(n\) vertices by its \(\binom n2\)-bit edge indicator. For every edge indicator enumerate every vertex subset; retain a subset if it is independent and dominates every vertex outside it, precisely the test for maximal independentness. Compute \(v\) from all query supports and the full trace collection. Compute \(\ell\) using the exact recurrence
\[
L(\mathcal H)=\begin{cases}0,&|\mathcal H|\le1,\\
1+\max_{x\,\text{with both branches nonempty}}\min\{L(\mathcal H_{x,0}),L(\mathcal H_{x,1})\},&\text{otherwise,}
\end{cases}
\]
with maximum of an empty set taken as \(-1\) for purposes of the displayed second line, yielding zero if no genuine split exists. This recurrence follows by conditioning a shattered tree on its root query and is exact. Exhaustively applying it to the \(1,2,8,64,1024\) labeled graphs on \(1,2,3,4,5\) vertices, respectively, gives no gap through order four and precisely \(90\) gaps at order five. For all \(90\), the dimensions are \((1,2)\). Under all \(5!\) vertex relabelings, they form exactly two canonical graph codes, with orbit multiplicities \(60\) and \(30\). The first representative is the diamond-with-leaf and the second is \(F\); an induced-four-path test identifies only the second as a cograph. The provided checkers enumerate the *entire finite domain*, including all isomorphism comparisons, rather than sampling graphs.

## Verification

With Python 3, run `python3 verify.py`, `python3 independent_check.py`, and `python3 amplification_check.py` from the directory containing those files. No nonstandard packages are required. The first two programs independently enumerate all labeled graphs through five vertices: one tests independentness and domination by bit masks and memoizes exact Littlestone ranks, while the other enumerates complement cliques and tests the existence of complete shattered trees at each depth. They agree on the five-vertex full distribution \((0,0):1\), \((1,1):611\), \((1,2):90\), \((2,2):322\). Canonical relabeling groups the gap graphs into exactly two types. The third program tests the connected-cograph construction for \(m=1,2\), including its induced-path exclusion and exact dimensions. These finite checks independently support the boundary classification and illustrative cases; the infinite amplification is established by Steps 1–3 above.

## Relationship to prior work

Bassino, Bouvel, Drmota, Féray, Gerin, Maazoun and Pierrot (arXiv:2104.07444, first public version 2021-04-15) study the structure and enumeration of independent sets in cographs and describe their recursive join/disjoint-union representation. Their results concern independence numbers and random-cograph enumeration; their introductory discussion expressly distinguishes a proposed study of *maximal* independent sets. They do not give the present VC/Littlestone classification. Ghazi, Golowich, Kumar and Manurangsi (arXiv:2007.03668, first public version 2020-07-07) establish general Littlestone-dimension bounds under aggregation, not exact values for maximal independent sets of cographs. Earlier graph-family calculations for forests and cycles likewise do not imply the five-vertex cograph construction or the connected-cograph amplification. No claim of exhaustive historical priority is made.

## Limitations

The classification of first failures is complete only through five graph vertices, although the displayed infinite connected-cograph family has exact dimensions for all parameters. There is no claim of a dimension formula for arbitrary cographs. The result concerns *all inclusion-maximal independent sets*, not minimum-cardinality independent dominating sets or maximum-cardinality independent sets. The exact finite census has two independent executable implementations, but independent mathematical audit and a comprehensive historical-priority determination remain outstanding.

## References

- F. Bassino, M. Bouvel, M. Drmota, V. Féray, L. Gerin, M. Maazoun and A. Pierrot, *Linear-sized independent sets in random cographs and increasing subsequences in separable permutations*, arXiv:2104.07444 (first public version 2021-04-15). https://arxiv.org/abs/2104.07444
- B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight closure bounds for the Littlestone and threshold dimensions*, arXiv:2007.03668 (first public version 2020-07-07); Proceedings of Machine Learning Research 132 (2021). https://proceedings.mlr.press/v132/ghazi21a.html
