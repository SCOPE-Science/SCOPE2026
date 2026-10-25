# Exact stationary error floors for one-direction finite-difference Newton sketches

## Finding

Consider the noise-free, strongly convex planar quadratic
\[
f(x)=\frac12\bigl(a x_1^2+b x_2^2\bigr),\qquad a,b>0,
\]
and the one-direction zeroth-order randomized subspace Newton method with **fixed** forward-difference radius \(h>0\), unit step length, and independent unit directions. Compare (H) a uniform direction on the unit circle (equivalently, a normalized two-dimensional standard Gaussian), and (C) a uniformly sampled signed coordinate direction \(\{\pm e_1,\pm e_2\}\). Both are valid unit-orthonormal one-column sketches; both require the same three function values per un-cached Hessian-and-gradient estimate.

For either direction law, the iterates converge in distribution and in second moments to a unique stationary law with finite second moment, for every deterministic starting point. The stationary means vanish. In the orthonormal eigenbasis of the Hessian, their stationary second-moment matrices are exactly
\[
\begin{aligned}
\lim_{n\to\infty}\mathbb E[x_nx_n^\mathsf T]\big|_{\mathrm H}
&=\frac{h^2}{24}\operatorname{diag}\left(
\frac{3a+b+2\sqrt{ab}}a,\frac{a+3b+2\sqrt{ab}}b\right),\\
\lim_{n\to\infty}\mathbb E[x_nx_n^\mathsf T]\big|_{\mathrm C}
&=\frac{h^2}{4}I_2.
\end{aligned}
\]
Consequently the asymptotic expected objective errors are
\[
\boxed{\mathcal E_{\mathrm H}=\frac{h^2}{12}(a+b+\sqrt{ab}),\qquad
\mathcal E_{\mathrm C}=\frac{h^2}{8}(a+b)}
\]
and their **exact strict anisotropy gap** is
\[
\boxed{\mathcal E_{\mathrm C}-\mathcal E_{\mathrm H}
=\frac{h^2}{24}(\sqrt a-\sqrt b)^2.}
\]
In particular, a uniform random direction gives strictly smaller *limiting expected objective error* whenever \(a\ne b\), with equality at \(a=b\). This is not a blanket domination in transient convergence: the sharp expected squared-error coupling factors in the Hessian metric are respectively \(\max\{\sqrt a,\sqrt b\}/(\sqrt a+\sqrt b)\) for H and \(1/2\) for C. At the optimizer \(x_0=0\), both methods have identical expected error after one step, \(h^2(a+b)/16\).

## Assumptions and scope

Fix any \(a,b,h>0\), a deterministic \(x_0\in\mathbb R^2\), and independent identically distributed directions \(u_n\) drawn at each step from either specified law. Use exact function evaluations and arithmetic. The forward-difference projected gradient and directional Hessian are
\[
\widehat g(x,u)=\frac{f(x+hu)-f(x)}h,\qquad
\widehat d(x,u)=\frac{f(x+2hu)-2f(x+hu)+f(x)}{h^2}.
\]
The update is
\[
x_{n+1}=x_n-\frac{\widehat g(x_n,u_n)}{\widehat d(x_n,u_n)}u_n.
\]
The estimator uses forward, not centered, differences. The Hessian in the denominator is the exact directional Hessian for these quadratics. There is no line search, step rejection, clipping, or finite-precision noise. The term *stationary error* refers to the limit of \(\mathbb E f(x_n)\), not a claim that every sample path converges to a fixed point.

## Proof

**1. Exact update.** Put \(H=\operatorname{diag}(a,b)\). Direct finite differences give
\[
\widehat g=u^\mathsf THx+\frac h2 u^\mathsf THu,
\qquad \widehat d=u^\mathsf THu>0.
\]
Thus, for \(z=H^{1/2}x\), \(w=H^{1/2}u\), and \(v=w/\|w\|\),
\[
\boxed{z_{n+1}=(I-v_nv_n^\mathsf T)z_n-\frac h2w_n.}\tag{1}
\]
The reflection \(u\mapsto-u\) fixes the projector and changes the sign of the forcing. Therefore the cross terms in the expected covariance recursion vanish. Both direction laws are invariant under sign changes of either coordinate.

**2. Stationarity and its convergence.** Couple two copies of (1) with the same successive directions. Their difference obeys \(\Delta z_{n+1}=(I-v_nv_n^\mathsf T)\Delta z_n\), so
\[
\mathbb E[\|\Delta z_{n+1}\|^2\mid\Delta z_n]
=\Delta z_n^\mathsf T(I-\mathbb E[vv^\mathsf T])\Delta z_n.
\]
For the signed coordinates, \(\mathbb E[vv^\mathsf T]=I_2/2\). For uniform-circle directions, write \(r=\sqrt a\), \(s=\sqrt b\). The angular integral in Step 3 gives
\[
\mathbb E[vv^\mathsf T]=\operatorname{diag}\left(\frac r{r+s},\frac s{r+s}\right).
\]
Both are positive definite. Hence the transition is a strict contraction on probability distributions with finite second moment in squared \(2\)-Wasserstein distance, with the respective sharp one-step constants asserted above. Because the additive term has bounded second moment, the usual synchronous-coupling fixed-point argument supplies a unique stationary law and convergence from every initial finite-second-moment distribution. Reflection equivariance makes its mean zero and its covariance diagonal. This proves existence and justifies passing to the limiting second moments below.

