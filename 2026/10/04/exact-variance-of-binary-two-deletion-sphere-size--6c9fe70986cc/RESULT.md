# Exact variance of binary two-deletion sphere size
## Finding
For uniformly random \(X\in\{0,1\}^n\) with \(n\ge 2\), let \(\mathcal D_2(X)\) be the set of distinct length-\(n-2\) subsequences obtainable by exactly two deletions, and let \(B_n=|\mathcal D_2(X)|\). Then
\[
\operatorname{Var}(B_n)=\frac{(n-1)(n-2)(2n-3)}{32}.
\]
Consequently
\[
\operatorname{sd}(B_n)=\frac14 n^{3/2}(1+O(n^{-1})).
\]

## Assumptions and scope
The alphabet is binary, the input word is uniform on \(\{0,1\}^n\), and exactly two symbols are deleted. Distinct channel outputs are counted once even if several deletion-position pairs produce the same subsequence. The statement concerns the distribution of the deletion-ball cardinality across centers, not pairwise intersections of deletion balls and not a stochastic channel in which deletion locations are sampled.

For a word \(x\), write \(R(x)\) for its number of runs, \(I(x)\) for the number of singleton runs that are neither the first nor the last run, and \(E(x)\) for the number of singleton endpoint runs. A classical run-length enumeration gives
\[
|\mathcal D_2(x)|=\binom{R(x)+1}{2}-2I(x)-E(x).
\]
This identity is also reconstructed directly below.

## Proof
First, the run-length identity follows by enumerating two deletions. Two deletions assigned to the same run are possible precisely for a run of length at least two. If deletions are assigned to two distinct runs, the only collisions arise when an internal singleton run is deleted together with one of its two neighboring runs: choosing the left neighbor or the right neighbor gives the same descendant. Consecutive singleton runs create chains of exactly these identifications, so each internal singleton removes exactly one nominal choice. Endpoint singleton runs do not create such a two-neighbor identification. Combining the same-run and distinct-run cases yields
\[
|\mathcal D_2(x)|=\binom{R(x)+1}{2}-2I(x)-E(x).
\]
This is the same run enumeration appearing in Swart and Ferreira's Proposition 3.1.

Now assume \(n\ge3\), put \(m=n-1\), and define boundary indicators
\[
Z_i=\mathbf 1\{X_i\ne X_{i+1}\},\qquad 1\le i\le m.
\]
For a uniform binary word, \(Z_1,\ldots,Z_m\) are independent Bernoulli variables with parameter \(1/2\): the map from \((X_1,Z_1,\ldots,Z_m)\) to \(X\) is bijective. We have
\[
R=1+\sum_{i=1}^m Z_i,
\qquad
I=\sum_{i=1}^{m-1}Z_iZ_{i+1},
\qquad
E=Z_1+Z_m.
\]
Substitution into the run formula gives the quadratic polynomial
\[
B_n=1+\sum_{i=1}^m a_iZ_i+\sum_{1\le i<j\le m}c_{ij}Z_iZ_j,
\]
where \(a_1=a_m=1\), \(a_i=2\) for \(1<i<m\), and
\[
c_{ij}=\begin{cases}-1,&j=i+1,\\1,&j\ge i+2.\end{cases}
\]
Let \(\varepsilon_i=2Z_i-1\). These are independent Rademacher variables. In the Walsh expansion of \(B_n\), the coefficient of every linear character \(\varepsilon_i\) is \((m-1)/4\). Indeed, at an endpoint the signed pair-coefficient row sum is \(m-3\), while at an interior index it is \(m-5\); after adding the contribution of \(a_iZ_i\), both cases give \((m-1)/4\). Every quadratic character \(\varepsilon_i\varepsilon_j\) has coefficient \(c_{ij}/4\), hence magnitude \(1/4\). There are no higher-order characters.

Orthogonality of distinct Walsh characters therefore gives
\[
\operatorname{Var}(B_n)
=\frac{m(m-1)^2}{16}+\frac{\binom m2}{16}
=\frac{m(m-1)(2m-1)}{32}
=\frac{(n-1)(n-2)(2n-3)}{32}.
\]
For \(n=2\), every two-deletion ball is the singleton containing the empty word, so the same formula gives variance zero.

As a consistency check, double-counting pairs \((x,y)\) with \(y\in\mathcal D_2(x)\) gives
\[
\mathbb E B_n=\frac{n^2+n+2}{8}.
\]
Indeed, every binary word of length \(n-2\) has exactly \(1+n+\binom n2\) distinct length-\(n\) supersequences obtained by two insertions. The variance formula then implies the stated standard-deviation asymptotic.

## Verification
The bundled `verify.py` constructs every distinct two-deletion descendant directly for every binary word with \(2\le n\le12\). It independently computes run statistics, checks the run-length formula word by word, and compares the exact empirical first and second moments with
\[
\mathbb E B_n=\frac{n^2+n+2}{8}
\quad\text{and}\quad
\operatorname{Var}(B_n)=\frac{(n-1)(n-2)(2n-3)}{32}.
\]
It also checks the closed Walsh-variance simplification arithmetically for \(3\le n\le200\). These finite checks corroborate the all-\(n\) proof; they are not used to infer it.

## Relationship to prior work
Pham, Goyal, and Kiah define the binary deletion ball \(\mathcal D_t(x)\) and use its extremal cardinality as a basic parameter in sequence reconstruction. Their work concerns worst-case intersections and extremal sizes, not the variance of \(|\mathcal D_2(X)|\) over a random center. Their first public version appeared on 2021-11-08 and is classified MSC 94B99.

Swart and Ferreira give the exact per-word run-length formula for the number of distinct subsequences after two deletions. That formula supplies the structural starting point used here, but their paper does not state a variance calculation. The present result turns that deterministic run statistic into an exact second moment by exploiting the independent boundary representation of a uniform binary word.

Alon, Bourla, Graham, He, and Kravitz emphasize that deletion graphs are highly nonregular, which makes local structure relevant in deletion coding. The variance here quantifies one natural source of this nonregularity at deletion radius two: the fluctuation of the number of distinct length-\(n-2\) descendants.

## Limitations
No claim is made for nonbinary alphabets, for three or more deletions, for deletion-ball intersections, or for the full distribution beyond its variance. The proof relies essentially on the independence of binary boundary indicators under the uniform measure. The originality search cannot exclude an unindexed or differently phrased prior derivation of the same second moment.

## References
1. V. L. P. Pham, K. Goyal, and H. M. Kiah, “Sequence Reconstruction Problem for Deletion Channels: A Complete Asymptotic Solution,” arXiv:2111.04255, first posted 2021-11-08.
2. T. G. Swart and H. C. Ferreira, “A note on double insertion/deletion correcting codes,” IEEE Transactions on Information Theory 49(1), 269–273, DOI 10.1109/TIT.2002.806155.
3. N. Alon, G. Bourla, B. Graham, X. He, and N. Kravitz, “Logarithmically larger deletion codes of all distances,” arXiv:2209.11882, first posted 2022-09-23.
