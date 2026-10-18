# A Moore-space affine quotient of the Paley-11 directed flag complex

## Finding
Let \(P_{11}\) be the tournament on \(\mathbb F_{11}\) with \(x\to y\) if and only if \(y-x\in Q=\{1,3,4,5,9\}\) modulo eleven. Let \(X=\operatorname{dFl}(P_{11})\) be the simplicial complex whose nonempty faces are the transitive subtournaments. Set
\[
G=\{x\mapsto ax+b:a\in Q,\ b\in\mathbb F_{11}\}\cong C_{11}\rtimes C_5,
\]
and denote its translation and multiplier subgroups by \(T\cong C_{11}\) and \(H\cong C_5\), respectively. Then
\[
\boxed{|X|/G\simeq M(\mathbb Z/2,2).}
\]
The subgroup quotients satisfy
\[
\begin{aligned}
\widetilde H_1(|X|/T;\mathbb Z)&\cong\mathbb Z/11, &
\widetilde H_2(|X|/T;\mathbb Z)&\cong\mathbb Z/2,\\
\widetilde H_2(|X|/H;\mathbb Z)&\cong\mathbb Z^2\oplus\mathbb Z/2.
\end{aligned}
\]
All unlisted reduced integral homology groups of those two subgroup orbit spaces vanish. Thus the full affine quotient removes the ten free second-homology generators of the original complex while retaining the two-torsion Moore space.

## Assumptions and scope
The Paley tournament is defined by the explicit quadratic-residue difference orientation above; \(Q\) is the unique multiplicative subgroup of order five in \(\mathbb F_{11}^{\times}\), so all fifty-five affine maps preserve tournament edges. The symbol \(|X|/K\) denotes the ordinary *topological* quotient of the geometric realization by the indicated finite group; it is not an equivariant Borel construction. The Moore space \(M(\mathbb Z/2,2)\) is a three-dimensional CW complex with one zero-cell, one two-cell and one three-cell attached by degree two. A simplex of a directed flag complex is the uniquely oriented linear order on a transitive subtournament.

## Proof
**Orbit cells.** Every automorphism of a transitive tournament that fixes its vertex set fixes each vertex: the transitive tournament has a unique source, then a unique source after deletion, and so on. Consequently any group element stabilizing a simplex acts pointwise and preserves its orientation. This makes the quotient an admissible finite cellular quotient: its \(k\)-cells correspond exactly to orbits of \(k\)-simplices, with boundary signs inherited from the unique tournament order. In particular the resulting integral orbit-chain complex computes the integral homology of the *topological* quotient, rather than just group coinvariants in homology.

The faces of \(X\) have cardinality distribution \((11,55,110,55)\) in dimensions zero through three, with no higher-dimensional faces. Enumerating all transitive subsets via their unique source and then the full affine orbits gives the quotient cell counts
\[
\begin{array}{c|rrrr}
\text{group}&c_0&c_1&c_2&c_3\\\hline
G&1&1&2&1\\
T&1&5&10&5\\
H&3&11&22&11
\end{array}
\]
(all counts include only nonempty simplices). For an ordered simplex \((v_0,\ldots,v_k)\), the cellular boundary of its orbit is \(\sum_{i=0}^k(-1)^i[(v_0,\ldots,\widehat v_i,\ldots,v_k)]\). This is well-defined because every affine automorphism preserves the directed linear order on a transitive subtournament.

**The full quotient and its homotopy type.** With a choice of orbit-cell bases, the complete cellular differentials for \(|X|/G\), from dimension three downwards, are
\[
\partial_3=\begin{pmatrix}-2\\2\end{pmatrix},\qquad
\partial_2=\begin{pmatrix}1&1\end{pmatrix},\qquad
\partial_1=(0).
\]
The first two-cell is attached to the unique one-cell by a map of degree one, since its cellular coefficient is \(+1\). The subcomplex consisting of the zero-cell, one-cell and this two-cell is therefore contractible: it is the mapping cone of a degree-one circle map. Collapse that contractible subcomplex. The remaining two-cell gives an \(S^2\), and the remaining three-cell attaches to it by a map of degree two, as read from the second coordinate of \(\partial_3\). Collapsing a contractible CW subcomplex is a homotopy equivalence, so the quotient is the degree-two mapping cone \(M(\mathbb Z/2,2)\).

