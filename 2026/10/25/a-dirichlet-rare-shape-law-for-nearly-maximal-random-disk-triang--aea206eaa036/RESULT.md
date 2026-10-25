# A Dirichlet rare-shape law for nearly maximal random disk triangles

## Finding

Three independently sampled points inside a disk can form a triangle almost as large as the largest inscribed triangle. The complete leading rare-event law depends only on a boundary radial exponent and a threefold correlation of the angular sampling density. More strongly, after suitable rescaling, the joint geometry of the rare triangle has a Dirichlet limit.

Let \(X_j=R_j(\cos\Theta_j,\sin\Theta_j)\) for \(j=1,2,3\), with i.i.d. pairs \((R_j,\Theta_j)\). The radius and angle are independent within each pair. Suppose \(0\le R_j\le1\), each \(\Theta_j\) has a strictly positive continuous density \(p\) on \([0,2\pi)\) normalized to one, and \(T_j=1-R_j\) has a density satisfying \(g(t)=a t^{b-1}(1+o(1))\) as \(t\downarrow0\), where \(a>0\) and \(b>0\).

Put
\[
M=\frac{3\sqrt3}{4},\quad c=\frac{\sqrt3}{2},\quad
W(\phi)=p(\phi)p(\phi+2\pi/3)p(\phi+4\pi/3),\quad
I_p=\int_0^{2\pi}W(\phi)\,d\phi.
\]
If \(A\) is the unsigned Euclidean area of the triangle, the sharp upper tail is
\[
\boxed{\Pr(A>M-\varepsilon)\sim
\frac{16\pi}{3}\,I_p\,a^3 c^{-3b}
\frac{\Gamma(b)^3}{\Gamma(3b+2)}\varepsilon^{3b+1}.}
\]

The upper-tail event has a fuller shape description. Orient the labeled triangle by \(\sigma\in\{-1,+1\}\), with positive sign for counterclockwise order \(X_1,X_2,X_3\). On the rare-event neighborhood choose continuous lifts of the polar angles and write
\[
\Theta_2=\Theta_1+\sigma(2\pi/3+x),\qquad
\Theta_3=\Theta_2+\sigma(2\pi/3+y).
\]
Define the positive matrix
\[
B=\frac{\sqrt3}{8}\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad \sqrt{\det B}=\frac38,
\]
and set \(U_j=cT_j/\varepsilon\), \(Z=B^{1/2}(x,y)^\mathsf T/\sqrt\varepsilon\), \(V=\lVert Z\rVert^2\), and \(S=1-U_1-U_2-U_3-V\). Conditional on \(A>M-\varepsilon\),
\[
(U_1,U_2,U_3,V,S)\ \Longrightarrow\
\operatorname{Dirichlet}(b,b,b,1,1).
\]
The angular phase \(\arg Z\) tends to an independent uniform angle. In this joint limit, \(\Theta_1\) has density \(W/I_p\) independently of the five shares and angular phase, and \(\sigma\) is an independent fair sign. At finite positive \(\varepsilon\), the normal-form slack \(S\) can have a vanishingly small negative value, which has no effect on weak convergence.

For three points sampled uniformly by area from the unit disk, \(g(t)=2(1-t)\), so \(a=2\), \(b=1\), and \(p=1/(2\pi)\). The theorem becomes
\[
\boxed{\Pr(A>M-\varepsilon)\sim\frac{32}{27\sqrt3\pi}\varepsilon^4,\qquad
(U_1,U_2,U_3,V,S)\Longrightarrow\operatorname{Dirichlet}(1,1,1,1,1).}
\]
The result concerns a single triangle drawn from three independent points, not an extreme-value law over all triples in a growing sample.

## Assumptions and scope

The only regularity required of \(p\) is strict positivity and continuity. The radial-deficit density need not be smooth and may diverge at zero when \(0<b<1\). The sample size is exactly three and is fixed as \(\varepsilon\downarrow0\). The statistical model is independent radius-angle sampling, not an arbitrary joint law of polar coordinates. The theorem applies to conditional weak convergence for the stated variables, including bounded continuous test functions; it makes no uniform remainder claim over families of varying \(a,b,p\).

## Proof

**Maximizers and localization.** The area is continuous on the compact cube of three closed disks. Holding two distinct vertices fixed, it is affine in the third vertex on either orientation branch, hence a global nondegenerate maximizer has all three vertices on the unit circle. Maximizing the inscribed triangle area by the classical chord/gap inequality (or the elementary stationarity condition that each opposite side is parallel to the circle tangent at the third vertex) shows that the only maximizing triples are the two labeled rotations of an equilateral triangle. Their common area is \(M\). It follows by compactness that every configuration with area deficit tending to zero approaches exactly one of these two families. At a maximizing triple the inward radial derivatives of area are all \(-c\), so within sufficiently small neighborhoods the deficit controls \(\sum_j T_j\) from below. The angular Hessian is positive transverse to the common rotation; consequently the deficit also controls \(x^2+y^2\).

**Exact area and normal form.** In either orientation chart the unsigned area has the exact representation
\[
A=\frac12\left[(1-T_1)(1-T_2)\sin(2\pi/3+x)
+(1-T_2)(1-T_3)\sin(2\pi/3+y)
+(1-T_3)(1-T_1)\sin(2\pi/3-x-y)\right].
\]
Taylor expansion at the maximizing triple gives
\[
M-A=c(T_1+T_2+T_3)+(x,y)B(x,y)^\mathsf T
+O\!\left((\sum T_j)^2+(\sum T_j)(|x|+|y|)+(|x|+|y|)^3\right).
\]
Since \(B\) is positive definite and the only maximizing families were identified above, sufficiently rare events satisfy \(T_j=O(\varepsilon)\) and \(|x|+|y|=O(\sqrt\varepsilon)\). The Taylor remainder is uniformly \(o(\varepsilon)\) throughout these neighborhoods. In particular the rescaled support tends to \(\{u_j\ge0:\sum u_j+\lVert z\rVert^2<1\}\).

