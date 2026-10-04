# Exact parameterized von Neumann–Jordan profile of the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For \(0\le\lambda\le1\), define
\[
C'_{\mathrm{NJ}}(\lambda,X_8)=\sup_{x,y\in S_{X_8}}\left(N(\lambda x+(1-\lambda)y)^2+\lambda(1-\lambda)N(x-y)^2\right).
\]
Put \(m=\min\{\lambda,1-\lambda\}\) and \(m_*=(4-\sqrt2)/7\). Then
\[
C'_{\mathrm{NJ}}(\lambda,X_8)=
\begin{cases}
1+(4-2\sqrt2)m-2m^2,&0\le m\le m_*,\\
1+4(\sqrt2-1)^2m(1-m),&m_*\le m\le1/2.
\end{cases}
\]
The first branch is attained by a pair of octagon vertices separated by three edges and the second by adjacent vertices. Hence the maximizer changes type at \(m_*\). At \(\lambda=1/2\), the formula gives \(C'_{\mathrm{NJ}}(1/2,X_8)=4-2\sqrt2\), recovering the classical modified von Neumann–Jordan value for the regular octagonal plane.

## Assumptions and scope
The scalar field is real. The formula concerns the unit-sphere parameterized constant introduced in arXiv:2110.15741, not the unrestricted \(C_\alpha\) constant and not the two-parameter \(L'_{YJ}\) constant. The displayed norm is one standard realization of the regular octagonal Banach plane; linearly isometric realizations have the same constant.

The unit ball has vertices
\[
(1,r),(r,1),(-r,1),(-1,r),(-1,-r),(-r,-1),(r,-1),(1,-r),
\qquad r=\sqrt2-1.
\]
Only \(0\le m\le1/2\) needs to be considered because interchanging \(x\) and \(y\) shows \(C'_{\mathrm{NJ}}(\lambda,X_8)=C'_{\mathrm{NJ}}(1-\lambda,X_8)\).

## Proof
For fixed \(y\), the objective is a convex function of \(x\) on the polygonal unit ball: each summand is the square of a norm composed with an affine map. Its maximum over the unit ball is therefore attained at a vertex. With that vertex fixed, the same argument applies to \(y\). Since every vertex is on the unit sphere, the sphere supremum equals the maximum over vertex pairs.

Dihedral symmetry fixes the first vertex as \(v_0=(1,r)\), and it suffices to compare \(v_k\) for separations \(k=0,1,2,3,4\). Write the corresponding objectives as \(F_k(m)\). Direct support-function evaluation of the octagonal norm gives
\[
F_0(m)=F_4(m)=1,
\]
\[
F_1(m)=1+4r^2m(1-m),
\]
\[
F_2(m)=\left(1-(2-\sqrt2)m\right)^2+2m(1-m),
\]
and
\[
F_3(m)=
\begin{cases}
1+(4-2\sqrt2)m-2m^2,&0\le m\le r,\\
r^2+4m(1-m),&r\le m\le1/2.
\end{cases}
\]
For completeness, the support changes behind these formulas are elementary. For \(k=1\), the convex combination of adjacent vertices stays on the supporting line \(|s|+|t|=\sqrt2\), while \(N(v_0-v_1)=2r\). For \(k=2\), the second coordinate supports the norm throughout \(0\le m\le1/2\), and \(N(v_0-v_2)=\sqrt2\). For \(k=3\), the diagonal support gives \(1-\sqrt2m\) until \(m=r\), after which the constant coordinate \(r\) supports the norm; moreover \(N(v_0-v_3)=2\).

The comparison is exact. On \(0<m<1\),
\[
F_3^{\mathrm{first}}(m)-F_2(m)=2m(2\sqrt2-3)(m-1)>0.
\]
Also
\[
F_3^{\mathrm{first}}(m)-F_1(m)
=-2m\left((-5+4\sqrt2)m+4-3\sqrt2\right),
\]
whose nonzero factor has the unique zero
\[
m_*=-\frac{4-3\sqrt2}{-5+4\sqrt2}=\frac{4-\sqrt2}{7}.
\]
Since \(m_*<r\), the three-edge pair dominates through \(m_*\), and the adjacent pair dominates it afterwards. The remaining comparisons do not create another envelope branch: \(F_1-F_2\) changes sign only at \(1/2-\sqrt2/4<m_*\), and for \(r\le m\le1/2\),
\[
F_1(m)-F_3^{\mathrm{second}}(m)=2(\sqrt2-1)(2m-1)^2\ge0.
\]
Both surviving branches are at least \(1\), so \(F_0\) and \(F_4\) are also dominated. This proves the stated profile.

## Verification
The accompanying `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\). It reconstructs the five vertex-separation distances, certifies the support changes for the \(k=2\) and \(k=3\) cases by exact endpoint inequalities for affine functions, checks the polynomial factor identities used in the envelope comparison, verifies \(0<(1/2-\sqrt2/4)<m_*<\sqrt2-1<1/2\), and checks continuity and the \(\lambda=1/2\) endpoint. A successful run prints `VERIFY_OK`. No floating-point computation is used in the certificate.

## Relationship to prior work
Wang, Liu, Li, Ni, Yang, Sarfraz and Li introduced \(C'_{\mathrm{NJ}}(\lambda,X)\) and proved general bounds and structural consequences in arXiv:2110.15741. Their current full text was inspected at the definition, propositions, examples and the sections containing the two related higher-order parameterized constants; a full-text search for “octagon” returns no occurrence. Their concrete calculations therefore do not state the profile above.

Yang, Li and Yang, Filomat 38:5 (2024), 1583–1593, compute exact \(L_{YJ}(\lambda,\mu,X)\) and \(L'_{YJ}(\lambda,\mu,X)\) values for the regular octagon. That work is the closest inspected octagon calculation, but its unit-sphere functional is
\[
\frac{N(\lambda x+\mu y)^2+N(\mu x-\lambda y)^2}{2(\lambda^2+\mu^2)},
\]
which is not the present functional: the second term has swapped coefficients instead of \(\lambda(1-\lambda)N(x-y)^2\). The two functionals meet the classical modified von Neumann–Jordan setting only at the symmetric endpoint after normalization, so the 2024 formulas do not imply the full profile proved here.

Targeted searches for the exact threshold, the regular-octagon \(C'_{\mathrm{NJ}}\) profile, parameter aliases, and the older unrestricted \(C_\alpha\) formulation did not locate a statement covering the displayed formula. Search failure alone is not used as a novelty proof; the substantive comparison is with the defining full text and the later exact regular-octagon paper above.

## Limitations
This is an exact result for one two-dimensional polyhedral Banach space and one specific unit-sphere invariant. It does not determine the unrestricted \(C_\alpha(X_8)\), does not classify all regular polygonal norms, and does not assert that the same two-branch pattern persists beyond the octagon. The literature comparison is strong for the defining paper and the closest exact regular-octagon paper, but there remains ordinary bibliographic risk that an independently phrased equivalent calculation exists outside the sources and databases searched.

## References
1. Y. Wang, Q. Liu, Q. Li, Q. Ni, Z. Yang, M. Sarfraz, Y. Li, “Novel constants based on the generalization of Von Neumann-Jordan constant,” arXiv:2110.15741. First public version: 29 October 2021. Primary MSC 2020: \(46B20\).
2. X. Yang, H. Li, C. Yang, “On the \(L_{YJ}(\lambda,\mu,X)\) constant for the regular octagon space,” Filomat 38:5 (2024), 1583–1593, DOI: 10.2298/FIL2405583Y.
3. H. Fetter and V. Pérez García, “Another version of the von Neumann-Jordan constant,” Journal of Nonlinear and Convex Analysis 13(1) (2012), 125–139, as cited in arXiv:2110.15741 for the unrestricted \(C_\alpha\) constant.
