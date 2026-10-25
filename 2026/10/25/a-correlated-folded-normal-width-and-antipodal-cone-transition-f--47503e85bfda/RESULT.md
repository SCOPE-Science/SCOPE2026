# A correlated folded-normal width and antipodal-cone transition for two-level chain polytopes

## Finding

Consider the chain polytope \(P_{p,q}\) of the complete two-level poset with \(p\) lower and \(q\) upper elements. The central geometric result is a **joint width–antipodal-normal-fan limit**: if \(n=p+q\to\infty\) and \((p-q)/\sqrt n\to t\in\mathbb R\), the centered directional width and the two exposed vertex classes converge together to a law built from one independent Gaussian and two **negatively correlated folded Gaussians**.

Set
\[
\mu=\frac1{\sqrt{2\pi}},\qquad
\sigma^2=\frac{\pi-1}{2\pi},\qquad
\rho=-\frac1{\pi-1}.
\]
Let \((Z_+,Z_-)\) be a centered standard bivariate Gaussian of correlation \(\rho\), and \(Y\) be an independent Gaussian of variance \((1-3/\pi)/4\). Put \(T_\pm=\mu t+\sigma Z_\pm\). If \(U_n\) is a uniformly random ambient Euclidean unit vector and \(W_n\) is the width of \(P_{p,q}\) along \(U_n\), then
\[
\boxed{\left(W_n-\mu\sqrt n,\mathbf1\{J_+=1\},\mathbf1\{J_-=1\}\right)
\ \Longrightarrow\ 
\left(Y+\frac{|T_+|+|T_-|}{2},\mathbf1\{T_+>0\},\mathbf1\{T_->0\}\right).}
\]
Here \(J_+\) and \(J_-\) label the parts containing the vertices exposed by \(U_n\) and \(-U_n\), respectively, with any fixed tie convention on the vanishing-probability origin event specified below.

The spherical probability of **same-part antipodal exposure** therefore tends to
\[
F(t)=\Phi_2(a,a;\rho)+\Phi_2(-a,-a;\rho),\qquad a=\mu t/\sigma,
\]
where \(\Phi_2\) is the standard bivariate Gaussian cumulative distribution function with correlation \(\rho\). In the balanced case,
\[
\boxed{F(0)=\frac12-\frac1\pi\arcsin\frac1{\pi-1}=0.345355605927424\ldots.}
\]
It is even and strictly increasing for positive \(t\), approaches one as \(|t|\to\infty\), and also tends to one along any sequence with \(|p-q|/\sqrt n\to\infty\). The critical geometric imbalance scale is \(|p-q|\asymp\sqrt n\). For every finite \(t\), the centered-width limit is non-Gaussian.

## Assumptions and scope

Let \(p,q\) be positive integers, \(n=p+q\), and let \(A_p\oplus A_q\) denote the ordinal sum of two antichains: every first-level element is less than every second-level element. Its standard chain polytope is
\[
P_{p,q}=\{(x,y)\in\mathbb R_{\ge0}^p\times\mathbb R_{\ge0}^q:\ x_i+y_j\le1\text{ for every }1\le i\le p,1\le j\le q\}.
\]
It is the convex hull of coordinate indicator vectors of arbitrary subsets entirely contained within either level, including the common empty subset; equivalently it is the stable-set polytope of the complete bipartite graph \(K_{p,q}\). For completeness, given any point in the inequality description, put \(a=\max_i x_i\) and \(b=\max_j y_j\); then \(a+b\le1\). It decomposes as \(a(x/a,0)+b(0,y/b)+(1-a-b)0\), omitting a zero-weight term if necessary. The nonzero normalized vectors belong to unit coordinate cubes, each of which is the convex hull of its zero-one indicator vectors; this proves the hull description without invoking integrality. The polytope is full-dimensional in the **unweighted ambient Euclidean metric** \(\mathbb R^n\). It is not an orthogonal or volume-preserving re-embedding of a different realization.

For any compact convex \(K\subset\mathbb R^n\), let \(h_K(u)=\max_{x\in K}\langle u,x\rangle\) and let \(W_K(u)=h_K(u)+h_K(-u)\) for \(\|u\|_2=1\). For generic directions, the maximizing vertices are unique. Their level labels are \(J_+,J_-\in\{1,2\}\); if either exposed vertex equals the origin, set the corresponding label to \(2\) by convention. This exceptional event has total spherical probability \(2^{1-n}\), and thus does not influence the limits. The normal cones themselves retain their usual geometric definition; the class-label probabilities are sums of spherical measures of their antipodal intersections.

