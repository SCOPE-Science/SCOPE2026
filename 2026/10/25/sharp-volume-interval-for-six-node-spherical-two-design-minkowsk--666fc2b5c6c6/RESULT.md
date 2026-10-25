# Sharp volume interval for six-node spherical two-design Minkowski polyhedra

## Finding

Let \(X=\{x_1,\ldots,x_6\}\subset S^2\) be any six **distinct**, equally weighted spherical \(2\)-design nodes. Let \(P_X\) be the convex polytope, unique up to translation, with these six outward unit facet normals and each facet of area \(2\pi/3\). There exists an angle \(0\leq\phi\leq\pi/3\) such that \(X\), up to a Euclidean orthogonal transformation and relabeling, is
\[
 u_j=\left(\sqrt{\frac23}\cos\frac{2\pi j}{3},\sqrt{\frac23}\sin\frac{2\pi j}{3},\frac1{\sqrt3}\right),\quad
 v_j=\left(\sqrt{\frac23}\cos\left(\frac{2\pi j}{3}+\phi\right),\sqrt{\frac23}\sin\left(\frac{2\pi j}{3}+\phi\right),-\frac1{\sqrt3}\right),\quad j=0,1,2.
\]
Set \(t=2\cos(\pi/3-\phi)\in[1,2]\). Then the exact volume, with the stated facet-area normalization, is
\[
 \boxed{\operatorname{Vol}_3(P_X)=\frac{4\pi^{3/2}}{9\sqrt3}\frac{t+1}{\sqrt t}.}
\]
It is strictly increasing as \(\phi\) increases from \(0\) to \(\pi/3\). Consequently,
\[
 \boxed{\frac{8\pi^{3/2}}{9\sqrt3}\leq\operatorname{Vol}_3(P_X)\leq\left(\frac{2\pi}{3}\right)^{3/2}.}
\]
The lower equality occurs precisely for the \(\phi=0\) normal configuration, whose Minkowski polytope is a triangular bipyramid. The upper equality occurs precisely for \(\phi=\pi/3\), the antipodal orthonormal-octahedron normals, whose Minkowski polytope is a cube. For \(0<\phi<\pi/3\), the polytope has six congruent-area quadrilateral facets and eight vertices (combinatorial cube). Every intermediate volume is attained. The one-parameter classification and the sharp volume statement are one integrated finding.

## Assumptions and scope

A six-node equally weighted spherical \(2\)-design means six distinct unit vectors whose sum is zero and whose outer-product sum is \(2I_3\). These are exactly the degree-at-most-two spherical quadrature equations on \(S^2\). The surface-area measure specifying \(P_X\) is \(\frac{2\pi}{3}\sum_{x\in X}\delta_x\); total surface area is \(4\pi\). Volume is independent of the translation chosen. All angles are radians, all areas Euclidean, and all bodies are three-dimensional convex polytopes. The claim concerns exactly six *unweighted* normals; no assertion is made for weighted nodes or other cardinalities.

## Proof

**1. Orthogonal-triplet classification.** Form the real \(3\times6\) matrix \(M\) whose columns are the design nodes. The two design identities give \(M\mathbf1=0\) and \(MM^{\mathsf T}=2I_3\). Therefore \(E=\frac12M^{\mathsf T}M\) is a rank-three orthogonal projector, annihilates \(\mathbf1\), and has all diagonal entries \(1/2\). Let \(J=\mathbf1\mathbf1^{\mathsf T}\) and put \(F=I_6-J/6-E\). This is the orthogonal projector onto the two-dimensional complement of \(\mathbf1\) and the row space of \(M\), with every diagonal entry equal to \(1/3\).

