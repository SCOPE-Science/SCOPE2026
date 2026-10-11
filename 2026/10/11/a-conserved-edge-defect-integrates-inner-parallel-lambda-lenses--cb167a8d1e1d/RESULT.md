# A conserved edge defect integrates inner-parallel \(\lambda\)-lenses in three-dimensional space forms
## Finding
Let \(L_0\subset M^3(c)\) be a \(\lambda_0\)-convex lens in a three-dimensional space form, let \(L_t\) be its inner parallel body for \(0\le t<r(L_0)\), and write \(\lambda_t\) for the curvature of its two totally umbilical facets, \(A_t=|\partial L_t|\), \(\ell_t\) for its unique edge length, and \(\beta_t\) for the angle between the outer normals along that edge. Then
\[
J_t:=\ell_t\tan(\beta_t/2)
\]
is independent of \(t\). Thus the two geometric edge variables enter the whole inner-parallel evolution only through the conserved scalar \(J=J_0\).

If \(\lambda_0^2+c\ne0\), then \(\lambda_t^2+c\ne0\) throughout the interval of definition and
\[
A_t=\frac{4\pi-2J\lambda_t}{\lambda_t^2+c},\qquad
J=\frac{4\pi-(\lambda_0^2+c)A_0}{2\lambda_0}.
\]
Moreover, for \(0\le a<b<r(L_0)\),
\[
|L_a|-|L_b|=F_{c,J}(\lambda_b)-F_{c,J}(\lambda_a),
\]
where
\[
F_{c,J}(\lambda)=4\pi I_c(\lambda)+\frac{J}{\lambda^2+c},\qquad I_c'(\lambda)=\frac1{(\lambda^2+c)^2},
\]
and one may take
\[
I_c(\lambda)=
\begin{cases}
\dfrac{\lambda}{2c(\lambda^2+c)}+\dfrac1{2c^{3/2}}\arctan\!\dfrac{\lambda}{\sqrt c},&c>0,\\[6pt]
-\dfrac1{3\lambda^3},&c=0,\\[6pt]
-\dfrac{\lambda}{2k^2(\lambda^2-k^2)}+\dfrac1{4k^3}\log\!\left|\dfrac{\lambda+k}{\lambda-k}\right|,&c=-k^2<0.
\end{cases}
\]
In the critical hyperbolic case \(c=-k^2<0\), \(\lambda_0=k\), one has \(\lambda_t=k\), \(J=2\pi/k\), and the exact exceptional profile is
\[
A_t=\left(A_0+\frac{2\pi}{k^2}\right)e^{-2kt}-\frac{2\pi}{k^2},
\]
with
\[
|L_0|-|L_t|=\frac{A_0+2\pi/k^2}{2k}(1-e^{-2kt})-\frac{2\pi}{k^2}t.
\]
Hence the inner-parallel area and volume-loss profiles of every three-dimensional \(\lambda\)-lens are explicitly determined by \(c\), \(\lambda_0\), and \(A_0\), including the horospherical critical regime.

## Assumptions and scope
The ambient space \(M^3(c)\) is the simply connected three-dimensional space form of constant sectional curvature \(c\). A \(\lambda\)-lens is the compact intersection of two \(\lambda\)-balls whose boundary has two totally umbilical facets and one edge. The inner parallel body is
\[
L_t=\{x:B(x,t)\subset L_0\}.
\]
The lead source proves that an inner parallel \(\lambda\)-convex polyhedron is \(\lambda_t\)-convex with
\[
\lambda_t'=\lambda_t^2+c,
\]
and supplies both the three-dimensional Gauss--Bonnet identity and the surface-area variation formula. The statement here concerns the lens specialization before extinction, \(0\le t<r(L_0)\). No claim is made about arbitrary \(\lambda\)-convex polyhedra, whose edge set can change and whose vertex terms need not vanish.

