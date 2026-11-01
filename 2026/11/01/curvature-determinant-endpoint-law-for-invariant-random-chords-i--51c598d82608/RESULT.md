# Curvature-determinant endpoint law for invariant random chords in smooth convex bodies

## Finding

Let \(d\ge3\), \(q=d-1\), and let \(K\subset\mathbb R^d\) be a full-dimensional compact strictly convex body with \(C^3\) boundary. Write \(D=\operatorname{diam}(K)\) and \(S(K)=\mathcal H^{d-1}(\partial K)\). Suppose there are finitely many unordered pairs \(\{p_{j,-},p_{j,+}\}\) attaining \(\|p_{j,+}-p_{j,-}\|=D\), and that the principal curvatures at their endpoints are strictly positive. Identify the common tangent hyperplanes at each pair by parallel translation, and let \(R_{j,-},R_{j,+}\) be the positive-definite \(q\times q\) matrices of curvature radii (inverses of the shape operators with outward normals). Assume the **nondegenerate diameter condition**

\[
G_j=D I_q-R_{j,-}-R_{j,+}\succ0\quad\text{for every }j.
\]

Sample an unoriented affine line from Euclidean-motion-invariant measure conditioned on meeting \(K\), and let \(L\) be its chord length. Then

\[
\boxed{\Pr\{L>D-\varepsilon\}=C_K\varepsilon^{d-1}+o(\varepsilon^{d-1})},\qquad\varepsilon\downarrow0,
\]

where, writing \(\kappa_m=\pi^{m/2}/\Gamma(1+m/2)\) for the volume of the unit \(m\)-ball,

\[
\boxed{C_K=\frac{2^{q+1}\kappa_{2q}}{\kappa_q S(K)D^{q/2}}
\sum_j\sqrt{\frac{\det R_{j,-}\det R_{j,+}}{\det(D I_q-R_{j,-}-R_{j,+})}}}.
\]

The principal-radius operators need not commute. The all-dimensional coefficient depends only on the surface area, diameter, and curvature tensors at the finitely many diametral endpoint pairs, not on any other local boundary jets. For \(d=3\), the probability exponent is exactly two and the prefactor simplifies to \(4\pi/[S(K)D]\) times the sum of the determinant ratios. The planar counterpart is not claimed as novel because terminal densities for planar chord distributions are part of earlier literature.

## Assumptions and scope

The invariant line measure uses spherical surface measure for unoriented directions and Lebesgue measure on each perpendicular offset space. Its total mass on lines meeting \(K\) equals \(\kappa_q S(K)/2\). The finite diametral-pair hypothesis excludes spheres and other bodies with continua of maximizing chords. The strict matrix inequality excludes degenerate maxima, even when the maximizing diameter is unique. A chord means the full segment \(K\cap\ell\). No claim is made for other chord sampling conventions, nonconvex solids, singular curvature, or degenerate diameter sets. If the hypotheses hold at finitely many pairs, those pairs contribute additively.

## Proof

**1. Localization.** A diameter of a smooth convex body must join points with opposing outward normals parallel to the joining segment, because first variations of its Euclidean length along either boundary vanish. In adapted orthonormal coordinates near any diameter, take the axis along the segment, the endpoints at \((\mp D/2,0)\), and common tangent variables \(z\in\mathbb R^q\). Positive curvatures and \(C^3\) regularity give graph expansions

\[
x_-(z)=-D/2+\tfrac12z^{\mathsf T}B_-z+O(\|z\|^3),\qquad
x_+(z)=D/2-\tfrac12z^{\mathsf T}B_+z+O(\|z\|^3),
\]

with \(B_\pm=R_\pm^{-1}\). Parameterize nearby lines by \(\ell_{v,y}=\{(x,y+vx):x\in\mathbb R\}\), where \(v,y\in\mathbb R^q\). The endpoints of the chord then have transverse coordinates

\[
z_-=y-Dv/2+O(\|(y,v)\|^2),\qquad
z_+=y+Dv/2+O(\|(y,v)\|^2).
\]

The Euclidean chord length is \(\sqrt{1+\|v\|^2}\) times the difference of endpoint axial coordinates. Consequently

\[
D-L(\ell_{v,y})=Q(v,y)+O(\|(v,y)\|^3),
\]

\[
Q(v,y)=\tfrac12\bigl[(y-Dv/2)^{\mathsf T}B_-(y-Dv/2)
+(y+Dv/2)^{\mathsf T}B_+(y+Dv/2)-D\|v\|^2\bigr].
\]

This expansion holds uniformly in a sufficiently small fixed neighborhood. The set of lines meeting the compact body is compact in unoriented line coordinates. Therefore any sequence of chords with lengths tending to \(D\) must approach one of the finitely many maximizing diameter lines, so the local models exhaust the upper tail.

**2. Nondegeneracy and determinant.** Set \(z_-=y-Dv/2\), \(z_+=y+Dv/2\). In these variables,

\[
Q=\tfrac12\begin{pmatrix}z_-\\z_+\end{pmatrix}^{\mathsf T}
\begin{pmatrix}B_--D^{-1}I_q&D^{-1}I_q\\D^{-1}I_q&B_+-D^{-1}I_q\end{pmatrix}
\begin{pmatrix}z_-\\z_+\end{pmatrix}.
\]

