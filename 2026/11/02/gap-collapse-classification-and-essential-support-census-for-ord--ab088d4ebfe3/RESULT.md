# Gap-collapse classification and essential-support census for ordered atoms

## Finding

Let \(G=\operatorname{Aut}(\mathbb Q,<)\) be the group of increasing bijections of the rational order. For a finite set \(S=\{s_1<\cdots<s_k\}\subset\mathbb Q\), let \(G_S\) be its pointwise stabilizer. An equivalence relation \(E\subseteq\mathbb Q^2\) is **supported by** \(S\) if every element of \(G_S\) preserves \(E\). Write \(B_n\) for the Bell number, the number of partitions of an \(n\)-element set.

**Classification and census.** An \(S\)-supported equivalence relation is specified uniquely by choosing which of the \(k+1\) open gaps of \(\mathbb Q\setminus S\) are collapsed into single equivalence blocks, leaving every point of each other gap as a singleton; and then partitioning the \(k\) distinguished points jointly with the collapsed-gap blocks. Therefore the number of \(S\)-supported equivalence relations is

\[
F_k=\sum_{j=0}^{k+1}\binom{k+1}{j}B_{k+j}.
\]

The counts for \(k=0,1,2,3,4,5\) are \(2,10,114,2066,52922,1788850\), respectively. These numerical values occur already in OEIS A208782 for a different combinatorial interpretation; their values are **not** asserted to be new.

**Exact essential-support census.** Let \(H_k\) count those \(S\)-supported equivalence relations whose unique least finite support is exactly \(S\). Then

\[
H_k=\sum_{t=0}^{k}(-1)^{k-t}\binom{k}{t}F_t.
\]

The first six counts are \(2,8,96,1752,45304,1543808\). In particular the proportion of the \(S\)-supported relations for which every named point is essential tends to one. Quantitatively, for \(k\ge1\),

\[
0\le 1-\frac{H_k}{F_k}
\le k\frac{F_{k-1}}{F_k}
\le k\frac{B_{k-1}}{B_{k+1}}
=O\!\left(\frac{(\log k)^2}{k}\right).
\]

## Assumptions and scope

The carrier is the entire countable dense unbounded linear order \((\mathbb Q,<)\). Support means invariance under all order automorphisms fixing the specified finite rational parameters *pointwise*, not finite permutation support, not invariance under order-reversing bijections, and not a statement about arbitrary equivalence relations lacking finite support. The given set \(S\) is fixed and ordered, while equivalence classes themselves are unlabelled. The case \(k=0\) is included. The uniform distribution in the proportion statement is over the finite set of all relations supported by that fixed \(S\).

The relevant MSC2020 subject is finite-support structures in set theory and nominal mathematics (03E25). The formula is an exact classification of all equivalence relations under this specified symmetry, not a classification of arbitrary binary relations.

## Proof

**Step 1 (orbits and gap dichotomy).** The complement of \(S\) is the disjoint union of \(k+1\) nonempty convex intervals (the exterior intervals are unbounded). The restriction of \(G_S\) to each such interval is the full increasing automorphism group of a copy of \((\mathbb Q,<)\), and these actions can be chosen independently. In particular, the group acts transitively on each interval; on ordered distinct pairs inside one interval it has precisely the two orientations, and it acts transitively on pairs taken from two different intervals, or from one interval and one named point.

Fix a gap \(I\). If two distinct points of \(I\) are \(E\)-equivalent, transitivity of the group on ordered increasing pairs, together with symmetry of \(E\), implies that every pair of points in \(I\) is \(E\)-equivalent. If no distinct pair is equivalent, the restriction of \(E\) to \(I\) is equality. Furthermore, if some \(x\in I\) is \(E\)-equivalent to \(y\notin I\), then independent transitivity on the \(I\) coordinate forces every \(x'\in I\) to satisfy \(x' E y\). Therefore the entire gap is a single equivalence class internally. Thus every gap is of exactly one of two types: (i) *discrete*, all its points singleton classes and unrelated to anything outside that gap, or (ii) *collapsed*, all its points form one block, possibly merged with named points or other collapsed gaps.

**Step 2 (complete classification).** Select the set \(J\) of collapsed gaps. There is no additional freedom for a discrete gap. Since the \(k\) named points and the \(|J|\) collapsed gaps are each indivisible units for \(E\), an arbitrary set partition of these \(k+|J|\) distinguishable units determines precisely the remaining equivalence classes. Conversely, every such partition produces an equivalence relation preserved by \(G_S\), since automorphisms preserve the distinguished points and each gap setwise. Both constructions are inverse to each other. With \(|J|=j\), there are \(\binom{k+1}{j}B_{k+j}\) choices, proving the formula for \(F_k\), including \(k=0\).

