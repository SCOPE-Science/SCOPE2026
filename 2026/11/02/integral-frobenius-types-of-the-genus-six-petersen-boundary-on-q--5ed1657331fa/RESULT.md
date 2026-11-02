# Integral Frobenius types of the genus-six Petersen boundary on quintic del Pezzo surfaces

## Finding

**Theorem.** Let \(k=\mathbb F_q\) be any finite field and \(S/k\) a smooth del Pezzo surface of degree five. Let \(B\subset S\) be the reduced union of its ten geometric \((-1)\)-curves. It is a geometrically connected, stable, nodal curve of arithmetic genus six. Its geometric components, nodes and branches number \(10\), \(15\) and \(30\), respectively. Its divisor class is \(-2K_S\).

The Frobenius action on the configuration is specified by a conjugacy class \(\lambda\) of \(S_5\), equivalently a partition of five. The following table determines, **up to isomorphism over \(k\)**, the connected generalized Jacobian \(J_B=\operatorname{Pic}^0_{B/k}\), its entire finite abelian group \(J_B(k)\), and the number of points on \(B\) itself. Write \(R_m=\operatorname{Res}_{\mathbb F_{q^m}/k}\mathbb G_m\), let \(N_2\) denote the norm-one torus of \(\mathbb F_{q^2}/k\), and let \(U_4=\operatorname{Res}_{\mathbb F_{q^2}/k}(\operatorname{Res}^{(1)}_{\mathbb F_{q^4}/\mathbb F_{q^2}}\mathbb G_m)\). Thus \(U_4\) has dimension two and rational points cyclic of order \(q^2+1\). Denote by \(C_n\) a cyclic group of order \(n\); \(C_1\) is trivial.

