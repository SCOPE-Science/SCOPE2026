# Sharp lattice Gaussian law for the odd–even total-weight discrepancy of integer partitions

## Finding

For an unrestricted partition \(\lambda\vdash n\), define the **odd–even total-weight discrepancy**
\[
D(\lambda)=\sum_{j\ge1}(-1)^{j-1}j\,m_j(\lambda),
\]
where \(m_j(\lambda)\) counts parts of size \(j\). Let \(p(n)\) denote the number of unrestricted integer partitions of \(n\), \(Q(n)\) the number of partitions into odd-sized parts, and \(N_n(d)\) the number with \(D(\lambda)=d\). Define \(p(t)=Q(t)=0\) when \(t\) is not a nonnegative integer.

The **exact coefficient formula** is
\[
N_n(d)=Q\!\left(\frac{n+d}{2}\right)p\!\left(\frac{n-d}{4}\right)
\quad(n\ge0,\ d\in\mathbb Z).
\]
In particular, the support is contained in \(d\equiv n\pmod4\). For every fixed \(K>0\), as \(n\to\infty\), uniformly over the lattice integers \(d\equiv n\pmod4\) with \(|d|\le K n^{3/4}\),
\[
\frac{N_n(d)}{p(n)}=
\frac{2}{6^{1/4}n^{3/4}}
\exp\!\left(-\frac{\pi d^2}{4\sqrt6\,n^{3/2}}\right)
\bigl(1+o_K(1)\bigr).
\tag{1}
\]
If a partition of \(n\) is uniformly random, then
\[
\frac{D(\lambda)}{n^{3/4}}\ \Longrightarrow\
\mathcal N\!\left(0,\frac{2\sqrt6}{\pi}\right).
\tag{2}
\]
Consequently, the probabilities of positive and negative discrepancy both tend to \(1/2\). The number of exactly balanced partitions is zero unless \(4\mid n\); for multiples of four it is **exactly** \(Q(n/2)p(n/4)\) and satisfies
\[
N_n(0)\sim\frac{2}{6^{1/4}}\frac{p(n)}{n^{3/4}}.
\tag{3}
\]

## Assumptions and scope

These are ordinary integer partitions with unlimited multiplicities and integer part sizes. The discrepancy counts **total values of parts**, not the number of odd or even parts and not alternating signs by position in a partition. The asymptotic parameter \(n\) is any positive integer tending to infinity; \(K\) is fixed and positive, and the relative error in (1) is uniform over its indicated finite lattice window. The variance in (2) is for the normalized discrepancy, not the unscaled random variable. No independence assumptions on the parts of a uniformly random partition are needed.

## Proof

**1. Exact factorization and lattice.** Decompose a partition uniquely into its odd-sized subpartition, of total weight \(a\), and its even-sized subpartition, of total weight \(2b\). Halving each even part gives an unrestricted partition of \(b\), while the odd subpartition is one of \(Q(a)\) choices. The equations \(n=a+2b\), \(d=a-2b\) have the unique solution
\[
a=(n+d)/2,\qquad b=(n-d)/4.
\]
This proves the exact formula for all \(n\ge0\) and \(d\in\mathbb Z\), and the support assertion. Summing it over all \(d\) gives \(p(n)\) by the disjoint decomposition.

**2. Classical asymptotics.** As \(t\to\infty\) over positive integers, Hardy–Ramanujan asymptotics and the classical odd/distinct partition asymptotic give
\[
p(t)\sim \frac{\exp(\pi\sqrt{2t/3})}{4\sqrt3\,t},
\qquad
Q(t)\sim\frac{\exp(\pi\sqrt{t/3})}{4\,3^{1/4}t^{3/4}}.
\tag{4}
\]
Euler's odd/distinct partition identity identifies \(Q\) with the familiar distinct-part partition count. For \(|d|\le K n^{3/4}\), the two indices \(a=(n+d)/2\) and \(b=(n-d)/4\) both tend to infinity uniformly because they are constant multiples of \(n\) plus \(O_K(n^{3/4})\). Hence the relative errors in (4) are uniform in this window, even after multiplication.

