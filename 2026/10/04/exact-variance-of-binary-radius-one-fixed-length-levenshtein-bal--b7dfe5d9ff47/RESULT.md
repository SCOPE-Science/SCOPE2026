# Exact variance of binary radius-one fixed-length Levenshtein balls
## Finding
Let \(X\) be uniformly random in \(\{0,1\}^n\). Write \(L_1(X)\) for the radius-one fixed-length Levenshtein ball centered at \(X\), and set \(B_n=|L_1(X)|\). Then, for every integer \(n\ge 1\),
\[
\mathbb E B_n=\frac{n(n-1)}2+3-2^{1-n},
\]
and
\[
\operatorname{Var}(B_n)=\frac{n^3-9n^2+48n-120}{4}+\frac{n^2+3n+17}{2^{n-1}}-\frac{1}{4^{n-1}}.
\]
In particular,
\[
\operatorname{Var}(B_n)=\frac14 n^3+O(n^2),\qquad
\operatorname{sd}(B_n)=\frac12 n^{3/2}(1+O(n^{-1})).
\]
The expectation is the known normalization. The new point is the exact second-moment law for every length and the resulting sharp root-mean-square scale.

## Assumptions and scope
The alphabet is binary, the center is uniform on \(\{0,1\}^n\), and the ball has radius one in fixed-length Levenshtein distance: a word lies in \(L_1(x)\) exactly when it can be obtained from \(x\) by at most one matched deletion/insertion operation. Equivalently, one may delete one coordinate of \(x\) and insert one binary symbol, with duplicate outputs counted once. The theorem includes the boundary case \(n=1\).

## Proof
Put \(m=n-1\). For \(1\le i\le m\), define
\[
E_i=\mathbf 1\{X_i=X_{i+1}\}.
\]
For a uniform binary word, \(E_1,\ldots,E_m\) are independent Bernoulli variables with parameter \(1/2\): after choosing \(X_1\), any prescribed equality/inequality pattern determines the rest of the word uniquely. Let
\[
K=\sum_{i=1}^{m}E_i.
\]
The maximal alternating segments of \(X\) correspond to the zero-runs of \((E_i)\), allowing zero-length runs at the ends and between adjacent ones. If their zero-run lengths are \(L_1,\ldots,L_{K+1}\), define
\[
Q=\sum_j\binom{L_j}{2}
  =\sum_{1\le i<j\le m}\mathbf 1\{E_i=E_{i+1}=\cdots=E_j=0\}.
\]
The standard radius-one FLL ball formula in terms of runs and alternating segments simplifies in the binary case to the exact identity
\[
B_n=n(n-1)+2-mK-Q. \tag{1}
\]
This identity can also be checked directly from the run/alternating-segment formula: the number of ordinary runs is \(n-K\), while an alternating segment corresponding to a zero-run of length \(L_j\) has length \(L_j+1\).

The first moments are immediate:
\[
\mathbb E K=\frac m2,
\qquad
\mathbb E Q=\sum_{\ell=2}^{m}(m-\ell+1)2^{-\ell}
=\frac m2-1+2^{-m}.
\]
Substituting in (1) gives
\[
\mathbb E B_n=\frac{n(n-1)}2+3-2^{1-n}.
\]

For the covariance, an all-zero interval of length \(\ell\) has covariance \(-2^{-\ell-1}\) with each one of the \(\ell\) Bernoulli coordinates it contains and covariance zero with coordinates outside it. Hence
\[
\operatorname{Cov}(K,Q)
=-\frac12\sum_{\ell=2}^{m}(m-\ell+1)\ell 2^{-\ell}
=\frac{8-3m}{4}-\frac{2m+8}{2^{m+2}}. \tag{2}
\]

