# Generic deck-normalizer trichotomy for four-point cyclic prime covers

## Finding
For each odd prime \(p\), consider connected cyclic degree-\(p\) covers of the complex projective line totally ramified at exactly four distinct points with **generic** unordered cross-ratio (the four-point stabilizer in \(\operatorname{PGL}_2(\mathbb C)\) is exactly the Klein four group). Write \(H\cong C_p\) for the cyclic deck group and \(N=N_{\operatorname{Aut}(C)}(H)\) for its normalizer in the full automorphism group. The genus of the source curve is \(p-1\). Here \(D_p\) denotes the dihedral group of order \(2p\).

The four local monodromy exponents \(a_i\in\mathbb F_p^\times\) sum to zero. They are considered up to simultaneous nonzero scalar multiplication and reordering, as in the classical classification of cyclic actions. There are precisely three generic deck-normalizer types:

1. If the multiset is \(\{a,a,-a,-a\}\), then \(N\cong D_p\times C_2\). Exactly **one** topological class has this pattern.
2. If it is \(\{a,-a,b,-b\}\) with \(b\not\in\{a,-a\}\), then \(N\cong D_p\). Exactly \(\lfloor(p-1)/4\rfloor\) topological classes have this pattern.
3. All remaining exponent multisets give \(N\cong C_p\).

For \(p\ge5\), the previously known total number of action classes is
\[
N_p=\frac{p^2+6p+5+12\mathbf 1_{p\equiv1\pmod4}}{24}.
\]
Thus the third type occurs for exactly \(N_p-1-\lfloor(p-1)/4\rfloor\) classes. For \(p=3\), the only class is of the first type. **The formula for total \(N_p\) is from Broughton--Wootton (2007), not a new result.** The contribution here is the exact geometry and counts of the three generic deck-normalizer strata.

## Assumptions and scope
The base field is \(\mathbb C\); the prime \(p\) is odd. All four branch points have ramification index exactly \(p\). The branch configuration has stabilizer precisely \(V_4\), which holds outside the finite harmonic/equianharmonic cross-ratio exceptions. The result classifies normalizers of the marked deck group, **not** arbitrary automorphisms of the covering curve. Counts are of topological classes of cyclic actions, not individual curves or isomorphism classes within a varying cross-ratio family.

## Proof
**1. Branch monodromy.** The orbifold fundamental group of the four-punctured projective line has generators around the punctures with product one. Its epimorphisms onto \(C_p\), requiring nonzero images of every local generator, correspond to \((a_1,a_2,a_3,a_4)\in(\mathbb F_p^\times)^4\) with \(\sum_i a_i=0\). Deck-group automorphisms scale all entries, and mapping-class changes permute them because the target group is abelian.

**2. Lifting criterion.** For a generic unordered four-point set, the base Möbius stabilizer is \(V_4\), consisting of the identity and the three double transpositions. A base permutation \(\pi\) lifts to an automorphism normalizing \(H\) exactly when \(a_{\pi(i)}=\lambda a_i\) holds for every \(i\) and some \(\lambda\in\mathbb F_p^\times\). Necessity follows by conjugating monodromy. For sufficiency choose a Kummer presentation \(y^p=F(x)\) whose valuations at the four branch points represent the exponents. The quotient of the pulled-back Kummer function by \(F(x)^\lambda\) has every valuation divisible by \(p\). Since \(\operatorname{Pic}^0(\mathbb P^1)=0\) and \(\mathbb C\) contains all \(p\)-th roots, that quotient is a \(p\)-th power in \(\mathbb C(x)\). Its root supplies a lift.

**3. Classifying the lifted double transpositions.** For a double transposition \(\pi\), the relation applied twice forces \(\lambda^2=1\); as \(p\) is odd, \(\lambda=\pm1\). For \(\lambda=1\), entries on both transposed pairs are equal: the sum-zero condition forces \(\{a,a,-a,-a\}\). For \(\lambda=-1\), both pairs have opposite entries, forcing \(\{a,-a,b,-b\}\). When the two opposite pairs coincide (\(b=\pm a\)), the three nontrivial elements of \(V_4\) lift: one with conjugation action \(+1\) on \(H\) and two with action \(-1\). When they do not coincide, exactly one nonidentity element of \(V_4\) lifts, acting by inversion. For any other monodromy multiset, no nonidentity base symmetry lifts.

