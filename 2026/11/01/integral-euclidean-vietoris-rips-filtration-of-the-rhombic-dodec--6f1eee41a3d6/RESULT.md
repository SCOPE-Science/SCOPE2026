# Integral Euclidean Vietoris–Rips filtration of the rhombic dodecahedron

## Finding
Let \(V\subset\mathbb R^3\) be the fourteen-point vertex set
\[
V=\{\pm2e_1,\pm2e_2,\pm2e_3\}\ \cup\ \{(\epsilon_1,\epsilon_2,\epsilon_3):\epsilon_i\in\{-1,1\}\}.
\]
This is the standard rhombic-dodecahedral vertex configuration, with Euclidean rather than graph distance. For each real \(r\ge0\), let \(K_r\) be the **inclusive** Vietoris–Rips complex: a nonempty finite subset \(\sigma\subseteq V\) is a simplex precisely when every two points of \(\sigma\) have Euclidean distance at most \(r\).

The complete integral homotopy classification is
\[
K_r\simeq\begin{cases}
\bigvee^{13}S^0,&0\le r<\sqrt3,\\
\bigvee^{11}S^1,&\sqrt3\le r<2,\\
S^2,&2\le r<2\sqrt2,\\
S^3,&2\sqrt2\le r<\sqrt{11},\\
S^6,&\sqrt{11}\le r<2\sqrt3,\\
\ast,&r\ge2\sqrt3.
\end{cases}
\]
All assertions include their left endpoints as written. Consequently the **entire reduced integral persistent homology** is the direct sum of thirteen copies of \(\mathbb Z\) in degree zero on \([0,\sqrt3)\), eleven copies in degree one on \([\sqrt3,2)\), and one copy each in degrees two, three and six on \([2,2\sqrt2)\), \([2\sqrt2,\sqrt{11})\) and \([\sqrt{11},2\sqrt3)\), respectively. All integral homology is torsion-free. These intervals describe integral persistence modules, not only Betti numbers at isolated scales.

## Assumptions and scope
The coordinates are fixed exactly, without radial normalization: the six coordinate-axis vertices have Euclidean norm \(2\), and the eight cube corners have norm \(\sqrt3\). Distances are the ordinary ambient Euclidean distances, not shortest-path distances in the polyhedral one-skeleton. Changing the overall scale multiplies all parameter values by the same factor. The claim is exclusively for this fourteen-point configuration and inclusive thresholds, with no assertion about deformations or arbitrary Catalan solids.

## Proof
**1. Exhaustion of thresholds.** Every distinct squared distance is one of \(3,4,8,11,12,16\), with respective unordered-pair multiplicities \(24,12,24,24,4,3\). Indeed, between an axis vertex \(2se_i\) and a corner \(\epsilon\), the square is \(7-4s\epsilon_i\), hence \(3\) or \(11\); two perpendicular axis vertices have square \(8\), and two opposite axis vertices have square \(16\). Two cube corners differing in \(h\in\{1,2,3\}\) signs have square \(4h\). No change occurs between the six successive distances.

**2. Radius below \(2\).** Below \(\sqrt3\) there are fourteen isolated points. At \(\sqrt3\) only the twenty-four axis–corner incidences are edges, forming the connected one-skeleton of the rhombic dodecahedron. As a connected graph on fourteen vertices and twenty-four edges, it is \(\bigvee^{11}S^1\).

**3. Radius \(2\).** Exactly twelve additional cube edges, whose corners differ in one sign, occur. For each axis vertex, its four incident corners form a four-cycle, and four triangles cone this cycle from the axis vertex. These are all the triangles and there are no higher-dimensional simplices. In this triangulation each edge belongs to exactly two triangles; every vertex link is a connected cycle (length four at an axis vertex and length six at a corner), and the complex is connected with face vector \((14,36,24)\) and Euler characteristic \(14-36+24=2\). By the classification of closed connected surfaces it is homeomorphic to \(S^2\). Geometrically, this is the boundary of the rhombic dodecahedron with each of its twelve rhombi triangulated along the cube-corner diagonal.

**4. Radius \(2\sqrt2\): an explicit simple-homotopy reduction.** The stage with squared threshold eight has face vector \((14,60,100,60,6)\), comprising 240 nonempty simplices. Delete the six axis vertices in the fixed order \((-2,0,0),(2,0,0),(0,-2,0),(0,2,0),(0,0,-2),(0,0,2)\). At the moment each vertex is removed, its simplicial link collapses to a single corner vertex. The successive links have \(39,39,23,23,15,15\) nonempty faces and require \(19,19,11,11,7,7\) elementary collapse pairs. Lifting a link collapse \((\sigma,\tau)\) to \((v\cup\sigma,v\cup\tau)\) in the ambient complex, and finally collapsing \((\{v\},\{v,w\})\) when the remaining link is \(\{w\}\), gives exactly eighty elementary free-face pairs. The entire ordered certificate is `collapse_8.json`; `verify.py` regenerates the entire initial complex and checks that each pair consists of present faces, has codimension one, and has **exactly one immediate coface at that step**. This is a genuine sequence of elementary simplicial collapses, not an inference from Betti numbers or from a partial Morse matching.

