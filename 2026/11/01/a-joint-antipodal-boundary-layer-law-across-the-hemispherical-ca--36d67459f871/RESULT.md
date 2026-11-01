# A joint antipodal boundary-layer law across the hemispherical cap transition

## Finding

Let \(q\ge 3\) be an integer, let \(\mathbb S^q\subset\mathbb R^{q+1}\) be the unit round sphere, and let
\[
 C_\alpha=\{x\in\mathbb S^q:x_{q+1}\ge\cos\alpha\},\qquad 0<\alpha<\pi.
\]
Choose \(X_\varepsilon,Y_\varepsilon\) independently and uniformly with respect to spherical \(q\)-area on \(C_{\alpha_\varepsilon}\), where \(\alpha_\varepsilon=\pi/2+\lambda\varepsilon\), \(\lambda\in\mathbb R\) is fixed, and \(\varepsilon\downarrow0\). Put \(D_\varepsilon=\arccos(X_\varepsilon\cdot Y_\varepsilon)\). The distance is the ambient round-sphere great-circle distance; for large caps it is not defined as a shortest path restricted to the cap.

Write
\[
 \sigma_j=\frac{2\pi^{(j+1)/2}}{\Gamma((j+1)/2)},\quad
 \kappa_j=\frac{\pi^{j/2}}{\Gamma(j/2+1)},\quad
 A_0=\sigma_q/2,
\]
\[
 J_q(\lambda)=\int_{\|h\|<1}(2\lambda-h_q)_+\,dh
 =\kappa_{q-1}\int_{-1}^{1}(2\lambda-t)_+(1-t^2)^{(q-1)/2}\,dt.
\]
Here \((v)_+=\max(v,0)\). Then the full sharp joint-scale upper-distance law is
\[
 \boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-(q+1)}
 \Pr\{D_\varepsilon>\pi-\varepsilon\}
 =\Psi_q(\lambda):=\frac{\sigma_{q-1}}{A_0^2}J_q(\lambda).}
\]
Convergence of the unconditioned scaled probability is uniform for \(\lambda\) in compact sets. In particular, the event is impossible for all sufficiently small \(\varepsilon\) if \(\lambda\le-1/2\), while \(J_q(\lambda)>0\) for \(\lambda>-1/2\). For \(\lambda\ge1/2\), \(J_q(\lambda)=2\lambda\kappa_q\); at the hemisphere, \(J_q(0)=\kappa_{q-1}/(q+1)\).

The stronger joint-configuration conclusion follows. On the event \(D_\varepsilon>\pi-\varepsilon\), write \(Z_\varepsilon=-Y_\varepsilon\), let \(u\in\mathbb S^{q-1}\) be the normalized equatorial part of \(X_\varepsilon\), and let \(v\in\mathbb S^{q-1}\) be the normalized equatorial part of \(Z_\varepsilon\). For sufficiently small \(\varepsilon\) these are well defined and lie within the injectivity radius of each other. Let \(t,s\) be their signed latitudes, so that
\[
 X_\varepsilon=(\cos t\,u,\sin t),\quad
 Z_\varepsilon=(\cos s\,v,\sin s).
\]
Set
\[
 a=t/\varepsilon,\qquad c=(s-t)/\varepsilon,\qquad
 b=\varepsilon^{-1}\operatorname{Log}_u(v)\in T_u\mathbb S^{q-1}.
\]
For every fixed \(\lambda>-1/2\), the conditional law of \((u,a,b,c)\) given \(D_\varepsilon>\pi-\varepsilon\) converges weakly to normalized product-bundle volume on
\[
 \boxed{\mathcal R_\lambda=\{(u,a,b,c):u\in\mathbb S^{q-1},\ b\in T_u\mathbb S^{q-1},\ -\lambda\le a\le\lambda-c,\ \|b\|^2+c^2<1\}.}
\]
Its density relative to \(d\sigma_{q-1}(u)\,da\,db\,dc\) is exactly \((\sigma_{q-1}J_q(\lambda))^{-1}\) on \(\mathcal R_\lambda\). In particular the conditional rescaled displacement \(h=(b,c)\) has density
\[
 \boxed{f_{q,\lambda}(h)=\frac{(2\lambda-h_q)_+\,\mathbf1_{\{\|h\|<1\}}}{J_q(\lambda)}.}
\]
Thus the joint limiting geometry, and not merely its pair-distance marginal, changes from a truncated displacement ball when \(-1/2<\lambda<1/2\) to the full displacement ball when \(\lambda\ge1/2\).

