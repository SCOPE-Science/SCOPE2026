# Exact clipping and moment laws for Gaussian Euler–Heun PI step control

## Finding

Consider a forward stochastic Euler–Heun trial step for an isotropic Ornstein–Uhlenbeck system, with the *same* Brownian increment used in the predictor and corrector. When the normalized predictor–corrector difference controls the next step by a proportional–integral (PI) rule, the unbounded **raw** step multiplier has an exact noncentral chi-square distribution after a power transformation. The actual **clipped** multiplier has two calculable boundary atoms. The raw-multiplier moment threshold and high-dimensional clipping rates are sharp; they must not be mistaken for infinite moments of the implemented, clipped method.

Write \(k=k_i+k_p>0\), \(C=\alpha^{k_i}e_{prev}^{k_p}>0\), and
\[
 s=\frac{\lambda g h^{3/2}}2,\qquad
 \Delta=\frac{\lambda^2h\|x\|_2^2}{g^2},\qquad
 Q(u)=\left(\frac{T\sqrt d}{s}\right)^2\left(\frac C u\right)^{2/k}.
\]
For every \(u>0\) the raw PI factor \(U\) has survival function
\[
 \boxed{\Pr(U>u)=F_{d,\Delta}(Q(u)),}
\]
where \(F_{d,\Delta}\) denotes the distribution function of the noncentral chi-square law with \(d\) degrees of freedom and noncentrality \(\Delta\). Moreover,
\[
 \boxed{\Pr(U>u)\sim\frac{e^{-\Delta/2}}{2^{d/2}\Gamma(1+d/2)}
 \left(\frac{T\sqrt d}{s}\right)^d C^{d/k}u^{-d/k}.}
\]
For every \(q>0\), \(\mathbb E[U^q]<\infty\) **if and only if** \(q<d/k\); equality diverges. For the published gain pair \(k_i=0.3\), \(k_p=0.1\), the raw factor has the exact positive-moment threshold \(2.5d\).

Fix caps \(0<m<1<M<\infty\) and set \(V=\min(M,\max(m,U))\). Then
\[
 \boxed{\Pr(V=M)=F_{d,\Delta}(Q(M)),\qquad
 \Pr(V=m)=1-F_{d,\Delta}(Q(m)).}
\]
Both atoms are strictly positive for every fixed finite \(d\). The continuous part on \((m,M)\) has density \((2/k)Q(v)f_{d,\Delta}(Q(v))/v\). Unlike the raw factor, \(V\) is bounded and has finite moments of all positive orders.

For the special but natural one-step normalization \(x=0\), \(T=s/\alpha\), \(e_{prev}=\alpha\), we obtain \(U=(\sqrt d/\|Z\|_2)^k\) with \(Z\sim N(0,I_d)\). Consequently, if \(I(z)=(z-1-\log z)/2\),
\[
 \boxed{\lim_{d\to\infty}-\frac1d\log\Pr(V=M)=I(M^{-2/k}),\quad
 \lim_{d\to\infty}-\frac1d\log\Pr(V=m)=I(m^{-2/k}).}
\]
Both rates are strictly positive. Thus for fixed caps the frequency of clipping decays exponentially in dimension in this normalized equilibrium benchmark, despite the heavy-tailed raw gain at every fixed dimension.

## Assumptions and scope

Let \(d\in\{1,2,\ldots\}\), \(\lambda>0\), \(g>0\), \(h>0\), and a conditional starting state \(x\in\mathbb R^d\) be fixed. The SDE is \(dX_t=-\lambda X_t\,dt+g\,dW_t\), with standard \(d\)-dimensional Brownian motion. The proposed step uses a fresh increment \(\Delta W=\sqrt h Z\), independent of the conditioning information, with \(Z\sim N(0,I_d)\). Both methods use the same increment, as in a shared-noise stochastic Heun predictor/corrector. Let \(T>0\) be a deterministic scalar noise-normalization tolerance at this step. It may represent \(\tau_{abs}+\tau_{rel}\sigma(t)\), but is held constant when conditioning.

