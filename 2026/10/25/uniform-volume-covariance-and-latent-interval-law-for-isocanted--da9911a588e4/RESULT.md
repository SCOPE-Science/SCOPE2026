# Uniform-volume covariance and latent interval law for isocanted cubes

## Finding

For every integer \(d\geq2\), \(\ell>0\), and \(0<a<\ell\), put \(\delta=\ell-a\) and consider the isocanted cube
\[
K_d=\{x\in\mathbb R^d:|x_i|\le\ell/2,\quad |x_i-x_j|\le\delta\text{ for all }i,j\}.
\]
If \(X^{(d)}\) is uniformly distributed with respect to \(d\)-dimensional Lebesgue volume on \(K_d\), then \(\mathbb EX^{(d)}=0\). Write \(P_\parallel=\mathbf1\mathbf1^{\mathsf T}/d\) and \(P_\perp=I-P_\parallel\). Its complete covariance matrix is
\[
\boxed{\operatorname{Cov}(X^{(d)})=\lambda_\perp P_\perp+\lambda_\parallel P_\parallel},\qquad
\boxed{\lambda_\parallel=\frac{\ell^2+(d-1)a^2}{12}},\qquad
\boxed{\lambda_\perp=\frac{\delta^2[\delta+(d+2)a]}{12(\delta+da)}}.
\]
The transverse eigenvalue has multiplicity \(d-1\), and the diagonal eigenvalue has multiplicity one. In particular the off-diagonal covariance is strictly positive:
\[
\boxed{\operatorname{Cov}(X_i^{(d)},X_j^{(d)})=
\frac{a^2(3\delta+da)}{12(\delta+da)}}\quad(i\ne j).
\]

Define the volume-normalized isotropic constant by
\[
L(K_d)^{2d}=\frac{\det\operatorname{Cov}(X^{(d)})}{\operatorname{vol}_d(K_d)^2}.
\]
Then, exactly,
\[
\boxed{(12L(K_d)^2)^d=
\left(1+\frac{2a}{\delta+da}\right)^{d-1}
\frac{\ell^2+(d-1)a^2}{(\delta+da)^2}}.
\]
For every fixed pair \((\ell,a)\) with \(0<a<\ell\), as \(d\to\infty\),
\[
\boxed{d\log(12L(K_d)^2)+\log d\longrightarrow2},\qquad
L(K_d)\longrightarrow\frac1{\sqrt{12}}.
\]
Thus the approach to the cube isotropic constant has a universal negative logarithmic correction, despite increasingly strong covariance in the diagonal direction.

There is also a distributional explanation. Let \(T\sim\operatorname{Unif}[-a/2,a/2]\) and let \(U_1,U_2,\ldots\) be independent \(\operatorname{Unif}[-\delta/2,\delta/2]\) variables independent of \(T\). For every fixed integer \(k\ge1\) and all \(d\ge\max\{2,k\}\),
\[
\boxed{\bigl\|\mathcal L(X^{(d)}_1,\ldots,X^{(d)}_k)
-\mathcal L(T+U_1,\ldots,T+U_k)\bigr\|_{\mathrm{TV}}
\le\frac{\delta+ka}{\delta+da}}.
\]
Consequently the finite-coordinate limit is a genuinely dependent exchangeable shared-uniform-shift law. The empirical mean \(d^{-1}\sum_iX^{(d)}_i\) converges in distribution to \(T\). Under the explicit coupling in the proof, its fluctuations about the latent shift satisfy
\[
\left(T_d,\sqrt d\left[d^{-1}\sum_{i=1}^dX^{(d)}_i-T_d\right]\right)
\Longrightarrow(T,G),\quad G\sim N(0,\delta^2/12),\quad G\perp T.
\]

## Assumptions and scope