**4. Group identification.** Reduction to the base yields an exact sequence \(1\to H\to N\to K\to1\) where \(K\) is respectively \(V_4\), \(C_2\) or trivial. As \(p\) is odd and \(|K|\) divides four, Schur--Zassenhaus gives a complement. The conjugation actions of \(K\) on \(H\) described above identify the semidirect products as \(D_p\times C_2\), \(D_p\) and \(C_p\), respectively.

**5. Counting the nontrivial strata.** An unordered pair \(\{\pm a\}\) is an element of \(A=\mathbb F_p^\times/\{\pm1\}\), a cyclic group of order \(m=(p-1)/2\). A balanced four-exponent multiset \(\{\pm a,\pm b\}\), up to simultaneous scaling and swapping pairs, is specified by the ratio \(d=b/a\) in \(A\), modulo inversion \(d\sim d^{-1}\). An involution on the cyclic group of size \(m\) has exactly \(\lfloor m/2\rfloor+1\) inversion orbits. One orbit, the identity ratio, gives the repeated opposite-pair pattern; the other \(\lfloor m/2\rfloor=\lfloor(p-1)/4\rfloor\) orbits give \(D_p\). The number of remaining actions follows by subtracting these classes from the independently published total \(N_p\).

## Verification
The standalone file `verify.py` enumerates exact \(\mathbb F_p\) monodromy classes and tests the liftability of all three double transpositions. For every odd prime \(3\le p\le41\) it reproduces the normalizer-type counts. This is a bounded consistency check; the statements for all odd primes follow from the proofs above. Run using `python3 verify.py` with no third-party dependencies.

## Relationship to prior work
Disney-Hogg and Zuev (arXiv:2610.21981v1, October 15, 2026) study the topological-action classification using monodromy vectors and computational tabulation; their work motivates a geometric stratification by additional automorphisms. Broughton and Wootton, *Finite abelian subgroups of the mapping class group*, Algebraic & Geometric Topology 7 (2007), Table 10, **already calculate the total** \(N_p\), and their group-action orbit methodology supplies general ingredients. The result here is the classification and cardinality of the **generic normalizer group types**, not a recount of their total. Broughton's subsequent algorithmic account of prime cyclic actions likewise tabulates classes. Kallel--Sjerve's complete three-branch-point automorphism calculations concern a different branch-number regime.

## Limitations
The conclusion does not classify full automorphism groups, normalizers at exceptional harmonic or equianharmonic branch cross-ratios, or automorphisms that conjugate the deck subgroup to a different subgroup. While no published statement of the exact three-stratum generic normalizer counts was found in the inspected sources, the lifting tools and orbit counts are classical; an earlier equivalent or immediately implicit computation remains a material priority risk. The source's numerical classification is not an independent proof of novelty.

## References
1. L. Disney-Hogg and M. Zuev, *Deep Learning of Topological Equivalence Classes*, arXiv:2610.21981v1 (2026), https://arxiv.org/abs/2610.21981.
2. S. A. Broughton and A. Wootton, *Finite abelian subgroups of the mapping class group*, Algebraic & Geometric Topology **7** (2007), 1651--1697, Table 10, https://msp.org/agt/2007/7-4/agt-v7-n4-p02-s.pdf.
3. S. A. Broughton, *Topological and Hq Equivalence of Prime Cyclic p-gonal Actions on Riemann Surfaces* (2016), enumerative algorithm for cyclic actions.
4. S. Kallel and D. Sjerve, *On the group of automorphisms of cyclic covers of the Riemann sphere*, arXiv:math/0310053, three-point automorphism calculations.
