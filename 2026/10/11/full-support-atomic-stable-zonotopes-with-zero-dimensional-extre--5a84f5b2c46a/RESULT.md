# Full-support atomic stable zonotopes with zero-dimensional extreme sets

## Finding

**Theorem (geometrically decaying atomic spectral laws).** Let \(d\ge2\), \(0<\alpha<1\), and let \((v_j)_{j\ge1}\) be distinct unit vectors whose set is dense in \(S^{d-1}\). Let \(p_j>0\) satisfy \(\sum_{j\ge1}p_j=1\), and assume that there are \(C_0<\infty\) and \(0<\rho<1\) such that
\[
\sum_{j>n}p_j\le C_0\rho^n\quad\text{for every integer }n\ge1.
\]
Let \((\Gamma_k)_{k\ge1}\) denote the increasing points of a rate-one Poisson process on \((0,\infty)\); independently choose iid \(\varepsilon_k\) with law \(\sigma=\sum_{j\ge1}p_j\delta_{v_j}\). The random countable stable zonotope is the Hausdorff-convergent Minkowski series
\[
Z_\alpha=\bigoplus_{k\ge1}\Gamma_k^{-1/\alpha}[0,\varepsilon_k].
\]
Almost surely, \(Z_\alpha\) has nonempty interior and continuum-many exposed points, yet
\[
\dim_H(\operatorname{ext}Z_\alpha)
=\dim_P(\operatorname{ext}Z_\alpha)
=\overline{\dim}_B(\operatorname{ext}Z_\alpha)=0.
\]
Indeed, with \(N_r\) denoting the minimum number of Euclidean **closed balls of radius \(r\)** covering a set, there is a finite random \(C_{\omega,d,\alpha,\sigma}\) such that
\[
N_r(\operatorname{ext}Z_\alpha)
\le C_{\omega,d,\alpha,\sigma}\bigl(1+\log(1/r)\bigr)^{d-1}
\quad(0<r<1/2).
\]
For an explicit full-support law, enumerate all distinct normalized primitive nonzero integer vectors, beginning with a linearly independent selection, and take \(p_j=2^{-j}\). Thus full topological support does not by itself impose any positive fractal dimension on the set of extreme points, even for a full-dimensional stable zonotope with uncountably many exposed points.

## Assumptions and scope

The norm and all metric dimensions are Euclidean; \(\dim_H\), \(\dim_P\), and \(\overline{\dim}_B\) mean Hausdorff, packing, and upper box dimensions, respectively. The upper box dimension is defined through finite-radius covering numbers and therefore applies also when the set of extreme points is not closed. A point is *exposed* if it uniquely maximizes some nonzero linear functional, and *extreme* if it lies in no nontrivial open segment of the body. The deterministic directional atoms are pairwise distinct, dense in the entire sphere, and have positive masses summing to one. The exponential-tail hypothesis is on their **ordered mass tail**, not on the Poisson jump sizes.

No claim is made for uniform spherical or absolutely continuous spectral measures or for all full-support spectral measures. The theorem is almost sure with respect to the underlying marked Poisson process. The normal vectors used in the support-map proof are distinct from the random directional marks.

## Proof

**1. Absolute convergence and grouped jumps.** By the strong law \(\Gamma_k/k\to1\) almost surely, and \(\sum_{k\ge1}k^{-1/\alpha}<\infty\). Therefore the Minkowski series converges and the total length is finite almost surely. Group all its segments with the same direction:
\[
L_j=\sum_{k:\varepsilon_k=v_j}\Gamma_k^{-1/\alpha},\qquad
Z_\alpha=\bigoplus_{j\ge1}L_j[0,v_j],\qquad
R_n=\sum_{j>n}L_j.
\]
Independently marking Poisson points produces the intensity \(\alpha r^{-1-\alpha}\,\mathrm{d}r\,\sigma(\mathrm{d}v)\). For any set of marked directions with total probability \(w\), the sum \(T_w\) of lengths has Laplace transform
\[
\mathbb E e^{-tT_w}
=\exp\left[-w\int_0^\infty(1-e^{-tr})\alpha r^{-1-\alpha}\,\mathrm{d}r\right]
=\exp\bigl(-w\Gamma(1-\alpha)t^\alpha\bigr),\quad t\ge0.
\]
In particular, each \(L_j\) is strictly positive almost surely: its Poisson intensity of jumps is infinite, and all jumps are positive. Put \(w_n=\sum_{j>n}p_j\); then \(R_n\) has the same law as \(w_n^{1/\alpha}T_1\). For any \(0<q<\alpha\), the fractional moment of the positive \(\alpha\)-stable variable \(T_1\) is finite. This also follows directly from the above Laplace transform and the identity
\[
\mathbb E T_1^q
=\frac q{\Gamma(1-q)}\int_0^\infty
\bigl(1-\mathbb E e^{-tT_1}\bigr)t^{-q-1}\,\mathrm{d}t<\infty.
\]
Thus, for \(K_{\alpha,q}=\mathbb E T_1^q<\infty\),
\[
\mathbb E R_n^q=K_{\alpha,q}w_n^{q/\alpha}
\le K_{\alpha,q}C_0^{q/\alpha}\rho^{nq/\alpha}.
\]
Let \(b=-\log\rho>0\) and choose any \(0<c<b/\alpha\). Markov's inequality gives
\[
\mathbb P\{R_n>e^{-cn}\}
\le K_{\alpha,q}C_0^{q/\alpha}
 e^{-nq(b/\alpha-c)},
\]
a summable sequence. Borel–Cantelli therefore yields \(R_n\le e^{-cn}\) for all sufficiently large \(n\), almost surely.

