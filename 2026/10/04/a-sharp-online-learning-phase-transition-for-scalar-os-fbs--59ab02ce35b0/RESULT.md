# A sharp online-learning phase transition for scalar OS-FBS
## Finding
Consider Algorithm 1 of Zhang--Gao--Udell specialized to online-scaled forward--backward splitting (OS-FBS) on
\[
f(x)=\frac{a}{2}x^2,\qquad g\equiv0,
\]
where \(a>0\). Let \(0<\gamma<1/a\), set \(s=\gamma a\in(0,1)\), use the scalar preconditioner set
\[
\mathcal P=[1,2/s-1],
\]
initialize \(p_0=1\), and use the unregularized feedback \(\beta=0\) with constant online stepsize \(\eta>0\). Define
\[
\theta=\eta a(1-s),\qquad \rho=1-\theta.
\]
For every nonzero initial point \(x_0\), every probe is accepted by the null step. The online-learning parameter has a sharp dynamical transition at \(\theta=2\).

If \(0<\theta<2\) and \(\theta\ne1\), then the projection never activates and
\[
p_k=\frac1s+\rho^k\left(1-\frac1s\right),
\qquad
x_k=x_0(1-s)^k\rho^{k(k-1)/2}.
\]
Consequently
\[
\frac{|x_{k+1}|}{|x_k|}=(1-s)|\rho|^k\longrightarrow0,
\]
so the primal sequence converges Q-superlinearly, with \(\log|x_k|=\frac12k^2\log|\rho|+O(k)\). At the distinguished value \(\theta=1\), the learned preconditioner reaches \(1/s\) after one online update and the second primal probe lands exactly at the minimizer: \(x_2=0\).

For every \(\theta\ge2\), the projected preconditioner instead satisfies
\[
p_{2j}=1,\qquad p_{2j+1}=\frac2s-1,
\]
and the primal iterates obey
\[
|x_k|=(1-s)^k|x_0|.
\]
Thus overly aggressive online learning does not cause objective growth here; projection produces a stable endpoint two-cycle and collapses the superlinear acceleration back to the base linear contraction. The null-step safeguard does not detect this loss of acceleration because every proposed point strictly decreases the envelope whenever the current point is nonzero.

## Assumptions and scope
The statement concerns the exact scalar, deterministic OS-FBS iteration from Algorithm 1 of arXiv:2609.10732v1. The smooth term has Lipschitz constant \(L=a\), the nonsmooth term is zero, and the splitting stepsize satisfies the paper's strict condition \(0<\gamma<1/L\). The interval \([1,2/s-1]\) is the smallest interval symmetric about the exact one-step residual preconditioner \(p_\star=1/s\) that contains the prescribed initialization \(p_0=1\). It is compact, convex, positive, contains the identity, and contains \(p_\star\).

The online stepsize \(\eta\) is constant. This is an admissible input to Algorithm 1, but it is not the particular horizon-dependent choice used in the paper's global and local theorems. The finding is an exact phase law for this specialization, not a worst-case statement for general OSOP, matrix preconditioners, nonsmooth problems, AdaGrad schedulers, or the efficient ADMM variants.

## Proof
For \(g\equiv0\), the forward--backward map is
\[
T(x)=x-\gamma ax=(1-s)x,
\]
so its fixed-point residual is \(x-T(x)=sx\). Equation (6) of the source gives the forward--backward envelope
\[
F_\gamma(x)=f(x)-\frac{\gamma}{2}|f'(x)|^2
=\frac{a(1-s)}{2}x^2.
\]
Because this envelope is strongly convex, Algorithm 1 uses \(\beta=0\).

For a nonzero \(x\), the scalar version of the source feedback (17) is
\[
\ell_x(p)=\frac{F_\gamma((1-sp)x)-F_\gamma(x)}{s^2x^2}
=\frac{a(1-s)}{2}\left(p^2-\frac{2p}{s}\right).
\]
Hence
\[
\ell_x'(p)=a(1-s)\left(p-\frac1s\right).
\]
The feedback is independent of \(x\), and the projected online-gradient update becomes
\[
p_{k+1}=\Pi_{[1,2/s-1]}
\left[
\frac1s+\rho\left(p_k-\frac1s\right)
\right],
\qquad \rho=1-\theta.
\]

Every \(p\in[1,2/s-1]\) satisfies
\[
-(1-s)\le 1-sp\le 1-s.
\]
Therefore, for \(x\ne0\),
\[
F_\gamma((1-sp)x)\le(1-s)^2F_\gamma(x)<F_\gamma(x).
\]
Thus the null step always accepts the probe and
\[
x_{k+1}=(1-sp_k)x_k.
\]

