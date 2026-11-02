# A singular optimal-sampling limit for randomized two-mode semigroups

## Finding

A reciprocal-probability randomized time-splitting method for a two-mode dissipative system has an exact and unique minimax mean-square contraction design at every positive step size. Unlike the design minimizing variance of the sampled generator, its contraction-optimal design always samples the *faster* mode less often than the slower mode. As the physical time step vanishes, the fast-mode sampling probability becomes proportional to the step size, and the corresponding numerical trajectories converge to a nondegenerate Poisson-jump limit instead of the original deterministic solution. Thus optimizing worst-case expected energy decay, even to its exact continuous-time value, need not yield a convergent time discretization.

More precisely, let \(a>b>0\), \(h>0\), and \(0<p<1\). Put
\[
q_a(p,h)=1-p\bigl(1-e^{-2ah/p}\bigr),\qquad
q_b(p,h)=1-(1-p)\bigl(1-e^{-2bh/(1-p)}\bigr).
\]
For every integer \(n\ge1\), the sharp worst-initial-vector expected squared-norm ratio after \(n\) steps is
\[
\sup_{x\ne0}\frac{\mathbb E\|X_n\|_2^2}{\|x\|_2^2}
=\bigl[\max\{q_a(p,h),q_b(p,h)\}\bigr]^n.
\]
There is exactly one minimizer \(p_h\in(0,1/2)\), characterized by \(q_a(p_h,h)=q_b(p_h,h)\). This is opposite to the generator-variance minimizing probability \(p_{\rm var}=a/(a+b)>1/2\).

Let \(\kappa>0\) be the unique solution of
\[
\kappa\bigl(1-e^{-2a/\kappa}\bigr)=2b.
\]
Then
\[
\lim_{h\downarrow0}\frac{p_h}{h}=\kappa,
\qquad
\lim_{h\downarrow0}\frac{1-\max\{q_a(p_h,h),q_b(p_h,h)\}}{h}=2b.
\]
For every fixed \(T>0\), take \(n_h=\lfloor T/h\rfloor\) independent steps and use \(p=p_h\) for that mesh. Their terminal state satisfies
\[
X_{n_h}\ \Rightarrow\
\begin{pmatrix}x_1e^{-aN/\kappa}\\x_2e^{-bT}\end{pmatrix},
\qquad N\sim\operatorname{Poisson}(\kappa T).
\]
In particular,
\[
\lim_{h\downarrow0}\sup_{x\ne0}
\frac{\mathbb E\|X_{n_h}\|_2^2}{\|x\|_2^2}
=e^{-2bT},
\]
which equals the exact semigroup's worst-case squared-norm ratio, but for any \(x_1\ne0\) the error from the exact terminal state does *not* tend to zero in mean square. Its sharp positive limit is
\[
|x_1|^2\left[e^{-2bT}
-2e^{-aT-\kappa T(1-e^{-a/\kappa})}+e^{-2aT}\right]>0.
\]
For any fixed \(p\in(0,1)\) independent of \(h\), the same scheme instead converges in mean square to the exact state as \(h\downarrow0\). Therefore the loss of consistency is caused by optimizing the sampling probability anew at each mesh size.

At the opposite endpoint \(h\to\infty\), the contraction-optimal probability obeys
\[
p_h=\frac12-\frac14e^{-4bh}+o(e^{-4bh}),
\]
and the sharp contraction factor approaches \(1/2\); the generator-variance choice has limiting contraction factor \(a/(a+b)\), giving the exact asymptotic factor ratio \(2a/(a+b)>1\).

## Assumptions and scope

