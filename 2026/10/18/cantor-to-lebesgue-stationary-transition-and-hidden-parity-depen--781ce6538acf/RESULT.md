# Cantor-to-Lebesgue stationary transition and hidden parity dependence in a stochastic border-collision map

## Finding

For the stochastic planar border-collision recurrence described below, a single parameter \(d\in(0,1)\) controls a sharp transition in the *support* of the unique stationary measure. In the same system, first-coordinate observations have zero covariance at every nonzero lag, yet their joint laws alternate between exact independence at odd lags and mutual singularity with the independent law at every positive even lag.

Write \(B=\mu/(1-d)\), \(A=\mu(1-2d)/(1-d)\), and \(I=[A,B]\). Let \(K_d\) be the unique compact set satisfying
\[
K_d=(\mu+dK_d)\cup(\mu-dK_d).
\]
The unique invariant probability \(\pi_d\) of the random planar map has support
\[
\operatorname{supp}\pi_d=K_d\times d(K_d\cup(-K_d)).
\]
For \(0<d<1/2\), its support is a separated Cantor product of Hausdorff dimension
\[
\dim_H(\operatorname{supp}\pi_d)=\frac{2\log 2}{\log(1/d)}.
\]
For \(1/2\le d<1\), its support is the complete rectangle
\[
I\times[-dB,dB].
\]
Exactly at \(d=1/2\), \(\pi_{1/2}\) is normalized two-dimensional Lebesgue measure on \([0,2\mu]\times[-\mu,\mu]\), with density \(1/(4\mu^2)\).

If \((X_n,Y_n)_{n\in\mathbb Z}\) is the stationary process, then for every integer \(k\ge1\),
\[
\operatorname{Cov}(X_0,X_k)=0,
\qquad
\left\|\mathcal L(X_0,X_k)-\mathcal L(X_0)^{\otimes2}\right\|_{\mathrm{TV}}
=\begin{cases}0,&k\text{ odd},\\1,&k\text{ even}.\end{cases}
\]
Here \(\|P-Q\|_{\mathrm{TV}}=\sup_E|P(E)-Q(E)|\). Equivalently, the pair mutual information is zero at every odd lag and infinite at every positive even lag. The even-lag dependence is visible to a quadratic statistic:
\[
\operatorname{Cov}\bigl(X_0^2,(X_{2k}-\mu)^2\bigr)=d^{2k}\operatorname{Var}(X_0^2)>0.
\]
In particular, at the Lebesgue critical point the right-hand side is \(64\mu^4/(45\cdot4^k)\).

## Assumptions and scope

Fix \(\mu>0\), \(0<d<1\), and \(h>\mu/(1-d)\). Independently at each integer time, select a switching threshold \(\xi_n\in\{-h,h\}\) with both values equally likely. In the planar stochastic border-collision normal form of Glendinning [1], take trace parameters \(T_0=T_1=0\) and determinant parameters \(D_0=-d\), \(D_1=d\), so the branches are
\[
F_0(x,y)=(\mu+y,dx),\qquad F_1(x,y)=(\mu+y,-dx).
\]
Use branch zero when \(x<\xi_n\) and branch one when \(x\ge\xi_n\). A stationary probability means invariant under the Markov kernel obtained by averaging over the independent threshold at each step. The process is considered in its unique two-sided stationary realization. The conclusions concern this exact high-noise, symmetric two-point-threshold subfamily; they are not asserted for uniform noise, unequal traces, or deterministic switching.

## Proof

