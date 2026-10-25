# The first failure of uniform refinement coupling occurs on twenty points

## Finding

Let \(\mathcal P_{n,k}\) denote the set of set partitions of \(\{1,\ldots,n\}\) into exactly \(k\) nonempty blocks, and let \(U_{n,k}\) be uniform on \(\mathcal P_{n,k}\). A *refinement coupling* of \(U_{n,k}\) and \(U_{n,k+1}\) is a joint law \((P,Q)\) with these marginals such that every block of \(Q\) is contained in a block of \(P\) almost surely.

**Theorem (sharp finite threshold).** For every integer \(2\le n\le19\) and every \(1\le k<n\), a refinement coupling exists. At \(n=20\), there is no refinement coupling of \(U_{20,2}\) and \(U_{20,3}\). Thus 20 is the smallest ground-set size at which the family of uniform fixed-block-count partition laws fails refinement stochastic monotonicity.

The obstruction is explicit. The probability of the two-block size profile \((10,10)\) is \(92378/524287\), whereas the probability under the three-block uniform law of *any* refinement of a \((10,10)\) partition is only \(94410316/580606446\). The strict inequality rules out a coupling.

## Assumptions and scope

The ground set is labeled, every set partition with the stipulated number of blocks has equal probability, and refinement means splitting blocks without moving an element between old blocks. The theorem compares *adjacent* levels \(k\) and \(k+1\). There are \(n-1\) such pairs for each \(n\ge2\). The positive range is completely classified for all ground-set sizes through 19; the negative assertion applies to one pair at size 20. No assertion is made about all pairs at sizes greater than 20.

Write \(\lambda=(\lambda_1,\ldots,\lambda_k)\vdash n\) for a nonincreasing integer partition recording the sizes of blocks of a set partition. If \(m_j\) counts occurrences of part size \(j\), its labeled orbit has size
\[
N_n(\lambda)=\frac{n!}{\prod_{j=1}^n (j!)^{m_j}m_j!}.
\]
The total number of partitions into \(k\) blocks is the Stirling number \(S(n,k)=\sum_{\lambda\vdash n,\,\ell(\lambda)=k}N_n(\lambda)\).

## Proof

**1. Exact symmetry reduction.** Let \(A_k\) be the integer-partition profiles \(\lambda\vdash n\) with \(\ell(\lambda)=k\). Put a directed edge \(\lambda\to\mu\) precisely when \(\mu\) is obtained by replacing one part \(r\ge2\) of \(\lambda\) with two positive parts summing to \(r\), then sorting. Let \(a_\lambda=N_n(\lambda)/S(n,k)\), \(b_\mu=N_n(\mu)/S(n,k+1)\).

A refinement coupling induces nonnegative edge weights \(x_{\lambda\mu}\) with row sums \(a_\lambda\) and column sums \(b_\mu\). Conversely, if such weights exist, sample the profile edge with probability \(x_{\lambda\mu}\); choose one specific labeled pair of partitions realizing that profile edge; simultaneously relabel both partitions by a uniform permutation of \(\{1,\ldots,n\}\). The two marginals are uniform within their respective block-size profiles by the transitive relabeling action, and therefore exactly \(U_{n,k}\) and \(U_{n,k+1}\). Thus an arbitrary refinement coupling exists **if and only if** a nonnegative profile-edge transportation flow exists. This is an exact equivalence, not a heuristic symmetry assumption.

**2. Integral max-flow criterion.** Set \(L=\operatorname{lcm}(S(n,k),S(n,k+1))\). Form a network with arcs from a source to each \(\lambda\in A_k\) of integer capacity \(L a_\lambda\), arcs from each \(\mu\in A_{k+1}\) to a sink of integer capacity \(L b_\mu\), and arcs \(\lambda\to\mu\) of capacity \(L\) whenever splitting is possible. By the integral max-flow theorem, the desired transportation flow exists exactly when the maximum flow has value \(L\). Every input capacity is a nonnegative integer; the integral max-flow algorithm in `verify_refinement.py` performs only exact integer operations.

**3. All lower orders.** The accompanying standalone program generates every integer partition of \(n\), computes all orbit sizes by the displayed factorial formula, constructs every legal profile split, and executes an exact integer maximum-flow calculation for every pair
\[
2\le n\le19,\qquad1\le k<n.
\]
All \(171=\sum_{n=2}^{19}(n-1)\) networks have maximal flow equal to \(L\). The complete finite search is exhaustive over profiles, and step 1 proves that this reduced search also certifies the full labeled probability spaces. Execute `python3 verify_refinement.py` using Python's standard library. The last line reports the 171 saturated networks and the independent finite obstruction. Standard correctness of integral max flow, together with the transparent integer arithmetic in the verifier, proves the finite positive assertions.

