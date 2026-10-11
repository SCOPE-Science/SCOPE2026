# Exact fractional illumination of the regular dodecahedron and icosahedron
## Finding
Let \(D\subset\mathbb R^3\) be a regular dodecahedron and let \(I\subset\mathbb R^3\) be a regular icosahedron. Then
\[
\boxed{i^*(D)=i^*(I)=4}.
\tag{1}
\]
In addition,
\[
\boxed{i(D)=5}.
\tag{2}
\]
Consequently the regular dodecahedron has the exact ordinary-to-fractional gap
\[
\boxed{\frac{i(D)}{i^*(D)}=\frac54}.
\tag{3}
\]

The mechanism is a general symmetry identity. If \(P\) is a vertex-transitive polytope and
\[
\alpha(P)=\max_u\#\{v\in\operatorname{vert}P:u\text{ illuminates }v\},
\]
then
\[
\boxed{i^*(P)=\frac{f_0(P)}{\alpha(P)}}.
\tag{4}
\]
For the dual Platonic pair,
\[
\alpha(D)=5,
\qquad
\alpha(I)=3.
\tag{5}
\]

## Assumptions and scope
A direction \(u\in S^2\) illuminates a boundary point \(x\) of a convex body \(K\) when \(x+\varepsilon u\in\operatorname{int}K\) for some \(\varepsilon>0\). A finite nonnegative measure \(\mu\) on directions is a fractional illumination when every boundary point receives total illuminating weight at least \(1\). The infimum of \(\mu(S^2)\) is \(i^*(K)\).

For a polytope, it is enough to impose the fractional constraints at the vertices. Indeed, if a boundary point \(x\) belongs to a face and
\[
x=\lambda v+(1-\lambda)y,
\qquad
0<\lambda\le1,
\]
with \(v\) a vertex of that face and \(y\in P\), then every direction illuminating \(v\) also illuminates \(x\): if \(v+\varepsilon u\in\operatorname{int}P\), then
\[
x+\lambda\varepsilon u
=
\lambda(v+\varepsilon u)+(1-\lambda)y
\in\operatorname{int}P.
\]

The ordinary statement (2) concerns parallel-direction illumination, not the different norm-weighted illumination parameter studied by Kiss and de Wet.

## Proof
### 1. A vertex-transitive fractional formula
Let \(P\) have \(N=f_0(P)\) vertices and put \(\alpha=\alpha(P)\). For any fractional illumination \(\mu\), summing the \(N\) vertex constraints gives
\[
N
\le
\sum_{v\in\operatorname{vert}P}
\mu\{u:u\text{ illuminates }v\}.
\]
Interchanging the finite vertex sum with the finitely supported measure yields
\[
N
\le
\int \#\{v:u\text{ illuminates }v\}\,d\mu(u)
\le
\alpha\,\mu(S^2).
\]
Thus
\[
i^*(P)\ge\frac N\alpha.
\tag{6}
\]

For the reverse inequality, choose a direction \(u_0\) illuminating exactly \(\alpha\) vertices, and let \(G\) be a finite symmetry group acting transitively on the vertices. Average the Dirac mass at \(u_0\) over \(G\), assigning weight
\[
\frac{N}{\alpha|G|}
\]
to each group element's image of \(u_0\), with repeated directions combined. The total number of incidences
\[
(g,v):g u_0\text{ illuminates }v
\]
is \(|G|\alpha\). Vertex transitivity makes the incidence count the same at every vertex, hence each vertex receives total weight exactly \(1\). The total mass is \(N/\alpha\), proving (4).

### 2. Polar reformulation
Let \(P=Q^\circ\), with the origin in the interiors. A vertex \(v\) of \(P\) corresponds to the facet
\[
F_v=\{y\in Q:\langle v,y\rangle=1\}
\]
of \(Q\). The direction \(u\) illuminates \(v\) exactly when every active inequality decreases, that is,
\[
\langle u,y\rangle<0
\qquad
\text{for every vertex }y\text{ of }F_v.
\tag{7}
\]
Thus \(\alpha(P)\) is the maximum number of facets of \(Q\) lying wholly in one open halfspace bounded by a plane through the origin.

Both regular duals are centrally symmetric. If a central plane contains no vertex, one side contains exactly one vertex from every antipodal pair. If a plane is nongeneric but contains some vertices, a sufficiently small perturbation preserves every facet already lying strictly in the chosen open halfspace. Therefore an upper bound may be obtained by enumerating every antipodal transversal, even transversals that are not geometrically realizable by a plane.

### 3. Exact finite certificates for \(\alpha(D)\) and \(\alpha(I)\)
Use the standard regular icosahedron
\[
Q_I=
\operatorname{conv}
\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]
It has six antipodal vertex pairs and twenty triangular facets. Exhausting the \(64\) choices of one vertex from every antipodal pair gives the following exact distribution for the number of triangular facets contained in the chosen six-vertex set:
\[
12\text{ choices contain }0,
\quad
20\text{ contain }1,
\quad
20\text{ contain }4,
\quad
12\text{ contain }5.
\tag{8}
\]
Hence at most five facets can lie in an open central halfspace. The bound is attained by explicit integer halfspace normals, as checked in `verify.py`. Since \(Q_I^\circ\) is a regular dodecahedron,
\[
\alpha(D)=5.
\tag{9}
\]

