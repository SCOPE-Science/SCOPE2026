# Involutive nodal symmetry of the exceptional Hirzebruch Batyrev mirror pair

## Finding

Let \(\Delta\) be the explicit reflexive four-polytope with 22 vertices in Wuebben's unique doubly isolated Batyrev mirror pair carrying an anticanonical \(\mathbb F_1\)-cone singularity. Its complete integral lattice stabilizer is
\[
\operatorname{Aut}_{\mathbb Z}(\Delta)=\{I,T\}\cong C_2,\qquad
T=\begin{pmatrix}1&1&0&0\\0&-1&0&0\\0&0&1&1\\0&0&0&-1\end{pmatrix}.
\]
The nonidentity element has the following *complete orbit profile* on two-dimensional faces. On \(\Delta\), the 50 smooth triangles form 25 pairs, the 20 unit squares form ten pairs, and the unique \(\mathbb F_1\) quadrilateral and unique degree-six del Pezzo hexagon are each fixed. On the polar \(\Delta^\circ\), the 38 triangles form 19 pairs, the 26 unit squares form twelve pairs and two fixed faces, and the two degree-seven pentagons and the two degree-six hexagons each form one pair.

For each of the 26 polar unit squares, let \(\rho_S\in\mathbb Q^{26}\) be its alternating diagonal-relation vector in the vector space indexed by the 26 polar vertices. Define \(\rho:\mathbb Q^{26}_{\mathrm{nodes}}\to\mathbb Q^{26}_{\mathrm{vertices}}\) by sending the basis symbol of \(S\) to \(\rho_S\). The involution acts on the node domain by the signed permutation required to intertwine \(\rho\) with its permutation action on vertices. Its eight-dimensional relation kernel has the eigenspace decomposition
\[
\boxed{\dim\ker(\rho)^+=5,\qquad\dim\ker(\rho)^-=3.}
\]
Moreover, the two coloop square faces in the polar node system, previously identified in the originating article, are **exchanged** by this involution.

These are statements about the lattice polytope, its face-fan toric symmetry, and its polar node-relation vector space. They are **not** assertions that a generic anticanonical hypersurface is invariant under \(T\).

## Assumptions and scope

Work over the integer lattice \(N=\mathbb Z^4\) and its dual \(M\). To fix coordinates without reference to a software database, define \(\Delta=\operatorname{conv}(V)\), where
\[
\begin{aligned}
V=\{&(1,0,0,0),(0,1,0,0),(1,-1,0,0),(0,0,1,0),\\
&(0,0,0,1),(0,0,1,-1),(0,0,-1,1),(0,0,0,-1),\\
&(0,0,-1,0),(-1,1,0,0),(0,-1,0,0),(-1,1,-1,1),\\
&(0,-1,0,-1),(0,-1,-1,0),(-1,1,-1,0),(-1,0,0,-1),\\
&(-1,0,-1,1),(-1,-1,0,-1),(-2,1,-1,1),(-2,1,-1,0),\\
&(-1,-1,-1,0),(-2,0,-1,0)\}.
\end{aligned}
\]
The polar uses Wuebben's sign convention
\[\Delta^\circ=\{u\in M_{\mathbb R}:\langle u,v\rangle\ge-1\text{ for all }v\in\Delta\}.\]
A unit square means a four-vertex parallelogram face without interior lattice points; the cited face classification identifies precisely 20 such faces of \(\Delta\) and 26 of \(\Delta^\circ\). A coloop of \(\rho\) is a column whose deletion lowers the rank of its matrix; it is equivalently a node coordinate forced to vanish in every vector of \(\ker\rho\). The plus/minus eigenspaces are over \(\mathbb Q\).

## Proof

**Exhausting the integral stabilizer.** The first, second, fourth and fifth displayed vertices form the standard lattice basis \(e_1,e_2,e_3,e_4\). Any lattice automorphism of \(\Delta\) permutes its vertices and is therefore determined by the ordered quadruple \((a,b,c,d)=(A e_1,A e_2,A e_3,A e_4)\) of vertices. The displayed set contains \(\pm(e_1-e_2)\), \(\pm(e_3-e_4)\), \(-e_3\), and \(-e_4\). Consequently the image pair \((a,b)\) must satisfy \(\pm(a-b)\in V\) and \((c,d)\) must satisfy \(\pm(c-d),-c,-d\in V\). Direct integer enumeration of the fixed 22-vector set gives respectively 52 and 12 ordered pairs, hence 624 candidate quadruples. For each candidate construct its integer matrix from these columns, retain determinant \(\pm1\), and check whether its image of every vertex lies in \(V\). Precisely two pass: \(I\) and the displayed \(T\). Their determinants are units, their actions are bijective on \(V\), and \(T^2=I\), proving the group statement. Every tested condition is an integer equality and the enumeration is exhaustive, not a random sample.