| Frobenius type \(\lambda\) | Isomorphism type of \(J_B\) | Abelian group \(J_B(k)\) | \(\#B(k)\) |
|---|---|---|---|
| \((5)\) | \(R_5\times\mathbb G_m\) | \(C_{q^5-1}\times C_{q-1}\) | \(0\) |
| \((4,1)\) | \(R_4\times U_4\) | \(C_{q^4-1}\times C_{q^2+1}\) | \(1\) |
| \((3,2)\) | \(R_6\) | \(C_{q^6-1}\) | \(q+1\) |
| \((3,1,1)\) | \(R_3^2\) | \(C_{q^3-1}^2\) | \(q+1\) |
| \((2,2,1)\) | \(R_2^2\times N_2^2\) | \(C_{q^2-1}^2\times C_{q+1}^2\) | \(2q+3\) |
| \((2,1,1,1)\) | \(R_2^3\) | \(C_{q^2-1}^3\) | \(4q+1\) |
| \((1,1,1,1,1)\) | \(\mathbb G_m^6\) | \(C_{q-1}^6\) | \(10q-5\) |

These are **integral torus isomorphisms**, not merely rational-representation identities or equality of group orders. In particular, the type \((3,2)\) gives a cyclic group of order \(q^6-1\); type \((5)\) gives no rational point on the curve despite a split one-dimensional torus factor; and type \((4,1)\) gives one rational point (a nonsplit node), even though none of the ten components is individually defined over \(k\).

The complete zeta function of \(B\), over every finite extension of \(k\), is also determined. Let \(v_d,e_d,b_d\) count Frobenius orbits of length \(d\) on its ten components, fifteen nodes and thirty node-branches, respectively. Set \(r:s\) in the table to mean \(s\) distinct orbits of length \(r\), with omitted lengths having zero multiplicity.

| \(\lambda\) | Component orbits \(v\) | Node orbits \(e\) | Branch orbits \(b\) |
|---|---|---|---|
| \((5)\) | \(5:2\) | \(5:3\) | \(5:6\) |
| \((4,1)\) | \(2:1,4:2\) | \(1:1,2:1,4:3\) | \(2:1,4:7\) |
| \((3,2)\) | \(1:1,3:1,6:1\) | \(3:1,6:2\) | \(3:2,6:4\) |
| \((3,1,1)\) | \(1:1,3:3\) | \(3:5\) | \(3:10\) |
| \((2,2,1)\) | \(1:2,2:4\) | \(1:3,2:6\) | \(1:2,2:14\) |
| \((2,1,1,1)\) | \(1:4,2:3\) | \(1:3,2:6\) | \(1:6,2:12\) |
| \((1,1,1,1,1)\) | \(1:10\) | \(1:15\) | \(1:30\) |

With \(T\) the formal zeta variable, the formula is

\[
Z(B,T)=\prod_{d\ge1}\frac{(1-T^d)^{b_d-v_d-e_d}}{(1-q^dT^d)^{v_d}}.
\]

Equivalently, for every integer \(n\ge1\),

\[
\# B(\mathbb F_{q^n})=(q^n+1)\sum_{d\mid n}d\,v_d-\sum_{d\mid n}d\,b_d+\sum_{d\mid n}d\,e_d.
\]

## Assumptions and scope

The surface is smooth, its anticanonical degree is five, and its base field is finite. The characteristic is **unrestricted**, including two, three and five. The ten curves are taken geometrically and then united as a **reduced** \(k\)-subscheme; individual components need not be rational. The theorem classifies the connected generalized Jacobian, not the component group of the full Picard functor or any Jacobian of a smooth member of the Wiman–Edge pencil. All seven types correspond to Frobenius conjugacy classes of permutations on five labels; the conclusion applies to each actual surface of the indicated class.

## Proof

**1. Geometry and arithmetic genus.** Over an algebraic closure, write \(S\) as the blow-up of \(\mathbb P^2\) in four general points, with hyperplane class \(H\) and exceptional divisors \(E_1,\dots,E_4\). The ten \((-1)\)-curves are the four \(E_i\) and the six transforms \(L_{ij}=H-E_i-E_j\). Summing their classes gives \(6H-2\sum_iE_i=-2K_S\). Classically, they can also be indexed by the ten two-element subsets of \(\{1,2,3,4,5\}\), with two components intersecting transversely if and only if the subsets are disjoint. This is the Petersen graph: it has ten vertices, fifteen edges, degree three at every vertex, and no triangles. Thus all intersection points are distinct ordinary nodes, with thirty branches. The curve is connected, and each rational component has three nodes; hence it is stable. Its arithmetic genus is \(15-10+1=6\).

**2. Descent and normalization.** The intrinsic automorphism group of the ten-curve incidence graph is \(S_5\). Arithmetic Frobenius consequently acts as a permutation \(\sigma\) on the five labels. For the normalization \(\nu:\widetilde B\to B\), let \(D\) be the reduced node scheme and \(\widetilde D=\nu^{-1}D\) the branch scheme. On points over every finite extension,

\[
\#B(\mathbb F_{q^n})=\#\widetilde B(\mathbb F_{q^n})-\#\widetilde D(\mathbb F_{q^n})+\#D(\mathbb F_{q^n}).
\]

Every Frobenius orbit of \(d\) geometrically rational components contributes the zeta factor \(((1-T^d)(1-q^dT^d))^{-1}\), because a smooth genus-zero curve over a finite field is a projective line. Each branch orbit contributes \((1-T^d)\), while each node orbit contributes \((1-T^d)^{-1}\). Multiplying gives the displayed zeta formula and extension-field point counts.

**3. Integral character lattice.** As every normalized component is geometrically \(\mathbb P^1\), the normalization exact sequence for units identifies the connected generalized Jacobian with a six-dimensional torus whose **integral character lattice** is \(H_1(\Gamma,\mathbb Z)\), where \(\Gamma\) is the Petersen incidence graph. With arbitrary fixed orientations of the edges, there is a Frobenius-equivariant exact sequence

\[
0\longrightarrow H_1(\Gamma,\mathbb Z)\longrightarrow\mathbb Z^{15}\xrightarrow{\partial}\mathbb Z^{10}\longrightarrow\mathbb Z\longrightarrow0.
\]

Here \(\sigma\) permutes vertices and acts as a **signed** permutation of oriented edges; this sign is necessary when it exchanges the two endpoints of a node. The rank of the kernel is \(15-10+1=6\). A spanning tree gives six fundamental cycles as an integral basis. Thus the integral matrix \(M_\sigma\) of Frobenius is derived without choices outside the given configuration.

**4. Integral block classification.** Let \(R_m\) denote the rank-\(m\) integral cyclic-permutation module; let \(N_2\) denote the rank-one sign module; and let \(U_4\) denote the rank-two module with Frobenius matrix \(\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\). In the preceding integral cycle basis, an explicit collection of columns \(u,\sigma u,\ldots\), together with any sign or invariant columns stated below, has determinant \(\pm1\) for each representative \(\sigma\):

- \((5)\): five translates of the first unit cycle and the invariant vector \((-1,1,0,-1,0,0)\), yielding \(R_5\oplus\mathbb Z\).
- \((4,1)\): four translates of the first unit cycle and the third unit cycle together with its translate, yielding \(R_4\oplus U_4\).
- \((3,2)\): six translates of the first unit cycle, yielding \(R_6\).
- \((3,1,1)\): three translates each of the first and second unit cycles, yielding \(R_3^2\).
- \((2,2,1)\): two translates each of the third and fourth unit cycles and the first two (sign) unit cycles, yielding \(R_2^2\oplus N_2^2\).
- \((2,1,1,1)\): two translates each of the first, third and fourth unit cycles, yielding \(R_2^3\).
- \((1,1,1,1,1)\): the identity basis, yielding \(\mathbb Z^6\).

The representative permutations and spanning-tree basis are canonicalized lexicographically by `verify.py`, and every column and exact unimodular determinant is printed by that program. The result for any conjugate permutation follows by relabeling the five indices. The module blocks correspond, by the integral equivalence between finite-field tori and Frobenius lattices, to the named Weil restrictions and norm-one tori. Their rational groups are the corresponding cyclic multiplicative groups, proving **group isomorphism**, not just cardinality. For example, in type \((3,2)\), the six-cycle module is the character module of \(R_6\), whose rational points are \(\mathbb F_{q^6}^{\times}\).

**5. Exhaustion.** There are exactly seven conjugacy types in \(S_5\). Acting on the ten pairs, fifteen unordered disjoint pairs and thirty oriented incidences determines the three Frobenius orbit spectra in the tables. A complete enumeration of all \(120\) permutations (not a sample) independently checks the classification and the seven unimodular integral module decompositions. The eigenvalue characteristic polynomial of the torus can also be reconstructed directly from the exact graph chain sequence:

\[
\det(tI-M_\sigma)=(t-1)\,\frac{\det(tI-S_\sigma)}{\det(tI-V_\sigma)},
\]

where \(S_\sigma\) is the signed edge permutation and \(V_\sigma\) the vertex permutation. A separate fundamental-cycle matrix calculation reproduces this polynomial. The rational representation agrees with \(\bigwedge^2\) of the four-dimensional standard \(S_5\)-representation; this rational character identity alone would *not* establish the integral torus decompositions. The exact integral block certificates do.

## Verification

Run `python3 verify.py` using Python 3.9 or later; no external packages or files are required. It builds the Petersen graph from all unordered pairs of five labels and independently constructs its six-cycle lattice from a spanning tree. It tests all \(120\) permutations, all seven conjugacy classes, node/branch orbits, the signed-edge characteristic-polynomial identity, a separate integer characteristic polynomial of the six-cycle action, the exterior-square trace identity, and extension-field point counts for degrees one through twelve. It then constructs explicit integral block bases for each class, verifies each integer determinant has absolute value one by fraction-free elimination, and compares torus-order factors at five small prime-power arguments. Its terminal line is `VERIFY_OK`; `verify_output.txt` records the full successful run.

The finite computation is exhaustive because the algebraic proof reduces every finite-field Frobenius class to one of the \(120\) permutations in \(S_5\), **not** because small finite fields are assumed representative of arbitrary ones.

## Relationship to prior work

The geometry of ten exceptional curves, the Petersen graph and its \(S_5\)-action is classical and **not new here**. González-Sánchez, Harrison, Polo-Blanco and Schicho (2010) give the ground-field classification of degree-five del Pezzo surfaces through the Galois action. Candelas, de la Ossa, van Geemen and van Straten (2012), §3 and §6, identify the ten-curve divisor with the reducible Wiman-pencil member. Dolgachev, Farb and Looijenga (2018), especially §§2–3, establish the Wiman–Edge boundary, stable genus-six geometry and related rational \(S_5\)-representations. Their data make the finite-field study natural, and rational character calculations can be inferred from them.

The present contribution is the **seven-case integral, rather than merely rational, Frobenius-lattice classification of the connected generalized Jacobian**, the corresponding exact finite abelian groups and the complete boundary-curve zeta functions. In the inspected relevant text, the sources do not state or classify these integral tori over finite fields. This is a literature-based originality assessment, not a claim that no implicit derivation or earlier unindexed statement exists. A more specialized source could still anticipate parts of the classification.

## Limitations

The theorem is restricted to the canonical reduced nodal boundary of **smooth degree-five del Pezzo surfaces over finite fields**. It does not determine full Picard functor components, other degenerations in the Wiman–Edge pencil, or the zeta function of the ambient surface. The torus descriptions are exact over the base field, but they do not assert that the given curve has a rational smooth point in every twist: type \((5)\) has no rational points at all. The six-cycle character modules rely on correct branch orientation; omitting the edge-reversal signs would change the answer. An independent mathematical audit has not been performed.

## References

1. J. González-Sánchez, M. Harrison, I. Polo-Blanco and J. Schicho, *Algorithms for Del Pezzo Surfaces of Degree 5 (Construction, Parametrization)*, arXiv:1009.4044, initial public version September 21, 2010. https://arxiv.org/abs/1009.4044 ; full text https://arxiv.org/html/1009.4044v2 .
2. P. Candelas, X. de la Ossa, B. van Geemen and D. van Straten, *Lines on the Dwork Pencil of Quintic Threefolds*, arXiv:1206.4961, initial public version June 21, 2012, especially §§3 and 6. https://arxiv.org/html/1206.4961v1 .
3. I. Dolgachev, B. Farb and E. Looijenga, *Geometry of the Wiman–Edge Pencil, I: Algebro-geometric Aspects*, European Journal of Mathematics **4** (2018), 879–930, especially §§2–3. https://link.springer.com/article/10.1007/s40879-018-0231-3 .
