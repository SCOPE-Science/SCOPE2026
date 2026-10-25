# Resolving number of every Johnson graph: a two-exception binomial law

## Finding

For all integers \(n\ge 2\) and \(1\le k\le n-1\), the resolving number (equivalently, metric-dimension threshold) of the Johnson graph \(J(n,k)\) is
\[
\operatorname{res}(J(n,k))=
\begin{cases}
5,&(n,k)=(4,2),\\
37,&(n,k)=(8,4),\\
\displaystyle\binom nk-2\binom{n-2}{k-1}+1,&\text{otherwise}.
\end{cases}
\]
In particular, pairs of adjacent vertices give a largest possible set of nonresolving landmarks, except in the two exceptional Johnson graphs, where pairs at maximal distance give strictly larger nonresolving sets. The two exceptions are genuine: in \(J(4,2)\), adjacent and opposite pairs admit respectively \(2\) and \(4\) common equidistant vertices; in \(J(8,4)\), these counts are respectively \(30\) and \(36\).

## Assumptions and scope

The graph \(J(n,k)\) has as vertices the \(k\)-subsets of \([n]=\{1,\ldots,n\}\); two vertices are adjacent exactly when their intersection has cardinality \(k-1\). Its distance is \(d(A,B)=k-|A\cap B|\). A set \(S\) resolves the graph if, for each distinct pair \(A,B\), at least one \(W\in S\) has \(d(W,A)\ne d(W,B)\). Define \(\operatorname{res}(G)\) to be the least integer \(t\) for which **every** \(t\)-element vertex set resolves \(G\). This is not the usual metric dimension, which minimizes the size of **some** resolving set. We adopt the convention \(\binom ab=0\) when \(b<0\) or \(b>a\).

The complement map identifies \(J(n,k)\) with \(J(n,n-k)\); throughout the proof we therefore assume \(1\le k\le n/2\) without loss of generality. All statements are for finite simple graphs and all admissible integer parameters, not merely tested dimensions.

## Proof

**1. Reduction to equal-distance counts.** For distinct vertices \(A,B\), let \(E(A,B)=\{W:d(W,A)=d(W,B)\}\). A set is nonresolving precisely when it lies inside some \(E(A,B)\). Consequently
\[
\operatorname{res}(G)=1+\max_{A\ne B}|E(A,B)|.
\]
Write \(r=|A\setminus B|=|B\setminus A|\); then \(1\le r\le k\). The criterion \(d(W,A)=d(W,B)\) says \(|W\cap(A\setminus B)|=|W\cap(B\setminus A)|\). Hence the number of equal-distance vertices for any pair at distance \(r\) is exactly
\[
E_r(n,k)=\sum_{j=0}^{r}\binom rj^2\binom{n-2r}{k-2j}
=[z^k](1+z)^{n-2r}S_r(z),\qquad
S_r(z)=\sum_{j=0}^{r}\binom rj^2z^{2j}.
\]
In particular,
\[
E_1(n,k)=\binom{n-2}{k}+\binom{n-2}{k-2}
=\binom nk-2\binom{n-2}{k-1}.
\]

**2. A coefficientwise binomial inequality.** For every integer \(r\ge1\), the polynomial
\[
D_r(z)=(1+z)^{2r-1}(1+z^2)-(1+z)S_r(z)
\]
has nonnegative coefficients. Both terms are palindromic of degree \(2r+1\), so it suffices to check degrees at most \(r\). At an even degree \(2j<r\), the coefficient on the left before subtraction is \(\binom{2r-1}{2j}+\binom{2r-1}{2j-2}\), while the coefficient of \((1+z)S_r(z)\) is \(\binom rj^2\). The case \(j=0\) is equality. Otherwise, Vandermonde's identity, splitting \(2r-1\) into blocks of lengths \(r\) and \(r-1\), gives
\[
\binom{2r-1}{2j}\ge
\binom rj\binom{r-1}{j}
+\binom r{j+1}\binom{r-1}{j-1}
\ge\binom rj^2,
\]
since \(2j<r\) ensures \(\binom r{j+1}\ge\binom rj\). At an odd degree \(2j+1\le r\), the corresponding Vandermonde terms yield
\[
\binom{2r-1}{2j+1}+\binom{2r-1}{2j-1}
\ge \binom r{j+1}\binom{r-1}{j}
+\binom rj\binom{r-1}{j-1}
\ge\binom rj^2.
\]
Here \(2j+1\le r\) similarly implies \(\binom r{j+1}\ge\binom rj\); for \(j=0\), terms with lower index \(-1\) vanish.

