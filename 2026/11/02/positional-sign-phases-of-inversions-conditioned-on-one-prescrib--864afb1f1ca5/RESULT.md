# Positional sign phases of inversions conditioned on one prescribed two-cycle

## Finding
Let \(n\geq3\), let \(\Pi\) be uniform on the symmetric group \(S_n\), and write
\[
I(\Pi)=\sum_{1\leq a<b\leq n}\mathbf 1\{\Pi(a)>\Pi(b)\}.
\]
For \(1\leq i<j\leq n\), let \(T_{ij}=\mathbf 1\{\Pi(i)=j,\ \Pi(j)=i\}\): the indicated two labels form a disjoint two-cycle, regardless of all other cycles. Put
\[
\Delta_{n,i,j}=\mathbb E[I(\Pi)\mid T_{ij}=1]-\mathbb E I(\Pi).
\]
**Theorem (labeled two-cycle positional profile).** For all these parameters,
\[
\boxed{\Delta_{n,i,j}=\frac12+\frac{(j-i-1)^2-(i+j-n-1)^2}{n-2}
=\frac12+\frac{(n-2i)(2j-n-2)}{n-2}.}
\]
Consequently,
\[
\operatorname{Cov}(I(\Pi),T_{ij})
=\frac{\Delta_{n,i,j}}{n(n-1)}.
\]
The exact sign is the sign of \(n-2+2(n-2i)(2j-n-2)\), including the zero case. If \(i/n\to u\) and \(j/n\to v\), with \(0\leq u<v\leq1\), then
\[
\lim_{n\to\infty}\frac{\Delta_{n,i,j}}n=(1-2u)(2v-1).
\]
Thus, away from the midpoint boundaries, a prescribed two-cycle *increases* expected inversions if and only if its two labels straddle the midpoint, and *decreases* them if both lie on the same side. The fraction of pairs \((i,j)\), \(i<j\), having positive \(\Delta_{n,i,j}\) tends to \(1/2\).

For comparison, the local effects cancel almost completely when summed over all pairs: if \(C_2=\sum_{i<j}T_{ij}\) counts two-cycles, then
\[
\operatorname{Cov}(I(\Pi),C_2)=\frac1{12}\qquad(n\ge3).
\]
This aggregate identity is included as a check, **not** as a claim of historical originality; it follows from known conjugacy-class expectations.

## Assumptions and scope
The permutation is sampled uniformly from all \(n!\) permutations of the **labeled** set \(\{1,\ldots,n\}\). A two-cycle means \(\Pi(i)=j\) and \(\Pi(j)=i\), not merely that the pair occurs consecutively in one-line notation. Conditioning on \(T_{ij}=1\) has positive probability \(1/[n(n-1)]\), and the restriction of \(\Pi\) to the other \(n-2\) labels is a uniform permutation of that set. All finite equations hold at \(n=3\). The macroscopic sign assertion excludes the boundary \(u=1/2\) or \(v=1/2\), where the finite exact formula, not the limiting sign, must be used.

## Proof
Write \(x=i-1\), \(y=j-i-1\), \(z=n-j\), and \(d=x+y+z=n-2\). The values and positions outside \(\{i,j\}\) are the same \(d\)-element set. Conditional on \(T_{ij}=1\), comparisons between two such positions contribute \(\binom d2/2\) in expectation, and comparison of positions \(i,j\) contributes exactly one.

