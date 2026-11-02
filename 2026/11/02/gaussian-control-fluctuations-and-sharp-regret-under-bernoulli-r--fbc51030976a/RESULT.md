# Gaussian control fluctuations and sharp regret under Bernoulli randomized time-splitting

## Finding

A scalar dissipative instance of randomized time-splitting for linear-quadratic control has an explicit nondegenerate Gaussian limit for its pathwise optimal control, together with strictly positive and sharp leading constants for expected squared-control error and deterministic cost regret. The published general theory provides an upper convergence rate; the statements below determine the distribution and the exact leading-order coefficients for this model.

For every fixed \(T>0\), let \(h=T/N\) with integer \(N\to\infty\), and let \(u_h\) be the exact samplewise minimizer defined below. Then
\[
h^{-1/2}(u_h-u)\ \Longrightarrow\ Z=\int_0^T G_r\,dB_r
\quad\text{in }L^2(0,T),
\]
where \(Z\) is a centered Gaussian random element with covariance \(\Sigma_T=\int_0^T G_r\otimes G_r\,dr\). In addition,
\[
\|\mathbb E u_h-u\|_2=O(h),\qquad
\lim_{h\downarrow0}\frac{\mathbb E\|u_h-u\|_2^2}{h}=C_T:=\int_0^T\|G_r\|_2^2\,dr>0,
\]
and
\[
\lim_{h\downarrow0}\frac{\mathbb E[J_0(u_h)-J_0(u)]}{h}
=R_T:=\frac12\int_0^T\langle G_r,HG_r\rangle\,dr>0.
\]
These are limit constants rather than explicit elementary closed forms; the defining deterministic Volterra operators determine them uniquely and admit convergent quadrature.

## Assumptions and scope

All functions below are real and the control space is the Hilbert space \(\mathcal H=L^2(0,T)\), with inner product \(\langle f,g\rangle=\int_0^T f(t)g(t)\,dt\). The deterministic dynamics, initial state, and running cost are
\[
x'(t)=-x(t)+u(t),\quad x(0)=0,\qquad
J_0(u)=\frac12\int_0^T\bigl((x(t)-1)^2+u(t)^2\bigr)\,dt.
\]
Split the scalar coefficient \(-1\) as two dissipative subcoefficients \(a_1=0\) and \(a_2=-1\). On each interval \([jh,(j+1)h)\), select exactly one with probability \(1/2\), independently over \(j=0,\ldots,N-1\), and scale the selected subcoefficient by the reciprocal selection probability as in [1]. Thus the randomized coefficient is \(a_h(t)=-1+\xi_j\in\{0,-2\}\), where the \(\xi_j\) are independent symmetric signs. The sampled dynamics is \(x_h'=a_hx_h+u\), with zero initial state; \(J_h\) has the same tracking and control penalties as \(J_0\) but evaluates the sampled dynamics. For each entire coefficient realization, \(u_h\) minimizes \(J_h\) over the unrestricted space \(\mathcal H\). This is an *offline, pathwise* optimization, not a causal/adapted feedback theorem.

Define the bounded Volterra operator \((Kf)(t)=\int_0^t e^{-(t-s)}f(s)\,ds\), its adjoint \((K^*f)(s)=\int_s^T e^{-(t-s)}f(t)\,dt\), \(H=I+K^*K\), and the baseline optimal control and state
\[
u=H^{-1}K^*\mathbf1,\qquad x=Ku.
\]
For each \(0<r<T\), set
\[
\psi_r(s)=\mathbf1_{0<s<r}e^{-(r-s)},\qquad
\phi_r(t)=\mathbf1_{r<t<T}e^{-(t-r)},
\]
and set the deterministic \(\mathcal H\)-valued sensitivity kernel
\[
G_r=H^{-1}\left[\psi_r\langle\phi_r,\mathbf1-x\rangle-x(r)K^*\phi_r\right].
\]
Boundary values of \(G_r\) may be assigned by continuity; they do not affect the integral. The stochastic integral in the finding uses a standard one-dimensional Brownian motion \(B\) over \([0,T]\) and a deterministic square-integrable Hilbert-space integrand \(G\).

## Proof

**1. Exact operator representation.** Put \(W_h(t)=\int_0^t(a_h(s)+1)\,ds=\int_0^t\xi(s)\,ds\). Since \(W_h\) is absolutely continuous and \(W_h(0)=0\), variation of constants gives \(x_h=K_{W_h}u\), where for any \(w\in C([0,T])\) with \(w(0)=0\),
\[
(K_w f)(t)=\int_0^t e^{-(t-s)+w(t)-w(s)}f(s)\,ds.
\]
Strict convexity gives the unique optimizer
\[
u_h=\Phi(W_h),\qquad
\Phi(w)=(I+K_w^*K_w)^{-1}K_w^*\mathbf1.
\]
The positive operator \(I+K_w^*K_w\) has inverse norm at most one for all real \(w\). On the sup-norm ball \(\|w\|_\infty\le T\), the kernels \(K_w\) and their first two Fréchet derivatives with respect to \(w\) have bounds depending only on \(T\). Differentiating the uniformly invertible normal equation twice consequently gives
\[
\|\Phi(w)-\Phi(0)-D\Phi(0)[w]\|_2\le M_T\|w\|_\infty^2.
\]
This bound applies to \(W_h\), because \(\|W_h\|_\infty\le T\) for every realization.

**2. Sensitivity factorization.** Differentiating the Volterra kernel gives
\[
(DK_0[w]f)(t)=\int_0^t e^{-(t-s)}(w(t)-w(s))f(s)\,ds.
\]
For absolutely continuous \(w\) with \(w(0)=0\), Fubini's theorem and \(w(t)-w(s)=\int_s^t w'(r)\,dr\) give the rank-one factorization
\[
DK_0[w]=\int_0^T (\phi_r\otimes\psi_r)w'(r)\,dr.
\]
Differentiation of the normal equation \((I+K_w^*K_w)\Phi(w)=K_w^*\mathbf1\) therefore gives
\[
D\Phi(0)[w]=H^{-1}\left[(DK_0[w])^*(\mathbf1-x)-K^*(DK_0[w])u\right]
=\int_0^T G_r w'(r)\,dr.
\]
Here \(\langle\psi_r,u\rangle=x(r)\). The \(\mathcal H\)-valued map \(r\mapsto G_r\) is continuous, in particular bounded and square-integrable.

