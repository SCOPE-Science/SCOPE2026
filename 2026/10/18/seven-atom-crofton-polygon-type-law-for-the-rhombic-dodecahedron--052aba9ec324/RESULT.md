# Seven-atom Crofton polygon-type law for the rhombic dodecahedron

## Finding

Let \(K\subset\mathbb R^3\) be the standard rhombic dodecahedron
\[
K=\{(x_1,x_2,x_3): |x_i|+|x_j|\le2\text{ whenever }1\le i<j\le3\}.
\]
Choose an unoriented affine plane from Euclidean-motion-invariant plane measure, conditioned on meeting the interior of \(K\). Its section has \(N\) sides. Define
\[
\alpha=\arctan\frac1{2\sqrt2},\quad
\beta=\arctan\frac{\sqrt2}{5},\quad
\gamma=\arctan\frac1{\sqrt2}=\alpha+\beta,\quad
\delta=\arctan\frac1{\sqrt{11}}.
\]
Then \(N\) takes exactly the seven values \(3,4,5,6,7,8,9\), each with positive probability. Put \(Z=\pi\sqrt3/6\). Their **exact probabilities** are \(\Pr(N=k)=J_k/Z\), with
\[
\begin{aligned}
J_3&=\frac{\pi\sqrt3}{6}-\sqrt2\,\gamma,\\
J_4&=\frac{\pi\sqrt3}{6}-\frac\pi4,\\
J_5&=\pi\left(\frac12-\frac{\sqrt3}{3}\right)+\sqrt2\,\beta,\\
J_6&=-\frac\pi2+\sqrt2\,\gamma+\sqrt{11}\,\delta,\\
J_7&=\pi\left(\frac12-\frac{\sqrt3}{6}\right)+\sqrt2\,\alpha-\sqrt{11}\,\delta,\\
J_8&=\pi\left(\frac{\sqrt3}{3}-\frac14\right)+\sqrt2(\alpha-\beta)-\sqrt{11}\,\delta,\\
J_9&=\sqrt{11}\,\delta-2\sqrt2\,\alpha.
\end{aligned}
\]
The seven probabilities, in increasing order of side count, are approximately
\[
(0.040224879851,\ 0.133974596216,\ 0.161886425233,\ 0.298680246895,\ 0.191034375739,\ 0.163122546722,\ 0.011076929345).
\]
In particular, the quadrilateral probability simplifies to
\[
\boxed{\Pr(N=4)=1-\sqrt3/2},
\]
and the **exact mean** is
\[
\boxed{\mathbb E N=6}.
\]

## Assumptions and scope

Represent an oriented plane by \(\{x:u\cdot x=t\}\) with \(u\in S^2\). The invariant plane measure is a constant multiple of \(d\omega(u)\,dt\). After conditioning on intersection, \(-h_K(u)<t<h_K(u)\); the two orientations \((u,t)\) and \((-u,-t)\) represent the same plane, a factor that cancels from all ratios. In particular, one must **not** sample a uniform normal followed by a conditionally uniform offset without weighting the normal by \(2h_K(u)\). All assertions about section side counts exclude the measure-zero planes meeting a vertex or containing an edge. No generic plane tangent to the boundary contributes probability.

The displayed coordinates are a similarity-normalized model; the distribution is unchanged under uniform rescaling or rigid motion. It need not be unchanged under a general affine deformation, because Euclidean plane measure is not affine invariant.

## Proof

**1. Polytope and edge certificates.** The vertices are precisely the six \(\pm2e_i\) and the eight \((\pm1,\pm1,\pm1)\). Each of the twelve active planes \(\pm x_i\pm x_j=2\), with independently chosen signs, supports a rhombus whose corners are an axis vertex pair and two cube-shell vertices. This proves completeness of the vertex list and gives twenty-four edges, each of length \(\sqrt3\). The outward unit normals of neighboring facets have inner product \(1/2\), hence the exterior dihedral angle is \(\pi/3\). A generic section vertex corresponds bijectively to an edge with endpoint heights strictly straddling \(t\).