## Proof

**1. Exact finite-dimensional Gaussian width identity.** Let \(G=(G_1,\ldots,G_n)\) have independent standard normal coordinates, and put \(U=G/\|G\|_2\). For real \(s\), write \(s_+=\max(s,0)\). Define
\[
A_+=\sum_{i\le p}(G_i)_+,\quad B_+=\sum_{i>p}(G_i)_+,\quad
A_-=\sum_{i\le p}(-G_i)_+,\quad B_-=\sum_{i>p}(-G_i)_+,\quad D_\pm=A_\pm-B_\pm.
\]
Because every stable set belongs entirely to one level, optimization over its indicator vector gives
\[
h_{P_{p,q}}(G)=\max(A_+,B_+),\qquad h_{P_{p,q}}(-G)=\max(A_-,B_-).
\]
Applying \(\max(a,b)=(a+b+|a-b|)/2\) twice yields the **exact identity**
\[
\boxed{W_{P_{p,q}}(U)=\frac{\sum_{i=1}^n|G_i|+|D_+|+|D_-|}{2\sqrt{\sum_{i=1}^nG_i^2}}.}\tag{1}
\]
Except when all \(G_i\) are negative, the maximizing level for \(G\) is level one if and only if \(D_+>0\). Except when all \(G_i\) are positive, the maximizing level for \(-G\) is level one if and only if \(D_->0\). These two exceptional events are disjoint and each has probability \(2^{-n}\). Ties at other directions have spherical measure zero.

**2. A bivariate central limit law.** For \(g\sim N(0,1)\),
\[
\mathbb E(g)_+=\mu,\quad\operatorname{Var}((g)_+)=\sigma^2=\frac12-\mu^2,\quad\operatorname{Cov}((g)_+,(-g)_+)=-\mu^2.
\]
Consequently the exact mean and covariance relations for every \(p,q\) are
\[
\mathbb ED_\pm=\mu(p-q),\quad\operatorname{Var}D_\pm=n\sigma^2,\quad\operatorname{Cov}(D_+,D_-)=-n\mu^2.
\]
The multivariate central limit theorem, together with \((p-q)/\sqrt n\to t\), gives
\[
\left(\frac{D_+}{\sqrt n},\frac{D_-}{\sqrt n}\right)
\Longrightarrow (T_+,T_-),\qquad \operatorname{Corr}(T_+,T_-)=\rho=-\frac{\mu^2}{\sigma^2}=-\frac1{\pi-1}.
\tag{2}
\]
In particular this negative correlation survives at every finite imbalance parameter.

**3. Independence from the radial cube fluctuation.** Set \(M_n=\sum_i|G_i|\) and \(Q_n=\sum_iG_i^2\). The joint central limit theorem for
\[
\left(\frac{M_n-2\mu n}{\sqrt n},\frac{Q_n-n}{\sqrt n},\frac{D_+-\mu(p-q)}{\sqrt n},\frac{D_--\mu(p-q)}{\sqrt n}\right)
\]
shows that the first two limiting coordinates are independent of the last two: the respective cross-covariances equal a fixed one-coordinate covariance multiplied by \((p-q)/n\to0\). This follows because the second level enters \(D_\pm\) with opposite sign, while \(|G_i|\) and \(G_i^2\) have the same distribution in both levels. More explicitly,
\[
\operatorname{Cov}(|g|,(g)_+)=\frac12-2\mu^2,\quad
\operatorname{Cov}(g^2,(g)_+)=\mu,
\]
and the same formulas hold with \((-g)_+\).

The delta method at \((\mathbb E|g|,\mathbb Eg^2)=(2\mu,1)\) yields
\[
\frac{M_n}{2\sqrt{Q_n}}-\mu\sqrt n\Longrightarrow Y,
\quad\operatorname{Var}(Y)=\frac14\left(1-\frac3\pi\right).
\tag{3}
\]
For completeness, the gradient is \((1/2,-\mu/2)\) with respect to fluctuations of \((M_n/n,Q_n/n)\); using \(\operatorname{Var}|g|=1-4\mu^2\), \(\operatorname{Var}g^2=2\), and \(\operatorname{Cov}(|g|,g^2)=2\mu\) gives exactly the displayed variance. The limiting \(Y\) is independent of \((Z_+,Z_-)\).

Since \(Q_n/n\to1\) almost surely, the continuous mapping theorem applied to (1)–(3) proves the joint width-and-level assertion. No finite numerical test substitutes for this infinite-dimensional argument.

