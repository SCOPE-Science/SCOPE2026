# A sharp six-party boundary for uniqueness of envy-free proportional quota lotteries

## Finding

Consider random allocation of the integer surplus seats in an apportionment instance with exactly **three distinct lower-quota strata**, and suppose fractional quotas are strictly ordered within each stratum. Every instance with at most five parties has **at most one** probability distribution on quota-respecting, envy-free, exactly sized seat allocations whose per-party expected seats equal the standard quotas. This is sharp: there is a six-party instance with three two-party strata and two distinct such lotteries.

The result is a uniqueness statement, **not** an existence theorem: for some input quotas no envy-free proportional lottery exists.

## Assumptions and scope

Let the three strata have distinct nonnegative integer lower quotas \(F_1,F_2,F_3\), sizes \(m_1,m_2,m_3\geq1\), and strictly ordered fractional residues \(0\leq r_{b,1}<\cdots<r_{b,m_b}<1\). Thus \(n=m_1+m_2+m_3\) parties have standard quotas \(F_b+r_{b,j}\). Assume the fixed total house size is integral, equivalently \(k=\sum_{b,j}r_{b,j}\in\{0,\ldots,n\}\). Every realization gives each party its floor or floor-plus-one and awards exactly \(k\) additional seats. Proportionality means the probability that party \((b,j)\) receives the additional seat is exactly \(r_{b,j}\). Envy means a party entitled to a larger standard quota receives strictly fewer seats than another party. A lottery is envy-free when every positive-probability realization has zero envy.

Two lotteries are distinct if they assign different probabilities to at least one deterministic allocation, not merely if implemented by different random seeds or algorithms.

## Proof

**1. Nested form.** Distinct integer floors cannot produce envy under quota-respecting rounding: when one floor is larger, the corresponding assigned seat count is never strictly below a smaller-floor party's count. Within a stratum, strict residue order means zero envy holds exactly when the parties rounded up are a top-residue suffix. Thus each zero-envy outcome corresponds uniquely to a triple \(t=(t_1,t_2,t_3)\) with \(0\leq t_b\leq m_b\) and \(t_1+t_2+t_3=k\), where \(t_b\) is the number selected from stratum \(b\).

**2. The probability map.** Let \(\mathcal T_{\boldsymbol m,k}\) consist of all such triples. Put a probability variable \(p_t\) on each triple. Normalization and proportionality give the matrix system

\[
M_{\boldsymbol m,k}p=\left(1,r_{1,1},\ldots,r_{1,m_1},r_{2,1},\ldots,r_{3,m_3}\right)^{\!\mathsf T},
\]

where columns are indexed lexicographically by \(t\in\mathcal T_{\boldsymbol m,k}\). Row zero of \(M\) is all ones; row \((b,j)\) in increasing-residue order is \(\mathbf1\{t_b\ge m_b-j+1\}\). Every entry is zero or one. If \(M\) has linearly independent columns, the distribution \(p\) is uniquely determined whenever a nonnegative solution exists.

**3. Exhaustive exact-rank certificates for \(n\le5\).** Up to permutation of strata, the only three-positive-part size patterns are \((1,1,1)\), \((2,1,1)\), \((2,2,1)\), and \((3,1,1)\). When \(k=0\) or \(k=n\), there is just one possible triple. For each nontrivial \(k\) the table gives the number \(N\) of columns, a set of \(N\) row indices of \(M\) (zero-based), and the determinant of that square minor. Every displayed determinant has absolute value one and hence certifies full column rank.

