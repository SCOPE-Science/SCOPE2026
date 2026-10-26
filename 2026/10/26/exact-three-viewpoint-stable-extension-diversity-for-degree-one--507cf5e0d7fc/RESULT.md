# Exact three-viewpoint stable-extension diversity for degree-one argumentation graphs

## Finding

Let \(F=(V,R)\) be a finite Dung abstract argumentation framework whose directed attack graph has indegree and outdegree at most one at each vertex. Assume that every directed cycle has even length and that there are at least two such cycles, of lengths \(\ell_1,\ldots,\ell_r\), where \(r\geq2\); put \(W=\sum_{i=1}^r\ell_i\). A stable extension is a conflict-free set of vertices that attacks every vertex outside it. For three **pairwise distinct** stable extensions, define the worst-pair diversity optimum
\[
\Delta_3(F)=\max_{E_1,E_2,E_3\ \mathrm{pairwise\ distinct}}\ \min_{1\leq a<b\leq3}|E_a\mathbin{\triangle}E_b|.
\]
Then the exact value is
\[
\boxed{\displaystyle
\Delta_3(F)=W-\min_{B_1\sqcup B_2\sqcup B_3=\{1,\ldots,r\}}
\max_{j=1,2,3}\ \sum_{i\in B_j}\ell_i .}
\]
Empty bins are allowed. Thus triple diversity is exactly the complement of optimal three-bin makespan for the even-cycle lengths. Its value is computable in \(O(rW^2)\) time and \(O(W^2)\) working space, hence polynomial time in \(|V|\), without enumerating the exponentially many stable extensions.

In particular,
\[
\Delta_3(F)\leq\frac{2W}{3},
\]
with equality if and only if the cycle lengths admit a partition into three groups of total length exactly \(W/3\) each. If all \(r\) cycles have the same even length \(L\), then
\[
\Delta_3(F)=L\left\lfloor\frac{2r}{3}\right\rfloor .
\]

## Assumptions and scope

The attack relation is an ordinary set of directed arcs; no parallel arcs occur. A loop is a directed cycle of length one and is excluded by the even-cycle hypothesis. Directed path components, including isolated vertices, are allowed. All graphs are finite. For \(r<2\), fewer than three stable extensions exist, so the displayed triple optimum is not defined. If an odd directed cycle is present, there is no stable extension at all; this is a separate obstruction rather than a zero diversity value. No assertion is made for branching attack graphs or other extension semantics.

## Proof

**Component decomposition.** Because every vertex has at most one incoming and one outgoing arc, each weak component of a finite attack graph is either a directed path or a directed cycle. Stable semantics is componentwise: if no attack connects two components, a union is a stable extension precisely when its intersection with each component is stable. This follows directly because both conflict-freeness and attacking every excluded vertex are local.

**Phase choices.** On a directed path, the source must belong to every stable extension, since otherwise it has no attacker in the extension. Its successor must be excluded, the following vertex included, and so on; this determines a unique stable extension. On a directed cycle, write \(s_i\in\{0,1\}\) for membership of consecutive vertices (indices cyclically). Conflict-freeness plus the requirement to attack every excluded vertex forces \(s_i=1-s_{i-1}\) for every vertex. There are two alternating solutions for even length and none for odd length. Consequently, under the hypotheses the stable extensions are in bijection with \(\{0,1\}^r\), one phase bit for each even cycle. The unique path selections are common to all extensions. Two phase choices that disagree on cycle \(i\) have disjoint complementary vertex selections there and therefore contribute **all** \(\ell_i\) vertices to their symmetric difference. Hence
\[
|E_x\mathbin{\triangle}E_y|=\sum_{i:x_i\ne y_i}\ell_i.
\]

**Reduction from triples to three bins.** Fix three bit vectors corresponding to stable extensions. At a given cycle, if the three bits are equal then the cycle contributes zero to every pairwise distance. Replacing this constant coordinate by any nonconstant triple of bits leaves the previously unequal coordinates unchanged and weakly increases every pairwise distance. Thus the maximum of the minimum can be attained using only nonconstant triples at every cycle. Among three binary bits which are not all equal, exactly one of the three pairs \((1,2)\), \((1,3)\), \((2,3)\) agrees. Put cycle \(i\) in bin \(B_j\) according to this agreeing pair, and let \(w_j=\sum_{i\in B_j}\ell_i\). The three pairwise distances are precisely \(W-w_1\), \(W-w_2\), and \(W-w_3\), so their minimum is \(W-\max_j w_j\).

