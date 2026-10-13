# All \(k\)-tuple total restrained dominating sets of crown graphs
## Finding
Let \(n\ge3\) and \(1\le k\le n-1\). Write the crown graph as
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\},
\]
with bipartition classes \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). A set \(S\subseteq V(\operatorname{Cr}_n)\) is a \(k\)-tuple total restrained dominating set when every vertex has at least \(k\) neighbors in \(S\), and every vertex outside \(S\) also has at least \(k\) neighbors outside \(S\).

Define
\[
I=\{i:a_i\in S\},\qquad J=\{i:b_i\in S\},\qquad
X=[n]\setminus I,\qquad Y=[n]\setminus J.
\]
Then \(S\) is feasible exactly in either of the following cases:

1. \(S=V(\operatorname{Cr}_n)\); or
2. \(S\ne V(\operatorname{Cr}_n)\), both \(|I|\) and \(|J|\) are at least \(k+1\), both \(|X|\) and \(|Y|\) lie between \(k\) and \(n-k-1\), and
\[
X\cap Y=\varnothing
\]
whenever \(|X|=k\) or \(|Y|=k\).

Thus if \(n\le2k\), the full vertex set is the only feasible set. If \(n\ge2k+1\), put \(N=n-k-1\). The complete cardinality enumerator
\[
T_{n,k}(x)=\sum_{S}x^{|S|}
\]
over all \(k\)-tuple total restrained dominating sets is
\[
\begin{aligned}
T_{n,k}(x)=\;&x^{2n}
+\sum_{a=k+1}^N\sum_{b=k+1}^N
\binom{n}{a}\binom{n}{b}x^{2n-a-b}\\
&+2\sum_{b=k+1}^N
\binom{n}{k}\binom{n-k}{b}x^{2n-k-b}
+\binom{n}{k}\binom{n-k}{k}x^{2n-2k}.
\end{aligned}
\]
The empty sums are interpreted as zero.

Consequently,
\[
\gamma_{\times k,t}^r(\operatorname{Cr}_n)=
\begin{cases}
2n,&n\le2k,\\
2k+2,&n\ge2k+1.
\end{cases}
\]
The number of minimum sets is \(1\) when \(n\le2k\), is \(\binom{n}{k}\binom{n-k}{k}\) when \(n=2k+1\), and is \(\binom{n}{k+1}^2\) when \(n\ge2k+2\).

## Assumptions and scope
The graph is finite, simple, and undirected. The theorem is stated for \(n\ge3\), so the crown graph is connected, and for every admissible \(k\) with \(1\le k\le n-1\), which is the full range allowed by the minimum degree \(n-1\). The result concerns \(k\)-tuple **total restrained** domination, not ordinary \(k\)-tuple domination, ordinary restrained domination, or \(k\)-tuple restrained domination using closed neighborhoods.

## Proof
For each \(i\), the neighbors of \(a_i\) are all vertices of \(B\) except \(b_i\). Hence
\[
|N(a_i)\cap S|=|J|-\mathbf 1_{i\in J}.
\]
Because \(k\ge1\), the set \(J\) is nonempty in any feasible solution, and the worst case occurs at an index in \(J\). Therefore every \(a_i\) has at least \(k\) neighbors in \(S\) exactly when \(|J|\ge k+1\). By symmetry, every \(b_i\) has at least \(k\) neighbors in \(S\) exactly when \(|I|\ge k+1\).

Now let \(a_i\notin S\), so \(i\in X\). The number of its neighbors outside \(S\) is
\[
|N(a_i)\setminus S|=|Y|-\mathbf 1_{i\in Y}.
\]
If \(|Y|\ge k+1\), this is automatically at least \(k\). If \(|Y|=k\), it is at least \(k\) for every \(i\in X\) exactly when no such \(i\) lies in \(Y\), equivalently \(X\cap Y=\varnothing\). If \(|Y|<k\), feasibility is impossible. The symmetric statement for vertices \(b_j\notin S\) says that \(|X|\ge k\), with the same disjointness condition when \(|X|=k\).

If exactly one of \(X,Y\) is empty, an outside vertex on the opposite side has no outside neighbor, so such a set is impossible. If both are empty, \(S=V\) is feasible because every vertex has degree \(n-1\ge k\). Combining these observations proves the structural criterion.

