# A local shielding law for records and descents in uniform permutations

## Finding

Let \(\Pi\) be a uniformly random permutation of \(\{1,\ldots,n\}\), with \(n\ge2\). Define the upper-record indicators and ordinary descent indicators by
\[
R_i=\mathbf 1\{\Pi(i)>\max_{h<i}\Pi(h)\},\quad 1\le i\le n,\qquad
D_j=\mathbf 1\{\Pi(j)>\Pi(j+1)\},\quad 1\le j<n,
\]
with \(R_1=1\). For every \(j<n\), the descent \(D_j\) is independent **jointly** of the entire vector \((R_i:i\notin\{j,j+1\})\). More generally, if \(J\subseteq\{1,\ldots,n-1\}\) contains no consecutive integers and \(E(J)=\bigcup_{j\in J}\{j,j+1\}\), then
\[
(D_j:j\in J)\quad\text{are mutually independent fair Bernoulli variables, jointly independent of }(R_i:i\notin E(J)).
\]
This is conditional joint independence, not merely vanishing pairwise covariance.

For all \(1\le i\le n\) and \(1\le j<n\), the exact cross-covariance matrix is
\[
\boxed{\operatorname{Cov}(R_i,D_j)=
\begin{cases}
\dfrac{j-1}{2j(j+1)},&i=j,\\[2pt]
-\dfrac1{2(j+1)},&i=j+1,\\[2pt]
0,&\text{otherwise}.
\end{cases}}
\]
Consequently, writing \(K_n=\sum_{i=1}^n R_i\) for the number of records and \(T_n=\sum_{j=1}^{n-1}D_j\) for the number of descents,
\[
\boxed{\operatorname{Cov}(K_n,D_j)=-\frac1{2j(j+1)},\qquad
\operatorname{Cov}(K_n,T_n)=-\frac{n-1}{2n}.}
\]
As \(n\to\infty\),
\[
\operatorname{Corr}(K_n,T_n)\sim-\sqrt{\frac3{n\log n}}.
\]

## Assumptions and scope

The permutation is uniform on the whole symmetric group. Upper records use the strict inequality in birth/position order; descents compare adjacent positions in its one-line notation. All statements are exact for integer \(n\ge2\). The matching condition on \(J\) means that the pairs of positions \(\{j,j+1\}\), \(j\in J\), are disjoint. The statement does not claim that the entire vector of all descents is jointly independent of the entire record process.

## Proof

Represent the permutation by ranks of independent continuous uniform variables \(U_1,\ldots,U_n\), so comparisons, records and descents agree almost surely. Fix \(j\), and interchange the observations at indices \(j\) and \(j+1\). Uniform sampling is invariant under this involution, the descent indicator \(D_j\) is replaced by \(1-D_j\), and every record indicator outside the set \(\{j,j+1\}\) is unchanged: for \(i<j\) the inspected prefix is untouched, and for \(i>j+1\) the set of values in the inspected prefix is unchanged. Thus, conditional on the entire outside-record vector, the two values of \(D_j\) are equiprobable. This proves joint independence, not only pairwise independence.

For a matching \(J\), the adjacent interchanges at distinct sites commute. Their \(2^{|J|}\)-element action preserves the vector of records outside \(E(J)\) while acting freely and transitively on the \(2^{|J|}\) possible sign vectors of the comparisons at these sites. Under the uniform measure, conditional on the outside-record vector every sign vector therefore has probability \(2^{-|J|}\). This proves the matching-site statement.

The record event has probability \(\mathbb P(R_i=1)=1/i\), and every descent has probability \(1/2\). By the shielding identity, \(\operatorname{Cov}(R_i,D_j)=0\) outside the two adjacent record indices. For \(i=j\), conditional on \(R_j=1\), \(U_j\) is the maximum of \(j\) independent uniforms, with conditional mean \(j/(j+1)\); hence \(\mathbb P(D_j=1\mid R_j=1)=j/(j+1)\). Therefore
\[
\operatorname{Cov}(R_j,D_j)=\frac1j\left(\frac{j}{j+1}-\frac12\right)=\frac{j-1}{2j(j+1)}.
\]
For \(i=j+1\), \(R_{j+1}=1\) forces an ascent from position \(j\) to position \(j+1\), so \(R_{j+1}D_j=0\), and
\[
\operatorname{Cov}(R_{j+1},D_j)=-\frac1{2(j+1)}.
\]
Summing the two entries in a column yields \(-1/[2j(j+1)]\). Summing these columns and telescoping \(\sum_{j=1}^{n-1}1/[j(j+1)]=1-1/n\) proves the total covariance.

For the correlation, the classical independent-record-indicator law gives \(\operatorname{Var}(K_n)=H_n-H_n^{(2)}\), where \(H_n=\sum_{k=1}^{n}1/k\) and \(H_n^{(2)}=\sum_{k=1}^{n}1/k^2\). Each descent has variance \(1/4\); nonadjacent descents are independent, while adjacent descents have covariance \(-1/12\) by ordering three exchangeable continuous variables. Hence \(\operatorname{Var}(T_n)=(n+1)/12\). Substitution gives the displayed asymptotic correlation.

## Verification

The standalone `records_descents_verify.py` computes the entire cross-covariance matrix and total covariance exactly by enumerating every permutation through \(n=9\); it also checks conditional matching-site shielding across all eligible matching-site subsets through \(n=7\). The checker reports 528 exact comparisons. These finite computations confirm boundary cases and notation; they do not replace the all-\(n\) symmetry proof.

## Relationship to prior work

Gnedin's treatment of record statistics in coherent random permutations develops record-based distributions without an ordinary-descent/local-record shielding theorem. Jin develops generating functions for aggregate Euler–Stirling statistics including descents and left-to-right maxima; such total-statistic formulas encompass aggregate mixed moments but erase the particular positions needed for the conditional shielding property. A published fixed-point–descent result gives a sparse position-wise covariance law for *fixed points*, not the nonlocal prefix-maximum indicators here. Its result concerns second moments and does not imply the matching-site conditional independence asserted above.

The new structural content is the record-vector shielding under disjoint adjacent swaps and its exact two-diagonal consequence. The aggregate covariance alone is not claimed as a historical novelty independent of known aggregate generating functions.

## Limitations

This law depends on exchangeability of a uniform permutation. It need not hold for distributions biased by inversions, records or other parameters. The covariance matrix alone does not determine the full joint law of all record and descent indicators. General enumerations of descent sets with positional record constraints may contain an equivalent shielding result; that remains a priority risk, and no historical-uniqueness assertion is made.

## References

1. A. Gnedin, “Coherent random permutations with record statistics,” arXiv:math/0611538, first submitted 2006-11-17.
2. E. Y. Jin, “Symmetric generating functions and Euler-Stirling statistics on permutations,” arXiv:2210.08789, first submitted 2022-10-17.
3. “Boundary localization of fixed-point–descent dependence in a uniform permutation,” published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-boundary-localization-of-fixed-point-descent-dependence-in-a-uni--6e228e1e9495 .
