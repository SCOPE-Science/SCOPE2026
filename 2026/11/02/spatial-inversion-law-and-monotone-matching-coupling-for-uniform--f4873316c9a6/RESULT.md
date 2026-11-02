# Spatial inversion law and monotone matching coupling for uniform involutions

## Finding

For integers \(n\ge 2\) and \(0\le k\le\lfloor n/2\rfloor\), let \(\Pi_{n,k}\) be uniformly distributed over involutions of \([n]=\{1,\ldots,n\}\) having exactly \(k\) two-cycles. Define the inversion count
\[
I(\pi)=\sum_{1\le a<b\le n}\mathbf 1\{\pi(a)>\pi(b)\}.
\]

**Spatial inversion profile.** For \(n\ge3\), any \(1\le a<b\le n\), and \(d=b-a\),
\[
\boxed{\Pr\{\Pi_{n,k}(a)>\Pi_{n,k}(b)\}
=\frac{2k^2}{n(n-1)}
+\frac{2k(n-2k)(n-d-1)}{n(n-1)(n-2)}.}
\tag{1}
\]
The probability depends on the positions only through their gap \(d\). At fixed \(n,k\), it decreases across successive gaps by exactly
\[
\frac{2k(n-2k)}{n(n-1)(n-2)}.
\]
This decrease is strict precisely when \(0<k<n/2\); when all positions are fixed or, for even \(n\), all positions are moved, the profile is constant. For every admissible gap, the probability is strictly increasing in \(k\) along \(k=0,\ldots,\lfloor n/2\rfloor\). For \(n=2\), the only inversion probability is \(k\in\{0,1\}\).

**Distributional transposition filtration.** All the \(\Pi_{n,k}\) can be coupled so that each marginal is uniform on its prescribed class and
\[
I(\Pi_{n,k+1})-I(\Pi_{n,k})
=1+2\#\{t:a<t<b,\ a<\Pi_{n,k}(t)<b\}\ge1
\tag{2}
\]
when the transition pairs two previously fixed positions \(a<b\). In particular, for every strictly increasing function \(h\) on the finite integer range of inversions,
\[
\mathbb E\,h(I(\Pi_{n,k+1}))>
\mathbb E\,h(I(\Pi_{n,k})).
\tag{3}
\]
If \(K\) has any non-degenerate distribution on \(\{0,\ldots,\lfloor n/2\rfloor\}\), and an involution is conditionally uniform given its number \(K\) of two-cycles, then
\[
\operatorname{Cov}(K,h(I))>0,\qquad
\operatorname{Cov}(n-2K,h(I))<0.
\]

Summing (1) yields the global consistency formula
\[
\mathbb E\,I(\Pi_{n,k})=\frac{k(2n-k)}3.
\tag{4}
\]
This global first moment and the univariate inversion distribution are not claimed as new: classical inversion-generating polynomials already determine them. The assessed result is the position-resolved formula together with the explicit all-class, almost-surely strictly increasing coupling.

For \(k/n\to\tau\in[0,1/2]\) and \(d/n\to\delta\in[0,1]\) along admissible integer sequences, (1) also gives the nontrivial macroscopic profile
\[
\Pr\{\Pi_{n,k}(a)>\Pi_{n,k}(b)\}
\longrightarrow 2\tau^2+2\tau(1-2\tau)(1-\delta).
\tag{5}
\]

## Assumptions and scope

An involution is a permutation \(\pi\) with \(\pi^2=\mathrm{id}\). Its disjoint cycles have length one or two. The sample space at \((n,k)\) has cardinality
\[
N_{n,k}=\frac{n!}{2^k k!(n-2k)!},
\]
so every involution with exactly \(k\) two-cycles receives probability \(1/N_{n,k}\). All quantifiers in (1) cover each integer \(n\ge3\), \(0\le k\le\lfloor n/2\rfloor\), and \(1\le a<b\le n\). The full-chain coupling and inversion monotonicity cover \(n\ge2\). The covariance conclusions require non-degenerate \(K\). No independence of individual inversion indicators is assumed.

