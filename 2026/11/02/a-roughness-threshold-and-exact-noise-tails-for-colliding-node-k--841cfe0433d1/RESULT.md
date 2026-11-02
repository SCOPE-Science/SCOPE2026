# A roughness threshold and exact noise tails for colliding-node kernel quadrature

## Finding

Consider two independent uniform integration nodes on \([0,1]\) and an exact kernel-interpolatory quadrature rule using the power-exponential kernel \(k_{\alpha,\lambda}(x,y)=\exp(-\lambda|x-y|^\alpha)\), where \(0<\alpha\le2\) and \(\lambda>0\). Add two independent centered Gaussian observation errors with standard deviation \(\sigma>0\). **Kernel roughness causes a sharp second-moment transition at \(\alpha=3/2\)**: the unregularized noisy quadrature error has finite variance for \(0<\alpha<3/2\), infinite variance at and beyond that endpoint, and a complete one-sided regularly varying tail law for \(\alpha>1\). The corresponding diagonal-nugget penalty has a finite limit below the threshold, logarithmic divergence at the threshold, and an exact fractional-power divergence above it.

Define the exact kernel mean and its derivative by
\[
m(u)=\int_0^1 e^{-\lambda|u-v|^\alpha}\,dv,\qquad m'(u)=e^{-\lambda u^\alpha}-e^{-\lambda(1-u)^\alpha}.
\]
For \(1<\alpha\le2\), set \(\beta=1/(\alpha-1)\). If \(E\) is the noisy quadrature error, then for *every fixed Lipschitz integrand* \(f\),
\[
\lim_{t\to\infty}t^\beta\Pr(E>t)=\lim_{t\to\infty}t^\beta\Pr(E<-t)=C_{\alpha,\lambda,\sigma},
\quad C_{\alpha,\lambda,\sigma}=\left(\frac{\sigma}{\lambda}\right)^\beta\frac{\Gamma((\beta+1)/2)}{\sqrt\pi}\int_0^1|m'(u)|^\beta\,du.
\]
The coefficient is strictly positive and finite. The precise absolute-moment condition is \(\mathbb E|E|^q<\infty\) if and only if \(0<q<\beta\); at \(q=\beta\) the moment already diverges. For \(0<\alpha\le1\), the rule weights are uniformly bounded and \(E\) has every absolute moment.

For regularized weights \(w^\eta=(K+\eta I)^{-1}(m(X),m(Y))^{\mathsf T}\) and \(M_\eta=\mathbb E\|w^\eta\|_2^2\),
\[
\lim_{\eta\downarrow0}M_\eta=M_0<\infty\quad(0<\alpha<3/2),
\]
\[
\lim_{\eta\downarrow0}\frac{M_\eta}{\log(1/\eta)}=\frac{2}{3\lambda^2}\int_0^1m'(u)^2\,du\quad(\alpha=3/2),
\]
and
\[
\lim_{\eta\downarrow0}\eta^{2-3/\alpha}M_\eta
=\frac{\lambda^{-3/\alpha}}{\alpha}\Gamma(3/\alpha)\Gamma(2-3/\alpha)\int_0^1m'(u)^2\,du\quad(3/2<\alpha\le2).
\]
For the zero integrand, the entire mean-squared error equals \(\sigma^2M_\eta\), so these are exact noise-induced mean-squared-error asymptotics, not merely weight-norm estimates.

## Assumptions and scope

All random variables are on one probability space. The nodes \(X\) and \(Y\) are independent \(U[0,1]\) variables; their almost-sure distinctness makes the two-by-two Gram matrix \(K\), with diagonal \(1\) and off-diagonal \(k_{\alpha,\lambda}(X,Y)\), invertible. The independent observation errors \(\varepsilon_1,\varepsilon_2\) are centered Gaussian with variance \(\sigma^2\), independent of the nodes. The integrand \(f:[0,1]\to\mathbb R\) is fixed and Lipschitz. The quadrature estimate is \(Q_f=w_1(f(X)+\varepsilon_1)+w_2(f(Y)+\varepsilon_2)\) where \(w=K^{-1}(m(X),m(Y))^{\mathsf T}\). The quadrature error is \(E=Q_f-\int_0^1f\). Regularization affects the Gram matrix through a strictly positive *diagonal* nugget \(\eta\), and \(M_\eta\) is averaged over both uniform nodes, not over observation noise. For \(0<\alpha\le2\), the kernel is positive definite; the main identities use only the two-by-two Gram matrix and its positive eigenvalues. The limiting statements keep \(\alpha,\lambda,\sigma\) fixed while \(t\to\infty\) or \(\eta\downarrow0\).

## Proof