**2. Finite chamber covering.** Work on a sample for which every \(L_j>0\), the total length is finite, and the exponential tail bound holds. Define the finite zonotope
\[
P_n=\bigoplus_{j=1}^nL_j[0,v_j]
\quad\text{and}\quad
G=S^{d-1}\setminus\bigcup_{j\ge1}\{u:\langle u,v_j\rangle=0\}.
\]
The set \(G\) has full spherical surface measure. For every \(u\in G\), the functional \(\langle u,\cdot\rangle\) has the **unique** maximizer
\[
X(u)=\sum_{j\ge1}L_jv_j\mathbf1_{\{\langle u,v_j\rangle>0\}}
\]
on \(Z_\alpha\). Its truncation \(X_n(u)\) is a vertex of \(P_n\) and satisfies \(\|X(u)-X_n(u)\|\le R_n\). Conversely, if a normal is orthogonal to some \(v_j\), the support face contains a translate of the nondegenerate segment \(L_j[0,v_j]\) and is not a singleton. Hence all exposed points are exactly \(X(G)\). Straszewicz's theorem gives
\[
\operatorname{ext}Z_\alpha\subset\overline{X(G)}.
\]
A central arrangement of \(n\) hyperplanes through the origin in \(\mathbb R^d\) has at most
\[
M_d(n)=2\sum_{i=0}^{d-1}\binom{n-1}{i}
\]
open chambers. This bound follows by inserting hyperplanes successively and counting the induced arrangement in dimension one less; degeneracies only reduce the number. On each chamber of \(\{\langle u,v_j\rangle=0\}_{j\le n}\), the truncated support point \(X_n(u)\) is constant. Consequently the set of all \(X_n(u)\), \(u\in G\), has at most \(M_d(n)\) elements. Each \(X(u)\) lies in a closed ball of radius \(R_n\) centered at one such element. **Because this is a finite union of closed balls**, its closure also contains \(\operatorname{ext}Z_\alpha\); no unjustified dimension argument from a dense subset is used. For all sufficiently large \(n\),
\[
N_{e^{-cn}}(\operatorname{ext}Z_\alpha)\le M_d(n)\le C_d n^{d-1}.
\]
For arbitrary sufficiently small \(r\), take \(n=\lceil c^{-1}\log(1/r)\rceil\), making \(e^{-cn}\le r\). Increasing the random multiplicative constant accommodates the finitely many remaining radii \(0<r<1/2\). This proves the asserted polylogarithmic covering bound and
\[
\overline{\dim}_B(\operatorname{ext}Z_\alpha)
=\limsup_{r\downarrow0}\frac{\log N_r(\operatorname{ext}Z_\alpha)}{\log(1/r)}=0.
\]
Hausdorff and packing dimensions are nonnegative and are at most upper box dimension, so both are zero.

**3. Dimension of the body and number of exposed points.** A dense set of directions contains \(d\) linearly independent vectors; since all associated \(L_j\) are positive, their Minkowski sum is a full-dimensional parallelotope contained in \(Z_\alpha\). Thus the body has interior. If \(u,v\in G\) are distinct, choose \(w=(u-v)/\|u-v\|\). Then \(\langle u,w\rangle>0>\langle v,w\rangle\). By density, some \(v_j\) has these same strict inequalities. At this index \(j\), the endpoint selected by \(X(u)\) fails strictly to maximize \(\langle v,\cdot\rangle\); all other segment contributions have nonnegative shortfall, and their total is absolutely convergent. Consequently
\[
\langle v,X(u)\rangle<h_{Z_\alpha}(v)=\langle v,X(v)\rangle,
\]
so \(X(u)\neq X(v)\). Hence \(X\) is injective on the full-surface-measure set \(G\); in particular, \(Z_\alpha\) has continuum-many exposed (and thus extreme) points. All claims follow.