**2. Exact normal decomposition.** Signed coordinate permutations reduce the sphere to forty-eight congruent chambers with ordered unit-normal coordinates \(a>b>c>0\). Write \(u=(1,p,q)/\sqrt{1+p^2+q^2}\), where \(0<q<p<1\). The fundamental triangle in the \((p,q)\)-chart has corners \(A=(0,0), F=(1,0), H=(1,1)\). Two lines split it into three spherical triangles:
\[
\begin{array}{c|c|c}
T_0&A,F,E&a>b+c\\
T_1&F,G,E&a<b+c,\ a+b>3c\\
T_2&G,H,E&a+b<3c
\end{array}
\quad E=(1/2,1/2),\quad G=(1,2/3).
\]
Within each triangle, let \(L_k(u)\) denote the total length in offsets \(t\) for which the section has exactly \(k\) sides. A coefficient triple \((r,s,v)\) in the following table denotes \(L_k(u)=ra+sb+vc\); a dash denotes zero.

| Zone | \(k=3\) | \(k=4\) | \(k=5\) | \(k=6\) | \(k=7\) | \(k=8\) | \(k=9\) |
|---|---|---|---|---|---|---|---|
| \(T_0\) | — | \((2,-2,-2)\) | \((0,0,4)\) | \((0,4,-4)\) | \((0,0,4)\) | \((2,-2,-2)\) | — |
| \(T_1\) | \((-2,2,2)\) | — | \((4,-4,0)\) | \((0,4,-4)\) | \((2,-2,2)\) | \((-2,2,2)\) | — |
| \(T_2\) | \((-2,2,2)\) | — | \((4,-4,0)\) | \((-2,2,2)\) | \((4,0,-4)\) | \((0,4,-4)\) | \((-2,-2,6)\) |

To verify this table without assuming a picture: sort the fourteen linear vertex-height forms \(u\cdot v\). For each interval between successive heights, count edges whose endpoint heights straddle the interval midpoint, and add the difference of the two bounding height vectors to the corresponding \(L_k\). A complete rational subdivision resolving all height orderings uses the seven chart triangles
\[
(A,B,C),\ (B,D,C),\ (D,E,C),\ (B,F,D),\ (F,E,D),\ (F,G,E),\ (G,H,E),
\]
where \(B=(1/3,0), C=(1/4,1/4), D=(2/5,1/5)\). The first five triangles lie in \(T_0\) and give **identical** offset-length coefficients despite different individual vertex-height orderings; the last two are \(T_1,T_2\). Every pairwise height difference has a constant sign on the interior of each of these seven triangles (a rational linear-inequality check), so the enumeration is exhaustive. The supplied standalone checker reconstructs all facets and edges, tests every pair of height forms with rational arithmetic on all seven triangles, and verifies the resulting table.

**3. Exact spherical integration.** For a counterclockwise spherical geodesic triangle \(T\) with nonzero corner vectors \(w_1,w_2,w_3\), put \(w_4=w_1\). Its vector first moment is
\[
M(T)=\int_T u\,d\omega(u)
=\frac12\sum_{j=1}^3
\arccos\left(\frac{w_j\cdot w_{j+1}}{\|w_j\|\,\|w_{j+1}\|}\right)
\frac{w_j\times w_{j+1}}{\|w_j\times w_{j+1}\|}.
\]
Indeed, the spherical Laplacian of any linear coordinate function is minus twice that function; the spherical divergence theorem reduces its area integral to the three constant inward conormals of the great-circle edges, giving this formula. In the chart above take the homogeneous corner representatives
\[
A=(1,0,0),\ F=(1,1,0),\ E=(2,1,1),\ G=(3,3,2),\ H=(1,1,1).
\]
For convenience put \(\eta=\arctan(\sqrt2/3)\) and \(\zeta=\arctan(\sqrt2/8)\). Direct cross products give
\[
\begin{aligned}
2M(T_0)&=\tfrac\pi4(0,0,1)+\tfrac\pi{6\sqrt3}(1,-1,-1)+\tfrac\gamma{\sqrt2}(0,1,-1),\\
2M(T_1)&=\tfrac\eta{\sqrt2}(1,-1,0)+\tfrac\delta{\sqrt{11}}(1,1,-3)+\tfrac\pi{6\sqrt3}(-1,1,1),\\
2M(T_2)&=\tfrac\zeta{\sqrt2}(1,-1,0)+\tfrac\alpha{\sqrt2}(0,1,-1)+\tfrac\delta{\sqrt{11}}(-1,-1,3).
\end{aligned}
\]
The elementary tangent addition identities are \(\eta+\zeta=\gamma=\alpha+\beta\). Taking the dot products of these moments with the coefficient triples in the table, then adding across the three triangles, yields precisely the seven unnormalized masses \(J_3,\ldots,J_9\) displayed above.

