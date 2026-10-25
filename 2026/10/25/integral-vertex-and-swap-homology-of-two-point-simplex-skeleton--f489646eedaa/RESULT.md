# Integral vertex-and-swap homology of two-point simplex-skeleton configurations

## Finding
For every integer \(n\ge4\), let \(K_n=\operatorname{sk}_{n-3}(\Delta^{n-1})\), and let \(X_n=\operatorname{DConf}(K_n,2)\) denote the ordered two-particle discretized configuration complex. It has a natural action of \(G_n=S_n\times C_2\), with vertex permutations and interchange of the two particles. Let \(P_n=\mathbb Z[[n]\times\{1,2\}]\) be the integral permutation lattice on the \(2n\) vertex-role pairs, and let \(\mathbf 1=\sum_{i=1}^n(e_{i,1}+e_{i,2})\). Define the one-dimensional character
\[
\epsilon_n(\sigma,t)=\operatorname{sgn}(\sigma)(-1)^{(n-1)t},\qquad \sigma\in S_n,\quad t\in\{0,1\}.
\]
Then the entire nonzero reduced integral homology, as an **integral group module**, is
\[
\boxed{\widetilde H_{n-3}(X_n;\mathbb Z)\cong_{\mathbb Z[G_n]}\mathbb Z_{\epsilon_n}\otimes_\mathbb Z(P_n/\mathbb Z\mathbf 1),}
\]
and all other reduced integral homology vanishes. This quotient lattice, rather than the augmentation *kernel*, is the canonical integral result; it is free of rank \(2n-1\).

Consequently the complete rational character for \(g=(\sigma,t)\) is
\[
\operatorname{tr}(g\mid\widetilde H_{n-3}(X_n;\mathbb Q))=
\begin{cases}
\operatorname{sgn}(\sigma)(2f(\sigma)-1),&t=0,\\
(-1)^n\operatorname{sgn}(\sigma),&t=1,
\end{cases}
\]
where \(f(\sigma)\) is the number of fixed vertices. For the unlabeled-particle quotient \(X_n/C_2\), reduced rational homology is concentrated in degree \(n-3\), of rank \(n-1\) for odd \(n\) and \(n\) for even \(n\). For the vertex-unlabeled quotient \(X_n/S_n\), all reduced rational homology vanishes.

## Assumptions and scope
\(\Delta^{n-1}\) is the full simplex on \([n]\), and its \((n-3)\)-skeleton consists of nonempty faces having at most \(n-2\) vertices. The regular CW cells of \(X_n\) are ordered products of simplex interiors indexed by disjoint nonempty \(A,B\subset[n]\) satisfying \(|A|,|B|\le n-2\). Their dimension is \(|A|+|B|-2\). Both points are labeled until a quotient is expressly taken. Homology is reduced and integral unless the coefficient field is indicated. No assertion is made for \(n<4\), for collision-permitting sink configurations, or for more than two particles.

## Proof
**1. The ambient deleted product is an equivariant sphere.** Put \(Y_n=\operatorname{DConf}(\Delta^{n-1},2)\). For a point \((x,y)\in Y_n\), the two vectors of barycentric coordinates have disjoint nonempty positive supports and each sums to one. The map
\[
(x,y)\longmapsto \frac{x-y}{\|x-y\|_2}
\]
is a \(G_n\)-equivariant homeomorphism from \(Y_n\) to the unit sphere of \(H_n=\{z\in\mathbb R^n:\sum_i z_i=0\}\). Its inverse sends a unit vector \(z\) to \((z^+/s,z^-/s)\), where \(s=\sum_i z_i^+=\sum_i z_i^->0\). Vertex permutations act orthogonally by permuting coordinates, with determinant \(\operatorname{sgn}(\sigma)\) on \(H_n\); particle exchange acts by antipodal \(z\mapsto-z\), whose sphere degree is \((-1)^{n-1}\). Hence \(\widetilde H_{n-2}(Y_n;\mathbb Z)=\mathbb Z_{\epsilon_n}\), with all other reduced homology zero.

**2. Exactly \(2n\) open top cells are removed.** An ambient cell indexed by \((A,B)\) is absent from \(X_n\) precisely when one part has at least \(n-1\) vertices. Since the parts are disjoint and nonempty, the only possibilities are \((A,B)=([n]\setminus\{i\},\{i\})\) or its exchange, for \(i\in[n]\). These are \(2n\) distinct cells of dimension \(n-2\). Every lower-dimensional cell of \(Y_n\) remains in \(X_n\); thus the cellular relative chain complex \(C_*(Y_n,X_n;\mathbb Z)\) is concentrated in degree \(n-2\).