The 80 remaining nonempty simplices are exactly the induced clique complex on the eight cube corners. Among these corners the only nonedges are the four antipodal pairs, so the residual complex is the join of four copies of \(S^0\), i.e. the boundary of a four-dimensional crosspolytope. It is homeomorphic to \(S^3\). Thus the full 14-vertex complex *simplicially collapses* to \(S^3\).

**5. Radius \(\sqrt{11}\).** Every pair of distinct vertices is connected except the three opposite pairs of axis vertices, at squared distance sixteen, and the four antipodal pairs of cube corners, at squared distance twelve. These seven missing edges form a perfect matching on fourteen vertices. Therefore \(K_{\sqrt{11}}\) is precisely the boundary complex of a seven-dimensional crosspolytope, \((S^0)^{\ast7}\cong S^6\). Its face vector is \((14,84,280,560,672,448,128)\).

**6. Radius \(2\sqrt3\) and above.** All eight cube corners are adjacent to every vertex once the squared threshold reaches twelve. Hence any one corner is a cone apex and \(K_r\) is contractible for all larger radii. At radius four the complex becomes the full thirteen-simplex.

**7. Integral persistence maps.** Each nontrivial reduced homology degree occurs at exactly one of the successive stages, and all stages are constant within their displayed half-open intervals. Therefore every map crossing a transition between nontrivial stages is zero in each positive degree; at the first transition all thirteen reduced zero-dimensional generators die because the graph becomes connected. The simplicial collapses and sphere identifications establish integral homology, not merely field ranks. No torsion or additional intervals can occur.

## Verification
The self-contained Python 3 standard-library checker `verify.py`, run alongside `collapse_8.json`, recomputes all 91 exact squared distances, enumerates every simplex at each threshold, checks the connected closed two-manifold at squared radius four, replays all 80 elementary collapses from the actual radius-eight complex, checks the four antipodal nonedges in the eight-corner residual complex, checks the seven-pair perfect complement at squared radius eleven, and verifies universal cone vertices at squared radius twelve. Run with `python3 verify.py`. An independently generated exact certificate is embedded as `collapse_8.json`. The recorded run is `verification_output.txt`; the checker terminates with `VERIFY_OK` only after all assertions pass. No random computation or numerical floating-point tolerance is involved.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (first public 2011-04-03) develops the finite flag-complex and collapse framework, primarily for shortest-path graph powers and cycles; it does not treat the ambient Euclidean vertex distances here. Saleh, Titz Mite and Witzel's *Vietoris–Rips complexes of Platonic solids* (first public 2023-02-28) gives complete classifications for the five Platonic solids; its cube calculation covers the homotopy type of the **eight-corner induced subcomplex** at squared radius eight, but does not assert that adjoining the six axis vertices preserves this type, nor classify the other five thresholds of the fourteen-point rhombic dodecahedron. The present proof makes that reduction explicit and exhibits the complete integral persistence of the non-vertex-transitive Catalan solid. Nada Saleh's 2023 dissertation discusses a different 32-vertex Catalan solid, the rhombic triacontahedron, and explicitly poses the classification of Vietoris–Rips homotopy types of Catalan solids as future research (p. 75). Its stated computational tables do not contain the present 14-point configuration. Published calculations for the Euclidean cuboctahedron and the rhombic-dodecahedral *matching complex* concern distinct point sets or distinct simplicial constructions. A targeted literature search did not locate a published equivalent calculation; that negative observation is not a proof of uniqueness.

## Limitations
No claim is made about arbitrary rhombic dodecahedra, their graph-metric Rips complexes, other radial ratios, or equivariant homotopy. The eighty elementary pairs are exact for the stated coordinate order; they are not claimed to be symmetric under the whole polyhedral automorphism group. Publication priority remains subject to discovery of unpublished or unindexed equivalent work. No independent mathematical audit is represented by the reproducibility checks.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public 2011-04-03), https://arxiv.org/abs/1104.0433.
2. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first public 2023-02-28), https://arxiv.org/abs/2302.14388.
3. J.-D. Boissonnat and S. Pritam, *Edge Collapse and Persistence of Flag Complexes*, SoCG 2020, https://doi.org/10.4230/LIPIcs.SoCG.2020.19 (general collapse methods; not a computation for this fourteen-point configuration).
4. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral dissertation (2023), DOI 10.22029/jlupub-17950, https://jlupub.ub.uni-giessen.de/items/0a69b981-1372-4ab7-9e75-03b44faa5f67.
