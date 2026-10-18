# Sharp simplex gap between projected Gaussian convex order and Gaussian-block certificates

## Finding

Let \(d\ge2\), let \(v_1,\ldots,v_{d+1}\) be the unit vertices of a centred regular simplex in \(\mathbb R^d\), and set
\[
X_s\sim N_d(0,s^2I_d),\qquad
\mathcal L(Y)=\frac1{d+1}\sum_{i=1}^{d+1}N_d(0,v_iv_i^{\mathsf T}),\quad s\ge0.
\]
The following **two exactly determined thresholds are distinct**:

1. Every one-dimensional linear projection of \(X_s\) is dominated in scalar convex order by the same projection of \(Y\) if and only if
\[
0\le s\le s_{\mathrm{proj}}=\sqrt{\frac{2}{d(d+1)}}.
\]
2. There exists a jointly Gaussian coupling \((Z_1,\ldots,Z_{d+1})\), with individual laws \(N_d(0,v_iv_i^{\mathsf T})\), whose arithmetic mean has covariance dominating \(s^2I_d\), if and only if
\[
0\le s\le s_{\mathrm{block}}=\frac1d.
\]
The coupling attaining \(s_{\mathrm{block}}\) has **unique scalar correlation matrix** \(C_{ij}=v_i\cdot v_j\). Consequently, the ratio of the thresholds is exactly
\[
\frac{s_{\mathrm{proj}}}{s_{\mathrm{block}}}=\sqrt{\frac{2d}{d+1}}>1
\qquad(d\ge2),
\]
and increases to \(\sqrt2\). In the nonempty interval \(1/d<s\le\sqrt{2/[d(d+1)]}\), every projected test passes but the Gaussian-block Jensen certificate is impossible.

This is a separation between a **necessary projected criterion** and one **sufficient Gaussian-coupling certificate**. It is **not** a proof that multivariate convex order itself fails anywhere in that interval.

## Assumptions and scope

Fix an integer \(d\ge2\), write \(n=d+1\), and choose vectors satisfying
\[
\|v_i\|=1,\quad v_i\cdot v_j=-1/d\ (i\ne j),\quad
\sum_i v_i=0,\quad \sum_i v_iv_i^{\mathsf T}=(n/d)I_d.
\]
These identities characterize a centred regular unit simplex up to an orthogonal transformation. All Gaussian laws are centred; the component covariances have rank one. For integrable real laws with equal means, scalar convex order means comparison of expectations of every convex function. The **Gaussian-block certificate** is the existence of a joint centred Gaussian vector with the prescribed marginal covariance blocks and \(\operatorname{Cov}(n^{-1}\sum_i Z_i)\succeq s^2I_d\). By Gaussian covariance comparison followed by Jensen's inequality, this condition implies \(X_s\le_{\mathrm{cx}}Y\) in multivariate convex order; the converse is not asserted.

## Proof

**Step 1: the scalar comparison lemma.** Let \(p_i>0\) sum to one, and let \(r_i\ge0\). For a standard normal \(G\), the law \(\sum_i p_iN(0,r_i^2)\) is that of \(RG\), where \(R\) is independent of \(G\) and takes value \(r_i\) with probability \(p_i\). If \(t\le\mathbb ER\), Gaussian variance comparison and conditional Jensen yield
\[
N(0,t^2)\le_{\mathrm{cx}}N(0,(\mathbb ER)^2)\le_{\mathrm{cx}}\mathcal L(RG).
\]
Conversely, applying the convex test \(x\mapsto|x|\) gives \(t\le\mathbb ER\). Thus this condition is necessary and sufficient, including at zero and at equality.

**Step 2: exact minimum of projected absolute norms.** For a unit direction \(u\), the preceding lemma gives the precise condition
\[
s\le\frac1n\sum_{i=1}^n|u\cdot v_i|.
\]
Put \(a_i=u\cdot v_i\). Then \(\sum_i a_i=0\) and \(\sum_i a_i^2=n/d\). For any real zero-sum list, let \(T\) be its common total positive and total absolute negative mass. Each positive or negative squared sub-sum is at most \(T^2\), so
\[
\sum_i a_i^2\le2T^2=\frac12\left(\sum_i|a_i|\right)^2.
\]
This implies \(n^{-1}\sum_i|a_i|\ge\sqrt{2/(dn)}\). Equality is attained: prescribe \(a=(c,-c,0,\ldots,0)\) with \(c=\sqrt{n/(2d)}\); the map \(u\mapsto(u\cdot v_i)_i\) is an isomorphism of \(\mathbb R^d\) onto the zero-sum hyperplane, scaled in squared norm by \(n/d\). Hence there exists a unit \(u\) with exactly those projections. Both necessity and sufficiency follow for every direction; scaling handles nonunit directions.

