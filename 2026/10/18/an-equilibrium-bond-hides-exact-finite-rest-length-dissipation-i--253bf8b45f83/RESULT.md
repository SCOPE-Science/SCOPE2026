# An equilibrium bond hides exact finite-rest-length dissipation in a nonreciprocal Brownian dimer

## Finding

For the two-dimensional overdamped Brownian dimer defined below, **the complete stationary trajectory law of the relative displacement, not just its bond-length distribution, is independent of the division of spring stiffness between the two monomers** when their sum is fixed. Nevertheless, the joint two-monomer dynamics dissipates energy at a strictly positive rate whenever the stiffnesses differ. The exact entropy-production rate, valid for every nonnegative spring rest length (including genuinely nonlinear positive rest length), is

\[
\sigma=\frac{(k_2-k_1)^2}{2\gamma k_{\mathrm B}T}\left\langle F,(-L_q)(a-L_q)^{-1}F\right\rangle_{\pi},
\qquad a=\frac{k_0}{\gamma},
\]

where the inner product sums both Cartesian components, \(F(q)=(|q|-\ell)q/|q|\) away from the origin, and \(L_q\) is the explicitly reversible relative-coordinate generator given below. The resolvent quadratic form is strictly positive and depends on \(k_0,k_1+k_2,\ell,T,\gamma\), but **not** on \(k_2-k_1\). Hence the dissipation varies **exactly quadratically** in the stiffness asymmetry at fixed sum, even though any experiment recording only the complete bond trajectory sees precisely the same process as in the reciprocal equilibrium case. In particular, no bond-only path statistic can identify the sign or magnitude of this asymmetry.

In the linear zero-rest-length case, the exact formula reduces to the check

\[
\sigma=\frac{2(k_2-k_1)^2}{\gamma(2k_0+k_1+k_2)}.
\]

## Assumptions and scope

Take \(k_0,\gamma,T,k_1,k_2>0\), \(\ell\ge0\), Boltzmann constant \(k_{\mathrm B}>0\), and independent standard two-dimensional Brownian motions \(W_1,W_2\). The monomer positions \(r_1,r_2\in\mathbb R^2\) obey

\[
\begin{aligned}
d r_1&=-\gamma^{-1}[k_0r_1+k_1F(q)]\,dt+\sqrt{2D}\,dW_1,\\
d r_2&=-\gamma^{-1}[k_0r_2-k_2F(q)]\,dt+\sqrt{2D}\,dW_2,\\
q&=r_1-r_2,\qquad D=k_{\mathrm B}T/\gamma.
\end{aligned}
\]

Set \(F(0)=0\), which has no effect on the process because the relative diffusion is nondegenerate; for \(\ell>0\) the radial force is bounded but direction-discontinuous at the origin. These equations have an ergodic stationary weak solution; their polynomial-moment bounds follow from the quadratic confinement and bounded radial perturbation. The entropy production \(\sigma\) is the stationary long-time mean of the total Stratonovich environmental heat divided by \(k_{\mathrm B}T\) and elapsed time. All limits are for fixed finite model parameters; the result does not assert a closed elementary formula for the full four-dimensional invariant density.

Define \(s=k_1+k_2\), \(b=s/\gamma\), \(\delta=(k_2-k_1)/(2\gamma)\), and \(R=(r_1+r_2)/2\). The relative generator acting on scalar test functions \(\varphi\) is

\[
L_q\varphi=2D\Delta\varphi-(a q+bF(q))\cdot\nabla\varphi,
\qquad
\pi(dq)=Z^{-1}\exp\!\left[-\frac{a|q|^2+b(|q|-\ell)^2}{4D}\right]dq.
\]

The relative bond length \(r=|q|\) has density proportional to \(r\exp[-(k_0r^2+s(r-\ell)^2)/(4k_{\mathrm B}T)]\) on \(r>0\). No separate limit of small \(\ell\), weak asymmetry, or weak coupling is assumed.

## Proof

**1. Exact autonomous relative dynamics.** Orthogonally combine the noises as \(B^q=(W_1-W_2)/\sqrt2\) and \(B^R=(W_1+W_2)/\sqrt2\). They are independent standard planar Brownian motions. Direct subtraction and averaging yield

\[
\begin{aligned}
dq_t&=-(a q_t+bF(q_t))\,dt+\sqrt{4D}\,dB_t^q,\\
dR_t&=(-aR_t+\delta F(q_t))\,dt+\sqrt D\,dB_t^R.
\end{aligned}
\]

