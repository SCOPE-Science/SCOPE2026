# A Stirling law for complete bivariate-record kills and the sharp fixed-k error constant
## Finding
For independent bivariate observations with continuous independent coordinates, adopt the record-small convention. Let \(r_{n-1}\) be the number of current Pareto records after the first \(n-1\) observations, let \(K_n\) be the number of current records killed by observation \(n\), and put
\[
C_{n,k}=\Pr\{r_{n-1}=k,\ K_n=k\}.
\]
For every integer \(n\ge2\) and \(1\le k\le n-1\),
\[
C_{n,k}=rac{\left[{n-1top k}ight]}{n^2 (n-1)!},
\]
where \(\left[{mtop k}ight]\) denotes the unsigned Stirling number of the first kind. Equivalently, conditional on the event that the \(n\)th observation kills every current record, the random variable \(r_{n-1}\) has the cycle-count distribution of a uniform permutation of \(n-1\) elements.

If
\[
A_{n,k}=2^{-(k+1)}n^{-1}H_n-(k-1)2^{-(k+2)}n^{-1}
\]
is the approximation from Theorem 3.9 of Fill, then for each fixed integer \(k\ge1\),
\[
\Pr\{K_n=k\}-A_{n,k}
\sim rac{1}{4(k-1)!}\,n^{-3}(\log n)^{k-1}.
\]
Thus the fixed-\(k\) sharp error-rate conjecture in Remark 3.11(b) holds, with the leading constant made explicit.

## Assumptions and scope
The observations are iid bivariate vectors with independent continuous coordinates. Coordinatewise monotone transformations reduce the model to iid uniform points in \((0,1)^2\), exactly the model used in the motivating source. The statement uses record-small values: a current record is a Pareto minimum. The exact formula is finite-sample and valid for all \(n\ge2\) and \(1\le k\le n-1\). The asymptotic statement keeps \(k\) fixed while \(n	o\infty\); it does not assert a uniform approximation when \(k\) grows with \(n\).

## Proof
Let \(E_n\) be the event that observation \(n\) kills every current record. Fill's Lemma 3.6 identifies
\[
E_n=\{X^{(n)}\prec X^{(i)}	ext{ for every }1\le i<n\},
\qquad \Pr(E_n)=n^{-2},
\]
and
\[
C_{n,k}=\Pr\{r_{n-1}=k,E_n\}.
\]
The two coordinate-rank permutations of the \(n\) labeled observations are independent and uniform. Conditioning on \(E_n\) merely fixes label \(n\) to have rank one in both coordinates. The relative coordinate ranks of labels \(1,\ldots,n-1\) therefore remain two independent uniform permutations. Ordering these \(n-1\) observations by increasing first coordinate, their second-coordinate ranks form a uniform permutation \(\pi\) of \(m=n-1\) symbols.

A point is a current Pareto minimum exactly when its second-coordinate rank is a new left-to-right minimum of \(\pi\). For \(j=1,\ldots,m\), the relative rank of \(\pi_j\) among \(\pi_1,\ldots,\pi_j\) is independent and uniform on \(\{1,\ldots,j\}\). Hence the record-minimum indicators are independent Bernoulli variables with success probabilities \(1/j\), and the probability generating function of their sum \(R_m\) is
\[
\mathbb E z^{R_m}
=\prod_{j=1}^m\left(1-rac1j+rac zjight)
=rac{z(z+1)\cdots(z+m-1)}{m!}
=\sum_{k=1}^mrac{\left[{mtop k}ight]}{m!}z^k.
\]
Therefore \(\Pr\{r_{n-1}=k\mid E_n\}=\left[{n-1top k}ight]/(n-1)!\). Multiplying by \(\Pr(E_n)=n^{-2}\) proves the exact formula.