Similarly, use the standard regular dodecahedron with vertices
\[
(\pm1,\pm1,\pm1),
\quad
(0,\pm\varphi^{-1},\pm\varphi),
\quad
(\pm\varphi^{-1},\pm\varphi,0),
\quad
(\pm\varphi,0,\pm\varphi^{-1}).
\]
It has ten antipodal vertex pairs and twelve pentagonal facets. The \(1024\) antipodal transversals have exact facet-count distribution
\[
740\text{ choices contain }0,
\quad
204\text{ contain }1,
\quad
60\text{ contain }2,
\quad
20\text{ contain }3.
\tag{10}
\]
Again the maximum is attained by a genuine open central halfspace. Since the polar is a regular icosahedron,
\[
\alpha(I)=3.
\tag{11}
\]

Applying (4) to the vertex-transitive solids gives
\[
i^*(D)=\frac{20}{5}=4,
\qquad
 i^*(I)=\frac{12}{3}=4,
\]
which proves (1).

### 4. The ordinary dodecahedral value
The upper bound in (9) implies
\[
i(D)\ge4.
\]
Suppose four directions illuminated all twenty vertices. Since every direction illuminates at most five vertices, each direction would have to illuminate exactly five, and the four five-sets would have to be pairwise disjoint.

The twelve size-five transversal sets occurring in (8) form a finite superset of all possible five-vertex parallel illumination sets. The bundled exhaustive certificate checks all
\[
\binom{12}{4}=495
\]
quadruples and finds no quadruple whose union is all twenty facets of \(Q_I\). Hence four directions are impossible.

For the matching upper bound, in the displayed icosahedral coordinates the five central-halfspace normals
\[
(-5,-5,-5),
\quad
(-5,-5,-3),
\quad
(-5,4,-2),
\quad
(1,0,-1),
\quad
(1,0,2)
\tag{12}
\]
have positive halfspaces whose contained triangular facets together cover all twenty facets of \(Q_I\). Via (7), their negatives give five illuminating directions for the polar regular dodecahedron. Therefore
\[
i(D)=5,
\]
proving (2) and (3).

## Verification
The standalone `verify.py` works exactly in the quadratic field \(\mathbb Q(\sqrt5)\), represented as \(a+b\varphi\) with \(\varphi^2=\varphi+1\). It uses no floating-point comparisons for the scientific certificate.

It reconstructs the icosahedral edge graph from the exact squared edge length \(4\), proves that its twenty three-cliques are exactly the listed triangular facets, reconstructs the dodecahedral edge graph from squared edge length \(8-4\varphi\), and proves that its twelve five-cycles are exactly the listed pentagonal facets.

It then exhausts all \(64\) and \(1024\) antipodal transversals, verifies the distributions (8) and (10), checks the nonexistence of a four-set dodecahedral cover, and verifies the five explicit halfspace normals in (12). It also verifies an explicit four-halfspace cover in the dual dodecahedral model as a consistency check for the known icosahedral ordinary cover.

## Relationship to prior work
Naszódi introduced \(i^*(K)\), proved the general centrally symmetric bound
\[
i^*(K)\le 2^d,
\]
and formulated fractional illumination as a fractional transversal problem. His paper gives a regular-pentagon lower bound but no dodecahedral or icosahedral evaluation.

Kiss and de Wet later studied the regular dodecahedron and icosahedron in detail, but their principal invariant is a different norm-weighted illumination parameter. Their full text does define the ordinary illumination number and supplies geometric facts highly relevant here: in the dodecahedral analysis a single finite light source can illuminate at most five vertices, and in the icosahedral analysis at most three; it also records a four-face cover of the icosahedral vertices. The paper contains no occurrence of fractional illumination and does not state (1)--(3). The present proof independently certifies the parallel-direction incidence bounds in the polar models and performs the fractional optimization.

A modern general theorem gives the sharp universal exponential bound for fractional illumination and characterizes equality at parallelotopes, but it does not determine the exact value for either Platonic solid.

Targeted searches under fractional illumination, Platonic solids, dodecahedron, icosahedron, ordinary illumination number, and symmetry-orbit formulations did not locate an implication-equivalent published evaluation.

## Limitations
The symmetry identity (4) reduces fractional illumination of a vertex-transitive polytope to the finite invariant \(\alpha(P)\), but computing \(\alpha(P)\) can still be difficult in higher dimensions.

The ordinary value \(i(I)=4\) is not claimed as new here; it is already implicit in the 2012 Platonic-solid analysis. The new ordinary assertion is the dodecahedral value (2), combined with the exact fractional evaluations and the gap (3).

The dodecahedral and icosahedral finite certificates exploit central symmetry and Platonic duality and do not automatically extend to nonregular realizations of the same combinatorial types.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, *Contributions to Discrete Mathematics* 4 (2009), 83--88. DOI: 10.55016/ojs/cdm.v4i2.62022.
2. G. Kiss and P. Oloff de Wet, *Notes on the illumination parameters of convex polytopes*, *Contributions to Discrete Mathematics* 7 (2012), 58--67. DOI: 10.55016/ojs/cdm.v7i1.62108.
3. H. Martini and P. S. Soltan, *Combinatorial problems on the illumination of convex bodies*, *Aequationes Mathematicae* 57 (1999), 121--152. DOI: 10.1007/s000100050074.
4. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1, 20 September 2026.