**1. Exact symmetric--antisymmetric decomposition.** Write \(\delta=X-Y\), \(u=(X+Y)/2\), \(k=e^{-\lambda|\delta|^\alpha}\), and \(m_\pm=m(u\pm\delta/2)\). On the domain \(|\delta|<1\), \(|\delta|/2\le u\le1-|\delta|/2\), the Jacobian from \((X,Y)\) to \((u,\delta)\) is one. Direct diagonalization of \(K\) yields
\[
w_X=\frac{m_++m_-}{2(1+k)}+\frac{m_+-m_-}{2(1-k)},\qquad
w_Y=\frac{m_++m_-}{2(1+k)}-\frac{m_+-m_-}{2(1-k)}.
\]
The same formulas hold for \(w^\eta\) after replacing both denominators \(1\pm k\) by \(1+\eta\pm k\). In particular,
\[
\|w^\eta\|_2^2=\frac12\left(\frac{(m_++m_-)^2}{(1+\eta+k)^2}+\frac{(m_+-m_-)^2}{(1+\eta-k)^2}\right).
\]
These identities are exact, including arbitrarily close but distinct nodes.

**2. Uniform collision expansions and the noiseless remainder.** The kernel mean is continuously differentiable on the entire closed interval, with the derivative displayed above; its derivative is uniformly continuous. Uniformly in allowed \(u\), as \(\delta\to0\),
\[
m_+-m_-=m'(u)\delta+o(|\delta|),\qquad
1-k=\lambda|\delta|^\alpha(1+o(1)).
\]
The symmetric part of either weight is uniformly bounded. The antisymmetric part is \((m'(u)/(2\lambda))\operatorname{sgn}(\delta)|\delta|^{1-\alpha}+o(|\delta|^{1-\alpha})\). Hence each weight is uniformly bounded if \(\alpha\le1\). For every \(\alpha\le2\) the *noiseless* quadrature contribution is bounded: the antisymmetric component multiplies \(f(X)-f(Y)=O(|\delta|)\), giving \(O(|\delta|^{2-\alpha})\), whereas the symmetric component multiplies a bounded sum. This also bounds the deterministic bias term in \(E\) uniformly across the node square.

**3. Exact power tails.** Put \(s=\alpha-1>0\), \(\beta=1/s\), and \(Z=\varepsilon_1-\varepsilon_2\sim N(0,2\sigma^2)\). The only potentially unbounded part of the noisy quadrature error near a collision is
\[
\frac{m_+-m_-}{2(1-k)}Z
=\frac{m'(u)}{2\lambda}\operatorname{sgn}(\delta)|\delta|^{-s}Z+o(|\delta|^{-s})Z.
\]
Its other Gaussian component has a uniformly bounded coefficient and the deterministic contribution is uniformly bounded. To justify the tail limit, first restrict the midpoint to a compact interior interval and \(|\delta|\) below a fixed small radius; uniform continuity gives uniform multiplicative coefficient control. For each fixed midpoint, changing variables \(v=t|\delta|^s\) and integrating the normal survival function gives the tail integral \(t^{-\beta}\mathbb E[(cZ)_+^\beta]\) from each sign of \(\delta\), where \(c=m'(u)/(2\lambda)\). The two signs together contribute \(t^{-\beta}\mathbb E|cZ|^\beta\). The error terms are negligible by Gaussian absolute-moment domination and the bound \(|m_+-m_-|\le \|m'\|_\infty|\delta|\). The outer part of the node square contributes a Gaussian tail, and shrinking midpoint endpoint strips have vanishing contribution by the same uniform domination. The normal moment identity
\[
\mathbb E|Z|^\beta=(2\sigma)^\beta\frac{\Gamma((\beta+1)/2)}{\sqrt\pi}
\]
therefore gives exactly \(C_{\alpha,\lambda,\sigma}\). The derivative is nonzero except at the midpoint \(u=1/2\), which proves strict positivity of the coefficient. The layer-cake moment identity \(\mathbb E|E|^q=q\int_0^\infty t^{q-1}\Pr(|E|>t)\,dt\) proves the sharp moment criterion, including divergence at equality. For \(\alpha\le1\), bounded conditional Gaussian coefficients and bounded deterministic bias give moments of every positive order.

**4. Ridge weight-norm and its three regimes.** Integrate the exact norm identity over the two-node square using midpoint--difference coordinates. The symmetric summand is uniformly integrable as \(\eta\downarrow0\); its expectation stays bounded. The two signs of \(\delta\), together with the factor \(1/2\) in the antisymmetric norm, produce the leading model integral
\[
I_\eta=\left(\int_0^1m'(u)^2\,du\right)\int_0^\epsilon\frac{d^2}{(\eta+\lambda d^\alpha)^2}\,dd.
\]
Uniform differentiability controls the substitution of \(m'(u)d\) for the mean difference, and uniform \(1-e^{-\lambda d^\alpha}\sim\lambda d^\alpha\) controls the denominator. The midpoint admissibility interval differs from \([0,1]\) by length \(d\), negligible at every divergent scale. For \(\alpha<3/2\), the unregularized integrand is locally \(d^{2-2\alpha}\), which is integrable, so dominated convergence yields a finite \(M_0\). When \(\alpha=3/2\), the region \(d\gg(\eta/\lambda)^{2/3}\) contributes \(\lambda^{-2}\int d^{-1}dd\), hence \((2/(3\lambda^2))\log(1/\eta)\) times the derivative energy; the inner region contributes only a bounded remainder at logarithmic scale. For \(3/2<\alpha\le2\), rescale \(d=(\eta/\lambda)^{1/\alpha}v\); the positive integrable model is \(v^2/(1+v^\alpha)^2\), with integral
\[
\int_0^\infty\frac{v^2}{(1+v^\alpha)^2}\,dv
=\frac{\Gamma(3/\alpha)\Gamma(2-3/\alpha)}{\alpha}.
\]
The near-collision approximation and the far-region bound give the asserted limit by dominated convergence and cutoff arguments. All displayed coefficients are finite and strictly positive because \(m'\) is continuous and not identically zero.

**5. The variance boundary.** Conditional on the nodes, the observation-noise variance is exactly \(\sigma^2\|w\|_2^2\). The noiseless part is uniformly bounded, so the law of total variance and the weight-norm integrability criterion show that the full noisy quadrature error has finite second moment precisely when \(\alpha<3/2\). The strict divergence at the critical exponent follows also from the exact tail with \(\beta=2\). The only random inputs are the two nodes and Gaussian observation errors; no large-sample approximation is invoked in these identities.

## Verification

The accompanying script `verify_power_kernel.py` independently constructs kernel means through incomplete-gamma integrals, differentiates them numerically, checks the two-node linear systems and norm decompositions, and performs numerical integration at and around the critical roughness. It uses Python, NumPy and SciPy; dependencies appear in `requirements.txt`. At the recorded verification it passed **109 deterministic checks**. Illustrative limits with \(\lambda=1\): at \(\alpha=3/2\), the predicted logarithmic coefficient was \(0.10346437177972002\) against a finite-nugget difference estimate \(0.10332075866067487\); at \(\alpha=7/4\), the predicted power coefficient was \(0.2603660746138136\), with finite-nugget estimate \(0.2554319129115096\). At \(\alpha=2\), the predicted square-root coefficient was \(0.12437813466940074\), with estimate \(0.12359851032016213\). These tests corroborate but do not replace the analytic proof of the infinite-domain limits or their uniform bounds.

## Relationship to prior work

Hayakawa, Oberhauser and Lyons (2023) analyze sampling-based Nyström approximation and kernel quadrature and motivate studying actual sampled nodes; their main quadrature guarantees use selected subspaces and convex rules, not an exact collision-noise distribution for unconstrained two-node kernel interpolation. Karvonen, Kanagawa and Särkkä (2018) analyze positivity and magnitudes of Bayesian quadrature weights and emphasize separation radius, but do not in the inspected results give a uniform-iid-node, Gaussian-noise, power-exponential all-exponent moment classification. Briol, Oates, Cockayne, Chen and Girolami (2017) analyze probabilistic integration and random-node kernel methods at a more general level. Prior two-node **Gaussian-kernel** collision-tail and square-root-nugget formulas cover the special case \(\alpha=2\), \(\lambda=1\). That case is **not** asserted as new. The additional mathematical contribution here is the distinct general-exponent family, especially the finite/infinite-variance threshold \(\alpha=3/2\), its exact logarithmic boundary coefficient, and the continuous family of tail and nugget exponents. The generic prior weight-separation estimates do not by themselves imply these exact averaged stochastic thresholds. The probability tail and ridge asymptotic results are claimed only for the stated model and do not establish absolute publication priority.

## Limitations

The theorem is restricted to two iid uniform points in one dimension, fixed power-exponential kernel and Gaussian independent measurement errors, a fixed Lipschitz integrand, and exact arithmetic. It makes no claim for more nodes, alternative node repulsion laws, general kernels, floating-point roundoff or optimal design. The nugget statements concern expected squared weights and, for the zero integrand, exact noise mean-squared error; they do not themselves establish optimal regularization for a general nonzero integrand. The heavy-tail proof requires \(\sigma>0\) and does not imply heavy tails for noiseless data. The finite numerical tests are diagnostic, not exhaustive or an infinite proof. Possible earlier specialized treatments of collision asymptotics remain a publication-priority risk; independent external validation has not been performed.

## References

1. S. Hayakawa, H. Oberhauser and T. Lyons, *Sampling-based Nyström Approximation and Kernel Quadrature*, arXiv:2301.09517 (first public version 23 January 2023), https://arxiv.org/abs/2301.09517.
2. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509 (2018), https://arxiv.org/abs/1812.08509.
3. F.-X. Briol, C. Oates, J. Cockayne, W. Chen and M. Girolami, arXiv:1706.03369 (2017), https://arxiv.org/abs/1706.03369.