Choose a real \(2\times6\) matrix \(Y\) with orthonormal rows such that \(F=Y^{\mathsf T}Y\). Its columns \(y_i\) satisfy \(\lVert y_i\rVert^2=1/3\), \(\sum_i y_i=0\), and \(\sum_i y_i y_i^{\mathsf T}=I_2\). Write \(z_i=\sqrt3(y_{1i}+\mathrm{i}y_{2i})\); these are six complex numbers of modulus one satisfying \(\sum_i z_i=0\) and \(\sum_i z_i^2=0\). Newton's identity gives the first two elementary symmetric functions \(e_1=e_2=0\). The unit-modulus roots obey \(e_{6-k}=e_6\overline{e_k}\), so \(e_4=e_5=0\). Their characteristic polynomial therefore has the form \(z^6-e_3z^3+e_6\), which factors as \((z^3-\alpha)(z^3-\beta)\). Thus the six \(z_i\), counted with multiplicity, partition into two equilateral triples on the unit circle (even when \(\alpha=\beta\)). For distinct indices in the same triple, \(y_i\cdot y_j=-1/6\). From \(E_{ij}=\delta_{ij}-1/6-y_i\cdot y_j\), one obtains \(x_i\cdot x_j=2E_{ij}=0\). Hence \(X\) partitions into two orthonormal triples.

The sums of those triples are opposite and each has norm \(\sqrt3\). Choose the normalized first sum as the vertical axis. Each first-triple vector has vertical coordinate \(1/\sqrt3\), each second-triple vector has vertical coordinate \(-1/\sqrt3\), and their horizontal components form equilateral triples of common radius \(\sqrt{2/3}\). Horizontal rotation and dihedral relabeling reduce their relative twist to \(\phi\in[0,\pi/3]\), yielding the displayed parametrization. Conversely this parametrization is an orthonormal-triple union with opposite sums, hence satisfies both design equations for every allowed \(\phi\).

**Minimal cardinality of the flexible case.** For four nodes the same projector argument leaves no complementary subspace and forces the regular tetrahedral Gram matrix. Five nodes are impossible: the complementary projector would have rank one and diagonal \(1/5\), so its spanning unit vector would have five entries all equal to \(\pm1/\sqrt5\). It must also be orthogonal to \(\mathbf1\), which is impossible with an odd number of such entries. Thus six is the first node count admitting designs other than the unique tetrahedral configuration.

**2. The unit-support polyhedron.** Define
\[
 Q_\phi=\{w\in\mathbb R^3: w\cdot u_j\leq1,\ w\cdot v_j\leq1,\ j=0,1,2\}.
\]
The six supporting planes are tangent to the unit ball. Rotations by \(2\pi/3\) about the vertical axis, together with the half-turn \((r,\theta,z)\mapsto(r,\phi-\theta,-z)\), act transitively on the six facet normals. Thus all six facet areas of \(Q_\phi\) are equal. Put
\[
 h=\sqrt{2/3},\quad t=2\cos(\pi/3-\phi),\quad R=\frac4{h(t+1)},\quad z_0=\frac{\sqrt3(t-1)}{t+1}.
\]
Its vertices are the two poles \((0,0,\pm\sqrt3)\) and the two triples
\[
 B_j=(R\cos(\pi/3+2\pi j/3),R\sin(\pi/3+2\pi j/3),z_0),\quad
 C_j=(R\cos(\phi+\pi/3+2\pi j/3),R\sin(\phi+\pi/3+2\pi j/3),-z_0).
\]
Indeed, direct substitution checks that each point satisfies all six inequalities, with the indicated incident supporting planes. Exhaustion follows by polarity: the convex hull of the six normals is a triangular antiprism with eight faces when \(\phi>0\), and a triangular prism with five faces when \(\phi=0\). At the latter endpoint the triples \(B_j,C_j\) coincide, giving just five vertices. The antiprism polar has eight vertices throughout \(0<\phi\leq\pi/3\).

**3. Exact facet area and volume.** Consider the face \(w\cdot u_0=1\). Its four cyclic vertices (allowing a doubled vertex at \(\phi=0\)) are the upper pole, \(B_0\), \(C_2\), and \(B_2\). The diagonals are the segments joining \(B_0\) to \(B_2\) and the upper pole to \(C_2\). Computing half the norm of their cross product gives
\[
 \operatorname{Area}(Q_\phi\cap\{w:w\cdot u_0=1\})
   =\frac34R^2t=\frac{18t}{(t+1)^2}=:A_0(t).
\]
One direct simplification is \(\sqrt3+z_0=\sqrt2R\cos(\phi-\pi/3)\), which follows from the supporting-plane equation. By facet transitivity the total area is \(6A_0(t)\). The divergence theorem, all outward supports being one, gives
\[
 \operatorname{Vol}_3(Q_\phi)=\frac13\sum_{\text{six facets}}1\cdot A_0(t)=2A_0(t)=\frac{36t}{(t+1)^2}.
\]

