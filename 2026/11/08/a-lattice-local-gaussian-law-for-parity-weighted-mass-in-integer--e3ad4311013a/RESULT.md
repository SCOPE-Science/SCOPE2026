# A lattice-local Gaussian law for parity-weighted mass in integer partitions

## Finding

Let \(\lambda\vdash n\) be an ordinary partition of a positive integer \(n\), sampled uniformly from the \(p(n)\) partitions. Define the signed parity mass
\[
D_n(\lambda)=\sum_{j\text{ odd}}j\,m_j(\lambda)-\sum_{j\text{ even}}j\,m_j(\lambda),
\]
where \(m_j(\lambda)\) counts parts of size \(j\). Let \(p(r)\) count ordinary partitions of \(r\), and let \(q(r)\) count partitions of \(r\) into odd parts, equivalently into distinct parts; both are zero at negative indices and satisfy \(p(0)=q(0)=1\).

**Exact fibers.** For every \(n\ge1\) and integer \(d\),
\[
\#\{\lambda\vdash n:D_n(\lambda)=d\}=
\begin{cases}
p((n-d)/4)\,q((n+d)/2),&d\equiv n\pmod4,\ |d|\le n,\\
0,&\text{otherwise}.
\end{cases}
\]

**Lattice-local Gaussian law.** Set \(s^2=2\sqrt6/\pi\). For each fixed \(K>0\), as \(n\to\infty\), uniformly over integers \(d\equiv n\pmod4\) with \(|d|\le K n^{3/4}\),
\[
\Pr(D_n=d)=\frac{4}{\sqrt{2\pi s^2}\,n^{3/4}}
\exp\!\left(-\frac{d^2}{2s^2n^{3/2}}\right)(1+o_K(1)).
\]
Consequently,
\[
\frac{D_n}{n^{3/4}}\ \xrightarrow{\ d\ }\ N(0,s^2),\qquad
\operatorname{Var}(D_n)\sim\frac{2\sqrt6}{\pi}n^{3/2},\qquad
\Pr(D_n>0)\to\frac12.
\]
For balanced parity mass, \(\Pr(D_n=0)=0\) if \(4\nmid n\), while for \(4\mid n\),
\[
\Pr(D_n=0)=\frac{p(n/4)q(n/2)}{p(n)}
\sim\frac{4}{\sqrt{2\pi s^2}\,n^{3/4}}.
\]
The exact factorization is a simple combinatorial identity; the local Gaussian asymptotic and its sharp lattice normalization are the principal quantitative results.

## Assumptions and scope

All parts are positive integers, arbitrary multiplicities are permitted, and the probability measure is uniform on partitions of total size \(n\), not a grand-canonical or independent-part model. Odd and even refer to **part values**, not their positions in the nonincreasing partition list. The limit ranges over all positive integer \(n\); the local assertion has any fixed finite window parameter \(K\) and holds only on the forced lattice \(d\equiv n\pmod4\). All asymptotic constants are explicit and universal.

## Proof

**1. Exact factorization and lattice.** Given a partition \(\lambda\), write \(O\) for the sum of its odd parts and \(E\) for the sum of its even parts. Then \(n=O+E\), \(d=O-E\), hence \(O=(n+d)/2\) and \(E=(n-d)/2\). Every even part is twice a positive integer; halving the even parts gives an arbitrary partition of \(E/2=(n-d)/4\). The odd parts form independently a partition of \(O=(n+d)/2\) into odd-valued parts. Conversely the two subpartitions uniquely reconstruct \(\lambda\). The condition that \(E\) is an even nonnegative integer forces \(d\equiv n\pmod4\), while \(O,E\ge0\) forces \(|d|\le n\). This proves the exact formula. Euler's odd-parts/distinct-parts identity identifies the two interpretations of \(q\).

**2. Uniform central expansion.** Put \(C=\pi\sqrt{2/3}\). The classical Hardy–Ramanujan and distinct-part asymptotics are
\[
p(r)\sim\frac{e^{C\sqrt r}}{4\sqrt3\,r},\qquad
q(r)\sim\frac{e^{(C/\sqrt2)\sqrt r}}{4\,3^{1/4}r^{3/4}}
\qquad(r\to\infty).
\]
Here \(C/\sqrt2=\pi/\sqrt3\). For \(d\) in the prescribed window, let \(u=d/n\), \(r=(n-d)/4\), and \(v=(n+d)/2\); both arguments tend uniformly to infinity. Their exponential factor divided by the exponential factor of \(p(n)\) has logarithm
\[
\frac{C\sqrt n}{2}\big(\sqrt{1-u}+\sqrt{1+u}-2\big)
=-\frac{C d^2}{8n^{3/2}}+O_K(n^{-1/2}).
\]
Their polynomial prefactors, divided by the prefactor of \(p(n)\), are uniformly
\[
\frac{2^{3/4}}{3^{1/4}}n^{-3/4}(1+o_K(1))
=\frac4{\sqrt{2\pi s^2}}n^{-3/4}(1+o_K(1)).
\]
Since \(1/(2s^2)=C/8\), multiplication proves the claimed local Gaussian formula. The normalization factor \(4\) is exactly the gap between adjacent permitted values of \(d\).

