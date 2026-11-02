# Ternary-positive points classify toric rank-two positroids, with an exact dimension polynomial

## Finding
For every integer \(n\ge2\), the support of a nonnegative ternary Plücker vector defines a canonical bijection
\[
\operatorname{Gr}^{\ge0}(2,n)(\mathbb F_3)\ \longleftrightarrow\ \{\Pi_M\subseteq\operatorname{Gr}_{\mathbb C}(2,n): \Pi_M\text{ is a toric positroid variety}\}.
\]
The right side counts **distinct labeled embedded subvarieties**, not abstract isomorphism classes. If \(d\) is complex dimension, its complete enumerator is
\[
T_n(z)=\sum_{\Pi_M\text{ toric}}z^{\dim\Pi_M}
=\binom n2(1+z)^{n-2}+\binom n3z^2(1+z)^{n-3},
\]
where for \(n=2\) the second summand is defined to be zero. Thus
\[
\#\{\Pi_M\text{ toric}\}=\frac{n(n-1)(n+4)}3\,2^{n-4}.
\]
The last, **unrefined** count is not new: it coincides with Machacek's published count of ternary totally nonnegative planes and OEIS A001794. The claims advanced here are the geometric support correspondence and the dimension-refined count.

## Assumptions and scope
Work over \(\mathbb C\) for positroid varieties, and over \(\mathbb F_3\) for finite-field points. The nonnegative elements of \(\mathbb F_3\) are its squares \(\{0,1\}\), as in Machacek. A ternary plane is called nonnegative when some representative of its Plücker point has every ordered Plücker coordinate in \(\{0,1\}\). A rank-two positroid on labeled ground set \([n]\) may have loops and parallel elements. Its variety \(\Pi_M\) is the standard closure of the corresponding open positroid stratum. The support map sends the ternary Plücker point to the set of pairs with coordinate \(1\). The resulting matroid, and hence variety, is independent of representatives. In rank two, the nonloop set has size \(m\ge2\); it is partitioned into \(c\ge2\) parallel classes. All assertions allow arbitrary loops.

## Proof
**1. Classification and toricity.** A rank-two matroid is determined by its loop set and partition of its nonloops into parallel classes. The cyclic-interval criterion for rank-two positroids says that each parallel class is a consecutive block in the induced cyclic order on nonloops (Mohammadi–Zaffalon, Definition 3.8 and Proposition 3.9). A rank-two matroid is regular precisely when it has at most three parallel classes: with four classes, a choice of four representatives yields the nonbinary uniform minor \(U_{2,4}\); with two or three classes, the matroid is obtained from \(U_{2,2}\) or \(U_{2,3}\) by loops and parallel extensions, operations preserving regularity. McNeill's toricity theorem says a positroid variety is toric if and only if the positroid is regular. Thus the toric cases are exactly \(c\in\{2,3\}\).

**2. Map from ternary planes to toric positroids.** Normalize a nonnegative ternary Plücker vector so its entries \(p_{ij}\) are exactly \(0\) or \(1\). For any \(i<j<k<l\), the rank-two Plücker relation is
\[
p_{ij}p_{kl}-p_{ik}p_{jl}+p_{il}p_{jk}=0\quad\text{in }\mathbb F_3.
\]
The same expression on the integral zero-one lifts lies between \(-1\) and \(2\). Its only multiple of \(3\) is zero. Consequently all integral quadratic Plücker relations vanish. They define the Plücker-embedded Grassmannian in rank two, so the lift gives a real totally nonnegative plane and its support is a positroid. Four nonparallel classes are impossible: choosing one element from each would make all six coordinates one and give \(1-1+1=1\ne0\) in \(\mathbb F_3\). Thus the support positroid has \(c\in\{2,3\}\), and its complex variety is toric by step 1. Two ternary points with equal support have identical normalized zero-one Plücker coordinates, hence coincide, proving injectivity.

**3. Surjectivity.** Given a toric rank-two positroid, cyclically order its nonzero columns into its two or three parallel blocks. If there are two blocks use column directions \((1,0),(0,1)\). For three use \((1,0),(1,1),(0,1)\). Give every column in each block its indicated direction and give loops zero columns. Every nonzero ordered minor is \(1\), so this defines a nonnegative ternary point. A cyclic shift of an ordered rank-two matrix with sign reversal of the wrapped column preserves each ordered maximal minor's nonnegative value; applying inverse signed cyclic shifts transports the construction to the original labeled arrangement. The support is exactly the required positroid. This proves surjectivity and canonicity of the support bijection, although the displayed matrix is merely an existence construction.

