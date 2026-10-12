# Sharp seven-vertex threshold for variance reversals in incidence-based species accumulation

## Finding

Let a community consist of \(h\ge1\) sites and \(s\ge1\) distinct species, represented by a binary \(s\times h\) incidence matrix without zero rows or columns. Uniformly choose \(k\) of the \(h\) sites without replacement; let \(R_k\) denote the number of species present in at least one chosen site. Compare two communities having identical \(h\), \(s\), and multisets of species occupancies (row sums). They consequently have the same expected richness for every \(k\).

A **strict variance reversal** means that at two distinct sample depths \(1\le k<\ell<h\) the communities' population variances \(\operatorname{Var}(R_k)\) and \(\operatorname{Var}(R_\ell)\) have opposite strict orderings.

**Theorem.** Strict variance reversal is impossible whenever \(h+s\le6\), and possible when \(h+s=7\). At this sharp boundary, all reversing pairs, up to independent relabeling of sites and species within each community and exchange of the two communities, are exactly the four pairs in the following table. A row mask \(m\) encodes occupancy of site \(j\) by bit \(2^{j-1}\); parentheses list the masks for all species.

| Sites \(h\) | Occupancy multiset | Community A masks | Community B masks |
| --- | --- | --- | --- |
| \(3\) | \((1,1,2,2)\) | `(1,1,6,6)` | `(1,2,3,5)` |
| \(3\) | \((1,1,2,2)\) | `(1,1,6,6)` | `(1,2,5,5)` |
| \(3\) | \((1,1,2,3)\) | `(1,1,6,7)` | `(1,2,3,7)` |
| \(4\) | \((2,2,2)\) | `(3,3,12)` | `(3,5,9)` |

For both first two pairs, the variances \((V_A(1),V_B(1);V_A(2),V_B(2))\) are \((0,2/3;8/9,2/9)\). For the third pair they are \((2/9,8/9;8/9,2/9)\). For the fourth pair they are \((1/4,3/4;7/12,1/4)\); both variances vanish at sampling depth \(3\). All inequalities are strict as required at depths \(1\) and \(2\).

A further structural statement holds for **all** three-site communities, regardless of species count: if \(c_j\) is richness at site \(j\), and \(e_j\) is the number of species occurring only at site \(j\), then
\[
\operatorname{Var}(R_1)=\frac13\sum_{j=1}^3c_j^2-\left(\frac13\sum_{j=1}^3c_j\right)^2,\qquad
\operatorname{Var}(R_2)=\frac13\sum_{j=1}^3e_j^2-\left(\frac13\sum_{j=1}^3e_j\right)^2.
\]
For communities having a common occupancy multiset, a strict reversal therefore occurs **if and only if** their differences in \(\sum c_j^2\) and \(\sum e_j^2\) have opposite nonzero signs. This provides a direct structural diagnostic, independent of numerical simulation.

## Assumptions and scope

All sites and species are represented in the incidence table; different species are permitted to occupy identical sets of sites. Sites are sampled uniformly as an unordered \(k\)-subset of the fixed finite site collection, not as independent draws with replacement. Variance is the population variance over all \(\binom hk\) equally likely site subsets. The two incidence tables may be independently relabeled, because only their respective richness laws are compared; they are not required to embed in a jointly labeled landscape. Occupancy frequencies (row-sum multisets) are held fixed between the two communities. The classification counts pair-orbits, not labeled pairs.

## Proof

Let \(A_i\subseteq[h]\) be the nonempty set of sites containing species \(i\). For \(1\le k\le h\) set
\[
q_i(k)=\frac{\binom{h-|A_i|}{k}}{\binom hk},\qquad
q_{ij}(k)=\frac{\binom{h-|A_i\cup A_j|}{k}}{\binom hk},
\]
where a binomial coefficient with upper argument smaller than the nonnegative lower argument is zero. Writing \(I_i\) for the indicator that sampled sites contain species \(i\), we have \(R_k=\sum_i I_i\), \(\mathbb E I_i=1-q_i\), and \(\mathbb E(I_iI_j)=1-q_i-q_j+q_{ij}\). Hence
\[
\mathbb E R_k=\sum_i(1-q_i(k)),\qquad
\operatorname{Var}(R_k)=\sum_iq_i(k)(1-q_i(k))+
2\sum_{i<j}\left(q_{ij}(k)-q_i(k)q_j(k)\right).
\]
The mean is determined by the occupancy multiset. For a fixed multiset, the only part of the variance that changes with the incidence arrangement is the sum of the joint-absence terms \(q_{ij}\). This identity is a specialization of the established sample-based accumulation variance formula; it is not claimed as a new result.

