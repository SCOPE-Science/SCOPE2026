# Exact positive-equilibrium classification for a six-compartment social-contagion SIR model

## Finding

For the **constant-control** six-compartment compliant/noncompliant SIR system in Ngo, Parkinson and Wang, arXiv:2509.09075v3, equation (2.2), there is exactly one disease-free equilibrium and **exactly one strictly positive endemic equilibrium if and only if** the actual next-generation invasion reproduction number \(\mathcal R_{\mathrm{inv}}\) exceeds one; there is no positive endemic equilibrium when \(\mathcal R_{\mathrm{inv}}\leq1\). This holds on the entire interior birth/behavior parameter domain stated below. The endemic-equilibrium condition reduces **exactly to a scalar quadratic**, not the quartic anticipated in the motivating study. A strict monotonicity argument supplies existence and uniqueness without assuming endemic-equilibrium stability.

The distinction between the printed reproduction ratio in equation (2.6) and the actual next-generation number has been established previously; **that formula correction and disease-free local instability are not claimed as new here**. As a consequence of the new complete positive-equilibrium classification, we nevertheless obtain an exact, fully positive rational endemic equilibrium at a point where the printed ratio is \(913/925<1\). The new contribution is the **global count of positive equilibria on the full stated parameter domain** and the closed quadratic reduction, not the already-known formula discrepancy.

## Assumptions and scope

Let \(S,I,R\) be compliant susceptible, infected and recovered populations, and let \(S^*,I^*,R^*\) be the analogous noncompliant populations. Write \(N^*=S^*+I^*+R^*\), \(A=1-\alpha\), \(q=\mu^*-\mu\), and \(\lambda=\beta(AI+I^*)\). All parameters and controls are **constant in time** and satisfy
\[
 b,\delta,\gamma,\beta>0,\quad 0<\xi<1,\quad 0\leq\alpha<1,\quad \eta\geq0,\quad q>0,\quad\nu>0,\quad 0\leq\mu<\mu^*.
\]
The fixed controls are admissible whenever their prescribed upper bounds allow these chosen values. The source's state equations, with a dot denoting the time derivative, are
\[
\begin{aligned}
\dot S&=(1-\xi)b-A\lambda S-qSN^*+\nu S^*-\delta S,\\
\dot I&=A\lambda S-(\gamma+\eta+\delta)I-qIN^*+\nu I^*,\\
\dot R&=(\gamma+\eta)I-qRN^*+\nu R^*-\delta R,\\
\dot S^*&=\xi b-\lambda S^*+qSN^*-(\nu+\delta)S^*,\\
\dot I^*&=\lambda S^*+qIN^*-(\gamma+\nu+\delta)I^*,\\
\dot R^*&=\gamma I^*+qRN^*-(\nu+\delta)R^*.
\end{aligned}
\]
A **disease-free equilibrium** has \(I=I^*=0\), and a **strictly positive endemic equilibrium** has all six components positive. No assertion about global attraction, time-varying controls, stochastic variants or spatially varying states is included.

Write \(K=b/\delta\). Let \(u\) be the unique root in \((0,K)\) of
\[
q u^2+(\nu+\delta-qK)u-\xi b=0.
\]
Set \(m=qu\), \(g=\gamma+\delta\), \(\ell=\gamma+\eta+\delta\), and
\[
J=(\ell+m)(g+\nu)-\nu m=\ell(g+\nu)+gm>0,\quad
P=A\big[A(g+\nu)+m\big]>0,\quad Q=A\nu+\ell+m>0.
\]
At the unique disease-free equilibrium, denote the susceptible levels by \(s,s^*\); explicitly
\[
s=\frac{b\,[\nu+(1-\xi)\delta]}{\delta(\delta+m+\nu)},\qquad
s^*=\frac{b\,[m+\xi\delta]}{\delta(\delta+m+\nu)}.
\]
The correct invasion threshold is
\[
\boxed{\mathcal R_{\mathrm{inv}}=\frac{\beta}{J}(Ps+Qs^*).}
\]

## Proof

**1. Behavior totals and the disease-free state.** Every equilibrium has total population \(K\), since the sum of all six equations obeys \(\dot N_{\mathrm{total}}=b-\delta N_{\mathrm{total}}\). Writing \(v=N^*\) and adding the noncompliant equations yields
\[
0=\xi b+q(K-v)v-(\nu+\delta)v.
\]
The left side is positive at \(v=0\) and negative at \(v=K\), and the polynomial's two roots have negative product \(-\xi b/q\). Hence exactly one root \(u\in(0,K)\) exists. At every equilibrium \(qN^*=m\), independent of the disease load. With \(I=I^*=0\), recovered populations necessarily vanish and the susceptible equations give the displayed positive \(s,s^*\). Thus the disease-free equilibrium is unique.

