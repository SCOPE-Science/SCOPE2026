# Exact finite null coupling of Mann–Whitney and two-sample Cramér–von Mises
## Finding
Take two independent samples of sizes \(m,n\ge1\) from the same continuous distribution and put \(N=m+n\). After pooling and sorting the observations, write
\[
X_j=\mathbf 1\{\text{the }j\text{th pooled rank comes from sample 1}\},
\qquad
A_j=\sum_{i=1}^jX_i.
\]
Under the null, \((X_1,\ldots,X_N)\) is uniform over all binary words with exactly \(m\) ones and \(n\) zeros. Define the bridge coordinates
\[
B_j=NA_j-mj,\qquad 1\le j\le N-1.
\]
Let \(U\) be the Mann–Whitney count obtained by subtracting \(m(m+1)/2\) from the sum of the sample-1 pooled ranks, and put
\[
Q=U-\frac{mn}2,
\qquad
Z=\frac{Q}{\sqrt{mn(N+1)/12}}.
\]
Let Anderson's two-sample Cramér–von Mises statistic be
\[
T=\frac{mn}N\int (F_m-G_n)^2\,dH_N.
\]
Then
\[
T=\frac1{mnN^2}\sum_{j=1}^{N-1}B_j^2
\]
and the exact finite-sample covariance is
\[
\boxed{
\operatorname{Cov}(Z^2,T)
=\frac{(3N+4)mn-N(2N+1)}{15mnN}
}.
\]
Equivalently,
\[
\boxed{
\operatorname{Cov}\!\left(Q^2,\sum_{j=1}^{N-1}B_j^2\right)
=\frac{N(N+1)mn}{180}
\bigl((3N+4)mn-N(2N+1)\bigr)
}.
\]
For \(N=2\) the only case is \(m=n=1\), and the covariance is zero. For every \(N\ge3\) it is strictly positive. If \(m/N\to\lambda\in(0,1)\), then
\[
\operatorname{Cov}(Z^2,T)\longrightarrow\frac15.
\]
Thus the squared standardized Mann–Whitney location component retains a universal positive covariance \(1/5\) with the omnibus Cramér–von Mises statistic under proportional two-sample asymptotics.

## Assumptions and scope
The two samples are independent and drawn from one common continuous null distribution, so ties occur with probability zero and the pooled label word is exactly uniform conditional on \(m,n\). The chosen Mann–Whitney orientation does not matter after squaring the centered statistic. The Cramér–von Mises normalization is Anderson's
\[
T=\frac{mn}N\int(F_m-G_n)^2\,dH_N.
\]
No claim is made for ties, unequal null distributions, estimated nuisance parameters, or alternative normalizations without the displayed conversion.

## Proof
Let
\[
R=\sum_{j=1}^N jX_j
\]
be the sample-1 rank sum. Since \(U=R-m(m+1)/2\),
\[
Q=R-\frac{m(N+1)}2.
\]
Summation by parts gives the bridge-area identity
\[
\sum_{j=1}^{N-1}B_j=-NQ.
\]
At pooled rank \(j\),
\[
F_m-G_n=\frac{A_j}m-\frac{j-A_j}n=\frac{B_j}{mn},
\]
while \(H_N\) places mass \(1/N\) at each pooled observation. Hence
\[
T=\frac1{mnN^2}S,
\qquad
S:=\sum_{j=1}^{N-1}B_j^2.
\]

We use the following finite-population moment lemma for a uniformly chosen \(m\)-subset of \(\{1,\ldots,N\}\):
\[
\mathbb E Q^2=\frac{mn(N+1)}{12},
\qquad
\mathbb E S=\frac{mnN(N+1)}6,
\]
and
\[
\mathbb E(Q^2S)
=\frac{N(N+1)mn}{360}
\left((11N+13)mn-2N(2N+1)\right).
\tag{1}
\]
The first identity is the usual variance of a simple-random-sample rank sum. For the second, \(A_j\) is hypergeometric, so
\[
\mathbb E B_j^2
=\frac{mn}{N-1}j(N-j),
\]
and summing \(j(N-j)\) gives the displayed formula.

