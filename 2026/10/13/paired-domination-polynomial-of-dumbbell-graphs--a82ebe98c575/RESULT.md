# Paired-domination polynomial of dumbbell graphs
## Finding
For integers \(r,s\ge 2\), let \(D_{r,s}\) be the graph obtained from disjoint cliques \(L\cong K_r\) and \(R\cong K_s\) by adding one bridge \(uv\) with \(u\in L\) and \(v\in R\). Define
\[
E_m(x)=\sum_{\substack{2\le k\le m\\ k\ \mathrm{even}}}\binom{m}{k}x^k
=\frac{(1+x)^m+(1-x)^m}{2}-1
\]
and
\[
Q_m(x)=\sum_{\substack{0\le k\le m\\ k\ \mathrm{even}}}\binom{m}{k}x^k
=\frac{(1+x)^m+(1-x)^m}{2}.
\]
Then the paired-domination polynomial of \(D_{r,s}\) is
\[
D_{\mathrm{pr}}(D_{r,s};x)=E_r(x)E_s(x)+x^2Q_{r-1}(x)Q_{s-1}(x).
\]
Consequently,
\[
D_{\mathrm{pr}}(D_{r,s};1)=\bigl(2^{r-1}-1\bigr)\bigl(2^{s-1}-1\bigr)+2^{r+s-4},
\]
and
\[
\gamma_{\mathrm{pr}}(D_{r,s})=2.
\]
The bridge endpoints \(\{u,v\}\) form the unique minimum paired-dominating set.

## Assumptions and scope
Graphs are finite, simple, and undirected. A paired-dominating set is a dominating set whose induced subgraph contains a perfect matching. The parameters satisfy \(r,s\ge2\); this includes the symmetric barbell family as the case \(r=s\).

## Proof
Let \(S\subseteq V(D_{r,s})\), and write \(a=|S\cap L|\) and \(b=|S\cap R|\). If \(S\) misses one clique, then a non-bridge vertex in that clique is not dominated, because the bridge is the only edge joining the two cliques. Conversely, if \(S\) meets both cliques, every vertex outside \(S\) is adjacent to a selected vertex in its own clique. Thus domination is equivalent to \(a\ge1\) and \(b\ge1\).

It remains to characterize perfect matchings in the induced graph \(D_{r,s}[S]\). The bridge \(uv\) is its only possible edge between \(S\cap L\) and \(S\cap R\). If a perfect matching does not use \(uv\), then each selected clique must be matched internally, so both \(a\) and \(b\) are even. Conversely, if both are positive and even, the selected vertices in each clique have an internal perfect matching.

If a perfect matching uses \(uv\), then \(u,v\in S\), and after deleting these two vertices the remaining selected vertices in each clique must have even cardinality. Hence both \(a\) and \(b\) are odd. Conversely, when both are odd and \(u,v\in S\), use \(uv\) and match the remaining even sets inside their cliques. Therefore
\[
S\text{ is paired-dominating}\iff
\begin{cases}
a,b\text{ are positive and even},&\text{or}\\
a,b\text{ are odd and }u,v\in S.&
\end{cases}
\]

The positive-even case contributes \(E_r(x)E_s(x)\). In the odd case the bridge endpoints contribute \(x^2\), while an even number of the remaining \(r-1\) and \(s-1\) vertices may be chosen independently, contributing \(Q_{r-1}(x)Q_{s-1}(x)\). This proves the polynomial identity. Evaluating at \(x=1\) gives the total count. The coefficient of \(x^2\) is exactly one, from \(S=\{u,v\}\), proving both the minimum value and its uniqueness.

## Verification
The standalone verifier enumerates all vertex subsets for \(2\le r,s\le7\) with \(r+s\le12\). It tests domination directly, tests existence of a perfect matching by a generic recursive matching routine, compares every set with the structural criterion above, and compares the resulting coefficient dictionary with the closed formula. Its successful output is:

`VERIFY_OK pairs=33 subset_checks=30736 paired_sets=8446 structural_checks=30736 coefficient_checks=134 max_order=12`

This finite computation is a consistency check only; the proof above establishes the statement for every allowed \(r\) and \(s\).

## Relationship to prior work
Haynes and Slater introduced paired domination and studied the minimum parameter, bounds, complexity, and relations with other domination parameters. Pious and Joseph later studied this exact two-clique bridge family under the name dumbbell graph \(D_{r,s}\), proving that its ordinary and independent domination numbers are both \(2\). Their result does not impose the perfect-matching condition and therefore does not determine the paired-dominating sets.

A 2016 one-page conference artifact introduced the paired-domination polynomial and states that some standard graph families were computed. The complete accessible artifact was inspected; it contains the definition and abstract-level scope but no displayed family formula or dumbbell result. Searches under both “dumbbell” and “barbell” terminology, together with searches for the exact polynomial and paired-domination number, found no source implying the formula above. The closest indexed coefficientwise results concern chain graphs and complete multipartite graphs; neither class contains \(D_{r,s}\) for the stated parameter range.

## Limitations
The literature search cannot rule out an unindexed or inaccessible dumbbell-specific result. The 2016 conference artifact is only one page, so it does not reveal the full list of families that may have been discussed in a presentation. The theorem concerns the bridge-length-one two-clique dumbbell family only; dumbbell terminology is also used elsewhere for two cycles joined by a path, which is a different graph family.

## References
1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F. First published 1998-12-07.
2. F. Pious and M. Joseph, “On Equality and Strong Equality of Domination Number and Independent Domination Number in Graphs,” *Mapana Journal of Sciences* 14(3) (2015), 73–82. Section 2.1.1 defines \(D_{r,s}\) as two complete graphs joined by one edge and proves the ordinary/independent domination value \(2\).
3. Puttaswamy, A. Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” ICMAGT 2016 conference artifact, September 26–27, 2016, record 52964.
4. H. Jiang, P. Wu, J. Zhang, and Y. Rao, “Upper paired domination in graphs,” *AIMS Mathematics* 7 (2022), with MSC 05C69, DOI: 10.3934/math.2022069.