**2. Strictly monotone endemic-equilibrium equation.** At any equilibrium let \(\lambda=\beta(AI+I^*)\). If \(\lambda=0\), then \(I=I^*=0\). For \(\lambda>0\), the susceptible equations are
\[
M(\lambda)\binom{S}{S^*}=b\binom{1-\xi}{\xi},\qquad
M(\lambda)=\begin{pmatrix}\delta+m+A\lambda&-\nu\\-m&\delta+\nu+\lambda\end{pmatrix}.
\]
Its determinant
\[
\Delta(\lambda)=\delta(\delta+m+\nu)+[\delta+m+A(\delta+\nu)]\lambda+A\lambda^2
\]
is positive for all \(\lambda\geq0\). The inverse has strictly positive entries, so the unique susceptible pair is positive and satisfies
\[
S(\lambda)=\frac{b[\nu+(1-\xi)(\delta+\lambda)]}{\Delta(\lambda)},\qquad
S^*(\lambda)=\frac{b[m+\xi\delta+\xi A\lambda]}{\Delta(\lambda)}.
\]
The infected equilibrium equations have coefficient matrix
\[
V=\begin{pmatrix}\ell+m&-\nu\\-m&g+\nu\end{pmatrix},
\qquad
\binom{I}{I^*}=\lambda V^{-1}\binom{AS(\lambda)}{S^*(\lambda)}.
\]
Because \(V^{-1}\) is strictly positive, \(I,I^*>0\). Substituting into the definition of \(\lambda\) gives the **single scalar condition**
\[
F(\lambda)=\frac{\beta}{J}\,[P S(\lambda)+Q S^*(\lambda)]=1.
\]
Differentiating the susceptible system gives
\[
\frac{d}{d\lambda}\binom{S}{S^*}=-M(\lambda)^{-1}
\begin{pmatrix}A&0\\0&1\end{pmatrix}\binom{S}{S^*}<0
\]
componentwise, because \(A>0\). Hence \(F\) is strictly decreasing, \(F(0)=\mathcal R_{\mathrm{inv}}\), and \(F(\lambda)\to0\) as \(\lambda\to\infty\). This proves that \(\lambda>0\) solving the equilibrium equations exists uniquely exactly when \(\mathcal R_{\mathrm{inv}}>1\).

For an explicit scalar polynomial, put
\[
E_0=P[\nu+(1-\xi)\delta]+Q[m+\xi\delta],\qquad
E_1=P(1-\xi)+Q\xi A.
\]
The condition \(F(\lambda)=1\) is equivalent to
\[
\boxed{JA\lambda^2+
\big[J(\delta+m+A(\delta+\nu))-\beta b E_1\big]\lambda
+J\delta(\delta+m+\nu)-\beta bE_0=0.}
\]
This is a quadratic with a unique positive root when its constant term is negative, and none when that term is nonnegative, as the preceding monotonic argument independently establishes.

**3. Recovering all six compartments.** The recovered equilibrium equations uniquely determine
\[
\binom R{R^*}=
\begin{pmatrix}\delta+m&-\nu\\-m&\delta+\nu\end{pmatrix}^{-1}
\binom{(\gamma+\eta)I}{\gamma I^*}>0.
\]
By summing the constructed six equilibrium equations, their total is \(K\). Summing the three noncompliant equations gives
\(0=\xi b+m(K-N^*)-(\nu+\delta)N^*\), whose unique solution is \(N^*=u\) because \(u\) satisfies the same relation. Therefore the fixed value \(m=qu\) used to construct all six components is self-consistent. Conversely every positive equilibrium must solve this scalar equation. Existence, strict positivity, uniqueness and nonexistence below threshold follow.

**4. Invasion threshold and contextual comparison with the printed expression.** At the disease-free equilibrium the standard new-infection and transfer matrices on \((I,I^*)\) are
\[
\mathsf F=\beta\binom{As}{s^*}(A,1),\qquad
\mathsf V=\begin{pmatrix}\ell+m&-\nu\\-m&g+\nu\end{pmatrix}.
\]
The rank-one matrix \(\mathsf F\mathsf V^{-1}\) has its sole nonzero eigenvalue equal to \(\mathcal R_{\mathrm{inv}}\). Direct simplification of the source's printed expression \(\mathscr R_{0,\mathrm{print}}\) in equation (2.6), retaining its printed isolated \(\mu\), gives the exact identity
\[
\boxed{\mathcal R_{\mathrm{inv}}-\mathscr R_{0,\mathrm{print}}
=\frac{\beta\alpha(1-\alpha)s s^*[(\mu^*-\mu)-\mu]}{J}.}
\]
In particular, replacing the isolated \(\mu\) inside the numerator of the source's equation (2.6) by \(\mu^*-\mu\) restores the next-generation formula. The sign of the discrepancy depends on parameters; it is not claimed to have a universal sign.