The only remaining coefficient has degree \(r\) when \(r\) is even. At \(r=2\), its two sides are \(4\) and \(4\); at \(r=4\), they are \(56\) and \(36\). For even \(r\ge6\), write \(a=\binom r{r/2}\) and \(b=\binom r{r/2-1}=a\,r/(r+2)\). Since \(2b^2\ge a^2\), Vandermonde gives
\[
\binom{2r-1}{r}=\tfrac12\binom{2r}{r}
=\tfrac12\sum_{i=0}^r\binom ri^2
\ge\tfrac12(a^2+2b^2)\ge a^2.
\]
The other summand \(\binom{2r-1}{r-2}\) is nonnegative. This finishes the coefficientwise proof.

**3. Non-antipodal pairs are controlled by adjacent pairs.** If \(n\ge2r+1\), then
\[
E_1(n,k)-E_r(n,k)
=[z^k](1+z)^{n-2r-1}D_r(z)\ge0.
\]
Thus only the special case \(n=2r\) might beat adjacent pairs. As \(r\le k\le n/2\), that case forces \(n=2k\) and \(r=k\).

**4. The two antipodal exceptions.** When \(n=2k\) and \(r=k\), we have \(E_k(2k,k)=0\) if \(k\) is odd, whereas for \(k=2h\) even,
\[
E_k(2k,k)=\binom{2h}{h}^2,
\qquad E_1(2k,k)=2\binom{4h-2}{2h-2}.
\]
Put \(B=\binom{2h-1}{h-1}\), so \(\binom{2h}{h}=2B\). For \(h\ge3\), Vandermonde's central term and two neighboring terms give
\[
\binom{4h-2}{2h-2}
\ge B^2+2B\binom{2h-1}{h-2}
=B^2\left(1+\frac{2(h-1)}{h+1}\right)
\ge2B^2.
\]
Therefore \(E_1\ge E_k\) for all even \(k\ge6\). At \(h=1\) the two values are \(2\) and \(4\); at \(h=2\) they are \(30\) and \(36\). These are the only exceptions. Taking the maximum in Step 1 proves the stated formula, and the complement isomorphism extends it from \(k\le n/2\) to all \(1\le k\le n-1\). \(\square\)

## Verification

The standalone standard-library Python program `verify.py` computes \(E_r(n,k)\) by exact integer binomial sums, checks the coefficientwise lemma for \(1\le r\le150\), and verifies the closed formula for all \(2\le n\le80\) and \(1\le k\le\lfloor n/2\rfloor\) (1,600 parameter pairs). Separately, it enumerates actual Johnson vertices, all vertex pairs, and their equidistant witnesses when the graph has at most 150 vertices, covering all tested small cases including both exceptions. The script prints `ALL_PASS` if all assertions succeed. These finite computations are cross-checks, not substitutes for Steps 1–4.

## Relationship to prior work

Garijo, González and Márquez (2013) defined the resolving number and proved the general equal-distance obstruction reduction (their Proposition 2.1), which is used explicitly in Step 1. Bailey and collaborators (2012, published 2013) developed resolving-set constructions for Johnson and Kneser graphs, but addressed the existence of small resolving sets, not the size at which *all* sets resolve. González, Hernando and Mora (first posted July 22, 2021) studied **distance-equalizer sets**, a different condition asking for equal-distance witnesses, and gave Johnson-graph bounds but not the worst-pair equal-distance count required here. Korivand, Khashyarmanesh and Tavakoli (2022) studied the same all-sets invariant under the name *metric dimension threshold*, mainly in other graph families. The new work is the explicit maximization of the Johnson equal-distance count for every \(n,k\), including its two antipodal exceptions; this is not implied merely by a generic obstruction formula.

## Limitations

This theorem determines the resolving number, not the minimum metric dimension, the equidistant dimension, or a complete classification of every maximum nonresolving pair. The proof covers all stated integers; the verification program checks finite ranges only. Published comparisons do not exclude unindexed results in graph-resolvability or constant-weight-code literature. No independent external audit has been performed.

## References

1. A. González, C. Hernando, M. Mora, *The Equidistant Dimension of Graphs*, arXiv:2107.10805v1 (first posted 2021-07-22), and Bulletin of the Malaysian Mathematical Sciences Society 45 (2022), 1757–1775. https://arxiv.org/abs/2107.10805
2. D. Garijo, A. González, A. Márquez, *The resolving number of a graph*, arXiv:1309.0252 (first posted 2013-09-01), Discrete Mathematics & Theoretical Computer Science 15(3) (2013), 155–166. https://arxiv.org/abs/1309.0252
3. R. F. Bailey, J. Cáceres, D. Garijo, A. González, A. Márquez, K. Meagher, M. L. Puertas, *Resolving sets for Johnson and Kneser graphs*, arXiv:1203.2660 (first posted 2012-03-12), European Journal of Combinatorics 34 (2013), 736–751. https://arxiv.org/abs/1203.2660
4. M. Korivand, K. Khashyarmanesh, M. Tavakoli, *Metric Dimension Threshold of Graphs*, Journal of Mathematics 2022, Article 1838719 (first published 2022-09-14). https://doi.org/10.1155/2022/1838719