The original unforced linear differential equation is
\[
\dot x=Ax,\quad A=\operatorname{diag}(-a,-b),\quad x(0)=(x_1,x_2)^\top\in\mathbb R^2,
\]
where \(a>b>0\) are fixed. Split \(A=A_1+A_2\), with \(A_1=\operatorname{diag}(-a,0)\) and \(A_2=\operatorname{diag}(0,-b)\). At each step of physical duration \(h>0\), independently select \(A_1/p\) with probability \(p\) or \(A_2/(1-p)\) with probability \(1-p\), then evolve the selected constant-coefficient system **exactly** for that duration. This keeps the sampled infinitesimal generator unbiased: \(\mathbb E\widetilde A=A\). The selection is independent across steps; the same fixed \(p\) is used within a mesh, but the optimizer \(p_h\) may depend on the mesh size. No spatial discretization, forcing, time-stepping approximation inside a selected subflow, or adaptive state-dependent selection is included. Terminal time uses \(n_h=\lfloor T/h\rfloor\); the harmless final interval below \(h\) is omitted, so the exact reference time tends to \(T\).

The optimization objective is the sharp *worst-initial-vector expected squared energy after a fixed positive number of steps*, equivalently the largest diagonal entry of the expected squared propagator. It is **not** mean-square error relative to the true solution, nor expected physical-work efficiency. The generator-variance comparator minimizes \(\mathbb E\|\widetilde A-A\|_2^2\) with the matrix operator norm taken inside the expectation; in this two-block setting the squared generator deviation has equal operator norm in the two outcomes and equals the formula in the proof. This is the variance proxy of the motivating time-splitting construction, not the variance of the numerical state.

## Proof

**1. Exact finite-horizon law.** Let \(N_n\) count the selections of \(A_1/p\) in \(n\) independent trials, so \(N_n\sim\operatorname{Bin}(n,p)\). Diagonality and commutation of the selected exact subflows give the pathwise identity
\[
X_n=\begin{pmatrix}x_1e^{-ahN_n/p}\\x_2e^{-bh(n-N_n)/(1-p)}\end{pmatrix}.
\]
The binomial probability-generating function yields
\[
\mathbb E\|X_n\|_2^2
=|x_1|^2(1-p+pe^{-2ah/p})^n
 +|x_2|^2(p+(1-p)e^{-2bh/(1-p)})^n.
\]
The stated worst-initial-vector formula follows exactly, with equality attained by whichever coordinate has larger scalar factor.

**2. Uniqueness and direction of optimal sampling.** For \(c>0\) and \(u>0\), let \(F_c(u)=u(1-e^{-c/u})\). Then
\[
F_c'(u)=1-(1+c/u)e^{-c/u}>0,
\]
by the strict inequality \(e^z>1+z\) for \(z>0\). Consequently \(q_a(p,h)=1-F_{2ah}(p)\) strictly decreases as \(p\) increases, while \(q_b(p,h)=1-F_{2bh}(1-p)\) strictly increases. As \(p\downarrow0\), the pair converges to \((1,e^{-2bh})\); as \(p\uparrow1\), it converges to \((e^{-2ah},1)\). Hence there is exactly one crossing, and the pointwise maximum decreases strictly before and increases strictly after it. Moreover, at \(p=1/2\),
\[
q_a(1/2,h)=\tfrac12(1+e^{-4ah})
<\tfrac12(1+e^{-4bh})=q_b(1/2,h),
\]
so the crossing lies strictly below \(1/2\). Raising the maximum to any positive integer power preserves the optimizer.

**3. Opposite optimizer for the generator-variance proxy.** With probability \(p\), \(\widetilde A-A=\operatorname{diag}(-a(1-p)/p,b)\); with complementary probability it equals \(\operatorname{diag}(a,-bp/(1-p))\). The mean-square operator-norm deviation used in the motivating construction reduces, after grouping the two scalar blocks, to
\[
\mathrm{Var}_{\rm gen}(p)
=\max\left\{a^2\frac{1-p}{p},\ b^2\frac{p}{1-p}\right\}.
\]
To verify this exact expression, note the two deviations are scalar multiples of the common diagonal matrix \(\operatorname{diag}(-a(1-p),bp)\), with multipliers \(1/p\) and \(-1/(1-p)\). Thus the expected square of their operator norms is
\[
\max\{a^2(1-p)^2,b^2p^2\}\left(\frac1p+\frac1{1-p}\right).
\]
The first branch decreases in \(p\), the second increases, and their unique crossing is \(p_{\rm var}=a/(a+b)>1/2\). Therefore the two sampling design objectives make strictly opposite choices for every \(h>0\).