**Complete face action.** Each facet is specified by a primitive supporting integer covector taking minimum \(-1\) on at least four affinely independent input vertices. Every such covector can be obtained from a four-vertex combination by taking the primitive signed vector of its three affine differences. This finite exact search yields 26 distinct facets of \(\Delta\); their primitive inner normals are exactly the 26 vertices of \(\Delta^\circ\). Running the same construction on the polar yields 22 facets. A two-face of a four-polytope is the intersection of two facets having affine dimension two. Exhaustively forming these intersections gives 72 primal two-faces and 68 polar two-faces, with the face-size counts
\[
\begin{array}{c|rrrr}
&\text{triangles}&\text{quadrilaterals}&\text{pentagons}&\text{hexagons}\\\hline
\Delta&50&21&0&1\\
\Delta^\circ&38&26&2&2
\end{array}.
\]
A quadrilateral is a parallelogram exactly when its four vertices partition into two pairs with equal vector sum. This identifies the 20 primal and 26 polar unit-square types using the published face classification. Apply \(T\) on the primal vertices and \((T^{-1})^{\mathsf T}=T^{\mathsf T}\) on the polar vertices, obtaining precisely the orbit profiles in the finding. In particular no primal square is fixed, whereas exactly two polar squares are fixed.

**Equivariant node relations.** For any polar square with cyclic vertex order \((a,b,c,d)\), take \(\rho_S=e_a-e_b+e_c-e_d\), defined up to simultaneous sign. Under the polar lattice involution these columns transform into signed columns of the same type, so the signed action on the 26-dimensional node-symbol space is well-defined up to conjugation by diagonal sign changes. Integer elimination of the 26 square-diagonal columns gives rank 18. There are 12 swapped square pairs and two invariant squares; on the two invariant squares the alternating relation is preserved with positive sign. Hence the node-symbol space has eigendimensions 14 and 12. Applying the equivariant diagonal map to the two eigenspaces yields image dimensions 9 and 9 by exact rational elimination. The rank-nullity theorem therefore gives \(14-9=5\) and \(12-9=3\). Direct rank deletion identifies exactly two coloop squares, which are
\[
\begin{aligned}
S_-&=\{(-1,-1,0,-1),(-1,0,0,-1),(0,1,0,-1),(0,0,0,-1)\},\\
S_+&=\{(-1,-1,0,1),(0,-1,0,1),(0,0,0,1),(-1,0,0,1)\}.
\end{aligned}
\]
Applying \(T^{\mathsf T}\) directly to all four vertices of \(S_-\) produces the vertex set \(S_+\), completing the proof.

## Verification

The companion standalone Python 3 standard-library program `verify.py` regenerates all vertices, facets, two-face intersections, stabilizer candidates, node-diagonal vectors, coloop checks, and both rational eigenspace ranks from the 22 recorded vertices. Run `python3 verify.py`; the final line is:

`VERIFY_OK polytope_aut=C2 tested_images=624 primal_nodes=10_pairs mirror_nodes=12_pairs+2_fixed mirror_coloops=exchanged node_relations=5_plus+3_minus`

All face incidence and linear algebra calculations use integer arithmetic or exact rational Gaussian elimination. The computation enumerates all relevant finite candidates; it is not a numerical approximation or an extrapolation from a sample.

## Relationship to prior work

Wuebben, arXiv:2610.03753v1, Theorem 6.1 gives the explicit 22-vertex polytope, both face inventories, and the node singularities on both sides. Remark 6.3 establishes the polar node matrix rank 18 and singles out the two coloop squares. Those results are retained as prior art. A separate prior calculation classified the five minimal three-square dependence circuits in the same polar node system; that circuit census is also not claimed here. Neither source gives the complete integral lattice stabilizer, its action on both singularity-stratum inventories, or the eigenspace character of the eight-dimensional node-dependency space. General lattice-polytope symmetry algorithms give a method but do not specify the group or character of this exceptional example.

## Limitations

The group is the **integral lattice stabilizer**, equivalently the toric fan lattice-symmetry group, not the full automorphism group of the ambient toric variety or of any particular Calabi–Yau hypersurface. The node relations are the combinatorial diagonal-relation subsystem; the dimensions \(5\) and \(3\) do not by themselves establish the existence of an equivariant smoothing, and the originating paper's nonsmoothability conclusion is unchanged. The calculation concerns only the explicit unique exceptional mirror pair, not all 590 both-sides-unit polytopes. Historical priority for an unpublished or database-implicit computation is not independently certified.

## References

1. Bernd Johannes Wuebben, *Doubly isolated Batyrev mirror pairs and non-smoothable Calabi–Yau threefolds*, arXiv:2610.03753v1 (first public posting 2026-09-26), Theorem 6.1 and Remark 6.3, https://arxiv.org/html/2610.03753v1.
2. V. V. Batyrev, *Dual polyhedra and mirror symmetry for Calabi–Yau hypersurfaces in toric varieties*, Journal of Algebraic Geometry 3 (1994), 493–535.
