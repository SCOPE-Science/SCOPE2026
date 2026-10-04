# A generic weak-focus criterion at the nominal center of a three-dimensional scroll flow
## Finding
Consider
\[
\dot x=ay-yz,\qquad
\dot y=-bz+xz,\qquad
\dot z=cx+xy-dz,
\]
with \(b\ne0\) and \(d>0\). The equilibrium
\[
S_3=\left(b,0,\frac{bc}{d}\right)
\]
has characteristic polynomial
\[
(\lambda+d)\left(\lambda^2+\frac{bc(bc-ad)}{d^2}\right).
\]
Thus, when \(K:=bc(bc-ad)>0\), the linearization has one stable eigenvalue and a purely imaginary pair. This does not make \(S_3\) a nonlinear center. Writing
\[
z_0=\frac{bc}{d},\qquad \omega=\frac{\sqrt K}{d},
\]
the first nonzero cubic focal coefficient on the two-dimensional center manifold has sign
\[
\operatorname{sgn}\ell=-\operatorname{sgn}\!\left(abc(b^2-d^2)\right)
\]
whenever \(a\ne0\) and \(b^2\ne d^2\). Consequently, \(S_3\) is locally asymptotically stable if \(abc(b^2-d^2)>0\) and is unstable if \(abc(b^2-d^2)<0\).

At the parameter choice used in the source to display its two-scroll attractor,
\[
(a,b,c,d)=(5,50,-6,13),
\]
one has
\[
\omega=\frac{10\sqrt{1095}}{13},
\qquad
\ell=\frac{51590875683243\sqrt{1095}}{7747903716039146000}>0.
\]
Therefore the source's \(S_3\) is an unstable weak focus on its center manifold, not a center.
## Assumptions and scope
The statement concerns the smooth real three-dimensional vector field above, with \(b\ne0\), \(d>0\), and \(K>0\). Under \(K>0\), both \(b\) and \(c\) are nonzero. The generic classification additionally assumes \(a\ne0\) and \(b^2\ne d^2\). On the exceptional surfaces \(a=0\) or \(b^2=d^2\), the cubic focal coefficient vanishes and higher-order terms are required.

The conclusion is local near \(S_3\). It neither proves nor disproves the existence of the remote chaotic or two-scroll attractors reported numerically in the source.
## Proof
Shift coordinates by
\[
X=x-b,\qquad Y=y,\qquad Z=z-z_0,
\qquad z_0=\frac{bc}{d}.
\]
The vector field becomes
\[
\dot X=\left(a-z_0\right)Y-YZ,
\]
\[
\dot Y=z_0X+XZ,
\]
\[
\dot Z=cX+bY-dZ+XY.
\]
Because
\[
\omega^2=-z_0(a-z_0)=\frac{bc(bc-ad)}{d^2}>0,
\]
the linear part \(A\) has eigenvalues \(-d\) and \(\pm i\omega\). Let \(B\) denote the symmetric quadratic bilinear form determined by
\[
\frac12B(U,U)=(-YZ,XZ,XY).
\]
Choose a center eigenvector \(q\) satisfying \(Aq=i\omega q\) and \(q_3=1\), and an adjoint eigenvector \(p\) satisfying \(A^Tp=-i\omega p\) and \(\langle p,q\rangle=1\). Since the vector field is quadratic, the cubic center-manifold focal coefficient is obtained from the standard normal-form expression
\[
\ell=\frac{1}{2\omega}\operatorname{Re}\left\langle p,
-2B\!\left(q,A^{-1}B(q,\bar q)\right)
+B\!\left(\bar q,(2i\omega I-A)^{-1}B(q,q)\right)
\right\rangle.
\]
Exact simplification gives
\[
\ell=-\frac{d(b^2-d^2)(z_0^2-\omega^2)P}
{2\omega^3z_0^2(b^4+d^2\omega^2)(d^2+\omega^2)(d^2+4\omega^2)},
\]
where
\[
P=b^2d^2z_0^2+6b^2\omega^4+7b^2\omega^2z_0^2
+d^2\omega^4+7\omega^6+6\omega^4z_0^2.
\]
Every term in \(P\) is nonnegative and at least one is positive under the stated hypotheses, so \(P>0\). Moreover,
\[
z_0^2-\omega^2=\frac{abc}{d}.
\]
Substitution yields
\[
\ell=-\frac{abc(b^2-d^2)P}
{2\omega^3z_0^2(b^4+d^2\omega^2)(d^2+\omega^2)(d^2+4\omega^2)}.
\]
The denominator is strictly positive. Therefore the sign of \(\ell\) is exactly the negative of the sign of \(abc(b^2-d^2)\). A nonzero cubic focal coefficient makes the center manifold a weak focus: negative sign gives local attraction and positive sign gives local repulsion. The stable transverse eigenvalue \(-d\) transfers the same local stability classification to the full equilibrium.

For \((a,b,c,d)=(5,50,-6,13)\), direct exact substitution gives
\[
z_0=-\frac{300}{13},\qquad
\omega=\frac{10\sqrt{1095}}{13},
\]
and the normalized coefficient displayed in the Finding is strictly positive.
## Verification
The bundled `verify.py` reconstructs the shifted Jacobian at the source's two-scroll parameters, verifies the exact factorization
\[
\chi(\lambda)=(\lambda+13)\left(\lambda^2+\frac{109500}{169}\right),
\]
computes the cubic focal coefficient directly from the bilinear normal-form formula using exact symbolic arithmetic, and checks that the result is positive. It prints `VERIFY_OK` on success.

The general factorization was independently simplified symbolically before packaging. The verification is algebraic; no finite trajectory simulation is used as proof.
## Relationship to prior work
Liu, Wu, and Fu introduce this vector field, list \(S_3\), derive its characteristic polynomial, and state that \(S_3\) is a center when \(bc(bc-ad)>0\). Their same paper then uses \((5,50,-6,13)\) as a two-scroll example and reports the linear spectrum \(-13,\pm25.4544i\). The source does not perform a center-manifold or focal-value calculation for \(S_3\).

Targeted searches for the exact title, DOI, vector field, the condition \(bc(bc-ad)>0\), and combinations of "center", "weak focus", and "first Lyapunov coefficient" did not locate a published same-system calculation of this nonlinear classification. Broader center-manifold and Hopf-normal-form theory supplies the method, but not the source-specific factorization above.
## Limitations
The result is local and does not classify global basins, scroll geometry, or chaotic attractors. It does not settle the exceptional cases \(a=0\) or \(b^2=d^2\), where the cubic coefficient vanishes. It also does not assert that the source's numerically displayed two-scroll attractor is absent or invalid.
## References
1. M. Liu, Z. Wu, and X. Fu, "Dynamical Analysis of a One- and Two-Scroll Chaotic System," *Mathematics* 10 (2022), 4682. DOI: 10.3390/math10244682.
2. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, 2004; center-manifold and Hopf normal-form coefficient formulas.
