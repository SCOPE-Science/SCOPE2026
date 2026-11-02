# Exact two-step Gaussian Euler mesh phases and a residual-quantile terminal-error gap

## Finding

**Theorem (finite-grid phase diagram and surrogate mismatch).** For any \(c>0\), take the scalar Gaussian transport problem
\[
\dot X(s)=-csX(s),\quad 0\le s\le1,\quad X(0)\sim\mathcal N(0,1),
\]
and its two-step, left-endpoint explicit Euler discretization on \(0<t<1\). Define \(r_c=e^{-c/2}\) and \(M_c(t)=1-ct(1-t)\). The exact terminal Wasserstein error is
\[
E_c(t)=W_2\bigl(\mathcal N(0,M_c(t)^2),\mathcal N(0,e^{-c})\bigr)
=\bigl|\,|M_c(t)|-r_c\,\bigr|.
\]
Its best attainable value is
\[
\inf_{0<t<1}E_c(t)=\max\{0,1-c/4-r_c\}.
\]
There are unique positive constants \(c_+\in(3,4)\) and \(c_-\in(4,5)\) satisfying, respectively,
\[
c_+=4(1-e^{-c_+/2}),\qquad c_-=4(1+e^{-c_-/2}).
\]
The number of distinct interior grids giving exactly zero terminal \(W_2\) is \(0,1,2,3,4\), respectively, on \((0,c_+),\{c_+\},(c_+,c_-),\{c_-\},(c_-,\infty)\). Every such grid is given, when its square root is real, by
\[
t^{(+)}_{\pm}=\frac12\left(1\pm\sqrt{1-\frac{4(1-r_c)}{c}}\right),\quad
t^{(-)}_{\pm}=\frac12\left(1\pm\sqrt{1-\frac{4(1+r_c)}{c}}\right).
\]
Here the first family has positive multiplier and the second family has negative multiplier; the subscript signs enumerate the two reflected grids. At \(c=c_-\) the negative-multiplier roots merge into a single grid. On the negative branch, the terminal *law* is exact, yet the mean squared paired-particle discrepancy is \(4e^{-c}\).

The source-motivated Euler local-residual quantile is **not** terminal-error competitive at this two-step budget. At \(c=4\), let \(q\) be the unique median of the density proportional to \(\sqrt{|4s^2-1|}\) on \([0,1]\):
\[
\int_0^q\sqrt{|4s^2-1|}\,ds=\frac12\int_0^1\sqrt{|4s^2-1|}\,ds.
\]
Then \(1/2<q<2/3\) and
\[
E_4(q)>e^{-2}-\frac19>0,
\qquad \inf_{0<t<1}E_4(t)=0.
\]
The mismatch persists for the **strictly contractive** analytic drifts \(\dot X=-(4s+\epsilon)X\), for every sufficiently small \(\epsilon>0\), even after replacing their nonnegative residual profile by an arbitrarily sufficiently small strictly positive regularization. In these perturbed models a two-step grid attains exact terminal \(W_2=0\), whereas the unique regularized local-surrogate minimizer has a positive terminal error. Thus there is no finite constant multiplying the globally best terminal \(W_2\) that universally bounds the endpoint error of this propagated-residual quantile rule on these smooth contracting Gaussian flows.

## Assumptions and scope

Everything is one-dimensional, in exact arithmetic, on the fixed time interval \([0,1]\), with exactly two **left-endpoint explicit Euler** steps and an interior split \(t\in(0,1)\). The initial variable is standard normal. The finite-surrogate objective for Euler and two cells is
\[
\mathcal S_1(t)=\left(\int_0^t\sqrt{W(s)}\,ds\right)^2+
\left(\int_t^1\sqrt{W(s)}\,ds\right)^2,
\]
where \(W=K(1,s)R_1(s)\) is the terminally propagated density-active local Euler defect. The exact residual has an isolated zero at \(c=4\); the minimizer remains unique because \(\sqrt W\) has strictly positive mass in every nontrivial interval. When comparison requires the source theorem's everywhere-positive weight hypothesis, take \(W+\delta\) for \(\delta>0\), and then let \(\delta\downarrow0\). No guarantee is claimed for finite-\(N\) terminal errors from the source's *surrogate* theorem.

## Proof