The first autonomous diffusion is the gradient system with potential \(V(q)=a|q|^2/2+b(|q|-\ell)^2/2\) and diffusivity \(2D\), thus has the normalized invariant density \(\pi\) stated above and a reversible stationary path law. In particular its semigroup, finite-dimensional distributions and the law of the full continuous stationary path depend on the spring constants only through their sum \(s\). This includes the reciprocal choice \(k_1=k_2=s/2\).

**2. Stationary causal representation.** Stability of the center equation and independence of the two noises give the unique stationary construction

\[
R_t=\delta\int_0^\infty e^{-au}F(q_{t-u})\,du
+\sqrt D\int_{-\infty}^{t}e^{-a(t-u)}dB^R_u.
\]

The last noise integral is centered and independent of the relative path. By stationarity, reversibility of the relative diffusion, and Fubini (the force has all polynomial moments),

\[
\langle R\cdot F(q)\rangle
=\delta\int_0^\infty e^{-au}C_F(u)\,du,
\qquad C_F(u)=\mathbb E_\pi[F(q_0)\cdot F(q_u)].
\]

The Laplace integral equals \(\langle F,(a-L_q)^{-1}F\rangle_\pi\) by the resolvent representation of the reversible semigroup.

**3. Exact stationary heat and entropy.** Write the monomer forces divided by friction as \(v_1=-a r_1-k_1F/\gamma\) and \(v_2=-a r_2+k_2F/\gamma\). Under the linear invertible change \((r_1,r_2)\leftrightarrow(R,q)\), their Stratonovich work becomes

\[
\begin{aligned}
v_1\cdot\circ dr_1+v_2\cdot\circ dr_2
={}&(-2aR+2\delta F(q))\cdot\circ dR\\
&-\tfrac12(aq+bF(q))\cdot\circ dq.
\end{aligned}
\]

The term \(-2aR\cdot\circ dR\) is the exact differential \(-a\,d|R|^2\). The entire \(q\) term is the exact differential of \(-[a|q|^2+b(|q|-\ell)^2]/4\). Their stationary mean rates vanish; the origin's radial nonsmoothness does not affect the chain rule (approximate the radial potential by smooth convex radial functions, or apply the locally absolutely continuous radial chain rule away from a polar point). Since \(B^R\) and \(B^q\) are independent, \(F(q)\) and \(R\) have zero instantaneous quadratic covariation. Consequently

\[
\begin{aligned}
\sigma
&=\frac{2\delta}{D}\mathbb E[F(q_t)\cdot(-aR_t+\delta F(q_t))]\\
&=\frac{2\delta^2}{D}\left(\langle |F|^2\rangle_\pi-a\int_0^\infty e^{-au}C_F(u)du\right)\\
&=\frac{2\delta^2}{D}\left\langle F,(-L_q)(a-L_q)^{-1}F\right\rangle_\pi,
\end{aligned}
\]

where the last equality uses \(I-a(a-L_q)^{-1}=(-L_q)(a-L_q)^{-1}\). Substitution of \(2\delta^2/D=(k_2-k_1)^2/(2\gamma k_{\mathrm B}T)\) proves the displayed formula. At equilibrium in the reciprocal case, the full drift is a gradient, so this stationary heat agrees with the usual path-relative-entropy production normalization; the standard isothermal overdamped equivalence also applies away from the reciprocal case.

**4. Strictness and no-go inference.** The Dirichlet form of \(-L_q\) is \(2D\int|\nabla\varphi|^2d\pi\), and the confining reversible semigroup has constants as its only zero mode. Rotational symmetry gives \(\langle F\rangle_\pi=0\), while \(\langle|F|^2\rangle_\pi>0\). Thus the spectral theorem shows

\[
0<\left\langle F,(-L_q)(a-L_q)^{-1}F\right\rangle_\pi
<\langle |F|^2\rangle_\pi.
\]

The strict upper inequality follows because \(a>0\) and the resolvent quadratic form is positive. The lower follows because \(F\) has no zero-eigenvalue component and is nonzero. Therefore \(\sigma=0\) exactly when \(k_1=k_2\); otherwise the positive rate depends quadratically on asymmetry at fixed sum. Meanwhile the complete \(q\)-path distribution is identical for all these parameter choices, proving that no statistic measurable from that path can distinguish them.

**5. Check at zero rest length.** When \(\ell=0\), \(F(q)=q\), and the planar relative diffusion is Ornstein–Uhlenbeck with relaxation \(a+b\) and \(\langle|q|^2\rangle=4D/(a+b)\). Its force autocorrelation is \(C_F(u)=4D\exp[-(a+b)u]/(a+b)\), giving

