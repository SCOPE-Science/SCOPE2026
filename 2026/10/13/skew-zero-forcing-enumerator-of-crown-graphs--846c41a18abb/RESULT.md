# Skew zero-forcing enumerator of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\), with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where the deleted perfect matching consists of the nonedges \(a_i b_i\). For an initial blue set \(S\), define the white-index sets
\[
I=\{i:a_i\notin S\},\qquad J=\{j:b_j\notin S\}.
\]
Then \(S\) is a skew zero-forcing set if and only if
\[
|I|\le2\quad\text{and}\quad |J|\le2.
\]
Consequently, if
\[
A_n(x)=x^n+n x^{n-1}+\binom n2 x^{n-2},
\]
then the complete cardinality enumerator of skew zero-forcing sets is
\[
\mathcal Z^-(\operatorname{Cr}_n;x)=A_n(x)^2.
\]
Thus
\[
Z^-(\operatorname{Cr}_n)=2n-4,
\qquad
[z^{2n-4}]\,\mathcal Z^-(\operatorname{Cr}_n;z)=\binom n2^2.
\]
The second equality says that there are exactly \(\binom n2^2\) minimum skew zero-forcing sets.

There is also a sharp comparison with ordinary zero forcing. Among sets satisfying \(|I|,|J|\le2\), the only extra sets admitted by the skew rule are those with \(I=J\) a two-element set. Hence the skew and ordinary all-set enumerators agree in every coefficient except the minimum layer, where the skew enumerator has exactly \(\binom n2\) additional sets.

## Assumptions and scope
Graphs are finite, simple and undirected. The crown graph is taken in its standard connected range \(n\ge3\). Skew zero forcing uses the rule that a vertex of either color may force when it has exactly one white neighbor. The polynomial records every initial skew zero-forcing set by cardinality; it is not a propagation-time polynomial and does not weight forcing sequences.

The scalar minimum is included as a corollary of the all-set classification. The principal content is the necessary-and-sufficient white-index criterion, its complete enumerator, and the exact one-layer difference between skew and ordinary zero forcing on this matched-deletion family.

## Proof
At any stage of the skew process, let \(I\) and \(J\) denote the indices of the remaining white vertices in \(A\) and \(B\). For any \(r\in[n]\), the vertex \(a_r\) has exactly
\[
|J|-\mathbf 1_{\{r\in J\}}
\]
white neighbors, because it is adjacent to every vertex of \(B\) except \(b_r\). Similarly, \(b_r\) has exactly
\[
|I|-\mathbf 1_{\{r\in I\}}
\]
white neighbors.

If \(|J|\ge3\), then every \(a_r\) has at least two white neighbors, so no force from \(A\) into \(B\) is possible. Therefore \(J\) cannot decrease. Symmetrically, if \(|I|\ge3\), then \(I\) cannot decrease. Hence a skew zero-forcing set must satisfy \(|I|,|J|\le2\).

Conversely, suppose \(|I|,|J|\le2\). If \(|J|=2\), choose \(r\in J\). The vertex \(a_r\), regardless of its own color, is nonadjacent to \(b_r\) and has the other white vertex of \(B\) as its unique white neighbor, so it forces that vertex. Now \(|J|=1\). If \(J=\{j\}\), choose any \(r\ne j\); since \(n\ge3\), such an index exists, and \(a_r\) has \(b_j\) as its unique white neighbor, so it forces \(b_j\). Thus all of \(B\) becomes blue. The same argument with the two sides interchanged then clears \(A\). This proves the criterion.

For a fixed side, choosing zero, one, or two white vertices contributes respectively
\[
x^n,
\qquad n x^{n-1},
\qquad \binom n2 x^{n-2}
\]
to the cardinality enumerator. The two side choices are independent under the criterion, so multiplication gives \(\mathcal Z^-(\operatorname{Cr}_n;x)=A_n(x)^2\). Its least exponent is \(2n-4\), with coefficient \(\binom n2^2\).

For the comparison with ordinary zero forcing, note first that every ordinary force is a skew force. When \(|I|=|J|=2\) and \(I=J\), the only vertices having exactly one white neighbor on the opposite side are indexed by these two omitted indices, and those vertices are themselves white. Hence no ordinary first force exists, while the skew proof above starts precisely by allowing one of them to force. If the two two-element omission sets are not equal, or one side has at most one white vertex, a blue forcing vertex exists on at least one side; after that force the process reduces to a smaller white-index state, and alternating the same observation clears all vertices. Thus the only skew-but-not-ordinary states are \(I=J\in\binom{[n]}2\), giving exactly \(\binom n2\) additional minimum sets.

## Verification
The accompanying verifier constructs \(\operatorname{Cr}_n\) directly and independently simulates both skew and ordinary zero forcing for every initial subset when \(3\le n\le8\). It checks the skew criterion against the dynamics, checks every coefficient against \(A_n(x)^2\), verifies the minimum coefficient \(\binom n2^2\), and verifies that the skew-but-not-ordinary sets are exactly the states \(I=J\) with two omitted indices. Its deterministic output is:

`VERIFY_OK n_range=3..8 subset_checks=87360 skew_sets=3120 ordinary_comparison_checks=87360 coefficient_checks=30 max_order=16`

This finite computation is a regression check only. The theorem for arbitrary \(n\) is supplied by the symbolic neighborhood-count argument above.

## Relationship to prior work
DeAlba's 2014 paper gives the standard skew color-change rule, records primary classification \(05C50\), and studies minimum skew zero-forcing sets through matching structure in broad graph classes. Its public v1 is dated 2014-04-06. The present result refines the question on the crown family from the minimum parameter to a classification of every skew zero-forcing set and its complete cardinality enumerator. The possibility that broad matching results imply the scalar value \(Z^-(\operatorname{Cr}_n)=2n-4\) is therefore not used as the originality basis.

Boyer et al. introduced the ordinary zero forcing polynomial and developed all-cardinality enumeration for ordinary zero forcing. The crown result here is for the skew rule and exposes a particularly small but structural defect between the two processes: allowing white vertices to force changes exactly one coefficient and exactly the matched two-pair omission states.

## Limitations
The result is restricted to ordinary crown graphs with \(n\ge3\) and the standard skew color-change rule. It does not classify forcing sequences or propagation times, and it makes no matrix-rank equality claim beyond the combinatorial forcing parameter. Literature searches did not locate an all-cardinality skew zero-forcing enumerator for crown graphs, but nonindexed theses or specialized tables remain a residual originality risk. The minimum skew zero-forcing number by itself may also be implied by earlier matching or minimum-skew-rank results; the accepted claim is the all-set classification, complete enumerator, and exact skew-versus-ordinary defect.

## References
1. L. M. DeAlba, *Some results on minimum skew zero forcing sets, and skew zero forcing number*, arXiv:1404.1618v1, submitted 2014-04-06. Primary MSC \(05C50\).
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, submitted 2018-01-26.
3. IMA-ISU Research Group on Minimum Rank, *Minimum rank of skew-symmetric matrices described by a graph*, Linear Algebra and its Applications 432 (2010), 2457--2472, DOI 10.1016/j.laa.2009.10.001. This is cited by DeAlba as the source introducing the skew parameter; an exact earlier public-posting day was not used for the date field.