The PI gain uses \(\alpha>0\), \(k_i,k_p\ge0\), \(k_i+k_p>0\), and prescribed \(e_{prev}>0\); the user may set \(0<\alpha\le1\). Caps satisfy \(0<m<1<M<\infty\). These are one-step distributional statements; no assumption of stationarity of adaptive errors is made. The forward-time additive-noise OU model is a **specialization of the algebraic shared-noise Euler–Heun estimator and PI update**, not a claim that the motivating reverse-diffusion generative sampler has precisely OU dynamics.

## Proof

**1. Discrepancy law.** Let \(\delta=-\lambda h x+g\Delta W\) be the Euler increment. The predictor is \(x_E=x+\delta\). For linear drift and constant diffusion, the second-stage increment is \(-\lambda h x_E+g\Delta W=\delta-\lambda h\delta\). The Heun approximation is therefore \(x_H=x+\delta-\lambda h\delta/2\). Their difference satisfies
\[
 x_E-x_H=\frac{\lambda h}2\delta
 =-\frac{\lambda^2h^2}{2}x+\frac{\lambda g h^{3/2}}2 Z.
\]
Put \(s=\lambda g h^{3/2}/2\). Then \((x_E-x_H)/s\) is normal with identity covariance and mean \(-\lambda\sqrt h x/g\). Its squared Euclidean norm is noncentral chi-square with \(d\) degrees of freedom and parameter \(\Delta=\lambda^2h\|x\|_2^2/g^2\). With normalized discrepancy \(\epsilon=\|x_E-x_H\|_2/(T\sqrt d)\), this gives the asserted distribution.

**2. Complete gain law and cap atoms.** The raw PI update is
\[
 U=\left(\frac\alpha\epsilon\right)^{k_i+k_p}
 \left(\frac{e_{prev}}\alpha\right)^{k_p}=C\epsilon^{-k}.
\]
Since \(k>0\), the event \(U>u\) is equivalent to
\(\epsilon<(C/u)^{1/k}\); rewriting this in terms of the noncentral chi-square variable yields \(\Pr(U>u)=F_{d,\Delta}(Q(u))\). The noncentral chi-square distribution has a continuous strictly positive density on positive arguments. Clipping maps precisely \(U\ge M\) to \(V=M\) and \(U\le m\) to \(V=m\); these events therefore have the displayed strictly positive probabilities. A change of variables \(z=Q(v)\) yields the density on the open interval \((m,M)\).

**3. Sharp tail and moments.** The noncentral chi-square law admits the Poisson mixture \(F_{d,\Delta}(z)=e^{-\Delta/2}\sum_{j\ge0}(\Delta/2)^jF_{\chi^2_{d+2j}}(z)/j!\). At \(z\downarrow0\), the central chi-square term with \(j=0\) is leading; direct integration of its gamma density gives
\[
 F_{d,\Delta}(z)=\frac{e^{-\Delta/2}}{2^{d/2}\Gamma(1+d/2)}z^{d/2}(1+O(z)).
\]
Substituting \(z=Q(u)\) proves the regularly varying tail with positive explicit constant. For any positive random variable \(Y\), the layer-cake identity \(\mathbb E Y^q=q\int_0^\infty u^{q-1}\Pr(Y>u)\,du\) shows that the positive tail is integrable exactly for \(q<d/k\); at equality its integral diverges logarithmically. Boundedness \(m\le V\le M\) settles all clipped moments.