**Measure conversion.** In each chart \(d\Theta_1\,d\Theta_2\,d\Theta_3=d\phi\,dx\,dy\) in absolute value. The radial variables contribute
\[
\prod_{j=1}^3 g(T_j)dT_j
\sim a^3\,c^{-3b}\varepsilon^{3b}\prod_{j=1}^3 u_j^{b-1}\,du_j,
\]
and \(dx\,dy=\varepsilon(\det B)^{-1/2}d^2z\). The angular densities converge uniformly on the rescaled neighborhood to \(W(\phi)\) for both orientations. Positivity of \(c\) and \(B\), compact localization, and a local uniform bound on \(g(t)/t^{b-1}\) justify dominated convergence even when \(0<b<1\).

The remaining normalized volume is exactly
\[
\begin{aligned}
J_b&=\int_{u_j\ge0,\;\sum u_j+\lVert z\rVert^2<1}
\prod_{j=1}^3u_j^{b-1}\,d^3u\,d^2z\\
&=\pi\int_{u_j\ge0,\;\sum u_j<1}
\prod_{j=1}^3u_j^{b-1}(1-\sum u_j)\,d^3u
=\pi\frac{\Gamma(b)^3}{\Gamma(3b+2)}.
\end{aligned}
\]
Two orientation charts, \(\sqrt{\det B}=3/8\), and the integral \(I_p\) yield
\[
2I_p\,a^3c^{-3b}(8/3)J_b
=\frac{16\pi I_pa^3\Gamma(b)^3}{3c^{3b}\Gamma(3b+2)}.
\]

**Conditional law.** The limiting density in \((u,z)\) is proportional to \(\prod u_j^{b-1}\) on the above bounded domain. In polar coordinates \(z=\sqrt v(\cos\psi,\sin\psi)\), \(d^2z=\tfrac12\,dv\,d\psi\). Thus the normalized joint density of \((u_1,u_2,u_3,v,1-\sum u_j-v)\) is Dirichlet with parameters \((b,b,b,1,1)\), while \(\psi\) is uniform and independent. The separate factor \(W(\phi)\) and the two identical chart factors establish the claimed orientation law, independence, and fair sign. The disk specialization follows by substitution of \(a=2\), \(b=1\), \(p=1/(2\pi)\).

## Verification

The accompanying `verify.py` requires Python with NumPy. Run `python verify.py` in the extracted directory. It checks the radial first derivatives, the exact positive transverse quadratic form, its determinant, the closed beta-integral coefficient, and a threefold sampling-density correlation. It then independently evaluates finite-deficit triangle areas in importance-sampled neighborhoods, with parameter choices \(b\in\{1/2,1,2\}\) and nonuniform threefold angular density. The resulting coefficients approach the analytic limits, and the conditional share means agree with Dirichlet predictions. These numerical tests are corroborative; the proof above establishes the infinite-limit statements.

## Relationship to prior work

Lao and Mayer (arXiv:0704.1379, 11 April 2007) develop extreme-value theory and compute a sharp near-maximal **perimeter** coefficient for triangles sampled on a circle (section 6). Koroleva and Nikitin (arXiv:1301.1360, 7 January 2013, Theorem B and Lemma B) establish the near-maximal **area** coefficient \(4/(3\pi)\) for three points sampled on the circumference. Those angular boundary results are prerequisites and are not presented here as new. Nikitin and Simarova (arXiv:2010.04460, section 3) generalize extreme-value theorems for kernels on the circle and allow nonuniform angular sampling; their underlying sample space remains a circle, rather than the two-dimensional disk with a variable radial boundary exponent. The classical disk-triangle-picking literature supplies area expectations but not the present full conditional high-area shape limit. This theorem gives an explicit radial-angular convolution with a sharp exponent, a five-component conditional Dirichlet law, and a direction-density tilt. Standard normal-form and beta-integral methods underlie the proof; only the fully specified combined result is asserted.

## Limitations

The claim is an asymptotic statement for a fixed three-point model. No rate of weak convergence, complete finite-threshold area density, or growing-sample Poisson law is established. The circular-boundary law is a separate singular sampling model and is not covered by setting \(b=0\). Independently verified historical priority remains open; broad generic Laplace principles may provide alternative derivations, and a search cannot exclude unindexed equivalent results. Computational checks are finite and do not establish any infinite assertion.

## References

- W. Lao and M. Mayer, *U-max-Statistics*, arXiv:0704.1379v1, first posted 11 April 2007, https://arxiv.org/abs/0704.1379.
- E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1, posted 7 January 2013, https://arxiv.org/abs/1301.1360.
- Ya. Yu. Nikitin and E. N. Simarova, *Generalized Limit Theorems For U-max Statistics*, arXiv:2010.04460v1, posted 9 October 2020, https://arxiv.org/abs/2010.04460.
- E. W. Weisstein, *Disk Triangle Picking*, MathWorld, https://mathworld.wolfram.com/DiskTrianglePicking.html (background expectation, not an upper-tail result).