**4. Small-step singular optimum.** The crossing condition is
\[
p_h(1-e^{-2ah/p_h})=(1-p_h)(1-e^{-2bh/(1-p_h)}).
\]
First \(p_h\to0\) as \(h\downarrow0\): otherwise, along a sequence bounded away from zero, division by \(h\) gives a left limit \(2a\) and a right limit \(2b\), a contradiction. Here \(p_h<1/2\) keeps the right-hand expansion uniform. Its right side divided by \(h\) therefore tends to \(2b\). Put \(v_h=p_h/h\) and
\[
G(v)=v(1-e^{-2a/v}),\quad v>0;\qquad G(0)=0.
\]
The crossing reads \(G(v_h)\to2b\). The function \(G\) is continuous and strictly increasing from \(0\) to \(2a\), as seen from the same derivative calculation and the exponential limit. Since \(0<2b<2a\), the unique \(\kappa\in(0,\infty)\) with \(G(\kappa)=2b\) exists, and \(v_h\to\kappa\). The common contraction factor is \(1-(1-p_h)(1-e^{-2bh/(1-p_h)})=1-2bh+o(h)\). No assumption of a uniform lower bound for \(p_h\) is made.

**5. Poisson terminal law and positive exact-solution error.** Since \(n_h p_h\to\kappa T\) and \(p_h\to0\), binomial-to-Poisson convergence gives \(N_{n_h}\Rightarrow N\sim\operatorname{Poisson}(\kappa T)\). Furthermore \(hN_{n_h}/p_h=N_{n_h}/(p_h/h)\Rightarrow N/\kappa\), and \(h(n_h-N_{n_h})/(1-p_h)\to T\) in probability. Continuity of the exponential function proves the stated joint terminal-state limit. Boundedness of all exponential factors by one permits passage to first and second moments. The Poisson generating-function formula
\[
\mathbb E e^{-sN}=e^{-\kappa T(1-e^{-s})},\qquad s\ge0,
\]
implies \(\mathbb E e^{-2aN/\kappa}=e^{-2bT}\) by the definition of \(\kappa\), and \(\mathbb E e^{-aN/\kappa}=e^{-\kappa T(1-e^{-a/\kappa})}\). Expanding the square of the fast-coordinate error supplies the displayed positive constant. Strict positivity follows because \(e^{-aN/\kappa}\) is nonconstant for \(T>0\), so it cannot agree almost surely with the deterministic number \(e^{-aT}\); this reasoning also establishes the result without relying on a numerical sign test. The slow coordinate converges to the exact slow solution, so its mean-square error tends to zero. The expected-energy limit equals \(e^{-2bT}\) because both diagonal second-moment factors tend to that value.

**6. Fixed-probability consistency.** If \(p\) is fixed in \((0,1)\) as \(h\downarrow0\), then \(hN_{n_h}/p\to T\) in probability since its variance is \(h^2 n_h(1-p)/p=O(h)\), and similarly \(h(n_h-N_{n_h})/(1-p)\to T\). Thus \(X_{n_h}\to(e^{-aT}x_1,e^{-bT}x_2)\) in probability. Each coordinate factor lies in \([0,1]\), giving convergence of mean-square error by bounded convergence in probability.

**7. Large-step asymptotics.** Write \(p_h=1/2-\delta_h\), where \(\delta_h>0\). Crossing gives
\[
2\delta_h=(1-p_h)e^{-2bh/(1-p_h)}
-p_he^{-2ah/p_h}.
\]
First \(\delta_h\to0\): for any fixed \(p<1/2\), as \(h\to\infty\) the crossing difference approaches \(1-2p>0\), so its zero eventually lies above \(p\). The displayed identity first gives \(\delta_h=O(e^{-2bh})\): since \(1-p_h<1\), its first term is at most \(e^{-2bh}\), and the second is nonnegative. This preliminary bound already implies \(h\delta_h\to0\). Since \(a>b\), the second exponential is \(o(e^{-4bh})\) and the first equals \((1/2+o(1))e^{-4bh}(1+o(1))\) by that preliminary bound. Hence \(2\delta_h\sim (1/2)e^{-4bh}\), yielding the stated expansion. The limit of the minimized maximum is \(1/2\). At the fixed variance-optimal \(p_{\rm var}>1/2\), the limiting maximum is \(\max\{1-p_{\rm var},p_{\rm var}\}=p_{\rm var}\), which completes the factor comparison.