## Verification

The proof is analytic rather than based on a finite sample. Its checkable ingredients are: the Poisson intensity transformation \(s=r^{-\alpha}\); the Laplace integral \(\int_0^\infty(1-e^{-tr})\alpha r^{-1-\alpha}\mathrm{d}r=\Gamma(1-\alpha)t^\alpha\); the fractional moment range \(0<q<\alpha\); the summable Markov bound; the central-hyperplane arrangement count; and finite closed-ball covering before taking closures. At each stage, the finite constants may depend on the realization, dimension, stability index, and mass law but never on the radius \(r\). The continuum claim is certified by injectivity of the explicit support-point map, not by a cardinality inference from positive volume.

## Relationship to prior work

Davydov and Paulauskas, *Remarks on random countable stable zonotopes* (2019), study this same stable Minkowski sum, prove a planar Hausdorff upper bound for arbitrary spectral laws and a matching result under a suitable diffuse angular assumption. Their Remark 6 identifies the **finite-atomic** case as dimension zero and asks about dependence on the directional distribution. The present theorem differs by requiring **infinitely many dense atoms** (hence full topological support and uncountably many exposed points), proving zero **upper box and packing dimensions** in every ambient dimension, and giving quantitative polylogarithmic covering numbers.

Kukushkin, *Hausdorff Dimension of the Set of Extreme Points of a Random Countable Stable Zonotope* (arXiv:2608.28004, first submitted August 28, 2026; version 2 inspected), proves the positive value \((d-1)\alpha\) for the **uniform** directional measure, develops hyperplane-arrangement coverings, and explicitly discusses anisotropic spectral-law assumptions in Section 7. The uniform belt assumption relevant to that theorem fails for the present atomic law: any normal perpendicular to one atom has a belt with measure bounded below by that atom's positive mass, at all positive belt widths. Thus the uniform-density result does not imply this zero-dimensional full-support construction. The chamber-counting and support-parametrization principles are acknowledged as prior tools, not claimed as new lemmas.

Kukushkin, *Geometrical Characteristics of Random Countable Zonotopes* (2025), establishes the general upper bound \(\dim_H\operatorname{ext}Z_\alpha\le\alpha+d-2\) for arbitrary directions. It does not imply zero dimension or any upper-box covering estimate. Its published abstract and theorem statement were consulted; the full PDF could not be visually checked, leaving an explicit residual risk about possible further special constructions.

## Limitations

The spectral law is singular and purely atomic; full support refers only to the topological support, not absolute continuity or a lower density bound. Geometric decay of the **ordered** atomic mass tail is sufficient but not asserted necessary. The conclusion does not determine dimensions for arbitrary infinite atomic laws, mixed atomic–diffuse laws, or uniform measures. The exact leading constant in the covering estimate and any optimal gauge are not determined. Earlier unindexed constructions with equivalent dense-atomic tails remain a literature risk; a positive search result would require reevaluating originality. No computational experiment or independent certification is offered as a substitute for the stated proof.

## References

1. Y. Davydov and V. Paulauskas (2019), *Remarks on random countable stable zonotopes*, Statistics & Probability Letters **153**, 187–191. DOI: 10.1016/j.spl.2019.06.018. Full manuscript text inspected through an openly readable transcription; in particular Theorem 5 and Remark 6.
2. M. Kukushkin (2026), *Hausdorff Dimension of the Set of Extreme Points of a Random Countable Stable Zonotope*, arXiv:2608.28004v1 (August 28, 2026), with full-text inspection of v2 (September 3, 2026), Sections 2–3, 5, 7 and Appendix B.
3. M. A. Kukushkin (2025), *Geometrical Characteristics of Random Countable Zonotopes*, Zapiski Nauchnykh Seminarov POMI **544**, 185–210; mathematical summary and published theorem statement inspected, full-PDF comparison incomplete.
4. R. Schneider (2014), *Convex Bodies: The Brunn–Minkowski Theory*, second edition, Cambridge University Press; standard convex-geometric support and exposed-point facts, as cited in the primary literature.
