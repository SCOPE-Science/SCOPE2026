# A first-order lattice phase for the largest block of a near-diagonal random set partition

## Finding
Let \(\Pi_{n,r}\) be a uniformly random partition of \(\{1,\ldots,n\}\) into exactly \(n-r\) nonempty blocks, and let \(M_{n,r}\) be its largest block size. Put \(u=r^2/n\), \(\lambda=2u/3\). As \(n\to\infty\) along any integer sequence with \(r\to\infty\) and \(u\) confined to a compact subinterval of \((0,\infty)\),
\[
 \Pr(M_{n,r}=2)=e^{-2u/3}\left[1+\frac{2u/3-7u^2/9}{r}+o\!\left(\frac1r\right)\right].
\]
The remainder is uniform when \(u\) varies in a prescribed compact subset of \((0,\infty)\). For fixed \(t>0\), setting \(r=\lfloor t\sqrt n\rfloor\) and \(\delta_n=\{t\sqrt n\}\) therefore gives the finer lattice-phase law
\[
 r\left[\Pr(M_{n,r}=2)-e^{-2t^2/3}\right]
 =e^{-2t^2/3}\left(\frac{2t^2}{3}-\frac{7t^4}{9}+\frac{4t^2}{3}\delta_n\right)+o(1).
\]
In particular, this rescaled difference need not converge. At \(t=1\), along \(n=m^2\) it converges to \(-e^{-2/3}/9\), while along \(n=m^2+2m\) it converges to \(11e^{-2/3}/9\). Thus the single nonoscillatory coefficient posited for the set-partition case in Conjecture 3.7 of Arratia and DeSalvo (2016) does not exist. In fact, as the phase \(\delta_n\) ranges over subsequential limits in \([0,1]\), the coefficient fills the corresponding nondegenerate closed interval.

## Assumptions and scope
Here \(n,r\) are integers, \(r\ge1\), \(2r\le n\); the asymptotic statements also require \(r\to\infty\) and \(0<c\le r^2/n\le C<\infty\) for fixed constants \(c,C\). The event \(M_{n,r}=2\) means every block has size one or two, and at least one block is a pair. \(S(n,n-r)\) denotes a Stirling number of the second kind. The displayed phase law has fixed \(t>0\). The claim is about set partitions, not permutations or arbitrary weighted combinatorial assemblies.

## Proof
**1. Exact profile ratios.** Let \(c_j\) count blocks of size \(j\). Set \(s=\sum_{j\ge3}(j-1)c_j\) and \(h=\sum_{j\ge3}(j-2)c_j\). The constraints force \(c_2=r-s\) and \(c_1=n-2r+h\). For a feasible profile its number of labeled set partitions equals \(n!/\prod_j(c_j!(j!)^{c_j})\). The all-singleton-and-pair count is
\[
W_0=\frac{n!}{(n-2r)!\,r!\,2^r}.
\]
Using the falling factorial \((r)_{\underline s}=r(r-1)\cdots(r-s+1)\) and rising factorial \((N)^{\overline h}=N(N+1)\cdots(N+h-1)\), direct cancellation gives the exact ratio
\[
 \frac{W(\mathbf c)}{W_0}=\frac{(r)_{\underline s}}{(n-2r+1)^{\overline h}}\prod_{j\ge3}\frac{(2^{j-1}/j!)^{c_j}}{c_j!}.
\]
In particular \(\Pr(M_{n,r}=2)=W_0/S(n,n-r)\).

**2. Tripleton contribution.** For exactly \(j\) tripletons and no larger blocks the ratio is
\[
 q_j=\frac{(2/3)^j(r)_{\underline{2j}}}{j!\,(n-2r+1)^{\overline j}}
 =\frac{\lambda^j}{j!}\left[1+\frac{2ju-j(2j-1)}r+O\!\left(\frac{(1+j)^4}{r^2}\right)\right]
\]
for \(j\) bounded or at most a fixed multiple of \(\log r\), with uniform bounds on compact \(u\)-ranges. Terms with \(2j>r\) vanish. Summing against the Poisson weights, since \(\sum_j j\lambda^j/j!=\lambda e^\lambda\) and \(\sum_j j^2\lambda^j/j!=(\lambda^2+\lambda)e^\lambda\), yields
\[
 \sum_jq_j=e^\lambda\left[1+\frac{2u\lambda-2\lambda^2-\lambda}{r}+o(1/r)\right].
\]
To justify interchange uniformly, \(q_j\le a_3^j/j!\) with \(a_3=2r^2/[3(n-2r+1)]\) bounded. Truncating at \(j\le B\log r\) with sufficiently large fixed \(B\) leaves a Poisson tail \(o(r^{-2})\); on the truncated range the displayed Taylor error is \(O((\log r)^4/r^2)\) after summation.