The Euclidean metric and Lebesgue probability are the ordinary standard-coordinate ones, not Gaussian directional sampling. The parameters \(\ell,a\) are fixed in all high-dimensional statements, with \(0<a<\ell\); there is no claim of uniformity when the cant varies with dimension. The total-variation inequality is meaningful for any integer \(1\le k\le d\). The previous exact volume formula is used and independently recovered below. It is not presented as new.

## Proof

**1. Geometric decomposition.** Set \(C=[-\delta/2,\delta/2]^d\), \(\mathbf1=(1,\ldots,1)\), and \(Z=C+[0,a]\mathbf1\). The known Minkowski representation gives \(K_d=Z-(a/2)\mathbf1\). For each \(j\), let \(F_j=\{u\in C:u_j=\delta/2\}\). There is an almost-everywhere disjoint decomposition
\[
Z=C\;\dot\cup\;\bigcup_{j=1}^{d}(F_j+[0,a]\mathbf1).
\]
To prove coverage, for \(z\in Z\) set \(t_0=\max\{0,\max_i(z_i-\delta/2)\}\). If \(t_0=0\), then \(z\in C\); otherwise \(z-t_0\mathbf1\in C\), and every index where \(z_i\) is maximal supplies an upper facet. Apart from coordinate-maximum ties (a null set), the index is unique. Each swept facet is parametrized by \(t\in[0,a]\), \(u_i\in[-\delta/2,\delta/2]\) for \(i\ne j\), with \(z_j=\delta/2+t\), \(z_i=u_i+t\). This triangular Jacobian has absolute determinant one. Thus the central cube has volume \(\delta^d\) and each wing has volume \(a\delta^{d-1}\), yielding
\[
\operatorname{vol}_d(K_d)=\delta^{d-1}(\delta+da).
\]

**2. Exact sampling mixture.** Equivalently, sample a label \(J\in\{0,1,\ldots,d\}\) with probabilities
\[
\Pr(J=0)=\frac\delta{\delta+da},\qquad
\Pr(J=j)=\frac a{\delta+da}\quad(1\le j\le d).
\]
If \(J=0\), draw independent \(U_i\sim\operatorname{Unif}[-\delta/2,\delta/2]\) and put \(X_i=U_i-a/2\). If \(J=j>0\), draw an independent \(T\sim\operatorname{Unif}[-a/2,a/2]\), draw independent \(U_i\sim\operatorname{Unif}[-\delta/2,\delta/2]\) for \(i\ne j\), and put
\[
X_j=T+\delta/2,\qquad X_i=T+U_i\quad(i\ne j).
\]
The Jacobian and equal-volume calculations above prove this is the exact uniform-volume law. Directly, every coordinate has mean \(-a\delta/[2(\delta+da)]+a\delta/[2(\delta+da)]=0\).

**3. Second moments.** In the central tile the second moments are \(\mathbb E X_i^2=\delta^2/12+a^2/4\) and \(\mathbb EX_iX_j=a^2/4\) for distinct indices. In wing \(j\), the special coordinate has second moment \(\delta^2/4+a^2/12\); an ordinary coordinate has second moment \(\delta^2/12+a^2/12\). Every distinct-coordinate cross moment in a wing is \(a^2/12\). Weighting these expressions gives
\[
\mathbb EX_iX_j=\frac{a^2(3\delta+da)}{12(\delta+da)}\quad(i\ne j),
\]
\[
\mathbb EX_i^2-\mathbb EX_iX_j=
\frac{\delta^2[\delta+(d+2)a]}{12(\delta+da)}.
\]
The covariance is invariant under coordinate permutations, so these determine the two orthogonal eigenspaces. Adding \(d\) times the cross moment to the transverse eigenvalue gives the asserted diagonal eigenvalue after cancellation.

**4. Isotropic scale.** The determinant is \(\lambda_\parallel\lambda_\perp^{d-1}\). Substitution together with the recovered volume yields the exact formula. For fixed \(a>0\), the logarithm of its right-hand side is
\[
(d-1)\log\left(1+\frac{2a}{\delta+da}\right)
+\log(\ell^2+(d-1)a^2)-2\log(\delta+da)
=2-\log d+o(1).
\]
This proves the asserted logarithmic correction and the limiting cube isotropic constant. No asymptotic transfer beyond fixed positive cant is used.