The matrix determinant lemma or the Schur complement of the positive diagonal block \(\operatorname{diag}(B_-,B_+)\) shows that this quadratic form is positive definite exactly when \(G=D I_q-R_--R_+\succ0\). Let \(M\) be the symmetric \(2q\times2q\) matrix satisfying \(Q=(y,v)^{\mathsf T}M(y,v)\). The change of variables \((y,v)\mapsto(z_-,z_+)\) has determinant \(D^q\), and the same determinant lemma gives

\[
\det M=4^{-q}D^q\det(B_-)\det(B_+)\det(DI_q-R_--R_+).
\]

No simultaneous diagonalization of the two shape operators is required. In particular,

\[
(\det M)^{-1/2}=\frac{2^q}{D^{q/2}}
\sqrt{\frac{\det R_-\det R_+}{\det G}}.
\]

**3. Invariant measure and sublevel volume.** The unoriented direction near the diameter is represented by \(u=(1,v)/\sqrt{1+\|v\|^2}\). The spherical direction measure and the perpendicular offset measure together have density

\[
d\mu=(1+\|v\|^2)^{-(d+1)/2}\,d^qv\,d^qy
=\bigl(1+O(\|v\|^2)\bigr)d^qv\,d^qy.
\]

The \(2q\)-dimensional ellipsoidal sublevel set \(\{Q<\varepsilon\}\) has volume \(\kappa_{2q}\varepsilon^q/\sqrt{\det M}\). Taylor remainder control and rescaling \((v,y)=\sqrt\varepsilon\,(V,Y)\), followed by dominated convergence on a fixed compact neighborhood, imply that the true upper-tail line measure has the same leading term. The finite neighborhoods are disjoint and their masses add. Finally Cauchy's projection formula yields

\[
\mu\{\ell:\ell\cap K\ne\varnothing\}
=\int_{\mathbb{RP}^{d-1}}\!\operatorname{vol}_q(\operatorname{proj}_{u^\perp}K)\,d\sigma(u)
=\frac{\kappa_q}{2}S(K).
\]

Dividing the local masses by this normalizer gives the stated coefficient and exponent. This completes the proof.

## Verification

`verify.py` implements two independent checks of the critical computations. It first checks the Hessian determinant identity with exact SymPy rational arithmetic for tangent dimensions one, two, and three, including noncommuting pairs of positive-definite matrices. It then evaluates, by numerical Gaussian-Legendre angular integration, the exact upper-tail invariant-line mass of planar ellipses and three-dimensional ellipsoids with simple largest semiaxis. The resulting \(\varepsilon^{-q}\)-rescaled masses converge numerically to the curvature formula. Run `python verify.py` with Python, NumPy, SciPy, and SymPy installed. Numerical tests confirm examples, not the infinite-domain theorem, which follows from the proof above.

For an ellipsoid with semiaxes \(a>b_2,\ldots,b_d>0\), the two endpoint radius matrices are equal to \(\operatorname{diag}(b_i^2/a)\), and \(D=2a\). The displayed formula therefore specializes to its familiar separated-axis endpoint exponent \(d-1\), providing an independent normalization check. This special case is not claimed as new.

## Relationship to prior work

The invariant-line chord distribution and its normalization are classical in integral geometry; see Vlasov (2010), whose full publicly accessible article was inspected in its chord-method and normalization sections. Gates (1987) specifically discusses terminal densities for **planar** chord distributions; the planar \(d=2\) specialization is therefore excluded from the claimed new contribution. Ren (2014) provides general containment-function formulas for distributions of random chords. The full text of this potentially relevant paper could not be accessed, so the precise extent to which it evaluates curvature-dependent endpoint coefficients remains a historical-priority risk. The present result is a closed curvature-tensor asymptotic for all \(d\ge3\), including arbitrary noncoaxial endpoint shapes; a general unevaluated CDF representation does not by itself state its determinant coefficient.

The 2023 work of van der Jagt, Jongbloed, and Vittorietti proves absolute continuity and gives density-approximation methods for randomly oriented hyperplane sections. In dimension \(d\ge3\), these codimension-one sections are not the random **lines** here. Previously established exact ellipsoid chord laws cover the special ellipsoidal case, not the universal curvature-matrix statement for general bodies. The precise formula and its historical priority have not undergone independent review.

## Limitations

The asymptotic does not control the remainder at a universal rate for all \(C^3\) bodies. Degenerate diameter pairs may have a different exponent; if infinitely many diameter pairs exist, the localization sum is invalid. The global surface area \(S(K)\) remains in the conditioning normalizer. Computational checks cover selected matrices and ellipsoids only. The full text of Gates (1987) and Ren (2014) was not accessed; their exact comparison remains a material bibliographic uncertainty, especially for possible previously derived endpoint asymptotics. There is no claim of independent certification.

## References

1. A. Yu. Vlasov, *Extension of Dirac's chord method to the case of a nonconvex set by use of quasi-probability distributions*, arXiv:1012.4411 (first publicly dated 2010-12-20), https://arxiv.org/abs/1012.4411.
2. J. Gates, *Some properties of chord length distributions*, Journal of Applied Probability 24 (1987), 863–874, https://doi.org/10.2307/3214211.
3. D. Ren, *Random chord distributions and containment functions*, Advances in Applied Mathematics 58 (2014), 1–20, https://doi.org/10.1016/j.aam.2014.05.003.
4. T. van der Jagt, G. Jongbloed, M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, Image Analysis and Stereology 42 (2023), 171–184, https://doi.org/10.5566/ias.2923.
