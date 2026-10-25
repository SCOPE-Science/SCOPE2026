# The full \(\mathfrak S_7\)-homology character of pairwise-intersecting triples

## Finding

Let \(X\) have the 35 three-element subsets of \([7]\) as vertices, with a set of vertices spanning a simplex exactly when its triples intersect pairwise. Thus \(X=\operatorname{Ind}(\operatorname{KG}(3,1))\); the symmetric group \(\mathfrak S_7\) acts by relabeling the seven ground points. Over the rationals the entire graded reduced homology representation is

\[
\widetilde H_6(X;\mathbb Q)\cong S^{(7)}\oplus S^{(4,3)}\oplus S^{(2,2,2,1)},\qquad
\widetilde H_9(X;\mathbb Q)\cong S^{(1,1,1,1,1,1,1)}\oplus S^{(2,1,1,1,1,1)},
\]

and all other rational reduced homology groups vanish. Here \(S^{\lambda}\) is the rational Specht representation of \(\mathfrak S_7\) indexed by partition \(\lambda\). The degree-six summands have dimensions \(1,14,14\), and the two degree-nine summands have dimensions \(1,6\). Since the two 14-dimensional representations are sign twists of each other, every odd ground-set permutation has degree-six homological trace exactly \(1\). There is exactly one \(\mathfrak S_7\)-invariant line in degree six.

## Assumptions and scope

The theorem concerns the ordinary independence complex of the Kneser disjointness graph on triples of exactly seven ground points, rather than the different open-neighborhood complex, a stable Kneser graph, or integral homology. Coefficients are \(\mathbb Q\) throughout. The rational homology ranks \(\beta_6=29\) and \(\beta_9=7\), with vanishing in other degrees, are established in the published preprint [1, Theorem 18]; the seven independent top classes indexed by six-element ground subsets were constructed in [2, Theorem 10]. These cited results provide the nonequivariant input, not the equivariant answer.

## Proof

**Degree nine.** For any six-element subset \(S\subset[7]\), the subcomplex on triples contained in \(S\) is a join of ten antipodal zero-spheres: a triple of \(S\) is disjoint from precisely its complementary triple. It is therefore the boundary of a ten-dimensional cross-polytope, with a canonical fundamental class up to sign in degree nine. By [2, Theorem 10], the seven classes from the seven possible \(S\) are independent in \(H_9(X;\mathbb Q)\). Their number equals \(\beta_9=7\) by [1, Theorem 18], so they form a basis. A transposition of the six ground points reverses cross-polytope orientation: on the ten complementary pairs of triples it induces an odd permutation of three pairs and no exchange within a fixed pair. Hence the stabilizer of \(S\) acts on its top line via its sign character. Thus

\[
\widetilde H_9(X;\mathbb Q)\cong
\operatorname{Ind}_{\mathfrak S_6}^{\mathfrak S_7}(\operatorname{sgn}_6)
\cong\operatorname{sgn}_7\otimes\mathbb Q^7
\cong S^{(1,1,1,1,1,1,1)}\oplus S^{(2,1,1,1,1,1)}.
\]

In particular, if \(g\in\mathfrak S_7\) fixes \(f(g)\) of the ground points, then \(\chi_9(g)=\operatorname{sgn}(g)f(g)\).

**A finite signed-Lefschetz formula.** Fix \(g\in\mathfrak S_7\). Its permutation of the 35 triple-vertices has finitely many orbits. Call a vertex orbit *admissible* if all of its triples pairwise intersect. Form a graph \(Q_g\) whose vertices are these admissible orbits, connecting two orbits when a triple in one is disjoint from a triple in the other. Every \(g\)-invariant simplex of \(X\) is exactly the union of a unique independent set \(I\) in \(Q_g\). If \(I\) has \(t\) orbits containing altogether \(s\) triple-vertices, the signed simplex-permutation is \((-1)^{s-t}\), and its reduced Euler-chain weight is \((-1)^{s-1}\). Their product is \((-1)^{t+1}\). Including the empty simplex gives

\[
\widetilde L(g)=-I(Q_g;-1),\qquad
I(Q;z)=\sum_{I\,\mathrm{independent}}z^{|I|}.
\]

By [1, Theorem 18], only degree six and degree nine rational reduced homology survive, so the Hopf trace theorem gives \(\chi_6(g)-\chi_9(g)=-I(Q_g;-1)\). Hence