**5. Finite marginals and empirical mean.** Couple the exact mixture with independent \(T,U_1,\ldots,U_k\) having the distributions stated above. On the event \(J\in\{k+1,\ldots,d\}\), the first \(k\) coordinates coincide with \((T+U_1,\ldots,T+U_k)\); its complement has probability \((\delta+ka)/(\delta+da)\), proving the total-variation bound. For \(d\to\infty\), the central-label probability tends to zero. On a wing, with independent latent \(T_d=T\),
\[
\frac1d\sum_iX_i-T_d=\frac{\delta}{2d}+\frac1d\sum_{i\ne J}U_i.
\]
The classical independent-uniform central limit theorem implies the stated joint limit, with independence from \(T\). The event \(J=0\) has vanishing probability, so it does not affect convergence; there define \(T_d\) as an arbitrary independent uniform latent variable. The empirical-mean limit follows.

## Verification

The standalone `verify.py` uses only Python's standard library. It verifies exact rational covariance identities and exact isotropic determinant identities for 76 dimension-parameter profiles, plus four independent two-dimensional polygon moment integrals using exact rational triangulation. These calculations do not assume the proposed second-moment formulas. It additionally draws uniform points by rejection directly from the defining inequalities (not from the decomposition) in dimensions two, three, and four, comparing their covariance entries with the theorem. Finally, it checks numerical convergence of the logarithmic correction at dimensions \(10^3,10^4,10^5\). Execute `python3 verify.py`; the last line is `VERIFY_OK exact_profiles 80 rejection_dimensions 3`.

## Relationship to prior work

De la Puente and Clavería introduced this family and its zonotope representation and obtained its combinatorial invariants [1]. Their subsequent paper proves the scalar Euclidean volume determinant and the dual volume formula [2]. Both the zonotope representation and volume are treated here as established background, not new results. A later paper [3] addresses lower-dimensional face volumes, incidence numbers and tiling symmetries. The present statement instead concerns the *uniform interior probability law*, its complete second-moment tensor, an affine-invariant isotropic correction, and dependent high-dimensional finite-coordinate limits. A separate spherical-directional-width analysis concerns support functions, not volume-uniform point distributions. Standard facts about uniform order statistics may offer alternative routes to the mixture argument; the unverified possibility of equivalent conditional-range formulas is a bibliographic limitation.

## Limitations

The formulas depend on the stated standard Euclidean realization, although the isotropic constant itself is affine invariant. The universal logarithmic limit assumes fixed \(0<a<\ell\), and does not cover a cant tending to zero or to the full edge length. The numerical experiments verify finite cases, not the asymptotic theorem. No assertion is made that the underlying volume identity, the zonotope tiling, or the independent-uniform central limit theorem is new. A related 2025 article was available at abstract level only during the comparison, and equivalent statements from conditional range-constrained uniform sampling are not categorically ruled out. Independent review remains outstanding.

## References

[1] M. J. de la Puente and P. L. Clavería, *Isocanted alcoved polytopes*, arXiv:2009.13858 (first publicly posted 2020-09-29), Applications of Mathematics **65** (2020), 703–726, DOI:10.21136/AM.2020.0373-19.

[2] M. J. de la Puente and P. L. Clavería, *The volume of an isocanted cube is a determinant*, arXiv:2406.01565 (first publicly posted 2024-06-03), DOI:10.1080/03081087.2024.2368240.

[3] M. J. de la Puente, *Isocanted cube: the lower Lebesgue volumes, incidence numbers and symmetries of this d-dimensional tile*, Extracta Mathematicae **40** (2025), 1–26, DOI:10.17398/2605-5686.40.1.1.
