# Strict translation-fiber Brunn–Minkowski concavity for the critical covariogram transition body

## Finding
Fix a full-dimensional convex body \(K\subset\mathbb R^d\), \(d\ge2\). Define the support function \(h_K\), surface-area measure \(S_K\) on \(\mathbb S^{d-1}\), and for any \(z\in\operatorname{int}K\) put
\[
a_z(u)=h_K(u)-\langle z,u\rangle>0,\qquad
\Phi_z(y)=\int_{\mathbb S^{d-1}}
a_z(u)\log\cosh\!\left(\frac{\langle y,u\rangle}{2a_z(u)}\right)\,dS_K(u).
\]
For any \(\tau>0\), let \(T_z(\tau)=\{y\in\mathbb R^d:\Phi_z(y)\le\tau\}\). Each \(T_z(\tau)\) is a centrally symmetric, full-dimensional convex body, even when \(K\) is not centrally symmetric.

**Theorem (strict translation-fiber concavity).** For any \(z_0,z_1\in\operatorname{int}K\), \(0<t<1\), and \(z_t=(1-t)z_0+tz_1\),
\[
(1-t)T_{z_0}(\tau)+tT_{z_1}(\tau)\subseteq T_{z_t}(\tau).
\tag{1}
\]
If \(z_0\ne z_1\), this yields the *strict* Brunn–Minkowski inequality
\[
\operatorname{vol}_d(T_{z_t}(\tau))^{1/d}>
(1-t)\operatorname{vol}_d(T_{z_0}(\tau))^{1/d}+
t\operatorname{vol}_d(T_{z_1}(\tau))^{1/d}.
\tag{2}
\]
In particular the volume has at most one maximizing origin in the interior of \(K\). If \(K\) is centrally symmetric about \(c\), then \(T_z(\tau)\subseteq T_c(\tau)\) for all interior \(z\), strictly in volume unless \(z=c\). If \(K\) is any \(d\)-simplex, its centroid is the unique volume-maximizing origin for every \(\tau>0\).

There are two quantitative endpoint consequences. With
\[
M_z=\int_{\mathbb S^{d-1}}\frac{uu^\top}{a_z(u)}\,dS_K(u),\qquad
D(z)=(\det M_z)^{-1/(2d)},
\]
the function \(D\) is concave on \(\operatorname{int}K\) and
\[
\lim_{\tau\downarrow0}\frac{\operatorname{vol}_d(T_z(\tau))^{1/d}}{\sqrt{8\tau}}
=\kappa_d^{1/d}D(z),
\tag{3}
\]
where \(\kappa_d\) is the volume of the unit Euclidean ball. If \(K\) is centrally symmetric, \(M_z\succeq M_c\), with \(\det M_z>\det M_c\) when \(z\ne c\).

Let \(\Pi^\circ K=\{y:h_{\Pi K}(y)\le1\}\), with \(h_{\Pi K}(y)=\frac12\int|\langle y,u\rangle|\,dS_K(u)\). Uniformly over interior origins, 
\[
\tau\Pi^\circ K\subseteq T_z(\tau)
\subseteq\bigl(\tau+d\operatorname{vol}_d(K)\log2\bigr)\Pi^\circ K.
\tag{4}
\]
Thus the large-threshold convergence to the polar projection body has a uniform explicit relative error of order \(\tau^{-1}\).

## Assumptions and scope
The surface-area measure \(S_K\) is the standard finite Borel measure of outward unit normals. The theorem requires no differentiability or strict convexity of \(K\); its statements about the integral-defined bodies include polytopes. The connection to the critical *covariogram limit* proved in [1] assumes that \(K-z\) has \(C^3\) boundary, as in that paper; the present theorem does not extend the underlying smooth-covariogram convergence theorem to polytopes. All levels \(\tau\) are fixed positive real numbers. Volumes are ordinary \(d\)-dimensional Lebesgue measures. Strictness means strict inequality for every distinct interior pair and every \(0<t<1\), not just almost every pair.

## Proof
**1. Surface-area identities and proper fibers.** The divergence theorem/Minkowski first integral supplies
\[
\int u\,dS_K(u)=0,\qquad \int h_K(u)\,dS_K(u)=d\operatorname{vol}_d(K).
\tag{5}
\]
Consequently \(\int a_z\,dS_K=d\operatorname{vol}_d(K)\), independent of \(z\). Since \(z\) lies in the interior, \(a_z\) has a positive minimum. The surface-area measure is not supported on any proper great subsphere: otherwise \(K\) would be lower dimensional. Hence \(h_{\Pi K}\) is a genuine norm.

