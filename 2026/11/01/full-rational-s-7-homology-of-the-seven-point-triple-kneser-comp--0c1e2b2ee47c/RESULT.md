# Full rational \(S_7\)-homology of the seven-point triple Kneser complex

## Finding
Let \(X=\operatorname{Ind}(\operatorname{KG}(7,3))\), where the Kneser graph has as vertices the \(35\) three-element subsets of \([7]\), with an edge exactly between disjoint triples. Thus simplices of \(X\) are pairwise-intersecting families of triples. The natural ground-set permutation group \(S_7\) acts simplicially on \(X\). Denote the irreducible rational Specht module indexed by a partition \(\lambda\vdash7\) by \(S^\lambda\).

The entire reduced rational homology representation is
\[
\boxed{\begin{aligned}
\widetilde H_6(X;\mathbb Q)&\cong S^{(7)}\oplus S^{(4,3)}\oplus S^{(2,2,2,1)},\\
\widetilde H_9(X;\mathbb Q)&\cong S^{(1,1,1,1,1,1,1)}\oplus S^{(2,1,1,1,1,1)},\\
\widetilde H_i(X;\mathbb Q)&=0\quad(i\notin\{6,9\}).
\end{aligned}}
\]
In particular, degree six contains one invariant rational line, whereas degree nine is the sign twist of the seven-point permutation representation. Their dimensions are \(29\) and \(7\), respectively. The Betti numbers and vanishing are inputs from the cited 2026 theorem; the decomposition into irreducible symmetry representations is the present result.

## Assumptions and scope
The notation \(\operatorname{KG}(7,3)\) uses the conventional convention (ground-set size, subset size). The corresponding graph appears as \(\operatorname{KG}(3,1)\) in the parameters of Feng (2026); both denote disjointness among three-element subsets of a seven-element set.

All homology is reduced simplicial homology over \(\mathbb Q\). The action is induced by permutations of the seven underlying points, not arbitrary permutations of the \(35\) vertices. The standard partition convention is weakly decreasing. The case is the first triple-Kneser independence complex in which two distinct positive homological degrees occur. No extension to larger ground sets or integral coefficients is asserted.

## Proof
**1. The fixed-face Lefschetz formula.** Fix \(g\in S_7\). It permutes the \(35\) triple-vertices. Partition them into cycles \(O_1,\dots,O_s\). Discard a cycle if it contains two disjoint triples; its entire set cannot belong to a simplex. For the remaining cycles, make a finite graph \(Q_g\): two cycle-vertices are adjacent when some triple of the first cycle is disjoint from some triple of the second. Each \(g\)-invariant simplex is exactly a union of an independent collection of the surviving cycles. This is a bijection including the empty simplex.

If an invariant nonempty simplex consists of \(c\) cycles comprising \(N\) triple-vertices, the sign of the permutation induced by \(g\) on its oriented chain generator is \((-1)^{N-c}\). Multiplying by the alternating chain-degree factor \((-1)^{N-1}\) gives \((-1)^{c-1}\). The empty simplex contributes \(-1\) in the reduced augmented chain complex. Thus the reduced Lefschetz character \(L(g)=\sum_i(-1)^i\operatorname{tr}(g\mid\widetilde H_i(X;\mathbb Q))\) is the integer
\[
L(g)=-\sum_{I\in\operatorname{Ind}(Q_g)}(-1)^{|I|},
\]
where the empty independent set is included. The equality uses the Hopf trace theorem for the finite chain complex and holds without choosing homology bases.

**2. Exact finite character.** The ground-set cycle type \(\mu\vdash7\) determines the class of \(g\), hence the value \(L(g)\). For any induced subgraph \(H\) of \(Q_g\), define \(F(H)=\sum_{I\in\operatorname{Ind}(H)}(-1)^{|I|}\). For any vertex \(v\), partitioning independent sets according to whether they contain \(v\) gives
\[
F(H)=F(H-v)-F(H-N_H[v]),\qquad F(\varnothing)=1.
\]
This finite recursion completely evaluates the previous formula without truncated search or numerical approximation. The resulting reduced Lefschetz values for every conjugacy class, ordered by descending cycle partition, are:

| Cycle type \(\mu\) | \(L(\mu)\) | Cycle type \(\mu\) | \(L(\mu)\) |
|---|---:|---|---:|
| \((1^7)\) | 22 | \((2,1^5)\) | 6 |
| \((3,1^4)\) | -5 | \((2^2,1^3)\) | 2 |
| \((4,1^3)\) | 4 | \((3,2,1^2)\) | 3 |
| \((5,1^2)\) | -3 | \((2^3,1)\) | 2 |
| \((4,2,1)\) | 0 | \((3^2,1)\) | 4 |
| \((6,1)\) | 2 | \((3,2^2)\) | -1 |
| \((5,2)\) | 1 | \((4,3)\) | 1 |
| \((7)\) | 1 |  |  |