For the first included dimension \(q=3\) the entire scalar crossover is elementary:
\[
 \boxed{\Psi_3(\lambda)=
 \begin{cases}
 0,&\lambda\le-1/2,\\
 \dfrac{(3-2\lambda)(1+2\lambda)^3}{3\pi^2},&-1/2<\lambda<1/2,\\
 \dfrac{32\lambda}{3\pi^2},&\lambda\ge1/2.
 \end{cases}}
\]
The onset is nonanalytic in general dimension: for \(\eta\downarrow0\),
\[
 J_q(-1/2+\eta)\sim
 \frac{2^{q+1}\pi^{(q-1)/2}}{\Gamma((q+5)/2)}\eta^{(q+3)/2}.
\]

## Assumptions and scope

The theorem holds for each fixed integer \(q\ge3\), each fixed real \(\lambda\), and all sufficiently small positive \(\varepsilon\) for which \(0<\alpha_\varepsilon<\pi\). All areas use unnormalized spherical Hausdorff measure before normalizing the sampling law. Boundary sets have zero measure. The strict threshold \(D_\varepsilon>\pi-\varepsilon\) is essential at \(\lambda=-1/2\). The conditional assertion is made only when \(\lambda>-1/2\), so the conditioning event has positive probability for small \(\varepsilon\).

The tangent vectors \(b\) live in the varying Euclidean spaces \(T_u\mathbb S^{q-1}\). Weak convergence is tested against bounded continuous functions on this tangent bundle together with the real coordinates \(a,c\). There is no global frame assumption.

## Proof

**1. Antipodal reduction and localization.** Set \(Z=-Y\). The exact spherical identity
\[
 d_{\mathbb S^q}(X,Y)=\pi-d_{\mathbb S^q}(X,Z)
\]
turns the event into \(d_{\mathbb S^q}(X,Z)<\varepsilon\). Let \(t,s\) be signed latitudes. Since \(\cos(\pi/2+\lambda\varepsilon)=-\sin(\lambda\varepsilon)\), the two cap conditions are exactly \(t\ge-\lambda\varepsilon\) and \(s\le\lambda\varepsilon\), when latitudes are in \((-\pi/2,\pi/2)\). The latitude function is one-Lipschitz for geodesic distance, so \(|s-t|<\varepsilon\). Therefore
\[
 -\lambda\varepsilon\le t\le(\lambda+1)\varepsilon,
 \qquad (-\lambda-1)\varepsilon\le s\le\lambda\varepsilon.
\]
In particular both are \(O_\lambda(\varepsilon)\). If \(\lambda\le-1/2\), the cap constraints imply \(t-s\ge-2\lambda\varepsilon\ge\varepsilon\), so the strict event is empty. For \(\lambda>-1/2\), the event localizes to an \(O(\varepsilon)\)-neighborhood of the equator, and the equatorial directions \(u,v\) differ by \(O(\varepsilon)\).

**2. Exact coordinate Jacobian.** In normal coordinates around \(u\in\mathbb S^{q-1}\), write \(v=\operatorname{Exp}_u(\varepsilon b)\), \(t=\varepsilon a\), and \(s=\varepsilon(a+c)\). The joint product area element is
\[
 \varepsilon^{q+1}
 [\cos(\varepsilon a)\cos(\varepsilon(a+c))]^{q-1}
 \left(\frac{\sin(\varepsilon\|b\|)}{\varepsilon\|b\|}\right)^{q-2}
 d\sigma_{q-1}(u)\,da\,db\,dc,
\]
where the last factor is interpreted as one at \(b=0\). This is the exact volume element on the chosen normal-coordinate chart; its ratio to \(\varepsilon^{q+1}\) converges uniformly to one on bounded coordinate sets.

**3. Distance and limiting region.** The spherical cosine formula gives exactly
\[
 X\cdot Z=
 \cos(\varepsilon a)\cos(\varepsilon(a+c))\cos(\varepsilon\|b\|)
 +\sin(\varepsilon a)\sin(\varepsilon(a+c)).
\]
Consequently, uniformly over every bounded set of \((a,b,c)\),
\[
 \frac{d_{\mathbb S^q}(X,Z)^2}{\varepsilon^2}
 =\|b\|^2+c^2+O(\varepsilon^2).
\]
The exact cap constraints become \(a\ge-\lambda\) and \(a+c\le\lambda\). On the distance event, \(b,c\) remain uniformly bounded and the allowed \(a\) interval is bounded for fixed \(\lambda\). The boundary of the limit region \(\mathcal R_\lambda\) has product volume zero. The characteristic functions therefore converge almost everywhere, with compact domination. Applying dominated convergence to the Jacobian proves
\[
 \int_{C_{\alpha_\varepsilon}}\int_{-C_{\alpha_\varepsilon}}
 \mathbf1_{\{d(X,Z)<\varepsilon\}}\,d\sigma(Z)\,d\sigma(X)
 =\varepsilon^{q+1}\sigma_{q-1}J_q(\lambda)+o(\varepsilon^{q+1}).
\]
The area of the cap tends to \(A_0=\sigma_q/2\); division by its square proves the probability formula. The preceding estimates are uniform for \(\lambda\) in compact sets, proving compact-uniform convergence. Inserting any bounded continuous test function into the same dominated-convergence argument, then dividing by the positive limiting mass, proves the full conditional configuration law.