**4. Antipodal angular transition.** Away from the exponentially rare origin events, the two exposed vertices lie in the same level if and only if \(D_+D_->0\). The bivariate Gaussian limit in (2) has no mass on either coordinate axis, so the portmanteau theorem gives
\[
\Pr\{J_+=J_-\}\to\Pr\{T_+T_->0\}=\Phi_2(a,a;\rho)+\Phi_2(-a,-a;\rho).
\]
The centered Gaussian orthant identity yields \(F(0)=1/2+\pi^{-1}\arcsin\rho\). Differentiating the bivariate Gaussian distribution along the diagonal gives, for \(a>0\),
\[
\frac{dF}{da}=2\varphi(a)\left[2\Phi\left(\frac{a(1-\rho)}{\sqrt{1-\rho^2}}\right)-1\right]>0,
\]
so the transition is strictly monotone in positive \(t\) and even in \(t\). Gaussian tail convergence implies \(F(t)\to1\) as \(|t|\to\infty\). Without assuming finite \(t\), if \(|p-q|/\sqrt n\to\infty\), each \(D_\pm\) has mean \(\mu(p-q)\) and variance \(n\sigma^2\), so Chebyshev's inequality and a union bound show that both differences have the same sign with probability tending to one.

**5. Genuine non-Gaussianity.** For finite \(t\), \((|T_+|+|T_-|)/2\) is nonnegative, nonconstant, and independent of the nondegenerate normal \(Y\). If their sum were Gaussian, Cramér's decomposition theorem would force the nonnegative nonconstant summand to be Gaussian, which is impossible. Thus the full width limit is not normal. The normal-fan asymmetry is not a generic restatement of the standard cube central limit theorem.

## Verification

A standalone reproducibility script (`check.py`) exhaustively lists all candidate stable sets for each of 864 independently generated small-dimensional Gaussian directions (all two-level splits in dimensions 2 through 9), checking both the support maximum and exact identity (1). It also evaluates the bivariate normal integral for \(F(t)\), verifies the arcsine reduction at balance, and compares 25,000 random directions for each of three imbalance regimes in dimension 1,400 with the limiting first two width moments and same-level exposure probability. Its captured output is in `verification_output.txt`. The script uses NumPy and SciPy and is independent of any unpublished data or other package.

The finite checks verify identities only on tested vectors; the infinite asymptotic assertion follows from the explicit proof above and is not claimed to be computationally certified.

## Relationship to prior work

Ahmad–Fourier–Joswig study order and chain polytopes of maximal ranked posets, establishing their combinatorial structure and face comparisons (arXiv:2309.01626, initially public 2023-09-04). Aliniaeifard–Benedetti–Bergeron–Li–Saliola treat stable-set polytopes and their edges (arXiv:1804.00360, 2018). Kabluchko–Litvak–Zaporozhets establish Gaussian methods and the classical centered random-width central limit theorem for regular cubes (arXiv:1511.08479, 2015). Their cube theorem supplies a compatible **marginal** Gaussian term but does not give the joint law of the two level-exposure indicators or the correlated folded-normal correction.

An earlier complete-multipartite stable-set calculation of **mean width**, including the elementary two-block folded-normal expectation, is acknowledged as prior. Mean-width formulas do not determine full directional-width distributions, negative dependence of the two antipodal exposed classes, the balanced arcsine value, or their joint limiting law. Related work on Euclidean inballs, enclosing spheres, John ellipsoids, and inertia of these polytopes concerns different geometric invariants. The present result does **not** claim novelty for the support-function decomposition alone, standard Gaussian central limit methods, or the two-block mean width.

## Limitations

The theorem concerns the precise canonical ambient Euclidean embedding, not arbitrary affine transformations or intrinsically renormalized versions. It assumes Gaussian/Haar-uniform random directions; it does not address non-isotropic directional measures. The central folded-normal joint limit requires a finite square-root-scale imbalance \(t\); the separately proved large-imbalance statement concerns only the same-level probability, not a centered-width law in that regime. A literature search cannot exclude unindexed equivalent Gaussian order-statistic or random-optimization treatments, so bibliographic novelty remains subject to independent expert assessment. No independent mathematical audit or validation is asserted.

## References

1. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626 (first public version September 4, 2023), https://arxiv.org/abs/2309.01626.
2. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (2018), https://arxiv.org/abs/1804.00360.
3. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (2015), https://arxiv.org/abs/1511.08479.
