# First spherical-cap width transitions of anisotropic orthotopes in dimension four and higher

## Finding

Let \(d\ge4\) and let \(B=\prod_{i=1}^d[-a_i/2,a_i/2]\) be a Euclidean orthotope with \(a_i>0\). For \(U\) uniform on \(S^{d-1}\), its one-dimensional directional width is \(W=\sum_{i=1}^d a_i|U_i|\). Write
\[
L=\Big(\sum_{i=1}^d a_i^2\Big)^{1/2},\qquad m=\min_i a_i,\qquad k=\#\{i:a_i=m\},\qquad q=(L^2-m^2)^{1/2}.
\]
Define \(H(t)=\Pr\{W\ge t\}\) and the unrestricted diagonal-cap expression
\[
C(t)=2^{d-1} I_{1-t^2/L^2}\!\left(\frac{d-1}{2},\frac12\right),\quad 0\le t\le L,
\]
where \(I_z\) is the regularized incomplete beta function. Then the following are **exactly** true:

1. \(H(t)=C(t)\) for \(q\le t\le L\), and \(H(t)<C(t)\) for every \(0<t<q\). Thus \(q\) is the sharp first cap–coordinate-face transition.
2. As \(\varepsilon\downarrow0\),
\[
C(q-\varepsilon)-H(q-\varepsilon)
=\frac{2^d k}{d\pi m}\left(\frac2q\right)^{(d-2)/2}\varepsilon^{d/2}
+o(\varepsilon^{d/2}). \tag{1}
\]
The coefficient is strictly positive for every choice of side lengths, including repeated lengths.
3. In known dimension \(d\), the exact law of \(W\) determines the longest width \(L\), the first transition \(q\), the shortest edge length \(m=(L^2-q^2)^{1/2}\), and its multiplicity \(k\), explicitly obtained from the coefficient in (1). This is a **local transition-based recovery formula**, not a claim that these are the only recoverable geometric parameters.

**Exact local high-tail universality in every dimension.** For all sufficiently small \(q-t>0\), define
\[
s(t)=\frac{-tm+q\sqrt{L^2-t^2}}{L^2},\qquad
G_d(t)=\frac{\Gamma(d/2)}{2\sqrt\pi\,\Gamma((d-1)/2)}
\int_0^{s(t)}(1-s^2)^{(d-3)/2}
I_{1-(t+ms)^2/[q^2(1-s^2)]}\!\left(\frac{d-2}2,\frac12\right)ds.
\]
There is \(\eta>0\) such that
\[
H(t)=C(t)-2^d k\,G_d(t)\quad(q-\eta<t<q). \tag{3}
\]
Hence **the entire high-tail germ**, not merely its leading coefficient, depends only on \((d,L,m,k)\). In dimension four, for example, the two noncongruent boxes with edge vectors \((1,2,3,4)\) and \((1,\sqrt5,\sqrt8,4)\) have \(L=\sqrt{30}\), \(m=1\), \(k=1\), and exactly the same width survival functions throughout some common interval \((q-\eta,L]\). The local tail does **not** determine the remaining side lengths, although the complete law does by previously established moment tomography.

For \(d=4\) there is also an **elementary exact correction** on some nonempty interval \(q-\eta<t<q\) (with \(\eta>0\) depending on the lengths). Define
\[
s(t)=\frac{-tm+q\sqrt{L^2-t^2}}{L^2},\qquad
G(t)=\frac1\pi\left[\frac{\arcsin s(t)+s(t)\sqrt{1-s(t)^2}}2
-\frac{t\,s(t)+m\,s(t)^2/2}{q}\right].
\]
Then
\[
H(t)=8 I_{1-t^2/L^2}\!\left(\frac32,\frac12\right)-16k\,G(t)
\qquad (q-\eta<t<q). \tag{2}
\]
In particular, the coefficient in (1) simplifies to \(8k/(\pi m q)\) in dimension four. Equation (2) is a full finite-threshold identity, not solely an asymptotic expansion.

## Assumptions and scope

The orthotope is full-dimensional, the side lengths are positive real numbers, the direction has normalized Haar/surface law, and \(d\ge4\) is fixed. All widths are ordinary Euclidean line-projection lengths, not volumes of planar shadows. The first-threshold result remains valid when several shortest edges tie; their number is \(k\). The notation \(q\) is a positive **length**, not a probability. The high-tail comparison \(C\) is deliberately not called a probability distribution below \(q\): its unrestricted spherical caps can overlap coordinate orthants there.

The true support of \(W\) is \([\min_i a_i,L]\), and endpoint values are interpreted continuously. The inequality \(H(t)<C(t)\) is asserted for \(0<t<q\), which includes low thresholds where \(C(t)\) can exceed one. The exact elementary formula is local near the first threshold; it is not claimed across additional intersections with multiple coordinate faces.

## Proof

