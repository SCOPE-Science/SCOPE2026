# Two Poisson obstruction fields at the sparse-Mallows adjacent-matching threshold

## Finding

Let \(\Pi_n\) have the Mallows distribution on permutations of \(\{1,\ldots,n\}\), proportional to \(q^{\operatorname{inv}(\pi)}\), and let \(\mathcal M_n\) be the event that \(\Pi_n\) is a product of pairwise disjoint adjacent transpositions (including the empty product). For every \(n\ge1\) and \(0<q<1\),
\[
\mathbb P_q(\mathcal M_n)=\frac{F_n(q)}{Z_n(q)},\quad
F_n(q)=\sum_{k=0}^{\lfloor n/2\rfloor}{n-k\choose k}q^k,
\quad Z_n(q)=\prod_{j=1}^n\frac{1-q^j}{1-q}.
\]
Here \(F_0=F_1=1\) and \(F_n=F_{n-1}+qF_{n-2}\) for \(n\ge2\). Uniformly as \(q\downarrow0\), for integer \(n\ge2\),
\[
\log\mathbb P_q(\mathcal M_n)=-2nq^2+O(nq^3+q^2).
\]
Consequently, along any sequence \(q_n\in(0,1)\) with \(q_n\to0\), the probability tends to \(1\) if \(nq_n^2\to0\), to \(e^{-2c}\) if \(nq_n^2\to c\in(0,\infty)\), and to \(0\) if \(nq_n^2\to\infty\).

More structurally, use the insertion inversion code \(E_j\), the number of values smaller than \(j\) appearing to its right in \(\Pi_n\), for \(j=1,\ldots,n\). Define defects \(A_j=\mathbf1\{E_j\ge2\}\) for \(3\le j\le n\) and \(B_j=\mathbf1\{E_j=E_{j+1}=1\}\) for \(2\le j<n\). If \(nq_n^2\to c\in[0,\infty)\), the marked point process
\[
\mathcal N_n=\sum_{j=3}^n A_j\delta_{(j/n,\mathrm A)}+
\sum_{j=2}^{n-1} B_j\delta_{(j/n,\mathrm B)}
\]
converges on \([0,1]\times\{\mathrm A,\mathrm B\}\) to a Poisson random measure of intensity \(c\,dt\otimes(\delta_{\mathrm A}+\delta_{\mathrm B})\). In particular, the two numbers of defects converge jointly to independent \(\operatorname{Pois}(c)\) variables. The matching event is exactly the event of no defects.

## Assumptions and scope

All finite statements use integer \(n\ge1\) and real \(0<q<1\), with permutation composition interpreted as disjoint swaps of positions \(i\) and \(i+1\). The limit statements require \(q=q_n\to0\); the point-process assertion additionally assumes finite limit \(nq_n^2\to c\). The intensity is understood as zero when \(c=0\). Each \(E_j\in\{0,\ldots,j-1\}\) and \(E_1=0\). An insertion of value \(j\) is made into the existing permutation of \(1,\ldots,j-1\) so that exactly \(E_j\) existing values lie to its right. The insertion code uniquely determines the permutation; its coordinates are independent, with
\[
\mathbb P(E_j=k)=\frac{(1-q)q^k}{1-q^j},\qquad 0\le k\le j-1.
\]
These standard Mallows-code facts are included as premises with a direct proof below.

## Proof

**Insertion law.** The insertion algorithm is bijective from the Cartesian product of code ranges to permutations. Inserting value \(j\) creates exactly \(E_j\) new inversions, so the Mallows weight factors as \(q^{\sum_j E_j}\) and normalization factors as \(Z_n(q)\). Thus the code coordinates are independent with the stated truncated-geometric laws.

**Structural equivalence.** Induct on \(j\) in the insertion algorithm. If the already formed prefix is a product of disjoint adjacent transpositions, appending the maximum \(j\) (code \(E_j=0\)) preserves this property. Inserting it one place from the end (code \(E_j=1\)) swaps \(j\) with \(j-1\) exactly when \(E_{j-1}=0\); otherwise \(j-1\) is already paired and insertion produces a component involving at least three values. Inserting \(j\) farther from the end (code \(E_j\ge2\)) also produces a component involving at least three values. Conversely, deleting the greatest value from any disjoint-adjacent-swap permutation removes either its fixed point or its terminal swap, giving the inverse induction. Therefore
\[
\mathcal M_n=\{E_j\le1\text{ for all }j\}\cap\{E_jE_{j+1}=0\text{ for }1\le j<n\}=
\{\mathcal N_n([0,1]\times\{\mathrm A,\mathrm B\})=0\}.
\]
There are exactly \({n-k\choose k}\) ways to choose \(k\) mutually nonadjacent edges of an \(n\)-vertex path. Each corresponding permutation has \(k\) inversions. This proves the exact polynomial numerator and recurrence.

**Uniform logarithmic expansion.** Put \(r_{\pm}(q)=(1\pm\sqrt{1+4q})/2\). The path recurrence gives
\[
F_n(q)=\frac{r_+(q)^{n+1}-r_-(q)^{n+1}}{\sqrt{1+4q}}.
\]
Since \(Z_n(q)=(1-q)^{-n}\prod_{j=1}^n(1-q^j)\), for \(n\ge2\),
\[
\log\frac{F_n(q)}{Z_n(q)}=
(n+1)\log r_+(q)-\tfrac12\log(1+4q)
+\log\bigl(1-(r_-/r_+)^{n+1}\bigr)
+n\log(1-q)-\sum_{j=1}^n\log(1-q^j).
\]
The coefficient multiplying \(n\) equals
\[\log[(1-q)r_+(q)]=-2q^2+O(q^3).\]
The remaining terms can be regrouped as \(\log[r_+^2/\sqrt{1+4q}]\), \(\log(1-(r_-/r_+)^{n+1})\), and \(-\sum_{j=2}^n\log(1-q^j)\), plus at most one extra \(O(q^2)\) boundary term; each grouped term is \(O(q^2)\) uniformly over \(n\ge2\), using \(r_-/r_+=O(q)\) and \(\sum_{j\ge2}q^j=O(q^2)\). This proves the expansion and its three probability regimes.

