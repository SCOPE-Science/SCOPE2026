# Superexponential two-facet deficit of Haar central cube sections

## Finding
Let \(d\ge3\) be an integer and \(Q_d=[-1,1]^d\). Choose a Haar-uniform unoriented hyperplane \(H\) through the origin and let \(F_d\) be the number of facets (faces of dimension \(d-2\)) of the \((d-1)\)-polytope \(Q_d\cap H\). Almost surely, \(F_d\in\{2d-2,2d\}\). The exceptional probability \(p_d=\Pr(F_d=2d-2)\) has the sharp dimension-asymptotic law
\[
\boxed{p_d=\frac{d\,e^{-1}}{\pi^{(d-1)/2}\Gamma((d+1)/2)}\left(1+\frac{7}{2(d-1)}+O((d-1)^{-2})\right),\qquad d\longrightarrow\infty.}
\]
In particular,
\[
\boxed{p_d\sim\frac{d}{e\sqrt{\pi(d-1)}}\left(\frac{2e}{\pi(d-1)}\right)^{(d-1)/2}.}
\]
The exact finite-dimensional geometry and the almost-sure two-value support are background facts; the claimed contribution is the **explicit superexponential probability scale, leading factor \(e^{-1}\), and first relative correction \(7/(2(d-1))\)**.

## Assumptions and scope
The normal vector to \(H\) is uniform on the unit sphere, with antipodal normals representing the same hyperplane. All equalities below are almost sure because the exceptional sets where a normal coordinate vanishes or a signed sum of its coordinates vanishes have spherical measure zero. Dimensions are integers \(d\ge3\) and the limit is \(d\to\infty\), not a limit in section offset. The measure is rotationally invariant on central hyperplanes; no arbitrary-offset line or plane distribution is used.

Write \(m=d-1\), let \(G_0,\ldots,G_m\) be independent standard Gaussians, and set \(Y_i=|G_i|\). Their half-normal density is \(c\exp(-y^2/2)\) for \(y>0\), with \(c=\sqrt{2/\pi}\).

## Proof
**1. Geometric event and disjointness.** A facet of \(Q_d\) is obtained by fixing coordinate \(i\) to \(+1\) or \(-1\). On that facet the linear functional \(x\mapsto G\cdot x\) ranges from \(\pm G_i-\sum_{j\ne i}|G_j|\) to \(\pm G_i+\sum_{j\ne i}|G_j|\). For a generic normal, both opposite facets are intersected transversally if and only if \(|G_i|<\sum_{j\ne i}|G_j|\); otherwise both are missed. At most one index can violate this strict inequality because two different coordinates cannot each exceed the sum of all the others. Thus \(F_d\) equals either \(2d\) or \(2d-2\) almost surely, and
\[
p_d=d\,q_m,\qquad q_m=\Pr(Y_0>Y_1+\cdots+Y_m).
\]

**2. Exact normalization and simplex mixture.** The survival function of \(Y_0\) is \(\operatorname{erfc}(s/\sqrt2)\). Hence
\[
q_m=c^m\int_{(0,\infty)^m}\exp\!\left(-\tfrac12\sum_{i=1}^m y_i^2\right)\operatorname{erfc}\!\left(\frac{\sum_i y_i}{\sqrt2}\right)\,dy_1\cdots dy_m.
\]
Make the substitution \(s=\sum_i y_i\), \(y_i=sU_i\), where \(U=(U_1,\ldots,U_m)\) is uniformly distributed on the standard \((m-1)\)-simplex (the \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution). The simplex-slice Jacobian is \(s^{m-1}/(m-1)!\), so
\[
q_m=B_m\,\mathbb E\exp(-X_m),\qquad
B_m=\frac{c^m\mathbb E Y_0^m}{m!}=\frac{1}{\pi^{m/2}\Gamma(m/2+1)},
\]
where
\[
X_m=\frac12S_m^2\sum_{i=1}^m U_i^2,
\quad f_{S_m}(s)=\frac{m s^{m-1}\operatorname{erfc}(s/\sqrt2)}{\mathbb E Y_0^m},\quad s>0,
\]
and \(S_m\) and \(U\) are independent. The displayed density integrates to one by the layer-cake identity \(\mathbb E Y_0^m=m\int_0^\infty s^{m-1}\Pr(Y_0>s)ds\). The expression for \(B_m\) uses \(\mathbb E Y_0^m=2^{m/2}\Gamma((m+1)/2)/\sqrt\pi\) and the Gamma duplication identity.

An equivalent exact sampling representation is
\[
S_m^2\overset{\mathrm d}=Z_m V^{2/m},\qquad Z_m\sim\chi^2_{m+1},\quad V\sim\operatorname{Uniform}(0,1),
\]
with \(Z_m,V,U\) independent. Indeed, the half-normal law weighted by \(Y_0^m\) gives \(Z_m\), and conditionally on the size-biased value \(Y_0=z\), the simplex-sum variable has density \(m s^{m-1}/z^m\) on \((0,z)\).