The inequalities \(|r|-\log2\le\log\cosh r\le|r|\) give, for every \(z,y\),
\[
h_{\Pi K}(y)-d\operatorname{vol}_d(K)\log2\le\Phi_z(y)\le h_{\Pi K}(y).
\tag{6}
\]
The integrand is strictly convex in its second argument; therefore \(\Phi_z\) is even and strictly convex in \(y\), and (6) makes it coercive. Thus each \(T_z(\tau)\) is compact, has interior containing zero, is strictly convex as a set, and is centrally symmetric. Formula (6) also proves (4) immediately.

**2. The perspective inequality and Minkowski inclusion.** Let
\[
\psi(a,b)=a\log\cosh\left(\frac{b}{2a}\right),\qquad a>0.
\]
This is the perspective of the strictly convex function \(b\mapsto\log\cosh(b/2)\). For \(0<t<1\), its two-point Jensen inequality is
\[
\psi((1-t)a_0+ta_1,(1-t)b_0+tb_1)
\le(1-t)\psi(a_0,b_0)+t\psi(a_1,b_1),
\tag{7}
\]
with equality precisely when \(b_0/a_0=b_1/a_1\). The general perspective inequality is standard and appears already in [2, Eq. (1.1)]; the translation-fiber application and strict volume consequence are the assertions here. For \(a_j=a_{z_j}(u)\), \(b_j=\langle y_j,u\rangle\), their interpolants are \(a_{z_t}(u)\) and \(\langle(1-t)y_0+ty_1,u\rangle\). Integrating (7) gives
\[
\Phi_{z_t}((1-t)y_0+ty_1)
\le(1-t)\Phi_{z_0}(y_0)+t\Phi_{z_1}(y_1).
\tag{8}
\]
For endpoint points in their sublevel bodies, (8) proves (1). The ordinary Brunn–Minkowski inequality applied to (1) gives the non-strict form of (2).

**3. Rigidity and the strict volume inequality.** Suppose equality holds in the volume-root inequality for some \(0<t<1\). Both the inclusion-volume inequality and the Brunn–Minkowski inequality must be equalities. Equality in Brunn–Minkowski for full-dimensional convex bodies forces the endpoint bodies to be homothetic. Because both are symmetric about the origin, their translation offset vanishes: \(T_{z_1}(\tau)=sT_{z_0}(\tau)\) for some \(s>0\). Equality of volumes in the inclusion of step 2 then gives exactly
\[
T_{z_t}(\tau)=((1-t)+ts)T_{z_0}(\tau).
\tag{9}
\]
Choose \(y\in\partial T_{z_0}(\tau)\) with \(S_K(\{u:\langle y,u\rangle=0\})=0\). Such a boundary vector exists: almost every ray direction has this property by Fubini, and every ray intersects the boundary exactly once. The three boundary values \(y,sy,((1-t)+ts)y\) attain the common sublevel value \(\tau\). In (8) equality must therefore hold in the integrand for \(S_K\)-almost every \(u\). The sharp equality condition of (7), with \(b_1=s b_0\), implies
\[
a_{z_1}(u)=s a_{z_0}(u)\qquad S_K\text{-almost everywhere.}
\tag{10}
\]
Integrate (10) and use (5) to conclude \(s=1\). Since \(a_{z_1}-a_{z_0}=-\langle z_1-z_0,u\rangle\), the same relation implies \(\langle z_1-z_0,u\rangle=0\) \(S_K\)-almost everywhere, contradicting the full-dimensional span of the normal measure unless \(z_1=z_0\). Thus equality is impossible for distinct origins, proving (2).

**4. Symmetry centers.** Suppose \(K\) is symmetric about \(c\). The measure \(S_K\) is even and \(a_c(-u)=a_c(u)\). If \(v=z-c\), the opposite-normal pair of terms in \(\Phi_{c+v}(y)\) has denominators \(a_c(u)\mp\langle v,u\rangle\) and identical absolute numerators. Convexity in the denominator of the perspective yields \(\Phi_c(y)\le\Phi_{c+v}(y)\) pointwise, and hence \(T_{c+v}(\tau)\subseteq T_c(\tau)\). If \(v\ne0\), choose \(y\) parallel to \(v\); positive surface-area mass has \(\langle v,u\rangle\ne0\), so the pairwise Jensen inequality is strict there. Scaling this \(y\) to \(\partial T_{c+v}(\tau)\) shows that the inclusion is proper and the volume inequality strict.

