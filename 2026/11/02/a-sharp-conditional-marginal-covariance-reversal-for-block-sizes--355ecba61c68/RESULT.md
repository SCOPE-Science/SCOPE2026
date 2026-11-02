# A sharp conditional–marginal covariance reversal for block sizes in random noncrossing partitions

## Finding

Let \(\Pi_n\) be uniformly distributed on the noncrossing partitions of \([n]\), with \(n\ge 2\). Let \(K\) be its total number of blocks, and \(S_j\) its number of blocks containing exactly \(j\) elements.

**Theorem (conditional phase boundary and unconditional sign).** For every \(n\ge4\), \(2\le r\le n-2\), and \(2\le k\le n-r+1\), define
\[
p_{n,k,r}=\frac{\binom{n-r-1}{k-2}}{\binom{n-1}{k-1}}>0.
\]
Then the conditional covariance has the exact factorization
\[
\operatorname{Cov}(S_1,S_r\mid K=k)
=\frac{k(k-1)p_{n,k,r}}{(n-1)(n-r-1)}\bigl(rk-2(n-1)\bigr).
\]
In particular, its sign is negative, zero, or positive according as \(rk\) is less than, equal to, or greater than \(2(n-1)\). If \(k=1\) or \(k>n-r+1\), this covariance is zero because the relevant count is deterministic. The exceptional near-full-block case is \(r=n-1\): for \(k=2\) and \(n\ge3\),
\[
\operatorname{Cov}(S_1,S_{n-1}\mid K=2)=\frac{2(n-3)}{(n-1)^2},
\]
whereas it is zero for all other values of \(k\). For \(r=n\), the conditional covariance vanishes for every \(k\).

In contrast, **without conditioning on \(K\)**,
\[
\operatorname{Cov}(S_1,S_r)<0
\qquad (n\ge2,\ 2\le r\le n).
\]
Thus conditioning on the number of blocks can reverse the sign of the dependence, not just its magnitude.

This reversal persists on the linear scale at the typical number of blocks. For each fixed \(r\ge5\), taking \(k_n=\lfloor(n+1)/2\rfloor\) gives
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(S_1,S_r\mid K=k_n)}{n}
=\frac{r-4}{2^{r+3}}>0,
\qquad
\lim_{n\to\infty}\frac{\operatorname{Cov}(S_1,S_r)}{n}
=-\frac1{2^{r+3}}<0.
\]

## Assumptions and scope

A noncrossing partition of \([n]\) is a set partition containing no two blocks with elements \(a<c\) and \(b<d\), respectively, in cyclic order \(a<b<c<d\). The law is uniform on all such partitions; the conditional law given \(K=k\) is defined for every integer \(1\le k\le n\). The theorem concerns distinct block sizes \(1\) and \(r\ge2\), and the covariance is taken with respect to the stated finite probability space.

The conditional conclusion remains valid under any positive reweighting of partitions that depends **only** on \(K\), because such a reweighting does not change the law given \(K=k\). This invariance is not asserted for arbitrary block-size weights. The case \(n=2\) in the unconditional assertion is checked directly; cases excluded from the displayed conditional formula are addressed explicitly in the theorem.

## Proof

**1. Block profiles and conditional compositions.** Let \(m_j\) be the number of blocks of size \(j\) in a noncrossing partition, where \(\sum_j j m_j=n\) and \(\sum_jm_j=k\). The classical noncrossing-block profile formula is
\[
N_n((m_j))=\frac{n!}{(n+1-k)!\prod_jm_j!}.
\]
For completeness, write the multivariate ordinary generating function as
\[
F(z)=1+\sum_{j\ge1}u_j(zF(z))^j,
\quad T(z)=zF(z).
\]
The decomposition by the block containing the first point yields \(T=z(1+\sum_{j\ge1}u_jT^j)\). Lagrange inversion gives
\[
[z^n]F(z)=\frac1{n+1}[t^n]\left(1+\sum_{j\ge1}u_jt^j\right)^{n+1},
\]
whose coefficient of \(\prod_j u_j^{m_j}\) is exactly the stated profile count.

