# An exact all-modulus rank-defect census for the Fourier rows \(\{0,1,3,4\}\)

## Finding
For every integer \(N\ge5\), let \(F_N=(\zeta_N^{rc})_{r,c\in\mathbb Z/N\mathbb Z}\), with \(\zeta_N=e^{2\pi i/N}\). Retain exactly the four rows \(M=\{0,1,3,4\}\). For every four-element column set \(C\), its minor \(F_N[M,C]\) has rank either \(3\) or \(4\). The number \(D(N)\) of rank-three minors is
\[
\boxed{D(N)=\mathbf1_{2\mid N}\frac{N(N-2)}4
-\mathbf1_{4\mid N}\frac N4
+\mathbf1_{3\mid N}\frac{N(N-3)}3
-\mathbf1_{6\mid N}N
+\mathbf1_{30\mid N}2N.}
\]
In particular, the correction of exactly \(2N\) at multiples of \(30\) arises from two exceptional cyclic orbits that are neither antipodal-pair nor cube-root-coset configurations.

All singular column sets are exhausted by the following three (partly overlapping) families. We identify a column exponent \(c\) with its root \(x=\zeta_N^c\).

**Antipodal-inverse family.** When \(2\mid N\), \(C\) consists of four distinct roots \(\{u,-u,v,w\}\) with \(vw=u^2\). In exponent coordinates this means a pair \(\{a,a+N/2\}\) and two other columns \(b,c\) satisfying \(b+c\equiv2a\pmod N\).

**Ternary-coset family.** When \(3\mid N\), \(C\) contains the entire coset \(\{u,u\omega,u\omega^2\}\) of the subgroup of third roots, where \(\omega^3=1\) and \(\omega\ne1\); its fourth root is arbitrary outside this triple.

**Primitive-thirtieth-root family.** When \(30\mid N\), \(C\) is a global multiplicative translate of one of the two sets
\[
\{\zeta_{30}^j:j\in\{0,12,13,19\}\},\qquad
\{\zeta_{30}^j:j\in\{0,6,7,19\}\},
\]
with \(\zeta_{30}=e^{2\pi i/30}\). These are two disjoint free translation orbits, each of size \(N\), and are disjoint from the other two families.

## Assumptions and scope
The complex Fourier matrix is unnormalized; any nonzero common row/column normalization leaves the ranks unchanged. The four row indices are pairwise distinct because \(N\ge5\). Each minor is counted once for its unordered four-element set of distinct columns. The indicator \(\mathbf1_{d\mid N}\) is one if \(d\) divides \(N\), otherwise zero. The theorem concerns the fixed row pattern \(\{0,1,3,4\}\), not arbitrary four-row sets or principal minors.

## Proof
**1. Determinant and rank.** Set \(x_j=\zeta_N^{c_j}\) for the distinct selected columns. The generalized Vandermonde identity gives
\[
\det(x_j^{r})_{r\in\{0,1,3,4\},1\le j\le4}
=\pm\prod_{i<j}(x_j-x_i)\,e_2(x_1,x_2,x_3,x_4),
\qquad e_2=\sum_{i<j}x_ix_j.
\]
Since the Vandermonde factor is nonzero, the minor is singular exactly when its six pair-products sum to zero. Furthermore, any left-null vector gives a polynomial supported in degrees \(0,1,3,4\), vanishing at the four distinct \(x_j\). A nonzero polynomial of degree at most four with those four roots is a scalar multiple of \(\prod_j(z-x_j)\), so the left nullspace has dimension at most one. Thus every singular minor has rank exactly three.

**2. Exhaustion by minimal root relations.** The six pair-products are roots of unity, counted with multiplicity. Poonen and Rubinstein's classification of minimal vanishing sums through weight six (Theorem 3 and Table 1 of [1]) implies that every vanishing six-term sum is a disjoint sum of three opposite pairs, a disjoint sum of two equilateral triples, or the unique primitive weight-six relation up to rotation:
\[
\zeta_6+\zeta_6^{-1}+\zeta_5+\zeta_5^2+\zeta_5^3+\zeta_5^4=0.
\]
No other partition of weight six into positive minimal weights is possible, since these weights are \(2,3,5,6\).

