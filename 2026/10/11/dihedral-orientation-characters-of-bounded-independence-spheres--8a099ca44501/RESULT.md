# Dihedral orientation characters of bounded-independence spheres on cycles

## Finding
For integers \(d\ge2\) and \(n\ge2d\), let \(C_n\) be the simple cycle on \(\mathbb Z/n\mathbb Z\), and let
\[
B_d(C_n)=\{S\subseteq V(C_n):\alpha(C_n[S])<d\}.
\]
Write \(D_n=\langle r,s\rangle\), where \(r(i)=i+1\) and \(s(i)=-i\). The known sphere homotopy classification gives \(B_d(C_n)\simeq S^{2d-3}\). **The new equivariant assertion** identifies the complete action on its unique nonzero reduced integral homology group:
\[
\operatorname{tr}(r^a\mid\widetilde H_{2d-3})=1,\qquad
\operatorname{tr}(r^as\mid\widetilde H_{2d-3})=(-1)^{d-1}
\quad(a\in\mathbb Z).
\]
Thus \(\widetilde H_{2d-3}(B_d(C_n);\mathbb Z)\cong H_1(C_n;\mathbb Z)^{\otimes(d-1)}\) as rank-one integral \(D_n\)-representations. The equality of representations, not a canonical identification of generators, is asserted.

For the natural actions on geometric realizations, the reduced rational homology of \(B_d(C_n)/\langle r\rangle\) is \(\mathbb Q\) in degree \(2d-3\) and zero otherwise. The same holds for \(B_d(C_n)/D_n\) when \(d\) is odd; when \(d\) is even, all reduced rational homology of that quotient is zero.

For \(d\ge3\), \(p\ge1\) and \(n\ge2pd\), all these statements remain valid with \(C_n\) replaced by its \(p\)-th power \(C_n^p\). The action of \(D_n\) remains the one induced from the cycle labels.

## Assumptions and scope
A vertex subset is a face precisely when its induced graph contains no independent set of size \(d\). Indices are taken modulo \(n\). Graph powers join vertices at cycle distance at most \(p\). All homology outside the quotient statement is integral; quotient homology is over \(\mathbb Q\), and no integral quotient homology is claimed. The existing homotopy-equivalence inputs used below are explicitly attributed to Carnero Bravo.

## Proof
**Step 1: base sphere and orientation.** At \(n=2d\) the only independent sets of cardinality \(d\) in the cycle are the even and odd vertex classes \(E\) and \(O\). Therefore
\[
B_d(C_{2d})=\partial\Delta^E*\partial\Delta^O\cong S^{2d-3}.
\]
On this top homology, any permutation respecting the classes acts by the product of its two restriction signs. Exchanging the two factors contributes \((-1)^{(d-1)^2}=(-1)^{d-1}\), the orientation sign of a join of two \((d-2)\)-spheres. The one-step rotation exchanges the classes, is cyclic on precisely one of them, and consequently has sign \((-1)^{d-1}(-1)^{d-1}=1\). The reflection \(i\mapsto-i\) preserves the classes. Its induced permutations on their \(d\) positions are \(j\mapsto-j\) and \(j\mapsto-j-1\); their sign product is the sign of translation by one on \(d\) positions, namely \((-1)^{d-1}\).

**Step 2: degree-one cyclic contractions.** Call a map \(f:\mathbb Z/n\mathbb Z\to\mathbb Z/(2d)\mathbb Z\) a cyclic contraction if it is specified by a word of \(n\) increments, each \(0\) or \(1\), with precisely \(2d\) increments equal to \(1\), and by one initial target value. It is a graph map taking edges either to edges or to singletons. For any face \(S\) of \(B_d(C_n)\), its image is a face of \(B_d(C_{2d})\): otherwise, the image contains one of the two alternating independent \(d\)-sets of \(C_{2d}\). Choosing one source representative for each of its target vertices gives \(d\) pairwise nonadjacent vertices in \(S\), a contradiction. Hence \(f\) induces a simplicial map \(F_f\) of bounded-independence complexes.

**Step 3: adjacent swaps give simplicial contiguity.** Suppose two increment words based at the same target value differ by interchanging adjacent increments \(0,1\) and \(1,0\) at positions not crossing the chosen initial position. Their cyclic contractions \(f,g\) differ only at one source vertex \(v\): the two target values are adjacent, say \(a,b\), and both neighbors of \(v\) have their common images among \(\{a,b\}\). To prove the induced simplicial maps are contiguous, assume some face \(S\) has \(f(S)\cup g(S)\) not a face of \(B_d(C_{2d})\). It contains an independent alternating target class \(P\) of size \(d\). Because \(f(S)\) is itself a face, the new target value, say \(b\), belongs to \(P\), whereas \(a\notin P\). For each of the other \(d-1\) vertices of \(P\), choose a distinct representative \(w_t\in S\setminus\{v\}\) having that target value under \(f\). Since adjacent source vertices cannot map to two distinct nonadjacent target vertices, the representatives are pairwise nonadjacent. Neither neighbor of \(v\) can be a representative: its image is \(a\) or \(b\), neither of which belongs to \(P\setminus\{b\}\). Thus \(\{v\}\cup\{w_t:t\in P\setminus\{b\}\}\) is an independent set of size \(d\) in \(S\), contradiction. The reverse adjacent swap is symmetric. Therefore the induced maps are contiguous and hence homotopic.