**The two subgroup quotients.** For \(T\), the chain-group ranks are \((1,5,10,5)\). The exact Smith invariant factors of \(\partial_1,\partial_2,\partial_3\) are, respectively, no nonzero factors, \((1,1,1,1,11)\), and \((1,1,1,1,2)\). The differentials have ranks \((0,5,5)\); hence \(\widetilde H_1\cong\mathbb Z/11\), \(\widetilde H_2\cong\mathbb Z/2\), and all remaining reduced groups vanish. For \(H\), cell ranks are \((3,11,22,11)\) and the Smith factors of the three consecutive differentials are \((1,1)\), \((1^9)\), and \((1^{10},2)\). Their ranks are \((2,9,11)\), giving \(\widetilde H_2\cong\mathbb Z^2\oplus\mathbb Z/2\), and no other reduced homology. To infer the torsion of \(H_2\) from \(\partial_3\), use the short exact sequence \(0\to H_2\to\operatorname{coker}\partial_3\to\operatorname{im}\partial_2\to0\): the final group is free, so the torsion of the first group equals the torsion of the middle group. The analogous assertion holds in all three quotient complexes.

**Independent structural checks.** Exact integer Smith form for the original \(X\) gives \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z^{10}\oplus\mathbb Z/2\), reproducing the nonequivariant result of Govc [2]. The rational second-homology character under \(G\) is \(10\) at the identity, \(-1\) at each nontrivial translation, and \(0\) at each nontranslation affine map: a setwise invariant transitive face is pointwise fixed, so the Lefschetz number is the Euler characteristic of the fixed-vertex subcomplex. This is the augmentation character of the eleven-point affine permutation action and confirms the rational Betti numbers \(0\), \(0\), and \(2\) for the three quotients, respectively. The integral quotient calculations above refine these rational checks.

## Verification
The standalone exact-arithmetic programs `verify_quotients_directed.py` and `verify_quotients_sorted.py` independently reconstruct the three integral orbit-chain complexes. They use different simplex orientations—respectively the tournament's canonical order and numerical vertex order with explicit permutation signs—then verify chain identities, cell counts, boundary ranks and Smith invariant factors. `verify_smith.py` independently computes the original complex's integer Smith forms and checks its boundary compositions. `verify_affine.py` enumerates all fifty-five affine maps and all fixed faces and checks the Lefschetz character. Each program is executable with Python 3; Smith computations require the open-source SymPy package. Their exact outputs appear in `verification_output.json`.

## Relationship to prior work
Govc [2, Proposition 3.4] already proves that the eleven-vertex doubly regular tournament has directed flag complex \(M(\mathbb Z/2,2)\vee\bigvee^{10}S^2\). This is **not** claimed as new. The present determination of the integral homology of the natural affine subgroup orbit spaces and the *homotopy type* of the full fifty-five-element quotient are additional, equivariant topological assertions: a nonequivariant wedge decomposition does not determine the homology or homotopy of its orbit spaces. Govc, Levi and Smith [1] develop the broader tournament-complex setting without the affine-orbit classification stated here. Existing calculations for other Paley tournament orders concern different spaces and parameters and do not imply this quotient result.

## Limitations
The result concerns exactly the Paley tournament on eleven vertices, its specified affine group and two named subgroups. It does not classify orbit spaces for other tournaments, determine an integral representation lattice for every homology group, or identify the equivariant homotopy type of the original complex. The calculation of subgroup quotient homology is not asserted to be a full homotopy classification of those subgroup quotients. The original non-equivariant Moore-space homotopy classification is credited to [2].

## References
[1] D. Govc, R. Levi, J. P. Smith, “Complexes of Tournaments, Directionality Filtrations and Persistent Homology,” arXiv:2003.00324, first submitted 2020-02-29; *Journal of Applied and Computational Topology* 5 (2021), 313–337.

[2] D. Govc, “Computing Homotopy Types of Directed Flag Complexes,” arXiv:2006.05333v1, first submitted 2020-06-09, Proposition 3.4 (the eleven-vertex nonequivariant homotopy type).
