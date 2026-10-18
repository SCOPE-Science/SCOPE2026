# Exact Haar polygon-type law for central sections of the regular truncated octahedron

## Finding
Let
\[
T=\{(q_1,q_2,q_3)\in\mathbb R^3:|q_i|\le2\ (i=1,2,3),\quad |q_1|+|q_2|+|q_3|\le3\}.
\]
This is a regular truncated octahedron, with vertex set the 24 distinct signed permutations of \((0,1,2)\). Let \(U\) be uniformly distributed on the Euclidean unit sphere. Away from a null set of orientations, let \(N(U)\) denote the number of vertices, equivalently edges, of the planar convex polygon \(T\cap U^\perp\). Define
\[
\alpha=\arccos(4/5),\qquad
D=11+3\sqrt{14}+4\sqrt6+2\sqrt{21},\qquad
p=\frac{24}{\pi}\arctan\left(\frac1D\right).
\]
Then the exact distribution is
\[
\begin{aligned}
\Pr(N(U)=6)&=4-\frac{18\alpha}{\pi}+p,\\
\Pr(N(U)=8)&=\frac{18\alpha}{\pi}-3-2p,\\
\Pr(N(U)=10)&=p,
\end{aligned}
\qquad \Pr(N(U)\notin\{6,8,10\})=0.
\]
Moreover \(\mathbb E N(U)=36\alpha/\pi\). The probabilities, respectively, are approximately \(0.498450689917704\), \(0.316108855580190\), and \(0.185440454502106\), and the mean is approximately \(7.373979529168803\).

## Assumptions and scope
Planes pass through the polytope center and have an unoriented Haar-uniform normal; choosing \(U\) uniformly on the sphere gives this law because \(U\) and \(-U\) represent the same plane. A normal orthogonal to a polytope vertex is excluded when counting ordinary polygon intersections; these finitely many great circles have zero probability. Scaling or rigidly moving the regular truncated octahedron does not alter the answer when the plane is translated to its center.

## Proof
**1. The edge-crossing identity.** The 14 facet inequalities defining \(T\) have six coordinate faces and eight diagonal faces. Its 24 vertices are all signed permutations of \((0,1,2)\). The 36 edges are exactly the 36 unordered vertex pairs at squared Euclidean distance \(2\): each of the 24 vertices has exactly three such neighbors, and the three edges lie in the corresponding active facet intersections. Thus every edge joins two vertices of squared norm \(5\) and scalar product \(4\).

For generic \(u\), the central plane intersects an edge exactly when its endpoints have strictly opposite signs under \(v\mapsto u\cdot v\). No two such edge crossings coincide, because a generic plane avoids the vertices. Accordingly,
\[
N(u)=\#\{\{v,w\}\in E(T):(u\cdot v)(u\cdot w)<0\}.
\]
This is a finite, exhaustive equality, not a sampling approximation.

**2. All orientation chambers.** Signed coordinate permutations of \(u\) preserve \(T\) and \(N\). It suffices to take \(x>y>z>0\) for \(u=(x,y,z)\). In this sector the only possible zeros of \(u\cdot v\), for the 24 vertices \(v\), occur at \(x=2y\), \(x=2z\), or \(y=2z\). The edge-crossing count is constant on each of the following five feasible open sign chambers. In the table, the three signs refer in order to \(x-2y\), \(x-2z\), and \(y-2z\); each representative has exact integer coordinates.

| Sign chamber | Representative normal | Polygon sides |
|:--|:--|--:|
| \((+,+,+)\) | \((9,4,1)\) | 8 |
| \((+,+,-)\) | \((9,4,3)\) | 10 |
| \((-,+,+)\) | \((7,4,1)\) | 6 |
| \((-,+,-)\) | \((7,4,3)\) | 8 |
| \((-,-,-)\) | \((5,4,3)\) | 6 |

The remaining three sign choices are impossible: \(x>2y\) forces \(x>2z\), whereas \(x<2z\) forces both \(x<2y\) and \(y<2z\). Enumerating the 36 finite edge pairs in the identity above gives exactly the five table counts; a complete deterministic enumerator is included as `truncated_octahedron_section_checker.py`.