For completeness, the third identity is a direct fourth-order sampling-without-replacement calculation. Put
\[
c_i=i-\frac{N+1}2,
\qquad Q=\sum_{i=1}^N c_iX_i.
\]
Expand \(Q^2S\) as a multilinear polynomial in the indicators \(X_i\), reducing every \(X_i^r\) to \(X_i\). For every set of \(r\) distinct indices,
\[
\mathbb E\prod_{i\in J}X_i=\frac{(m)_r}{(N)_r},
\qquad 0\le r\le4.
\tag{2}
\]
Substituting (2), collecting equality patterns of the four indicator indices, and using the elementary power sums through degree four yields
\[
360\,\mathbb E(Q^2S)
=N(N+1)mn\left((11N+13)mn-2N(2N+1)\right),
\]
which is (1). This calculation contains no limiting step; it is an identity in the integers \(m,n\).

Subtracting the product of the first two moments from (1) gives
\[
\operatorname{Cov}(Q^2,S)
=\frac{N(N+1)mn}{180}
\left((3N+4)mn-N(2N+1)\right).
\]
Finally divide by \(mnN^2\) to replace \(S\) by \(T\), and by \(mn(N+1)/12\) to replace \(Q^2\) by \(Z^2\). This gives
\[
\operatorname{Cov}(Z^2,T)
=\frac{(3N+4)mn-N(2N+1)}{15mnN}.
\]
Since \(mn\ge N-1\),
\[
(3N+4)mn-N(2N+1)
\ge (3N+4)(N-1)-N(2N+1)=N^2-4,
\]
so the covariance is positive for \(N\ge3\). Under \(m/N\to\lambda\in(0,1)\), division of numerator and denominator by \(mnN\) gives the limit \(1/5\).

## Verification
The accompanying `checker.py` exhaustively enumerates every pooled binary label word for every positive pair \(m,n\) with \(m+n\le14\). It checks the bridge-area identity, the Cramér–von Mises normalization, the two marginal second moments, the mixed fourth moment (1), the raw covariance, and the standardized covariance using exact rational arithmetic. The all-\(m,n\) proof is the algebra above; the finite enumeration is supplementary.

## Relationship to prior work
Anderson's 1962 paper introduced and studied the exact finite-sample distribution of the two-sample Cramér–von Mises statistic, including its rank representation. That source supplies the classical statistic and finite-null framework, but the checked accessible material does not state the mixed moment with a Mann–Whitney component.

Pettitt's 1979 paper is the closest conceptual comparison located. Its abstract states that weighted two-sample Cramér–von Mises rank statistics can be written as sums of squares of linear rank statistics and specifically relates examples to Wilcoxon, Mood, normal-scores, and Savage statistics. Open-access retrieval did not expose the full article, and a full-text retrieval attempt reached a publisher verification gate, so the article could not be inspected beyond its abstract and indexed metadata in this run. It therefore remains an explicit residual literature risk rather than being asserted not to contain a related formula.

A modern full-text treatment of the two-sample Cramér–von Mises statistic confirms Anderson's normalization and distribution-free null formulation. Searches using the exact covariance form, squared Wilcoxon/Mann–Whitney aliases, bridge-area terminology, and component language did not locate the finite covariance displayed here. Published-record searches likewise returned no statement implying it.

## Limitations
The novelty comparison is bounded by the inaccessible full text of Pettitt's 1979 article, which is unusually relevant because it explicitly connects Cramér–von Mises components to Wilcoxon rank statistics. The present result should therefore be read as an exact finite identity not found in the sources that could be materially inspected, not as proof of absence from all historical literature.

The theorem assumes a continuous common null and Anderson's normalization. It describes a covariance, not independence or a complete joint distribution.

## References
1. T. W. Anderson, “On the Distribution of the Two-Sample Cramer-von Mises Criterion,” *Annals of Mathematical Statistics* 33 (1962), 1148–1159. DOI: 10.1214/aoms/1177704477.
2. A. N. Pettitt, “Two-Sample Cramér-Von Mises Type Rank Statistics,” *Journal of the Royal Statistical Society, Series B* 41 (1979), 46–53. DOI: 10.1111/j.2517-6161.1979.tb01056.x.
