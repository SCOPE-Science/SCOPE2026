# Complete Euclidean Rips homotopy and signed-permutation characters of the rhombic dodecahedron

## Finding

Let \(A=\{\pm2e_1,\pm2e_2,\pm2e_3\}\), \(C=\{(\epsilon_1,\epsilon_2,\epsilon_3):\epsilon_i\in\{-1,1\}\}\), and \(P=A\cup C\subset\mathbb R^3\). This is the full fourteen-vertex set of the rhombic dodecahedron dual to the cuboctahedron. Let \(K_r=\operatorname{VR}_{\le r}(P)\) denote the inclusive Euclidean Vietoris–Rips complex, including all vertices at radius zero. For every real \(r\ge0\), its **integral homotopy type** is

\[
K_r\simeq
\begin{cases}
\bigsqcup^{14}\mathrm{pt},&0\le r<\sqrt3,\\
\bigvee^{11}S^1,&\sqrt3\le r<2,\\
S^2,&2\le r<\sqrt8,\\
S^3,&\sqrt8\le r<\sqrt{11},\\
S^6,&\sqrt{11}\le r<\sqrt{12},\\
\mathrm{pt},&r\ge\sqrt{12}.
\end{cases}
\]

More precisely, at radius \(2\) the simplicial complex is exactly the rhombic-dodecahedral boundary triangulated along all twelve short diagonals. At radius \(\sqrt8\), the inclusion of the eight-cube-vertex induced subcomplex is a **simple-homotopy equivalence**, certified by an explicit sequence of eighty elementary collapses; the retained subcomplex is the boundary of a four-dimensional crosspolytope, homeomorphic to \(S^3\). At radius \(\sqrt{11}\), the complex is the boundary of a seven-dimensional crosspolytope, homeomorphic to \(S^6\). The complex is contractible at and above radius \(\sqrt{12}\), even though three longer antipodal distances persist.

The complete **reduced integral persistence barcode**, with endpoints understood in the inclusive convention, consists of thirteen degree-zero intervals \([0,\sqrt3)\); eleven degree-one intervals \([\sqrt3,2)\); one degree-two interval \([2,\sqrt8)\); one degree-three interval \([\sqrt8,\sqrt{11})\); and one degree-six interval \([\sqrt{11},\sqrt{12})\). No other reduced integral bars or torsion occur.

Write \(G\) for the full signed-coordinate-permutation group (order \(48\)), acting on \(P\). For \(g\in G\), let \(\delta(g)=\det(g\mid\mathbb R^3)\), and let \(\pi_g\in S_4\) be its induced permutation of the four body-diagonal **unoriented pairs** of cube vertices. On the three single-rank higher homology stages its characters are, respectively,

\[
\operatorname{tr}(g\mid\widetilde H_2(K_2;\mathbb Z))=\delta(g),\qquad
\operatorname{tr}(g\mid\widetilde H_3(K_{\sqrt8};\mathbb Z))=\operatorname{sgn}(\pi_g),\qquad
\operatorname{tr}(g\mid\widetilde H_6(K_{\sqrt{11}};\mathbb Z))=\delta(g)\operatorname{sgn}(\pi_g).
\]

At the graph stage \(\sqrt3\le r<2\), the integral first homology has rank eleven, and its character is \(1+E_g-V_g\), where \(V_g\) is the number of fixed vertices and \(E_g\) is the number of pointwise fixed edges of the rhombic-dodecahedral graph. These formulas determine all rational character values; the three one-dimensional higher homology modules are specified integrally as sign modules.

## Assumptions and scope

Coordinates, distances, inclusivity and the full symmetry group are exactly as above. All assertions refer to the **unrescaled Euclidean metric** in \(\mathbb R^3\), not graph shortest-path distance, spherical distance, a radially normalized fourteen-point set or the twelve-vertex cuboctahedron. Homology is reduced integral simplicial homology unless indicated. The ambient source literature used for context predates the archive cutoff; the source-publication dates in the references are distinct from later revisions.

The six squared pair-distance shells, with multiplicities, are \(3:24\), \(4:12\), \(8:24\), \(11:24\), \(12:4\), and \(16:3\). The twenty-four radius-\(\sqrt3\) edges join one point of \(A\) to a coordinate-compatible point of \(C\). These exhaust the graph's edges, producing a connected graph of cyclomatic rank \(24-14+1=11\).

