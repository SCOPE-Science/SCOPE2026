# Eight minimum-support octahedral spheres give the integral hyperoctahedral module of the four-cube independence complex

## Finding

Let \(Q_4\) have vertex set \(\mathbb F_2^4\), with an edge precisely when two vertices differ in one bit. Write \(K=\operatorname{Ind}(Q_4)\) for its ordinary simplicial independence complex. Exactly **eight** induced subcomplexes on eight vertices are combinatorial octahedral three-spheres \((S^0)^{*4}\). Every nonzero class of \(\widetilde H_3(K;\mathbb Z)\) supported on an induced subcomplex needs at least eight vertices. The eight fundamental sphere classes generate \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^7\), and **any seven** constitute an integral basis.

There is one primitive integral relation between the eight classes. Orient and normalize the classes as \(E_{i,p}\), with \(i\in\{0,1,2,3\}\) and \(p\in\mathbb F_2\), as specified below. They obey

\[
\sum_{i=0}^3\sum_{p=0}^1 E_{i,p}=0.
\]

The entire cube automorphism group \(B_4=(C_2)^4\rtimes S_4\) acts as follows. If \(g(v)=\pi(v)\oplus t\), where \(\pi\) permutes bit positions and \(t\in\mathbb F_2^4\), then

\[
gE_{i,p}=\operatorname{sgn}(\pi)E_{\pi(i),\ p+\sum_{k\ne\pi(i)}t_k}.
\]

In particular, the **integral group module**, and not just the rational character, is

\[
\widetilde H_3(K;\mathbb Z)\cong_{\mathbb Z[B_4]}
\operatorname{sgn}_{S_4}\otimes_{\mathbb Z}
\left(\mathbb Z[\{(i,p):0\le i<4,\ p\in\mathbb F_2\}]
\big/\mathbb Z\!\sum_{i,p}[(i,p)]\right).
\]

The quotient is by the diagonal rank-one submodule; it is **not** claimed to equal the integral augmentation kernel. The nonequivariant homotopy type \(K\simeq\bigvee^7S^3\) was already established and is not the new claim.

## Assumptions and scope

Index vertices by integers from 0 through 15, interpreted as four-bit words. For direction \(i\) and parity \(p\), take the four cube edges in direction \(i\) whose three fixed coordinates have parity \(p\). Their eight endpoints induce exactly four disjoint edges in \(Q_4\), since two distinct three-bit words of the same parity differ in two coordinates. The induced independence subcomplex is therefore \((S^0)^{*4}\). Orient the fundamental three-cycle by expanding the exterior join of four differences, each written as the lower integer endpoint minus the higher endpoint, and order the four edges by the lower endpoint. Denote it \(z_{i,p}\).

Order these eight cycles by

\[
(0,0),(1,0),(2,0),(3,0),(1,1),(2,1),(3,1),(0,1).
\]

In this order set \((r_j)=(1,-1,1,-1,-1,1,-1,1)\) and \(E_j=r_jz_j\). No equivariant homotopy splitting, homology in higher cubes, or arbitrary-grid theorem is asserted.

## Proof

**Sharp universal support bound.** In any finite flag complex, a nonzero reduced \(d\)-homology class with \(d\ge0\) requires at least \(2d+2\) vertices in its supporting induced subcomplex. At equality the induced subcomplex is the boundary of a \((d+1)\)-crosspolytope. To prove this inductively, the case \(d=0\) needs two disconnected vertices. For \(d\ge1\), take a flag complex \(L\) with nonzero \(\widetilde H_d(L)\) on at most \(2d+2\) vertices. Every one-vertex deletion has zero \(\widetilde H_d\) by induction on vertex count (or use the strictly smaller universal support bound); and \(L\) is not a cone. For any vertex \(v\), the decomposition into the deletion and the cone on \(\operatorname{link}_L(v)\), with its Mayer–Vietoris sequence, forces \(\widetilde H_{d-1}(\operatorname{link}_L(v))\ne0\). The inductive dimensional bound puts at least \(2d\) vertices in this link. Since \(v\) has a nonneighbor (otherwise \(L\) is a cone), there are at most \(2d\) neighbors. Thus, at equality, every vertex has exactly one nonneighbor. The complement graph is a perfect matching, and flagness makes \(L=(S^0)^{*(d+1)}\). For the minimum bound, the same induction shows \(2d+2\) necessary even when there are more vertices; a vertex-minimal nonzero complex supplies the deletion condition. Apply this with \(d=3\) to all induced subcomplexes of \(K\).

**Exhaustive eight-vertex classification.** At equality an induced eight-vertex carrier must induce four disjoint graph edges. The verifier enumerates **all** four-element subsets of the 32 cube edges, retaining those with eight distinct endpoints and exactly one internal neighbor at every endpoint. It finds precisely eight and independently checks that their direction/parity labels exhaust \(\{(i,p)\}\). Each yields a signed integral 3-cycle with sixteen oriented tetrahedra and zero simplicial boundary.