**1. Spherical-cap representation.** In the positive orthant \(\mathcal O\) set \(v=(a_1,\ldots,a_d)/L\). For positive \(U\), \(W=L\langle U,v\rangle\). The corresponding superlevel set is the intersection of \(\mathcal O\) with the spherical cap of angular radius \(\theta=\arccos(t/L)\) about \(v\). All \(2^d\) orthants contribute equally to \(H\). A full cap has normalized spherical measure
\[
\frac12 I_{1-t^2/L^2}\!\left(\frac{d-1}{2},\frac12\right),
\]
which follows by integrating \((\sin\phi)^{d-2}\) in polar coordinates. This gives \(C\) after multiplication by \(2^d\), before restricting each cap to its orthant.

The spherical distance from \(v\) to the face \(U_i=0\) is \(\arcsin(a_i/L)\). Its smallest value is \(\arcsin(m/L)\). Therefore the cap is contained in \(\mathcal O\) if and only if \(\arccos(t/L)\le\arcsin(m/L)\), namely \(t\ge q\). When \(t<q\) a cap crosses a coordinate face in an open positive-area region, giving strict \(H<C\). This proves the first assertion for the entire stated range.

**2. Distinct facet crossings cannot overlap near \(q\).** If two specified coordinates of \(u\in S^{d-1}\) are nonpositive, the nonnegative coefficients imply
\[
\sum_{i=1}^d a_i u_i\le\sum_{\ell\ne i,j} a_\ell u_\ell
\le \sqrt{L^2-a_i^2-a_j^2}<q.
\]
There are finitely many pairs, so there is an interval immediately below \(q\) where no cap region outside one coordinate face simultaneously lies outside another. The only individual faces crossed in that interval are those with \(a_i=m\). Exactly \(k\) disjoint facet-excess regions must therefore be removed from the unrestricted cap in each orthant. This is a local exact inclusion-exclusion identity, not an asymptotic approximation.

**3. Universal leading facet-excess area.** Fix a shortest coordinate and write its negative value as \(-s\) with \(s\ge0\). In the complementary coordinates, let \(v'\in S^{d-2}\) be the normalized remaining coefficient vector, of norm \(q\). Put the complementary unit direction in geodesic coordinates \(\omega=\sqrt{1-|y|^2}\,v'+y\), \(y\perp v'\), \(y\in\mathbb R^{d-2}\). The cap-excess condition for \(t=q-\varepsilon\) is precisely
\[
-ms+q\sqrt{1-s^2}\sqrt{1-|y|^2}\ge q-\varepsilon.
\]
It forces \(s=O(\varepsilon)\) and \(|y|=O(\sqrt\varepsilon)\), while the normalized spherical area density tends to ordinary Lebesgue density in \((s,y)\) at the tangency point. Rescaling \(s=\varepsilon z\), \(y=\sqrt\varepsilon\,\xi\), the rescaled excess tends to the bounded region
\[
\bigl\{z\ge0:\ mz+q|\xi|^2/2\le1\bigr\}.
\]
Standard dominated convergence follows by bounding the angular aperture and the normal-coordinate width uniformly inside a compact rescaled neighborhood (the strict quadratic maximum of the cap determines these bounds). Its Euclidean volume is
\[
\int_0^{1/m}\kappa_{d-2}\Big(\frac{2(1-mz)}q\Big)^{(d-2)/2}\,dz
=\frac{2\kappa_{d-2}}{dm}\Big(\frac2q\Big)^{(d-2)/2},
\]
where \(\kappa_{d-2}=\pi^{(d-2)/2}/\Gamma(d/2)\). Since \(|S^{d-1}|=2\pi^{d/2}/\Gamma(d/2)\), their ratio is \(\kappa_{d-2}/|S^{d-1}|=1/(2\pi)\). Multiplication by \(2^d\) orthants and \(k\) shortest faces yields exactly the positive coefficient in (1), without assuming the box is a cube.

**4. Exact all-dimensional local face correction and its information boundary.** For one shortest coordinate, spherical slicing at \(u_j=-s\) gives marginal density
\[
\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-s^2)^{(d-3)/2}.
\]
Conditional on this coordinate, the remaining direction is uniform on \(S^{d-2}\); the cap fraction beyond the height \((t+ms)/(q\sqrt{1-s^2})\) is one half of the regularized incomplete beta function displayed in (3). Its nonzero range is \(0<s<s(t)\), determined by the quadratic cap equality. Multiplying the resulting single-face probability \(G_d(t)\) by exactly \(2^d k\) disjoint crossings proves (3). The integral uses only \(d,m,q\), not the distribution of the remaining positive coefficients. Since \(L^2=m^2+q^2\), any two boxes with the same \((d,L,m,k)\) consequently have identical high-tail laws on an intersection of their positive first-crossing neighborhoods. The two explicitly displayed four-dimensional side vectors have the same four invariants but different side multisets, proving the stated local nonidentifiability.