| Stratum sizes | \(k\) | \(N\) | Row indices | Determinant |
|---|---:|---:|---|---:|
| \((1,1,1)\) | 1 | 3 | 0,1,2 | -1 |
| \((1,1,1)\) | 2 | 3 | 0,1,2 | 1 |
| \((2,1,1)\) | 1 | 3 | 0,2,3 | -1 |
| \((2,1,1)\) | 2 | 4 | 0,1,2,3 | 1 |
| \((2,1,1)\) | 3 | 3 | 0,1,3 | 1 |
| \((2,2,1)\) | 1 | 3 | 0,2,4 | -1 |
| \((2,2,1)\) | 2 | 5 | 0,1,2,3,4 | 1 |
| \((2,2,1)\) | 3 | 5 | 0,1,2,3,4 | 1 |
| \((2,2,1)\) | 4 | 3 | 0,1,3 | 1 |
| \((3,1,1)\) | 1 | 3 | 0,3,4 | -1 |
| \((3,1,1)\) | 2 | 4 | 0,2,3,4 | 1 |
| \((3,1,1)\) | 3 | 4 | 0,1,2,4 | 1 |
| \((3,1,1)\) | 4 | 3 | 0,1,4 | 1 |

Each certificate is reproducible by substituting the specified triples in the explicit formula for \(M\) and applying ordinary exact determinant arithmetic. Since the partition list is exhaustive, every three-stratum instance of size at most five has at most one envy-free proportional lottery.

**4. Sharp six-party example.** Take three lower-quota strata with distinct floors \((1,2,3)\), and two parties in each stratum with fractional residues \((1/5,4/5)\). The total house size is \(2(1+2+3)+3=15\), with three surplus seats. In the triple-count notation, put probability \(2/5\) on \((1,1,1)\). The first lottery puts probability \(1/10\) on **each** of the six permutations of \((0,1,2)\). The second puts probability \(1/5\) on precisely \((0,1,2)\), \((1,2,0)\), and \((2,0,1)\); other noncentral outcomes receive probability zero. In both lotteries, each stratum's round-up count has probabilities \((1/5,3/5,1/5)\) on counts \((0,1,2)\). Therefore its lower-residue party rounds up with probability \(1/5\), and its higher-residue party with probability \(4/5\). All outcomes select top-residue suffixes and have three surplus seats, proving both lotteries are feasible. They differ, completing sharpness.

## Verification

The standalone `verify_rank.py` enumerates every integer stratum-size pattern and surplus-seat count described above, builds the zero-one matrix from the displayed definition, checks exact rational rank, and reproduces each of the thirteen unit-determinant certificates. It also finds rank six for the seven-column \((2,2,2)\), \(k=3\) matrix and checks both six-party witness lotteries using exact fractions. Run `python verify_rank.py` with standard Python 3; no third-party packages are needed. The finite determinant table, not numerical sampling, supplies the exhaustive proof for the finite minimum-size assertion.

## Relationship to prior work

La Commare, Tucker-Foltz and Verdugo (2026), Proposition 4.2 and Section 4.2, establish an exact network-flow linear-program formulation for the **existence** of zero-envy quota-proportional apportionment. Their formulation implies the same nested-outcome representation used here. It does not give the full-column-rank certificates or assert that the probability distribution must be unique for every three-stratum instance up to five parties. The six-party nonuniqueness witness is closely related to transportation-polytope families previously studied in the three-pair setting; the new assertion is the **sharp universal uniqueness guarantee below that size**, not a claim to invent the general flow formulation or transportation-table method.

## Limitations

Uniqueness is conditional on feasibility. All three floor levels must be mutually distinct and all within-stratum fractional residues strictly ordered. Ties, more than three floor levels, and arbitrary non-quota allocations are not covered. The six-party witness shows failure of universal uniqueness, not that every six-party instance has multiple feasible lotteries. The result does not compare total expected envy when zero envy is unattainable. Although primary published results were inspected, an unindexed earlier exact uniqueness cutoff remains a priority risk; no independent scientific audit has been performed.

## References

Francesco La Commare, Jamie Tucker-Foltz, and Victor Verdugo, *Envy-Free Randomized Apportionment*, arXiv:2610.24217, version 1 publicly posted October 16, 2026, https://arxiv.org/pdf/2610.24217. See Sections 2.2 and 4.2, especially Proposition 4.2.
