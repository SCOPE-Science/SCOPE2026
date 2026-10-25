# Exact sectoral-mode threshold for constant-width convex bodies

## Finding

For every odd integer \(m\ge3\), define the smooth function on the unit sphere
\[
 h_\varepsilon(\theta,\phi)=1+\varepsilon\sin^m\!\theta\cos(m\phi).
\]
It is the support function of a convex body of constant width \(2\) exactly when
\[
 |\varepsilon|\le\frac{1}{m^2-1}.
\]
For strict inequality the principal-radius tensor is positive definite. At the positive endpoint, its zero-radius directions occur exactly at the equatorial normals \((\theta,\phi)=(\pi/2,2\pi j/m)\), for \(j=0,\ldots,m-1\); at the negative endpoint they occur exactly at \((\pi/2,(2j+1)\pi/m)\). The endpoint volume is
\[
 V_m=\frac{4\pi}{3}-\frac{\pi 2^{2m}(m!)^2(m+2)}{(2m+1)!(m-1)(m+1)^2},
\]
so the volume deficit from the unit ball is asymptotic to \(\pi^{3/2}/(2m^{5/2})\).

## Assumptions and scope

The sphere \(S^2\) is the unit sphere in Euclidean \(\mathbb R^3\); \(\theta\in[0,\pi]\) is colatitude and \(\phi\in[0,2\pi)\) is longitude. The integer \(m\) is odd and at least three. The support function is normalized so that the unperturbed unit ball has support function \(1\), hence width \(2\). The claim concerns only this one-parameter sectoral harmonic family; it does not identify a global minimum-volume body among all bodies of constant width.

## Proof

Put \(f(\theta,\phi)=\sin^m\!\theta\cos(m\phi)\). It is the restriction of the homogeneous harmonic polynomial \(\operatorname{Re}(x+iy)^m\), so \(\Delta_{S^2}f=-m(m+1)f\). Since \(m\) is odd, \(f(-u)=-f(u)\), and therefore \(h_\varepsilon(u)+h_\varepsilon(-u)=2\).

For a twice continuously differentiable function \(h\) on \(S^2\), the support-function criterion is that its principal-radius tensor \(R_h=\nabla^2_{S^2}h+hI\) be positive semidefinite. Write \(A=\nabla^2_{S^2}f+fI\), so \(R_h=I+\varepsilon A\). In the orthonormal meridional/azimuthal frame, set \(s=\sin\theta\), \(c=\cos\theta\), \(u=c^2\), \(x=\cos(m\phi)\), and \(y=\sin(m\phi)\). Direct differentiation gives
\[
 A=(m-1)s^{m-2}B,\qquad
 B=\begin{pmatrix}
 ((m+1)u-1)x&-mc y\\
 -mc y&-(m+1-u)x
 \end{pmatrix}.
\]

We prove \(-(m+1)I\preceq B\preceq(m+1)I\). For the lower bound, the diagonal entries of \(B+(m+1)I\) are nonnegative: the first is at least \(1\), because \(|(m+1)u-1|\le m\); the second is at least \(u\), because \(x\le1\). With \(t=1-u\in[0,1]\), its determinant is
\[
 2m+1+m^2t-(m+1)(m+2)tx+(m+1)t^2x^2.
\]
Its derivative with respect to \(x\) is \((m+1)t[-(m+2)+2tx]\le0\), so its minimum over \(-1\le x\le1\) occurs at \(x=1\). There it equals
\[
 (1-t)\bigl(2m+1-(m+1)t\bigr)\ge0.
\]
Thus \(B+(m+1)I\) is positive semidefinite. Replacing \(\phi\) by \(\phi+\pi/m\) changes \(B\) to \(-B\), proving the upper bound as well. Consequently
\[
 -(m^2-1)I\preceq A\preceq(m^2-1)I,
\]
because \(0\le s^{m-2}\le1\). Hence \(R_h\) is positive definite if \(|\varepsilon|<(m^2-1)^{-1}\) and positive semidefinite at equality. Also \(h_\varepsilon\ge1-(m^2-1)^{-1}>0\), so the support body is full-dimensional.

