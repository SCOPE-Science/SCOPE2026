# Two complementary Specht modules in two-particle complete-bipartite configuration homology

## Finding

For integers \(m,n\ge3\), write \(K_{m,n}\) for the simple complete bipartite graph and \(X_{m,n}=\operatorname{UConf}_2(|K_{m,n}|)\) for the space of *unordered pairs of distinct points* on its geometric realization. The group \(S_m\times S_n\) acts by relabeling the vertices of its two parts.

Let \(S^\lambda\) denote the rational Specht module of partition \(\lambda\). Put
\[
 B_k=\begin{cases}0&k=3,\\ S^{(k-2,2)}&k\ge4,\end{cases}
 \qquad C_k=S^{(k-2,1,1)}\quad(k\ge3).
\]
Then the complete second rational homology representation is
\[
 \boxed{H_2(X_{m,n};\mathbb Q)\cong (B_m\boxtimes C_n)\oplus(C_m\boxtimes B_n).}
\]
In particular, \(H_2(X_{m,n};\mathbb Q)^{S_m\times S_n}=0\), and the second Betti number equals
\[
 \frac{m(m-3)(n-1)(n-2)+(m-1)(m-2)n(n-3)}4.
\]
For a permutation \(\sigma\in S_k\), let \(f(\sigma)\) and \(t(\sigma)\) be its numbers of fixed points and two-cycles. Define
\[
 b_k(\sigma)=\binom{f(\sigma)}2+t(\sigma)-f(\sigma),\qquad
 c_k(\sigma)=\binom{f(\sigma)}2-t(\sigma)-f(\sigma)+1.
\]
Here \(b_3=0\). For every \((\sigma,\tau)\in S_m\times S_n\) the exact trace on degree-two homology is
\[
 \operatorname{tr}((\sigma,\tau)|H_2)=b_m(\sigma)c_n(\tau)+c_m(\sigma)b_n(\tau).
\]
When \(m=n\), every graph automorphism exchanging the two parts acts with trace zero on \(H_2\). For \(m=n\ge4\) this identifies the representation of the full graph automorphism group \((S_m\times S_m)\rtimes C_2\) as
\[
 \operatorname{Ind}_{S_m\times S_m}^{(S_m\times S_m)\rtimes C_2}(B_m\boxtimes C_m).
\]

## Assumptions and scope

The graph is treated as a one-dimensional CW complex, not as a finite discrete vertex set. Collision of the two points is forbidden everywhere, *including vertices*; vertex-sink variants are a different problem. All representations and decompositions in the theorem are over \(\mathbb Q\). The graph \(K_{m,n}\) is connected, nonplanar and three-vertex-connected for \(m,n\ge3\). The exterior tensor product notation \(\boxtimes\) refers to the separate actions of the two symmetric groups.

## Proof

**1. Natural first-homology representation.** A continuous unordered pair moving in the graph has a canonical total trajectory (sum of its two one-dimensional traces), giving an equivariant map
\[
 p_*:H_1(X_{m,n};\mathbb Q)\longrightarrow H_1(|K_{m,n}|;\mathbb Q).
\]
Every graph-cycle class is a rational linear combination of four-cycle classes. Given a four-cycle, at least one graph vertex lies outside it because \(m,n\ge3\). Holding one point at that external vertex and moving the other around the cycle proves that \(p_*\) is surjective. Ko and Park's first-homology theorem for unordered graph braid groups, Theorem 3.16 of [1], implies that a simple nonplanar three-connected graph has rational first Betti number equal to its graph cycle rank. Hence source and target have common dimension \((m-1)(n-1)\), so \(p_*\) is an equivariant isomorphism. With \(U_k=\mathbb Q^{[k]}\) the natural permutation representation, graph edge-chains are \(U_m\boxtimes U_n\), vertex-chains are \(U_m\oplus U_n\), and degree-zero homology is trivial. Thus
\[
 H_1(X_{m,n};\mathbb Q)\cong (U_m-\mathbf1)\boxtimes(U_n-\mathbf1).
\]
The last identity is an equality of actual modules because the usual graph chain sequence splits equivariantly in characteristic zero.

**2. Equivariant cubical cells.** The standard two-particle deleted-product cubical complex is a deformation retract of \(X_{m,n}\): each path between essential vertices has at least one edge, and every simple cycle has at least three edges, satisfying the two-particle subdivision conditions in [1]. Its cells are pairs of disjoint closed graph cells. We orient each graph edge from the \(m\)-part toward the \(n\)-part.

Let \(P_k=\mathbb Q^{\binom{[k]}2}\) be the permutation module on unordered distinct pairs of vertices and \(W_k=\bigwedge^2U_k\). Put \(Q_k=\mathbb Q^{\{(i,j):i\ne j\}}\); transposition of the ordered pair yields the equivariant splitting \(Q_k\cong P_k\oplus W_k\). Counting disjoint graph cells gives isomorphisms of \(S_m\times S_n\)-modules:
\[
 \begin{aligned}
 C_0&\cong P_m\oplus P_n\oplus(U_m\boxtimes U_n),\\
 C_1&\cong (Q_m\boxtimes U_n)\oplus(U_m\boxtimes Q_n),\\
 C_2&\cong (W_m\boxtimes P_n)\oplus(P_m\boxtimes W_n).
 \end{aligned}
\]
For the last splitting, select two distinct vertices in each part. There are exactly two disjoint-edge pairings of the resulting four vertices. Their sum and difference transform with, respectively, the alternating representation on one chosen vertex pair and the ordinary pair-permutation representation on the other. Interchanging the two occupied edges reverses the oriented square, supplying the required sign. The two eigenspaces give the displayed direct sum; this respects all relabelings, not merely dimensions.