**3. Exact moments.** For every positive integer \(k\), the independent-mixture representation gives
\[
\mathbb E X_m^k=\left(\prod_{j=0}^{k-1}\frac{m+2j+1}{2}\right)\frac{m}{m+2k}\,
\frac{k!}{(m)_{2k}}[t^k]\left(\sum_{r=0}^{k}\frac{(2r)!}{r!}t^r\right)^m,
\]
where \((m)_{2k}=m(m+1)\cdots(m+2k-1)\) and \([t^k]\) means coefficient extraction. This follows directly from the ordinary Dirichlet joint moments, \(\mathbb E\prod_i U_i^{r_i}=\prod_i r_i!/(m)_{\sum_i r_i}\). Expanding for \(k=1,2,3,4\) yields
\[
\begin{aligned}
\mathbb E X_m&=\frac{m}{m+2},\\
\mathbb E X_m^2&=\frac{m(m+5)}{(m+2)(m+4)},\\
\mathbb E X_m^3&=\frac{m(m^2+15m+74)}{(m+2)(m+4)(m+6)},\\
\mathbb E X_m^4&=\frac{m(m^3+30m^2+371m+2118)}{(m+2)(m+4)(m+6)(m+8)}.
\end{aligned}
\]
Consequently, writing \(\Delta_m=X_m-1\),
\[
\begin{aligned}
\mathbb E\Delta_m&=-\frac2{m+2},\\
\mathbb E\Delta_m^2&=\frac{3m+8}{(m+2)(m+4)},\\
\mathbb E\Delta_m^3&=\frac{12(m-4)}{(m+2)(m+4)(m+6)},\\
\mathbb E\Delta_m^4&=\frac{3(9m^2+274m+128)}{(m+2)(m+4)(m+6)(m+8)}.
\end{aligned}
\]
Since \(X_m\ge0\), we have \(\Delta_m\ge-1\). Taylor's theorem around zero, to cubic order, has a fourth-order remainder bounded by \(e|\Delta_m|^4/24\) for the function \(e^{-\Delta_m}\). Taking expectations and substituting the exact central moments yields
\[
\mathbb E e^{-X_m}
=e^{-1}\left(1-\mathbb E\Delta_m+\tfrac12\mathbb E\Delta_m^2-\tfrac16\mathbb E\Delta_m^3+O(\mathbb E\Delta_m^4)\right)
=e^{-1}\left(1+\frac7{2m}+O(m^{-2})\right).
\]
Together with \(p_d=dq_m\) and the exact \(B_m\) this proves the boxed asymptotic law. Stirling's formula for \(\Gamma(m/2+1)\) proves the second displayed equivalent.

## Verification
Execute `python3 verify.py` from the directory containing this file. Its standard-library checks reconstruct the first four \(X_m\) moments independently from the truncated Dirichlet generating polynomial and verify the rational formulas for dimensions \(m=1,\ldots,30\). It also enumerates all vertices of each cube facet for 1,250 independently sampled normals in dimensions three through seven, checking that the geometric crossing count equals the stated two-point law. A separate size-biased Gamma/Dirichlet sampler checks the normalized probability against the exact small-dimensional values and large-dimensional asymptotics; the random checks are explicitly diagnostics, not proofs.

The exact low-dimensional probabilities follow from independent earlier geometry: \(p_3=6\arcsin(1/3)/\pi\) and \(p_4=1/3\). For \(m=1\), \(q_1=1/2\). These values can be used to check numerical normalizations, but are not new claims.

## Relationship to prior work
Lonke (1998) established expected face-count formulas and leading fixed-codimension asymptotics for random cube sections. In the present codimension-one facet case his asymptotic implies \(\mathbb E F_d\sim2d\), consistent with \(p_d\to0\), but does not give the sharp superexponential deficit or its two leading constants. Kabluchko and Seidel (2020) obtain general finite-dimensional formulas for expected section face counts from conic intrinsic volumes (especially Section 4, Proposition 4.2); these imply a finite-dimensional expression for \(p_d\) together with the known two-point support, but do not state or derive its \(d\to\infty\) prefactor and correction. Donoho and Tanner (2008) address projected-hypercube face counts and different proportional-growth thresholds. Böröczky and Henk (1997 preprint; 2000 journal) treat projections of regular polytopes and spherical regular-simplex angles in a different, fixed-output-dimensional regime. A public exact calculation for the four-cube gives \(p_4=1/3\); that finite case does not imply the high-dimensional rate.

The sharp asymptotic is derived here from a half-normal rare event and an exact Dirichlet-mixture moment computation, rather than asserted to be a new general formula for cube-section face counts.

## Limitations
The estimate concerns only Haar-uniform **central** sections of the Euclidean cube; it does not extend as written to noncentral cuts, unequal box side lengths, or other random normal distributions. It is a dimension-asymptotic statement and makes no universal finite-dimensional inequality claim. General existing conic-volume formulas give implicit access to the probability, so historical-priority uncertainty remains for the explicit dimension-asymptotic constant and correction. The work has not received independent mathematical review.

## References
1. Y. Lonke, *On random sections of the cube*, arXiv:math/9812123, first posted 1998-12-21. https://arxiv.org/html/math/9812123v1.
2. Z. Kabluchko and H. Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492, first posted 2020-06-16, Sections 4 and 5.3. https://arxiv.org/html/2006.09492v2.
3. D. L. Donoho and J. Tanner, *Counting the faces of randomly-projected hypercubes and orthants, with applications*, arXiv:0807.3590, first posted 2008-07-23. https://arxiv.org/abs/0807.3590.
4. K. Böröczky Jr. and M. Henk, *Random projections of regular polytopes*, preprint dated May 1997; *Archiv der Mathematik* 2000. https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf.
5. *Exact two-point face-vector law for random central sections of the four-cube*, public research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-two-point-face-vector-law-for-random-central-sections-of-t--88770003c8ac.
