# Two-atom phase diagram for planar \(L_p\) Minkowski problems in cones
## Finding
Let \(C=\operatorname{pos}\{v_0,v_1\}\subset\mathbb R^2\) be a pointed cone with unit boundary generators in counterclockwise order, and let \(u_1,u_2\in\Omega_{C^\circ}\) be distinct unit normals. Put \(n_i=-u_i\) and order them so that the oriented angle \(\Delta\in(0,\pi)\) from \(n_1\) to \(n_2\) is positive. Define \(c=\langle n_2,v_0\rangle/\langle n_1,v_0\rangle\) and \(b=\langle n_2,v_1\rangle/\langle n_1,v_1\rangle\); then \(0<c<b\). For positive masses \(m_1,m_2\) and any real \(p\), every planar \(C\)-close solution with \(L_p\) surface area measure \(m_1\delta_{u_1}+m_2\delta_{u_2}\) is a two-facet set \(A=C\cap\{\langle n_1,x\rangle\ge a_1,\ \langle n_2,x\rangle\ge a_2\}\). Writing \(r=a_2/a_1\in(c,b)\) and \(\rho=m_2/m_1\), its shape is determined by the scalar equation \(\rho=\Phi_p(r)=r^{1-p}(r-c)/(c(b-r))\), while for \(p\ne2\) the scale is \(a_1=(m_1\sin\Delta/(b-r))^{1/(2-p)}\) and \(a_2=ra_1\). Define \(p_*=2\sqrt b/(\sqrt b-\sqrt c)\). If \(p\le p_*\) and \(p\ne2\), every positive pair \((m_1,m_2)\) has exactly one solution. If \(p>p_*\), let \(r_-<r_+\) be the two roots in \((c,b)\) of \(r^2-(b+c-(b-c)/(p-1))r+bc=0\), and set \(\rho_{\max}=\Phi_p(r_-)\), \(\rho_{\min}=\Phi_p(r_+)\). There is one solution for \(\rho\notin[\rho_{\min},\rho_{\max}]\), two at either endpoint, and three for \(\rho\in(\rho_{\min},\rho_{\max})\). At the critical homogeneity \(p=2\), a solution exists exactly when \(r=b-m_1\sin\Delta\in(c,b)\) and \(m_2=(r-c)/(c\,r\sin\Delta)\); when this holds, every positive common dilation is again a solution, so there is a one-parameter homothetic family.

This gives a complete two-atom solvability and multiplicity diagram in the planar cone setting. In the range \(0\le p\le1\) covered by the recent general existence-and-continuity theorem, the scalar map is strictly increasing and the formula is a constructive inverse. Beyond that range the same exact reduction identifies the first loss of uniqueness: it occurs only after the geometry-dependent threshold \(p_*\), apart from the scale-critical case \(p=2\).

## Assumptions and scope
Let \(C=\operatorname{pos}\{v_0,v_1\}\subset\mathbb R^2\) be a pointed closed cone with nonempty interior and unit boundary generators \(v_0,v_1\) listed counterclockwise. Let \(u_1,u_2\in\Omega_{C^\circ}\) be distinct unit vectors, put \(n_i=-u_i\), and relabel so that the oriented angle \(\Delta\in(0,\pi)\) from \(n_1\) to \(n_2\) is positive. Because \(u_i\) lie in the interior of the polar cone, \(\langle n_i,v_j\rangle>0\) for \(i=1,2\) and \(j=0,1\).

Define
\[
c=\frac{\langle n_2,v_0\rangle}{\langle n_1,v_0\rangle},\qquad
b=\frac{\langle n_2,v_1\rangle}{\langle n_1,v_1\rangle}.
\]
Writing the cone aperture as \(\gamma\in(0,\pi)\) and the directions of \(n_i\) as \(\phi_i\) with \(\phi_1<\phi_2\), direct expansion gives
\[
b-c=\frac{\sin\gamma\,\sin(\phi_2-\phi_1)}{\cos\phi_1\cos(\gamma-\phi_1)}>0,
\]
so \(0<c<b\).

The statement concerns positive masses \(m_1,m_2\), arbitrary real \(p\), and the standard \(L_p\) surface area measure \(dS_{1,p}=(-h_C)^{1-p}dS_1\). It does not assert higher-dimensional analogues or a multiplicity theorem for measures supported on three or more directions.

## Proof
Any solution whose \(L_p\) surface area measure is supported on exactly \(\{u_1,u_2\}\) has ordinary surface area measure with the same support, because the factor \((-h_C)^{1-p}\) is finite and strictly positive on \(\Omega_{C^\circ}\). On a planar convex boundary the Gauss angle is monotone. Hence the part of the boundary inside \(\operatorname{int}C\) consists of one segment with normal \(u_1\) and one segment with normal \(u_2\); all remaining boundary lies on the two cone rays, whose normals are outside \(\Omega_{C^\circ}\). Therefore every solution has the form
\[
A=C\cap\{x:\langle n_1,x\rangle\ge a_1\}\cap\{x:\langle n_2,x\rangle\ge a_2\}
\]
with \(a_1,a_2>0\).

