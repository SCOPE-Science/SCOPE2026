# The simplicial-section phase boundary of a cube and its exact spherical probability

## Finding

Fix an integer \(d\ge3\), the Euclidean cube \(Q_d=[-1,1]^d\), and an interior point \(z\in(-1,1)^d\). Choose an unoriented hyperplane \(H_U=\{x:\langle U,x-z\rangle=0\}\), where \(U\) is uniform on \(\mathbb S^{d-1}\). Let \(p_d(z)\) denote the probability that \(Q_d\cap H_U\) is a \((d-1)\)-simplex.

**Exact phase boundary.** The set of centers admitting simplex sections with positive spherical probability is exactly
\[
 \{z\in(-1,1)^d:p_d(z)>0\}=\{z:\|z\|_1>d-2\}.
\]
Thus the interior crosspolytope \(\|z\|_1\le d-2\) is precisely the zero-probability region, including its boundary.

**Full probability at arbitrary interior points.** For each \(\sigma\in\{-1,1\}^d\), put
\[
 c_i(\sigma,z)=1-\sigma_i z_i,\qquad h_\sigma=1-\tfrac12\sum_{i=1}^d c_i(\sigma,z).
\]
All \(c_i\) are positive. If \(G_1,\ldots,G_d\) are independent standard normals and \(\mathcal Q(c)=\Pr\big\{G_i>\tfrac12\sum_jc_jG_j\text{ for every }i\big\}\), then
\[
 \boxed{p_d(z)=2\sum_{\sigma:h_\sigma>0}\mathcal Q(c(\sigma,z)).}
\]
Each term is strictly positive exactly when \(h_\sigma>0\). More explicitly, writing \(s_{d-1}=2\pi^{d/2}/\Gamma(d/2)\) and \(\Delta_{d-1}=\{x_i\ge0,\sum_i x_i=1\}\), with its ordinary \((d-1)\)-simplex parameterization \((x_1,\ldots,x_{d-1})\),
\[
 \boxed{p_d(z)=\frac2{s_{d-1}}\sum_{\sigma:h_\sigma>0}\frac{h_\sigma^{d-1}}{\prod_i c_i(\sigma,z)}\int_{\Delta_{d-1}}\left\|\tfrac12\mathbf1+h_\sigma\big(x_i/c_i(\sigma,z)\big)_{i=1}^d\right\|^{-d}\,dx_1\cdots dx_{d-1}.}
\]
This formula is a finite sum of ordinary integrals on explicitly defined compact simplices; no distributional or combinatorial ambiguity remains.

**Critical diagonal behavior.** At \(z=t\mathbf1\), \(0\le t<1\), the function \(p_d(t\mathbf1)\) vanishes for \(t\le1-2/d\), increases strictly thereafter, and tends to \(2^{1-d}\) as \(t\uparrow1\). At the threshold,
\[
 \boxed{p_d(t\mathbf1)\sim\frac{\Gamma(d/2)d^{3d/2-1}}{2^{d-1}\pi^{d/2}(d-1)!}\left(t-1+\frac2d\right)^{d-1}}
\]
from above. The onset has exact integer order \(d-1\) in every dimension.

For \(d=3\), the entire diagonal profile is elementary: for \(1/3<t<1\), define \(\lambda=(1-t)/2\), \(\delta=1-3\lambda\), \(\rho^2=3\lambda^2+2\lambda\delta+\delta^2\), and \(q=3\lambda^2+2\lambda\delta\). Then
\[
 \boxed{p_3(t,t,t)=\frac1\pi\arctan\left(\frac{\delta^2}{\rho(\rho^2+3q)}\right).}
\]
For \(0\le t\le1/3\), the probability is zero, while the limit as \(t\uparrow1\) is \(1/4\).

## Assumptions and scope

The hyperplane passes through the fixed **interior** reference point, its normal is Haar-uniform on the unit sphere, and the hyperplane is unoriented. The dimension is an integer \(d\ge3\). A simplex section means a full \((d-1)\)-simplex, equivalently a generic section having exactly \(d\) vertices. Sampling directions that pass through cube vertices has probability zero and does not affect any formula. All integrals use Euclidean coordinates, and all probabilities normalize the full sphere to mass one. The profile claim uses only the main diagonal within the cube, not arbitrary rays.

## Proof

### 1. A nontrivial vertex partition crosses too many cube edges