Every two cyclic contractions with the same initial target value are linked by adjacent swaps of their \(0\)-\(1\) increment words (the usual connectivity of the fixed-weight binary words by adjacent transpositions), so their induced maps are homotopic.

**Step 4: transport the dihedral action.** For \(d\ge3\), the cyclic block-coloring map of Carnero Bravo, Theorem 33 of the 2026 preprint, is a cyclic contraction \(f:C_n\to C_{2d}\) whose induced map \(F_f:B_d(C_n)\to B_d(C_{2d})\) is a homotopy equivalence. By Step 3 every cyclic contraction induces the same homotopy equivalence after normalizing its initial target value. For \(d=2\), these are degree-one maps of simplicial circles, hence also homotopy equivalences.

Let \(R,S\) denote the rotation and reflection of the target cycle. If \(r\) is the source one-step rotation, then \(R^{-f(1)}\circ f\circ r\) is another cyclic contraction with initial target value \(0\) (take \(f(0)=0\)). The homotopy of Step 3 gives
\[
F_f\circ r\simeq R^{f(1)}\circ F_f.
\]
Similarly \(S\circ f\circ s\) is a degree-one cyclic contraction with initial value \(0\), so
\[
F_f\circ s\simeq S\circ F_f.
\]
Transporting to the rank-one top integral homology through the isomorphism induced by \(F_f\) and using Step 1 proves the character assertions for the source rotation and reflection, hence for every dihedral element.

**Step 5: powers and quotients.** For \(d\ge3\), Carnero Bravo, Theorem 33, proves that \(B_d(C_n)\hookrightarrow B_d(C_n^p)\) is a homotopy equivalence for \(n\ge2pd\). Because the inclusion commutes with the dihedral action, it transports the exact integral character. For any finite group acting simplicially, rational quotient homology is the invariant rational homology of the original complex, by averaging on the rational simplicial chain complex (equivalently, the rational transfer statement). Taking invariants of the one-dimensional character now yields the quotient classification.

## Verification
The accompanying standalone Python verifier enumerates admissible faces directly from independent-set tests, evaluates signed fixed-simplex Lefschetz traces for every dihedral element in stated finite ranges, and independently checks the adjacent-swap contiguity lemma in small examples. The proof, not finite enumeration, establishes all parameter ranges. Invoke `python3 verification.py`; it uses only the standard library.

## Relationship to prior work
Carnero Bravo, *Total cut complexes and their duals* (arXiv:2602.21427v1, February 24, 2026), Corollary 32 establishes \(B_d(C_n)\simeq S^{2d-3}\), and Theorem 33 constructs the coloring homotopy equivalences and the inclusions for cycle powers. These are essential inputs here; neither statement supplies the induced dihedral orientation character, and a nonequivariant homotopy equivalence by itself cannot identify the action. The adjacent-swap contiguity argument and orientation comparison fill that gap. The 2026 vertex-decomposability results of Zaare-Nahandi also study the same underlying complexes, but the publicly accessible abstract does not settle their equivariant homology representation. A prior equivariant Euler formula on connected bipartite graphs implies the special case \(d=3\) on even cycles after combining it with homology concentration; the present character theorem applies to all \(d\), odd cycles, and the indicated powers.

## Limitations
The result determines only the action on reduced homology, not an equivariant homotopy equivalence or an integral homology classification of orbit spaces. It relies on the published sphere and coloring-map theorems rather than re-proving them. The subscribed full text of Zaare-Nahandi's 2026 paper was unavailable; an equivalent equivariant calculation there or in unindexed literature cannot be ruled out. Numerical checks are finite corroboration, not exhaustive certification of an infinite theorem.

## References
1. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427v1 (first posted 2026-02-24), https://arxiv.org/html/2602.21427v1. In particular definitions, Proposition 14, Corollary 32, Theorem 33 and its proof.
2. R. Zaare-Nahandi, *Vertex Decomposability of Some Complexes Associated to Graphs*, Bulletin of the Iranian Mathematical Society 52 (2026), article 40, https://doi.org/10.1007/s41980-026-01052-z. Only the publisher abstract was available.
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, Discrete & Computational Geometry 73 (2025), 500–527, https://doi.org/10.1007/s00454-024-00630-4. Earlier nonequivariant cycle calculation, as quoted in reference 1.
