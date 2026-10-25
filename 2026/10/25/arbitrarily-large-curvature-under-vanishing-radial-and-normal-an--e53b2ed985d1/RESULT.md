# Arbitrarily large curvature under vanishing radial and normal-angle deviations

## Finding

Fix an integer dimension \(n\geq1\), a radius \(R>0\), and positive sequences \(\varepsilon_j\to0\), \(\theta_j\to0\), and \(L_j\to\infty\). There is a sequence of smooth, embedded radial graphs
\[
X_j(\omega)=\rho_j(\omega)\,\omega,\qquad \omega\in\mathbb S^n,
\]
whose enclosed volumes equal \(\omega_{n+1}R^{n+1}\) exactly and which satisfy
\[
R(1-\varepsilon_j)\leq \rho_j(\omega)\leq R(1+\varepsilon_j),\qquad
\langle\nu_j,\omega\rangle\geq\cos\theta_j,
\]
while \(\|A_j\|_{L^\infty}\geq L_j\). The frequencies may also be chosen so that \([\nu_j]_{C^\alpha}\to\infty\) for every fixed \(\alpha\in(0,1]\). Hence these two first-order geometric closeness conditions imply no uniform curvature bound or positive-Hölder control of the normal.

## Assumptions and scope

The ambient space is Euclidean \(\mathbb R^{n+1}\). The radial function is measured against the unit round metric on \(\mathbb S^n\), \(\omega_{n+1}\) denotes the volume of the unit ball in \(\mathbb R^{n+1}\), \(\nu_j\) is the outward unit normal, and \(A_j\) is the second fundamental form. For \(0<\alpha\leq1\), the seminorm \([\nu_j]_{C^\alpha}\) uses the ambient Euclidean distance between points on the hypersurface; equivalent chart-based norms give the same divergence. The assertion concerns the initial hypersurface class only; it does not assert a curvature blow-up along the subsequent flow.

## Proof

Choose a fixed coordinate chart on \(\mathbb S^n\), and a smooth cutoff \(\chi\) supported in that chart and equal to one on a smaller chart. In local coordinates set
\[
u_j(\omega)=a_j\chi(\omega)\sin(k_jx_1),\qquad a_j=\eta_j/k_j,
\]
where \(\eta_j>0\) is chosen sufficiently small compared with \(\theta_j\), with \(\eta_j\to0\). The integer frequencies \(k_j\) are chosen sufficiently large at each index. Uniform coordinate estimates give
\[
\|u_j\|_\infty\leq C\eta_j/k_j,\quad
\|\nabla u_j\|_\infty\leq C\eta_j,\quad
\|\nabla^2u_j\|_\infty\geq c\eta_j k_j
\]
for constants \(C,c>0\) independent of \(j\). The lower bound follows by evaluating at points in the region where \(\chi=1\) and the oscillatory second derivative has maximal magnitude.

First form the radial graph with radius \(R(1+u_j)\). Rescale it by
\[
c_j=\left(\frac1{|\mathbb S^n|}\int_{\mathbb S^n}(1+u_j)^{n+1}\,d\omega\right)^{-1/(n+1)},\qquad
\rho_j=Rc_j(1+u_j).
\]
The polar-coordinate volume formula \(\operatorname{Vol}(\Omega_j)=\frac1{n+1}\int_{\mathbb S^n}\rho_j^{n+1}\,d\omega\) shows exactly that \(\operatorname{Vol}(\Omega_j)=\omega_{n+1}R^{n+1}\). Since \(\|u_j\|_\infty\to0\), one has \(c_j=1+O(\eta_j/k_j)\). Taking \(k_j\) large enough therefore enforces the prescribed annular bound.

For a radial graph, the radial component of the unit normal is
\[
\langle\nu_j,\omega\rangle=\left(1+\frac{|\nabla\rho_j|^2}{\rho_j^2}\right)^{-1/2}.
\]
Thus \(\|\nabla\rho_j\|_\infty/\inf\rho_j\leq C\eta_j\), and choosing \(\eta_j\) small enough gives the required normal-angle bound. In local coordinates the second fundamental form has a leading Hessian term proportional to \(-\rho_j\nabla^2\rho_j/\sqrt{\rho_j^2+|\nabla\rho_j|^2}\); the remaining terms are bounded by constants depending on \(R\) plus terms of order \(\eta_j^2\). Consequently \(\|A_j\|_\infty\geq c_R\eta_j k_j-C_R\). Choose \(k_j\) so this is at least \(L_j\).

Finally, two points in the region \(\chi=1\), separated by distance comparable to \(k_j^{-1}\), can be chosen so that the tangential components of their normals differ by at least \(c\eta_j\). Therefore, for each fixed \(0<\alpha\leq1\),
\[
[\nu_j]_{C^\alpha}\geq c_\alpha\eta_j k_j^\alpha.
\]
At index \(j\), increase \(k_j\) further so that \(\eta_j k_j^{1/m}\geq j\) for every integer \(1\leq m\leq j\), as well as all preceding bounds. For any fixed \(\alpha>0\), choose \(m\) with \(1/m\leq\alpha\); for all sufficiently large \(j\), the last inequality implies \(\eta_jk_j^\alpha\geq j\). Hence every fixed positive-Hölder seminorm diverges. Increasing the frequency only improves the annular bound and leaves the gradient bound controlled by \(\eta_j\). This proves the claim.

## Verification

The volume identity is exact by the displayed normalization. The radial-angle identity follows by differentiating \(X_j(\omega)=\rho_j(\omega)\omega\) and normalizing the normal vector. The curvature lower bound follows from the oscillatory Hessian term, whose size is \(\eta_jk_j\), while the first derivatives remain of size \(O(\eta_j)\). The construction is analytic at the level of estimates and requires no numerical extrapolation. It proves only noncompactness of the initial geometric class; it does not claim a flow singularity or a new flow-existence theorem.

## Relationship to prior work

The recent paper *Geometric \(C^1\)-stability of geodesic spheres under volume-preserving mean curvature flow* motivates separating first-order closeness from higher-order control. The present statement is a static, volume-normalized construction: it gives arbitrary prescribed curvature lower bounds and divergence of every fixed positive-Hölder normal seminorm while the annular and normal-angle bounds tend to zero. A direct arXiv HTML retrieval was unavailable during this check, so no uninspected details of the paper's proof are used as proof of this construction. Searches of the indexed research records found no exact equivalent formulation; the general oscillatory mechanism itself is standard, and the contribution is its quantified geometric normalization and simultaneous rate statement.

## Limitations

This is a noncompactness construction, not a result about the evolution of these graphs. The constants in the local coordinate estimates depend on the fixed dimension, chart, cutoff, and radius, but not on frequency. No claim is made that the constructed graphs have constant mean curvature, convexity, or any second-order curvature pinching. The construction only establishes that the stated first-order closeness conditions alone cannot yield curvature or Hölder-normal bounds.

## References

1. *Geometric \(C^1\)-stability of geodesic spheres under volume-preserving mean curvature flow*, arXiv:2610.20265, version 1, first publicly available 14 October 2026. The article is used as motivation for the first-order geometric regime, not as a source for the oscillatory construction.
2. Z. Huang and L. Lin, *Stability of the surface area preserving mean curvature flow in Euclidean space*, arXiv:1211.0764 (2012), for earlier flow-stability context. Its hypotheses and flow are different from the static construction proved here.
