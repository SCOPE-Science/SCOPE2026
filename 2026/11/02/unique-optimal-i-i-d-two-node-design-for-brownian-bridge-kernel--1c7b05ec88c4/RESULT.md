# Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature

## Finding
Let \(k(s,t)=\min(s,t)-st\) on \([0,1]^2\), with reproducing-kernel Hilbert space \(H_0^1(0,1)\) and squared norm \(\int_0^1|f'(x)|^2\,dx\). The target is Lebesgue integration \(I(f)=\int_0^1 f(x)\,dx\). Draw two nodes independently from an arbitrary Borel probability \(\mu\) on \([0,1]\), and use the optimal fixed-node kernel quadrature weights (equivalently, integrate the piecewise-linear interpolant with zero boundary values). Write \(V(Z_1,Z_2)\) for its **squared worst-case integration error** on the unit ball of \(H_0^1\), equivalently the posterior integral variance under the Brownian-bridge Gaussian prior. Repeated nodes are treated as one distinct observation.

Among **all Borel probability distributions**, including atomic and endpoint-supported distributions, the unique minimizer of \(\mathbb E_{\mu^{\otimes2}} V(Z_1,Z_2)\) has density
\[
p_*(x)=\begin{cases}
\displaystyle\frac{2(1+r^2)}{[1+(2x-1)^2]^2},& |2x-1|\le r,\\[4pt]
0,& |2x-1|>r,
\end{cases}
\]
where \(r\) is the unique solution in \((0,1)\) of
\[
r+(1+r^2)\arctan r=1.
\]
In particular \(r=0.4673387737906299\ldots\); with \(a=(1-r)/2=0.2663306131046850\ldots\), the optimal sampling support is the strict central interval \([a,1-a]\). The minimum expected squared error is exactly
\[
\boxed{\inf_\mu\mathbb E V=\frac{3a-\tfrac32a^2-\tfrac12}{12}=0.016049487174914912\ldots.}
\]
For uniform independent nodes the same expectation is \(1/40=0.025\), so choosing the optimal **fixed i.i.d. sampling law** reduces expected posterior integral variance by \(35.8020513\ldots\%\). This is a distributional design optimum, not an optimum over correlated or deterministically selected two-node designs.

## Assumptions and scope
The target integration measure is uniform on \([0,1]\), distinct from the variable node-sampling distribution \(\mu\). Sampling uses precisely two independent draws with replacement. Evaluation is noiseless. The optimal fixed-node weights are recomputed from the sampled locations, and need not sum to one since the function class has homogeneous boundary values. The optimization criterion is \(\mathbb E[\sup_{\|f\|_{H_0^1}\le1}|I(f)-Q_Z(f)|^2]\). It is **not** the different criterion \(\sup_f\mathbb E|I(f)-Q_Z(f)|^2\), and makes no simultaneous worst-function risk claim.

The theorem does not impose an absolutely continuous sampling law or full support: such properties, or their failure, are consequences of the optimization. The density is interpreted as zero off its stated support; no boundary atoms occur.

## Proof
**1. Exact fixed-node error.** For two sampled locations, let \(0=x_0\le x_1\le x_2\le x_3=1\) denote the sorted locations and boundary points, allowing ties. The minimum-norm kernel interpolant is linear on each interval \([x_i,x_{i+1}]\). The residual kernel on an interval of length \(h\), after conditioning on its endpoints, is the bridge covariance \(\min(s,t)-st/h\) in interval-local coordinates. Its double integral is \(h^3/12\); cross-interval conditional covariances vanish. The squared worst-case error is therefore
\[
V(x_1,x_2)=\frac1{12}\sum_{i=0}^2 (x_{i+1}-x_i)^3.
\]
The same identity follows directly from \(\iint k-m_Z^\top K_Z^+m_Z\), using a pseudoinverse when the nodes coincide.

**2. Convex expected-gap functional.** Set \(S(\mu)=12\mathbb E_\mu V\). With independent \(X,Y\sim\mu\), define
\[
K(x,y)=\min(x,y)^3+|x-y|^3+[1-\max(x,y)]^3.
\]
Then \(S(\mu)=\iint K(x,y)\,d\mu(x)d\mu(y)\). Each interval gap of length \(h\) contributes \(h^3/6\) to \(\int_{u<v}(v-u)\mathbf1_{\{\text{no observed node in }(u,v)\}}\,du\,dv\). Thus, with atoms permitted,
\[
S(\mu)=6\int_{0<u<v<1}(v-u)[1-\mu((u,v))]^2\,du\,dv. \tag{1}
\]
For a signed zero-total-mass measure \(\eta\), the quadratic term is
\[
\iint K(x,y)\,d\eta(x)d\eta(y)=6\int_{0<u<v<1}(v-u)\eta((u,v))^2\,du\,dv\ge0.\tag{2}
\]
Equality in (2) implies that the restrictions of the two compared probability measures to \((0,1)\) agree (intervals distinguish finite measures there). This is the necessary qualification: mass can be transferred between the uninformative endpoints without changing (2).

**3. Construction of an equilibrium design.** Write \(q(x)=x^2+(1-x)^2\), take \(a\in(0,1/2)\), and consider the centered density
\[
p_a(x)=\frac{q(a)}{q(x)^2}\mathbf1_{[a,1-a]}(x).
\]
Set \(r=1-2a\). Substitution \(u=2x-1\) gives
\[
\int_a^{1-a}p_a(x)\,dx=r+(1+r^2)\arctan r.
\]
This quantity increases strictly from zero to \(1+\pi/2\) as \(r\) increases from zero to one; its derivative is \(2+2r\arctan r>0\). Hence there is exactly one normalizing \(r\) and the announced probability \(\mu_*\). Its mean is \(1/2\) by symmetry.

Define its potential \(U(x)=\int K(x,y)p_*(y)\,dy\). Differentiating the explicit piecewise-cubic expression for \(K\) at an interior support point gives
\[
U''(x)=6\int_a^x(1-y)p_*(y)\,dy+6\int_x^{1-a}yp_*(y)\,dy-3q(x)p_*(x).
\]
Since \(p_*(x)=q(a)/q(x)^2\), direct differentiation yields \(U'''(x)=0\) for \(a<x<1-a\). At \(x=a+\), symmetry and \(q(a)p_*(a+)=1\) imply \(U''(a+)=6(1/2)-3=0\). Hence \(U''\) vanishes throughout that interval, and symmetry gives \(U'(1/2)=0\): \(U\) is a constant \(c\) throughout \([a,1-a]\).

For \(x<a\) or \(x>1-a\), differentiating under the integral (the kernel changes polynomial branch only at a point outside the support) yields \(U''=3\). Continuity of \(U\) and \(U'\) at the support endpoints gives the exact obstacle profile
\[
U(x)=c+\frac32\operatorname{dist}(x,[a,1-a])^2.\tag{3}
\]
Thus \(U(x)\ge c\) globally, with equality precisely on the central support.

**4. Global optimality and uniqueness, with no regularity restriction on competitors.** For any Borel probability \(\nu\), write \(\eta=\nu-\mu_*\). Bilinearity and (2) yield
\[
S(\nu)-S(\mu_*)=2\int U\,d\eta+6\int_{0<u<v<1}(v-u)\eta((u,v))^2\,du\,dv.\tag{4}
\]
The first term equals \(2\int(U-c)\,d\nu\ge0\) by (3), because \(\mu_*\) is supported on \(U=c\); the second is nonnegative. If equality holds, the squared-interval integral vanishes, so \(\nu\) and \(\mu_*\) coincide on \((0,1)\). Since \(\mu_*\) already assigns unit mass to \((0,1)\), \(\nu\) has no endpoint mass and \(\nu=\mu_*\). This proves global optimality and uniqueness across all Borel probabilities.

**5. Exact optimum and uniform comparison.** For \(x<a\), differentiation of \(K(x,y)\) against a symmetric law gives \(U'(x)=3x-3\mathbb E_{\mu_*}Y^2\). Continuity and \(U'(a)=0\) imply \(\mathbb E Y^2=a\). Hence \(U(0)=1-3/2+3a\), and (3) yields \(c=3a-3a^2/2-1/2\). Because \(U=c\) on the support, \(S(\mu_*)=\int U\,d\mu_*=c\), proving the claimed minimum. For two iid uniform nodes the three gaps have the Dirichlet\((1,1,1)\) law, whose expected sum of cubes is \(3/10\), so \(\mathbb EV=1/40\).

## Verification
Run \(`python verify.py`\) with Python 3.10+, SymPy, and mpmath. The checks include the exact bridge covariance integral, 45 exact-rational two-node Gram-inverse comparisons, symbolic density-normalization and potential-derivative identities, the uniform-node expectation, high-precision root/normalization/second-moment comparisons, and direct numerical potential evaluations both inside and outside the optimal support. The analytic convexity-and-obstacle proof establishes the all-measure claim; finite checks do not substitute for that argument.

## Relationship to prior work
Santin (2022) identifies the Brownian-bridge interpolation kernel, cardinal functions, and unique equally spaced **deterministic** nodes minimizing the uniform pointwise power function. That theorem does not optimize the **expectation** of squared integration error over iid sampling laws, nor determine a positive-length truncated density. Briol, Oates, Cockayne, Chen and Girolami (2017) emphasize the importance of choosing the iid sampling law in kernel quadrature and study sampling-dependent integration error, but their displayed optimization (equation (3)) orders the supremum over functions and sampling expectation differently. Hayakawa, Oberhauser and Lyons (2023) develop general Nyström and kernel-quadrature bounds, including optimal weights at fixed nodes, not this exact finite-two-draw distributional design. General design-potential arguments are classical and are used here only after an explicit nonstandard equilibrium density and obstacle profile have been established.

## Limitations
This result addresses exactly two iid draws, the first-order Brownian-bridge kernel, uniform target integration, noiseless point evaluations, and the expected squared fixed-node worst-case error. Deterministic unequal or correlated-node designs can perform better. This does not solve the alternative worst-integrand-after-expectation objective, higher-order Sobolev kernels, higher-dimensional kernels, general sample counts, or noisy quadrature. A specialized unlocated prior result on optimal cubic spacings could affect publication priority; the mathematical claim is self-contained, not an assertion of independent scholarly certification.

## References
1. G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959v1, first public 2022-10-28, Sections 2, 4, 5, https://arxiv.org/abs/2210.15959.
2. F.-X. Briol, C. J. Oates, J. Cockayne, W. Y. Chen and M. Girolami, *On the Sampling Problem for Kernel Quadrature*, arXiv:1706.03369v1, first public 2017-06-11, Sections 1–3, https://arxiv.org/abs/1706.03369.
3. S. Hayakawa, H. Oberhauser and T. Lyons, *Sampling-based Nyström Approximation and Kernel Quadrature*, arXiv:2301.09517v1, first public 2023-01-23, PMLR 202 (2023), Sections 2–5 and Appendix, https://proceedings.mlr.press/v202/hayakawa23a.html.
4. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature, energy minimization, and space-filling design*, SIAM/ASA J. Uncertainty Quantification 8 (2020), 959–1011, https://doi.org/10.1137/18M1210332 (context for classical energy/potential design methods).