**5. Exact positive-equilibrium witness.** Choose
\[
b=\delta=\gamma=\nu=1,\quad \xi=\alpha=\tfrac12,\quad
\eta=1,\quad \mu^*=2,\quad\mu=0,\quad\beta=\tfrac{3652}{925}.
\]
Then the disease-free susceptible populations are \(s=s^*=1/2\), and direct substitution gives
\[
\mathscr R_{0,\mathrm{print}}=\frac{913}{925}<1<\frac{1909}{1850}=\mathcal R_{\mathrm{inv}}.
\]
The quadratic admits \(\lambda=1/25\), and the **exact strictly positive equilibrium**, ordered as \((S,I,R,S^*,I^*,R^*)\), is
\[
\boxed{\left(\frac{1900}{3901},\frac{379}{85822},\frac{366}{42911},
\frac{3775}{7802},\frac{340}{42911},\frac{353}{42911}\right).}
\]
All six derivatives vanish and the components sum to one, with compliant and noncompliant totals each \(1/2\). Moreover, the infectious two-by-two Jacobian block at the disease-free state has
\[
\operatorname{tr}=-\frac{1677}{370},\qquad
\det=-\frac{649}{1850}<0,
\]
so one eigenvalue is **strictly positive**. Thus the original disease-free equilibrium is linearly unstable although the threshold printed in equation (2.6) is below one. This directly contradicts the corresponding literal below-one assertion in Theorem 2.3(iii) of the v3 source; no appeal to simulation or global dynamics is needed.

## Verification

The accompanying standard-library script `verify.py` checks the exact rational six-ODE residuals, total-population and behavior identities, positive state, infection pressure, scalar quadratic, both threshold formulas, their difference, and the disease-free infected-block trace and determinant. Run `python3 verify.py`; the expected output is `VERIFY_OK`. The universal uniqueness theorem is **analytic**, not inferred from finite sampling; the script verifies the exact stated counterexample, not infinitely many parameter values.

## Relationship to prior work

Ngo, Parkinson and Wang (2025/2026), arXiv:2509.09075v3, define the six-dimensional model in equation (2.2), give the displayed disease-free reproduction ratio (2.6), and explicitly leave the disease-endemic equilibrium calculation unfinished, anticipating a quartic. An **earlier mathematical analysis of these very equations** has already identified the difference between the printed disease-free reproduction ratio and the actual next-generation matrix, including an exact reversal of a disease-free local stability prediction. This already-established correction is **presupposed**, not asserted to be new. Importantly, that analysis is limited to disease-free local invasion and explicitly does **not** classify any positive endemic equilibrium. The present proof instead closes the distinct model-wide existence-and-uniqueness question for strictly positive endemic equilibria when \(0<\xi<1\), via a complete scalar quadratic reduction and strict monotonicity. The exact rational six-compartment equilibrium is an illustrative witness for this new classification, not an independent novelty claim about the already-known printed formula discrepancy.

The arXiv v1 equations have a **different infection mixing term**, so the main claim specifically concerns v3. Parkinson and Wang, arXiv:2507.01046, study a related deterministic/stochastic model and designate equilibrium analysis as future work. Parkinson and Wang, arXiv:2303.01489, investigate reaction–diffusion extinction and persistence; Bongarti, Parkinson and Wang, arXiv:2407.17298, address PDE optimal control. Van den Driessche and Watmough (2002) supply generic next-generation and local-bifurcation techniques. None of these checked works proves the exact all-parameter positive-equilibrium count or the reduction to a quadratic for these specific six-dimensional equations. The monotonicity device as an abstract technique is established mathematics; the new claim is its complete source-model application.

## Limitations

The new equilibrium-classification claim covers only time-independent parameters satisfying \(0<\xi<1\), \(0\leq\alpha<1\), \(q>0\), \(\nu>0\); endpoint behavior, equilibria with other boundary parameters, general global convergence, limit cycles, time-dependent control, noise and diffusion are not classified. The result does not imply an epidemic prediction. The positive equilibrium's dynamical stability is not determined. The first arXiv preprint has a different infection mixing convention, and further later revisions may change the displayed formula; all comparisons are to version 3 as identified. Generic next-generation theory and different behavioral epidemic models remain prior art. Complete indexing of every possible publication cannot be guaranteed.

## References

1. C. Ngo, C. Parkinson and W. Wang, *Optimal Control of an SIR Model with Noncompliance as a Social Contagion*, arXiv:2509.09075v3 (19 June 2026); first public v1 11 September 2025. https://arxiv.org/pdf/2509.09075v3
2. C. Parkinson and W. Wang, *A Compartmental Model for Epidemiology with Human Behavior and Stochastic Effects*, arXiv:2507.01046v4 (2025). https://arxiv.org/html/2507.01046
3. C. Parkinson and W. Wang, *Analysis of a Reaction-Diffusion SIR Epidemic Model with Noncompliant Behavior*, SIAM Journal on Applied Mathematics 83 (2023), 1969–2002, arXiv:2303.01489. https://arxiv.org/pdf/2303.01489
4. M. Bongarti, C. Parkinson and W. Wang, *Optimal Control of a Reaction-Diffusion Epidemic Model with Noncompliance*, European Journal of Applied Mathematics (2026), arXiv:2407.17298. https://arxiv.org/pdf/2407.17298
5. P. van den Driessche and J. Watmough, *Reproduction Numbers and Sub-threshold Endemic Equilibria for Compartmental Models of Disease Transmission*, Mathematical Biosciences 180 (2002), 29–48. https://watmough.ext.unb.ca/papers/mgroup.pdf
