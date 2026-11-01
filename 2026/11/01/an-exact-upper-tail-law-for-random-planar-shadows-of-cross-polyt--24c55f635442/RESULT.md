# An exact upper-tail law for random planar shadows of cross-polytopes

## Finding

For every integer \(n\ge3\), set
\[
C_n=\operatorname{conv}\{\pm e_1,\ldots,\pm e_n\}\subset\mathbb R^n.
\]
Let \(E\) be Haar-uniform on the real Grassmannian \(\operatorname{Gr}(2,n)\), and let \(A_n(E)\) be the ordinary Euclidean area of the orthogonal projection of \(C_n\) onto \(E\). There exists a strictly positive number \(\delta_n\), defined explicitly by a compact variational prescription below, such that **for every real \(0<\varepsilon<\delta_n\)**,
\[
\boxed{\displaystyle
\mathbb P\{A_n(E)\ge2-\varepsilon\}
 =\binom n2\left(\frac{\varepsilon}{2}\right)^{n-2}.}
\]
The exponent \(n-2\) and the full coefficient are exact, with no omitted asymptotic terms on this nonempty upper-tail interval. In particular, for \(n=3\) this is \(3\varepsilon/2\), and for \(n=4\) it is \(3\varepsilon^2/2\).

For \(N\) independent Haar-uniform planes, write \(M_{n,N}\) for the greatest of their projected areas and \(c_n=\binom n2/2^{n-2}\). The same theorem yields the extreme-value limit
\[
\lim_{N\to\infty}
\mathbb P\{N^{1/(n-2)}(2-M_{n,N})>t\}
=\exp(-c_n t^{n-2})\qquad(t\ge0),
\]
and the sharp mean-deficit asymptotic
\[
\mathbb E(2-M_{n,N})\sim
\frac{\Gamma(1+1/(n-2))}{(c_nN)^{1/(n-2)}}.
\]
These are statements about random orientations of one fixed polytope, not random vertices or Gaussian linear images with unconstrained normalization.

## Assumptions and scope

Orient \(E\) arbitrarily and choose an orthonormal basis \(u,v\in\mathbb R^n\) of \(E\). Put \(w_i=(u_i,v_i)\in\mathbb R^2\) and
\[
p_{ij}(E)=|u_iv_j-u_jv_i|=|\det(w_i,w_j)|,\qquad i<j.
\]
The choice of basis affects the signs of determinants, not their absolute values or the projected area. Orthonormality gives
\[
\sum_{i=1}^n w_iw_i^{\mathsf T}=I_2,
\qquad\sum_{i<j}p_{ij}(E)^2=1.
\]
The latter is the Cauchy--Binet identity. The projected polygon is
\(\operatorname{conv}\{\pm w_1,\ldots,\pm w_n\}\).

Set \(s_0=\sqrt{2/3}\). The compact set
\[
\mathcal K_n=\{E\in\operatorname{Gr}(2,n):\max_{i<j}p_{ij}(E)\le s_0\}
\]
is nonempty: for \(n=3\), take the plane perpendicular to \((1,1,1)\); for larger \(n\), embed this plane into the first three coordinates. Define
\[
b_n=\max_{E\in\mathcal K_n}A_n(E),\qquad
\delta_n=\min\{2-b_n,\ 2(1-s_0)\}.
\]
The published exact equality characterization for cross-polytope projections implies \(b_n<2\), because every area-maximizing plane is a coordinate two-plane, whose largest Plücker coordinate is \(1>s_0\). Thus \(\delta_n>0\). This prescription makes the interval mathematically exact but does not evaluate its optimal endpoint or assert that it is best possible.

## Proof