## Proof

**Step 1: exact two-position inversion probability.** Put \(r=2k\) and \(f=n-r\). By conjugation symmetry, the moved set is a uniform \(r\)-subset; conditional on that set, the \(r\) moved positions form a uniform perfect matching. Fix \(a<b\) and \(d=b-a\).

If both are fixed, no inversion occurs. If both are moved, their joint probability is \(r(r-1)/(n(n-1))\). Conditional on both being moved, their two-cycle pairs them together with probability \(1/(r-1)\); this always creates the inversion. Otherwise, their two distinct partners have exchangeable order, creating the inversion with probability \(1/2\). Hence this case contributes
\[
\frac{r(r-1)}{n(n-1)}\left(\frac1{r-1}+\frac{r-2}{2(r-1)}\right)
=\frac{r^2}{2n(n-1)},
\]
for \(r\ge2\). Its contribution is zero for \(r=0\), consistent with the final expression.

If \(a\) is moved and \(b\) fixed, the probability of that status is \(rf/(n(n-1))\); the partner of \(a\) is uniform among the remaining \(n-2\) labels, and an inversion occurs iff that partner exceeds \(b\), giving \((n-b)/(n-2)\). If \(a\) is fixed and \(b\) moved, an inversion occurs iff the partner of \(b\) is below \(a\), giving \((a-1)/(n-2)\). The two mixed contributions sum to
\[
\frac{rf}{n(n-1)}\frac{(n-b)+(a-1)}{n-2}
=\frac{rf(n-d-1)}{n(n-1)(n-2)}.
\]
Adding these contributions and substituting \(r=2k\) proves (1). The argument is also valid at the degenerate endpoints by omitting impossible cases.

**Step 2: sharp monotonicity.** The nearest-neighbor and farthest-gap probabilities are
\[
p_{n,k}(1)=\frac{2k(n-k)}{n(n-1)},\qquad
p_{n,k}(n-1)=\frac{2k^2}{n(n-1)}.
\]
Equation (1) is the convex interpolation
\[
p_{n,k}(d)=\frac{n-d-1}{n-2}\,p_{n,k}(1)
+\frac{d-1}{n-2}\,p_{n,k}(n-1).
\]
Both endpoint expressions strictly increase when the admissible integer \(k\) is increased by one: the numerator increment for the near endpoint is \(n-2k-1>0\), and the far endpoint increases with \(k\). Their convex combination therefore strictly increases. Subtracting adjacent gaps in (1) proves the spatial slope and its exact equality cases. Summing over the \(n-d\) position pairs at each gap yields (4); equivalently use
\[
\sum_{d=1}^{n-1}(n-d)=\frac{n(n-1)}2,
\qquad
\sum_{d=1}^{n-1}(n-d)(n-d-1)=\frac{n(n-1)(n-2)}3.
\]

**Step 3: a uniform, strictly increasing coupling.** Start at the identity \(\Pi_{n,0}\). Suppose \(\Pi_{n,k}\) is uniform. Choose an unordered pair \(a<b\) uniformly among its \(n-2k\) fixed positions and replace the two fixed points with the transposition \((a\ b)\), obtaining \(\Pi_{n,k+1}\). Every involution having \(k+1\) transpositions has precisely \(k+1\) distinct predecessors: remove any one of its two-cycles, turning its endpoints into fixed points. Every source has the same number \(\binom{n-2k}{2}\) of choices, so a simple double count shows that the target is uniform.

For a fixed source \(\pi\), only comparisons involving \(a\) or \(b\) change. The inversion between \(a,b\) adds one. For \(t<a\) or \(t>b\), the sum of the two comparisons with \(a,b\) is unchanged. For each \(a<t<b\), the two comparisons together gain exactly two when \(a<\pi(t)<b\), and otherwise do not change; equality to an endpoint is impossible because \(a,b\) were fixed. This proves (2) and its strictly positive odd increment. Therefore (3) holds simultaneously for all successive \(k\). Conditioning on any non-degenerate \(K\), the function \(k\mapsto \mathbb E[h(I)\mid K=k]\) is strictly increasing, and the independent-copy identity
\[
2\operatorname{Cov}(K,g(K))=
\mathbb E[(K-K')(g(K)-g(K'))]
\]
proves the asserted strict covariance signs. Formula (5) follows by direct division of (1) by the appropriate powers of \(n\).

## Verification

Run `python verify_involution_filtration.py` with Python 3 and its standard library. The independent enumerator lists every involution of sizes \(2\) through \(10\), checks exact cardinalities, the full pairwise probability table at each two-cycle count, global inversion and descent moment identities, every possible fixed-pair increment, constant target-preimage counts, and uniformity of each coupling step. Additional exact-rational arithmetic checks through \(n=120\) test the closed formulas, the strict \(k\)-monotonicity, and gap slopes. One recorded execution completed **675,381 assertions**. These finite checks are reproducibility evidence only; the proof above establishes the unlimited quantifiers.

## Relationship to prior work

Désarménien's 1982 two-variable \(q\)-Hermite interpretation (his equation (3.10)) counts involutions jointly by fixed points and *total* inversion count. Dukes (2004, §2.3) and Hart–Rowley (2014, Theorem 1.1) present this literature and the Coxeter length polynomials for each two-cycle class. Consequently the marginal inversion law and its first moment in (4) are already known or derivable, and are not the assessed contribution. Those polynomials do not retain the position gap of an individual inversion event. The added statement is the spatially affine law (1) and the explicit simultaneous monotone coupling (2)–(3).

Pinsky's fixed-point-conditioned inversion study and Pinsky–Schickentanz's Ewens inversion study analyze different conjugation-invariant distributions on *all* permutations; conditioning an involution to have only one- and two-cycles is not their sampling law. Their formulas for individual inversions motivate the local question but do not directly furnish (1). Hansson's treatment of Bruhat-order structure on involution classes is order-theoretic and does not provide this uniform probability coupling.

## Limitations

The result concerns the uniform measures on involution conjugacy classes, not uniformly sampled arbitrary permutations conditioned only on fixed-point count. It does not determine joint dependence among two or more distinct inversion indicators, nor claim an optimal quantitative metric between consecutive inversion-count laws. Classical global inversion generating functions give stronger marginal enumerative information than (4). A complete literature search is not a proof of historical priority; older characterizations of involution length distributions could yield some distributional implications not stated explicitly.

## References

- J. Désarménien, *Les q-analogues des polynômes d'Hermite*, Séminaire Lotharingien de Combinatoire, B06b (1982), §3, equations (3.10)–(3.11). https://radon.mat.univie.ac.at/~slc/opapers/s06desar.pdf
- W. M. B. Dukes, *Permutation statistics on involutions*, first public arXiv submission 2004-12-11, §2.3. https://arxiv.org/abs/math/0412222
- S. B. Hart and P. J. Rowley, *Involution Statistics in Finite Coxeter Groups*, first public arXiv submission 2014-03-28, Theorem 1.1. https://arxiv.org/abs/1403.7506
- M. Hansson, *The Bruhat order on conjugation-invariant sets of involutions in the symmetric group*, Discrete Mathematics and Theoretical Computer Science (2015), Theorem 1. https://dmtcs.episciences.org/en/articles/2472/download
- R. G. Pinsky, *The Inversion Statistic in Derangements and in Other Permutations with a Prescribed Number of Fixed Points*, arXiv:2505.02058 (2025). https://arxiv.org/abs/2505.02058
- R. G. Pinsky and D. T. Schickentanz, *On Inversions in Random Permutations Under the Ewens Sampling Distribution*, first arXiv submission 2025-10-23, Theorem 1 and later conditioned variants. https://arxiv.org/abs/2510.20654