Set \(r=a_2/a_1\). The two interior facets are both nondegenerate exactly when \(c<r<b\). Let \(L_i\) be the length of the facet with normal \(u_i\). Comparing the value of \(\langle n_2,\cdot\rangle\) along the first supporting line, and the value of \(\langle n_1,\cdot\rangle\) along the second, gives
\[
L_1=\frac{a_1(b-r)}{\sin\Delta},\qquad
L_2=\frac{a_1(r-c)}{c\sin\Delta}.
\]
Since \(h_C(A,u_i)=-a_i\), the two atom masses are
\[
m_1=\frac{a_1^{2-p}(b-r)}{\sin\Delta},\qquad
m_2=\frac{a_1^{2-p}r^{1-p}(r-c)}{c\sin\Delta}.
\]
Taking their ratio yields
\[
\rho:=\frac{m_2}{m_1}=\Phi_p(r):=\frac{r^{1-p}(r-c)}{c(b-r)}.
\]
For \(p\ne2\), the first mass equation then fixes the scale uniquely:
\[
a_1=\left(\frac{m_1\sin\Delta}{b-r}\right)^{1/(2-p)},\qquad a_2=ra_1.
\]
Thus the number of solutions is exactly the number of roots of \(\Phi_p(r)=\rho\) in \((c,b)\), except at \(p=2\), where scale drops out.

The logarithmic derivative is
\[
\frac{\Phi_p'(r)}{\Phi_p(r)}=\frac{1-p}r+\frac1{r-c}+\frac1{b-r}.
\]
For \(p\le1\) this is positive. For \(p>1\), write \(q=p-1\). A critical point occurs exactly when
\[
q=H(r):=\frac{r(b-c)}{(r-c)(b-r)}.
\]
The function \(H\) has its unique minimum at \(r=\sqrt{bc}\), because
\[
\frac{H'(r)}{H(r)}=\frac1r-\frac1{r-c}+\frac1{b-r},
\]
and the critical equation reduces to \(r^2=bc\). The minimum is
\[
H(\sqrt{bc})=\frac{\sqrt b+\sqrt c}{\sqrt b-\sqrt c}.
\]
Consequently \(\Phi_p\) is strictly increasing for
\[
p\le p_*:=1+\frac{\sqrt b+\sqrt c}{\sqrt b-\sqrt c}=\frac{2\sqrt b}{\sqrt b-\sqrt c},
\]
with only a single zero derivative when \(p=p_*\), which does not destroy strict monotonicity. For \(p>p_*\), there are exactly two critical points \(r_-<r_+\), obtained from
\[
r^2-\left(b+c-\frac{b-c}{p-1}\right)r+bc=0.
\]
The derivative is positive, then negative, then positive, so \(r_-\) is a strict local maximum and \(r_+\) a strict local minimum of \(\Phi_p\). Since \(\Phi_p(r)\to0\) as \(r\downarrow c\) and \(\Phi_p(r)\to\infty\) as \(r\uparrow b\), the stated one/two/three-solution trichotomy follows.

At \(p=2\), the mass equations reduce to
\[
m_1=\frac{b-r}{\sin\Delta},\qquad
m_2=\frac{r-c}{c\,r\sin\Delta},
\]
which gives the stated compatibility condition. Neither equation contains \(a_1\), so every \(a_1>0\) gives a homothetic solution and these are all solutions.

## Verification
The accompanying `verify.py` reconstructs the facet lengths from line intersections for several cone geometries, checks the mass formulas for representative values of \(p\), verifies the closed critical-point equation, and exhibits the predicted three-root regime for a sample with \(p>p_*\). These computations are finite consistency checks; the all-parameter statements above follow from the analytic derivation.

A separate boundary check confirms that the two infinite boundary rays of \(A\) have outer normals on \(\partial C^\circ\), hence do not contribute to the measure on \(\Omega_{C^\circ}\).

## Relationship to prior work
Ai, Ye, and Zhu formulate the \(L_p\) Minkowski problem for \(C\)-close sets and prove existence and uniqueness for every nonzero finite Borel measure when \(0\le p\le1\). Their definition is exactly \(dS_{1,p}=(-h_C)^{1-p}dS_1\), but the paper does not provide an explicit inverse for two atomic directions or a multiplicity phase diagram outside that range.

Yang, Ye, and Zhu previously developed the \(L_p\) surface area measure for \(C\)-coconvex sets. For compactly supported data they obtain exact solvability when \(p\ne0,n\) and prove uniqueness for \(0<p<1\); in dimension two the excluded homogeneity is precisely \(p=2\). The present calculation resolves the two-atom planar model completely, including the exact \(p=2\) compatibility curve and the geometry-dependent onset of one-to-three multiplicity for large \(p\).

Khovanskiĭ and Timorin describe planar coconvex polygons by support numbers and show that edge-length/area data are linear/quadratic in those support parameters. That framework is consistent with the facet-length computation here but does not state the \(L_p\) two-atom inversion or the threshold \(p_*\).

Schneider gives a one-point-support example for ordinary surface area measure of pseudo-cones. Two atoms are therefore the first interacting finite-support case; the ratio equation above is the first place where relative facet placement and nonlinear \(L_p\) weighting interact.

## Limitations
The proof is planar and uses the order structure of boundary normals on a convex curve. It does not classify finitely supported problems with three or more interior normals, and it does not imply any general uniqueness or nonuniqueness theorem in higher dimension. The literature comparison found no statement equivalent to the exact two-atom phase diagram, but absence from the searched sources is not a proof that no obscure or unpublished source contains an equivalent calculation.

## References
1. W. Ai, D. Ye, B. Zhu, *The \(L_p\) Minkowski problem for \(C\)-close sets: existence and continuity*, arXiv:2609.23962v1, 21 September 2026.
2. J. Yang, D. Ye, B. Zhu, *On the \(L_p\) Brunn-Minkowski theory and the \(L_p\) Minkowski problem for \(C\)-coconvex sets*, arXiv:2204.00860v1; International Mathematics Research Notices 2023(7), 6252–6290.
3. R. Schneider, *Pseudo-cones*, arXiv:2305.00452v1; Beiträge zur Algebra und Geometrie 65 (2024).
4. A. Khovanskiĭ, V. Timorin, *On the Theory of Coconvex Bodies*, Discrete & Computational Geometry 52 (2014), 806–823, DOI 10.1007/s00454-014-9637-y.