## Verification

Run \(\texttt{python3 verify.py}\) from the directory containing this document and the standalone source. The verifier needs only the Python standard library. It enumerates the independent switching words for small horizons, computes the binomial and contraction formulas independently, tests uniqueness and the opposite side of the generator-variance optimizer over a heterogeneous parameter grid, probes the small-step Poisson coefficient and the large-step asymptotic, and numerically evaluates positive limiting exact-solution errors. On the packaged source it reports \(819\) successful deterministic checks. These finite checks corroborate the formulas; the proofs above, not enumeration, establish the statements for every permitted real parameter and time horizon.

For a reproducible contrast, take \(a=10\), \(b=1\), \(h=1\). Numerical root finding yields the contraction-optimal probability \(p_h\approx0.495197812728\), whereas \(p_{\rm var}=10/11\approx0.909090909091\). Their per-step worst mean-square factors are approximately \(0.504802187272\) and \(0.909090909116\), respectively. For \(a=3\), \(b=1\), one obtains \(\kappa\approx2.126574137756\), and for \(T=1\), \(x_1=1\), \(x_2=0\), the nonzero limiting mean-square error is approximately \(0.117865742027\).

## Relationship to prior work

Veldman and Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control* (first public version September 28, 2021, arXiv:2109.13798), introduce the reciprocal-probability generator scaling and derive convergence estimates. Their Example 3 analyzes exactly the general two-block diagonal decomposition and obtains \(a/(a+b)\) as the optimizer of the **generator-variance** objective. That result does not directly yield the opposite contraction-optimal design or its singular Poisson limiting trajectory; it holds under a different optimization objective, and its convergence constants are not uniform over probabilities approaching zero at the mesh scale.

Eisenmann and Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods* (arXiv:2210.05375, first public October 11, 2022), establish general convergence for randomized operator splitting with a different implicit step map, not this precise exact-semigroup minimax probability law. Richtárik and Takáč, *On optimal probabilities in stochastic coordinate descent methods* (Optimization Letters, 2016, online 2015), treat sampling optimization for stochastic coordinate-descent updates, not the sampled exact exponential semigroup or its mesh-dependent rare-event consistency boundary. The contribution claimed here is the explicit joint **contraction-optimization/consistency classification** in the narrow two-mode system, not the construction of reciprocal-probability sampling or generic binomial-to-Poisson convergence.

## Limitations

The theorem applies to two commuting scalar dissipative modes with positive distinct rates, independent mutually exclusive sampled exact subflows and one selected component per step. It does not assert optimality for arbitrary dimensions, noncommuting splittings, finite-horizon *error* rather than energy, control problems, state-dependent probabilities, or equalized computational cost. The singular inconsistency concerns recomputing the energy-optimal probability for each mesh size, not the fixed-probability schemes covered by ordinary convergence results. For finite \(h\) the numerical state is random and its generator only unbiased **before** exponentiation; unbiasedness of the generator does not imply unbiasedness of the propagated state. The positive limiting error proves an obstruction to mean-square consistency, but not any impossibility theorem for other samplers. Priority comparison with all historical specialized randomized-splitting literature remains incomplete; independent scientific audit has not been performed.

## References

1. D. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798, first version September 28, 2021, https://arxiv.org/abs/2109.13798 ; Numerische Mathematik **151** (2022), 495–549, https://doi.org/10.1007/s00211-022-01290-3.
2. M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375, first version October 11, 2022, https://arxiv.org/abs/2210.05375 ; Numerische Mathematik (2024), https://doi.org/10.1007/s00211-024-01396-w.
3. P. Richtárik and M. Takáč, *On optimal probabilities in stochastic coordinate descent methods*, Optimization Letters (2016), first online 2015, https://doi.org/10.1007/s11590-015-0916-1.