**4. Minkowski normalization and sharpness.** The homothetic polytope \(\lambda Q_\phi\), with
\[
 \lambda^2=\frac{2\pi/3}{A_0(t)}=\frac{\pi(t+1)^2}{27t},
\]
has the prescribed six normal directions and facet areas \(2\pi/3\). Minkowski uniqueness identifies it with \(P_X\) up to translation. Cubic volume scaling yields the boxed exact formula. The derivative
\[
 \frac{d}{dt}\frac{t+1}{\sqrt t}=\frac{t-1}{2t^{3/2}}
\]
is positive for \(1<t\leq2\), and \(t(\phi)\) is strictly increasing from \(1\) to \(2\) on \([0,\pi/3]\). Evaluation at the endpoints yields the sharp interval and equality cases. It also shows no distinct twist inside the fundamental interval gives the same volume, so the single modulus distinguishes the isometry classes of these normalized polytopes.

## Verification

The accompanying standalone script `verify.py` checks the symbolic facet-area identity, volume scaling, monotonicity derivative, endpoint formulas, all first and second design moments, and convex-hull areas, volumes, and vertex numbers for six representative twist angles including both endpoints. It constructs the polyhedra independently from their six halfspace inequalities using SciPy; all checks pass. The proof above is the all-parameter certificate; finite numerical tests alone would not establish the theorem. Run with `python verify.py` in an environment with NumPy, SciPy, and SymPy.

## Relationship to prior work

An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity* (first posted August 12, 2026), Theorems 3.1 and 3.4, establishes the equal-area Minkowski realization and its general equivalence with spherical designs. Its Theorem 4.2 treats normalized surface tensors; its mixed-volume result concerns a different, linear functional. This paper's full available text does not classify six-node designs, derive their unit-support facet areas, or bound the volumes of their Minkowski polyhedra. Chien and Kang, *Spherical 2-Designs from Finite Group Orbits* (first posted August 18, 2025), classifies design orbits via representations, without the six-node volume formula or extremizers. An, *Dual Geometry of Spherical Designs: Polarity, Self-Polar Rigidity, and Quadrature Structure* (first posted September 2, 2026), concerns polar-incidence and self-polar rigidity, not this complete six-normal volume interval. A published mathematical record concerning fourth-order affine rigidity of equal-area Minkowski polytopes addresses deformations preserving equal areas rather than the precise six-node two-design volume extremizers. Classical results on tight frames, triangular prisms, and triangular antiprisms may provide some components individually; this work's claim is their fully quantified synthesis for **all** six-node spherical two-design realizations.

## Limitations

Only the six-node, three-dimensional, equal-weight second-design case is classified. The result does not establish a corresponding volume interval for seven or more nodes, for weighted designs, or for all equal-area hexahedra without the second-design normal condition. It makes no claim that the orthogonal-basis decomposition by itself is unprecedented in frame theory; its novelty assessment concerns the integrated exact Minkowski volume classification. Older unindexed work on twisted triangular trapezohedra or isotropic normal configurations might overlap and is a residual priority risk. No external independent audit has been performed.

## References

1. Congpei An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570v1, first posted 2026-08-12, https://arxiv.org/abs/2608.11570 .
2. Kuan-Cheng Chien and Ming-Hsuan Kang, *Spherical 2-Designs from Finite Group Orbits*, arXiv:2508.12580v1, first posted 2025-08-18, https://arxiv.org/html/2508.12580 .
3. Congpei An, *Dual Geometry of Spherical Designs: Polarity, Self-Polar Rigidity, and Quadrature Structure*, arXiv:2609.02439v1, first posted 2026-09-02, https://arxiv.org/abs/2609.02439 .
4. H. Minkowski, classical existence and uniqueness theorem for surface area measures of convex polytopes (standard formulation as recalled in Reference 1, Theorem 2.2).