**3. The equivariant Euler identity.** The cubical model is connected and two-dimensional, so in the rational representation ring,
\[
 [H_2]=[C_2]-[C_1]+[C_0]-[\mathbf1]+[H_1].
\]
Set \(A_k=U_k-\mathbf1\). For \(k\ge4\), the standard Young permutation-module decompositions are
\[
 P_k=\mathbf1\oplus A_k\oplus B_k,
 \qquad W_k=A_k\oplus C_k.
\]
These remain valid at \(k=3\) with \(B_3=0\). Substitution of \(Q_k=P_k\oplus W_k\) and \(H_1=A_m\boxtimes A_n\) into the Euler identity cancels every term except
\[
 [H_2]=[B_m\boxtimes C_n]+[C_m\boxtimes B_n].
\]
Maschke's theorem over \(\mathbb Q\) upgrades equality of representation classes to the displayed module isomorphism. Hook-length dimensions yield the Betti formula. The standard character formulas for \(P_k\), \(U_k\), and \(\bigwedge^2U_k\) give the stated values of \(b_k\) and \(c_k\). Neither \(B_k\) nor \(C_k\) contains a trivial constituent, proving the invariant vanishing.

**4. Interchange of equal parts.** Suppose \(m=n\). A bipartition-interchanging automorphism has no fixed vertex. Its two-cycles on vertices correspond to fixed points of the composite permutation of one part induced by applying the automorphism twice; let their number be \(f\). Its trace on zero-cells is \(f\), on one-cells it is \(0\) (no fixed spectator vertex), and on two-cells it is \(0\): individually fixed disjoint-edge squares and swapped-edge squares occur in sign-opposite pairs. The same automorphism has graph first-homology trace \(1-f\), by the oriented graph-chain exact sequence, since it reverses each fixed edge. The Euler identity therefore gives \(\operatorname{tr}(g|H_2)=f-0+0-1+(1-f)=0\). For \(m\ge4\), the two distinct restricted constituents \(B_m\boxtimes C_m\) and \(C_m\boxtimes B_m\) are exchanged by the extra involution; the module is consequently the stated induced representation.

## Verification

The standalone program `verify.py` builds the cubical chain complex independently from disjoint vertices and edges, checks that the composition of consecutive boundary maps vanishes, and computes exact dimensions of the two differentials by arithmetic in \(\mathbb F_{1000003}\). These finite-field ranks are consistency checks only: the unrestricted rational theorem follows from the above argument and Ko–Park's published first-homology theorem.

For \((m,n)=(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)\), the finite-field consistency ranks agree with the rationally predicted second Betti numbers \(0,2,5,12,27,60\). For the first, second and fourth pairs the program also checks every side-preserving automorphism's signed cellular Lefschetz number against the claimed Specht character, and every bipartition swap in the balanced cases. A recorded run ends with `VERIFY_OK`.

## Relationship to prior work

Ko and Park [1, Theorem 3.16] determine the non-equivariant first homology of unordered graph braid groups, including its rational rank on nonplanar triconnected graphs. They also give a general **nonequivariant second-Betti-number formula** in Corollary 3.17, derived by an Euler-characteristic calculation. Neither result determines the degree-two symmetry module or the irreducible constituents calculated here. Barnett [2, Section 5.2] calculates second Betti numbers and intersection forms for the *ordered* two-point configuration spaces of complete bipartite graphs; the rational representation of the unordered space under both part-permutation groups is not stated there. Barnett and Farber [3] develop two-particle intersection methods, especially for planar graphs. The new result combines the older first-homology rank with a direct equivariant cubical-cell decomposition; it does **not** assert that the prior nonequivariant ranks were unknown.

## Limitations

The conclusion classifies rational representations only, not integer representation lattices, torsion, multiplicative cohomology, higher particle numbers or vertex-sink collision models. Its novelty assessment is literature-dependent; hidden equivalent formulations may exist. Its proof uses the published Ko–Park first-homology theorem as a premise, and the standalone finite calculations do not establish that theorem. No independent mathematical audit is asserted.

## References

[1] K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (first posted 2011-01-13), especially Theorem 3.16 and the discrete-model definitions. https://arxiv.org/abs/1101.2648

[2] K. Barnett, *The Configuration Space of Two Particles Moving on a Graph*, Durham University thesis (2010), Section 5.2 and Corollary 5.2.5. https://etheses.durham.ac.uk/293/

[3] K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, Algebraic & Geometric Topology 9 (2009), 593–624; preprint arXiv:0903.2180. https://arxiv.org/abs/0903.2180