**1. Entry into the fair-switching region.** Whichever branch is chosen, \(X_{n+1}=\mu+Y_n\) and \(|Y_{n+1}|=d|X_n|\). Consequently
\[
|X_{n+2}|\le\mu+d|X_n|.
\]
Both parity subsequences therefore eventually lie in \((-h,h)\) for every finite initial condition, because their deterministic upper bounds approach \(B=\mu/(1-d)<h\). Once inside the strip, the threshold \(+h\) selects branch zero and \(-h\) selects branch one, independently of the state. Thus after a finite initial transient, \(\sigma_n\) are independent fair signs in
\[
X_{n+1}=\mu+Y_n,\qquad Y_{n+1}=\sigma_n dX_n,
\qquad X_{n+2}=\mu+\sigma_n dX_n.
\]
Two successive planar maps have linear part \(\operatorname{diag}(\sigma_nd,\sigma_{n+1}d)\), a Euclidean contraction by \(d\). This gives unique stationary distribution and weak convergence to it from every deterministic finite initial point. For an arbitrary stationary probability, applying the displayed deterministic bound at time \(2m\) and taking \(m\to\infty\) forces \(|X|\le B\) almost surely; hence every stationary probability lies in the fair-switching regime. The stationary measure is therefore globally unique, not merely unique within a nominated trapping set.

**2. Product law and supports.** The scalar random affine contractions \(f_\pm(t)=\mu\pm dt\) admit a unique stationary probability \(\nu_d\), satisfying
\[
\nu_d=\tfrac12(f_+)_*\nu_d+\tfrac12(f_-)_*\nu_d.
\]
The stationary even and odd coordinate subsequences use disjoint sets of past signs and are independent. Equivalently, direct substitution into the transition kernel shows that
\[
\pi_d=\nu_d\otimes\left[\tfrac12(d\cdot)_*\nu_d+\tfrac12(-d\cdot)_*\nu_d\right]
\]
is invariant, hence is the unique stationary law. Its support is the claimed product.

The scalar interval \(I=[A,B]\) is invariant under both \(f_\pm\), with
\[
f_-(I)=[A,\mu-dA],\qquad f_+(I)=[\mu+dA,B].
\]
If \(d<1/2\), then \(A>0\), the intervals have a positive gap, and the two-map self-similar attractor \(K_d\) satisfies the strong separation condition. The elementary self-similar dimension calculation gives \(\dim_H K_d=\log2/\log(1/d)\); the disjoint reflected copy in the second coordinate gives the doubled dimension for the product (the separated self-similar measure supplies matching product mass bounds). If \(d\ge1/2\), then \(A\le0\), the two image intervals cover \(I\), and uniqueness of the compact attractor forces \(K_d=I\). Since \(|A|\le B\), its reflected union covers \([-B,B]\), giving the full rectangle support.

At \(d=1/2\), \(I=[0,2\mu]\) and the two images are exactly \([0,\mu]\) and \([\mu,2\mu]\). Uniform measure on \(I\) is invariant for the scalar maps, and therefore equals \(\nu_{1/2}\). The reflected, scaled mixture is uniform on \([-\mu,\mu]\). Their product is the stated planar Lebesgue law.

**3. Nonatomic marginal.** For \(\mu>0\) and \(d>0\), the stationary scalar measure \(\nu_d\) has no atoms. Otherwise select the finite set of atoms of maximal positive mass \(M\) (the maximum exists for any atomic probability). Stationarity and the fair two-branch weights force the preimage of each maximal atom under *both* injective contractions to be another maximal atom. Both inverse maps hence permute the finite maximal-atom set. A strict contraction cannot permute a finite set containing two different points, so the set is a singleton fixed by both \(f_+\) and \(f_-\). These maps have distinct fixed points, \(\mu/(1-d)\) and \(\mu/(1+d)\), a contradiction.

**4. The parity-dependent two-point laws.** In the bi-infinite stationary representation, \(X_n\) is a function only of signs with indices \(n-2,n-4,\ldots\). For odd \(k\), the signs defining \(X_{n+k}\) have the other index parity, so the observations are exactly independent. For even \(k=2j\), the scalar recursion gives
\[
X_{n+2j}=g_{\sigma_n,\sigma_{n+2},\ldots,\sigma_{n+2j-2}}(X_n),
\]
where each \(g\) is an affine function and there are at most \(2^j\) possible such functions. Thus the pair law is concentrated on a finite union of graphs. Because \(\nu_d\) is nonatomic, the product measure \(\nu_d\otimes\nu_d\) assigns zero mass to that union. The joint law and the product are mutually singular, yielding total variation one and infinite Kullback--Leibler divergence. For odd lags they agree exactly, so total variation and mutual information both vanish.

