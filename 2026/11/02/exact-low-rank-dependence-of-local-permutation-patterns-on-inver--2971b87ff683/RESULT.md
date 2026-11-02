# Exact low-rank dependence of local permutation patterns on inverse descents

## Finding

Let \(\pi\) be a uniformly random permutation of \(\{1,\ldots,n\}\). Fix integers \(2\le k\le n\), a window \(1\le i\le n-k+1\), and a permutation pattern \(\sigma\in S_k\). Define \(A_{i,\sigma}\) to indicate that \((\pi(i),\ldots,\pi(i+k-1))\) has relative rank pattern \(\sigma\). For \(1\le j<n\), let \(D_j=\mathbf 1\{\pi^{-1}(j)>\pi^{-1}(j+1)\}\), the inverse-descent indicator at *value* \(j\). Write

\[
\epsilon_r(\sigma)=
\begin{cases}
+1,&\sigma^{-1}(r)>\sigma^{-1}(r+1),\\
-1,&\sigma^{-1}(r)<\sigma^{-1}(r+1),
\end{cases}
\qquad 1\le r<k.
\]

**Exact covariance theorem.** For every stated \(n,k,i,\sigma,j\),

\[
\boxed{
\operatorname{Cov}(A_{i,\sigma},D_j)
=\frac{1}{2k!\binom nk}
\sum_{r=1}^{k-1}\epsilon_r(\sigma)
\binom{j-1}{r-1}\binom{n-j-1}{k-r-1}.}
\tag{1}
\]

Binomial coefficients with inadmissible lower index are zero. The covariance is *independent of the window start* \(i\).

**Exact rank and classification theorem.** For each fixed \(n\ge k\ge2\), let \(C_{n,k}\) be the \(k!\)-by-\((n-1)\) matrix with rows indexed by patterns \(\sigma\in S_k\), columns by values \(j\), and entries from (1). Then

\[
\boxed{\operatorname{rank} C_{n,k}=k-1.}
\tag{2}
\]

Two patterns give identical complete covariance profiles across all \(j\) if and only if their *inverse descent sets* coincide. There are therefore exactly \(2^{k-1}\) distinct profiles, irrespective of \(n\ge k\).

**Fixed-pattern scaling.** For fixed \(k\), if \(j/n\to x\in(0,1)\), then

\[
\boxed{
 n^2\operatorname{Cov}(A_{i,\sigma},D_j)
\longrightarrow
\frac{1}{2(k-2)!}\sum_{r=1}^{k-1}\epsilon_r(\sigma)
\binom{k-2}{r-1}x^{r-1}(1-x)^{k-r-1}.}
\tag{3}
\]

The limit is a signed Bernstein polynomial, exhibiting the inverse descent signature directly. For length three, \(\sigma=132\) and \(\sigma=231\) produce opposite affine profiles \((2j-n)/(2n(n-1)(n-2))\) and \((n-2j)/(2n(n-1)(n-2))\). Their sum is zero: a peak at any fixed interior position is uncorrelated with each individual inverse descent, although that does not imply independence.

## Assumptions and scope

Every permutation has probability \(1/n!\). The reduced pattern \(\sigma\) records *within-window ranks*, not values or positions outside the window; the inverse-descent index \(j\) refers to a pair of consecutive *values*. All claims concern exact finite-sample covariances under the uniform model, with integer \(n,k,i,j\) in the quantified ranges. The rank is over the real numbers; no claim is made about independence of the full indicator vectors or about nonuniform permutation distributions.

## Proof

First, \(\mathbb P(A_{i,\sigma})=1/k!\) and \(\mathbb P(D_j)=1/2\). Let \(T_j\) swap the labels \(j\) and \(j+1\) everywhere in \(\pi\). This is a probability-preserving involution, and \(D_j(T_j\pi)=1-D_j(\pi)\). If the window contains at most one of the two adjacent numerical labels, its reduced pattern does not change under \(T_j\): no other value can lie strictly between these two values. Thus, on that invariant subset, the expectation of \(A_{i,\sigma}(D_j-1/2)\) vanishes.

If both labels occur in the window, they necessarily occupy consecutive *within-window ranks* \(r,r+1\), for some \(1\le r<k\). Exactly \(r-1\) of the other selected labels must lie below \(j\), chosen from \(j-1\) possibilities, and \(k-r-1\) lie above \(j+1\), chosen from \(n-j-1\) possibilities. There are consequently \(\binom{j-1}{r-1}\binom{n-j-1}{k-r-1}\) eligible unordered window value sets. Every set of \(k\) values is equally likely and, conditionally on that set, every order is equally likely. Hence the joint probability of \(A_{i,\sigma}\), both labels in the window, and these ranks equals the count divided by \(k!\binom nk\). On this event, \(D_j-1/2=\epsilon_r(\sigma)/2\). Summing proves (1), including all boundary indices.