**4. The first obstruction.** Consider the set \(\mathcal A\subset\mathcal P_{20,2}\) of balanced two-block partitions, whose size profile is \((10,10)\). There are
\[
|\mathcal A|=\frac12\binom{20}{10}=92378,
\qquad |\mathcal P_{20,2}|=S(20,2)=524287.
\]
A one-block split of a balanced partition produces exactly one of the five three-block profiles
\[
(10,9,1),\ (10,8,2),\ (10,7,3),\ (10,6,4),\ (10,5,5).
\]
Conversely, every partition of these profiles refines at least one balanced two-block partition (merge the two blocks not of size 10). The union \(\mathcal N(\mathcal A)\) of all possible refinements therefore has the exact size
\[
1847560+8314020+22170720+38798760+23279256=94410316.
\]
Also \(S(20,3)=580606446\). Consequently,
\[
\frac{|\mathcal A|}{S(20,2)}
=\frac{92378}{524287}
>\frac{94410316}{580606446}
=\frac{|\mathcal N(\mathcal A)|}{S(20,3)}.
\]
After cross multiplication the positive difference is exactly \(4137160923896\). In every refinement coupling, \(P\in\mathcal A\) would imply \(Q\in\mathcal N(\mathcal A)\), contradicting the displayed probability inequality. Thus the coupling fails at \((n,k)=(20,2)\), establishing the claimed sharp threshold.

## Verification

The dependency-free file `verify_refinement.py` computes all profile orbit counts, tests each possible block split, and verifies exact maximum-flow saturation for the 171 required cases. It separately checks every integer in the size-20 Hall obstruction and confirms non-saturation for \((20,2)\). A complete run produced: `PASS 171 exact feasible adjacent couplings for n<=19; exact obstruction for n=20,k=2`. This is finite exhaustive computation backed by the explicit orbit reduction; no claim about untested larger sizes is inferred from numerical evidence.

## Relationship to prior work

Classical work on the partition lattice asks whether there is an *injective matching* from the smaller of two adjacent levels into the larger (Canfield, 1993, and the discussion by Graham). A matching condition is not the normalized transportation condition here: when the level sizes are unequal, a fractional coupling requires each group of starting partitions to have a proportionately large refinement neighborhood, not merely enough distinct neighbors for an injection. The two properties cannot be conflated. In particular, a theorem about matchings or large antichains does not by itself supply the complete exact classification of uniform-law refinement couplings through size 20.

Pittel (2000) investigates meet and join of independently sampled *unconditioned* uniform set partitions and supplies relevant probabilistic background, not a coupling between adjacent fixed-block-count laws. Graham's note discusses Hall's theorem, antichains, and the classical matching question rather than normalized coupling of the two uniform probability measures. The entire Canfield paper was not accessible during the comparison; its abstract and metadata were checked, so an implicit antecedent in its proof remains a historical-priority risk. No assertion of uniqueness in the full literature follows from search absence.

## Limitations

The finite positive range is certified using exact algorithmic enumeration, not a closed-form symbolic construction of the 171 flows. The algorithm is reproducible and dependency-free, but each claimed flow is a finite computation. The original Canfield matching article could not be inspected in full; independent priority review is warranted. The result does not establish a monotone coupling for all \(n\) or describe which pairs fail for \(n>20\), and it does not claim that every scalar partition statistic reverses its stochastic order at 20.

## References

1. E. R. Canfield, *Matchings in the Partition Lattice*, SIAM Journal on Discrete Mathematics 6 (1993), 100–109, DOI: 10.1137/0406008. Abstract and metadata inspected; full paper not accessible.
2. B. Pittel, *Where the Typical Set Partitions Meet and Join*, Electronic Journal of Combinatorics 7 (2000), R5, DOI: 10.37236/1483. Public PDF, introduction and theorem statements inspected; published 2000-01-15.
3. R. L. Graham, *Maximum Antichains in the Partition Lattice*, publicly available scan, https://www.math.ucsd.edu/~ronspubs/78_14_antichains.pdf. Material on pages 84–85 inspected.
4. Classical integral max-flow/min-cut theorem and Stirling-number partition count; the verifier supplies every case-specific integer input.