## Proof

**1. Exact metric classification.** Two cube points differing in exactly \(h\in\{1,2,3\}\) coordinate signs have squared distance \(4h\). The two distinct axis vertices \(\pm2e_i\) and \(\pm2e_j\) have squared distance \(8\) for distinct coordinates and \(16\) for opposite points on the same axis. An axis vertex \(2s e_i\) and a cube point \((\epsilon_1,\epsilon_2,\epsilon_3)\) have squared distance \(3\) if \(\epsilon_i=s\) and \(11\) if \(\epsilon_i=-s\). These formulas exhaust the \(\binom{14}{2}=91\) pairs and establish all critical radii.

**2. Sphere and graph stages.** Below \(\sqrt3\) there are no edges. At \(\sqrt3\) the edges are precisely the \(24\) axis–cube incidences; the graph is connected, giving eleven circles. At radius \(2\), the additional twelve cube–cube edges join pairs differing in one coordinate. For each two-coordinate choice \(i<j\) and signs \(s,t\), the plane \(s x_i+t x_j=2\) supports a rhombic face of \(\operatorname{conv}(P)\), with two compatible cube points and two axis points \(2s e_i,2t e_j\). These twelve rhombi form the complete boundary of the convex rhombic dodecahedron. Adding the cube–cube diagonal subdivides each rhombus into its two triangles. Every triangle of \(K_2\) is one of these twenty-four, and there are no higher simplices: \(K_2\) is exactly that triangulated convex boundary \(S^2\).

**3. The previously unforced relative collapse.** At squared threshold \(8\), the cube induced subcomplex \(Q=K_{\sqrt8}[C]\) consists of all cube-vertex subsets containing no antipodal pair, since nonantipodal cube pairs are at squared distance at most eight and antipodal pairs have squared distance twelve. Its four antipodal pairs form four copies of \(S^0\), so \(Q\cong(S^0)^{*4}\cong S^3\). The axis induced complex is \((S^0)^{*3}\). Every nonempty axis face \(S\) contains at most one sign on each coordinate axis. The cube points compatible with \(S\) have exactly the signs prescribed by \(S\); their number is \(2^{3-|S|}\). They form a simplex because their pairwise squared distances are at most eight. Consequently every face of \(K_{\sqrt8}\) containing an axis point has a unique axis subset \(S\ne\emptyset\) and an arbitrary cube subset of this simplex.

Choose the lexicographically first compatible cube vertex \(c(S)\). Match each face with axis subset \(S\) that omits \(c(S)\) to the face obtained by adding \(c(S)\). This pairs **all** faces outside \(Q\). It is acyclic: on a directed alternating cycle, the axis subset cannot decrease, as match steps never change it and other face-deletion steps can only remove axis vertices. Hence any such cycle would keep the same axis subset. Then a match step adds \(c(S)\), while an unmatched downward step can never remove \(c(S)\); a closed directed path is impossible. This relative acyclic matching gives a collapse \(K_{\sqrt8}\searrow Q\). For an independently replayable stronger certificate, `collapse_pairs.json` supplies one valid order of its \(80\) elementary free-face pairs, all of which leave \(Q\) unchanged.

**4. Final stages.** At squared threshold \(11\) every pair except the seven antipodal pairs is joined. Thus \(K_{\sqrt{11}}\cong (S^0)^{*7}\cong S^6\) simplicially. At squared threshold \(12\), all eight cube vertices span a seven-simplex, and each can join any axis simplex; the axis subcomplex is \((S^0)^{*3}\). Therefore \(K_{\sqrt{12}}\cong\Delta^7*(S^0)^{*3}\), a simplicial cone up to taking a join with a nonempty simplex, hence contractible. The last threshold \(16\) only fills the remaining axis-antipodal edges and does not change that conclusion.