For a decomposition into three opposite pairs, either two pair-products sharing a vertex are negatives—in which case the two other root vertices form an antipodal pair—or all three opposite pairings in the graph on four vertices pair disjoint edges. In the latter case, the equations \(x_1x_2=-x_3x_4\) and \(x_1x_3=-x_2x_4\) imply \((x_2/x_3)^2=1\). The roots are distinct, hence \(x_2=-x_3\). Thus every such relation contains an antipodal pair \(\{u,-u\}\). Substituting it into \(e_2\) gives \(e_2=u^2-vw\) up to sign, so the remaining roots obey \(vw=u^2\). Conversely this identity makes \(e_2\) vanish.

For a decomposition into two equilateral triples, partition the six edges of the complete graph on four vertices into two three-edge groups. If either group is a star or triangle, ratios of its edge-products imply that three of the original roots form a coset of the cube roots. Otherwise both groups are three-edge paths. Relabel so the first path has edges \(12,23,34\) and the second has \(13,14,24\). The first equilateral relation implies \(x_1/x_3\) and \(x_2/x_4\) are third roots, while the second implies \(x_3/x_4\) is a third root. All four roots would then occupy a single three-element coset, contradicting distinctness. Hence one group must be a star or triangle, establishing the ternary-coset family. Conversely, for \(u,u\omega,u\omega^2\) both the pair-product sum within the triple and the triple's sum vanish, so adjoining any fourth root leaves \(e_2=0\).

For the primitive weight-six case, represent the six pair-products up to common rotation by the exponent set
\[
S=\{5,25,6,12,18,24\}\pmod{30}.
\]
The products attached to each pair of opposite edges of the four-vertex graph all equal \(x_1x_2x_3x_4\). Consequently, the six exponents must admit a perfect matching into three pairs with the same sum modulo \(30\). A check of the \(15\) matchings gives the unique matching
\[
\{\{5,25\},\{6,24\},\{12,18\}\},
\]
whose three pair sums are zero modulo \(30\). Indeed, zero is the only pair-sum residue occurring at least three times among the fifteen unordered exponent pairs, and its occurrences are exactly these three pairs. Assigning these three paired edges to the opposite edge-pairs gives \(3!2^3=48\) labeled assignments. Reordering the four root vertices acts freely through a group of size \(4!=24\), leaving exactly two projective root configurations. Their normalized representatives are the displayed two thirtieth-root sets: their pair-product exponent multisets are respectively \(S+7\) and \(S+1\) modulo \(30\). The ratios of every pair of original roots are ratios of pair-products, hence are thirtieth roots. Since the primitive relation uses an element of exact order thirty relative to another, this case requires \(30\mid N\). The representatives are inequivalent under translation modulo \(30\); neither has an antipodal pair or a complete ternary coset. Each has trivial translation stabilizer, giving two disjoint orbits of size \(N\).

**3. Enumeration and overlaps.** There are \(N/2\) antipodal pairs. Fixing one pair \(\{u,-u\}\), the remaining unordered pairs \(\{v,w\}\) with \(vw=u^2\) number \((N-2)/2\). This counts \(N(N-2)/4\) configurations. A configuration is counted twice precisely when it has two antipodal pairs, forcing a translate of the four fourth-roots; these exist if \(4\mid N\) and number \(N/4\).

There are \(N/3\) ternary cosets; each admits any of \(N-3\) outside fourth roots, giving \(N(N-3)/3\) configurations, with no repetitions. A configuration lies in both these families exactly when it is a ternary coset together with the negative of one of its three members. Such configurations occur if \(6\mid N\), and there are \((N/3)\cdot3=N\). The primitive-thirtieth-root sets belong to neither family and contribute \(2N\) precisely for \(30\mid N\). Inclusion-exclusion yields the stated formula.