**3. Uniform saddle expansion and constant.** By the expressions for \(a,b\), the product of the two exponential factors in (4) equals
\[
\exp\!\left(\frac{\pi}{\sqrt6}
[\sqrt{n+d}+\sqrt{n-d}]\right).
\]
The elementary Taylor expansion, uniformly when \(|d|\le K n^{3/4}\), is
\[
\frac{\pi}{\sqrt6}\bigl(\sqrt{n+d}+\sqrt{n-d}-2\sqrt n\bigr)
=-\frac{\pi d^2}{4\sqrt6\,n^{3/2}}+O_K(n^{-1/2}).
\tag{5}
\]
The ratio of polynomial prefactors in \(Q(a)p(b)/p(n)\) equals
\[
\frac{n}{4\,3^{1/4}a^{3/4}b}
=\frac{2}{6^{1/4}n^{3/4}}\bigl(1+O_K(n^{-1/4})\bigr).
\tag{6}
\]
Combining (4)–(6) establishes (1), including the precise lattice normalization.

**4. Weak Gaussian convergence.** Let \(\sigma^2=2\sqrt6/\pi\) and let \(\phi_{\sigma}\) be the density of \(\mathcal N(0,\sigma^2)\). The right side of (1) is exactly \(4n^{-3/4}\phi_{\sigma}(d/n^{3/4})\) times \(1+o_K(1)\). The spacing between successive admissible values of the normalized discrepancy is \(4n^{-3/4}\). Thus finite-interval probability sums converge, by Riemann summation, to the Gaussian integral on that interval. Taking symmetric windows \([-K,K]\) and sending \(K\to\infty\), whose Gaussian mass tends to one, proves tightness and (2). The atom at zero tends to zero by (1), yielding equal limiting signs. Lastly, the exact lattice congruence permits \(D=0\) if and only if \(4\mid n\); (1) with \(d=0\) gives (3).

## Verification

The standalone file `verify.py` computes \(p(t)\) and \(Q(t)\) independently by partition recurrences. It exhaustively enumerates ordinary partitions for small \(n\), checks every discrepancy count against the exact product formula, and checks normalization at larger cutoffs. It also compares exact balanced fractions and nonzero lattice fractions against (1) for increasing multiples of four. Run with `python3 verify.py` in the directory containing this document; it prints `VERIFY_OK` on success. The asymptotic theorem follows from (4)–(6); finite experiments do **not** certify an infinite limit.

## Relationship to prior work

Andrews and Ghosh Dastidar introduced the aggregate signed odd/even *weight* statistic `SOME(n)` and derived its generating function and congruences [1]. Bardhan and Saikia developed additional congruences, arithmetic identities and monotonicity for the same aggregate statistic [2]. Neither full text states the *partition-level* local Gaussian lattice law (1). Craig and Li [3] study alternating summands according to their **position** in the ordered partition, a different random variable with different scaling; Bringmann–Man–Rolen–Storzer [4] study relative **numbers of parts** in residue classes, not the values summed here. The exact product factorization is elementary and is not claimed to be a new partition identity. The asserted contribution is the explicitly normalized local limit and its balanced-count consequence.

## Limitations

The local relative estimate is established only on windows \(|d|\le K n^{3/4}\) for fixed \(K\), not uniformly across the entire support or in large-deviation ranges. No effective uniform error constant, Berry–Esseen rate, or tail rate is claimed. Classical asymptotic ingredients are assumed known. A general multivariate partition-limit theorem may imply the conclusion without explicitly naming this statistic; bibliographic priority remains subject to independent scrutiny. The proof is a standalone derivation rather than a claim of a new general limit-theorem methodology.

## References

1. G. E. Andrews and M. Ghosh Dastidar, *\(p(5n+4)\) again*, The Ramanujan Journal 69 (2026), Article 26, DOI `10.1007/s11139-025-01280-7`; full open-access article: https://link.springer.com/article/10.1007/s11139-025-01280-7.
2. G. Bardhan and N. Saikia, *Some new congruences and identities for SOME(n), DSOME(n), overline-SOME(n) functions and analogues*, arXiv:2606.31264 (first posted 2026-06-30), https://arxiv.org/abs/2606.31264.
3. W. Craig and R. Li, *Distribution of Alternating Sums of Parts in Partitions*, arXiv:2501.17065, https://arxiv.org/html/2501.17065.
4. K. Bringmann, S. H. Man, L. Rolen and M. Storzer, *Asymptotics of parity biases for partitions into distinct parts via Nahm sums*, Proc. Lond. Math. Soc. 129 (2024), e70010, DOI `10.1112/plms.70010`.
5. G. H. Hardy and S. Ramanujan, classical asymptotics for integer partitions; the odd/distinct-part analogue is standard and follows from Euler's identity and classical partition asymptotics.