\[
\boxed{\chi_6(g)=-I(Q_g;-1)+\operatorname{sgn}(g)f(g).}
\]

**Exhaustion of the fifteen conjugacy classes.** For each partition of seven, choose the standard disjoint-cycle representative, form all orbits of its action on the 35 triples, discard internally incompatible orbits, and build \(Q_g\). The graph independence-polynomial specialization is evaluated exactly via
\[
I(Q;-1)=I(Q-v;-1)-I(Q-N[v];-1),\qquad I(\varnothing;-1)=1.
\]
The following exhaustive integer table lists conjugacy class type, \(I(Q_g;-1)\), and the two homology characters; parentheses denote cycle lengths.

| Cycle type | \(I(Q_g;-1)\) | \(\chi_9(g)\) | \(\chi_6(g)\) |
|:--|--:|--:|--:|
| \((1,1,1,1,1,1,1)\) | -22 | 7 | 29 |
| \((1,1,1,1,1,2)\) | -6 | -5 | 1 |
| \((1,1,1,1,3)\) | 5 | 4 | -1 |
| \((1,1,1,2,2)\) | -2 | 3 | 5 |
| \((1,1,1,4)\) | -4 | -3 | 1 |
| \((1,1,2,3)\) | -3 | -2 | 1 |
| \((1,1,5)\) | 3 | 2 | -1 |
| \((1,2,2,2)\) | -2 | -1 | 1 |
| \((1,2,4)\) | 0 | 1 | 1 |
| \((1,3,3)\) | -4 | 1 | 5 |
| \((1,6)\) | -2 | -1 | 1 |
| \((2,2,3)\) | 1 | 0 | -1 |
| \((2,5)\) | -1 | 0 | 1 |
| \((3,4)\) | -1 | 0 | 1 |
| \((7)\) | -1 | 0 | 1 |

Taking the exact rational character inner products, using Murnaghan–Nakayama to compute the \(\mathfrak S_7\) irreducible characters, yields multiplicity one precisely for partitions \((7)\), \((4,3)\), and \((2,2,2,1)\) in degree six; the degree-nine pair follows from the induced-sign module already established. This proves both graded representations.

## Verification

The standalone standard-library program `verify.py` reconstructs all 15 orbit graphs from the 35 triples, evaluates the exact independent-set recurrence, compares small orbit graphs with brute force, calculates all rational Specht character inner products via Murnaghan–Nakayama, verifies the complete character-table orthogonality relations and hook dimensions, and checks the cross-polytope transposition orientation. It reproduces every entry of the table and both module decompositions. The computation makes no extrapolation beyond seven ground points; the argument is exhaustive for this finite group and complex.

## Relationship to prior work

Feng and Wang [2, Theorem 8] construct Fano-plane-based degree-six spherical classes, and [2, Theorem 10] proves independent degree-nine cross-polytopal classes. Feng [1, Theorem 18] proves the complete *dimensions* of rational homology for Kneser graphs on triples, including the case here; the paper explicitly asks for a combinatorial explanation of its degree-six rank 29 [1, Question 21]. These results supply the ranks and top-sphere independence used in the proof but do not identify the symmetric-group action or the two distinct 14-dimensional degree-six irreducibles. The new statement is the equivariant refinement, not a new Betti-number or wedge-of-spheres classification. Results on stable Kneser independence complexes and on the open-neighborhood complex of a different Kneser graph concern different simplicial complexes.

## Limitations

The conclusion is a rational representation classification for exactly seven ground points. It neither constructs a concrete 29-element integral homology basis nor establishes torsion freeness, an integral Specht decomposition, any wedge-of-spheres homotopy type, or a general formula for larger ground sets. The degree-nine basis and the rational homological concentration are imported published premises, explicitly credited; the new exact invariant-simplex computation is independently reproducible. Equivalent unindexed equivariant results cannot be ruled out solely by bibliographic search.

## References

[1] Ziqin Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394v1, first public 2026-10-12. https://arxiv.org/html/2610.17394v1 . Theorem 18 and Question 21.

[2] Ziqin Feng and Guanghui Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1, first public 2024-04-16. https://arxiv.org/html/2404.10566v1 . Theorems 8 and 10.
