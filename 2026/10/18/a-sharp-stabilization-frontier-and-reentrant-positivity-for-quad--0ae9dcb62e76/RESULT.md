# A sharp stabilization frontier and reentrant positivity for quadratic ETDRK2

## Finding

For the second-order exponential time-differencing Runge--Kutta (ETDRK2) method of Fu, Shen and Yang, the unconditional *original-energy* dissipation threshold on a commuting quadratic gradient flow is exactly
\[
\beta\ge\max\left\{0,\frac12\max_j(a_j-\ell_j)\right\}.
\]
This condition is necessary as well as sufficient; equality still gives strict dissipation at each finite positive step. Within its energy-stable region the method can lose and then regain positivity as the stabilizer is *decreased*. The same amplification formula gives an exact minimax large-step damping stabilizer when the implicit linear part is scalar.

## Assumptions and scope

Let \(m\ge1\). Let \(L_0,F\in\mathbb R^{m\times m}\) be real symmetric commuting matrices with \(L_0\) positive definite and \(F\) positive semidefinite. Choose a common orthonormal eigenbasis with eigenvalues \(\ell_j>0\) of \(L_0\) and \(a_j\ge0\) of \(F\), for \(1\le j\le m\). Consider the linear gradient flow \(\dot u=-(L_0+F)u\) and its strictly convex original energy \(E(u)=\tfrac12u^\mathsf T(L_0+F)u\).

For \(\beta\ge0\) split \(L=L_0+\beta I\) and \(g(u)=(\beta I-F)u\), so \(\dot u=-Lu+g(u)\). For each \(h>0\), the precise ETDRK2 update is
\[
 v=e^{-hL}u+(I-e^{-hL})L^{-1}g(u),\qquad
 u^+=v+h\phi_2(-hL)[g(v)-g(u)],
\]
where \(\phi_2(z)=(e^z-1-z)/z^2\) and the continuous value at zero is \(1/2\). These are equations (3.4)--(3.5) of Fu--Shen--Yang specialized to \(G=-I\). No spatial truncation, nonlinear flow, noncommuting operator, floating-point theorem, or arbitrary ETDRK variant is included.

Define \(z_j=h(\ell_j+\beta)>0\), \(t_j=(\ell_j+a_j)/(\ell_j+\beta)>0\), \(s_j=1-e^{-z_j}\), and \(q_j=1-s_j/z_j\). The \(j\)-th modal amplification is exactly
\[
 R(z,t)=1-ts\bigl[1+(1-t)q\bigr],\qquad
 s=1-e^{-z},\quad q=1-\frac{s}{z}.
\]
The energy difference is \(E(u^+)-E(u)=\tfrac12\sum_j(\ell_j+a_j)(R(z_j,t_j)^2-1)|u_j|^2\).

## Proof

**Modal identity.** On an eigenmode \(L\) has value \(d=\ell+\beta\), while \(g\) has value \(d-\lambda\) with \(\lambda=\ell+a\). The predictor satisfies \(v/u=1-(\lambda/d)(1-e^{-hd})=1-ts\). Since \(h\phi_2(-hd)(d-\lambda)(v-u)/u=-t(1-t)s(1-s/(hd))\), the displayed formula follows. Simultaneous diagonalization then gives the exact quadratic energy difference.

**Complete unconditional dissipation classification.** For every finite \(z>0\), \(0<s<1\) and \(0<q<1\). If \(0<t\le1\), then \(0<ts[1+(1-t)q]<t(2-t)\le1\). Hence \(0<R(z,t)<1\). If \(1<t\le2\), then \(0<1-(t-1)q<1\), so \(0<ts[1-(t-1)q]<t\le2\), and therefore \(-1<R(z,t)<1\). At \(t=1\) the exact multiplier is \(e^{-z}\), so it is also strictly within the unit interval. For \(t>2\), taking \(z\to\infty\) yields \(R(z,t)\to(1-t)^2>1\), and continuity supplies finite arbitrarily large timesteps with energy growth in that mode. Consequently, strict decrease for every \(h>0\) and every nonzero \(u\) is equivalent to \(t_j\le2\) for every mode, or equivalently \(a_j-\ell_j\le2\beta\) for every \(j\). Since \(\beta\ge0\), the claimed sharp threshold follows. When any mode has \(t_j=2\), its multiplier tends to \(+1\) as \(h\to\infty\), despite strict energy decrease at every finite step; thus the inequality is sharp even on the boundary and uniform-in-step strict damping is not asserted.

**Rigorous reentrant positivity.** Take the scalar flow \(\dot u=-3u\) decomposed as \(\ell=1\), \(a=2\). Three progressively smaller stabilizers \(\beta=2,19/11,1\) correspond respectively to \(t=1,11/10,3/2\), all within the just-proved energy-stable regime (whose exact threshold is \(\beta=1/2\)). At \(\beta=2\), \(R(z,1)=e^{-z}>0\) for every \(z>0\). At \(\beta=19/11\), choosing \(z=6\), and writing \(w=e^{-6}\), gives the exact identity
\[
 600R(6,11/10)=-5+616w-11w^2<0.
\]
Indeed \(e^6>\sum_{k=0}^{13}6^k/k!>400\), hence \(0<w<1/400\) and \(-5+616w-11w^2<-5+616/400<0\). The physical timestep in this case is \(h=6/(1+19/11)=11/5\). At \(\beta=1\), \(t=3/2\), direct simplification gives
\[
4zR(z,3/2)=z(1+3e^{-z})-3(1-e^{-z})^2.
\]
After multiplication by \(e^{2z}\), the right side becomes \((z-3)e^{2z}+(3z+6)e^z-3\). Its power series has zero constant term and, for every integer \(n\ge1\), strictly positive coefficient
\[
\frac{2^{n-1}(n-6)+3n+6}{n!}.
\]
For \(1\le n\le5\), the numerators are respectively \(4,4,3,2,5\); for \(n\ge6\), they are manifestly positive. Therefore \(R(z,3/2)>0\) for every finite \(z>0\). Decreasing \(\beta\) thus changes unconditional positivity to actual sign reversal and back to unconditional positivity, while energy is decreasing throughout. The claim is this proven three-parameter reentry; no classification of every intermediate positivity interval is asserted.

