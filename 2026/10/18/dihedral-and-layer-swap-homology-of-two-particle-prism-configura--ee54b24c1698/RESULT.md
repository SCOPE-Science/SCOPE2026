# Dihedral and layer-swap homology of two-particle prism configurations

## Finding
For every integer \(n\ge5\), let \(G_n=C_n\square K_2\) be the \(n\)-gonal prism graph and let \(X_n=\operatorname{UConf}_2(|G_n|)\) be the space of unordered pairs of distinct points in its geometric realization. Index vertices by \((i,t)\), with \(i\in\mathbb Z/n\mathbb Z\) and \(t\in\{0,1\}\). The natural group \(D_n\times C_2\) acts by rotations \(r(i,t)=(i+1,t)\), polygon reflections \(s(i,t)=(-i,t)\), and layer exchange \(h(i,t)=(i,1-t)\).

Write \(F_n=\{Q_0,\ldots,Q_{n-1},U_0,U_1\}\) for the \(n\) rectangular side faces and two caps of the planar prism embedding. Let \(\epsilon(r^ks^ah^b)=(-1)^{a+b}\). Let \(\mathbb Q[F_n]\) be the permutation module on these \(n+2\) faces.

The full ordinary rational homology representations are
\[
H_0(X_n;\mathbb Q)=\mathbb Q,\qquad
H_1(X_n;\mathbb Q)\cong\epsilon\otimes\mathbb Q[F_n],
\]
\[
H_2(X_n;\mathbb Q)\cong
\mathbb Q_{\chi_h}\oplus
\operatorname{span}_{\mathbb Q}\{e_i\wedge e_j: i-j\not\equiv0,\pm1\pmod n\},
\qquad H_j(X_n;\mathbb Q)=0\quad(j>2),
\]
where the second summand is the subrepresentation of \(\bigwedge^2\mathbb Q^n\) on unordered nonadjacent pairs of side faces, with the usual antisymmetric permutation signs, and \(\chi_h(r^ks^ah^b)=(-1)^b\). The displayed second-homology decomposition holds already over \(\mathbb Z\) using the corresponding natural product-torus classes. In particular, the integral homology is torsion-free with Betti numbers \((1,n+2,1+n(n-3)/2)\).