For (2), factor the covariance matrix as \(C_{n,k}=EK/(2k!\binom nk)\), where \(E_{\sigma,r}=\epsilon_r(\sigma)\) and \(K_{r,j}=\binom{j-1}{r-1}\binom{n-j-1}{k-r-1}\). For \(1\le r,j<k\), \(K_{r,j}=0\) if \(j<r\), while \(K_{r,r}=\binom{n-r-1}{k-r-1}>0\); thus the first \(k-1\) columns form a nonsingular triangular matrix and \(K\) has full row rank. The identity permutation has signature \((-1,\ldots,-1)\), and swapping adjacent *values* \(r,r+1\) in that permutation changes only signature coordinate \(r\) to \(+1\). Differences of these \(k-1\) signature rows span \(\mathbb R^{k-1}\), so \(E\) has full column rank. Consequently their product has rank \(k-1\). As \(K\) has full row rank, equality of two profiles is equivalent to equality of their signatures. Every sign pattern occurs as the inverse descent set of some permutation (any descent set can be realized by a permutation), giving exactly \(2^{k-1}\) distinct profiles.

Finally, for fixed \(k\), insert \(j/n\to x\) into (1) and use \(\binom{n}{k}k!\sim n^k\) and the fixed-degree binomial asymptotics. This yields (3). Taking the two peak patterns \(132,231\) in (1) gives the displayed cancellation.

## Verification

The standalone program `verify.py` independently enumerates all uniform permutations through \(n=8\), all window starts, every pattern length \(2\le k\le\min(5,n)\), every pattern, and every inverse-descent value index, comparing the empirical integer covariance numerator against (1). It also checks the signature count, the nonzero triangular minor, equality and distinctness of signature profiles in additional cases, and the peak cancellation through \(n=69\). Execution completed with **20,321 exact assertions**, including **10,192 direct covariance comparisons**. The all-size conclusions follow from the preceding proof, not finite enumeration.

Reproduce with `python3 verify.py` using only the standard Python library.

## Relationship to prior work

Petersen (2012) studies global two-sided Eulerian distributions of descents and inverse descents. Elizalde (2015) surveys consecutive pattern occurrences, while Crane and DeSalvo (2015) give probabilistic approximations for pattern counts. Gessel and Zhuang (2023) derive aggregate joint distributions of peaks and inverse descents and more general two-sided *descent statistics*. None of the inspected relevant material supplies the fixed-window, fixed-value formula (1), rank theorem (2), or the inverse-descent-signature profile classification.

The distinction from aggregate descent-class distributions is substantive. The permutations \(1324\) and \(3412\) have identical descent sets for themselves and their inverses (both equal to \(\{2\}\)), but their first three entries have reduced patterns \(132\) and \(231\). Hence the two-sided descent-class data alone do not determine the individual local-pattern indicators. The result is a local mixed-covariance refinement, not a new formula for existing two-sided Eulerian polynomials. This comparison supports best-knowledge originality, not a claim of exhaustive historical priority.

## Limitations

The result is for uniform permutations; the transposition symmetry fails for generic nonuniform laws. It determines pairwise cross-covariances, not the full joint distribution or higher cumulants, and does not prove independent behavior. The Bernstein statement has fixed \(k\) and interior limiting value fraction. Literature searches and full-text comparisons cannot rule out every earlier specialized result or an obscure equivalent identity; independent historical review remains outstanding.

## References

- T. K. Petersen, *Two-sided Eulerian numbers via balls in boxes*, arXiv:1209.6273, first posted 2012-09-27. https://arxiv.org/abs/1209.6273
- S. Elizalde, *A survey of consecutive patterns in permutations*, arXiv:1504.07265, first posted 2015-04-27. https://arxiv.org/abs/1504.07265
- H. Crane and S. DeSalvo, *Pattern Avoidance for Random Permutations*, arXiv:1509.07941, first posted 2015-09-26. https://arxiv.org/abs/1509.07941
- I. M. Gessel and Y. Zhuang, *Two-sided permutation statistics via symmetric functions*, arXiv:2306.15785, first posted 2023-06-27. https://arxiv.org/abs/2306.15785