**4. Explicit profile and sharp boundaries.** Integrating first over \(a\) gives the factor \((2\lambda-c)_+\), and slicing the unit ball at normal coordinate \(c\) gives the stated one-dimensional integral for \(J_q\). For \(\lambda\ge1/2\), this positive part never vanishes in the unit ball; symmetry yields \(J_q=2\lambda\kappa_q\). For \(\lambda=0\), direct integration gives \(J_q(0)=\kappa_{q-1}/(q+1)\). For \(q=3\), the cross-section factor is \(\pi(1-c^2)\); evaluating its polynomial integral produces the three-branch expression. Finally put \(\lambda=-1/2+\eta\), \(c=-1+s\). The integrand is asymptotic to \((2\eta-s)(2s)^{(q-1)/2}\) for \(0<s<2\eta\). Beta integration yields the announced positive onset constant and exponent. These calculations also show continuity at both branch boundaries.

## Verification

The accompanying standalone `verify.py` is executable with the Python standard library. It checks the unit-ball cross-section normalization for dimensions \(3\) through \(9\), the exact polynomial formula for \(\Psi_3\), and convergence against an independent, finite-\(\varepsilon\) one-dimensional angular integral for two random points in a cap of \(\mathbb S^3\). The exact finite-parameter integral integrates the uniform equatorial cosine in dimension three, then integrates one latitude; it does not use the boundary-layer approximation. Additional tests verify the subhemispherical endpoint constant as a consistency check. All 117 deterministic checks passed in the recorded execution.

These calculations test finite-dimensional identities and convergence numerically. The limit theorem and conditional weak convergence are established by the analytical coordinate/Jacobian argument, not by extrapolation of finite tests. The code contains no external datasets or unstated numerical certificates.

## Relationship to prior work

Cabré, Fosalba, Gaztañaga and Manera (2007), Appendix B1, calculate polar-cap pair-containment probabilities on the ordinary two-dimensional sphere. Their work establishes substantial prior coverage of the scalar angular-separation distribution on \(\mathbb S^2\). That dimension is intentionally excluded from the accepted new result.

Moseeva, Tarasov and Zaporozhets (2020), Corollary 2.2, give an exact distance-density formula for points sampled in a spherical cap of radius strictly below \(\pi/2\) in arbitrary spherical dimension. Their main theorem applies to spherical convex bodies. Consequently the ordinary fixed-cap subhemisphere distance marginal is prior-covered; it is not claimed as new here. By complement decomposition, scalar information for larger caps can also be reconstructed from the known small-cap marginal. The present claim is instead the **joint conditional tangent-bundle configuration limit across the hemisphere** and its normalized simultaneous two-parameter law. A one-dimensional distance distribution does not determine this conditional joint geometric law, and the inspected sources do not state or imply it as a joint configuration statement.

The inspected literature contains no statement of the particular signed-latitude/tangent-displacement joint limit or of the associated complete support transition. Uninspected historical sources remain a priority risk.

## Limitations

The dimension is fixed as \(\varepsilon\to0\); there is no uniform-in-dimension statement. The cap radius is coupled to the deficit on the single scale \(\alpha_\varepsilon-\pi/2=\lambda\varepsilon\); varying \(\lambda\) with \(\varepsilon\) outside compact sets is not covered. The cap is an ordinary round cap and sampling is uniform by spherical area. The result concerns ambient geodesic distance and not cap-constrained paths. The conditional limit is not defined at or below \(\lambda=-1/2\) because the strict event is empty. Historical originality remains uncertain; an independent priority assessment has not been performed.

## References

1. A. Cabré, P. Fosalba, E. Gaztañaga and M. Manera, *Error analysis in cross-correlation of sky maps: application to the Integrated Sachs–Wolfe detection*, Monthly Notices of the Royal Astronomical Society 381 (2007), 1347–1368, Appendix B1, doi:10.1111/j.1365-2966.2007.12280.x. First public date used: 2007-10-17. https://doi.org/10.1111/j.1365-2966.2007.12280.x
2. T. Moseeva, A. Tarasov and D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297v1, first posted 2020-07-14, especially Definition of spherical convex body, Theorem 2.1, Corollary 2.2 and the proof. https://arxiv.org/abs/2007.07297