**5. Persistence and symmetry.** Each nonzero reduced integral group occurs in a degree absent at the immediately adjacent other stage. Since all interval-constant inclusions are identities on the same simplicial complex, and all across-threshold maps in the same nonzero degree have zero target or source, the listed reduced barcode follows over \(\mathbb Z\) without an extension or torsion ambiguity. The convex boundary orientation gives character \(\delta\) on \(H_2\). The cube inclusion at threshold \(8\) is \(G\)-invariant and induces an isomorphism on integral \(H_3\). Choose the four cube points of coordinate product \(+1\), one in each antipodal pair. Every signed coordinate permutation maps these four representatives either to four other representatives or to their four negatives, uniformly. On the four crosspolytope coordinate axes this gives a common sign (whose fourth power is \(+1\)) times the permutation \(\pi_g\); its degree on \(S^3\) is \(\operatorname{sgn}(\pi_g)\). At threshold \(11\), the complex is the join of the octahedral axis sphere \(S^2\) and the cube sphere \(S^3\); its top orientation character is the product \(\delta(g)\operatorname{sgn}(\pi_g)\). For the graph, the exact augmented cellular chain sequence gives \(\chi_{H_1}=1+\chi_{C_1}-\chi_{C_0}\); an edge cannot have its endpoints swapped by \(G\) because its ends have different Euclidean norms, proving the fixed-edge formula.

## Verification

The standalone program `verifier.py` uses integer arithmetic and the complete \(14\)-vertex face sets. It exhaustively checks the six distance-shell multiplicities, verifies with exact rational linear algebra that the twelve supporting halfspaces have precisely the prescribed fourteen vertices, checks the exact \(24\)-triangle convex boundary triangulation, connected first graph, four-antipodal-pair cube subcomplex, all \(80\) **sequential free-face collapses** stored in `collapse_pairs.json`, seven-antipodal-pair \(S^6\) stage, remaining three antipodal constraints at squared radius twelve, and the signed-simplicial Lefschetz characters for all \(48\) signed-coordinate permutations on four stages. Execution (Python standard library only): `python verifier.py` in the extracted package directory. The expected final marker is `VERIFY_OK`. The proof above, not finite Betti-number extrapolation, establishes the homotopy statements.

The face-set counts at squared thresholds \(3,4,8,11,12,16\) are respectively \(38,74,240,2186,6911,16383\) nonempty simplices. At squared threshold eight, exactly \(160\) simplices lie outside the retained \(80\)-simplex subcomplex, accounting for \(80\) elementary collapses.

## Relationship to prior work

Adamaszek's original graph-power work develops clique complexes and homotopy stability, with Rips complexes defined from graph shortest-path metrics [1]; it does not classify the distinct Euclidean distance shells of this fourteen-vertex dual polytope. The complete Platonic-solid classification of Saleh, Titz Mite and Witzel [3] covers the five Platonic solids, not the rhombic dodecahedron. Its general last-antipodal-pair argument already explains the \(S^6\) stage in this example and its cube calculation explains the isolated eight-cube-vertex \(S^3\); neither alone establishes the **inclusion-preserving collapse after adjoining the six axis vertices**, nor the complete metric persistence and octahedral characters. Those earlier ingredients are not claimed as new. Sethares and Budney [2] use a rhombic-dodecahedral fundamental domain for a lattice quotient in musical topology; the object there is not the Vietoris–Rips filtration of its fourteen Euclidean vertices.

## Limitations

The theorem concerns exactly these fourteen vertices with the unrescaled coordinate metric; it does not assert a universal result for all Catalan solids, different radial normalizations, or graph-distance filtrations. The \(80\)-step collapse is not claimed to be equivariant as a sequence, although the induced homology isomorphism is equivariant because the included cube subcomplex is preserved by the symmetry group. The result is supported by an explicit mathematical proof and independently replayable finite checks, but it has not undergone an independent external scientific audit. Equivalent specialized computations in literature indexed by other terminology remain possible; no search proves uniqueness.

## References

[1] M. Adamaszek, *Clique complexes and graph powers*, first publicly posted 2011-04-03, arXiv:1104.0433, https://arxiv.org/abs/1104.0433.

[2] W. A. Sethares and R. Budney, *Topology of Musical Data*, arXiv:1307.1201, https://arxiv.org/abs/1307.1201 (Section 3 and Appendix B use a rhombic-dodecahedral fundamental domain, not its vertex-set Rips filtration).

[3] N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, first publicly posted 2023-02-28, arXiv:2302.14388, https://arxiv.org/abs/2302.14388 (Theorem, Sections 2–4). This later reference provides comparison and does not govern the archive classification date.