## Proof
Put
\[
D_t=\lambda_t^2+c,\qquad J_t=\ell_t	an(eta_t/2).
\]
A lens has two facets, one edge, and no vertices. The Gauss--Bonnet formula of Drach--Solanes--Tatarko therefore becomes
\[
D_t A_t+2\lambda_tJ_t=4\pi. 	ag{1}
\]
Their inner-parallel variation theorem, specialized to dimension three and one edge, gives
\[
A_t'=-2\lambda_tA_t-2J_t, 	ag{2}
\]
while the curvature parameter satisfies
\[
\lambda_t'=D_t. 	ag{3}
\]
Differentiate (1) at every regular time. Since \(D_t'=2\lambda_tD_t\), equations (2)--(3) give
\[
0=D_t'A_t+D_tA_t'+2\lambda_t'J_t+2\lambda_tJ_t'
=2\lambda_tJ_t'.
\]
Because \(\lambda_t>0\), \(J_t'=0\). The geometric data depend continuously on \(t\), so the same constant extends across any exceptional time allowed by the general variation theorem. Hence
\[
J_t\equiv J_0=:J. 	ag{4}
\]

If \(D_0
e0\), uniqueness for the scalar ODE (3) prevents \(D_t\) from crossing zero. Solving (1) for area yields
\[
A_t=rac{4\pi-2J\lambda_t}{D_t},
\]
and setting \(t=0\) yields the displayed formula for \(J\) in terms of \(A_0\) and \(\lambda_0\).

The volume of inner parallel bodies satisfies \(d|L_t|/dt=-A_t\). Therefore, for \(0\le a<b<r(L_0)\),
\[
|L_a|-|L_b|=\int_a^bA_t\,dt
=\int_{\lambda_a}^{\lambda_b}rac{4\pi-2J\lambda}{(\lambda^2+c)^2}\,d\lambda.
\]
Since
\[
rac d{d\lambda}\left(rac J{\lambda^2+c}ight)
=-rac{2J\lambda}{(\lambda^2+c)^2},
\]
the last integral is \(F_{c,J}(\lambda_b)-F_{c,J}(\lambda_a)\). Direct differentiation gives the three displayed elementary choices of \(I_c\).

It remains to handle \(D_0=0\). This can only occur for \(c=-k^2<0\) and \(\lambda_0=k\). Equation (3) then gives \(\lambda_t=k\) identically. Equation (1) gives \(J=2\pi/k\), and (2) becomes
\[
A_t'+2kA_t=-rac{4\pi}k.
\]
Solving this linear equation gives the displayed exponential area profile. Integrating that profile from \(0\) to \(t\) gives the displayed volume loss.

As a Euclidean check, let the lens be the intersection of two radius-\(R\) balls whose centers are distance \(d\) apart. Under erosion the radius is \(R-t\), and elementary cap geometry gives
\[
A_t=4\pi(R-t)\left(R-t-rac d2ight).
\]
Here \(\lambda_t=1/(R-t)\) and the conserved quantity is \(J=\pi d\); substituting these into the general formula reproduces the cap-area expression exactly.

## Verification
The bundled script `artifacts/verify.py` checks with exact rational arithmetic that differentiating the noncritical area formula along \(\lambda'=\lambda^2+c\) reproduces the surface-area ODE and preserves Gauss--Bonnet. It also checks the Euclidean lens specialization numerically at multiple nondegenerate parameter values, differentiates each elementary antiderivative numerically against \((\lambda^2+c)^{-2}\), and checks the critical hyperbolic area and volume-loss ODEs. The universal proof is the algebra above; the script is a consistency check rather than a substitute for it.

## Relationship to prior work
Drach, Solanes, and Tatarko prove the sharp reverse isoperimetric inequality in three-dimensional space forms. Their Theorem 3.1 supplies the \(\lambda\)-polyhedral Gauss--Bonnet identity, Section 4 gives \(\lambda_t'=\lambda_t^2+c\), Theorem 4.2 gives the inner-parallel surface-area variation, and their proof of the main theorem uses those ingredients to compare a general body with a lens at times when their surface areas agree. The checked full text does not state conservation of \(\ell_t	an(eta_t/2)\), the resulting exact all-time lens area law, the volume state function, or the separate horospherical critical profile.

The earlier Euclidean work of Drach and Tatarko derives the first surface-area variation and Gauss--Bonnet edge contribution used in the Euclidean reverse-isoperimetric argument. Its checked Section 3.1 computes the local derivative and then propagates a comparison; it does not state the conserved edge product or the constant-curvature profiles above. Thus the present result is not the reverse-isoperimetric inequality itself, but an exact first integral and closed evolution law for its canonical extremal family.

## Limitations
The finding is specific to three-dimensional lenses. For general \(\lambda\)-convex polyhedra, vertex normal-cone terms and multiple changing edges prevent the same one-scalar reduction. The originality comparison covered the lead paper, its Euclidean precursor, direct semantic searches for the conserved edge product and inner-parallel profile, and the closest indexed geometric records; an unindexed classical formulation of the same lens first integral remains a residual risk. No claim of a new reverse-isoperimetric inequality is made.

## References
1. K. Drach, G. Solanes, K. Tatarko, *A reverse isoperimetric inequality in three-dimensional space forms*, arXiv:2603.08132v1 (2026), especially Theorems 3.1, 4.1, 4.2 and Section 5.
2. K. Drach, K. Tatarko, *Reverse isoperimetric problems under curvature constraints*, arXiv:2303.02294v1 (2023), especially Section 3.1.