**3. Exact decagonal solid angle.** In \(x>y>z>0\), the decagonal chamber is characterized by \(x>2y\) and \(y<2z\). Its closure is the spherical triangle whose extreme rays are \(a=(1,0,0)\), \(b=(4,2,1)\), and \(c=(2,1,1)\). The standard solid-angle identity for three rays gives
\[
\Omega=2\arctan\left(\frac{|\det(a,b,c)|}{\|a\|\|b\|\|c\|+(a\cdot b)\|c\|+(b\cdot c)\|a\|+(c\cdot a)\|b\|}\right).
\]
Here \(|\det(a,b,c)|=1\), the squared norms are \(1,21,6\), and the three pairwise inner products are \(4,11,2\). Hence \(\Omega=2\arctan(1/D)\). The signed-permutation fundamental sector has spherical area \(4\pi/48=\pi/12\). Therefore \(\Pr(N=10)=12\Omega/\pi=p\).

**4. An independent expectation identity determines the remaining probabilities.** Every edge's endpoint vectors enclose the angle \(\alpha=\arccos(4/5)\). The set of uniform normals for which two nonzero vectors have opposite projection signs occupies a spherical fraction equal to their angle divided by \(\pi\); this follows by taking the azimuth in their two-dimensional span. By linearity of expectation over the 36 edges,
\[
\mathbb E N=\sum_{\{v,w\}\in E(T)}\Pr((U\cdot v)(U\cdot w)<0)=\frac{36\alpha}{\pi}.
\]
If \(p_6,p_8,p_{10}\) denote the only three masses, then \(p_6+p_8+p_{10}=1\), \(6p_6+8p_8+10p_{10}=36\alpha/\pi\), and \(p_{10}=p\). Solving this linear system yields the stated formulas. All exceptional chamber walls have measure zero. This completes the proof.

## Verification
Run `python3 truncated_octahedron_section_checker.py` with Python 3 and its standard library. It exhaustively constructs the 24 vertices and 36 edges in exact integer arithmetic, verifies the five chamber representatives and polygon side counts, verifies the determinant and dot products in the spherical triangle, independently reconstructs 605 central sections from intersections of the 14 defining halfspaces, and checks the probability and expectation identities. A fixed-seed 120,000-orientation Monte Carlo check is only a numerical cross-check. Finite samples do not establish the continuous spherical probability formula, which follows analytically in the proof.

## Relationship to prior work
Cesaroni and Novaga (first public September 2, 2026) prove the distinguished isoperimetric property of the BCC Voronoi cell, the regular truncated octahedron; their surface-area theorem does not evaluate random central section polygon counts. Birkemeyer, Brose, Brandenburg and Prün (September 14, 2026) discuss combinatorial slicing signatures and reconstruction, motivating a quantitative angular section law; their available abstract does not assert the present distribution. De Loera, Lopez-Campos and Torres study feasible vertex counts in hyperplane sections of polytopes, including exact combinatorial methods, but their inspected theorems do not integrate the orientation chambers of this body. Published exact laws for central sections of the icosahedron or rectangular boxes concern different solids and cannot be substituted for the five-chamber calculation above.

## Limitations
The claim treats central, unoriented, Haar-random planes through a single regular truncated octahedron. It says nothing about planes with random offsets, affinely distorted truncated octahedra, or metric section area and perimeter. Exact historical priority remains subject to possible earlier calculations under the terms BCC Voronoi cell, Kelvin cell, or permutohedral slicing. No independent audit has been performed.

## References
1. A. Cesaroni and M. Novaga, *The truncated octahedron minimizes surface area among parallelohedra of equal volume*, arXiv:2609.02384 (first public 2026-09-02), https://arxiv.org/abs/2609.02384.
2. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (first public 2026-09-14), https://arxiv.org/abs/2609.16195.
3. J. A. De Loera, A. Lopez-Campos and R. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (first public 2024-12-17), https://arxiv.org/abs/2412.12419.
4. *Exact Haar polygon-type law for central icosahedron sections*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