Necessity and the endpoint locus are exact. At \(\theta=\pi/2\) and \(x=1\), the eigenvalues of \(A\) are \(-(m-1)\) and \(-(m^2-1)\); therefore any \(\varepsilon>(m^2-1)^{-1}\) makes \(R_h\) indefinite. The antipodal longitude shift gives the analogous obstruction for \(\varepsilon<-(m^2-1)^{-1}\). Equality in the lower spectral bound can occur only when \(s=1\) and \(x=1\); these are precisely the \(m\) normals listed for the positive endpoint. For the negative endpoint, use \(x=-1\).

For the volume, the support-function formula is
\[
 V(h)=\frac13\int_{S^2}h\det(\nabla^2h+hI)\,d\omega.
\]
Expanding at \(h=1+\varepsilon f\), the linear term vanishes since \(\int f\,d\omega=0\). The cubic term \(\int f\det A\,d\omega\) vanishes by antipodal parity: \(f\) changes sign and \(A\) changes sign, while \(\det A\) does not. The integrated Bochner identity on the unit sphere gives
\[
 \int_{S^2}\det A\,d\omega=-\frac12\int_{S^2}|\nabla f|^2\,d\omega+\int_{S^2}f^2\,d\omega.
\]
Using \(\operatorname{tr}A=\Delta f+2f\) and integration by parts yields the exact identity
\[
 V(h_\varepsilon)=\frac{4\pi}{3}-\frac{m(m+1)-2}{2}\varepsilon^2 I_m,
 \qquad I_m=\int_{S^2}f^2\,d\omega.
\]
The elementary beta-integral gives
\[
 I_m=\pi\int_0^\pi\sin^{2m+1}\!\theta\,d\theta
 =\frac{\pi 2^{2m+1}(m!)^2}{(2m+1)!}.
\]
Substituting \(|\varepsilon|=(m^2-1)^{-1}\) gives the stated endpoint volume. Finally, the gamma-ratio asymptotic \(I_m\sim\pi^{3/2}m^{-1/2}\) and the prefactor \((m+2)/(2(m-1)(m+1)^2)\sim(2m^2)^{-1}\) give the claimed deficit asymptotic.

## Verification

The curvature matrix was differentiated explicitly in the spherical orthonormal frame. The determinant reduction is exact and its lower bound factors into two nonnegative factors on \(t\in[0,1]\). The equatorial eigenvalues prove sharpness, not merely sufficiency. The volume calculation is exact; no finite numerical experiment is used as an infinite-dimensional proof.

## Relationship to prior work

Horváth's survey records the support/width relation and the open three-dimensional minimum-volume problem for bodies of constant width. Support-function methods express convexity through the curvature-radius tensor, while spherical-harmonic expansions provide natural finite-mode families. The present statement supplies an explicit all-odd-degree sectoral family, its sharp admissible amplitude, its exact endpoint degeneracy set, and its exact volume deficit. It is a benchmark family only, not a solution of the global minimum-volume problem.

## Limitations

The theorem covers only the sectoral mode \(\sin^m\!\theta\cos(m\phi)\). It does not compare all spherical-harmonic modes, prove global optimality, or establish a minimizer for the full class of constant-width bodies. Novelty is provisional pending independent literature review; a specialized result on this exact family could have escaped the searches.

## References

1. Á. G. Horváth, “On Convex Bodies that are Characterizable by Volume Function,” first posted 8 August 2019 as arXiv:1908.03196; journal version in *Arnold Mathematical Journal* **6** (2020), 1–20, DOI: \(10.1007/s40598-020-00132-0\). Public full text: https://arxiv.org/abs/1908.03196 and https://link.springer.com/article/10.1007/s40598-020-00132-0.
2. P. R. S. Antunes and B. Bogosel, “Parametric Shape Optimization using the Support Function,” arXiv:1809.00254 (2018). Public full text: https://arxiv.org/abs/1809.00254.
