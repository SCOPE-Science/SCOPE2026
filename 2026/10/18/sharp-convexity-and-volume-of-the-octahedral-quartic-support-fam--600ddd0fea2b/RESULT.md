# Sharp convexity and volume of the octahedral quartic support family

## Finding

Let \(u=(u_1,u_2,u_3)\in S^2\), and define the zero-mean, degree-four octahedrally symmetric spherical harmonic
\[
Y(u)=u_1^4+u_2^4+u_3^4-\frac35.
\]
For a real parameter \(\varepsilon\), put \(h_\varepsilon(u)=1+\varepsilon Y(u)\). The function \(h_\varepsilon\) is the support function, restricted to \(S^2\), of a full-dimensional convex body **if and only if**
\[
\boxed{-\frac{10}{39}\le\varepsilon\le\frac5{18}}.
\]
For every strict interior parameter the spherical curvature-radius tensor \(\nabla^2_{S^2}h_\varepsilon+h_\varepsilon I\) is positive definite at every normal. At the positive endpoint it has rank zero at precisely the six coordinate-axis normals, and is positive definite elsewhere. At the negative endpoint it has rank one at precisely the twelve signed face-diagonal normals, and is positive definite elsewhere. All members, including the two endpoints, are centrally symmetric and strictly convex.

Writing \(K_\varepsilon\) for the body with this support function, its volume throughout the exact convexity interval is
\[
\boxed{\operatorname{Vol}_3(K_\varepsilon)=\frac{4\pi}{3}\left(1-\frac{144}{175}\varepsilon^2+\frac{52224}{125125}\varepsilon^3\right).}
\]
The endpoint volume ratios relative to the Euclidean unit ball are respectively \(2654675/2827539\) at \(\varepsilon=-10/39\) and \(229975/243243\) at \(\varepsilon=5/18\).

## Assumptions and scope

The sphere has its standard round metric, \(\nabla^2_{S^2}\) is the covariant Hessian, and \(I\) is the identity on the tangent plane. Support functions are positive homogeneous on \(\mathbb R^3\), so the asserted support property refers to the extension \(H_\varepsilon(x)=\lVert x\rVert_2h_\varepsilon(x/\lVert x\rVert_2)\), with \(H_\varepsilon(0)=0\). The normal vectors in the rank classifications are directed unit vectors: six coordinate-axis normals \(\pm e_i\) and twelve vectors with two nonzero signed coordinates of absolute value \(1/\sqrt2\). The family is fixed by the sign and permutation symmetries of the cube; no other anisotropic modes are included.

## Proof

**1. Curvature quadratic form.** Write \(F(u)=\sum_i u_i^4\). For any orthonormal pair \(u,v\in\mathbb R^3\), the geodesic second derivative of \(F\) on the sphere is
\[
\nabla^2_{S^2}F(u)[v,v]=12\sum_i u_i^2v_i^2-4F(u).
\]
Consequently, if \(Q(u,v)=(\nabla^2_{S^2}Y+YI)(u)[v,v]\), then
\[
Q(u,v)=12\sum_i u_i^2v_i^2-3\sum_i u_i^4-\frac35.
\]
This formula has no unmentioned normalization constants.

**2. Sharp minimum.** Because \(\sum_i u_i^4\le1\) and \(\sum_i u_i^2v_i^2\ge0\),
\[
Q(u,v)\ge-\frac{18}{5}.
\]
Equality holds exactly when \(u\) is a coordinate-axis direction; then every tangent \(v\) gives equality.

**3. Sharp maximum.** Set \(a=u_1^2\), \(b=u_2^2\), \(c=u_3^2\), \(s=ab+bc+ca\), and \(r=abc\). Thus \(a+b+c=1\), \(0\le s\le1/3\), and \(\sum_i u_i^4=1-2s\). The eigenvalues of the diagonal form \(v\mapsto\sum_i u_i^2v_i^2\) restricted to \(u^\perp\) are the two roots of
\[
\lambda^2-2s\lambda+3r=0,
\]
namely \(s\pm\sqrt{s^2-3r}\). Therefore the two eigenvalues of \(\nabla^2_{S^2}Y+YI\) are
\[
Q_\pm=18s-\frac{18}{5}\pm12\sqrt{s^2-3r}.
\]
To show \(Q_+\le39/10\), observe that \(5/8-3s/2>0\). Squaring the equivalent inequality
\[
\sqrt{s^2-3r}\le\frac58-\frac{3s}{2}
\]
reduces the question exactly to the nonnegativity of
\[
P(s,r)=25-120s+80s^2+192r
=5(1-4s)(5-4s)+192r.
\]
For \(s\le1/4\) this is immediate. For \(s\ge1/4\), Schur's degree-three inequality \(1+9r\ge4s\) gives
\[
P(s,r)\ge(4s-1)\left(20s-\frac{11}{3}\right)\ge0.
\]
For completeness, Schur follows by sorting \(a\ge b\ge c\ge0\):
\[
1+9r-4s=\sum_{\mathrm{cyc}}a(a-b)(a-c)\ge0.
\]
Indeed, after ordering \(a\ge b\ge c\), the last cyclic sum equals \((a-b)^2(a+b-c)+c(a-c)(b-c)\), whose two summands are nonnegative.
Equality in \(P\ge0\) forces \(s=1/4\), \(r=0\), hence a permutation of \((a,b,c)=(1/2,1/2,0)\). Here \(\lambda_+=1/2\), with eigenvector \(v\) the complementary face diagonal, and \(Q_+=39/10\). The other eigenvalue is \(-21/10\). The strictness argument above excludes all other maximizers.