**3. Four-block contribution and higher-block remainder.** A profile with one four-block and \(j\) tripletons, and otherwise just pairs and singletons, has ratio
\[
 q_{j,4}=\frac{(2/3)^j(r)_{\underline{2j+3}}}{3j!\,(n-2r+1)^{\overline{j+2}}}
 =\frac{\lambda^j}{j!}\left[\frac{u^2}{3r}+o(1/r)\right]
\]
for each fixed \(j\); the sum of these contributions is \(e^\lambda u^2/(3r)+o(1/r)\). Indeed \(q_{j,4}/q_j\le r^3/[3(n-2r+1)^2]=O(1/r)\), which gives dominated convergence in the sum.

For a general profile, the ratio in step 1 is bounded termwise by independent exponential-series weights \(a_j^{c_j}/c_j!\), where
\[
 a_j=\frac{2^{j-1}r^{j-1}}{j!(n-2r+1)^{j-2}},\qquad j\ge3.
\]
Here \(a_3=O(1)\), \(a_4=O(1/r)\), and \(\sum_{j\ge5}a_j=O(1/r^2)\), because \(a_{j+1}/a_j=2r/[(j+1)(n-2r+1)]=O(1/r)\). Therefore profiles with a block of size at least five or at least two four-blocks contribute \(O(1/r^2)W_0\) in total. Collecting the three categories,
\[
 \frac{S(n,n-r)}{W_0}=e^\lambda\left[1+\frac{2u\lambda-2\lambda^2-\lambda+u^2/3}{r}+o(1/r)\right].
\]
Taking its reciprocal and using \(\lambda=2u/3\) proves the first display in **Finding**.

**4. Floor phase and failure of a single coefficient.** Write \(r=t\sqrt n-\delta_n\) with \(0\le\delta_n<1\). Then
\[
 r\left(\frac{r^2}{n}-t^2\right)=-2t^2\delta_n+o(1).
\]
Expanding \(e^{-2u/3}\) about \(u=t^2\) and inserting the proved first-order formula establishes the phase law. For \(n=m^2\) with \(t=1\), \(\delta_n=0\); for \(n=m^2+2m\), \(r=m\) and \(\delta_n\to1\), yielding the two distinct limits. For general \(t\) and \(\theta\in(0,1)\), choose integers \(n\) nearest \(((m+\theta)/t)^2\); then \(\{t\sqrt n\}\to\theta\), and endpoint phases follow by one-sided choices. This proves the asserted continuum of subsequential coefficients.

## Verification
Run `python3 verify.py` with Python 3 and no external packages. The script independently evaluates exact near-diagonal Stirling recurrences and fully enumerates feasible block profiles for small \(n,r\), checks the exact pair-only and single-tripleton counts, and uses 75-digit arithmetic to compare the two subsequences against their different predicted limits and the moving-parameter first-order expansion. It reports 96 successful assertions. Finite checks do not establish the uniform asymptotic remainders; the profile bounds in the proof do.

## Relationship to prior work
Arratia and DeSalvo (2016), arXiv:1606.04642, Theorem 3.3, prove the leading Poisson behavior of tripleton blocks in fixed-block set partitions and the limiting \(e^{-2t^2/3}\) probability for largest block size two. Their Conjectures 3.7 and 3.8 seek one fixed first-order coefficient for \(r=\lfloor t\sqrt n\rfloor\). The result here evaluates that coefficient with the moving parameter \(r^2/n\), including the four-block contribution, and shows that the stipulated fixed-\(t\) coefficient cannot exist: the floor phase survives exactly at the conjectured order. Their subsequent paper *Attacks and alignments: rooks, set partitions, and permutations* (arXiv:1807.03926, Theorem 1.2) gives a component-profile total-variation bound of order \(r^3/n^2\); it does not give this first-order phase coefficient. The basic Stirling recurrence and block-profile counting are classical and not asserted to be novel.

## Limitations
The expansion is proved only for ordinary, uniformly random set partitions with \(r^2/n\) bounded away from both zero and infinity; it does not treat arbitrary assemblies or a growing-unbounded \(u\). The claimed absence of a fixed coefficient is for the precise floor parametrization stated in the cited conjecture. No claim of independent validation or comprehensive historical-priority certification is made. Other near-diagonal Stirling expansions may imply this result after algebra not identified in the inspected sources.

## References
1. R. Arratia and S. DeSalvo, *Poisson and independent process approximation for random combinatorial structures with a given number of components, and near-universal behavior for low rank assemblies*, arXiv:1606.04642 (first publicly posted 2016-06-15), especially Theorem 3.3, Conjectures 3.7–3.8, and Remark 3.10. https://arxiv.org/html/1606.04642v2
2. R. Arratia and S. DeSalvo, *Attacks and alignments: rooks, set partitions, and permutations*, arXiv:1807.03926, Theorem 1.2. https://arxiv.org/pdf/1807.03926
3. R. Arratia and S. DeSalvo, *Completely effective error bounds for Stirling numbers of the first and second kind via Poisson approximation*, arXiv:1404.3007. https://arxiv.org/abs/1404.3007