For fixed \(k\), factor the generating polynomial as
\[
rac{z(z+1)\cdots(z+n-2)}{(n-1)!}
=rac z{n-1}\prod_{j=1}^{n-2}\left(1+rac zjight).
\]
Thus
\[
C_{n,k}=rac{1}{n^2(n-1)}
e_{k-1}\left(1,rac12,\ldots,rac1{n-2}ight),
\]
where \(e_r\) is the elementary symmetric polynomial. For fixed \(r\), expanding \(H_{n-2}^r\) into ordered index tuples shows
\[
e_r\left(1,rac12,\ldots,rac1{n-2}ight)
=rac{H_{n-2}^r}{r!}+O\left(H_{n-2}^{r-2}ight)
\]
for \(r\ge2\), while the cases \(r=0,1\) are exact. Since \(H_{n-2}\sim\log n\),
\[
C_{n,k}\sim rac{n^{-3}(\log n)^{k-1}}{(k-1)!}.
\]
For fixed \(k\), Theorem 3.9 gives, once \(n\ge k+3\),
\[
\Pr\{K_n=k\}-A_{n,k}
=rac14 C_{n,k}+
\sum_{j=1}^{k-1}c_{k-j}C_{n,j},
\]
where the coefficients \(c_{k-j}\) are fixed and bounded. Because \(C_{n,j}/C_{n,k}	o0\) for every fixed \(j<k\), the sum is \(o(C_{n,k})\). The asserted asymptotic follows.

## Verification
The finite-sample identity reproduces every entry of the \(C\)-matrix displayed in Example 3.10 of the motivating paper. In particular, for \(n=5\) the unsigned Stirling row \((6,11,6,1)\), divided by \(5^2\,4!=600\), gives \((1/100,11/600,1/100,1/600)\), exactly the published row. The accompanying `verify.py` independently generates unsigned Stirling rows from their recurrence, checks normalization, the source's formulas for \(C_1\), \(C_2\), and \(C_{n-1}\), and the displayed small-\(n\) rows. These finite checks support the algebra but are not used as proof of the infinite statements.

## Relationship to prior work
Fill's 2019 preprint, later published as *Breaking bivariate records*, defines the same \(C_k\), proves \(C_k=\Pr\{r_{n-1}=k,K_n=r_{n-1}\}\), and shows that the total complete-kill probability is \(n^{-2}\). It gives a finite-sum expression and the special cases \(C_1\), \(C_2\), and \(C_{n-1}\), but does not identify the full row with Stirling cycle numbers. Remark 3.11(b) explicitly conjectures the fixed-\(k\) rate \(\Theta(n^{-3}(\log n)^{k-1})\) and the leading \(-C_k/4\) error when the approximation is written as approximation minus probability. The exact Stirling law above supplies the missing asymptotic of \(C_k\) and therefore resolves that fixed-\(k\) conjecture.

The classical fact that the number of one-dimensional records in a random permutation has an unsigned-Stirling distribution is not new; here it becomes relevant because the complete-kill event is independent of the relative rank permutation of the first \(n-1\) observations. Fill's later *Breaking multivariate records* studies the limiting broken-record law in arbitrary dimension and recovers the bivariate geometric limit, but it does not state this finite-sample complete-kill law or the fixed-\(k\) remainder asymptotic.

## Limitations
The result concerns the bivariate independent-coordinate model and the complete-kill component \(C_{n,k}\). It does not resolve the uniform-in-\(k\) error rate also suggested in Remark 3.11(b), nor the empirical-frequency conjectures in Section 4 of the motivating paper. The originality search found no covering statement, but an equivalent observation could exist under the language of planar maxima or permutation records and remain poorly indexed.

## References
1. J. A. Fill, *Breaking Bivariate Records*, arXiv:1901.08232v1 (2019); Combinatorics, Probability and Computing 30 (2021), 105--123, DOI: 10.1017/S0963548320000309.
2. J. A. Fill, *Breaking Multivariate Records*, arXiv:2109.14846 (2021); Electronic Journal of Probability 28 (2023), DOI: 10.1214/23-EJP968.
3. B. C. Arnold, N. Balakrishnan, and H. N. Nagaraja, *Records*, Wiley, 1998; anniversary edition, 2012.