Let \(V=\{-1,1\}^d\) be the cube vertices and join pairs differing in one coordinate. If a vertex subset \(S\) contains \(m\) vertices, let \(e(S)\) be the number of graph edges internal to it. The standard cube edge-isoperimetric inequality
\[
 e(S)\le\tfrac m2\log_2m
\]
can be proved inductively: split \(S\) into the two coordinate halfcubes of sizes \(a\ge b\), bound cross edges by \(b\), and apply induction to each half. The remaining inequality is \(H_2(b/(a+b))\ge 2b/(a+b)\), where \(H_2\) is binary entropy; it follows from concavity on \([0,1/2]\) and equality at the interval endpoints. Consequently, the number of edges from \(S\) to its complement obeys
\[
 |\partial S|=dm-2e(S)\ge m(d-\log_2m).
\]
If both \(S\) and \(V\setminus S\) have at least two vertices, complement if necessary to have \(2\le m\le2^{d-1}\). The function \(m(d-\log_2m)\) is concave, so on this interval its minimum is at an endpoint and is at least \(2(d-1)\). Indeed the two endpoint values are \(2(d-1)\) and \(2^{d-1}\), and \(2^{d-1}\ge2(d-1)\) for \(d\ge3\). Thus \(|\partial S|>d\).

For a generic hyperplane through the interior of the cube, split cube vertices by the signs of their oriented heights. Exactly the cube edges between the two nonempty sign classes meet the hyperplane, and those intersections are exactly the vertices of the hyperplane section. By the preceding strict bound, the section has precisely \(d\) vertices if and only if one of the sign classes consists of one cube vertex. Conversely, isolating a cube vertex crosses exactly its \(d\) incident edges and produces a simplex. This proves the combinatorial reduction in all dimensions.

### 2. Cone associated with an isolated vertex

Fix a cube vertex \(\sigma\in\{-1,1\}^d\). For an oriented normal \(u\), put \(a_i=\sigma_i u_i\) and \(c_i=1-\sigma_i z_i\). The height of \(\sigma\) is \(H=\sum_i c_i a_i\), while each of its \(d\) adjacent vertices has height \(H-2a_i\). The vertex \(\sigma\) is the only positive vertex precisely when
\[
 a_i>H/2\quad(i=1,\ldots,d).
\]
These inequalities automatically imply \(H>0\), when \(\sum_i c_i<2\): summing after multiplication by \(c_i>0\) gives \(H>(\sum_i c_i)H/2\), and because \(1-\sum_i c_i/2>0\), one gets \(H>0\). Alternatively, with \(H=1\), write \(a_i=1/2+b_i\), where \(b_i>0\) and \(\sum_i c_i b_i=h_\sigma\). Such a solution exists exactly when \(h_\sigma>0\). If \(h_\sigma\le0\), no isolated-positive cone can have positive angle, because the strict inequalities give \(H>\tfrac12H\sum_i c_i\) and \(H>0\) for any genuine isolating orientation. (A direct reason for \(H>0\) is the positive sign of the isolated vertex.)

Since \(h_\sigma=(\langle\sigma,z\rangle-(d-2))/2\), a positive-angle isolated-vertex cone exists for some \(\sigma\) precisely when \(\max_\sigma\langle\sigma,z\rangle=\|z\|_1>d-2\). This proves the exact phase boundary. At equality the candidate cones become degenerate and have spherical measure zero.

### 3. Exact spherical probability

The positive cone for \(\sigma\) consists of the vectors \(a\) satisfying \(a_i>\frac12\sum_jc_ja_j\). Because multiplying coordinates by signs leaves the standard Gaussian law invariant, its spherical fraction equals \(\mathcal Q(c)\) as stated. The oriented normal \(-u\) represents the same unoriented section and swaps the unique positive and unique negative vertex. For \(d\ge3\), a section with \(d\) vertices cannot isolate a vertex on *both* sides, as the cube has \(2^d>2\) vertices. These disjoint events therefore account for the probability with the factor \(2\).

For the integral formula, intersect the cone with the affine hyperplane \(H=1\). The cross-section consists exactly of
\[
 a_i=\tfrac12+\frac{h_\sigma}{c_i}x_i,\qquad x_i\ge0,\quad\sum_ix_i=1.
\]
The Euclidean \((d-1)\)-dimensional area Jacobian of this simplex parameterization is \(h_\sigma^{d-1}\|c\|/\prod_i c_i\). The area element under radial projection to the sphere is its affine area element divided by \(\|c\|\|a\|^d\). Indeed the affine section has unit-normal \(c/\|c\|\) and distance \(1/\|c\|\) from the origin, so the general radial Jacobian is \(\operatorname{dist}(0,H)/\|a\|^d\). Dividing by the full sphere area \(s_{d-1}\) and summing the disjoint cones proves the compact-simplex integral formula.

### 4. Diagonal phase law and critical exponent