**3. Distributional limit and moment control.** On a mesh cell, \(W_h'=\xi_j\), so
\[
\frac{D\Phi(0)[W_h]}{\sqrt h}
=\sqrt h\sum_{j=0}^{N-1}\xi_j\,\overline G_j,
\qquad \overline G_j=\frac1h\int_{jh}^{(j+1)h}G_r\,dr.
\]
For any finite set of Hilbert-space test vectors, the Lindeberg central limit theorem applies to these independent centered terms: individual increments are bounded by \(\sqrt h\sup_r\|G_r\|_2\), and their covariance operators converge by the Riemann-sum rule to \(\Sigma_T=\int G_r\otimes G_rdr\). To justify convergence in \(\mathcal H\), approximate the compact continuous image \(\{G_r:r\in[0,T]\}\) uniformly by a finite-dimensional subspace. The expected squared norm of the discarded projection is bounded by its squared approximation error times \(T\); hence the array is tight and its limit is the asserted Hilbert-valued Gaussian element.

The partial sums of the signs form a martingale. The maximal fourth-moment inequality and the fourth moment of a symmetric random walk give
\[
\mathbb E\|W_h\|_\infty^4\le M'_T h^2,
\qquad \mathbb E\|W_h\|_\infty^2=O(h).
\]
The second-order Taylor remainder is therefore \(O_{L^2(\Omega;\mathcal H)}(h)\). It vanishes after division by \(\sqrt h\). This proves the Hilbert-space Gaussian limit; the stochastic-integral representation follows from its covariance, or equivalently deterministic-kernel stochastic Fubini applied to the Brownian limit of \(W_h/\sqrt h\).

The derivative term has exactly zero expectation. Its second moment satisfies
\[
\frac1h\mathbb E\|D\Phi(0)[W_h]\|_2^2
=h\sum_{j=0}^{N-1}\|\overline G_j\|_2^2\longrightarrow\int_0^T\|G_r\|_2^2\,dr.
\]
The above Taylor remainder, Cauchy–Schwarz, and the variance bound imply \(\|\mathbb Eu_h-u\|_2=O(h)\), and imply the claimed exact mean-square limit. The quadratic identity
\[
J_0(v)-J_0(u)=\frac12\langle v-u,H(v-u)\rangle
\]
holds for every \(v\in\mathcal H\) because \(u\) solves the deterministic normal equation. Applying the same covariance limit with bounded \(H\) establishes the regret limit.

**4. Strict nondegeneracy.** The deterministic state satisfies the boundary-value problem
\[
-x''(t)+2x(t)=1,\quad x(0)=0,\quad x'(T)+x(T)=0.
\]
The Green kernel for this positive Dirichlet–Robin problem is strictly positive at interior points, so \(x(r)>0\) for all \(0<r<T\). For \(s\in(r,T)\), the first term of \(HG_r\) vanishes, while the second is \(-x(r)(K^*\phi_r)(s)\), strictly negative for \(r<s<T\). Thus \(G_r\ne0\) for every interior \(r\). Consequently \(C_T>0\) and, since \(H\ge I\), also \(R_T>0\). This proves that the order-\(h\) expected squared-control error and regret constants are sharp for every \(T>0\).

## Verification

The standalone script `verify.py` requires Python 3 and NumPy (see `requirements.txt`). It reconstructs the discrete normal equations and continuous sensitivity kernel by independent matrix formulas, checks the directional derivative against a centered finite difference, compares the random-slope impulse representation with direct differentiation, and computes positive approximations of \(C_T\) on refining midpoint grids. Run `python verify.py` in the extracted package directory. Numerical quadrature and finite differences are corroboration only; the preceding proof supplies the infinite-dimensional and limit statements.

## Relationship to prior work

Veldman and Zuazua [1] introduce independent random time-splitting, use the same rescaling of selected dissipative suboperators, allow controls optimized after observing the sampled coefficient path, and prove general mean-square control convergence bounds. The present scalar specialization retains their exact coefficient rule but identifies the Gaussian first-order sensitivity law, its covariance, a strictly positive exact asymptotic squared-error constant and the corresponding deterministic-objective regret constant. It does not claim the original time-splitting framework or the order-\(\sqrt h\) upper convergence bound as new.

Na and Anitescu [2] analyze exponential decay of sensitivity in discrete nonlinear dynamic programming, rather than the Gaussian fluctuation of this independent time-splitting rule. Ou and collaborators [3] examine stochastic linear-quadratic control with process noise and polynomial-chaos methods, distinct from an offline minimizer of a randomly perturbed system matrix. Classical functional central limit theorems and smooth-map sensitivity principles are mathematical tools, not contributions claimed here.

## Limitations

This is a scalar, finite-horizon, full-path-information, fixed-cost, independent two-choice dissipative splitting example with no terminal state penalty and exact optimization/arithmetic. The limiting constants are defined through deterministic integral operators and are not asserted to be elementary formulas. The theorem is not about general matrix decompositions, online/adapted controls, nonquadratic costs, or discrete implementations of the state optimizer. Gaussian convergence alone would not establish moment convergence; the latter uses an explicit fourth-moment/Taylor remainder estimate. An equivalent special-case theorem might occur in earlier random-evolution sensitivity literature under other terminology; priority requires independent examination.

## References

[1] D. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798 (first public version 28 September 2021), https://arxiv.org/abs/2109.13798. Full-text Sections 2–3 and appendices inspected.

[2] S. Na and M. Anitescu, *Exponential Decay in the Sensitivity Analysis of Nonlinear Dynamic Programming*, arXiv:1912.06734, https://arxiv.org/abs/1912.06734.

[3] R. Ou and collaborators, *A Polynomial Chaos Approach to Stochastic LQ Optimal Control*, arXiv:2311.17596, https://arxiv.org/abs/2311.17596.