**3. Tail domination.** The asymptotic formulas above imply global estimates, with absolute constants, for all nonnegative integers \(r\):
\[
p(r)\ll (r+1)^{-1}e^{C\sqrt r},\qquad
q(r)\ll (r+1)^{-3/4}e^{(C/\sqrt2)\sqrt r}.
\]
For \(|d|\le n/2\), the algebraic prefactors of \(p((n-d)/4)q((n+d)/2)/p(n)\) are \(O(n^{-3/4})\). For \(|u|\le1\), the even concave function \(g(u)=(\sqrt{1-u}+\sqrt{1+u})/2\) satisfies \(g(0)=1\), \(g'(0)=0\), and \(g''(u)\le-1/4\) in the interior. Thus \(g(u)\le1-u^2/8\), and the probability of any supported \(d\) with \(|d|\le n/2\) is bounded by
\[
C_1 n^{-3/4}\exp\!\left(-\frac{C d^2}{8n^{3/2}}\right).
\]
For \(n/2<|d|\le n\), the same exponential inequality and the crude global polynomial bounds imply \(\Pr(D_n=d)\ll n^{A}e^{-c\sqrt n}\) for some fixed \(A,c>0\); at most \(n+1\) values can occur. Therefore, for every fixed \(r\ge0\), the normalized absolute \(r\)-th moments outside \(|d|>K n^{3/4}\) are uniformly bounded by a Gaussian tail integral plus a term tending to zero. In particular these tails vanish as \(K\to\infty\).

**4. Global law, variance and equality.** Summing the uniform local approximation over the arithmetic progression \(d\equiv n\pmod4\) gives Riemann sums with mesh \(4/n^{3/4}\). The tail bound proves convergence in law to the stated centered Gaussian and convergence of every fixed absolute moment. Hence \(\mathbb E[D_n]/n^{3/4}\to0\) and \(\mathbb E[D_n^2]/n^{3/2}\to s^2\), yielding \(\operatorname{Var}(D_n)\sim s^2n^{3/2}\). Symmetry and continuity of the Gaussian limit yield \(\Pr(D_n>0)\to1/2\). Finally, applying the exact fiber identity at \(d=0\), when \(4\mid n\), and the local limit proves the balanced-atom formula; when \(4\nmid n\), zero is forbidden by the lattice condition.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. It computes \(p\) by the pentagonal recurrence and \(q\) independently by odd-part dynamic programming, checks that the proposed fiber counts sum to \(p(n)\) for every \(1\le n\le200\), and independently enumerates all partitions for \(1\le n\le22\). It additionally compares exact moments and central lattice masses against the analytic scales for \(n=200,400,800,1600\). Execute `python3 verify.py`. All integer identities and enumeration checks are exact; decimal comparisons test trends but do not certify any asymptotic assertion.

## Relationship to prior work

Andrews and Ghosh Dastidar, *\(p(5n+4)\) again* (first public journal release January 3, 2026), named and developed the aggregate statistic `SOME`, which is \(\sum_{\lambda\vdash n} D_n(\lambda)\), and proved a generating function and congruences. Bardhan and Saikia (first public preprint June 30, 2026) extended these congruences and established parity-subsequence monotonicity. The earlier aggregate difference is already tabulated as OEIS A208477 (recorded in 2012), so neither the aggregate statistic nor its enumeration is claimed as new. The present result studies the full fiber distribution of the **per-partition** random variable, not those aggregate congruences. The simple exact splitting into odd and even parts is treated as an elementary reduction; its Gaussian lattice asymptotics, moment scale and balanced-atom asymptotic are the contribution claimed here.

Craig and Li study alternating signs assigned by **position of parts** in the sorted partition, a distinct statistic. Li and Zhao study **numbers** of parts in arithmetic-progression classes, with a log-gamma rather than Gaussian limit; Bringmann, Nazaroglu and van Ittersum likewise analyze arithmetic-progressions of part counts. Rausch and Stumpenhusen study aggregate signed masses for **restricted** partitions. None of the inspected statements supplies the present local formula or its lattice Gaussian law. A sufficiently general previously published local limit theorem for partition linear statistics could imply this result; that historical-priority risk is not excluded by an unsuccessful search.

## Limitations

This is a theorem for ordinary unrestricted integer partitions under uniform fixed-size sampling; it is not asserted for other partition ensembles, residues other than parity, or windows with \(K\) growing with \(n\). The proof uses standard global partition asymptotics; finite verification cannot certify the unbounded claims. The novelty comparison is limited to accessible published sources and indexed research records; historical uniqueness and independent validation are not certified.

## References

1. G. Bardhan and N. Saikia, *Some new congruences and identities for SOME(n), DSOME(n), overline SOME(n) functions and analogues*, arXiv:2606.31264 (first public June 30, 2026), https://arxiv.org/abs/2606.31264.
2. G. E. Andrews and M. Ghosh Dastidar, *\(p(5n+4)\) again*, Ramanujan Journal 69, Article 26 (2026), first public January 3, 2026, https://doi.org/10.1007/s11139-025-01280-7.
3. W. Craig and R. Li, *Distribution of Alternating Sums of Parts in Partitions*, arXiv:2501.17065 (2025), https://arxiv.org/abs/2501.17065.
4. J. Li and S. Zhao, *On Arithmetic-Progression Biases in Random Partitions: Limiting Laws and the Li-Zhao Conjecture*, arXiv:2610.30700 (2026), https://arxiv.org/abs/2610.30700.
5. K. Bringmann, C. Nazaroglu and J.-W. van Ittersum, *Asymptotics of partition parts in arithmetic progressions*, arXiv:2509.21202 (2025), https://arxiv.org/abs/2509.21202.
6. K. Rausch and J. Stumpenhusen, *The difference of the sums of odd and even parts of restricted partitions*, arXiv:2606.16585 (2026), https://arxiv.org/abs/2606.16585.
7. Classical Hardy–Ramanujan partition asymptotics, Euler's odd/distinct-parts identity, and the classical distinct-part partition asymptotic; these standard input theorems are not claimed as new.