\[
\langle |F|^2\rangle-a\int_0^\infty e^{-au}C_F(u)du
=\frac{4D}{2a+b}.
\]

It follows that \(\sigma=8\delta^2/(2a+b)=2(k_2-k_1)^2/[\gamma(2k_0+k_1+k_2)]\), as claimed.

## Verification

The standalone file `verify.py` implements two independent tests of the proof: an exact covariance/Lyapunov calculation of the linear zero-rest-length dynamics, and a finite-difference solution of the nonlinear radial first-angular-harmonic Poisson problem. For the radial resolvent, writing \((a-L_q)^{-1}F(q)=g(r)q/r\) gives the scalar boundary-value equation

\[
a g-2D(g''+g'/r-g/r^2)+[(a+b)r-b\ell]g'=r-\ell,
\]

regular at the origin, with decaying growth relative to its linear large-radius asymptotic. The stationary radial weight is \(r\exp[-(a r^2+b(r-\ell)^2)/(4D)]\). The script checks three independent zero-rest-length OU identities, three zero-rest-length radial quadratures, and grid convergence/positivity for \(\ell=0.4,0.8,1.5\) (all at positive stiffness and diffusion). These are finite numerical crosschecks, not proofs of the spectral strictness or general formula; those are provided above.

Run `python verify.py` with Python 3, NumPy and SciPy. All dependencies are mainstream third-party numerical libraries, and the script is standalone.

## Relationship to prior work

Pramanik, Dutta and Saha (2026), arXiv:2607.27740, introduced this trapped planar nonreciprocal Brownian dimer, solved its full four-dimensional stationary Gaussian law and currents at zero spring rest length, and studied nonzero rest length numerically. Its finite-rest-length numerical section does not provide the present explicit bond-only stationary path law or exact positive entropy-production resolvent identity. Its statement that the *full joint* finite-rest-length invariant law lacks a closed form is consistent with this result: only a particular autonomous projection and a scalar Green operator are solved here.

The two-particle sector of Zhang and Garcia-Millan (2023), arXiv:2209.09721, already gives a general exact pair-separation barometric distribution and entropy production for nonreciprocal interactions on a one-dimensional periodic ring without a harmonic trap. Therefore the relative-coordinate equilibrium observation, taken alone, is **not** claimed as a new general principle. Their periodic-ring formula lacks the trapped center coordinate and the finite-rest-length planar resolvent that controls its physical dissipation. Loos and Klapp (2020), arXiv:2008.00894, develop general nonreciprocal Langevin thermodynamics and exactly solvable linear systems; this work likewise does not claim the general coordinate reduction or stochastic-energetics formalism as novel.

The assessed joint contribution is the exact, all-\(\ell\) coincidence of full observed bond paths with equilibrium **combined** with strictly positive, exactly quadratic hidden dissipation and a recoverable model-specific resolvent coefficient. General path-level coarse-graining is known to conceal entropy production; the value here is its parameter-sharp realization in the nonlinear trapped dimer.

## Limitations

The theorem requires equal monomer friction, equal bath temperature, a common isotropic harmonic trap, the same central radial rest-length force profile for both monomers, finite positive stiffnesses, and two spatial dimensions. Altering diffusivities, monomer frictions, traps, or applying a noncentral force may destroy the autonomous equilibrium bond law. The resolvent need not admit an elementary closed expression for positive rest length. No statement is made about full-system stationary density, finite-time fluctuation theorems, optimal energy transduction, or identifiability from observables that include the monomer center. The exact EPR relies on continuous-time stationary trajectories and standard overdamped even-position time reversal.

## References

1. S. Pramanik, S. Dutta and A. Saha, “Non-reciprocity drives a Brownian dimer out of equilibrium,” arXiv:2607.27740v1 (2026), https://arxiv.org/abs/2607.27740.
2. Z. Zhang and R. Garcia-Millan, “Entropy production of non-reciprocal interactions,” *Physical Review Research* **5**, L022033 (2023), arXiv:2209.09721, https://arxiv.org/abs/2209.09721.
3. S. A. M. Loos and S. H. L. Klapp, “Irreversibility, heat and information flows induced by non-reciprocal interactions,” *New Journal of Physics* **22**, 123051 (2020), arXiv:2008.00894, https://arxiv.org/abs/2008.00894.
4. U. Seifert, “Stochastic thermodynamics, fluctuation theorems and molecular machines,” *Reports on Progress in Physics* **75**, 126001 (2012).