**1. A two-generator containment lemma.** Fix \(i<j\) with \(p=p_{ij}(E)\ge s_0\). The matrix \(W=[w_i\ \ w_j]\) is invertible. For \(k\notin\{i,j\}\), express \(w_k=Wz_k\) and set \(H=\sum_{k\ne i,j}z_kz_k^{\mathsf T}\succeq0\). The tight-frame identity becomes
\[
W(I_2+H)W^{\mathsf T}=I_2,
\qquad \det(I_2+H)=p^{-2}\le\frac32.
\]
Since \(\det(I_2+H)=1+\operatorname{tr}H+\det H\) for positive-semidefinite \(2\times2\) matrices,
\(\operatorname{tr}H\le1/2\). For every remaining generator,
\[
\|z_k\|_1\le\sqrt2\|z_k\|_2
\le\sqrt{2\operatorname{tr}H}\le1.
\]
Consequently \(w_k\in\operatorname{conv}\{\pm w_i,\pm w_j\}\). The entire projected cross-polytope equals this parallelogram and therefore
\[
A_n(E)=2p_{ij}(E).
\]
Because the Plücker squares sum to one and \(2s_0^2>1\), at most one pair can satisfy \(p_{ij}\ge s_0\).

**2. Reduction of the upper tail to a single Plücker coordinate.** The exact projection maximum is \(2\), attained only at coordinate two-planes (Ivanov, 2026, Theorem 1.1; already known in planar dimension). If \(0<\varepsilon<\delta_n\), every plane with \(A_n(E)\ge2-\varepsilon\) lies outside \(\mathcal K_n\), by the definition of \(b_n\). Thus it has one \(p_{ij}>s_0\), and the preceding lemma gives \(A_n(E)=2p_{ij}\). Conversely, if some \(p_{ij}\ge1-\varepsilon/2>s_0\), the same lemma gives \(A_n(E)\ge2-\varepsilon\). Hence the disjoint-event identity
\[
\{A_n(E)\ge2-\varepsilon\}
=\bigsqcup_{1\le i<j\le n}\{p_{ij}(E)\ge1-\varepsilon/2\}.
\]
This equality of events is the geometric input beyond the deterministic maximum theorem.

**3. Exact one-coordinate Plücker law.** Fix \(i<j\). Choose the orthonormal pair by first taking \(u\) uniform on \(S^{n-1}\) and then \(v\) uniform on the unit sphere of \(u^\perp\). Write \(R=\sqrt{u_i^2+u_j^2}\). Standard spherical coordinate laws give
\[
R^2\sim\operatorname{Beta}\left(1,\frac{n-2}{2}\right).
\]
For \(R>0\), the unit vector \(a=(-u_j e_i+u_i e_j)/R\) belongs to \(u^\perp\); conditional rotational invariance implies that \(Z=|\langle v,a\rangle|\) is independent of \(R\), with
\[
Z^2\sim\operatorname{Beta}\left(\frac12,\frac{n-2}{2}\right),
\qquad p_{ij}=RZ.
\]
For every integer \(k\ge0\), the beta-integral and Gamma duplication formula give
\[
\mathbb E[p_{ij}^{k}]
=\frac{\Gamma(1+k/2)\Gamma(n/2)}{\Gamma((n+k)/2)}
\frac{\Gamma((k+1)/2)\Gamma((n-1)/2)}{\sqrt\pi\,\Gamma((n+k-1)/2)}
=\frac{\Gamma(k+1)\Gamma(n-1)}{\Gamma(n+k-1)}.
\]
These are precisely the moments of \(\operatorname{Beta}(1,n-2)\). Probability measures on the compact interval \([0,1]\) are determined by their moments, so
\[
p_{ij}\sim\operatorname{Beta}(1,n-2),\qquad
\mathbb P\{p_{ij}\ge s\}=(1-s)^{n-2}\quad(0\le s\le1).
\]
The disjoint-event identity in Step 2, symmetry among all \(\binom n2\) coordinate pairs, and \(s=1-\varepsilon/2\) prove the boxed formula.

