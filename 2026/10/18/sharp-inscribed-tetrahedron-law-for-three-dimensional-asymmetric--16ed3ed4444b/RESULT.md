# Sharp inscribed-tetrahedron law for three-dimensional asymmetric simplex difference bodies

## Finding
Let \(\Delta=\operatorname{conv}\{v_0,v_1,v_2,v_3\}\subset\mathbb R^3\) be any nondegenerate tetrahedron, and let \(s>0\). For the Minkowski sum \(K_s=\Delta+s(-\Delta)\), the largest-volume tetrahedron among **all** tetrahedra \(T\subseteq K_s\) satisfies
\[
\boxed{\max_{T\subseteq K_s}\operatorname{Vol}_3(T)
=(1+s)(1+s^2)\operatorname{Vol}_3(\Delta).}
\]
Exactly six tetrahedra attain the bound. They are the vertex-supported tetrahedra
\[
T_\sigma=\operatorname{conv}\{v_i-sv_{\sigma(i)}:i=0,1,2,3\},
\]
indexed by the six directed Hamiltonian cycles \(\sigma\) on \(\{0,1,2,3\}\). There are no additional nonvertex maximizers. The six maximizing vertex sets intersect pairwise in at most one vertex.

The containing body and its optimal volume occupancy have exact profiles
\[
\operatorname{Vol}_3(K_s)=(1+9s+9s^2+s^3)\operatorname{Vol}_3(\Delta),
\quad \boxed{\rho(s)=\frac{1+s^2}{1+8s+s^2}.}
\]
The function \(\rho\) decreases strictly for \(0<s<1\), increases strictly for \(s>1\), and has its unique positive-parameter minimum \(\rho(1)=1/5\). The endpoint value at the symmetric difference body is previously covered by work on the cuboctahedron; **the contribution is the complete asymmetric-parameter maximum and rigidity law**, not that isolated endpoint value or the known Minkowski-sum volume polynomial.

## Assumptions and scope
All volumes are ordinary Lebesgue volumes. A tetrahedron \(T\subseteq K_s\) may have vertices anywhere in \(K_s\), including on edges, faces, or in the interior. No Euclidean regularity assumption is placed on \(\Delta\); every assertion is invariant under nonsingular affine maps. The six claimed optimizers require strictly positive \(s\). At \(s=0\), the body is \(\Delta\) itself and the unique maximizing tetrahedron is \(\Delta\). The limit as \(s\to\infty\) is the reflected analogous case.

## Proof
**1. Standard-simplex reduction and complete vertices.** Apply a nonsingular affine map and translation to take \(\Delta=S=\operatorname{conv}\{0,e_1,e_2,e_3\}\). Translation of \(S\) translates \(S-sS\) and leaves all relative volumes unchanged. For each ordered pair of distinct indices \(i,j\in\{0,1,2,3\}\), set \(p_{ij}=v_i-sv_j\), with \(v_0=0\) and \(v_i=e_i\) for \(i>0\). Each \(p_{ij}\) is an exposed vertex: there is an affine functional on the four affinely independent original vertices whose unique maximum occurs at \(v_i\) and unique minimum at \(v_j\). Its maximum over \(S-sS\) is attained uniquely at \(p_{ij}\). Conversely any vertex of the Minkowski sum is the sum of exposed vertices from the two simplices, and cannot be \(v_i-sv_i\), which has no exposing functional simultaneously maximized and minimized by the same \(v_i\). Hence \(K_s\) has precisely these twelve vertices for all \(s>0\).

**2. Vertex reduction.** For any ordered four points \(z_0,z_1,z_2,z_3\), the oriented tetrahedral determinant
\[d(z_0,z_1,z_2,z_3)=\det(z_1-z_0,z_2-z_0,z_3-z_0)\]
is affine in each of its four vector arguments separately (equivalently it is the determinant of the four homogeneous rows \((1,z_i)\)). Expressing each \(z_i\in K_s\) as a convex combination of its twelve vertices makes \(d\) a convex combination of determinant values of vertex quadruples. Thus the unrestricted maximum absolute determinant equals the largest absolute determinant of a vertex quadruple.

**3. Exact determinant-spectrum certificate.** Each determinant of four distinct \(p_{ij}\) is an integer polynomial of degree at most three in \(s\), up to global sign. With \(\binom{12}{4}=495\) unordered quadruples, the complete exact spectrum (up to sign) is

| Absolute-determinant polynomial class | Number of quadruples |
| --- | ---: |
| \(0\) | 78 |
| \(s(s+1)\) | 120 |
| \(s^2\) | 72 |
| \(s\) | 72 |
| \(s^2(s+1)\) | 48 |
| \(s+1\) | 48 |
| \(s(s^2+s+1)\) | 24 |
| \(s^2+s+1\) | 24 |
| \((s+1)(s^2+1)\) | 6 |
| \(\left|(s-1)(s+1)^2\right|\) | 3 |

Every class other than the last is coefficientwise at most \(D(s)=(s+1)(s^2+1)=1+s+s^2+s^3\), strictly smaller for every \(s>0\) unless it is \(D\) itself. For the last class the positive difference is
\[
D(s)-|(s-1)(s+1)^2|=\begin{cases}2s^2(1+s),&0<s\le1,\\2(1+s),&s\ge1.\end{cases}
\]
Therefore \(D(s)\) is the unique largest polynomial class for all \(s>0\). The **standalone exact-integer** `verify.py` regenerates all 495 determinants directly using the 4-by-4 permutation formula, checks this complete histogram, and checks that the six top quadruples are precisely the directed four-cycles. These finite computations are exhaustive algebraic certificates; the inequalities just established extend their consequence to every real positive \(s\), rather than merely sampled values. Since a tetrahedron's volume is absolute determinant divided by six, and \(\operatorname{Vol}_3(S)=1/6\), the displayed sharp-volume formula follows.