Conversely, any partition of cycle indices into three labeled bins is realized by choosing at each cycle one of the patterns \((0,0,1)\), \((0,1,0)\), or \((1,0,0)\), according to the agreeing pair. Since \(r\ge2\) and all lengths are positive, some partition has two nonempty bins and therefore \(\max_jw_j<W\). An optimal partition consequently has \(\max_jw_j<W\), meaning all three pairwise distances are positive and the resulting stable extensions are genuinely pairwise distinct. Taking the maximum over triples proves the boxed identity.

**Bounds and uniform case.** For every partition, \(w_1+w_2+w_3=W\), so \(\max_jw_j\ge W/3\); equality holds exactly for three equal bin totals. When all cycle lengths equal \(L\), balanced distribution of the \(r\) indices among three bins minimizes the maximum bin size to \(\lceil r/3\rceil\), giving the stated formula.

**Algorithm.** Process the cycle lengths in order, maintaining reachable pairs \((a,b)\) of total length assigned to the first and second bins. Initially only \((0,0)\) is reachable. For a new length \(\ell\), each reachable pair yields \((a+\ell,b)\), \((a,b+\ell)\), and \((a,b)\), corresponding to bins one, two, and three. After all cycles, evaluate \(\max(a,b,W-a-b)\) at every reachable pair and take the minimum. There are at most \((W+1)^2\) pairs and \(r\) stages. Two Boolean layers give the claimed time and working-space bounds; saving predecessor states across layers also reconstructs an optimal triple in polynomial time.

## Verification

The included standalone `verify.py` independently enumerates stable sets from the directed attack relation on 35 small disjoint unions of paths and cycles. For each it compares the maximum minimum of all triples computed by direct vertex-subset enumeration with the three-bin formula, and checks the predicted number of stable extensions, including odd-cycle and too-few-extension cases. It prints `PASS 35 exact stable-extension/three-diversity tests` when successful. This finite check is corroboration only: the proof above establishes the assertion for all finite frameworks satisfying the hypotheses.

## Relationship to prior work

Fichte, Hecher, Mahmood, and Wang (2026) introduce symmetric-difference diversity for argumentation semantics and analyze distance between **two** extensions, including complexity questions and componentwise extension composition (Lemma 24). The present statement concerns the simultaneous worst-pair separation of **three** stable extensions and gives a closed graph-structural expression and exact polynomial-time algorithm for degree-one frameworks. Neither that pairwise theory nor the componentwise factorization statement directly specifies the three-bin bottleneck value.

Matsuoka and Ito (2023) formulate the general maximum-minimum weighted-Hamming-distance problem for multiple solutions and prove approximation and hardness results. The phase-bit representation places the present question in that general framework; the exact three-bin identity and the stable-semantics domain decomposition are the additional specialized conclusion. The general elementary three-codeword distance-sum bound explains the \(2W/3\) upper bound, not the exact value for arbitrary cycle lengths.

## Limitations

The theorem classifies a deliberately structural fragment, not arbitrary abstract argumentation frameworks. The hypothesis \(r\ge2\) is essential for a triple of distinct stable extensions. No optimal-triple claim is made when an odd cycle blocks stable extensions. The exact weighted-cube optimization is a natural special case of broader diversity optimization; earlier equivalent treatments under other terminology remain a possible priority risk. Computational checks have finite scope and do not replace the proof.

## References

1. J. K. Fichte, M. Hecher, Y. Mahmood, and Z. Wang, “Diversity of Extensions in Abstract Argumentation,” arXiv:2605.13332v1 (first public 2026-05-13); IJCAI 2026, pages 3846–3854, doi:10.24963/ijcai.2026/428. https://arxiv.org/abs/2605.13332
2. T. Matsuoka and S. Ito, “Maximization of Minimum Weighted Hamming Distance between Set Pairs,” Proceedings of Machine Learning Research 222 (ACML 2023). https://proceedings.mlr.press/v222/matsuoka24a/matsuoka24a.pdf
3. P. M. Dung, “On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games,” Artificial Intelligence 77 (1995), 321–357.