**Step 3 (least-support count).** A standard least-support theorem for the total-order atom symmetry says every finitely supported element, including a supported binary relation regarded as an element of the powerset of ordered atom pairs, has a unique least finite support. The theorem is recorded for the total-order symmetry in Bojańczyk's *Nominal Monoids*, Section 2, with original references therein. For each \(T\subseteq S\), the number of relations supported by \(T\) is \(F_{|T|}\), since the order type of \(T\) alone determines this count by Step 2. A relation supported by \(S\) fails to have least support \(S\) precisely when it is also supported by \(S\setminus\{s_i\}\) for at least one \(s_i\). By uniqueness of least supports, an intersection of the removal events indexed by \(U\subseteq S\) is the set of relations supported by \(S\setminus U\). Inclusion-exclusion over the \(k\) named points gives

\[
H_k=\sum_{U\subseteq S}(-1)^{|U|}F_{k-|U|}
=\sum_{t=0}^{k}(-1)^{k-t}\binom{k}{t}F_t.
\]

This proof of exact essential-support enumeration depends on the named least-support theorem; the finite checks below are not substitutes for it.

**Step 4 (uniform probability).** A union bound on the same removal events immediately gives \(0\le F_k-H_k\le kF_{k-1}\). The Bell sequence is log-convex: Dobinski's moment representation \(B_n=e^{-1}\sum_{m=0}^{\infty}m^n/m!\) and Cauchy–Schwarz imply \(B_n^2\le B_{n-1}B_{n+1}\). By Pascal's identity,

\[
F_k=\sum_{j=0}^{k}\binom{k}{j}\bigl(B_{k+j}+B_{k+j+1}\bigr),
\qquad
F_{k-1}=\sum_{j=0}^{k}\binom{k}{j}B_{k-1+j}.
\]

Log-convexity gives \(B_{k+j+1}/B_{k+j-1}\ge B_{k+1}/B_{k-1}\), so termwise comparison yields \(F_k\ge (B_{k+1}/B_{k-1})F_{k-1}\). The known Bell-ratio estimate \(B_{n+1}/B_n\sim n/W(n)\), where \(W\) denotes the positive Lambert function, gives \(kB_{k-1}/B_{k+1}=O((\log k)^2/k)\to0\). This proves the probability claim.

## Verification

The standalone `checker.py` directly enumerates **all set partitions** of a finite ordered proxy with two generic points in each gap and one point for every distinguished parameter. It selects those equivalence relations invariant under swapping the two proxy points independently within each gap; these counts for \(k=0,1,2,3\) are respectively \(2,10,114,2066\), matching the formula. Two proxy points suffice for these finite orbit checks because an invariant equivalence relation can distinguish only diagonal from off-diagonal pairs inside a gap, and a gap's relations to other orbits are uniform. The independent enumerator does *not* prove that its finite proxy describes the rational order: that assertion is proved in Steps 1–2.

The checker also tests **essentiality** directly, by checking that each named point cannot be forgotten while preserving gap uniformity; its essential-support proxy counts for \(k=0,1,2,3\) are \(2,8,96,1752\). Finally it evaluates the Bell convolution and inclusion–exclusion formula through \(k=9\), and tests the elementary union-bound inequality against those exact values. Run with `python3 checker.py`; the expected terminal marker is `ALL_CHECKS_OK`. No external files, network or numerical approximations are needed by the checker.

## Relationship to prior work

Masters, *Logic of Sets with Atoms* (first publicly available November 25, 2025), develops permutation models of atoms and explicitly treats the ordered rational atom symmetry and finite supports. The inspected source discusses orbit-finite sets and parameter support; it does not give this equivalence-relation gap-collapse classification, the support counts, or the proportion theorem. Bojańczyk's *Nominal Monoids* (2013) develops total-order nominal symmetry and states least supports for this symmetry, which is used in Step 3; its inspected nominal-set and monoid results do not supply the stated binary-equivalence enumeration.

OEIS A208782 (Hardin, 2012) already lists the numerical sequence \(2,10,114,2066,\ldots\) with an array-coloring interpretation; neither those numeric values nor the fact that they occur is claimed as new. The present claim instead concerns their exact interpretation as supported equivalence relations, an explicit normal form, the count with essential named supports, and its asymptotic prevalence. Grunwald and Serafin (2024) provide prior Bell-ratio asymptotics used in Step 4.

## Limitations

Novelty is assessed against inspected sources and mathematical records, not independently established historical priority. Equivalent results might be present under the terminology of oligomorphic permutation groups, quantifier-free definable equivalence relations over dense linear orders, or partition species with marked points. In particular the underlying numeric sequence is known, so a stronger uninspected interpretation could subsume part of this theorem. The exact support formula uses the established least-support property of total-order atoms. Independent review has not been performed. The probability statement is asymptotic for fixed \(S\) of each size, and is not a claim about a canonical probability measure over all finitely supported relations with unbounded support size.

## References

1. J. Masters, *Logic of Sets with Atoms* (2025), arXiv:2512.02041, https://arxiv.org/abs/2512.02041. First public submission November 25, 2025.
2. M. Bojańczyk, *Nominal Monoids*, Theory of Computing Systems 53 (2013), 194–222, https://doi.org/10.1007/s00224-013-9464-1.
3. J. Grunwald and G. Serafin, *Explicit bounds for Bell numbers and their ratios* (2024), arXiv:2408.14182, https://arxiv.org/abs/2408.14182.
4. R. H. Hardin, OEIS A208782 (2012), https://oeis.org/A208782.