It remains to compute \(\operatorname{Var}(Q)\). Process the edge variables from left to right. After \(j\) edges, let \(R_j\) be the current trailing zero-run length and let \(Q_j\) be the accumulated value of \(Q\). If the next edge equals one, then \((R,Q)\) becomes \((0,Q)\); if it equals zero, it becomes \((R+1,Q+R)\). Therefore
\[
\begin{aligned}
\mathbb E R_{j+1}&=\frac{\mathbb E R_j+1}{2},\\
\mathbb E R_{j+1}^2&=\frac{\mathbb E R_j^2+2\mathbb E R_j+1}{2},\\
\mathbb E Q_{j+1}&=\mathbb E Q_j+\frac12\mathbb E R_j,\\
\mathbb E(Q_{j+1}R_{j+1})&=\frac{\mathbb E(Q_jR_j)+\mathbb E Q_j+\mathbb E R_j^2+\mathbb E R_j}{2},\\
\mathbb E Q_{j+1}^2&=\mathbb E Q_j^2+\mathbb E(Q_jR_j)+\frac12\mathbb E R_j^2.
\end{aligned}
\]
Starting from zero at \(j=0\), induction yields
\[
\begin{aligned}
\mathbb E R_j&=1-2^{-j},\\
\mathbb E R_j^2&=3-(2j+3)2^{-j},\\
\mathbb E Q_j&=\frac j2-1+2^{-j},\\
\mathbb E(Q_jR_j)&=\frac j2+2-(j^2+2j+2)2^{-j},\\
\mathbb E Q_j^2&=\frac{j^2+13j-76}{4}+(2j^2+10j+19)2^{-j}.
\end{aligned}
\]
Consequently, at \(j=m\),
\[
\operatorname{Var}(Q)=\frac{17m}{4}-20+(2m^2+9m+21)2^{-m}-4^{-m}. \tag{3}
\]
Since \(\operatorname{Var}(K)=m/4\), equations (1)--(3) give
\[
\operatorname{Var}(B_n)=m^2\frac m4+\operatorname{Var}(Q)+2m\operatorname{Cov}(K,Q).
\]
Substituting \(m=n-1\) and simplifying gives exactly
\[
\operatorname{Var}(B_n)=\frac{n^3-9n^2+48n-120}{4}+\frac{n^2+3n+17}{2^{n-1}}-\frac{1}{4^{n-1}}.
\]
This proves the claim for every \(n\ge1\).

## Verification
The accompanying `artifacts/verify.py` performs two checks independent of the symbolic simplification above. First, for every binary word of every length \(1\le n\le10\), it constructs the radius-one FLL ball literally by deleting each coordinate and reinserting each binary symbol at every position, deduplicates the outputs, and compares the exact rational mean and variance with the formulas. Second, it iterates the exact moment recurrences through \(m=200\), independently sums the covariance interval formula, and checks the assembled variance identity. Running `python artifacts/verify.py` produces:

`VERIFY_OK direct_binary_words=2046 n<=10 recurrence_m<=200`

These finite checks corroborate the proof; they are not used to infer the all-length theorem.

## Relationship to prior work
Wang and Wang, arXiv:2204.02201, study the size distribution of radius-one fixed-length Levenshtein balls and prove concentration around the mean using Azuma's inequality. Their paper records the exact radius-one ball-size formula in terms of runs and alternating segments and the exact mean. Bar-Lev, Etzion, and Yaakobi, arXiv:2206.07995, determine minimum, maximum, and average radius-one FLL ball sizes. The exact variance formula above is not implied by those extremal/average statements or by an Azuma tail bound; it requires the second-order dependence calculation for alternating-segment statistics.

Searches under exact-variance, second-moment, ball-size-distribution, and synchronization-channel formulations did not identify a published statement of this formula. That negative search is not treated as a proof of novelty; the statement-level comparisons above are the substantive basis for the originality assessment.

## Limitations
The result is restricted to the binary alphabet, a uniformly random center, and radius one. It does not prove a central limit theorem, an exact tail distribution, or a sharp large-deviation principle. The variance gives the exact root-mean-square scale but does not by itself replace concentration inequalities. An unindexed or differently phrased prior derivation remains a residual literature risk.

## References
1. G. Wang and Q. Wang, “On the size distribution of Levenshtein balls with radius one,” arXiv:2204.02201, first public version 2022-04-05.
2. D. Bar-Lev, T. Etzion, and E. Yaakobi, “On the Size of Balls and Anticodes of Small Diameter under the Fixed-Length Levenshtein Metric,” arXiv:2206.07995, 2022.