The fair-sign recursion gives \(\mathbb E[X_{n+2}\mid X_n]=\mu\) and the same conditional mean at every larger positive even lag, so all nonzero-lag covariances are zero. Iterating conditional second moments gives, for each integer \(j\ge1\),
\[
\mathbb E[(X_{n+2j}-\mu)^2\mid X_n=x]
=\frac{\mu^2d^2(1-d^{2(j-1)})}{1-d^2}+d^{2j}x^2.
\]
Subtracting its stationary expectation and multiplying by \(X_n^2\) yields the quadratic covariance identity. At \(d=1/2\), uniformity on \([0,2\mu]\) gives \(\operatorname{Var}(X^2)=64\mu^4/45\), completing the critical coefficient.

## Verification

The accompanying `check.py` uses exact rational arithmetic to check the invariant interval, separation/overlap threshold, two-step contraction, critical-image partition, stationary moments, and the conditional quadratic identity at fifteen lags. It also checks parity-index disjointness and performs a reproducible finite simulation of the critical stationary law; execution printed `VERIFY_OK`. These tests are supplementary. The proofs of uniqueness, nonatomicity, fractal dimension, and singular lag-pair laws are analytical and apply to infinitely many parameters and lags.

## Relationship to prior work

Glendinning [1, §§2–4, in particular Theorem 5 and Eq. (19)] introduced the random switching-surface border-collision map and established an iterated-function-system attractor for sufficiently small forcing under contraction hypotheses. That result provides the model and qualitative IFS setting; it does not give the explicit symmetric two-point-threshold stationary law, its sharp Cantor-to-rectangle transition, or its parity-resolved two-time dependence. The invariant-measure studies [2,3] address the *deterministic* border-collision form, chiefly in expanding regimes, rather than the present randomly switched contracting subfamily. Standard self-similar-set/Bernoulli-convolution theory supplies the dimension calculation after reduction to scalar affine maps; the underlying IFS theorem and scalar dimension formula are not claimed as independently new. The combined exact classification, and especially the alternation of independent and singular stationary observations despite vanishing covariance, is the contribution for this named stochastic dynamical family.

## Limitations

The switching law is a symmetric two-point distribution with amplitude larger than the stationary coordinate bound. Other noise laws generally make the branch probabilities state-dependent, and none of these formulas is asserted for them. For \(d>1/2\) the support fills a rectangle, but **no claim** is made that its stationary probability is absolutely continuous: scalar overlapping Bernoulli convolutions can have subtle regularity. The total-variation assertion concerns two-point laws, not total variation convergence of one-time distributions from a fixed initial point. Earlier unindexed treatments could contain related special calculations; independent priority evaluation has not been performed.

## References

[1] P. Glendinning, *The border collision normal form with stochastic switching surface*, MIMS EPrint 2012.76, dated 8 August 2012; open preprint https://eprints.maths.manchester.ac.uk/1856/1/noisyswitch.pdf ; journal version, SIAM Journal on Applied Dynamical Systems 13 (2014), 181–193, DOI 10.1137/130931643.

[2] P. Glendinning, *Invariant measures of the border collision normal form*, MIMS EPrint 2011.1, 2011, https://eprints.maths.manchester.ac.uk/1557/1/invmeas.pdf .

[3] P. Glendinning, *Invariant measures for the n-dimensional border collision normal form*, International Journal of Bifurcation and Chaos (2014); open version https://eprints.maths.manchester.ac.uk/2252/1/glendinningijbcv2.pdf .
