# The full \(S_7\)-character of the 29-sphere Kneser neighborhood complex

## Finding
Let \(G=\mathrm{KG}(7,2)\) be the graph whose vertices are the 21 two-element subsets of \([7]\), adjacent if and only if disjoint. Write \(X=\mathcal N(G)\) for the ordinary Lovász open-neighborhood complex. The natural \(S_7\)-action on its degree-three reduced rational homology has character
\[
\chi(g)=\operatorname{sgn}(g)\big(f(g)^2-3f(g)+1\big),
\]
where \(f(g)\) counts symbols fixed by \(g\). In Specht notation this means
\[
\widetilde H_3(X;\mathbb Q)\cong
S^{(2,2,1,1,1)}\oplus S^{(3,1,1,1,1)}.
\]
The two summands have dimensions 14 and 15. Every other reduced rational homology group is zero. There is no nonzero full-group invariant, so \(X/S_7\) has trivial reduced rational homology.

## Assumptions and scope
Everything uses the 21 vertices of the finite abstract graph, not the geometric realization of an edge-length metric graph. A simplex in \(X\) is a nonempty family of two-subsets that admits some disjoint two-subset as a common neighbor. Equivalently, the union of its underlying symbols has size at most five. The symmetric group \(S_7\) acts by permuting the original seven symbols and thus acts simplicially on \(X\). Homology and representations are over \(\mathbb Q\) unless explicitly stated otherwise. The full group is considered, not merely its cyclic or dihedral subgroup.

## Proof
**Nonequivariant input.** Nilakantan and Singh, Theorem 1.3 of arXiv:1802.05848 (first posted 2018-02-16), prove that the neighborhood complex of \(\mathrm{KG}_{2,k}\) is homotopy equivalent to a wedge of \(k^2+5k+5\) copies of the \(k\)-sphere; their definition has two-subsets of \([k+4]\). At \(k=3\), this is exactly the present \(G\), so \(\widetilde H_3(X;\mathbb Q)\cong\mathbb Q^{29}\), and all other reduced rational homology vanishes. This homotopy calculation is existing literature, not a new assertion.

**Finite signed Lefschetz calculation.** The common-neighbor criterion gives 21 ten-vertex neighborhood simplices; all nonempty faces are deduplicated. The numbers of faces of dimensions zero through nine are, respectively,
\[
(21,210,1225,3360,4872,4340,2520,945,210,21).
\]
This enumeration is independently reproduced by counting edge-sets on \(r\) used labels, where \(2\le r\le5\), via inclusion-exclusion. For a representative \(g\) of each of the 15 cycle types of \(S_7\), a face contributes to \(\operatorname{tr}(g\mid C_d(X;\mathbb Q))\) only if it is preserved setwise, with coefficient the sign of the induced permutation of its ordered vertices. Therefore the reduced simplicial Lefschetz number is
\[
\widetilde L(g)=\sum_{d=0}^{9}(-1)^d\operatorname{tr}(g\mid C_d(X;\mathbb Q))-1.
\]
The \(-1\) subtracts the augmented degree-minus-one chain group, fixed trivially. Because only reduced degree-three homology survives, \(\chi(g)=-\widetilde L(g)\). The complete 15-class calculation in the accompanying verifier finds \(\chi(g)=\operatorname{sgn}(g)(f(g)^2-3f(g)+1)\) for every class; no extrapolation from partial samples is made. In particular \(\chi(1)=29\). The class sizes sum to 5040, covering every group element.

**Irreducible identification.** Let \(M_1\) and \(M_2\) denote the rational permutation modules on one- and two-element subsets of \([7]\), and let \(V\) be the six-dimensional standard representation. For a permutation with \(f\) fixed symbols and \(t\) two-cycles, the virtual character of \(M_2-M_1\) is \(\binom f2+t-f\); standard Specht-module decompositions identify it with \(S^{(5,2)}\). The character of \(\bigwedge^2V\cong S^{(5,1,1)}\) is \((f-1)(f-2)/2-t\). Their sum is \(f^2-3f+1\). Conjugating partitions under the sign twist gives
\[
\operatorname{sgn}\otimes S^{(5,2)}=S^{(2,2,1,1,1)},\qquad
\operatorname{sgn}\otimes S^{(5,1,1)}=S^{(3,1,1,1,1)}.
\]
The verifier independently checks that the two characters have norm one and mutual inner product zero over the entire group, confirming that they are distinct irreducibles. The trivial constituent is absent, also confirmed by averaging the full character.

**Quotient.** Barycentrically subdividing \(X\) makes the finite simplicial action admissible without changing its rational homology. In characteristic zero, averaging identifies rational homology of the orbit space with group-invariant rational homology. Since the positive-degree representation has no trivial summand and the space is connected, the reduced rational homology of \(X/S_7\) vanishes.

## Verification
Run `python3 verify.py` in the directory containing the accompanying files, with Python 3 standard library only. It enumerates every nonempty face by every common neighbor, independently verifies the entire face vector using inclusion-exclusion on the union of labels, enumerates all 5040 permutations and all 15 cycle types, and computes the signed Lefschetz number for each representative. It compares each exact trace with the closed character formula, calculates character inner products with exact integer arithmetic, and checks the quotient-invariant dimension. The output `verify_output.txt` records the actual run. The verifier does **not** independently establish the previously published homotopy concentration; that step is supplied by the cited theorem.

## Relationship to prior work
Lovász introduced graph neighborhood complexes in the Kneser-coloring argument. Schultz's 2010 equivariant treatment of **stable** Kneser graphs studies canonical dihedral symmetry, rather than the full \(S_7\) action on this ordinary Kneser graph. Braun and Zeckner's 2011 stable-Kneser deformation-retract theorem likewise studies a different graph and symmetry. Nilakantan and Singh's 2018 Theorem 1.3 supplies precisely the nonequivariant wedge-of-29-spheres calculation, but its identified theorems and full-text proof do not state the present \(S_7\)-character. A public same-family record determines the \(S_6\)-module on \(\mathcal N(\mathrm{KG}(6,2))\), a different complex and group; a single lower-parameter calculation does not imply the seven-symbol module. The new contribution here is exactly the rational \(S_7\)-action and its quotient consequence, not the wedge homotopy type or general theory of Specht modules.

## Limitations
Only the rational representation and rational quotient homology are classified. This does not determine integral equivariant lattices, quotient homotopy type, or equivariant simple-homotopy type. The homology concentration is imported from a published proof rather than independently recomputed. Exact publication priority cannot be guaranteed; an unindexed equivalent character calculation remains possible. Independent mathematical review has not been performed.

## References
1. Carsten Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688 (first publicly posted 2010-03-29), especially the introduction and equivariant homotopy discussion.
2. Benjamin Braun and Matthew Zeckner, *Deformation Retracts of Neighborhood Complexes of Stable Kneser Graphs*, arXiv:1102.1984 (first publicly posted 2011-02-09), Theorems 1.2–1.3.
3. Nandini Nilakantan and Anurag Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, \(KG_{2,k}\)*, arXiv:1802.05848 (first publicly posted 2018-02-16), Theorem 1.3 and Definition 2.1.
4. *Rational symmetry decomposition of the Kneser neighborhood complex on six points*, publicly indexed published-finding corpus record `6890383e239b`, concerning the different complex \(\mathcal N(\mathrm{KG}(6,2))\). Only its indexed summary was accessible for comparison.