If there is only one or two sites, there cannot be two distinct interior sample depths. With only one species, the richness variance is fixed by its occupancy. With two species and a common occupancy multiset, the difference between two communities' variances at depth \(k\) is twice the difference between their joint-absence probabilities, which are each \(\binom{h-u}{k}/\binom hk\), with \(u=|A_1\cup A_2|\). Since this is nonincreasing in \(u\) for every \(k\), its ordering cannot reverse. Thus no strict reversal occurs for at most two species at any number of sites.

Next suppose \(h=3\). Let \(t_r\) be the number of species occupying exactly \(r\) sites, let \(e_j\) count species exclusive to site \(j\), and let \(b_j\) count species occupying exactly the two sites other than \(j\). Then
\[
c_j=e_j+t_2-b_j+t_3,\qquad \sum_j e_j=t_1,\quad\sum_jb_j=t_2.
\]
The one-site richness outcomes are precisely \((c_1,c_2,c_3)\). The two-site sample that omits site \(j\) observes exactly \(s-e_j\) species, so its three richness outcomes are \((s-e_1,s-e_2,s-e_3)\). These observations yield the stated variance identities and sign criterion for any \(s\).

For \(h=3\) and \(s\le3\), if \(t_1\le1\), the sum \(\sum e_j^2=t_1\) is fixed between communities, so their two-site variances tie. If \(t_1\ge2\) but \(t_2=0\), then \(c_j=e_j+t_3\); the two variance comparisons have the same sign or tie. The only remaining degree-count case is \((t_1,t_2,t_3)=(2,1,0)\). Requiring every site to contain a species forces the one-site richness multiset \((2,1,1)\): whether the singleton species share a site or occupy two sites, the two-site species covers exactly the sites needed to avoid an empty column. Thus the one-site variances tie. This proves the required three-site lower bound; together with the preceding cases, every instance satisfying \(h+s\le6\) is excluded.

To classify the sharp boundary \(h+s=7\), the only dimensions not already excluded are \((h,s)=(3,4)\) and \((4,3)\). For the former, the structural sign criterion above first restricts reversal to the row-occupancy profiles \((1,1,2,2)\) and \((1,1,2,3)\). The site-relabeling orbits for these two profiles, with their values of \((\sum c_j^2,\sum e_j^2)\), are:

| Profile | Canonical row masks | Squared-sum pair |
| --- | --- | --- |
| \((1,1,2,2)\) | `(1,1,3,5)` | \((18,4)\) |
| \((1,1,2,2)\) | `(1,1,3,6)` | \((14,4)\) |
| \((1,1,2,2)\) | `(1,1,6,6)` | \((12,4)\) |
| \((1,1,2,2)\) | `(1,2,3,5)` | \((14,2)\) |
| \((1,1,2,2)\) | `(1,2,5,5)` | \((14,2)\) |
| \((1,1,2,2)\) | `(1,2,5,6)` | \((12,2)\) |
| \((1,1,2,3)\) | `(1,1,3,7)` | \((21,4)\) |
| \((1,1,2,3)\) | `(1,1,6,7)` | \((17,4)\) |
| \((1,1,2,3)\) | `(1,2,3,7)` | \((19,2)\) |
| \((1,1,2,3)\) | `(1,2,5,7)` | \((17,2)\) |

Comparing the two squared sums leaves precisely the first three reversing pair-orbits in the theorem. To see that no unlisted occupancy profile can reverse, observe that \(t_1\le1\) fixes \(\sum e_j^2\), \(t_2=0\) preserves the ordering, and for \((t_1,t_2,t_3)=(3,1,0)\) the possible \(\sum e_j^2\) values \(9,5,3\) are accompanied respectively by \(\sum c_j^2\) values \(11\), either \(9\) or \(11\), and \(9\). These cannot yield opposite signs. The only other profiles are already excluded by \(s=4\) and positive occupancy.