**4. Crofton normalization and mean.** All twenty-four equal edges have exterior dihedral angle \(\pi/3\). The polyhedral mean-width identity therefore gives
\[
\overline w(K)=\frac1{4\pi}\sum_{e}|e|(\pi-\text{interior dihedral angle at }e)
=\frac{24\sqrt3\,(\pi/3)}{4\pi}=2\sqrt3.
\]
Thus the full-sphere plane measure of sections meeting \(K\) is \(4\pi\overline w(K)=8\pi\sqrt3\); the contribution from one of the forty-eight normal chambers is \(Z=\pi\sqrt3/6\). This proves \(\Pr(N=k)=J_k/Z\) and \(\sum_{k=3}^9J_k=Z\). Moreover, summing across the edges before integrating yields
\[
\int_{S^2}\int_{-h_K(u)}^{h_K(u)}N(u,t)\,dt\,d\omega(u)
=\sum_{e}\int_{S^2}|u\cdot e|\,d\omega(u)
=2\pi\sum_{e}|e|=48\pi\sqrt3.
\]
Dividing by \(8\pi\sqrt3\) proves \(\mathbb EN=6\). Every displayed \(J_k\) is positive, as also follows from positive offset intervals on the triangle interiors listed above.

## Verification

Run `python3 check.py` in a directory containing the supplied standalone checker. It requires only the Python standard library and reconstructs fourteen vertices, twelve facets, and twenty-four edges from the defining inequalities. Seven exact rational normal triangles and all vertex-height comparisons certify the classification table; floating-point evaluation checks the explicit spherical-moment reductions and probability identities; an independent weighted random-plane experiment checks all seven atoms. The actual run returned `RATIONAL_CHAMBERS_OK`, `EXACT_FORMULAS_OK`, and `WEIGHTED_RANDOM_PLANES_OK`. Rational checks establish finite chamber coverage; numerical checks are supplementary to, not substitutes for, the analytic integration and mean-width arguments.

## Relationship to prior work

Socha's 1988 study *Random Plane Section of a Polyhedron* explicitly treats rhombic-dodecahedral section **angles**, using a distribution pooled across section vertices; its full text and Fig. 2 do not state the joint edge-crossing or per-plane seven-atom side-count law. Koca, Koca and Koc (2014) describe a rhombic dodecahedron as a fourteen-vertex cube–octahedron compound obtained from a projection construction; they do not investigate isotropic affine-plane side counts. Exact Crofton section laws for rectangular boxes and for cuboctahedra concern different polytopes; the polar relationship between the rhombic dodecahedron and cuboctahedron does not identify their affine sections. The present claim is the **evaluated complete seven-atom law**, not the elementary general fact that polytope sections can be counted by crossed edges.

## Limitations

The theorem is specifically the Euclidean-motion-invariant **affine-plane** experiment conditioned on intersection with this regular rhombic dodecahedron. It is not a law for uniform central sections, Haar-only normals with uniform offsets, or arbitrary affine images. It gives neither the full angle/area/perimeter distribution nor joint correlations among these quantities. The absence of a matching formula in the inspected sources does not establish definitive historical priority; older unindexed stereological compilations may require further inspection.

## References

1. P. Socha, *Random Plane Section of a Polyhedron*, Acta Stereologica **7** (1988), 41–46. Full original paper: https://www.ias-iss.org/acta/ActaStereologica_pdf/Vol.1.2.5.7.8/VOL%207/NO%201/AS_7_n1_41_SOC.pdf .
2. M. Koca, N. O. Koca, and R. Koc, *Group Theoretical Analysis of Quasicrystallography from Projections of Higher Dimensional Lattices \(B_n\)*, arXiv:1403.2847 (first posted 12 March 2014), especially Section 3.1 and Figure 3. https://arxiv.org/abs/1403.2847 .