**Exact minimax stiff-step damping.** If \(L_0=\ell I\), \(\ell>0\), and the eigenvalues of \(F\) range from \(a_-\ge0\) to \(a_+>a_-\), the limiting state multiplier of mode \(a\) as \(h\to\infty\) is \([(\beta-a)/(\ell+\beta)]^2\). Hence the worst limiting state multiplier is \(\max\{(\beta-a_-)^2,(\beta-a_+)^2\}/(\ell+\beta)^2\). On \(0\le\beta\le(a_-+a_+)/2\), the dominant numerator is \((a_+-\beta)^2\), whose square-root ratio decreases strictly with \(\beta\). On \(\beta\ge(a_-+a_+)/2\), it is \((\beta-a_-)^2\), whose square-root ratio increases strictly. Thus the unique minimizer (among all nonnegative stabilizers, and also among the energy-stable ones) is
\[
\beta_*=(a_-+a_+)/2,\qquad
\min_{\beta\ge0}\max_j R(\infty,t_j)=\left(\frac{a_+-a_-}{a_-+a_++2\ell}\right)^2.
\]
It is energy stable because \(2\beta_*=a_-+a_+>a_+-\ell\). For coincident end eigenvalues, the same result becomes the trivial exact zero multiplier at \(\beta_*=a_-=a_+\).

## Verification

The standalone standard-library checker `verify.py` implements the independent predictor--corrector equations and compares their gains against the derived scalar formula for randomized \(h,\ell,a,\beta\). It checks the unit-disk bound in the proposed region, large-step violations beyond the boundary, the exact coefficient pattern for the positivity proof, a rational strict upper bound on \(e^{-6}\), the three-stabilizer witness, and the minimax expression. Run `python verify.py` from the extracted package. The supplied `verify_output.txt` reports 3958 passed deterministic checks. The mathematical proofs above, not finite sampling, establish the universal assertions.

## Relationship to prior work

Fu, Shen and Yang introduced and studied this ETDRK2 scheme as equations (3.4)--(3.5) and proved unconditional original-energy decrease under their sufficient framework with \(\beta\ge C_L\), where \(C_L\) is the Lipschitz constant of the explicit gradient term. For the positive semidefinite linear \(F\) here, this sufficient choice is \(\beta\ge\max_j a_j\), whereas the necessary-and-sufficient commuting-quadratic threshold above can be far smaller. Their paper also discusses stabilization-induced time delay and large-step numerical behavior, which motivate distinguishing energy decrease from positivity and asymptotic damping. The scalar modal multiplier and reentrant sign witness here are direct consequences of the established ETDRK2 update, not new methods or nonlinear generalizations.

Li, Qiao, Wang and Zheng analyze global-in-time ETDRK2 energy stability for a nonlinear phase-field-crystal equation. Their results use nonlinear regularity and a priori bounds rather than furnishing a necessary-and-sufficient commuting-quadratic threshold, but potentially related specialized spectral facts remain a literature-comparison risk. Jiang and coauthors also study maximum-bound-preserving ETD schemes for phase-field models; their MBP guarantees are not equivalent to unconstrained scalar positivity of the present separately split ODE. No claim of uniqueness among all historical exponential-integrator analyses is made.

## Limitations

The classification relies essentially on commutation and simultaneous orthogonal diagonalization; it makes no statement about noncommuting semilinear or nonlinear gradient flows. The reentry result is a concrete rigorous three-stabilizer witness, not a full positivity phase diagram. Large-step minimax damping concerns the limit of the state amplification, not finite-step optimality or global nonlinear error. Numerical checks are noncertifying tests and do not imply a proof beyond the analytic formulas. No independent scientific audit has been performed.

## References

1. Z. Fu, J. Shen, and J. Yang, *Higher-Order Energy-Decreasing Exponential Time Differencing Runge--Kutta methods for Gradient Flows*, arXiv:2402.15142, first submitted 2024-02-23, version 2 (2024-07-22), especially equations (2.7), (3.4)--(3.7), and Theorem 2.1. https://arxiv.org/html/2402.15142v2
2. X. Li, Z. Qiao, C. Wang, and N. Zheng, *Global-in-time energy stability analysis for the exponential time differencing Runge--Kutta scheme for the phase field crystal equation*, arXiv:2406.06272, submitted 2024-06-10. https://arxiv.org/abs/2406.06272
3. K. Jiang et al., *Unconditionally stable exponential time differencing schemes for a phase-field model* (full title as in accessible institutional manuscript), institutional OA manuscript. https://ira.lib.polyu.edu.hk/bitstream/10397/93294/1/Jiang_Unconditionally_Stable_Exponential.pdf