**4. All equality cases, including unrestricted interior points.** An attaining vertex quadruple must be one of the six \(D\)-class quadruples. The checker shows combinatorially that two distinct such quadruples share at most one labeled vertex. Suppose an attaining tetrahedron had a nonvertex corner, with its other three corners arbitrary. Expand the oriented determinant multilinearly using convex vertex decompositions of all four corners, orienting the original determinant positive. Every summand is bounded above by the sharp positive determinant \(D(s)\), so equality of the weighted average forces every positive-weight summand to be maximizing. Choose any positive-weight choices for the other three corners and two distinct positive-weight vertices in the decomposition of the nonvertex corner. This creates two different maximizing vertex quadruples sharing the other three vertices, a contradiction. Thus all corners must be vertices. The six directed cycles are the complete equality family.

**5. The containing-body volume.** A point \(x\in S-sS\) is characterized exactly by
\[
\sum_{i:x_i>0}x_i\le1,\qquad
\sum_{i:x_i<0}(-x_i)\le s.
\]
Necessity follows from the two simplex representations; sufficiency follows by taking their positive and negative coordinate parts. In an orthant with \(k\) positive coordinate directions the coordinate volume is \(s^{3-k}/(k!(3-k)!)\). Summing over \(\binom3k\) such orthants gives
\[
\operatorname{Vol}_3(S-sS)=\frac{1+9s+9s^2+s^3}{6}.
\]
Affine invariance yields the formula for every \(\Delta\). Dividing the sharp tetrahedron formula by this expression and using \(1+9s+9s^2+s^3=(1+s)(1+8s+s^2)\) yields \(\rho(s)\). Finally,
\[
\rho'(s)=\frac{8(s^2-1)}{(1+8s+s^2)^2},
\]
proving the claimed strict monotonicity and the unique minimum \(\rho(1)=1/5\).

## Verification
Using Python 3, run `python3 verify.py`. It requires no third-party packages. The checker constructs the twelve ordered-pair vertices, evaluates all 495 homogeneous 4-by-4 determinants in exact integer polynomial arithmetic, compares the complete ten-class spectrum with the table, identifies the six maximizing quadruples, tests their directed-cycle representation and their pairwise vertex overlaps, and verifies coefficientwise gaps for the eight remaining non-sign-changing classes. It prints `VERIFY_OK quadruples=495 determinant_classes=10 maximum_orbits=6` on success. The exceptional sign-changing class is handled analytically in Proof step 3; the center and derivative calculations are symbolic derivations in step 5, not inferences from finite sampling. The checker was executed successfully on this exact included source.

## Relationship to prior work
The symmetric special case \(s=1\) is a cuboctahedron (up to affine equivalence); a published exact tetrahedral-volume profile for a cube–octahedron intersection family includes the same one-point occupancy \(1/5\). The endpoint alone is **not original** here, and its known coverage does not imply the full asymmetric parameter formula. For \(s\ne1\), the twelve-vertex \(K_s\) lacks central symmetry, unlike all members of that published intersection family. A published exact Santaló/Mahler-product analysis of the **very same** asymmetric simplex difference-body family supplies its primal volume polynomial but determines a different extremal quantity, the product with the polar volume; it does not give the unrestricted inscribed-tetrahedron maximum or its six-cycle equality classification. The classical Rogers–Shephard/Minkowski-sum volume inequalities and the 2013 study of convolution bodies concern volume, not the maximal contained tetrahedron. Lassak's general maximum-inscribed-simplex approximation inequalities and Akopyan–Glazyrin's geometric structure results likewise do not state this continuous sharp family formula. These comparisons establish meaningful nonimplication for the inspected statements, not global proof of historical novelty.

## Limitations
The theorem is three-dimensional and concerns a simplex summed with a positive dilation of its reflection; no higher-dimensional determinant formula or general convex-body extremum is asserted. The finite exact arithmetic is justified by source code whose exhaustive iteration and polynomial operations still warrant independent scrutiny. The original-value claim is limited to the full positive-parameter sharp law and complete equality classification; the known volume polynomial and symmetric special case value are not claimed as new. A differently named historical statement or an uninspected primary source might imply the result. Independent scientific audit has not been performed.

## References
1. M. Lassak, *Approximation of convex bodies by inscribed simplices of maximum volume*, 2011, DOI 10.1007/s13366-011-0026-x (first publicly online 2011-05-03). https://doi.org/10.1007/s13366-011-0026-x
2. D. Alonso-Gutiérrez, B. González and C. H. Jiménez, *Volume inequalities for the i-th-Convolution bodies*, arXiv:1312.6005, first posted 2013-12-20. https://arxiv.org/abs/1312.6005
3. A. Akopyan and A. Glazyrin, *On maximum volume simplices in polytopes*, 2014, DOI 10.1007/s10998-014-0051-2. Author-hosted text: https://users.mccme.ru/akopyan/papers/Akopyan-Glazyrin-Maximum-Volume.pdf
4. *Strict Mahler-product monotonicity along simplex asymmetric difference bodies*, publicly available mathematical finding, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-mahler-product-monotonicity-along-simplex-asymmetric-diff--516fa817d276
5. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, publicly available mathematical finding, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-tetrahedral-volume-profile-in-the-cube-octahedron-intersec--9ba1a511dacf
