# Forest size profiles determine shattering by fixed-cardinality cuts

## Finding

Let \(n\ge2\) and \(1\le a\le\lfloor n/2\rfloor\). On the unordered pairs of \([n]\), consider the concept class \(\mathcal H_{n,a}\) containing, for each \(A\subseteq[n]\) of cardinality \(a\), the function \(h_A(\{u,v\})=1\) if and only if either both vertices belong to \(A\) or neither does. Thus the concepts are same-block responses from two-block partitions with prescribed block sizes \(a\) and \(n-a\), with duplicate concepts identified when the block sizes coincide.

**Forest size-profile theorem.** A query support \(S\subseteq\binom{[n]}2\) is VC-shattered by \(\mathcal H_{n,a}\) if and only if its graph \(([n],S)\) is a forest with connected-component orders \(t_1,\ldots,t_r\), including isolated vertices, and for every choice of integers \(0\le c_i\le\lfloor t_i/2\rfloor\), the polynomial
\[
\prod_{i=1}^r\bigl(z^{c_i}+z^{t_i-c_i}\bigr)
\]
has a strictly positive coefficient of \(z^a\). In particular, shattering depends on component orders but not on the shapes of the component trees.

This gives an all-parameter finite arithmetic characterization of shattered supports and a partition-profile procedure for determining the exact VC dimension: maximize \(n-r\) over integer partitions \((t_1,\ldots,t_r)\) of \(n\) passing the stated coefficient tests.

For every admissible \(n,a\),
\[
\operatorname{VCdim}(\mathcal H_{n,a})\le\min\{2a,n-2\}.
\]
The first bound is attained throughout a full stable range:
\[
\boxed{\operatorname{VCdim}(\mathcal H_{n,a})=2a\quad\text{whenever }n\ge3a+1.}
\]
For example, when the smaller block has exactly two vertices, the exact VC dimensions for \(n=4,5,6\) and all \(n\ge7\) are respectively \(1,2,3,4\).

## Assumptions and scope

Graphs are finite, simple and undirected. A query set is shattered only when every assignment of zeroes and ones to **all** its edges is realized by one set \(A\) of cardinality exactly \(a\); it is not enough to realize each assignment by a set of variable cardinality. The candidate query edges range over the complete graph, whereas the support graph \(([n],S)\) can be arbitrary. This theorem concerns ordinary static VC shattering and makes no claim about the Littlestone dimension of these classes.

## Proof

**1. Cycle obstruction.** If \(S\) contains a cycle, label exactly one edge on that cycle by zero (different blocks) and every other cycle edge by one (same block). Equality along the positive path forces the endpoints of the negative edge to belong to the same block, a contradiction. Every shattered \(S\) is therefore a forest.

**2. Labelings on a forest.** Fix an assignment of zeroes and ones to the edges of a forest. In each tree component, choose a root and assign it either one of the two block labels. The remaining vertex labels are forced along the unique paths, with positive edges preserving the label and negative edges flipping it. The two possible choices of root swap the labels of the entire component. If the first choice puts \(c_i\) vertices in \(A\), the other puts \(t_i-c_i\) vertices in \(A\). The assignment extends to a concept in \(\mathcal H_{n,a}\) precisely when some selection of these component flips has total \(a\), equivalently when the coefficient of \(z^a\) in the stated product is positive.

For a tree of order \(t_i\), every \(c_i\in\{0,1,\ldots,t_i\}\) can occur: choose any assignment of the two labels to the vertices with that number of vertices carrying the first label, then label the tree edges according to equality. Replacing \(c_i\) by \(t_i-c_i\) leaves the factor unchanged, so the range \(0\le c_i\le\lfloor t_i/2\rfloor\) is sufficient. The edge assignments in distinct tree components vary independently. Hence every possible edge labeling extends if and only if all the coefficient tests hold. The proof uses no information about the shapes of the trees beyond their connectedness and acyclicity.

**3. Universal upper bound.** In each component of order \(t_i\), select a binary vertex labeling whose two color-class sizes are \(\lfloor t_i/2\rfloor\) and \(\lceil t_i/2\rceil\), and use it to prescribe edge equalities. The least possible total number of vertices in \(A\) across component flips is \(\sum_i\lfloor t_i/2\rfloor\). Shattering forces
\[
\sum_i\lfloor t_i/2\rfloor\le a.
\]
Since \(t_i-1\le2\lfloor t_i/2\rfloor\), a shattered forest has
\[
|S|=\sum_i(t_i-1)\le 2a.
\]
It also has at least two components, because the all-positive edge labeling of a connected spanning tree forces a single block, contrary to \(1\le a<n\). Thus \(|S|=n-r\le n-2\).