Now order the \(k\) distinct blocks uniformly and record their sizes \((L_1,\ldots,L_k)\). For every positive composition \(\ell_1+\cdots+\ell_k=n\), the number of ordered noncrossing partitions with that size vector is
\[
N_n((m_j))\prod_jm_j!=\frac{n!}{(n+1-k)!},
\]
independent of the composition. Hence \((L_1,\ldots,L_k)\mid(K=k)\) is **uniform among the \(\binom{n-1}{k-1}\) positive compositions of \(n\) into \(k\) parts**. As \(S_j=\#\{i:L_i=j\}\), this equality holds for every joint block-size count statistic.

**2. Conditional factorial moments.** Fix \(n\ge4\), \(2\le r\le n-2\), and \(2\le k\le n-r+1\). Counting the remaining positive parts after prescribing one or two parts gives
\[
\begin{aligned}
\mathbb E[S_1\mid K=k]&=\frac{k\binom{n-2}{k-2}}{\binom{n-1}{k-1}}=\frac{k(k-1)}{n-1},\\
\mathbb E[S_r\mid K=k]&=\frac{k\binom{n-r-1}{k-2}}{\binom{n-1}{k-1}}=k p_{n,k,r},\\
\mathbb E[S_1S_r\mid K=k]&=\frac{k(k-1)\binom{n-r-2}{k-3}}{\binom{n-1}{k-1}}.
\end{aligned}
\]
Here \(\binom{a}{b}=0\) for \(b<0\) or \(b>a\) when \(a\ge0\). The ratio identity
\[
\frac{\binom{n-r-2}{k-3}}{\binom{n-r-1}{k-2}}=\frac{k-2}{n-r-1}
\]
(including \(k=2\), where both sides are zero) implies
\[
\begin{aligned}
\operatorname{Cov}(S_1,S_r\mid K=k)
&=k(k-1)p_{n,k,r}\left(\frac{k-2}{n-r-1}-\frac{k}{n-1}\right)\\
&=\frac{k(k-1)p_{n,k,r}}{(n-r-1)(n-1)}\bigl(rk-2(n-1)\bigr).
\end{aligned}
\]
All factors outside the final parenthesis are strictly positive. For \(r=n-1\), a block of that size can coexist with another block only when \(k=2\); the uniform positive-composition representation shows that \(S_1=S_{n-1}\) is Bernoulli with parameter \(2/(n-1)\), yielding the exceptional variance. The remaining degenerate cases follow from feasibility.

**3. Strict unconditional negativity.** Write \(C_n=\binom{2n}{n}/(n+1)\). Marking one or two blocks in the same generating function and applying Lagrange inversion gives, for \(n\ge3\),
\[
\begin{aligned}
\mathbb E S_1&=\frac{\binom{2n-2}{n-1}}{C_n},\\
\mathbb E S_r&=\frac{\binom{2n-r-1}{n-1}}{C_n},\\
\mathbb E(S_1S_r)&=\frac{n\binom{2n-r-3}{n-2}}{C_n}.
\end{aligned}
\]
For \(r=n\), the last binomial coefficient is interpreted as zero. Let \(b=2n-r-1\) and
\[
\Delta_{n,r}=(n+1)b(b-1)-2(2n-1)(n-1)(n-r).
\]
An exact cancellation of factorial ratios yields
\[
\operatorname{Cov}(S_1,S_r)
=-\frac{\mathbb E S_r\,n\,\Delta_{n,r}}{2(2n-1)b(b-1)}.
\]
All denominator terms and \(\mathbb E S_r\) are positive. The numerator has the strictly positive certificate
\[
4(n+1)\Delta_{n,r}=
\bigl(2(n+1)r-7n+5\bigr)^2
+16(n-3)^3+87(n-3)^2+144(n-3)+64>0.
\]
This proves unconditional negativity for \(n\ge3\). When \(n=2\) and \(r=2\), the two noncrossing partitions give covariance \(-1/2\).

**4. Linear-scale reversal.** For fixed \(r\) and \(k_n=\lfloor(n+1)/2\rfloor\), the binomial ratio \(p_{n,k_n,r}\to2^{-r}\) and \(k_n/n\to1/2\). Substitution in the conditional identity gives \((r-4)/2^{r+3}\) after division by \(n\). The exact unconditional expression, using \(\mathbb E S_r/n\to2^{-(r+1)}\) and \(\Delta_{n,r}/n^2\to4\), gives the other limit.

## Verification

The independent enumeration script `verify.py` constructs all set partitions as restricted-growth strings, filters noncrossing partitions directly, and compares every block profile with the Lagrange-inversion count through \(n=10\). It then compares conditional and unconditional covariances with exact rational sums over those objects, verifies all boundary cases, and checks the closed factorization and positive-square certificate for all integer parameters through \(n=160\). Running `python3 verify.py` produced **2,074,703 exact assertions passed**. These calculations are finite checks of the displayed analytic proof, not substitutes for its quantifiers.

As an illustrative arithmetic zero with genuine dependence, at \(n=7\), \(k=4\), \(r=3\), there are \(20\) positive compositions. Their size profiles have multiplicities \(4\) for \((4,1,1,1)\), \(12\) for \((3,2,1,1)\), and \(4\) for \((2,2,2,1)\). Thus \(\operatorname{Cov}(S_1,S_3\mid K=4)=0\), but the two counts are not independent: \(S_3=1\) forces \(S_1=2\), while \(S_3=0\) permits \(S_1=1\) or \(3\).

## Relationship to prior work

Kreweras established the full block-profile enumeration for noncrossing partitions; that enumeration is not claimed as new. Kortchemski and Marzouk (2015, arXiv:1503.09174v1) study uniform and weighted random noncrossing partitions, including block-size constraints, and give a tree-bijection framework. Kargin (2019, arXiv:1907.00632v1, §2.2) gives generating functions and the negative leading-order *unconditional* covariance of two distinct block-size counts. The contribution here is an exact finite-sample **conditional sign classification for all singleton/other-size pairs**, including its exceptional cases, and the resulting opposite-sign conditional/marginal dependence at a typical block count. It is a consequence requiring new comparison of moments extracted from known profile formulas, not a claim of new profile enumeration or statistical independence at the zero-covariance boundary.

## Limitations

The theorem does not classify conditional covariances between two sizes both greater than one, nor arbitrary nonuniform weights on individual block sizes. The assertion of novelty is restricted to the explicit signed dependence law and its contrast with the unconditional sign; the exact profile law itself is classical. Prior full-profile formulas already encode the needed factorial moments, so undiscovered earlier analyses of those formulas could contain an equivalent sign classification. No independent audit has been conducted.

## References

- G. Kreweras, *Sur les partitions non croisées d'un cycle*, Discrete Mathematics 1 (1972), 333–350. DOI: 10.1016/0012-365X(72)90041-6.
- I. Kortchemski and C. Marzouk, *Simply generated non-crossing partitions*, first public arXiv version dated 2015-03-31, arXiv:1503.09174v1, https://arxiv.org/abs/1503.09174.
- V. Kargin, *Limit theorems for statistics of non-crossing partitions*, first public arXiv version dated 2019-07-01, arXiv:1907.00632v1, https://arxiv.org/html/1907.00632v1, especially §2.2.
- C. A. Athanasiadis, *On noncrossing and nonnesting partitions for classical reflection groups*, Electronic Journal of Combinatorics 5 (1998), DOI: 10.37236/1380. Cited for the classical block-profile context only.
