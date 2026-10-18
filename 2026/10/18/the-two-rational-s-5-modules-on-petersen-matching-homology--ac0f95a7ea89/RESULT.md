# The two rational \(S_5\)-modules on Petersen matching homology

## Finding

Let \(P=KG(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{1,2,3,4,5\}\), and two vertices are adjacent exactly when they are disjoint. Let \(K=\mathcal M(P)\) be the *ordinary* matching complex, whose vertices are the fifteen graph edges and whose simplices are pairwise vertex-disjoint edges. The natural permutation action of \(S_5\) on the five symbols acts simplicially on \(K\).

Write \(E=\mathbb Q^5\) for the natural five-point permutation representation, \(\operatorname{sgn}\) for the sign representation, and \(S^{(3,2)}\) for the five-dimensional rational Specht representation indexed by the partition \((3,2)\). Then, as rational \(S_5\)-representations,

\[
\widetilde H_2(K;\mathbb Q)\cong\operatorname{sgn}\otimes E,
\qquad
\widetilde H_3(K;\mathbb Q)\cong S^{(3,2)},
\]

and \(\widetilde H_q(K;\mathbb Q)=0\) for every \(q\notin\{2,3\}\). In particular, the five-dimensional module in degree two is reducible (a sign line plus a four-dimensional irreducible), whereas the five-dimensional module in degree three is irreducible.

For \(g\in S_5\), put \(f(g)=|\operatorname{Fix}_{\{1,2,3,4,5\}}(g)|\). The character formulas are

\[
\chi_2(g)=\operatorname{sgn}(g)f(g),\qquad
\chi_3(g)=\frac{(f(g)-1)^2+f(g^2)-1}{2}-f(g).
\]

In conjugacy-class order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), their exact values are