For each other position \(k\), the corresponding image is uniform on the \(d\) available labels. Enumerate the inversions involving position \(i\) or position \(j\), grouping \(k\) as \(k<i\), \(i<k<j\), or \(k>j\). The respective *sum of the two inversion probabilities* is
\[
\frac{y+2z}{d},\qquad\frac{d+y}{d},\qquad\frac{2x+y}{d}.
\]
There are respectively \(x,y,z\) such positions. Therefore
\[
\mathbb E[I\mid T_{ij}=1]=
1+\frac{d(d-1)}4+
\frac{x(y+2z)+y(d+y)+z(2x+y)}d.
\]
Since \(\mathbb EI=n(n-1)/4\), elementary expansion gives
\[
\Delta_{n,i,j}=\frac12+\frac{y^2-(x-z)^2}{d}.
\]
Substituting \(y=j-i-1\), \(x-z=i+j-n-1\) and factoring the difference of squares proves the two displayed exact expressions. Also \(\mathbb P(T_{ij}=1)=(n-2)!/n!=1/[n(n-1)]\), so the covariance identity follows directly.

For the asymptotic profile, divide the factored expression by \(n\) and take the indicated limits. Its product is positive on the open region \(u<1/2<v\) and negative on either open same-side region. The boundaries have planar measure zero in \(0<u<v<1\). Riemann-sum counting therefore shows that the proportion of positive pairs tends to the area ratio
\[
\frac{(1/2)(1/2)}{1/2}=\frac12.
\]
For the aggregate check, direct summation of the factored formula yields
\[
\sum_{i<j}(n-2i)(2j-n-2)
=\sum_{j=2}^n (j-1)(n-j)(2j-n-2)
=-\frac{n(n-1)(n-2)}6.
\]
Consequently \(\sum_{i<j}\Delta_{n,i,j}=n(n-1)/12\). Summing the local covariances proves the stated aggregate identity.

## Verification
The accompanying standard-library script `verify.py` independently evaluates every conditional permutation for all \(3\leq n\leq8\) and all \(i<j\). It separately reconstructs expectations from individual pair-marginal probabilities, checks the exact covariance normalizations, verifies the aggregate identity through \(n=150\), and checks finite sign proportions at several large sizes. Execute `python3 verify.py`. A successful run prints `PASS 405 independent exact and sign checks`.

These computations check finite cases only; the all-size conclusions rest on the combinatorial calculation and the algebraic/Riemann-sum arguments above.

## Relationship to prior work
The cycle-statistics framework of Maples, Nikeghbali and Zeindler (2012) provides a probabilistic setting for uniform random permutations and cycle counts. Hultman (2013), especially Lemma 6.1 and Theorem 6.2, derives expected inversions when averaged over a whole conjugacy class, with dependency on the numbers of fixed points and two-cycles. These averages already imply the displayed *aggregate* covariance, and are not claimed as new.

The object here is different: condition on one **specified labeled pair** being a two-cycle, not on a conjugacy class or its cycle-count totals. The resulting exact positional saddle and its midpoint sign diagram are not determined by the class average alone. Pinsky (2025) studies inversions conditioned on a prescribed *number* of fixed points and certain inversion-pair probabilities; these also do not impose a specified labeled two-cycle. Closest available research-record summaries concern covariance with the *total* cycle count or precision of pairwise inversion indicators, different random variables. Historical completeness is not guaranteed.

## Limitations
No independence is inferred from zero or small covariances. The limiting sign theorem does not determine the sign of sequences approaching the midpoint boundary; the finite expression does. The analysis is for a *uniform* labeled permutation, not Ewens-weighted laws, prescribed conjugacy classes, or permutations with two-cycles constrained by additional events. The claim has self-review only and no independent audit. Discovery priority outside the searched sources remains uncertain.

## References
- K. Maples, A. Nikeghbali and D. Zeindler, *On the number of cycles in a random permutation*, arXiv:1203.4132, first public version 2012-03-19, https://arxiv.org/abs/1203.4132.
- A. Hultman, *Permutation statistics of products of random permutations*, arXiv:1301.0430v1, first public version 2013-01-03, Section 6, https://arxiv.org/html/1301.0430v1.
- R. G. Pinsky, *The inversion statistic in derangements and in other permutations with a prescribed number of fixed points*, arXiv:2505.02058, first public version 2025-05-04, https://arxiv.org/abs/2505.02058.