**Two-type Poisson point-process limit.** For \(j\ge3\), uniformly in \(j\),
\[
\mathbb P(A_j=1)=\frac{q^2-q^j}{1-q^j}=q^2[1+O(q)],
\]
and, uniformly for \(2\le j<n\),
\[
\mathbb P(B_j=1)=\frac{q^2(1-q)^2}{(1-q^j)(1-q^{j+1})}=q^2[1+O(q)].
\]
Two distinct \(A\)-events use independent code coordinates. Two \(B\)-events are independent unless their indices differ by one, and a run of \(\ell\ge2\) consecutive \(B\)-events forces \(\ell+1\) code coordinates to equal one, an event of probability \(O(q^{\ell+1})\). An \(A_j\)-event cannot coexist with a \(B\)-event using the same coordinate; otherwise \(A\)- and \(B\)-events are independent. For any fixed mixed factorial moment of counts in disjoint spatial intervals, the contribution from tuples with independent code supports has the limiting factorial moment of independent Poisson counts with means \(c\) times the interval lengths, by Riemann sums and \(nq^2\to c\). All other tuples either have probability zero or contain a cluster of at least two overlapping \(B\)-events. Every cluster of \(\ell\ge2\) contributes at most \(O(nq^{\ell+1})\), which tends to zero since \(nq^2\) is bounded and \(q\to0\). This bounds every nonisolated term, including several disjoint clusters. If \(c=0\), the expected total number of marks tends to zero directly. For \(c>0\), the mixed factorial moments therefore converge to those of independent Poisson counts on all finite collections of disjoint intervals. Tightness follows from bounded expected total count; count convergence on interval partitions identifies the marked Poisson random measure. Taking total mass gives independent Poisson defect counts. Combining with the exact structural equivalence proves the zero-defect probability limit (also provided directly by the uniform logarithmic expansion).

## Verification

The accompanying standalone standard-library program `verify.py` enumerates all permutations through size eight, checks the inversion-code bijection and structural equivalence, and verifies the path-matching numerator and Mallows normalizer at three rational parameters with exact arithmetic. It then checks the logarithmic formula and its bounded-error critical-scale behavior numerically at larger sample sizes. It reports 138780 successful assertions/check events. Enumeration is finite and **does not** certify the limiting point process; that conclusion follows from the preceding factorial-moment argument.

To reproduce: run `python3 verify.py` in a directory containing this document and the file. No network, extra dependencies, or randomness are required.

## Relationship to prior work

Mallows insertion coding and the \(q\)-factorial normalizer are classical; these are not presented as new. Pinsky (2019 preprint, published 2021) analyzes avoidance of **individual** length-three patterns under fixed \(q\) and states the independent truncated-geometric insertion code explicitly. Crane, DeSalvo and Elizalde (2016 preprint, 2018 journal) study **consecutive-pattern** avoidance at fixed \(q\) and related growth rates, not the joint obstruction process for disjoint adjacent transpositions under \(q_n\to0\). He (2021 preprint) and He, Müller and Verstraaten (2022 preprint, 2023 journal) establish cycle-count central limit theorems for **fixed** \(q\ne1\), not the present sparse-parameter matching transition. The distinction is a triangular array with a nontrivial \(nq_n^2\) limit and two marked independent Poisson obstruction mechanisms. It may be possible to derive the limiting law from more general local-dependence Poisson theorems plus standard Mallows insertion formulas; no novelty is claimed for those generic tools.

## Limitations

The result concerns the specific event of being a product of **disjoint adjacent** transpositions, not arbitrary involutions or all permutations with only one- and two-cycles. Its Poisson-field limit assumes \(q_n\to0\), and is not a fixed-positive-\(q\) theorem. The quantitative error in \(\log\mathbb P(\mathcal M_n)\) is a uniform asymptotic order, not an explicit optimal universal constant. Historical priority for an equivalent matching-probability identity or two-mark limit under different terminology is not independently established.

## References

1. J. He, *A central limit theorem for cycles of Mallows permutations*, arXiv:2112.09789 (first public 2021-12-17), https://arxiv.org/abs/2112.09789.
2. J. He, T. Müller, T. W. Verstraaten, *Cycles in Mallows random permutations*, arXiv:2201.11610 (2022 preprint), *Random Structures & Algorithms* 63 (2023), 1054–1099, https://arxiv.org/abs/2201.11610.
3. R. G. Pinsky, *Permutations avoiding a pattern of length three under Mallows distributions*, arXiv:1908.01382 (2019 preprint), *Random Structures & Algorithms* 58 (2021), 676–690, https://arxiv.org/abs/1908.01382.
4. H. Crane, S. DeSalvo, S. Elizalde, *The probability of avoiding consecutive patterns in the Mallows distribution*, arXiv:1609.01370 (2016 preprint), *Random Structures & Algorithms* 53 (2018), 417–447, https://arxiv.org/abs/1609.01370.