Set \(g=r^ks^ah^b\) and define \(q_g=\#\{i\in\mathbb Z/n\mathbb Z:k+(-1)^a i-a\equiv i\pmod n\}\), the number of side faces fixed by \(g\). Then
\[
\operatorname{tr}(g\mid H_1)=(-1)^{a+b}(q_g+2\mathbf 1_{b=0}),
\qquad
\operatorname{tr}(g\mid H_2)=(-1)^b+p_n(k,a).
\]
For rotations \((a=0)\), \(p_n(0,0)=n(n-3)/2\); a nonidentity non-half-turn rotation has \(p_n=0\); and, if \(n\) is even, the half-turn has \(p_n=-n/2\). For reflections \((a=1)\), \(p_n=(3-n)/2\) when \(n\) is odd, and \(p_n=(4-n)/2\) when \(n\) is even. Thus these formulas give the character of every group element.

For quotient spaces, taking rational invariants gives
\[
(\beta_1,\beta_2)(X_n/C_n)=(3,\lfloor(n-1)/2\rfloor),\quad
(\beta_1,\beta_2)(X_n/D_n)=(0,1),\quad
(\beta_1,\beta_2)(X_n/(D_n\times C_2))=(0,0).
\]
In every case \(\beta_0=1\) and higher Betti numbers vanish. In particular, the quotient by all polygon and layer symmetries is rationally acyclic, whereas the quotient by polygon symmetries alone retains one rational degree-two class.

## Assumptions and scope
All spaces use the ordinary (not sink or Borel–Moore) two-point unordered collision-free configuration space of the topological graph. The graph has exactly \(2n\) vertices, \(3n\) edges, and an embedded sphere-face set of \(n+2\) members. The group \(D_n\times C_2\) is the explicitly specified geometric symmetry group; for \(n\ge5\) it is also the full graph automorphism group. Statements about rational representations are representation isomorphisms, not merely identities of Betti numbers. For the integral assertion only degree two is identified equivariantly; no integral splitting of degree-one homology is asserted. All quotient statements concern rational singular homology of the topological quotient.

## Proof
**1. Cellular model and boundary.** The standard two-particle deleted cubical model is a deformation retract in this case: its cells are unordered sets of two graph cells having disjoint closures. The required subdivision conditions are that every simple cycle contain at least \(2+1=3\) edges and that every path between distinct vertices of degree other than two contain at least \(2-1=1\) edge. Both hold: the prism has girth four and each edge has length one. The retract is natural for graph automorphisms, so cellular traces compute the given action. The cells consist of unordered pairs of distinct vertices, vertex-and-nonincident-edge pairs, and pairs of vertex-disjoint edges. Their numbers are
\[
 c_0=n(2n-1),\qquad c_1=6n(n-1),\qquad c_2=\frac{9n^2-15n}{2}.
\]
An oriented two-cell \([e,f]\), with graph edges \(e<f\) oriented from smaller to larger vertex, has boundary \([\partial e,f]-[e,\partial f]\). No cells occur above dimension two, and the complex is connected.

**2. Integral top homology and natural action.** The known planar two-particle face-cycle description (Barnett–Farber in the ordered setting, and Ko–Park in the unordered planar braid setting) gives that \(H_2\) is free of rank equal to the number of unordered pairs of vertex-disjoint boundaries of bounded faces in the spherical embedding. Equivalently, the rank follows from the planar graph-braid computation. For a prism these are the pair of caps, and each pair of nonadjacent side squares: there are \(1+n(n-3)/2\) such pairs.

For two faces \(A,B\) with disjoint vertex boundaries, orient their embedded boundary cycles consistently using an orientation of the sphere. The alternating product chain
\[
 z_{A,B}=\sum_{e\in\partial A}\sum_{f\in\partial B}
 \operatorname{sgn}_{A}(e)\operatorname{sgn}_{B}(f)[e,f]
\]
with \([f,e]=-[e,f]\), is an integral two-cycle: every one-dimensional boundary term cancels. These cycles form an integral basis, not just a rational one. Indeed, for each nonadjacent \(Q_i,Q_j\), take the two-cell with top rim edges \(((i,0),(i+1,0))\) and \(((j,0),(j+1,0))\); it occurs with coefficient \(\pm1\) in precisely that square-pair torus and no other listed torus. For the cap pair take one top rim edge and the corresponding bottom rim edge; that cell occurs with coefficient \(\pm1\) only in the cap-pair torus. This produces a diagonal \(\pm1\) coefficient minor of size \(1+n(n-3)/2\). Thus these independent classes span a primitive sublattice of the full free group of the same rank and hence the entire group.

A graph symmetry acts on each consistently oriented planar facial boundary by the degree of its action on the ambient oriented sphere, namely \(\epsilon(g)=(-1)^{a+b}\), and permutes the faces. Its product-torus cycle consequently acquires \(\epsilon(g)^2=1\), and acquires an additional minus sign exactly when the two face factors are interchanged. Polygon reflections preserve each cap setwise; layer exchange interchanges the two caps. Consequently, the cap-pair torus is the character \(\chi_h\), while side-square pairs carry the signed exterior permutation representation claimed. Counting invariant nonadjacent pairs with sign gives the stated \(p_n(k,a)\): a nontrivial rotation fixes such a pair only when it is an even-order half-turn, when it swaps \(n/2\) opposite pairs; an odd-polygon reflection swaps \((n-3)/2\) admissible pairs, and an even-polygon reflection has net trace \((4-n)/2\).

**3. First-homology character.** Write \(A\) for the permutation of vertices induced by \(g\). For each geometric edge \(e=[u_e,v_e]\), let \(P(e)\) be its image edge, and let \(\eta(e)=1\) when \(A(u_e)<A(v_e)\), and \(-1\) otherwise. Denote by \(\mathcal E\) the edge set and by \(\mathcal D\) the set of unordered disjoint edge pairs. The alternating signed cellular trace is exactly
\[
\begin{aligned}
L(g)={}&\sum_{\{u,v\},u\ne v}\mathbf1_{\{A(u),A(v)\}=\{u,v\}}\\
&-\sum_{e\in\mathcal E}\sum_{v\notin e}
\eta(e)\mathbf1_{P(e)=e}\mathbf1_{A(v)=v}\\
&+\sum_{\{e,f\}\in\mathcal D} \eta(e)\eta(f)
\left[\mathbf1_{P(e)=e,P(f)=f}-\mathbf1_{P(e)=f,P(f)=e}\right].
\end{aligned}
\]
All terms are finite explicit modular equalities of \(n\)-indexed edges and vertices. Substituting \(A(i,t)=(k+(-1)^a i,t\mathbin{\mathrm{xor}}b)\) and grouping the indicator sums by fixed vertices, fixed edges, and exchanged edge pairs yields the following exhaustive table. Each entry gives \((L(g))_{b=0},(L(g))_{b=1}\):

| Polygon action \(r^ks^a\) | \(b=0\) | \(b=1\) |
|---|---:|---:|
| Identity | \(n(n-5)/2\) | \(n(n-1)/2\) |
| Nonidentity rotation other than half-turn | \(0\) | \(0\) |
| Half-turn (\(n\) even) | \(-n/2\) | \(-n/2\) |
| Reflection (\(n\) odd) | \((13-n)/2\) | \((1-n)/2\) |
| Reflection, \(n\) even, \(k\) even | \((12-n)/2\) | \((4-n)/2\) |
| Reflection, \(n\) even, \(k\) odd | \((16-n)/2\) | \(-n/2\) |

The table has no exceptional parameters beyond the stated parity and half-turn cases: the only congruences to solve are \(2i\equiv k\) and \(2i+1\equiv k\pmod n\), plus \(2k\equiv0\pmod n\), whose solution counts follow immediately from parity. The displayed modular indicator expression is also a direct all-parameter method for checking every table entry, without assuming any empirical periodicity. As \(X_n\) is connected and two-dimensional, the Lefschetz identity gives \(\operatorname{tr}_{H_1}(g)=1+\operatorname{tr}_{H_2}(g)-L(g)\). Inserting the signed top-homology character and the table gives precisely \((-1)^{a+b}(q_g+2\mathbf1_{b=0})\). This is the character of \(\epsilon\otimes\mathbb Q[F_n]\); rational character equality implies a representation isomorphism. Ko–Park's planar torsion-freeness theorem, or the equivalent first-homology presentation, gives integral \(H_1\cong\mathbb Z^{n+2}\), without asserting an equivariant integral splitting.

**4. Quotients.** For a finite group acting on a space, rational homology of its orbit space is the invariant part of rational homology. Rotation invariants in the degree-one sign-twisted face module have dimension three; dihedral reflections negate all three. In degree two, the cap-pair class is fixed by \(D_n\) and negated by \(h\). Each rim-pair orbit with cyclic separation strictly between one and \(n/2\) contributes one rotation-invariant line: there are \(\lfloor(n-1)/2\rfloor-1\) such lines, so together with the cap class the rotation-fixed rank is \(\lfloor(n-1)/2\rfloor\). Every such rim-pair orbit is reversed by a polygon reflection exchanging the two paired squares, killing its dihedral-invariant line. Thus precisely the quoted quotient Betti vectors result.

## Verification
The accompanying self-contained Python file `verify_prism.py` reconstructs the unordered deleted cubical model and tests the signed Lefschetz identities for **every** element of \(D_n\times C_2\) with \(4\le n\le18\). For \(4\le n\le10\) it separately checks all proposed torus-chain boundaries, the diagonal unit coefficient minor, and the rank of the second boundary over \(\mathbb F_2\), obtaining the predicted Betti numbers. These are exhaustive **finite** confirmations; the all-parameter theorem is proved by the indicator identities, the face-basis argument, and the cited planar configuration-space results. Run with `python3 verify_prism.py`; it needs only the Python standard library.

## Relationship to prior work
Barnett and Farber establish the ordered planar two-point intersection-form/face-pair framework; Ko and Park determine planar graph-braid first homology and describe the commutator/tori corresponding to disjoint face cycles. The planar nonequivariant rank and geometric face-pair description are **not** claimed as new. The result here specifies the full, simultaneous \(D_n\times C_2\) action on ordinary two-point **homology** for every prism size, including the integral top module, exact first-homology character, and different rational quotients by rotation, polygon dihedral, and full layer symmetries. Related published results on symmetry modules of other graph configurations or on independence/Čech complexes of prisms do not furnish this ordinary two-particle representation. Source coverage has not been exhaustively established for unpublished or difficult-to-index material.

## Limitations
No integral isomorphism \(H_1\cong\epsilon\otimes\mathbb Z[F_n]\) is claimed, and rationally acyclic quotients are not claimed contractible or integral-acyclic. This work does not classify cup products, braid-group presentations, higher-particle spaces, or finite exceptions outside \(n\ge5\). The finite verifier does not certify infinitely many parameter values or publication priority; independent scientific review has not been performed.

## References
1. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180v1 (first public version 2009-03-12), https://arxiv.org/abs/0903.2180.
2. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (2011-01-13), https://arxiv.org/abs/1101.2648.
3. B. An and T. Maciazek, *Geometric presentations of braid groups for particles on a graph*, Communications in Mathematical Physics, DOI:10.1007/s00220-021-04095-x.