**4. Convexity, endpoint rank, and strict convexity.** The one-homogeneous extension \(H_\varepsilon\) has nonnegative Euclidean Hessian away from the origin exactly when \(I+\varepsilon(\nabla^2_{S^2}Y+YI)\) is positive semidefinite at every \(u\). The two attained global eigenvalue extrema therefore give precisely \(-10/39\le\varepsilon\le5/18\). Inside this interval \(h_\varepsilon\) is positive: use \(-4/15\le Y\le2/5\) to obtain the uniform endpoint lower bounds \(35/39\) and \(25/27\). Convexity of the extension across segments through the origin follows from its evenness and positivity. At the positive endpoint exactly the six axes annihilate both tangent eigenvalues; at the negative endpoint exactly the twelve face diagonals annihilate one. Since the support extension is differentiable in every nonzero direction, every supporting face is a singleton and the resulting convex bodies are strictly convex, including at both endpoints. Outside the interval one of the attained tangent second derivatives is negative, precluding a support function.

**5. Exact volume.** Let \(A=\nabla^2_{S^2}Y+YI\). The eigenvalue formula from step 3 yields
\[
\operatorname{tr}A=36s-\frac{36}{5},\qquad
\det A=180s^2-\frac{648}{5}s+\frac{324}{25}+432r.
\]
For the strict interior parameters, the standard support-coordinate volume identity is
\[
\operatorname{Vol}_3(K_\varepsilon)=\frac13\int_{S^2}h_\varepsilon\det(I+\varepsilon A)\,d\sigma.
\]
With \(\mathbb E\) denoting normalized spherical averaging, elementary even-coordinate moments give
\[
\mathbb E Y=\mathbb E\operatorname{tr}A=0,\quad
\mathbb E\det A=-\frac{48}{175},\quad
\mathbb E(Y\operatorname{tr}A)=-\frac{96}{175},\quad
\mathbb E(Y\det A)=\frac{52224}{125125}.
\]
These fractions follow, without numerical integration, from
\[
\mathbb E(a^ib^jc^k)=\frac{(1/2)_i(1/2)_j(1/2)_k}{(3/2)_{i+j+k}}
\]
for nonnegative integers \(i,j,k\). Expanding \((1+\varepsilon Y)(1+\varepsilon\operatorname{tr}A+\varepsilon^2\det A)\) proves the stated cubic volume polynomial. Continuity of volumes in the support functions extends the formula to both semidefinite endpoints. Substitution gives the two stated rational volume ratios.

## Verification

Running `python3 verify_quartic.py` uses only the Python standard library. Its exact rational polynomial/moment evaluator independently recomputes all four spherical moment identities and the endpoint volume ratios; it also checks rational Schur and polynomial identities. Its sampled orthonormal-pair tests check the tensor quadratic form and sharp spectral interval numerically, but these finite checks are **not** the proof of the global inequalities: the algebraic argument in steps 2–3 proves them for all directions.

## Relationship to prior work

The Wulff construction and the general principle that a surface-tension function must have a convex homogeneous extension are classical. Miracle-Sole studies equilibrium shapes and facet formation for lattice interfaces and gives the general Wulff construction, but does not evaluate this octahedrally symmetric quartic family or its two critical amplitudes. Groemer gives general support-function perturbation criteria and discusses spherical-harmonic approximation; applying such a criterion here still requires the sharp two-tangent-vector optimization in step 3. Previously circulated results for degree-three, odd, constant-width support perturbations differ in parity and harmonic degree and do not imply the degree-four, even, cubic-symmetry thresholds, curvature-rank classification, or cubic volume polynomial.

## Limitations

This theorem does not characterize all octahedrally symmetric support functions or arbitrary combinations of spherical-harmonic modes. The endpoint rank statements refer to the curvature-radius tensor in normal coordinates, not finite-area planar facets. A full historical-priority verdict remains provisional: the complete text of a broad older support-perturbation reference was not available for inspection. Independent mathematical validation has not been performed.

## References

1. S. Miracle-Sole, *Facet shapes in a Wulff crystal*, available as arXiv:1206.3736 (first arXiv version 17 June 2012), especially the Wulff construction and the three-dimensional lattice discussion.
2. H. Groemer, *Perturbations and approximations of support functions of convex bodies*, Beiträge zur Algebra und Geometrie 34 (1993), available bibliographic record and abstract.
3. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, Cambridge University Press, 1993; standard support-coordinate volume and curvature identities.