Suppose \(0<\theta<2\), so \(|\rho|<1\). Starting from \(p_0=1\), the unprojected recursion gives
\[
p_k=\frac1s+\rho^k\left(1-\frac1s\right).
\]
If \(\rho\ge0\), these points lie between \(1\) and \(1/s\). If \(\rho<0\), even indices lie in that interval and odd indices lie strictly between \(1/s\) and its reflection \(2/s-1\). Hence the projection is inactive. Substitution gives
\[
1-sp_k=(1-s)\rho^k,
\]
so multiplication over \(j=0,\ldots,k-1\) yields
\[
x_k=x_0(1-s)^k\rho^{k(k-1)/2}.
\]
When \(\rho=0\), equivalently \(\theta=1\), the first online update gives \(p_1=1/s\), and the next accepted probe is exactly zero.

At \(\theta=2\), \(\rho=-1\), so the affine online step swaps the two endpoints \(1\) and \(2/s-1\). If \(\theta>2\), then \(\rho<-1\): the raw update from \(1\) lies above \(2/s-1\), while the raw update from \(2/s-1\) lies below \(1\). Projection therefore again swaps the endpoints exactly. Their probe multipliers are \(1-s\) and \(-(1-s)\), proving \(|x_k|=(1-s)^k|x_0|\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check the feedback identity, the projected preconditioner recursion, the closed form in the regime \(0<\theta<2\), finite termination at \(\theta=1\), and the endpoint two-cycle for \(\theta\ge2\) on several rational parameter choices. The proof above is symbolic and does not rely on those finite checks.

The key boundary checks are also immediate algebraically: \(0<\theta<2\) is exactly \(|\rho|<1\); at \(\theta=2\), \(\rho=-1\); and for \(\theta>2\), projection sends each symmetric endpoint past the opposite endpoint before clipping.

## Relationship to prior work
Zhang--Gao--Udell define the residual probe, normalized envelope feedback, projected online update, and null step in equations (16)--(18) and Algorithm 1 of arXiv:2609.10732v1. Their Theorem 4.24 proves a local superlinear bound when the splitting map is locally affine, using a horizon-dependent online stepsize. The inspected source does not state the constant-online-stepsize scalar phase transition, the exact \(\exp(-\Theta(k^2))\) law, or the endpoint two-cycle at and above the threshold.

There is an important equivalence to earlier hypergradient-descent work. Under the scalar change of variable \(\alpha=\gamma p\), the present smooth OS-FBS step is ordinary scalar gradient descent with an online-learned stepsize, and the effective hypergradient learning rate is rescaled by \(1-s\). Chu--Gao--Ye--Udell (arXiv:2502.11229v2) analyze projected hypergradient descent, null steps, quadratic local superlinear convergence, and preconditioner learning. Gao--Chu--Ye--Udell (arXiv:2505.23081v2) likewise develops the hypergradient-feedback framework and superlinear guarantees. In the inspected full texts, neither source states the exact \(\theta=2\) projected bifurcation, the symmetric endpoint cycle, or the resulting loss of superlinear acceleration while every null-step test succeeds.

Targeted semantic searches also returned a nearby published result on stochastic OSGM feedback and curvature stability, but that result concerns random-curvature population targets and support thresholds rather than the deterministic projected OS-FBS dynamics here. Other close records concern Polyak, Barzilai--Borwein, reflected-gradient, and extragradient stability frontiers and do not dominate this claim.

## Limitations
The result is one-dimensional and uses a deliberately symmetric candidate interval tied to the identity initialization and exact one-step preconditioner. It does not show that \(\theta=2\) is a universal threshold for other preconditioner sets, matrix-valued OSOP, varying online stepsizes, AdaGrad, or nonlinear splitting maps. The scalar OS-FBS dynamics are affinely equivalent to a scalar projected hypergradient-descent problem, so an older or unindexed treatment of that exact projected quadratic recurrence could contain the same phase law; no such statement was found in the inspected primary sources or targeted searches.

The null-step conclusion uses strict envelope decrease for nonzero \(x\) on the stated interval. At the minimizer Algorithm 1 stops before evaluating the normalized feedback, whose denominator would vanish.

## References
1. W. Zhang, W. Gao, and M. Udell, *Operator Splitting Methods with Online Scaling*, arXiv:2609.10732v1, 2026. See equations (6), (16)--(18), Algorithm 1, and Theorem 4.24.
2. Y.-C. Chu, W. Gao, Y. Ye, and M. Udell, *Provable and Practical Online Learning Rate Adaptation with Hypergradient Descent*, arXiv:2502.11229v2, 2025. See Algorithm 1, Section 3.3, and Lemma 3.1.
3. W. Gao, Y.-C. Chu, Y. Ye, and M. Udell, *Gradient Methods with Online Scaling Part I. Theoretical Foundations*, arXiv:2505.23081v2, 2025. See Section 3.2 and Theorem 6.9.