**Step 3: an exact trace obstruction for all joint Gaussian couplings.** Since the covariance of \(Z_i\) has rank one, \(Z_i=v_i g_i\) almost surely for standard normal scalars \(g_i\). Their joint scalar correlation matrix \(C=(\mathbb E g_ig_j)\) is positive semidefinite with \(C_{ii}=1\). The regular-simplex Gram relations give
\[
\operatorname{tr}\operatorname{Cov}\left(\frac1n\sum_i Z_i\right)
=\frac1{n^2}\sum_{i,j}C_{ij}(v_i\cdot v_j)
=\frac{n^2-\mathbf1^{\mathsf T}C\mathbf1}{dn^2}\le\frac1d.
\]
Therefore the smallest eigenvalue is at most \(1/d^2\), and a certificate with covariance at least \(s^2I_d\) forces \(s\le1/d\).

**Step 4: attainability and rigidity.** Take \(G\sim N_d(0,I_d)\), set \(g_i=v_i\cdot G\), and \(Z_i=v_i g_i\). They have the required marginal laws, and
\[
\frac1n\sum_i Z_i=\frac1n\sum_i v_iv_i^{\mathsf T}G=\frac1dG.
\]
Thus covariance \(I_d/d^2\) is attained and every smaller \(s\) is certified.

Suppose any coupling attains the endpoint, meaning its barycentre covariance dominates \(I_d/d^2\). Equality in the trace bound forces both \(C\mathbf1=0\) (since \(C\succeq0\)) and covariance exactly \(I_d/d^2\). Write \(V=[v_1\ \cdots\ v_n]\) and \(P=I_n-\mathbf1\mathbf1^{\mathsf T}/n\). Then \(V^{\mathsf T}V=(n/d)P\) and \(C=PCP\). From \(VCV^{\mathsf T}/n^2=I_d/d^2\), multiplication on the left and right by \(V^{\mathsf T}\), \(V\) gives \(C=(n/d)P=V^{\mathsf T}V\), the unique endpoint scalar correlation matrix. Every assertion follows.

## Verification

Run `python code/verify.py` using Python 3 without third-party dependencies. The checker uses exact rational arithmetic in dimensions \(2,3,\ldots,14,20,33,64\); it checks the simplex Gram identities, scaled projection identity, barycentre covariance identity, trace formula for three explicit correlation matrices, and strict threshold separation. Its expected output starts with `PASS: 21552 exact identities`. These are finite diagnostics, not an exhaustive proof across all dimensions. The algebraic proof above supplies that quantification.

## Relationship to prior work

Jourdain and Pagès (arXiv:2410.07958, first posted 10 October 2024) formulated intrinsic necessary projection inequalities and sufficient Gaussian-block conditions for convex comparisons with mixtures. Guéant (arXiv:2610.07404v1, first posted 5 October 2026) proves equivalence of projected and full convex order for two centred Gaussian components and explicitly leaves the larger-mixture case open; its Section 1.4 states the coupling condition and its Section 4 distinguishes the unsolved three-or-more-component case. Our result derives exact, dimension-dependent projection and block-*certificate* thresholds for a separate, uniform regular-simplex mixture with \(d+1\ge3\) rank-one components, including uniqueness of the extremizing coupling. It neither extends Guéant's two-component equivalence nor settles actual multivariate convex order.

A later unrefereed three-component construction, *Projection tests fail for three centred Gaussian components* (Evidence Press, 10 October 2026, version 1.1.0-candidate), proves a different full-order counterexample using unequal weights and asymmetric component directions. Its inspected manuscript does not study this equal-weight regular-simplex all-dimensional exact threshold or optimizer rigidity. Classical zero-sum norm inequalities and simplex frame identities underlie the proof and are not claimed as new independently.

## Limitations

The Gaussian-block condition is sufficient, not known to be necessary when more than two mixture components are present. Failure of that certificate, even with all projected tests passing, is **not** a multivariate stochastic-order counterexample. Gaussian couplings are deliberately required jointly normal, and the result is not a statement about arbitrary nonlinear or non-Gaussian martingale couplings. It applies only to uniform mixtures of \(d+1\) rank-one unit-simplex components and isotropic centred Gaussian targets, not to arbitrary component covariances or weights. The exact thresholds have an elementary proof; priority relative to unindexed literature cannot be absolutely excluded.

## References

1. B. Jourdain and G. Pagès, *Convex comparison of Gaussian mixtures*, arXiv:2410.07958 (first posted 10 October 2024); *Journal of Multivariate Analysis* **209** (2025), 105448.
2. O. Guéant, *Convex Order Beyond Dimension One: Projection Tests, Counterexamples and Gaussian Mixtures*, arXiv:2610.07404v1 (first posted 5 October 2026), especially Sections 1.4, 3, and 4.
3. *Projection tests fail for three centred Gaussian components*, unrefereed manuscript, Evidence Press version 1.1.0-candidate (10 October 2026), DOI: 10.5281/zenodo.23284191; accessible source at https://github.com/ipitchford/three-gaussian-projection-counterexample/blob/main/paper.tex.