**4. Exact dimension counts.** For a chosen nonloop support of size \(m\), placing cuts at \(c\) of the \(m\) circular gaps specifies exactly one partition into \(c\) cyclic consecutive nonempty parallel classes, and every such partition arises uniquely. Therefore there are \(\binom nm\binom mc\) rank-two positroids with parameters \((m,c)\). The dimension of the positroid variety is \(m+c-4\) (Mohammadi–Zaffalon, Proposition 4.1), so
\[
T_n(z)=\sum_{m=2}^n\binom nm\left[\binom m2 z^{m-2}+\binom m3 z^{m-1}\right].
\]
Applying \(\binom nm\binom mc=\binom nc\binom{n-c}{m-c}\) separately for \(c=2,3\) proves the stated polynomial. Its coefficient of \(z^d\) is
\[
\binom n2\binom{n-2}d+\binom n3\binom{n-3}{d-2},
\]
with out-of-range binomial coefficients interpreted as zero. Substituting \(z=1\) gives the stated total.

For comparison, counting all rank-two positroids (without toricity) by \(c=2,\ldots,m\) gives
\[
P_n(1)=3^n-(n+2)2^{n-1}.
\]
Hence, as \(n\to\infty\), their toric proportion satisfies
\[
\frac{T_n(1)}{P_n(1)}\sim\frac{n^3}{48}\left(\frac23\right)^n.
\]
The dimension refinement is thus an exact geometric decomposition of a previously known finite-field count, while the cross-characteristic support map explains why the two sets have the same cardinality.

## Verification
A standalone, Python-standard-library script `verify.py` independently enumerates cyclic interval set partitions and all reduced-row-echelon ternary two-planes through \(n=7\). It checks integral lifts of all rank-two Plücker relations, rank-two supports, parallel-class counts and the predicted dimension histograms; it also checks the counting identities through \(n=10\). Executing the actual embedded script prints `VERIFY_OK`. Sample polynomials are \(T_4(z)=6+12z+10z^2+4z^3\) and \(T_5(z)=10+30z+40z^2+30z^3+10z^4\). These finite checks do not prove the all-\(n\) result; the preceding symbolic and geometric argument does.

## Relationship to prior work
McNeill (2026, Theorem 1) proves the general classification of toric positroid varieties by regularity. Mohammadi–Zaffalon (2022/2025, Section 3 and Proposition 4.1) supply the rank-two cyclic-interval description and dimensions. Machacek (2024/2025, Theorem 5.3) already evaluates the ternary nonnegative Grassmannian's unrefined cardinality, equal to the \(z=1\) specialization above, so this numerical sequence is explicitly **not** claimed as original. Łukowski–Parisi–Williams give a complementary forest criterion for toric positroid varieties. The additional statement is the explicit support bijection and dimension-wise geometric census; equivalence under another formulation is a residual priority risk.

## Limitations
This classification is specific to rank two and \(\mathbb F_3\). It counts embedded, labeled varieties, not abstract-isomorphism orbits, and does not compute their singularities, intersection cohomology or Ehrhart data. The earlier unrefined sequence is known. Historical priority of the correspondence and dimension refinement is subject to specialist literature comparison; no independent mathematical audit has occurred.

## References
1. Avery McNeill, *There are no unexpected toric positroid varieties*, arXiv:2610.35914v1 (first public 2026-10-07), Theorem 1.
2. Fatemeh Mohammadi and Francesca Zaffalon, *Computing positroid cells in the Grassmannian of lines, their boundaries and their intersections*, arXiv:2206.14001v3, Definition 3.8, Proposition 3.9 and Proposition 4.1.
3. John Machacek, *A finite totally nonnegative Grassmannian*, arXiv:2410.06177v2, Theorem 5.3 and Section 6.3.
4. Tomasz Łukowski, Matteo Parisi and Lauren Williams, *The positive tropical Grassmannian, the hypersimplex, and the m=2 amplituhedron*, IMRN (2023), Propositions 3.15–3.16.
5. OEIS A001794, existing unrefined integer sequence.