For \(z=t\mathbf1\) with \(t\ge0\), a sign vector with any negative coordinate has scalar product at most \((d-2)t<d-2\), since \(t<1\). Hence only \(\sigma=\mathbf1\) is possible. Set \(\lambda=(1-t)/2\), \(\delta=1-d\lambda\). The preceding integral simplifies exactly to
\[
 p_d(t\mathbf1)=\frac{2\delta^{d-1}}{s_{d-1}}\int_{\Delta_{d-1}}\|\lambda\mathbf1+\delta x\|^{-d}\,dx,\qquad\delta>0.
\]
For \(t\le1-2/d\), the phase result makes it zero. As \(t\) increases above that threshold, \(\lambda\) decreases. The isolated-vertex cone is defined by \(a_i>\lambda\sum_j a_j\); any such vector has all positive components, and the inequalities become strictly weaker when \(\lambda\) decreases. The cones increase strictly in spherical measure. Their limit as \(t\uparrow1\) is the full positive orthant, of spherical fraction \(2^{-d}\); the unoriented section probability tends to \(2^{1-d}\).

As \(t\downarrow1-2/d\), one has \(\lambda\to1/d\), \(\delta=\frac d2(t-1+2/d)\to0\). The integrand tends uniformly on the compact simplex to \(d^{d/2}\), and the coordinate volume of \(\Delta_{d-1}\) is \(1/(d-1)!\). Substituting \(2/s_{d-1}=\Gamma(d/2)/\pi^{d/2}\) gives the precise claimed coefficient and power \(d-1\). This is an analytic limit, not an inference from finite tests.

### 5. Dimension three

When \(d=3\), the positive cone is generated by \(r_i=\lambda\mathbf1+\delta e_i\), since positive scalar multiplication does not change the angular cone. Their common length is \(\rho\), pairwise inner product is \(q\), and determinant equals \(\delta^2(3\lambda+\delta)=\delta^2\). The classical solid-angle formula for three linearly independent rays \(r_1,r_2,r_3\) is
\[
 \Omega=2\arctan\frac{|\det(r_1,r_2,r_3)|}{\|r_1\|\|r_2\|\|r_3\|+\sum_{i<j}\langle r_i,r_j\rangle\|r_k\|},
\]
where \(k\) is the remaining index. Therefore \(p_3=2\Omega/(4\pi)\), which yields exactly the displayed arctangent expression. Its critical coefficient is \(3^{7/2}/(16\pi)\), consistently with the all-dimensional asymptotic.

## Verification

`verify.py` performs independent finite exact-rational crossing-edge and isolated-vertex-cone comparisons in dimensions \(3,4,5,6\) (2,764 nondegenerate test instances with fixed-seed rational inputs). It also compares the three-dimensional solid-angle formula against an independent numerical integration over the standard triangle at six different diagonal shifts. Three decreasing critical-window gaps illustrate convergence to the analytically proved coefficient. Run `python verify.py` with Python 3 and SciPy installed. Each successful assertion is printed or covered by the final `all checks passed` line. This verifier does not prove the unrestricted theorem and requires the analytic arguments given above.

## Relationship to prior work

Schange (2026) develops solid-angle formulas for simplicial cones and shifted random sections of **acute orthocentric simplices and crosspolytopes**; his Theorem 1.1 gives an extensive general cone-angle framework. The present finding instead identifies the global *simplicial combinatorial type* for off-center sections of a cube, its sharp reference-point phase boundary and critical exponent, and a dimension-three elementary law. Cone/orthant methods are prior mathematics, not claimed novel. König (2020) studies extremal noncentral **section volumes and perimeters** of the cube, rather than the Haar probability of the simplicial section type. Kabluchko and Seidel's central-cube section formulas concern the center reference point and do not imply the off-center transition. Established cube edge isoperimetry and the trihedral solid-angle formula are used openly. Related work on central orthotope section polygon counts likewise does not give the sharp off-center reference-point threshold.

## Limitations

The probability formulas require a uniformly oriented hyperplane through an interior point of the Euclidean cube. They do not claim analogous phase boundaries for arbitrary parallelotopes with Euclidean-uniform directions, for boundary points, for nonuniform orientation distributions, or for section types other than simplices. The full arbitrary-point formula uses finite Gaussian probabilities or simplex integrals rather than a universal elementary closed form. The historical novelty assessment is limited by searchable literature and has not undergone independent review.

## References

1. Philipp Schange, *Solid-Angle Formulas for Simplicial Cones and Random Shifted Sections of Polytopes*, arXiv:2610.28084v1, first posted 20 October 2026; https://arxiv.org/html/2610.28084v1, especially Theorem 1.1 and Section 4.
2. Hermann König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743, first posted 25 February 2020; https://arxiv.org/pdf/2002.10743, especially introduction and results concerning cube section extrema.
3. Kabluchko and Seidel, central random sections of regular polytopes, as identified and contrasted in Schange, loc. cit., Introduction §1.2 (bibliographic details there).
4. Classical cube edge-isoperimetric inequality and the classical spherical trihedral solid-angle identity; their needed special forms are derived or substituted explicitly in the proof.
