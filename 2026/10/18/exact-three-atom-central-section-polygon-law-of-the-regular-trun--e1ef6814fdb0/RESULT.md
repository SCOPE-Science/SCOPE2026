# Exact three-atom central-section polygon law of the regular truncated tetrahedron

## Finding

For a uniformly oriented plane through the center of a regular truncated tetrahedron, its intersection polygon has **exactly four, five, or six vertices almost surely**. Its complete three-point law is elementary but nontrivial.

Write
\[
D_1=18\sqrt{10}+10\sqrt{30}+23\sqrt6+39\sqrt2,\qquad
D_2=6\sqrt5+9\sqrt2+13+4\sqrt{10},
\]
\[
q=\frac{24}{\pi}\left(\arctan\frac{2}{D_1}+\arctan\frac1{D_2}\right),\qquad
m=\frac{18}{\pi}\arccos\frac7{11}.
\]
Then the exact law is
\[
\boxed{\Pr(N=4)=q,\quad \Pr(N=5)=6-m-2q,\quad \Pr(N=6)=m-5+q.}
\]
The corresponding probabilities are, respectively,
\[
0.21593608531264047\ldots,\quad
0.52024746523893638\ldots,\quad
0.26381644944842315\ldots.
\]
The expected vertex count has the additional exact expression
\[
\mathbb E N=\frac{18}{\pi}\arccos\frac7{11}=5.04788036413578268\ldots.
\]

## Assumptions and scope

Let the original regular tetrahedron have vertices
\[
v_0=(1,1,1),\quad v_1=(1,-1,-1),\quad
v_2=(-1,1,-1),\quad v_3=(-1,-1,1).
\]
Uniformly truncate all four corners at one third of every incident edge. Thus the regular truncated tetrahedron is
\[
P=\operatorname{conv}\{(2v_i+v_j)/3:0\le i,j\le3,\ i\ne j\}.
\]
The origin is its center. The twelve vertices are equivalent to the signed permutations of \((3,1,1)/3\) having an even number of negative signs; there are eighteen edges. Let \(U\) be uniform on the Euclidean unit sphere and let \(N(U)\) count the vertices of \(P\cap U^\perp\). Since the unoriented planes corresponding to \(U\) and \(-U\) coincide, this defines the Haar distribution on central planes. We exclude the finitely many great circles for which a plane passes through a vertex. These exceptional orientations have spherical measure zero.

The statement is independent of a common positive scaling of the solid. It does **not** apply to uniformly translated affine planes, to projected silhouettes, or to partial and unequal truncations.

## Proof

### 1. Symmetry reduction

The full tetrahedral symmetry acts on the coordinate triples by arbitrary permutations and even sign changes; reversal of the plane normal does not alter a central section. Consequently the section vertex count is invariant under **all** signed permutations of the normal. Away from symmetry boundaries we may work in the fundamental cone
\[
x>y>z>0,\qquad U\parallel(x,y,z).
\]
Its spherical area is \(4\pi/48=\pi/12\). Put \(p=y/x\), \(s=z/x\). The cone becomes the rational triangle \(0<s<p<1\), with vertices \((0,0),(1,0),(1,1)\) in these projective coordinates.

### 2. Exact edge-crossing count

Label the twelve directed-edge vertices of \(P\) by \((i,j)\), meaning \((2v_i+v_j)/3\). The polytope has twelve edges inside the four small triangular truncation faces, connecting each pair \((i,j),(i,k)\) for distinct \(j,k\ne i\), and six edges \((i,j),(j,i)\) corresponding to the six original tetrahedron edges. This lists all eighteen edges.

For a generic central plane, an edge contributes exactly one section vertex if its endpoint scalar products with the plane normal have opposite signs. In the fundamental cone, four vertex scalar products are invariably positive, four invariably negative, and the remaining four have signs given by
\[
A=x-y-3z,\quad B=x-3y-z,\quad C=-x+3y-z,\quad D=-x-y+3z.
\]
Write \(a,b,c,d\in\{0,1\}\) for their positivity indicators. Directly counting the edges inside the four truncation triangles and the six bridge edges gives the exact identity
\[
\boxed{N=4+a+b+c+d-2ab.}
\]
Indeed the triangle-edge contribution is \(2(1-ab)+2c+2d\) and the bridge-edge contribution is \((1-c)+(1-d)+a+b\).

### 3. Exhaustive projective chamber arrangement

In the \((p,s)\) triangle, the four sign-change lines are
\[
p+3s=1,\quad3p+s=1,\quad3p-s=1,\quad3s-p=1.
\]
Intersecting their closed halfplanes with \(0\le s\le p\le1\) gives **exactly six** two-dimensional chambers. In the following table a quadruple records \((a,b,c,d)\), and each ordered pair is a rational \((p,s)\) vertex of the indicated chamber. This table results from exact linear halfplane intersections; checking all sixteen sign choices shows that the other ten choices have empty or lower-dimensional regions.

