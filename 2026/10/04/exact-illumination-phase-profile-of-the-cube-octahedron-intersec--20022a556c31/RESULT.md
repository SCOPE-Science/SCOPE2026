# Exact illumination phase profile of the cube–octahedron intersection family

## Finding

For \(1\le c\le3\), define the three-dimensional convex body
\[
K_c=[-1,1]^3\cap\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le c\}.
\]
Then
\[
\boxed{
\mathfrak I(K_c)=
\begin{cases}
6,&c=1,\\
4,&1<c<3,\\
8,&c=3.
\end{cases}}
\]
Moreover, throughout the whole open interval \(1<c<3\), one fixed tetrahedral set of directions works:
\[
\mathcal D=\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}.
\]
In particular,
\[
\mathfrak I(K_{3/2})=
\mathfrak I(K_2)=
\mathfrak I(K_{1+\sqrt2})=4,
\]
where these three bodies are respectively a regular truncated octahedron, a cuboctahedron, and a regular truncated cube.

## Assumptions and scope

A nonzero direction \(d\) illuminates a boundary point \(x\) of a convex body \(K\) if \(x+\varepsilon d\in\operatorname{int}K\) for some \(\varepsilon>0\). The illumination number \(\mathfrak I(K)\) is the least cardinality of a set of directions illuminating every boundary point.

For a polytope it is enough to illuminate every vertex. Equivalently, by the standard outer-normal criterion, a direction \(d\) illuminates a vertex \(x\) precisely when
\[
\langle d,u\rangle<0
\]
for every outer normal \(u\) in the normal cone at \(x\).

The family \(K_c\) is invariant under all coordinate permutations and sign changes. At \(c=1\) it is the regular octahedron and at \(c=3\) it is the cube. The theorem concerns the ordinary illumination number, not the weighted illumination parameter.

## Proof

First recall the universal lower bound
\[
\mathfrak I(K)\ge4
\]
for every three-dimensional convex body \(K\). Indeed, if a finite illuminating set \(D\) did not have the origin in the interior of \(\operatorname{conv}D\), a separating vector \(u\ne0\) could be chosen so that
\[
\langle u,d\rangle\ge0
\]
for every \(d\in D\). At a support point of \(K\) with outer normal \(u\), the outer-normal criterion would require some illuminating direction to have negative dot product with \(u\), a contradiction. Hence \(0\in\operatorname{int}\operatorname{conv}D\), which requires at least four directions in \(\mathbb R^3\).

Now suppose \(1<c<2\). Every vertex of \(K_c\) is a signed coordinate permutation of
\[
(1,c-1,0).
\]
Write such a vertex using two distinct coordinate indices \(i,j\), the remaining index \(k\), and signs \(s_i,s_j\in\{\pm1\}\). The active facet normals are
\[
s_i e_i
\]
and
\[
s_i e_i+s_j e_j+e_k,
\qquad
s_i e_i+s_j e_j-e_k.
\]
There is a unique \(d\in\mathcal D\) with
\[
d_i=-s_i,
\qquad
d_j=-s_j.
\]
For this direction,
\[
\langle d,s_i e_i\rangle=-1,
\]
while the other two active normals have dot products
\[
-2+d_k,
\qquad
-2-d_k,
\]
which are \(-1\) and \(-3\). Thus every vertex is illuminated by \(\mathcal D\).

At \(c=2\), every vertex is a signed permutation of \((1,1,0)\). The same choice of \(d\) also has dot product \(-1\) with each of the two active coordinate-facet normals, and still has dot products \(-1\) and \(-3\) with the two active \(\ell_1\)-facet normals. Hence \(\mathcal D\) illuminates \(K_2\).

Next suppose \(2<c<3\). Every vertex is a signed coordinate permutation of
\[
(1,1,c-2).
\]
Let \(i,j\) be the two coordinates of absolute value \(1\), let \(k\) be the remaining coordinate, and let \(s=(s_1,s_2,s_3)\) be the sign vector of the vertex. The active normals are
\[
s_i e_i,
\qquad
s_j e_j,
\qquad
s.
\]
Choose the unique \(d\in\mathcal D\) satisfying
\[
d_i=-s_i,
\qquad
d_j=-s_j.
\]
Then the first two dot products are \(-1\), while
\[
\langle s,d\rangle=-2+s_kd_k\in\{-3,-1\}.
\]
Again every active dot product is strictly negative. Therefore
\[
\mathfrak I(K_c)\le4
\]
for every \(1<c<3\). The universal lower bound gives equality.