**5. The exact four-dimensional expression.** On \(S^3\), the marginal density of one spherical coordinate \(x\) equals \((2/\pi)\sqrt{1-x^2}\). Conditional on that coordinate, the remaining normalized direction is uniform on \(S^2\), whose spherical-cap fraction at height \(h\in[-1,1]\) is \((1-h)/2\). Parameterizing the crossed facet by \(x=-s\), the one-face cap leakage is therefore
\[
\frac1\pi\int_0^{s(t)}\left[\sqrt{1-s^2}-\frac{t+ms}{q}\right]ds.
\]
The upper endpoint is determined by \(t+ms=q\sqrt{1-s^2}\) and has the explicit solution stated above. The antiderivative \(\int\sqrt{1-s^2}\,ds=(\arcsin s+s\sqrt{1-s^2})/2\) proves \(G(t)\). By Step 2 exactly \(k\) such regions are disjoint and no other faces are crossed for \(q-\eta<t<q\); multiplication by \(2^4=16\) gives (2).

**6. Inverse reading of the first transition.** The essential supremum of the observed width law is \(L\) by Cauchy–Schwarz and attainability of \(v\). As \(d\) is given, the function \(C\) is thereby determined by the observed law. The unique sharp boundary between equality and strict inequality is \(q\) by Step 1. Therefore \(m=\sqrt{L^2-q^2}\). Finally (1) and the known values \(d,m,q\) give \(k\) by direct division by a strictly positive factor. This requires the exact law; no statistical stability assertion is made.

## Verification

The standalone `verify.py` implements the beta-cap formula and computes individual facet leakage from independent one-dimensional spherical-coordinate quadrature. It tests the \(d/2\)-power coefficient in dimensions four, five and six, including both unequal and repeated minimum side lengths. For dimension four it independently checks the elementary integral (2), then compares the analytical upper-tail probability against seeded quasi-Monte-Carlo sampling of over a million uniformly distributed spherical directions. The program uses Python 3, NumPy and SciPy; run `python3 verify.py` in the same directory. Its actual successful output was `VERIFY_OK 87 independent numeric, exact integration and sphere-distribution tests`. These are checks, not substitutes for the universal analytic derivation above.

## Relationship to prior work

Finch's 2011 work on regular-polyhedron widths computes moments in three dimensions, including the cube; it does not derive a higher-dimensional anisotropic box transition. Kabluchko–Litvak–Zaporozhets provide general mean-width and Gaussian-maxima machinery for regular polytopes; Paouris–Pivovarov–Zinn study asymptotic cube projections. A separately published all-dimensional result gives the cube-only first spherical-cap crossing and its coefficient. That **entire equal-side specialization** is prior work, not new here: setting \(a_i=1\), \(k=d\) in (1) recovers its constant exactly.

Recent work by Abas (*Width Laws and Spectral Geometry*, 2026) proves that the first \(d\) full width moments recover an orthotope's complete side vector. We therefore make **no claim that mere recoverability of the shortest edge or its multiplicity from the entire law is new**; that follows already from stronger moment identification. The subject of this finding is instead the precise sharp face-crossing threshold, its explicitly normalized universal local singular coefficient and shortest-facet multiplicity, and a finite exact four-dimensional formula. Abas's companion work on rectangular-box width distributions concerns dimension three. The main 2026 paper’s introductory results, orthotope moment analysis, and three-dimensional singularity theorem were inspected in accessible full text; they do not state the higher-dimensional anisotropic first-cap coefficient. The companion three-dimensional paper was accessible only by abstract, and an equivalent local argument in uninspected text remains a priority risk.

## Limitations

The result exactly classifies only the first threshold neighborhood and not the complete distribution away from its first spherical-cap crossing. It does not provide noisy-data stability for reading \(q\) or \(k\), or a new proof of full side-vector identifiability, which is already established in the cited recent work. The exact elementary correction is specific to dimension four and local to \(q\). While the dimensional exponent and the cube specialization were known, the novel priority assessment concerns their anisotropic shortest-facet coefficient and local four-dimensional formula; overlap with the inaccessible complete three-dimensional companion work or other unlocated papers cannot be excluded. No independent external scientific audit has been performed.

## References

1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first posted 2011-10-04, https://arxiv.org/abs/1110.0671.
2. G. Paouris, P. Pivovarov, J. Zinn, *A central limit theorem for projections of the cube*, arXiv:1210.7012, first posted 2012-10-25, https://arxiv.org/abs/1210.7012.
3. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first posted 2015-11-26, https://arxiv.org/abs/1511.08479.
4. O. Abas, *Width distributions for rectangular boxes*, arXiv:2608.03305, first posted August 2026, https://arxiv.org/abs/2608.03305.
5. O. Abas, *Width Laws and Spectral Geometry*, arXiv:2608.06348, first posted 2026-08-06, https://arxiv.org/abs/2608.06348.
6. *Exact directional width law of the cube and its first spherical-cap transition*, publicly available mathematical report, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2/RESULT.md.