| Cycle type | \(1^5\) | \(2,1^3\) | \(2^2,1\) | \(3,1^2\) | \(3,2\) | \(4,1\) | \(5\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(\chi_2\) | 5 | -3 | 1 | 2 | 0 | -1 | 0 |
| \(\chi_3\) | 5 | 1 | 1 | -1 | 1 | -1 | 0 |

## Assumptions and scope

All graphs are finite and simple, all simplicial complexes are ordinary abstract matching complexes, and all homology in the theorem is reduced homology over \(\mathbb Q\). The action is induced by permutations of the five underlying symbols, rather than by independently permuting fifteen edges. The symbol \(S^{(3,2)}\) denotes the standard rational Specht module with the stated partition, not an unspecified five-dimensional representation. No assertion about torsion, the integral group-ring lattice, or equivariant homotopy type is made.

## Proof

**1. Complete chain complex.** Order the ten graph vertices lexicographically by their two-subsets and order the fifteen edges lexicographically by their endpoint indices. For \(k=0,\ldots,5\), form the vector space on all matchings of \(k\) edges (for \(k=0\), use the single empty matching). Orient each matching by increasing edge indices, and define the reduced boundary by deleting its edge in position \(j\) with sign \((-1)^j\), where positions start at zero. Complete enumeration gives the numbers of matchings of cardinality \(0,1,2,3,4,5\):

\[
(1,15,75,145,90,6).
\]

Exact rational Gaussian elimination on the five boundary matrices \(\partial_k:C_{k-1}\to C_{k-2}\) for \(1\le k\le5\) yields ranks

\[
(1,14,61,79,6).
\]

Thus \(\dim\widetilde H_2=145-61-79=5\) and \(\dim\widetilde H_3=90-79-6=5\); the other reduced rational Betti numbers vanish. These ranks are reconstructed independently, without invoking any previously obtained homotopy type, in `verify_invariants.py`.

**2. Invariant-chain calculation.** For each of the seven cycle types \(t\) in \(S_5\), choose one permutation \(g_t\) of that type, acting on the oriented simplices. A \(\langle g_t\rangle\)-orbit of simplices contributes an invariant-chain basis vector exactly when the product of its orientation multipliers around the orbit is \(+1\). In that case its coherently signed orbit sum is one basis vector; when the product is \(-1\), the orbit contributes none. Take the ordinary oriented boundary of each orbit sum and record its coefficient at each chosen representative of the target orbits. This gives an *exact integral* matrix for the differential on the invariant chains. Gaussian elimination over \(\mathbb Q\) gives the following completely exhaustive certificate. Here \(c^g\) lists invariant-chain dimensions in matching-cardinality degrees zero through five, \(r^g\) lists the five invariant-boundary ranks, and \(h^g\) lists the invariant homology dimensions in topological degrees two and three.

| \(t\) | \(c^g\) | \(r^g\) | \(h^g\) |
|---|---|---|---|
| \((1^5)\) | (1,15,75,145,90,6) | (1,14,61,79,6) | (5,5) |
| \((2,1^3)\) | (1,9,36,68,45,3) | (1,8,28,39,3) | (1,3) |
| \((2^2,1)\) | (1,9,37,69,44,4) | (1,8,29,37,4) | (3,3) |
| \((3,1^2)\) | (1,5,25,51,30,2) | (1,4,21,27,2) | (3,1) |
| \((3,2)\) | (1,3,12,24,15,1) | (1,2,10,13,1) | (1,1) |
| \((4,1)\) | (1,5,18,34,21,1) | (1,4,14,19,1) | (1,1) |
| \((5)\) | (1,3,15,29,18,2) | (1,2,13,15,2) | (1,1) |

Since averaging over a finite group is an exact functor in characteristic zero, the homology of the invariant-chain complex is precisely the invariant subspace of the homology. For a permutation \(g\) of order \(o\), this has dimension

\[
\dim H_q^{\langle g\rangle}=\frac1o\sum_{j=0}^{o-1}\chi_q(g^j).
\]

Consequently, the seven pairs \(h^g\) determine the two character rows displayed above: for orders two, three and five use the equality of the nontrivial conjugate powers, and for orders four and six also use the already determined traces of their proper powers. No equality of rational and modular ranks is assumed in this reconstruction.

**3. Identify both representations.** The character of \(\operatorname{sgn}\otimes E\) is \(g\mapsto\operatorname{sgn}(g)f(g)\), agreeing with \(\chi_2\). Put \(U=E/\mathbf1\), the four-dimensional standard representation, so \(\chi_U(g)=f(g)-1\). The symmetric-square character identity

\[
\chi_{\operatorname{Sym}^2U}(g)=\frac{\chi_U(g)^2+\chi_U(g^2)}2
\]

and the standard decomposition \(\operatorname{Sym}^2U\cong\mathbf1\oplus U\oplus S^{(3,2)}\) show that the displayed formula for \(\chi_3\) is exactly the character of \(S^{(3,2)}\). Rational representations of a finite group are semisimple; the two character equalities prove both module isomorphisms. The representation \(S^{(3,2)}\) is irreducible over \(\mathbb Q\). The character inner products over the seven conjugacy classes are \(\langle\chi_2,\chi_2\rangle=2\), \(\langle\chi_3,\chi_3\rangle=1\), and \(\langle\chi_2,\chi_3\rangle=0\), providing another exact representation-theoretic check.

## Verification

Run `python3 verify_invariants.py` with Python 3 standard library. It independently generates all matchings using a separate ordering of the fifteen Petersen edges, constructs every orientation-consistent cyclic invariant-chain complex, checks boundary equivariance, and computes all ranks using exact fractions. Its final line is `INDEPENDENT_ORBIT_PROOF_OK`.

Run `python3 verify_character.py`. A separate direct chain-action implementation builds the original oriented chain complex, eliminates each boundary image modulo the prime \(1000003\), traces permutations on images and chains for representatives of every conjugacy type, and checks both character tables. Its final line is `DIRECT_CHAIN_CHECK_OK`. The prime-field calculation is a cross-check, not a substitute for the exact rational calculation above. The scripts together enumerate all \(332\) simplices including the empty simplex and all seven conjugacy types, which cover the entire \(120\)-element group.

## Relationship to prior work

Bouc's symmetric-group representation theorem and its subsequent matching-complex literature concern the matching complexes of *complete* graphs. Shareshian and Wachs [1] give this general background and exact-sequence methods; their calculation for \(\mathcal M(K_n)\) does not directly determine homology of the proper subcomplex \(\mathcal M(P)\). Zaslavsky [2] classifies Petersen graph matchings into automorphism orbits; those orbit classifications constrain its chain modules but do not specify the boundary-image representations or the two separate homology characters. Bate, Everitt, Ford and Ramos [3] treat complete hypergraph matching complexes and a general stability setting, not this particular Petersen matching complex.

A previously recorded nonequivariant calculation [4] already gives the rank-five homology in degrees two and three and a mixed-dimensional sphere-wedge homotopy type. Neither those Betti numbers nor the sphere-wedge homotopy description is claimed as new. The present assertion identifies the two distinct rational symmetry modules, not just their equal dimensions.

## Limitations

The conclusion is specific to the Petersen graph and its natural \(S_5\)-action. It determines rational characters and isomorphism types; it neither determines integral equivariant homology lattices nor classifies equivariant homotopy. The finite graph computation is exhaustive for this exact graph, not an inference about an infinite family. Possible equivalent equivariant calculations in unindexed literature cannot be excluded solely by bibliographic searches.

## References

[1] J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, first arXiv version 2004-09-03, arXiv:math/0409054v1. https://arxiv.org/html/math/0409054v1

[2] T. Zaslavsky, *Six signed Petersen graphs, and their automorphisms*, Discrete Mathematics 312 (2012), 1558–1583. DOI:10.1016/j.disc.2011.12.010. https://doi.org/10.1016/j.disc.2011.12.010

[3] M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, first arXiv version 2023-12-21, arXiv:2312.13750v1. https://arxiv.org/html/2312.13750v3

[4] *The Petersen matching complex is a wedge of five two-spheres and five three-spheres*, earlier exact calculation, record identifier `80050a32-4367-4c54-9ae8-daf37b3378cd` (unpublished).