For a non-full feasible set, the inequalities \(|I|\ge k+1\) and \(|J|\ge k+1\) are equivalent to
\[
|X|,|Y|\le n-k-1.
\]
Together with the outside-neighbor conditions, this gives
\[
k\le |X|,|Y|\le n-k-1.
\]
If \(n\le2k\), this interval is empty, so only \(V\) survives.

Assume \(n\ge2k+1\) and write \(a=|X|\), \(b=|Y|\). When \(a,b\ge k+1\), there is no overlap restriction and the number of ordered pairs \((X,Y)\) is \(\binom{n}{a}\binom{n}{b}\). When \(a=k\) and \(b\ge k+1\), disjointness gives \(\binom{n}{k}\binom{n-k}{b}\) pairs; the symmetric boundary contributes the factor \(2\). When \(a=b=k\), the number is \(\binom{n}{k}\binom{n-k}{k}\). Since \(|S|=2n-a-b\), summing these cases gives the displayed enumerator.

Finally, if \(n=2k+1\), every non-full feasible set has \(|X|=|Y|=k\), hence weight \(2k+2\), with the stated disjoint-pair count. If \(n\ge2k+2\), the smallest weight is obtained by maximizing both outside sizes at \(n-k-1\); there is then no overlap restriction, so the minimum weight is \(2k+2\) and the count is
\[
\binom{n}{n-k-1}^2=\binom{n}{k+1}^2.
\]
This proves all claims.

## Verification
A standalone exhaustive checker enumerates every subset for \(3\le n\le8\) and every \(1\le k\le n-1\). It independently tests the neighborhood definition, the structural criterion, every coefficient of the claimed enumerator, the minimum value, and the minimum-set count. Its replay output is:

`VERIFY_OK n_range=3..8 subset_checks=582528 criterion_checks=582528 coefficient_checks=83 minimum_checks=54 max_order=16`

The finite computation is only a check of the symbolic proof above; it is not used as evidence for the infinite quantifiers.

## Relationship to prior work
Kazemi introduced \(k\)-tuple total restrained domination and proved, for a general bipartite graph of minimum degree at least \(k\), the lower bound \(2k\) together with a characterization of equality. That result does not determine the crown case: the deleted perfect matching forces at least \(k+1\) selected vertices on each bipartition side, so equality at \(2k\) never occurs. The present theorem resolves the next exact value and, more strongly, classifies and enumerates every feasible set for every admissible \(k\).

The earlier total-restrained paper of Ma, Chen, and Sun treats the case \(k=1\) and gives exact values for complete bipartite graphs, but a crown graph is obtained by deleting a perfect matching from a balanced complete bipartite graph and is not covered by that complete-bipartite formula. A later paper on diameter two or three gives general results and bounds but not the all-set crown classification. Searches for the crown aliases “crown graph,” “complete bipartite graph minus a perfect matching,” and the parameter name did not locate a prior statement of the theorem or enumerator.

## Limitations
The originality conclusion is based on the inspected primary sources, exact-phrase and alias searches, and comparison with the closest available published results; poorly indexed literature remains a residual risk. The theorem does not address the associated domatic number, upper minimal-set parameter, bondage variants, or crown graphs with an unbalanced matching deletion.

## References
1. A. P. Kazemi, “k-tuple total restrained domination and k-tuple total restrained domatic in graphs,” arXiv:1106.5591v1, 28 June 2011; later Bulletin of the Iranian Mathematical Society 40 (2014), 751–763. https://arxiv.org/abs/1106.5591
2. D.-x. Ma, X.-G. Chen, and L. Sun, “On total restrained domination in graphs,” Czechoslovak Mathematical Journal 55 (2005), 165–173, DOI: 10.1007/s10587-005-0012-2. https://dml.cz/handle/10338.dmlcz/127967
3. Z. Tahmasbzadehbaee, D. S. Nandappa, H. A. Ahangar, D. A. Mojdeh, and Y. Zhao, “Total restrained domination in graphs of diameter 2 or 3,” Mathematical Sciences 7 (2013), article 26, DOI: 10.1186/2251-7456-7-26.