For any affine automorphism \(f(x)=Ax+b\) of \(K\), the normal-area change of variables gives
\[
\Phi_{f(z)}(Ay)=|\det A|\Phi_z(y).
\tag{11}
\]
Since \(f(K)=K\), necessarily \(|\det A|=1\), so \(T_{f(z)}(\tau)=A T_z(\tau)\) and the fiber volumes agree. For a simplex, all vertex permutations are affine automorphisms. The average of the full permutation orbit of an interior \(z\) is precisely the vertex centroid \(c\); by concavity and permutation invariance, \(\operatorname{vol}_d(T_c(\tau))^{1/d}\) is at least the value at \(z\). Strictness in (2), applied along the averaging operation, makes it greater if \(z\ne c\). This proves the simplex classification.

**5. Quadratic and linear limiting geometry.** Since the denominator \(a_z\) is bounded away from zero at fixed \(z\), the uniform fourth-order Taylor remainder of \(\log\cosh r=r^2/2+O(r^4)\) gives
\[
\Phi_z(y)=\frac18 y^\top M_z y+O_z(\|y\|^4).
\tag{12}
\]
The matrix \(M_z\) is positive definite by normal span. Consequently \((8\tau)^{-1/2}T_z(\tau)\) converges in the Hausdorff metric to \(\{y:y^\top M_z y\le1\}\), proving (3). Divide the non-strict Brunn–Minkowski inequality by \(\sqrt{8\tau}\) and let \(\tau\downarrow0\) to deduce that \(D(z)\) is concave. For a symmetric \(K\), pair the terms in \(M_{c+v}\) and use
\[
\frac12\left(\frac1{a-b}+\frac1{a+b}\right)-\frac1a
=\frac{b^2}{a(a^2-b^2)}\ge0,
\tag{13}
\]
where \(a=a_c(u)>|b|=|\langle v,u\rangle|\). Thus \(M_{c+v}-M_c\) is positive semidefinite and nonzero for \(v\ne0\). Positive definiteness then implies \(\det M_{c+v}>\det M_c\). Formula (4) from step 1 gives the large-threshold conclusion, uniformly for all interior origins.

## Verification
The self-contained companion `verify_transition_centers.py` implements polygonal facet-normal surface-area measures, a stable evaluator for \(\log\cosh\), and a numerical radial-area integral. Its tests check the Jensen inequality in two polygons, strict volume-root concavity for representative distinct origins, and the symmetry-center inclusion on sampled rays. Run with `python3 verify_transition_centers.py` (Python standard library only). The analytic argument above proves the universal theorem; finitely many numerical tests neither certify the full-dimensional theorem nor establish historical novelty. All proofs use only formulas (5)–(13), standard Brunn–Minkowski equality, and the classical affine normal-area formula.

## Relationship to prior work
Haddad, Jiménez, and Resende [1, Theorem 5, dated October 8, 2026] derive precisely \(\Phi_z\) at \(\tau=1\) for the critical smooth-covariogram regime of \(K-z\) with \(C^3\) boundary. They give its quadratic and linear \(y\)-asymptotics, but their stated results do not compare different translation points of the *same* body. Lutwak, Yang, and Zhang [2] define general Orlicz projection bodies and explicitly record the convex perspective inequality (1.1); they prove a global Orlicz-Petty inequality over different bodies, not the stated strict volume-root translation-fiber law for fixed \(K\). Zhou, Ye, and Zhang [3] develop higher-order Orlicz bodies, not this fixed-shape center problem. The operator, elementary perspective inequality, and Brunn–Minkowski theorem are prior mathematics; the claimed contribution is their exact strict translation-fiber combination, equality rigidity, center characterizations, and uniform two-regime bounds. Priority is provisional pending wider literature review.

## Limitations
The theorem concerns integral-defined sublevel bodies for interior choices of origin, not the smooth-covariogram limit for nonsmooth \(K\). It does not claim that every nonsymmetric body has an interior maximizer, nor characterize the maximizer for every nonsymmetric body, nor assert strict concavity of the determinant limit \(D(z)\). The numerical verifier is illustrative and not an infinite-dimensional certificate. Earlier results under an alternative formulation of Orlicz-origin optimization remain a residual historical-priority possibility. There has been no independent mathematical audit.

## References
1. J. Haddad, C. H. Jiménez, and M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1 (first publicly posted 2026-10-08), https://arxiv.org/html/2610.11700v1 .
2. E. Lutwak, D. Yang, and G. Zhang, *Orlicz Projection Bodies*, Advances in Mathematics 223 (2010), 220–242, accessible author manuscript https://cims.nyu.edu/~yangd/papers/orlicz_projection_body.pdf .
3. X. Zhou, D. Ye, and Z. Zhang, *The mth Order Orlicz Projection Bodies*, arXiv:2501.07565, https://arxiv.org/pdf/2501.07565 .
4. R. J. Gardner, *Geometric Tomography*, 2nd ed., Cambridge University Press, 2006 (surface-area measures, projection bodies, and Brunn–Minkowski equality theory).