**4. Extreme-value law.** For fixed \(t\ge0\), the exact polynomial formula applies at \(\varepsilon=tN^{-1/(n-2)}\) for all sufficiently large \(N\). Independence yields
\[
\mathbb P\{N^{1/(n-2)}(2-M_{n,N})>t\}
=\left(1-\frac{c_nt^{n-2}}N\right)^N
\longrightarrow e^{-c_nt^{n-2}}.
\]
The limiting distribution has no atom at zero. Integrating survival functions gives its mean \(\Gamma(1+1/(n-2))c_n^{-1/(n-2)}\). For rigor in passing to expectations, fix \(0<\eta<\delta_n\). On \([0,\eta]\), use \((1-c_nx^{n-2})^N\le e^{-Nc_nx^{n-2}}\); on \([\eta,2]\), bound the survival probability by \((1-c_n\eta^{n-2})^N\), which is exponentially small. This gives uniform integrability at the stated scale.

## Verification

Run `python3 check.py`. The self-contained program uses only the Python standard library; it reconstructs Haar-orthonormal pairs using Gaussian Gram--Schmidt, computes planar convex-hull areas by the monotone-chain algorithm, checks the deterministic tight-frame and two-generator identities, and compares moment and high-tail frequencies with the derived formulas. It includes analytic Gamma-ratio checks in eleven dimensions and Monte Carlo comparisons in dimensions three through six (96,000 total random planes). Its finite experiments provide numerical diagnostics only; Steps 1--4 are the infinite-dimensional-quantifier proof.

## Relationship to prior work

Ivanov, *On the volume of projections of the cross-polytope* (arXiv:1808.09165, first posted 2018-08-28), already proves planar projection maximality and analyzes local extrema, including a regular-hexagon local maximizer. Ivanov, *The maximal volume of projections of the cross-polytope* (arXiv:2607.12072, first posted 2026-07-13), extends the maximum and equality classification to all projection dimensions; its equality theorem is used here. Neither inspected manuscript gives a Haar random-plane upper-tail distribution, the exact coordinate-minor reduction, or the extreme-value law. The marginal beta calculation belongs to standard spherical probability; it is not presented as a standalone newly discovered distribution. The contribution is its exact combination with the locally stable projected polygon and the resulting all-dimensional tail formula. Böröczky and Henk, *Random Projections of Regular Polytopes* (1997 preprint, Archiv der Mathematik 1999), treat the expected face counts of Haar-random projections and their high-dimensional asymptotics; the inspected preprint does not evaluate projected **area** near its maximum. Earlier extremal-projection work by Filliman (1988) is bibliographically identified but its full text was not inspected, so it remains a priority risk.

## Limitations

The positive endpoint \(\delta_n\) is defined implicitly via a compact maximum and is not evaluated or claimed optimal. No formula is claimed for the bulk or lower tail, and no analogous result is asserted for projection dimensions above two. The new theorem relies on the published equality case of Ivanov's cross-polytope projection bound; its deterministic extremal statement is not new. The numerical checks do not constitute proof of the probabilistic law or exclusion of historical equivalents. Historical priority is based on the accessible searches and inspected materials, and has not been independently adjudicated.

## References

1. G. Ivanov, *The maximal volume of projections of the cross-polytope*, arXiv:2607.12072, submitted 2026-07-13. https://arxiv.org/abs/2607.12072
2. G. Ivanov, *On the volume of projections of the cross-polytope* (also titled *Projections of the cross-polytope and related isotropic measures* in the preprint), arXiv:1808.09165, submitted 2018-08-28; Discrete Mathematics **344** (2021), 112312. https://arxiv.org/abs/1808.09165
3. P. Filliman, *The largest projections of regular polytopes*, Israel Journal of Mathematics **64** (1988), 207–228. DOI: 10.1007/BF02787224 (bibliographic reference; full text not inspected).
4. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, preprint SC 97-21 (May 1997), subsequently Archiv der Mathematik **73** (1999), 465–473. https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf
