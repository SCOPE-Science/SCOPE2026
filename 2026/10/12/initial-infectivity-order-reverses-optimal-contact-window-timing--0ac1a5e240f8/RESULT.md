# Initial infectivity order reverses optimal contact-window timing under reversible mutation

## Finding

**Exact pulse-shift ordering.** In the susceptible-frozen, linear mutation–selection epidemic model defined below, hold the duration and time profile of a single nonnegative contact window fixed and translate the window within a finite observation horizon. If the initial infected trait density is nonconstant and **decreases** with infectivity, the total infected mass at the horizon is strictly **increasing** in the start time. If that density is nonconstant and **increases** with infectivity, total infected mass is strictly **decreasing** in the start time. A uniform initial density makes the total exactly independent of placement. These statements hold for every positive mutation rate, every nonzero nonnegative contact profile, every finite horizon that fits the window, and every common recovery rate. No small-amplitude expansion in the contact strength is needed.

The same classification holds *exactly* for any finite symmetric nearest-neighbor mutation chain with positive edge rates and strictly increasing infectiousness traits. Thus, to minimize linearized cumulative prevalence at a fixed terminal time, an early contact window is best for a population initially concentrated at low-infectivity traits, whereas a late window is best for an increasing initial trait profile. The two preferences reverse when maximizing prevalence. The statement is about infected mass at a specified horizon, not outbreak peak, final epidemic size, or clinical intervention choice in a depleted-susceptible epidemic.

## Assumptions and scope

**Finite mutation model.** Fix an integer \(m\ge2\), ordered traits \(0\le\lambda_0<\cdots<\lambda_{m-1}\le1\), edge conductances \(c_0,\ldots,c_{m-2}>0\), common recovery rate \(\mu\ge0\), observation horizon \(T>0\), and window duration \(0<\ell\le T\). Let \(Q\) be the real symmetric matrix with
\[
(Qz)_i=c_{i-1}(z_{i-1}-z_i)+c_i(z_{i+1}-z_i),
\]
where absent endpoint terms are zero. In particular, \(Q\mathbf1=0\) and \(Q\) has strictly positive nearest-neighbor off-diagonals. Let the bounded measurable contact profile \(u:[0,\ell]\to[0,\infty)\) satisfy \(\int_0^\ell u(s)\,ds>0\). At each placement \(a\in[0,T-\ell]\), define \(u_a(t)=u(t-a)\) on \([a,a+\ell]\), zero elsewhere. Infected trait masses follow
\[
\dot\rho(t)=\bigl[Q+u_a(t)\operatorname{diag}(\lambda_0,\ldots,\lambda_{m-1})-\mu I\bigr]\rho(t),
\qquad \rho(0)=\rho^0\ge0,\quad\sum_i\rho_i^0>0.
\]
This is the linearized, fixed-susceptible version of evolving-infectivity SIR; the constant susceptible level is incorporated in \(u\). The mutation process is reversible with respect to uniform counting measure. The comparison is among *translations of the same* contact profile, not among controls with different total budgets or shapes. Write \(M(a)=\sum_i\rho_i(T)\).

**Continuum counterpart.** Fix mutation coefficient \(d>0\) and the trait interval \([0,1]\). With reflecting (Neumann) boundary conditions, take
\[
\partial_t\rho=d\,\partial_{xx}\rho+[u_a(t)x-\mu]\rho,
\qquad \partial_x\rho(t,0)=\partial_x\rho(t,1)=0.
\]
Assume \(\rho^0\in C^2([0,1])\), \(\rho^0\ge0\), \(\int_0^1\rho^0>0\), with the Neumann compatibility conditions \((\rho^0)'(0)=(\rho^0)'(1)=0\). The initial profile is either nonincreasing, nondecreasing, or constant in the trait coordinate, and \(M(a)=\int_0^1\rho(T,x)\,dx\). In both settings the recovery rate is independent of trait and time, and mutation continues outside the contact window.

## Proof

**1. Separating pulse placement from mutation.** Let \(H_t=e^{tQ}\) in the finite model and let \(U_u\) denote evolution during the contact window without recovery, under \(Q+u(s)\Lambda\) for \(0\le s\le\ell\), where \(\Lambda=\operatorname{diag}(\lambda_i)\). As \(\mathbf1^{\mathsf T}H_t=\mathbf1^{\mathsf T}\), the total mass at \(T\) is
\[
M(a)=e^{-\mu T}\,\mathbf1^{\mathsf T}U_uH_a\rho^0
=e^{-\mu T}\,f^{\mathsf T}H_a\rho^0,
\qquad f:=U_u^{\mathsf T}\mathbf1.
\]
The free-diffusion period after the contact window drops out because it conserves infected mass. The vector \(f\) is the time-\(\ell\) solution, starting at \(\mathbf1\), of the *time-reversed* adjoint contact equation \(\dot f=[Q+u(\ell-t)\Lambda]f\); this holds for measurable profiles by approximation or time-ordered evolution. The solution has all components strictly positive.

**2. Strict increase of the pulse weight across infectivity.** For any vector \(z\), define its edge differences \(Dz\) by \((Dz)_i=z_{i+1}-z_i\). Direct subtraction of adjacent mutation equations gives
\[
(DQz)_i=c_{i-1}(Dz)_{i-1}-2c_i(Dz)_i+c_{i+1}(Dz)_{i+1},
\]
with absent endpoint terms understood as zero. The tridiagonal operator \(B\) on the right has nonnegative off-diagonals and is irreducible. For \(g(t)=Df(t)\), the adjoint contact equation therefore gives
\[
\dot g_i=(Bg)_i+u(\ell-t)\lambda_{i+1}g_i
+u(\ell-t)(\lambda_{i+1}-\lambda_i)f_i(t),
\qquad g(0)=0.
\]
The positive-system variation-of-constants formula, strict ordering of the traits, positivity of \(f\), and \(\int_0^\ell u>0\) imply
\[
 f_{i+1}>f_i\qquad (0\le i<m-1).
\]
The conclusion remains true for all positive conductances and arbitrarily strong finite contact profiles.

**3. Monotonicity of the initial density is preserved.** Put \(p(a)=H_a\rho^0\), \(h(a)=Dp(a)\). The same subtraction yields \(\dot h=Bh\), so \(h(a)=e^{aB}h(0)\). For a nonconstant nonincreasing initial vector, \(h(0)\le0\) and \(h(0)\ne0\), hence \(h(a)<0\) componentwise for every \(a>0\), since \(B\) is irreducible Metzler. The inequalities reverse for an initially nondecreasing vector. A constant vector remains constant.

**4. Exact sign of the placement derivative.** Differentiating the expression for \(M\) and using symmetry and the weighted-graph Dirichlet identity,
\[
\frac{dM(a)}{da}=e^{-\mu T}\,f^{\mathsf T}Qp(a)
=-e^{-\mu T}\sum_{i=0}^{m-2}c_i
(f_{i+1}-f_i)(p_{i+1}(a)-p_i(a)).
\]
Every summand is strictly positive after the leading minus sign when \(\rho^0\) is nonconstant nonincreasing; every one is strictly negative when \(\rho^0\) is nonconstant nondecreasing. The derivative vanishes identically for the constant profile. The endpoint values follow by continuity, proving the strict monotonicity on the entire \([0,T-\ell]\) whenever this interval is nondegenerate. If \(T=\ell\) only one placement is available, and the ordering is vacuous.

**5. Exact two-trait quantitative witness.** For \(m=2\), take \(\lambda_0=0\), \(\lambda_1=1\), \(c_0=c>0\), and a constant contact intensity \(u(s)=q>0\). Writing \(f=(f_0,f_1)\) and \(\omega=\sqrt{q^2+4c^2}\), direct exponentiation gives
\[
f_1-f_0=\frac{2q}{\omega}e^{(q-2c)\ell/2}\sinh(\omega\ell/2)>0.
\]
For initial masses \(\rho^0=(r_0,r_1)\), the finite-horizon difference between any two starts \(0\le a<b\le T-\ell\) is exactly
\[
M(b)-M(a)=\frac{e^{-\mu T}}2\,(f_1-f_0)(r_0-r_1)
\bigl(e^{-2ca}-e^{-2cb}\bigr).
\]
Thus the direction reverses at \(r_0=r_1\), while neither time shift nor selection strength needs to be small.