It remains to treat the endpoints. For \(K_1\), the regular octahedron, consider a vertex \(s e_i\), with \(s\in\{\pm1\}\). The extreme outer normals at this vertex have \(i\)-th coordinate \(s\) and arbitrary signs in the other two coordinates. Hence a direction \(d\) can illuminate \(s e_i\) only if
\[
sd_i+|d_j|+|d_k|<0.
\]
This forces \(|d_i|>|d_j|+|d_k|\) and fixes the sign of \(d_i\). No one direction can satisfy the corresponding condition for two distinct octahedron vertices: opposite vertices demand opposite signs, while vertices on different axes would force both \(|d_i|>|d_j|\) and \(|d_j|>|d_i|\). Thus at least six directions are required. The six inward axial directions illuminate the six vertices, so
\[
\mathfrak I(K_1)=6.
\]

For \(K_3=[-1,1]^3\), a direction illuminates a cube vertex \(s\in\{\pm1\}^3\) only if
\[
s_i d_i<0
\]
for all three coordinates. Two distinct cube vertices differ in at least one sign and therefore cannot share an illuminating direction. Thus at least eight directions are needed, and the eight opposite vertex directions attain this bound. Hence
\[
\mathfrak I(K_3)=8.
\]

## Verification

The standalone `verify.py` exhausts every active-normal sign pattern in both open combinatorial chambers and at the transition \(c=2\). It confirms that the four tetrahedral directions give strictly negative dot products against every active facet normal. It also checks the explicit six-direction and eight-direction endpoint constructions and the combinatorial incompatibility underlying the endpoint lower bounds.

The replay output is:

`VERIFY_OK cube-octahedron illumination phase profile`

The finite checker is a consistency check for the chamber classification and sign algebra. The continuum claim for all \(c\) is proved symbolically above; it is not inferred from sampling finitely many parameters.

## Relationship to prior work

Sun and Vritsiou prove the Hadwiger–Boltyanski illumination conjecture for all 1-symmetric convex bodies in every dimension. Their Theorem 23 yields, in dimension three, an upper bound of six directions for normalized non-cubic 1-symmetric bodies under its hypotheses. Their paper also records the outer-normal illumination criterion used above. The present result is object-specific and sharper: it determines the exact number throughout a natural one-parameter 1-symmetric family, showing that every strict cube–octahedron mixture has the dimension-minimal value four.

Livshyts and Tikhomirov prove that every non-parallelotope sufficiently close to the cube can be illuminated by at most seven directions in dimension three. That result does not imply the four-direction conclusion here, including for parameters arbitrarily close to \(c=3\).

Kiss and de Wet study a different invariant, the weighted illumination parameter. They determine exact weighted values for centrally symmetric Platonic solids and give estimates for centrally symmetric Archimedean solids. Their invariant penalizes the norms of light-source positions; those statements do not determine the ordinary illumination number used here.

A separate indexed exact result gives illumination number four for one canonical truncated-octahedron representative. That agrees with the special value \(c=3/2\), but it neither covers the cuboctahedron or truncated cube nor implies the uniform four-direction statement for the continuous family. An earlier finding concerning independent truncations of cube corners also does not imply this theorem: for \(c>2\), all eight adjacent cube corners are truncated simultaneously, so the required independence condition fails, and the \(c\le2\) part has a different combinatorial structure.

## Limitations

The theorem is three-dimensional and specific to the intersection of the standard cube with a concentric \(\ell_1\)-ball. It does not classify illumination numbers of arbitrary 1-symmetric bodies or arbitrary Archimedean solids.

The four-direction proof exploits the exact active-normal patterns of this family. It does not show that a fixed tetrahedral set illuminates all non-cubic 1-symmetric bodies.

Targeted searches did not locate the continuous phase profile or the cuboctahedron/truncated-cube special cases as ordinary illumination-number statements. Because the proof is short and the solids are classical, differently phrased or unindexed prior observations remain a residual originality risk.

## References

W. R. Sun and B.-H. Vritsiou, “On the illumination of 1-symmetric convex bodies,” arXiv:2407.10314, first submitted 2024-07-14. Primary MSC 52A40, 52A37.

G. Livshyts and K. Tikhomirov, “Cube is a Strict Local Maximizer for the Illumination Number,” Discrete & Computational Geometry 63 (2020), 209–228, DOI 10.1007/s00454-019-00115-9.

G. Kiss and P. O. de Wet, “Notes on the illumination parameters of convex polytopes,” Contributions to Discrete Mathematics 7 (2012), 58–67, DOI 10.55016/ojs/cdm.v7i1.62108.