**Exact integral coordinates.** Enumerate all nonempty independent-set masks; the face vector in dimensions zero through seven is \((16,88,208,228,128,56,16,2)\). The reproducible pivot-toggle acyclic matching has 367 pairs and exactly one critical vertex and seven critical three-cells. Check acyclicity on all 2,816 nonempty Hasse incidences, not by assumption. Algebraically cancel the matched unit boundary coefficients over the integers, projecting all eight oriented octahedral cycles into the resulting integral Morse chain complex. The remaining Morse differential is zero and its seven critical three-cells freely generate \(\widetilde H_3(K;\mathbb Z)\).

In the critical three-cell order \((1680,2400,10370,17028,24600,33064,33096)\), and the eight-cycle order above, the projected coefficient matrix is

\[
M=\begin{pmatrix}
0&0&1&0&0&0&1&0\\
0&0&0&1&0&1&0&0\\
1&0&0&1&0&0&0&0\\
0&-1&-1&0&0&0&0&0\\
0&0&1&1&0&0&0&0\\
0&0&0&0&0&1&0&-1\\
0&0&0&0&-1&-1&0&0
\end{pmatrix}.
\]

Deleting successive columns produces the **exact integral determinants**

\[
(-1,-1,-1,-1,1,1,1,1).
\]

Every seven-cycle subfamily is therefore a unimodular basis. Direct multiplication gives \(M(r_j)^{\mathsf T}=0\); since \(M\) has rank seven, this is the unique primitive relation up to a global sign. All eight classes are primitive and nonzero.

**Full integral symmetry.** Every automorphism of the cube is uniquely a bit translation followed by a permutation of four coordinate positions, giving 384 elements. Its action carries the parallel-edge carrier \((i,p)\) to \((\pi(i),p+\sum_{k\ne\pi(i)}t_k)\). Applying the permutation to each of the sixteen *signed simplices* of \(z_j\), including orientation signs, proves

\[
gz_j=\operatorname{sgn}(\pi)\,r_jr_{g(j)}\,z_{g(j)}.
\]

The normalized classes consequently satisfy the announced signed-permutation action. Because the eight classes span a free rank-seven lattice with the sole relation their sum, the displayed quotient of the signed permutation lattice is an isomorphism over \(\mathbb Z[B_4]\); no appeal to characteristic-zero semisimplicity is made.

## Verification

Run `python3 verify_q4_integral.py` with Python 3.10 or later; no third-party packages or external data are needed. This standalone verifier reconstructs the graph, every one of the 742 nonempty faces, every matched Hasse incidence, all signed chain differentials and the 367 exact unit cancellations, the eight octahedral cycles, all eight 7-by-7 Bareiss determinants, the primitive relation, and every one of the 384 signed simplicial automorphism actions. The terminal message is `VERIFY_OK_Q4_INTEGRAL_CROSSCYCLE_AUGMENTATION_QUOTIENT`. This verifies a complete finite complex; the universal support theorem is proved independently above and is not inferred from a finite sample.

## Relationship to prior work

Bousquet-Mélou–Linusson–Nevo [1] treats open and cylindrical square-grid independence complexes and does not imply this toroidal integral representation. Jonsson [2] defines and studies crosspolytopal homology cycles in periodic grids; his Table 1 includes the **already known** integral Betti number \(\beta_3=7\) for the four-by-four toroidal grid, and his discussion specifically distinguishes constructing crosspolytope cycles from determining whether they generate all homology. The known Betti number, existence of crosspolytopal cycles, and general crosspolytopal construction are **not claimed as new**. Barmak [3] proves general suspension results for triangle-free independence complexes, but not the eight-cycle integral lattice and full signed hyperoctahedral action. A previously published exact calculation [4] proves the same complex is a wedge of seven three-spheres; its stated scope explicitly excludes a canonical equivariant decomposition. The novel assertions here are the sharp eight-carrier census, all-eight unimodular deletion basis, unique integral relation, and the complete integral \(B_4\)-module structure. Different topological constructions on the same cube, such as total cut and Čech complexes, have unrelated homology representations.

## Limitations

Only the ordinary independence complex of the sixteen-vertex four-cube is covered. The representation is an isomorphism of integral homology **modules**, not an equivariant equivalence of spaces. Literature search cannot rule out every unindexed computation; the strongest available work already knows the nonequivariant rank and does not establish the new lattice character. All exhaustive computations are supplied for independent finite replay; neither the finite enumeration nor the verifier is treated as a proof of general assertions about all cubes.

## References

[1] M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first public version 2007-01-30, https://arxiv.org/abs/math/0701890.

[2] J. Jonsson, *Certain Homology Cycles of the Independence Complex of Grids*, Discrete & Computational Geometry 43 (2010), 927–950, DOI 10.1007/s00454-009-9224-9; full text https://link.springer.com/content/pdf/10.1007/s00454-009-9224-9.pdf (especially §§1.2, 5.3 and Table 1).

[3] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first public 2010-07-02, https://arxiv.org/abs/1007.0418.

[4] *The four-cube independence complex is a wedge of seven three-spheres*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c.