## Verification
The standalone `verify_defect_census.py` first verifies the formal determinant factorization in four integer-polynomial variables, then computes the cyclotomic polynomial \(\Phi_N\) from exact monic polynomial divisions and reduces the six pair-product sum modulo \(\Phi_N\), with integer arithmetic only. Independently of that algebraic zero test, it checks each four-column set against the three structural families. It exhaustively checked every four-column set for nineteen orders between \(5\) and \(60\), including the first primitive-six-term exception at \(N=30\) and its doubled order \(N=60\), as recorded in `verification_output.txt`. It also checks the unique perfect matching of \(S\), distinctness of the two exceptional orbits, and orbit stabilizers. The exhaustive finite checks do not prove the formula for all \(N\); the preceding classification and count do.

Representative total rank-three counts are \(D(10)=20\), \(D(12)=51\), \(D(15)=60\), \(D(30)=510\), and \(D(60)=2055\). The primitive-family contributions at the last two orders are respectively \(60\) and \(120\).

## Relationship to prior work
Matter, Fischer, Pesavento, and Pfetsch [2] consider exactly the same Schur factor \(e_2\) for the continuous four-sensor array \(\{0,1,3,4\}\). Their Example V.1 describes continuous ambiguity families corresponding to the decompositions \(2+2+2\) and \(3+3\), and tabulates normalized exceptional configurations for the primitive six-term relation. Those **continuous configurations and determinant factorization are prior work**, not new discoveries here. They do not state an all-cyclic-order count of distinct four-column singular minors, its exact overlaps, or the congruence-sensitive \(2N\) jump. The present result extracts an exhaustive finite cyclic classification and rank census, making the arithmetic dependence on \(N\) explicit.

Alexeev, Cahill, and Mixon [3] identify the singular order-ten submatrix with the same row indices and give general full-spark criteria; they do not count defects at arbitrary orders. A later published all-order full-spark criterion for this exact row pattern characterizes whether the count is zero, namely the condition \(\gcd(N,6)=1\), but does not determine its positive values. An exact census for the different row pattern \(\{0,1,2,4\}\) also does not imply this one. The Poonen–Rubinstein root-relation classification [1] supplies a previously established critical ingredient, not a newly proved root-of-unity theorem.

## Limitations
The formula concerns a fixed four-row pattern, and its novel content is the all-modulus **number and exact orbit decomposition of singular minors**, not the generalized Vandermonde identity or the existence of continuous ambiguities. The comparison with the continuous-array treatment is close: a previously unnoticed enumeration extracted from that paper could supersede the novelty claim. The proof uses the published classification of minimal vanishing root sums of weight at most six. No assertions concern arbitrary row selections, noisy numerical conditioning, or nonlinear inverse uniqueness.

## References
1. B. Poonen and M. Rubinstein, *The Number of Intersection Points Made by the Diagonals of a Regular Polygon*, arXiv:math/9508209 (1995), Theorem 3 and Table 1.
2. F. Matter, T. Fischer, M. Pesavento, and M. E. Pfetsch, *Ambiguities in Direction-of-Arrival Estimation with Linear Arrays*, arXiv:2110.10756 (first posted October 20, 2021), especially Example V.1 and Table II.
3. B. Alexeev, J. Cahill, and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (2011), especially the composite-order counterexample following Theorem 9.
4. *Exact full-spark criterion for the four-row Fourier pattern \(\{0,1,3,4\}\)*, publicly available research result (2026), distinguishing mere existence from rank-defect enumeration.
5. *Exact singular minors for the near-consecutive four-row harmonic frame*, publicly available research result (2026), concerning the different rows \(\{0,1,2,4\}\).