For independent rechecking, `CHECKS/verify_faces.py` enumerates every invariant face (including all \(1{,}278{,}686\) faces for the identity) without the recurrence; `CHECKS/verify_character.py` implements the exact recurrence and separately evaluates the symmetric-group character table by the Murnaghan–Nakayama rim-hook rule. Their output is an exact exhaustive calculation, not a random sample. In particular \(L(1)=22\), consistent with the published \(29-7\) alternating Betti rank.

**3. Decompose the virtual character.** The rational character inner product on class functions is
\[
\langle L,\chi^\lambda\rangle
=\sum_{\mu\vdash7}\frac{L(\mu)\chi^\lambda(\mu)}{z_\mu},
\qquad z_\mu=\prod_{j\ge1}j^{m_j(\mu)}m_j(\mu)!.
\]
The Murnaghan–Nakayama rule and the fifteen exact entries above give coefficient \(+1\) for partitions \((7)\), \((4,3)\), \((2,2,2,1)\), coefficient \(-1\) for \((1^7)\), \((2,1^5)\), and zero for the other ten partitions. Thus, in the rational representation ring,
\[
[\widetilde H_6]-[\widetilde H_9]
=[S^{(7)}]+[S^{(4,3)}]+[S^{(2,2,2,1)}]
-[S^{(1^7)}]-[S^{(2,1^5)}].
\]
The cited 2026 homology theorem establishes that only these two degrees occur and that their dimensions are \(29\) and \(7\). Over \(\mathbb Q\), all finite-group representations are semisimple. The negative Specht coefficients force degree-nine homology to contain both \(S^{(1^7)}\) and \(S^{(2,1^5)}\). Their dimensions are \(1\) and \(6\), exhausting the entire seven-dimensional degree-nine space. Consequently degree nine is exactly their sum, and degree six is exactly the remaining positive part. The positive summands have dimensions \(1,14,14\), totalling \(29\). This proves the displayed classification without assuming that embedded six-point spheres form a homology basis.

## Verification
Run from the extracted package with a standard Python 3 interpreter:

`python CHECKS/verify_character.py`

`python CHECKS/verify_faces.py`

Both checkers use only the standard library. The first recomputes the fifteen orbit graphs, exact alternating independent-set sums, all fifteen Specht inner products, and both dimensional and classwise consistency checks. The second independently enumerates every invariant face for every cycle type and checks the same fifteen integer Lefschetz values; for the identity it traverses \(1{,}278{,}686\) faces including the empty face. Both completed successfully from these source files. The general algebraic steps are explicit above; the finite exhaustiveness follows from considering every triple orbit and every permissible orbit subset.

## Relationship to prior work
Feng (arXiv:2610.17394v1, first public 2026-10-12) proves the rational homology degrees and Betti numbers for all triple-Kneser independence complexes; its full-text introduction, theorem, and open-questions sections do not give symmetry character values or irreducible representations. Feng and Wang (arXiv:2404.10566, first public 2024-04-16) study homology generators, propagation, and finite Betti numbers, not an identified seven-point full \(S_7\) Specht decomposition in the inspected abstract. Neither the two Betti numbers alone nor general group representation theory implies this particular character: the fifteen signed Lefschetz values provide the missing information. Related calculations for Kneser neighborhood complexes and stable Kneser independence complexes concern different simplicial constructions or different graph families, so their representation statements do not imply the present one. The non-availability of a full-text inspection of the 2024 preprint remains a literature-comparison limitation.

## Limitations
This is a rational representation classification for exactly seven underlying points and \(3\)-element subsets. It does not establish integral homology, torsion-freeness, a wedge-of-spheres homotopy type, an explicit basis of cycles, or the character for larger parameters. It depends on the published rational Betti-number theorem. Absence of a matching result from indexed searches is not proof of uniqueness; implicit or unindexed coverage remains possible. Independent validation has not been performed.

## References
1. Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394v1 (first submitted 2026-10-12), https://arxiv.org/html/2610.17394v1.
2. Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566 (first submitted 2024-04-16), https://arxiv.org/abs/2404.10566.
3. B. E. Sagan, *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions*, 2nd ed., Springer (2001), for standard Specht characters and the Murnaghan–Nakayama rule.