For \((h,s)=(4,3)\), a complete finite classification uses the following exhaustive construction. Generate all multisets of three nonzero four-bit row masks whose bitwise union is the all-ones mask; these are exactly all incidence matrices up to species relabeling. Apply each of the \(4!\) permutations of site labels and retain the lexicographically smallest sorted row-mask tuple. There are \(400\) raw sorted-row representations and exactly \(42\) canonical site-and-species relabeling orbits. For each pair of orbits having an equal occupancy multiset, evaluate the three exact variances by enumerating all \(\binom4k\) site subsets, for \(k=1,2,3\). This yields exactly one reversing pair-orbit, `(3,3,12)` versus `(3,5,9)`, both having species occupancy profile \((2,2,2)\). Among the three graph shapes for that profile, the remaining simple path has variance vector \((1/4,1/4,0)\), so it makes no strict reversal with either graph.

This finite enumeration is a complete proof because each admissible incidence table corresponds to exactly one generated multiset, each relabeling lies in the explicitly iterated finite permutation group, and every permitted pair is tested within its exact occupancy-profile class. The standalone source file `verify.py` implements these bounds with exact fractions and independently checks every resulting moment using the joint-absence formula. It also enumerates all smaller admissible dimension pairs as a redundant boundary check. For \((3,4)\) it finds \(168\) raw multisets, \(42\) orbits and three reversing pair-orbits; for \((4,3)\), \(400\) raw multisets, \(42\) orbits and one reversing pair-orbit. This completes the classification.

## Verification

Run `python3 verify.py` from the directory containing the standalone verifier. It uses only Python's standard library, computes exact rational means and variances both by direct site-subset enumeration and by the covariances above, and independently confirms the complete sharp-boundary classification. Its successful output is:

```text
VERIFY_OK smaller_shape_pairs_tested=15 small_communities_34=42 small_communities_43=42 minimal_pair_orbits=4
```

The enumeration is exhaustive for the finite classification at the sharp boundary; it is not used to assert a theorem about arbitrary larger habitat counts. All infinite-dimensional lower-bound cases needed for sharp minimality are handled by the structural arguments above.

## Relationship to prior work

Ugland, Gray and Ellingsen (2003), especially Appendix I, derive general conditional expectation and variance formulas for accumulation in subsets of sites, including species covariance. Colwell, Mao and Chang (2004) derive incidence-based rarefaction estimators and present two incidence matrices with the same occupancy-count spectrum but distinct patchiness; their Table 2 already demonstrates that the full arrangement is not determined by the mean curve. Neither inspected work states the sharp seven-incidence-vertex variance-order reversal boundary or its four complete minimal pair-orbits. General covariance formulas certainly permit calculation of all examples after the fact; the contribution here is the sharp minimum, the all-three-site variance-order diagnostic and the exhaustive classification at the minimum, not the underlying expectation or variance identities.

## Limitations

The statement concerns deterministic binary incidence inventories sampled uniformly without replacement. It does not address random site occupancy models, observation error, sampling unequal sites with differing effort, or confidence intervals for an estimated population mean. Species may have identical occupied-site sets. For larger numbers of sites or species, the four-pair classification is not asserted to remain exhaustive. Although the inspected references do not contain this minimal classification, an unindexed stronger combinatorial result could overlap. Independent review has not been performed.

## References

1. Ugland, K. I., Gray, J. S., and Ellingsen, K. E. (2003). *The species–accumulation curve and estimation of species richness*. Journal of Animal Ecology 72, 888–897. First public online date 2003-08-15. DOI: https://doi.org/10.1046/j.1365-2656.2003.00748.x .
2. Colwell, R. K., Mao, C. X., and Chang, J. (2004). *Interpolating, extrapolating, and comparing incidence-based species accumulation curves*. Ecology 85, 2717–2727. DOI: https://doi.org/10.1890/03-0557 . Author-hosted full text: https://www.robertkcolwell.org/publications/7532.pdf .