**4. Sharp saturation.** Suppose \(n\ge3a+1\). Take a star with \(2a\) edges, one center, \(2a\) leaves, and at least \(a\) further isolated vertices. Consider any assignment to its \(2a\) edges, with exactly \(k\) negative edges. If \(k\le a\), put the center outside \(A\), the \(k\) negative-edge leaves inside \(A\), and choose the remaining \(a-k\) members of \(A\) among isolated vertices. If \(k\ge a+1\), put the center and all \(2a-k\) positive-edge leaves in \(A\); then choose another \(k-a-1\) isolated vertices. In both cases the chosen set has cardinality \(a\) and realizes the prescribed edge labels. All \(2^{2a}\) assignments are attained. Together with the upper bound, this gives equality.

**5. The small-block example.** For \(a=2\), the star construction with two, three or four edges and the remaining vertices isolated is shattered at \(n=5,6,7\), respectively. For \(n=4\), any single query is shattered. To see that the displayed values for \(n=4,5,6\) cannot be exceeded, use the forest criterion: a candidate with \(n-2\) edges has exactly two components. Their possible order profiles are respectively \((1,3),(2,2)\); \((1,4),(2,3)\); and \((1,5),(2,4),(3,3)\). For each profile, choose component color counts such that the coefficient of \(z^2\) vanishes: respectively \((0,0),(0,1)\); \((0,0),(1,0)\); and \((0,0),(1,0),(0,0)\). Therefore there are no shattered supports of \(n-2\) edges in those three orders, while the given lower bounds are attained. For all \(n\ge7\), the stable-range formula gives the value four.

## Verification

The standalone program `verify.py` exhaustively compares the coefficient criterion with direct enumeration of **every** support \(S\subseteq\binom{[n]}2\), for all \(2\le n\le6\) and all admissible \(a\). Its direct method enumerates every \(a\)-subset and every observed support pattern; its structural method independently checks cycles, component orders, and reachable subset sums. There are 100,490 triples \((n,a,S)\) in this exhaustive finite test. The program separately confirms the star certificate by the coefficient criterion for \(1\le a\le8\).

Run `python3 verify.py` in the same directory as this document. The recorded output in `verification_output.txt` ends with `ALL_FIXED_CARDINALITY_CUT_CHECKS_PASS 100490`. The general proof above, not these finite tests, establishes the theorem for arbitrary parameters.

## Relationship to prior work

The VC and Littlestone dimensions are standard dimensions of a Boolean concept class. Ghazi, Golowich, Kumar and Manurangsi (2020/2021) analyze general closure bounds, not the induced restriction of the graphic cut space to one fixed-cardinality layer. Manurangsi (2022/2023) establishes hardness of approximating arbitrary explicitly presented concept classes, not this structural forest-profile classification. Research on learning graph cuts has generally treated vertex-label or small-edge-cut parameters; here the instances are unordered **edge-pair comparisons** on the complete vertex set, while the fixed parameter is a **vertex-side cardinality**. These differences matter to the mathematical implications.

The previously considered refinement-closed families of partitions have substantially different feasibility conditions: the present class has an exact cardinality constraint and, in general, is not closed under refinement. Small prescribed-block-size examples alone do not imply the all-parameter coefficient criterion or the stable value \(2a\). No claim of exhaustive worldwide publication-priority certification is made.

## Limitations

The stable-range bound \(n\ge3a+1\) is sufficient, not claimed to be the optimal saturation threshold for every \(a\). Below this range the exact arithmetic profile criterion applies, but a single elementary closed formula for the VC dimension is not provided. The theorem concerns binary same-block queries only; it does not classify all adaptive mistake trees or arbitrary vertex-query cut classes. Published-record comparisons cannot exclude every unindexed or inaccessible prior theorem, and independent scientific validation remains outstanding.

## References

1. B. Ghazi, N. Golowich, R. Kumar, and P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668v1 (first public 2020-07-07), PMLR 132 (2021), 686–696. https://arxiv.org/abs/2007.03668 ; https://proceedings.mlr.press/v132/ghazi21a.html
2. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443v1 (2022-11-02), ITCS 2023. https://arxiv.org/abs/2211.01443
3. T. Gärtner and G. C. Garriga, *The Cost of Learning Directed Cuts*, primary text consulted for the distinction between vertex-cut learning and fixed-cardinality edge-comparison shattering. https://scispace.com/pdf/the-cost-of-learning-directed-cuts-2ay6ylzug2.pdf