| Signs | \(N\) | Chamber vertices in \((p,s)\) |
|:--|:--:|:--|
| 0000 | 4 | \((1/2,1/2),(1/4,1/4),(2/5,1/5)\) |
| 0010 | 5 | \((1,0),(1,2/3),(1/2,1/2),(2/5,1/5)\) |
| 0011 | 6 | \((1,2/3),(1,1),(1/2,1/2)\) |
| 1000 | 5 | \((1/3,0),(2/5,1/5),(1/4,1/4)\) |
| 1010 | 6 | \((1/3,0),(1,0),(2/5,1/5)\) |
| 1100 | 4 | \((0,0),(1/3,0),(1/4,1/4)\) |

The projective coordinates \((p,s)\) represent spherical rays \((1,p,s)/\sqrt{1+p^2+s^2}\). Thus the chamber edges are great-circle segments. The table alone proves that the generic support of \(N\) is exactly \(\{4,5,6\}\), because every displayed chamber has nonempty interior.

### 4. Exact solid-angle evaluation of the quadrilateral mass

For three nonzero vectors \(r_1,r_2,r_3\) spanning an acute spherical triangle, its solid angle is
\[
\Omega(r_1,r_2,r_3)=2\arctan\frac{|\det(r_1,r_2,r_3)|}{\|r_1\|\|r_2\|\|r_3\|+(r_1\cdot r_2)\|r_3\|+(r_2\cdot r_3)\|r_1\|+(r_3\cdot r_1)\|r_2\|}.
\]
This is the standard exact spherical-triangle identity; all denominators used here are positive.

The two quadrilateral-section chambers have spherical vertex rays
\[
(2,1,1),(4,1,1),(5,2,1),\qquad
(1,0,0),(3,1,0),(4,1,1).
\]
Their determinants have absolute values \(2\) and \(1\), respectively. Substitution into the solid-angle identity yields
\[
\Omega_1=2\arctan\frac{2}{D_1},\qquad
\Omega_2=2\arctan\frac{1}{D_2}.
\]
Because each fundamental cone has area \(\pi/12\), the Haar probability of a quadrilateral section is
\[
\Pr(N=4)=\frac{12}{\pi}(\Omega_1+\Omega_2)=q.
\]
This evaluates the only nontrivial probability needed for the remaining two atoms.

### 5. Mean vertex count and completion of the law

The twelve vertex rays have equal squared lengths \(11\) after the harmless scaling by three. **Every one of the eighteen polyhedron edges** joins a pair with dot product \(7\). For two unit vectors making angle \(\theta\in[0,\pi]\), a Haar-random central plane separates their endpoints with probability \(\theta/\pi\); this follows by restricting the uniformly random normal to the two-dimensional span and measuring the two separating angular sectors.

Consequently, linearity of expectation gives the exact count
\[
\mathbb E N=\sum_{\mathrm{edges}\ e}\Pr(e\text{ crosses the plane})
=\frac{18}{\pi}\arccos\frac7{11}=m.
\]
If \(p_k=\Pr(N=k)\), then \(p_4+p_5+p_6=1\) and \(4p_4+5p_5+6p_6=m\), hence \(p_6-p_4=m-5\). Substituting \(p_4=q\) gives
\[
p_6=m-5+q,\qquad p_5=6-m-2q,
\]
proving all three formulas. Positivity can be read directly from the nonempty spherical chambers in the table rather than from numerical approximations.

## Verification

The standalone standard-library checker `check.py` constructs all twelve vertices and eighteen edges, exhaustively clips all sixteen sign choices by exact rational arithmetic, verifies precisely the six chamber polygons and their section counts, evaluates the spherical triangle areas, and checks the independent eighteen-edge expectation identity. It additionally compares the derived vertex-count formula with ten thousand random normals and independently reconstructs 1,800 projected convex hulls of the exact edge-plane intersection points. Execute in the directory containing this file and the checker with `python3 check.py`. The numerical samples corroborate the formula; the all-direction proof consists of the exact edge graph, exhaustive sign-chamber arrangement, and solid-angle identities above.

## Relationship to prior work

The classical Archimedean truncated tetrahedron and its one-third vertex truncation are standard objects; Damasceno, Engel and Glotzer [1] study a family of truncated tetrahedra in the context of packing and assembly. The general study by De Loera, Lopez-Campos and Torres [2] gives extremal bounds, combinatorial slice enumeration principles, and attainable vertex-count sets for polytopes; its theorems and examples do not specify Haar probabilities for the central slices of this Archimedean solid. The present result measures the precise spherical sizes of all three generic section-complexity strata. It is not merely a restatement of the known possible polygon types or their mean.

This is a mathematical priority assessment against inspected evidence, not a claim of exhaustive historical priority.

## Limitations

The law treats uniformly oriented **central** sections of one fixed regular truncated tetrahedron. It does not cover affine offsets, uniformly random intersecting planes with a translation measure, other truncation depths, or the joint law with section area or perimeter. Exceptional normals lying on the twelve vertex-orthogonality great circles are excluded, as required for an almost-sure distribution. The 2011 packing source's full manuscript was inaccessible in this examination, leaving a residual historical-priority risk. Independent mathematical validation has not been performed.

## References

[1] P. F. Damasceno, M. Engel, S. C. Glotzer, *Crystalline Assemblies and Densest Packings of a Family of Truncated Tetrahedra and the Role of Directional Entropic Forces*, arXiv:1109.1323, initial public version 6 September 2011. https://arxiv.org/abs/1109.1323

[2] J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419, initial public version 17 December 2024. https://arxiv.org/abs/2412.12419