**3. Orient by the ambient sphere.** Each ambient top cell receives its orientation from the chosen orientation on the sphere \(Y_n\). These orientations are carried by each \(g\in G_n\) into \(\epsilon_n(g)\) times the chosen orientation of the image cell. Therefore, with the removed-cell labels \((i,1)\) and \((i,2)\),
\[
C_{n-2}(Y_n,X_n;\mathbb Z)\cong_{\mathbb Z[G_n]}\mathbb Z_{\epsilon_n}\otimes P_n.
\]
The fundamental cellular cycle of the oriented sphere \(Y_n\) has coefficient \(+1\) on *every* top cell when these induced orientations are used. Its map to the relative group is thus \(1\mapsto\mathbf1\), with the common orientation twist. In particular the map is primitive and injective, not multiplication by any higher integer.

**4. The exact sequence determines everything.** Since \(X_n\) contains the entire \((n-3)\)-skeleton of \(Y_n\), the reduced relative long exact sequence, together with the sphere homology of \(Y_n\), gives a \(G_n\)-equivariant short exact sequence
\[
0\longrightarrow\mathbb Z_{\epsilon_n}\xrightarrow{1\mapsto\mathbf1}\mathbb Z_{\epsilon_n}\otimes P_n\longrightarrow\widetilde H_{n-3}(X_n;\mathbb Z)\longrightarrow0.
\]
It also gives vanishing in every other reduced degree. Because \(\mathbf1\) is primitive in the free abelian group \(P_n\), the quotient is torsion-free and has rank \(2n-1\). No use of fieldwise experiments is needed for this all-parameter conclusion.

**5. Characters and quotient homology.** For \(t=0\), the permutation on vertex-role pairs has \(2f(\sigma)\) fixed points; for \(t=1\), it has none. The trace on \(P_n/\mathbb Q\mathbf1\) is therefore \(2f(\sigma)-1\) or \(-1\), respectively. Multiplication by \(\epsilon_n\) proves the displayed character. Over \(\mathbb Q\), particle exchange on \(P_n/\mathbb Q\mathbf1\) has invariant dimension \(n-1\) and anti-invariant dimension \(n\); applying the orientation twist produces the parity dichotomy. The \(S_n\)-module is the sign twist of two vertex permutation modules minus the trivial diagonal; for \(n\ge4\), neither the trivial module nor the standard \(S_n\)-module acquires invariants after this sign twist. Finally, for a finite group action the rational homology of the topological quotient identifies with rational homology invariants (cellular subdivision followed by averaging). This proves both quotient statements.

## Verification
The accompanying dependency-free Python 3 checker constructs all product cells. For \(n=4,5,6\), exact binary cellular-boundary rank calculations give the predicted Betti dimensions, and for \(n=4,5,6,7\), signed cellular Lefschetz traces match the character for the identity, a transposition, a long cycle, and vertex reversal, each with both particle-exchange states: 32 character cases. It also constructs a primitive top cellular fundamental cycle of the full deleted product, verifies every codimension-one incidence cancels, all removed-cell coefficients have absolute value one, and the orientation degree of each tested action. The finite tests corroborate the stated general proof rather than establish it.

Run from the extracted package directory: `python3 verify_deleted_skeleton.py`.

## Relationship to prior work
González and González, *An algorithmic discrete gradient field for non-colliding cell-like objects and the topology of pairs of points on skeleta of simplexes*, arXiv:2307.14454v1, Theorem 1.2(III), established the **nonequivariant** homotopy type \(X_n\simeq\bigvee^{2n-1}S^{n-3}\). Their Remark 1.7 notes that their optimal gradient field is not particle-swap equivariant. The present finding does not claim a new Betti rank or wedge decomposition: its point is the complete \(\mathbb Z[S_n\times C_2]\)-lattice, whose quotient structure and parity-sensitive quotient consequences require additional orientation-sensitive information.

Abrams, Gay and Hower, *Discretized configurations and partial partitions*, arXiv:1009.2935v2, studied full-simplex discretized configurations and partial partitions. Their introductory discussion explicitly does not determine the natural symmetric-group homology action. Its full-simplex sphere is the ambient space used here, but the codimension-two-skeleton subcomplex and integral vertex-by-particle action are distinct.

Related calculations for particles on complete-graph **sink** complexes concern collision rules and spaces different from \(X_n\), so their character formulas do not imply the present integral lattice.

## Limitations
The theorem treats exactly the codimension-two skeleton, two distinct labeled particles, and its canonical symmetry group. It gives no ring structure or corresponding classification for other skeleton depths or more than two particles. The rational quotient statements do not assert torsion-freeness for the quotient spaces. Although targeted scholarly and published-record comparisons found no covering symmetry formula, an equivalent unindexed derivation remains possible. Independent external mathematical validation has not been performed.

## References
1. E. J. González and J. González, *An algorithmic discrete gradient field for non-colliding cell-like objects and the topology of pairs of points on skeleta of simplexes*, arXiv:2307.14454v1 (first public version: 2023-07-26), Theorem 1.2(III) and Remark 1.7. https://arxiv.org/abs/2307.14454
2. A. Abrams, D. Gay and V. Hower, *Discretized configurations and partial partitions*, arXiv:1009.2935v2 (2011), Theorem 1.1 and Section 1.3. https://arxiv.org/abs/1009.2935