**6. Reflecting continuum limit.** Let \(H_t=e^{td\partial_{xx}}\) be the Neumann heat semigroup and let \(f=U_u^*1\) be the pulse adjoint weight. The same calculation yields
\[
M(a)=e^{-\mu T}\int_0^1 f(x)(H_a\rho^0)(x)\,dx.
\]
Let \(F(t,x)\) denote the adjoint pulse solution using the reversed profile, \(F(0,x)=1\), and \(G=\partial_xF\). Differentiation in space yields the Dirichlet problem
\[
\partial_tG=d\partial_{xx}G+u(\ell-t)xG+u(\ell-t)F,
\quad G(t,0)=G(t,1)=0,\quad G(0,x)=0.
\]
The strong parabolic positivity principle gives \(f'(x)>0\) for every interior \(x\). For \(p(a,x)=H_a\rho^0(x)\), its derivative \(\partial_xp\) evolves under Dirichlet heat flow. By positivity improvement, it is strictly negative in the interior for \(a>0\) if \(\rho^0\) is nonconstant nonincreasing, strictly positive if nonconstant nondecreasing, and zero if constant. Integration by parts, using Neumann boundary conditions, now gives
\[
\frac{dM(a)}{da}=-e^{-\mu T}d\int_0^1 f'(x)\,\partial_xp(a,x)\,dx,
\]
which has exactly the claimed signs. Smoothness and strong continuity extend the ordering to endpoints.

## Verification

The standalone `verify.py` uses exact rational arithmetic to check the discrete edge-gradient identity, its positive forcing decomposition, and the Dirichlet identity for 81 distinct sizes/parameter choices, with a direct two-trait numerical evaluation of the explicitly proved positive shift. Running `python verify.py` produces a `VERIFY_OK` line. This finite exercise checks algebraic implementation only; the unrestricted theorem follows from the semigroup and positivity arguments above. The quantitative two-trait formula can be verified independently by exponentiating the displayed symmetric \(2\times2\) matrix.

## Relationship to prior work

Lamata-Otín, Arenas, Gómez-Gardeñes and Soriano-Paños (2026) study mutation-driven evolution of viral infectiousness in SIR and how finite-duration interventions modify epidemic peaks and final attack rates. Their evolution equation motivates the selection–diffusion operator, but their control analysis addresses the nonlinear susceptible-depleting system and intervention *duration*, rather than translating a fixed-shaped contact window across a fixed horizon under a monotone initial trait profile. Their Supplementary Notes 1–6 were compared, including the intervention equations and diffusivity approximations.

Patil, Ahmed, Viossat and Noble (2025) investigate timing of multi-strike cancer therapy in a distinct stochastic multitype evolutionary-rescue model, not a reversible diffusive linear mutation–selection semigroup. Ballard, Bean and Ross (2017) optimize stochastic SIR fade-out under intervention timing; classic SIR control results without evolving transmission traits do not imply the present opposite timing preferences. General Dirichlet-form integration by parts, Metzler positivity and Feynman–Kac semigroup methods are acknowledged as established methods. The contribution claimed here is the exact domain-wide contact-window placement comparison in the evolving-infectivity invasion model, not the underlying positivity theory.

## Limitations

This is a result about finite-horizon *linearized infected mass*: susceptible depletion, epidemic peaks, endemic equilibria, intervention costs and final attack rates are outside the claim. It concerns one isolated translated nonnegative contact profile while mutation and recovery continue, with reversible nearest-neighbor mutation. It does not classify arbitrary nonmonotone initial trait densities, nonreversible mutation, unequal trait-specific mortality, or an evolving susceptible pool. The continuum proof uses reflecting mutation on a bounded infectivity range \([0,1]\), not an unbounded Gaussian approximation. Time-reversal and comparison-semigroup literature may contain equivalent abstract formulations; an application-specific originality assessment does not establish uniqueness across unpublished or unindexed work.

## References

1. S. Lamata-Otín, A. Arenas, J. Gómez-Gardeñes and D. Soriano-Paños, *Interplay between evolutionary and epidemic time scales challenges the outcome of control policies*, first public arXiv version 19 March 2026, arXiv:2603.18801v1; full version and supplementary notes arXiv:2603.18801v2, 3 October 2026. https://arxiv.org/abs/2603.18801 ; https://arxiv.t3mt.com/html/2603.18801v2
2. S. Patil, A. Ahmed, Y. Viossat and R. Noble, *Preventing evolutionary rescue in cancer using two-strike therapy*, Genetics 232(2), iyaf255, first published 26 November 2025, https://doi.org/10.1093/genetics/iyaf255 .
3. P. G. Ballard, N. G. Bean and J. V. Ross, *Intervention to maximise the probability of epidemic fade-out*, Mathematical Biosciences 293 (2017), 1–10, https://doi.org/10.1016/j.mbs.2017.08.003 .
4. P. Cattiaux, G. Conforti, I. Gentil and C. Léonard, *Time reversal of diffusion processes under a finite entropy condition*, arXiv:2104.07708 (2021), https://arxiv.org/abs/2104.07708 (background on reversal, not a source of the contact-window theorem).