**4. Dimension-dependent clipping rate.** At \(x=0\) with \(T=s/\alpha\) and \(e_{prev}=\alpha\), we have \(\epsilon=\alpha\|Z\|_2/\sqrt d\), and thus \(U=(\sqrt d/\|Z\|_2)^k\). Let \(S_d=d^{-1}\sum_{j=1}^d Z_j^2\). The upper cap event becomes \(S_d\le M^{-2/k}<1\), and the lower cap event becomes \(S_d\ge m^{-2/k}>1\). The sample mean of independent squared standard Gaussians obeys Cramér's theorem, because \(\log\mathbb E e^{tZ_j^2}=-\frac12\log(1-2t)\) for \(t<1/2\). Optimizing \(tz+\frac12\log(1-2t)\) over \(t<1/2\) gives \(I(z)=(z-1-\log z)/2\). The one-sided large-deviation bounds for the two open half-lines (their boundary rates agree by continuity) give both asserted limits.

## Verification

The accompanying `check_distribution.py` recomputes the Euler and stochastic Heun stages using **identical** Gaussian increments, checks the exact noncentral chi-square survival formula for four dimensions and four thresholds, compares 12 large-threshold tail evaluations with their leading constants, and verifies the clipped support. It additionally checks finite-dimensional approximation to the predicted large-deviation rate. The analytic normal transformation, small-ball expansion, moment criterion and Cramér argument prove the statements for all integers \(d\ge1\); finite simulations are corroboration only.

## Relationship to prior work

Kemperman and Ambrogioni (2026, arXiv:2610.03034v1, equations (3)–(4), Algorithm 1 and Appendix B.1) specify a shared-increment stochastic Euler–Heun error estimator with diffusion-noise normalization and clipped PI update. The present exact conditional gain distribution is derived for a particular additive-noise OU test problem, **not** for the full nonlinear reverse-diffusion model. Ilie, Jackson and Enright (2014 technical report, later *Numerical Algorithms*, Section 3.1) derive PI gain recursions and discuss controller stability and clipping for Milstein discretization; this does not provide the noncentral chi-square law, its sharp moment threshold, or the two dimension-dependent clipping rates. Lamba and Seaman (2006) analyze mean-square stability under different drift/diffusion error controls for linear SDEs with multiplicative noise; that is a different question from the conditional distribution of an embedded Euler–Heun PI multiplier. The chi-square, Poisson-mixture and Cramér tools themselves are classical and not claimed as discoveries.

## Limitations

The theorem is conditional on one fixed trial step, chosen before sampling its Gaussian increment; it does not analyze the joint distribution of future adaptive step sizes, rejection-biased increments, overall solver error, or computing cost. It assumes isotropic nondegenerate additive Gaussian noise, linear drift, exact arithmetic, common predictor–corrector increments, and deterministic normalization at the selected step. Anisotropy, multiplicative noise, correlated components and arbitrary nonlinear scores require different analyses. Infinite positive moments refer **only to the uncapped mathematical proposal**. With any fixed caps the implemented multiplier is bounded. Bibliographic uniqueness is not certified; analogous small-ball arguments may appear in incompletely indexed literature.

## References

1. E. Kemperman and L. Ambrogioni, *Adaptive Second-Order Solvers for Fast Stochastic Diffusion Sampling*, arXiv:2610.03034v1, first posted 2026-10-02, https://arxiv.org/html/2610.03034v1 ; equations (3)–(4), Algorithm 1, Appendix B.1.
2. S. Ilie, K. R. Jackson, W. H. Enright, *Adaptive time-stepping for the strong numerical solution of stochastic differential equations*, *Numerical Algorithms* 68 (2015), 791–812, https://doi.org/10.1007/s11075-014-9872-6 ; openly accessible 2014 preprint: https://www.cs.toronto.edu/pub/reports/na/SDE.Adaptive.Timestepping.NA.1.pdf , Section 3.1.
3. H. Lamba and T. Seaman, *Mean-square stability properties of an adaptive time-stepping SDE solver*, *J. Comput. Appl. Math.* 194 (2006), 245–254, https://math.gmu.edu/~harbir/stochstab.pdf .
4. A. Jolicoeur-Martineau et al., *Gotta Go Fast When Generating Data with Score-Based Models*, arXiv:2105.14080 (2021), https://arxiv.org/abs/2105.14080 ; adjacent adaptive diffusion-sampling framework, full-text overlap check incomplete.
