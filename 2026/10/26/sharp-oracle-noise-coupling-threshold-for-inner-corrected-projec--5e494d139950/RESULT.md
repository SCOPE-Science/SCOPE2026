# Sharp oracle-noise coupling threshold for inner-corrected projective Euler

## Finding

For the four-stage, two-microstep inner-derivative-corrected projective Forward Euler (IPFE) rule of Koellermeier and Samaey, a scalar contractive test equation has a sharp *stochastic* stability obstruction. Set the macroscopic step to \(h=1/a\) for \(a>0\), the microstep to \(\delta=\lambda h\), and \(0<\lambda<1/2\). Apply this IPFE rule to \(x'=-ax\) with centered additive noise in its four right-hand-side evaluations. Assume independent, equal-variance noise for the first two evaluations; the last two each have variance \(\sigma^2>0\), mutual correlation \(\rho\in[-1,1]\), and are independent of the first two. The four-dimensional noise vector is independent between outer steps, is independent of the incoming state, and has zero mean. No distributional assumption beyond second moments is required.

Put
\[
\xi=1-2\lambda+2\lambda^2,\qquad
L=1+\xi/2,\qquad
G=\lambda(1-\lambda)L.
\]
For every integer \(n\ge0\) and every deterministic initial value \(x_0\), the noisy IPFE iterates satisfy the **exact** identity
\[
\mathbb E[x_n^2]=G^{2n}x_0^2+
\frac{1-G^{2n}}{1-G^2}Q,
\]
where
\[
Q=h^2\sigma^2\left\{L^2\bigl[\lambda^4+(1-\lambda)^2\bigr]
+\frac{\xi^2}{4\lambda^2}\bigl[\lambda^2+2(1+\lambda)(1-\rho)\bigr]\right\}.
\]
The deterministic multiplier obeys \(0<G<3/8\). Nevertheless, its stationary mean-square level \(V_\infty=Q/(1-G^2)\) exhibits a sharp correlation threshold as \(\lambda\downarrow0\):
\[
\boxed{\ V_\infty=O(1)\quad\Longleftrightarrow\quad
1-\rho_\lambda=O(\lambda^2).\ }
\]
Here the correlation may vary arbitrarily with \(\lambda\), with \(-1\le\rho_\lambda\le1\). More precisely, at fixed \(\rho<1\),
\[
\lim_{\lambda\downarrow0}\lambda^2V_\infty
=\frac{h^2\sigma^2}{2}(1-\rho),
\]
and whenever \(\rho_\lambda=1-c\lambda^2+o(\lambda^2)\) for some \(c\ge0\),
\[
\lim_{\lambda\downarrow0}V_\infty
=h^2\sigma^2\left(\frac52+\frac c2\right).
\]
In particular independent correction evaluations have \(\rho=0\), so the stationary variance diverges exactly as \(h^2\sigma^2/(2\lambda^2)\); reusing an identical additive oracle error for the last two evaluations (\(\rho=1\)) gives the finite limit \(5h^2\sigma^2/2\).

For comparison, the two-evaluation uncorrected projective Forward Euler (PFE) method on the same equation, macrostep, microsteps, and independent first-two oracle noises has multiplier \(P=\lambda(1-\lambda)\) and stationary variance
\[
V_\mathrm{PFE}=
\frac{h^2\sigma^2[\lambda^4+(1-\lambda)^2]}{1-P^2}
\longrightarrow h^2\sigma^2.
\]
Thus, under independently sampled right-hand-side noise, IPFE's correction creates an arbitrarily large mean-square penalty relative to the uncorrected rule despite both deterministic multipliers tending to zero. If each independent evaluation instead averages \(B_\lambda\) iid unbiased elementary oracle samples of variance \(\sigma^2\), the corrected stationary variance is uniformly bounded as \(\lambda\downarrow0\) **if and only if** \(B_\lambda=\Omega(\lambda^{-2})\), where \(B_\lambda\) is a positive integer. Shared-noise coupling avoids this divergent sample-count requirement in the stipulated additive model.

## Assumptions and scope

The underlying differential equation is the scalar autonomous stable equation \(x'=-ax\), with \(a>0\) and a fixed macrostep \(h=1/a\). The time-domain numerical model is a discrete recurrence at outer-step boundaries, with independent fresh noise vectors at those boundaries. Each oracle returns \(-a y+\eta\) when evaluated at \(y\), where \(\eta\) is a centered additive error. The first two errors are independent of each other and of the final pair. The last pair is allowed exactly the stated covariance \(\rho\sigma^2\); its marginal variances both equal \(\sigma^2\). All errors are independent of the past and of the numerical state when the macrostep begins. Correlation \(\rho=1\) is allowed, meaning identical scalar errors almost surely. For \(\rho_\lambda\) in the asymptotic threshold statement, a separate oracle model is specified at each positive \(\lambda\). This theorem does not assume the right-hand-side evaluation errors are physical white-noise differential increments, nor does it analyze their continuous-time limit.

The IPFE update is explicitly defined without any reliance on an implicit solver or omitted tableaux. Within one macrostep, set
\[
\begin{aligned}
k_0&=-a x_n+\eta_0,\\
k_1&=-a(x_n+\delta k_0)+\eta_1,\\
v&=x_n+h[\lambda k_0+(1-\lambda)k_1],\\
k_2&=-av+\eta_2,\\
k_3&=-a(v+\delta k_2)+\eta_3,\\
x_{n+1}&=v+\frac{\xi h}{2\lambda}(k_3-k_2).
\end{aligned}
\]
These are precisely the four stages and endpoint weights of the published IPFE tableau, specialized to two inner microsteps (\(K=1\)). The reference paper supplies the tableau and its deterministic order/stability motivation; it does not supply the additive stochastic-oracle model or the theorem here. The uncorrected comparator uses only \(k_0,k_1\), returns \(v\), and therefore has two oracle calls rather than four.

## Proof

Write \(\delta=\lambda h\) and \(ah=1\). Direct substitution in the first two stages yields
\[
v=\lambda(1-\lambda)x_n
+h\bigl[\lambda^2\eta_0+(1-\lambda)\eta_1\bigr].
\]
The two extra derivative evaluations satisfy the exact identity
\[
k_3-k_2=a\delta\, a v-a\delta\eta_2+\eta_3-\eta_2
=\lambda a v-(1+\lambda)\eta_2+\eta_3.
\]
It follows that
\[
x_{n+1}=Gx_n+hL\bigl[\lambda^2\eta_0+(1-\lambda)\eta_1\bigr]
+\frac{h\xi}{2\lambda}\bigl[-(1+\lambda)\eta_2+\eta_3\bigr]
=:Gx_n+W_n.
\]
The identity is deterministic algebra for every realization of the four errors. Because \(0<\lambda<1/2\), one has \(0<\lambda(1-\lambda)<1/4\), \(0<\xi<1\), and \(1<L<3/2\). Hence \(0<G<3/8\).

By centering and independence across the two groups of evaluations,
\[
\mathbb E W_n=0,
\quad
\operatorname{Var}(W_n)=
(hL)^2\sigma^2\bigl[\lambda^4+(1-\lambda)^2\bigr]
+\left(\frac{h\xi}{2\lambda}\right)^2\sigma^2
\bigl[(1+\lambda)^2+1-2\rho(1+\lambda)\bigr].
\]
The bracket in the final term equals \(\lambda^2+2(1+\lambda)(1-\rho)\). This proves the asserted exact formula for \(Q\). Each \(W_n\) is independent of the preceding state, so iterating the scalar second-moment recurrence
\[
\mathbb E[x_{n+1}^2]=G^2\mathbb E[x_n^2]+Q
\]
proves the finite-time identity and its stationary limit. Its cross term vanishes by conditional centering even if the four stage noises are not jointly Gaussian.

As \(\lambda\downarrow0\), \(\xi\to1\), \(L\to3/2\), and \(G\to0\). Split \(Q\) into a bounded term
\[
Q_0=h^2\sigma^2\left[L^2\bigl(\lambda^4+(1-\lambda)^2\bigr)+\xi^2/4\right]
\]
and a nonnegative correlation-deficit term
\[
Q_1=h^2\sigma^2\frac{\xi^2(1+\lambda)}{2\lambda^2}(1-\rho_\lambda).
\]
The bounded term converges to \(h^2\sigma^2(9/4+1/4)=5h^2\sigma^2/2\). The factor multiplying \((1-\rho_\lambda)/\lambda^2\) in \(Q_1\) converges to \(h^2\sigma^2/2\) and is bounded above and bounded away from zero for all sufficiently small positive \(\lambda\). Since \(1-G^2\to1\) and is bounded away from zero, \(V_\infty\) is bounded **exactly when** \((1-\rho_\lambda)/\lambda^2\) is bounded. The two more precise limits follow by taking the corresponding limits of \(Q_0,Q_1\). Notice that this proof excludes any cancellation of the potentially divergent part, because \(Q_1\ge0\).

For PFE, \(v=Px_n+h[\lambda^2\eta_0+(1-\lambda)\eta_1]\), and repeating the independent-step second-moment calculation gives the displayed \(V_\mathrm{PFE}\). Finally, if all four noisy evaluations have independent average-of-\(B_\lambda\) errors, replace \(\sigma^2\) everywhere by \(\sigma^2/B_\lambda\) and set \(\rho=0\). The exact \(Q\) proves \(V_\infty\asymp (B_\lambda\lambda^2)^{-1}\) in this model; positivity of all contributing terms makes the condition \(B_\lambda=\Omega(\lambda^{-2})\) both necessary and sufficient for boundedness.

## Verification

The accompanying standalone \(\texttt{verify\_ipfe.py}\) uses only the Python standard library. For rational microstep ratios, states and oracle errors, it checks 1,680 exact stage-by-stage evaluations against the closed-form recurrence, verifies the noise-covariance polynomial for five correlations at every tested microstep ratio, and checks finite-ratio convergence toward the two predicted leading limits. Output:

`VERIFY_OK exact four-stage recurrence: 1680 fractional stage inputs; covariance polynomial and coupling limits`

The verifier is an exact finite algebra cross-check, not a replacement for the proof of the universal recurrence, the biconditional correlation threshold, or the asymptotic limits. To reproduce: \(\texttt{python3 verify\_ipfe.py}\). No downloaded datasets or external libraries are required.

## Relationship to prior work

Koellermeier and Samaey formulate PFE in their Section 2.2 and introduce the four-stage inner-derivative correction IPFE in Section 5.2, especially equation (114), proving deterministic second-order conditions and analyzing stiff stability. The calculations here retain exactly their stage mapping while adding explicitly correlated stochastic right-hand-side evaluation errors. In particular, their deterministic stability analysis does not imply bounded mean-square response to sampling noise.

Xiu and Kevrekidis study stochastic multiscale equation-free projective computation and motivate noisy fine-scale estimators, but their sampled coarse observables and uncorrected projective procedure differ from the IPFE four-stage derivative corrector. The standard variance identity for a correlated difference is not new. The new content assessed here is its exact interaction with IPFE's published four-stage coefficients, yielding an infinite-horizon necessary-and-sufficient coupling rate, leading constants and a directly quantified contrast with PFE and independent batching.

Papavasiliou and Kevrekidis investigate variance reduction in equation-free stochastic multiscale simulation. Only accessible abstract-level material was examined for that publication, so its precise full scope remains an originality risk; no unsupported claim is made that its full text lacks a more general implication. Earlier finite-difference variance-reduction principles could overlap conceptually with the coupling interpretation. A primary-literature search and comparisons with the inspected records did not identify an exact covering statement for this IPFE stochastic-oracle model; absence of a match is not a proof of publication priority.

## Limitations

The theorem applies only to the scalar decay mode \(x'=-ax\), the specified macrostep relation \(ah=1\), two inner microsteps, fixed additive stage errors with stated covariance, and independence between outer steps. For \(\rho=1\), identical stage-error fluctuations at two distinct states are assumed; this coupling may or may not be achievable by a particular physical or Monte Carlo model. A general stochastic nonlinear ODE, state-dependent noise, physical diffusions, more inner stages and multidimensional nonnormal dynamics require different analysis. The corrected scheme is deterministically stable here but not asserted to be a universally better integrator; its deterministic discretization bias is not removed in this fixed-macrostep comparison. The research calculation is not an independently validated publication-priority claim.

## References

1. J. Koellermeier and G. Samaey, *Projective Integration Methods in the Runge-Kutta Framework and the Extension to Adaptivity in Time*, arXiv:2210.08302 (first posted 2022-10-15), v2 (2024-01-19), especially Sections 2.2, 5.2, 6.2, equation (114). https://arxiv.org/html/2210.08302v2
2. D. Xiu and I. G. Kevrekidis, *Equation-free, multiscale computation for unsteady random diffusion*, arXiv:math/0504273 (2005), particularly projective computation and random microscale estimates. https://arxiv.org/abs/math/0504273
3. A. Papavasiliou and I. G. Kevrekidis, *Variance Reduction for the Equation-Free Simulation of Multiscale Stochastic Systems*, SIAM Journal on Scientific Computing, DOI:10.1137/060650635 (2007). https://doi.org/10.1137/060650635 (abstract-level comparison; full text not inspected).