**3. The angular moments.** For uniform \(u=(\cos\theta,\sin\theta)\), let
\[
X=v_1^2=\frac{a\cos^2\theta}{a\cos^2\theta+b\sin^2\theta}.
\]
Integrating with \(t=\tan\theta\) on the four quadrants gives
\[
m:=\mathbb E X=\frac r{r+s}.
\]
Differentiation under the integral (valid since \(a,b>0\)) yields
\[
\beta:=\mathbb E[X(1-X)]
=a\,\partial_a m
=\frac{rs}{2(r+s)^2}.
\]
The orthogonal complement projector \(I-vv^\mathsf T\) has diagonal entries \(1-X,X\), so its stationary diagonal covariance in \(z\)-coordinates, \(c_1,c_2\), satisfies the exact linear system
\[
\begin{pmatrix}m+\beta&-\beta\\-\beta&1-m+\beta\end{pmatrix}
\begin{pmatrix}c_1\\c_2\end{pmatrix}
=\frac{h^2}{8}\begin{pmatrix}a\\b\end{pmatrix}.
\]
The determinant is \(m(1-m)+\beta=3\beta>0\). Solving gives
\[
\boxed{c_1=\frac{h^2}{24}(3a+b+2\sqrt{ab}),\qquad
c_2=\frac{h^2}{24}(a+3b+2\sqrt{ab}).}
\]
Conjugation by \(H^{-1/2}\) gives the claimed covariance in the original coordinates, while the limiting expected objective is \((c_1+c_2)/2\).

**4. Coordinate law and strict comparison.** For \(u=\pm e_i\), the selected coordinate is replaced, independently of its former value, by \(-hu_i/2\); the unselected coordinate is unchanged. Each coordinate is selected eventually with probability one, and its most recent sign is symmetric. The unique stationary covariance is therefore \(h^2I_2/4\). Thus \(\mathcal E_{\mathrm C}=h^2(a+b)/8\). Subtraction yields the displayed nonnegative perfect square, vanishing only for \(a=b\).

**5. One-step boundary.** Starting from \(x_0=0\), equation (1) gives \(x_1=-hu/2\). Both direction laws satisfy \(\mathbb E[uu^\mathsf T]=I_2/2\), so \(\mathbb E f(x_1)=h^2(a+b)/16\). Hence the strict asymptotic difference does not follow from a different initial expected noise injection.

## Verification

The included standalone `verify.py` reconstructs the projected gradient and Hessian directly from three function evaluations; checks their agreement with (1) at randomized inputs; computes the full three-coordinate symmetric covariance fixed point using independent high-resolution angular quadrature rather than the closed-form angular moments; checks the derived angular identities and rational-square curvature comparisons; and simulates stationary trajectories with a fixed random seed. It uses only the Python standard library. At package preparation, it passed 1,450 checks. The exact theorem is proved by the steps above; no finite test establishes convergence for every parameter choice.

## Relationship to prior work

Berglund, Khirirat and Wang's zeroth-order randomized subspace Newton method [1] supplies the finite-difference update and general strongly-convex convergence estimates, but the inspected initial preprint does not give this exact two-policy, fixed-radius stationary covariance or the perfect-square anisotropy gap. Its numerical SQP variant includes additional safeguards not considered here. Kozak, Molinari, Rosasco, Tenorio and Villa [2] study a **different**, first-order projected finite-difference descent method, including coordinate and Haar direction choices. In Remark 4.2 they explicitly identify a tailored quadratic convergence analysis as future work; their fixed-radius PL bounds give an order-of-magnitude neighborhood, not the stationary constants for the Hessian-normalized update here. Berahas, Cao, Choromanski and Scheinberg [3] analyze errors in gradient approximations and line-search/descent requirements, rather than a stationary covariance comparison for one-direction finite-difference Newton iteration. The original exact-gradient randomized subspace Newton method of Gower, Kovalev, Lieder and Richtárik [4] uses exact derivative information, so its error-free contraction statements do not imply the fixed nonzero-difference-radius stationary law. The exact Gaussian/Haar angular moments are elementary ingredients, not an originality claim by themselves.

## Limitations

This is a complete planar result for the stated unguarded, exact-arithmetic, quadratic one-direction method; it is not a general-dimensional theorem, a superiority claim for all starting points or finite times, or a result about discrete line searches, stochastic function-value noise, nonquadratic losses, or finite-precision behavior. The comparison is between **signed** uniformly sampled coordinates and uniform-circle directions at equal fixed forward-difference radius. A shifted optimum can be reduced to the present centered case by translating coordinates. A centered-difference gradient has no curvature bias on quadratics and is outside the claim. A plausible equivalent formula may exist in more specialized stochastic approximation literature, and publication priority is not independently certified.

## References

[1] E. Berglund, S. Khirirat and X. Wang, *Zeroth-Order Randomized Subspace Newton Methods*, arXiv:2202.04612v1 (first public 2022-02-09), https://arxiv.org/html/2202.04612v1.

[2] D. Kozak, C. Molinari, L. Rosasco, L. Tenorio and S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941v1 (first public 2021-07-08), https://arxiv.org/abs/2107.03941.

[3] A. S. Berahas, L. Cao, K. Choromanski and K. Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization*, arXiv:1905.01332v1 (first public 2019-05-03), https://arxiv.org/abs/1905.01332.

[4] R. M. Gower, D. Kovalev, F. Lieder and P. Richtárik, *RSN: Randomized Subspace Newton*, arXiv:1905.10874 (first public 2019-05-26), https://arxiv.org/abs/1905.10874.
