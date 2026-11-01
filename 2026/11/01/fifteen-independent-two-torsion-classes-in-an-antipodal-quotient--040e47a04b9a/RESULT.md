# Fifteen independent two-torsion classes in an antipodal quotient of a simplicial double

## Finding
Let \(\mathcal O_6\) be the six-dimensional cross-polytope with vertices \(\{+1,-1,\ldots,+6,-6\}\). Its boundary complex \(X=\partial\mathcal O_6\) has as faces the subsets with at most one signed vertex from each coordinate pair. Form its simplicial double \(Y=D_2(X)\): vertices are unordered edges of \(X\), and collections of vertices of \(Y\) are simplices exactly when their edges in \(X\) are pairwise disjoint and their union is a face of \(X\).

Define the antipodal involution \(\tau\) on \(Y\) by replacing both signs in every signed edge. It acts freely on the geometric realization. Put \(Q=|Y|/\langle\tau\rangle\). Then the **complete reduced integral homology** of the quotient is

\[
\boxed{\widetilde H_i(Q;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{46}\oplus(\mathbb Z/2\mathbb Z)^{15},&i=1,\\
\mathbb Z^{195},&i=2,\\
0,&\text{otherwise}.
\end{cases}}
\]

In particular, a free involution of a space with torsion-free integral homology produces **fifteen independent order-two first-homology classes** in this canonical quotient. The ordinary nonequivariant homotopy type of the covering complex, \(Y\simeq\bigvee^{106}S^1\vee\bigvee^{405}S^2\), is already implied by the published vertex-inflation theorem and is cited only for comparison.

## Assumptions and scope
All spaces are finite CW realizations. The double means the disjoint-edge construction of Lesh, Schreiner and Wahl, **not** the classical two-color vertex inflation of the original cross-polytope boundary. The involution reverses every coordinate sign simultaneously. The quotient \(Q\) is treated as a \(\Delta\)-complex: distinct open cells may have the same set of orbit-vertices, so identifying it with the ordinary abstract simplicial complex on orbit-vertices would be wrong. Homology coefficients are \(\mathbb Z\) unless otherwise specified, and the action is on the geometric realization.

## Proof
**1. Free action and complete cell enumeration.** An edge of \(X\) is specified by an unordered coordinate pair \(\{a,b\}\subset[6]\) and independently assigned signs on those two coordinates. There are \(\binom62\cdot4=60\) signed edges. A simplex of \(Y\) is a matching of \(K_6\) together with independently chosen signs at all its coordinate endpoints. The numbers of matchings of sizes one, two and three are \(15,45,15\), respectively, so the numbers of nonempty simplices of \(Y\) in dimensions zero, one and two are \((60,720,960)\).

The involution maps a signed edge with signs \((\epsilon_a,\epsilon_b)\) to one with signs \((-\epsilon_a,-\epsilon_b)\). Each simplex of \(Y\) contains at most one signed edge for any given unordered coordinate pair. Therefore no nonempty simplex is carried to itself setwise: if it were, each of its uniquely indexed signed edges would have to equal its sign-reversed partner. Thus the geometric action is free, including in simplex interiors. Every simplex orbit has size two, and the quotient has exactly
\[
(f_0,f_1,f_2)=(30,360,480)
\]
open cells in its canonical \(\Delta\)-complex structure.

**2. Integral boundary matrices.** Order the fifteen underlying coordinate pairs lexicographically and order the four sign assignments within each pair. Orient any simplex by increasing underlying pair index. A global sign reversal leaves these pair indices unchanged, hence preserves the orientation of every simplex when taking its orbit.

Represent each cell orbit by the lexicographically smaller of the two signed simplices. For an oriented \(k\)-simplex orbit with representative \((e_0,\ldots,e_k)\), deleting position \(j\) contributes \((-1)^j\) to the orbit of \((e_0,\ldots,\widehat e_j,\ldots,e_k)\). These rules define exact integer cellular matrices
\[
\partial_1:\mathbb Z^{360}\longrightarrow\mathbb Z^{30},\qquad
\partial_2:\mathbb Z^{480}\longrightarrow\mathbb Z^{360}.
\]
The construction enumerates all signed matchings and all boundary incidences rather than relying on a precomputed table. It has exactly \(720\) nonzero incidences in \(\partial_1\) and \(1440\) in \(\partial_2\). Direct integral multiplication gives \(\partial_1\partial_2=0\). The quotient one-skeleton is connected, verified by traversing all 30 cell-vertices and 360 edge-cells; consequently \(\partial_1\) has rank 29 with unit nonzero invariant factors.

**3. Exact Smith factors.** Apply the following entirely integral elementary operation to the matrix \(A=\partial_2\). Whenever \(a_{ij}=\pm1\), use integer row and column operations to clear its row and column, and remove that unit diagonal block. The remaining matrix is its integer Schur complement, whose entry at remaining row \(k\), column \(\ell\) is
\[
 a'_{k\ell}=a_{k\ell}-a_{kj}a_{i\ell}/a_{ij}.
\]
Because the pivot is \(\pm1\), both operations are unimodular, so this changes neither the cokernel nor the remaining nonunit Smith factors. Select a pivot minimizing the product of the numbers of other nonzero entries in its row and column, breaking ties in the deterministic enumeration order supplied in `verify.py`. This algorithm makes **270 unit pivots**. The remaining integer matrix has 90 rows and 210 columns, and every one of its 240 nonzero entries is exactly \(+2\) or \(-2\).

Write this remaining matrix as \(2B\). The same exact unit-pivot procedure applied to \(B\) makes **15 further unit pivots**, leaving an all-zero \(75\)-by-\(195\) matrix. Since the row and column transformations are integral unimodular, applying the identical transformations to \(2B\) gives fifteen diagonal factors equal to two and no other nonzero factors. Thus the complete nonzero Smith invariant-factor list for \(\partial_2\) is
\[
\boxed{\underbrace{1,\ldots,1}_{270},\quad
\underbrace{2,\ldots,2}_{15}.}
\]
The attached standalone program constructs the specified matrices from first principles, executes every integer elementary operation and asserts the stated pivot counts, all residual entries, and complete zero residual. This is a finite exhaustive certificate; mod-two or rational ranks alone would not establish these exact integral factors.

**4. Homology.** Since the one-skeleton is connected, \(\ker\partial_1\) is free of rank \(360-29=331\) and a primitive direct summand of \(C_1(Q;\mathbb Z)\). Because \(\operatorname{im}\partial_2\subseteq\ker\partial_1\), the torsion invariant factors of \(H_1\) are the nonunit Smith factors of \(\partial_2\). Its free rank is \(331-(270+15)=46\), with exactly fifteen summands of order two. The complex is two-dimensional and \(\partial_2\) has rank 285, so \(H_2=\ker\partial_2\cong\mathbb Z^{480-285}=\mathbb Z^{195}\). The quotient is connected, so reduced zeroth homology vanishes, and higher chain groups are zero. Its Euler characteristic \(30-360+480=150\) agrees with \(1-46+195=150\).

**5. Comparison with the torsion-free cover.** The signed-edge description identifies \(Y\) with the uniform fourfold inflation of the ordinary matching complex \(\mathcal M(K_6)\). The latter collapses to a connected graph with 15 vertices and 30 edges, so \(\mathcal M(K_6)\simeq\bigvee^{16}S^1\). The established vertex-inflation wedge formula, using the three components of the link \(\mathcal M(K_4)\) and the empty links of maximal matchings, gives \(Y\simeq\bigvee^{106}S^1\vee\bigvee^{405}S^2\). This conclusion is an application of known work, not a new part of the present theorem. The quotient calculation above shows that the free geometric quotient of this torsion-free sphere wedge need not remain a sphere wedge.

## Verification
The self-contained `verify.py` uses only the Python standard library. It enumerates all 60 signed edges, all 720 signed two-edge matchings and all 960 signed perfect matchings. It checks that every simplex has a two-element antipodal orbit and builds the canonical quotient boundary matrices from orientation-preserving face orbits. It verifies the complete integer identity \(\partial_1\partial_2=0\), connectivity of the 30-vertex quotient one-skeleton, and the exact two-stage integer Smith reduction. It accepts only the output `ALL_VERIFY_OK` after every assertion succeeds.

Replay from a directory containing the provided `verify.py` using `python3 verify.py`. The complete finite computation is part of the proof; a printed log without the executable and its exact integer operations would not suffice.

## Relationship to prior work
Lesh, Schreiner and Wahl introduce the doubling operation and establish general connectivity results, but do not classify this particular quotient or its integral torsion. The classical homotopy formula of Björner, Wachs and Welker for **vertex inflations** applies to the covering complex \(Y\), not to its nontrivial global antipodal quotient \(Q\); the 2004 Wachs exposition also gives an equivariant homology formula for inflations, but that representation theorem does not itself provide the integral cellular Smith form of the quotient. Ayzenberg and Khoroshavkina study generalized inflations with **flabby sheaves**; no such flabbiness premise is invoked or established for the quotient in this proof. In particular, the quotient is not a fourfold vertex inflation of the base matching complex, and ordinary wedge decompositions cannot be simply descended through this free involution.

The natural question is whether taking global sign-quotients of simplicial doubles preserves the torsion-freeness guaranteed for certain covers by inflation formulas. This example gives an exact, nontrivial negative answer: fifteen independent order-two classes occur. Published results and relevant recorded calculations were compared by their mathematical implications, not just keywords; no inspected source supplies these quotient Smith factors.

## Limitations
The result concerns the six-dimensional cross-polytope and its **global** antipodal involution, not arbitrary cross-polytope dimensions, arbitrary subgroups of coordinate sign changes, or the full homotopy type of the quotient. No homotopy classification of \(Q\), fundamental group presentation or general torsion growth formula is claimed. The Smith reduction is exhaustive and reproducible but has not been independently validated. Equivalence to an unindexed prior calculation remains a residual originality risk.

## References
1. K. Lesh, B. Schreiner and N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436v1 (first public 2025-06-12), Definition 2.1 and Theorem A.
2. M. L. Wachs, *Poset Topology: Tools and Applications* (2004), Section 5.5, Theorems 5.5.2 and 5.5.4 (including the previously known equivariant inflation formula).
3. A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (2026-02-09), Theorem 1.2, Section 5 and Corollary 7.1.