**1. Exact flow, discretization, and minimax.** Integration gives \(X(s)=e^{-cs^2/2}X(0)\), hence terminal standard deviation \(r_c\). The first Euler stage is the identity, because the drift vanishes at \(s=0\). The second stage multiplies by \(1-ct(1-t)\). The scalar centered Gaussian \(W_2\) identity \(W_2(\mathcal N(0,a^2),\mathcal N(0,b^2))=\bigl||a|-|b|\bigr|\) proves the displayed error exactly, including when the numerical map reverses sign. Since \(t(1-t)\in(0,1/4]\), \(M_c(t)\in[1-c/4,1)\). If \(1-c/4>r_c\), its smallest absolute-value deviation occurs at \(t=1/2\) and equals \(1-c/4-r_c\). Otherwise \(+r_c\) belongs to this interval and the minimum is zero. This proves the infimum formula, including boundary cases.

**2. Threshold uniqueness and all exact grids.** A zero terminal error requires \(M_c(t)=r_c\) or \(M_c(t)=-r_c\). Solving \(t(1-t)=(1\mp r_c)/c\) gives the four formula branches. The positive branch exists precisely when \(c\ge4(1-r_c)\); the negative branch precisely when \(c\ge4(1+r_c)\). The function \(g_+(c)=c-4(1-e^{-c/2})\) has \(g_+(0)=0\), \(g_+'(0)=-1\), and \(g_+''(c)=e^{-c/2}>0\); it therefore has exactly one positive zero \(c_+\), lying between three and four. The function \(g_-(c)=c-4(1+e^{-c/2})\) increases strictly and crosses zero once between four and five. At either threshold the corresponding reflected roots merge at \(1/2\). The positive and negative roots cannot coincide because \(r_c>0\), giving the five root counts. At a negative root, \(X^{\mathrm{Euler}}(1)=-r_c X(0)\) versus \(X(1)=r_c X(0)\), so the squared paired difference has expectation \(4r_c^2=4e^{-c}\).

**3. Propagated local profile.** For a linear drift \(v(s,x)=\lambda(s)x\), its Euler material acceleration is \(a_v=(\lambda'(s)+\lambda(s)^2)x\). In a nondegenerate one-dimensional Gaussian, this vector field is already a Wasserstein gradient, so the local density-active residual is
\[
R_1(s)=\frac12|\lambda'(s)+\lambda(s)^2|\,\sigma(s),
\]
where \(\sigma(s)\) is the exact standard deviation. Propagation of a standard-deviation perturbation from \(s\) to \(1\) multiplies it by \(K(1,s)=\sigma(1)/\sigma(s)\). Thus
\[
W(s)=K(1,s)R_1(s)=\frac{\sigma(1)}2|\lambda'(s)+\lambda(s)^2|.
\]
For \(\lambda(s)=-4s\), \(\sigma(1)=e^{-2}\) and \(W(s)=2e^{-2}|4s^2-1|\). Positive constant factors do not change the quantile. The finite two-cell surrogate is a sum of squares of positive interval masses, hence it is uniquely minimized by the equal-mass (median) split.

**4. Strict separation of the surrogate median.** Set \(f(s)=\sqrt{|4s^2-1|}\). The first-half mass is exactly
\[
\int_0^{1/2}f(s)\,ds=\frac\pi8.
\]
On \([1/2,1]\), \(f(s)=\sqrt{4s^2-1}\) is strictly concave (its second derivative equals \(-4(4s^2-1)^{-3/2}\) in the interior). The trapezoidal chord therefore bounds its integral below by \(\sqrt3/4>\pi/8\), proving \(q>1/2\). Its chord on \([1/2,2/3]\) gives
\[
\int_0^{2/3}f\ge\frac\pi8+\frac{\sqrt7}{36}.
\]
Jensen's inequality on \([2/3,1]\) gives
\[
\int_{2/3}^1f\le\frac13 f(5/6)=\frac49.
\]
Since \(\pi>3\) and \(\sqrt7>5/2\), \(\pi/8+\sqrt7/36>4/9\), proving \(q<2/3\). At \(c=4\) the numerical multiplier is \(M_4(q)=(2q-1)^2<1/9<e^{-2}\) (using \(e<3\)); hence \(E_4(q)>e^{-2}-1/9>0\). But \(t=(1\pm e^{-1})/2\) gives \(M_4(t)=e^{-2}\) and exact terminal Wasserstein error zero.

**5. Robust, strictly contracting counterexample.** Put \(\lambda_\epsilon(s)=-(4s+\epsilon)\) with \(\epsilon>0\), so \(\partial_xv<0\) uniformly, \(\sigma_\epsilon(1)=e^{-2-\epsilon}\), and
\[
M_\epsilon(t)=(1-\epsilon t)\bigl[1-(4t+\epsilon)(1-t)\bigr].
\]
At \(\epsilon=0\), the positive-multiplier exact-grid roots are \(t_\pm=(1\pm e^{-1})/2\). Their derivative with respect to \(t\) of \(M_0(t)-e^{-2}\) is \(8t-4=\pm4e^{-1}\ne0\). The implicit-function theorem therefore continues each root to an interior \(t_\pm(\epsilon)\) satisfying \(M_\epsilon(t_\pm(\epsilon))=e^{-2-\epsilon}\) for all sufficiently small \(\epsilon>0\). Meanwhile
\[
W_{\epsilon,\delta}(s)=\frac{e^{-2-\epsilon}}2\Bigl(\bigl|(4s+\epsilon)^2-4\bigr|+\delta\Bigr),\quad\delta>0,
\]
is strictly positive. Its unique equal-mass quantile \(q_{\epsilon,\delta}\) depends continuously on \((\epsilon,\delta)\) as both tend to zero, by uniform continuity of the profiles and strict monotonicity of the limiting cumulative mass. It converges to \(q\). Continuity of the exact terminal Gaussian error then keeps \(E_\epsilon(q_{\epsilon,\delta})\) bounded away from zero while \(E_\epsilon(t_\pm(\epsilon))=0\). No fixed multiplicative terminal-error guarantee can hold. This is a finite-\(N\) phenomenon and does not contradict asymptotic surrogate optimality.

## Verification

Run `python3 check.py` (standard library only). The script checks the two transition constants, the exact-grid root counts, 4,000 independent numerical identities between the Euler composition and the closed multiplier, the local-profile median, small positive regularizations, strictly contractive continuation roots, and the negative-branch paired-particle identity. Sample values are \(c_+\approx3.187248520080\), \(c_-\approx4.435430211514\), \(q\approx0.63916669\), and \(E_4(q)\approx0.05786581\). These finite calculations are supplementary; the infinite-parameter theorem follows from the analytic steps above. Verification assumes standard real arithmetic for the proof; floating-point roundoff affects the code's printed final decimals only.

## Relationship to prior work

Obzherin and Khrulkov (2026), Sections 4–6 and Appendix H.3, derive the density-active Euler defect, the propagated-residual weighting, and exact minimization of their finite-budget **local surrogate** by a quantile grid; they explicitly distinguish it from minimization of full nonlinear terminal error. Their Appendix H.5 exhibits an unbounded **surrogate** ratio for residual-only versus propagation-aware allocation, which is not an endpoint-Wasserstein competitiveness result. The present theorem gives a distinct exact two-step marginal-error phase diagram and a smooth strictly contracting example with zero optimal terminal error but strictly positive terminal error at the **propagation-aware** quantile. Their Appendix G.2 already uses Gaussian standard-deviation formulas; those elementary formulas are not claimed as novel here. Pierret and Galerne (2024) calculate exact Gaussian Wasserstein errors for diffusion solvers, a general precursor that does not provide this particular mesh bifurcation or positive-profile surrogate mismatch. Pei, Hu, and Gu (2025) optimize schedules by reference-trajectory dynamic programming, a different objective and mechanism.

## Limitations

This is an exact two-step, one-dimensional Gaussian example, not a claim of inferior practical image-generation performance or of any failure in the existing theorem about its stated **surrogate** objective. The phenomenon can exploit cancellation between steps and, on the negative branch, law equality without sample coupling equality. The robust counterexample invokes a sufficiently small parameter via the implicit-function theorem, not a uniform explicit admissible parameter range. Historical priority among older special-function/mesh-cancellation studies is not exhaustively established. Independent mathematical audit has not been performed.

## References

1. E. Obzherin and V. Khrulkov, *Density-Level Backward Error for Low-NFE Generative Flows*, arXiv:2610.29475v1 (first public version 21 October 2026), https://arxiv.org/html/2610.29475v1 . Sections 4–7; Appendices G, H, and N.
2. É. Pierret and B. Galerne, *Diffusion Models for Gaussian Distributions: Exact Solutions and Wasserstein Errors*, arXiv:2405.14250v1 (2024), https://arxiv.org/abs/2405.14250 .
3. J. Pei, H. Hu, and S. Gu, *Optimal Stepsize for Diffusion Sampling*, arXiv:2503.21774v1 (2025), https://arxiv.org/abs/2503.21774 .
4. S. Gao et al., *Fast Diffusion Probabilistic Model Sampling through the Lens of Backward Error Analysis*, arXiv:2304.11446 (2023), https://arxiv.org/abs/2304.11446 .
