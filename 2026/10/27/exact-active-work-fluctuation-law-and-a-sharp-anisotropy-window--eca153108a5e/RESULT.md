# Exact active-work fluctuation law and a sharp anisotropy window for confined run-and-tumble motion

## Finding

For a thermal run-and-tumble particle harmonically confined in one dimension, with distinct right/left speeds and switching rates, the stationary active work has an explicit asymptotic variance and Gaussian fluctuation law. More surprisingly, the asymptotic work variance divided by its mean increases initially with trap stiffness and has one strict positive-stiffness maximum **if and only if** the right/left tumbling-rate ratio is strictly between \(1/2\) and \(2\). For every other ratio the normalized work noise strictly decreases with stiffness. The threshold is independent of both speeds and the thermal diffusion coefficient.

Write \(q_R=\alpha_R/2\), \(q_L=\alpha_L/2\), \(\Gamma=q_R+q_L\), \(p_R=q_L/\Gamma\), \(p_L=q_R/\Gamma\), and
\[
 s^2=p_Rp_L(v_R+v_L)^2,\qquad h=(p_L-p_R)(v_R+v_L).
\]
For the integrated normalized active work \(W_T=D^{-1}\int_0^T U_t\circ dX_t\), the exact long-time rates are
\[
 \bar w=\lim_{T\to\infty}\frac{\mathbb EW_T}{T}=\frac{\Gamma s^2}{D(\kappa+\Gamma)},
\]
\[
 \mathcal V=\lim_{T\to\infty}\frac{\operatorname{Var}(W_T)}T
 =2\bar w\left(1+\frac{\kappa s^2}{D(\kappa+\Gamma)^2}
 +\frac{h^2}{D(2\kappa+\Gamma)}\right).
\]
Moreover,
\[
 \frac{W_T-\bar wT}{\sqrt T}\ \Longrightarrow\ \mathcal N(0,\mathcal V).
\]
For \(F(\kappa)=\mathcal V/\bar w\), a unique interior maximizer \(\kappa_*\) exists exactly when \(1/2<\alpha_R/\alpha_L<2\); otherwise \(F\) is strictly decreasing on \((0,\infty)\). When the maximizer exists, \(0<\kappa_*\le\Gamma\), and its dimensionless coordinate \(t=\kappa_*/\Gamma\) is the unique root in \((0,1]\) of
\[
 \frac{(1-t)(1+2t)^2}{(1+t)^3}=\frac{2h^2}{s^2}.
\]
For equal tumbling rates \(\kappa_*=\Gamma\).

## Assumptions and scope

Fix arbitrary real parameters \(\kappa,D,\alpha_R,\alpha_L,v_R,v_L>0\). Let \(\eta_t\) be a continuous-time irreducible Markov chain on \(\{R,L\}\), jumping from \(R\) to \(L\) at rate \(\alpha_R/2\) and conversely at rate \(\alpha_L/2\). Set \(U_t=v_R\) on \(R\) and \(U_t=-v_L\) on \(L\). Let \(B_t\) be independent standard Brownian motion and define
\[
 dX_t=(-\kappa X_t+U_t)dt+\sqrt{2D}\,dB_t.
\]
The pair \((X_t,\eta_t)\) is started from its unique stationary law. Bounded telegraph forcing and positive harmonic damping ensure exponential ergodicity and moments of all orders. The active work \(W_T\) is the Stratonovich path integral above, which equals its Itô counterpart because \(X_t\) is continuous, \(U_t\) has finite-variation jump paths on finite intervals, and \([U,X]=0\). This is the **active-force contribution** to medium entropy flow; the statement does not identify the entire pathwise entropy production including possible internal-state or endpoint contributions.

## Proof

**1. Centering and moment identities.** Define \(m=p_Rv_R-p_Lv_L\), \(V_t=U_t-m\), and \(Y_t=X_t-m/\kappa\). Then
\[
 dY_t=(-\kappa Y_t+V_t)dt+\sqrt{2D}\,dB_t,
 \quad \mathbb EV_t=0,\quad\mathbb EV_t^2=s^2.
\]
The switching generator \(Q\) satisfies \(QV=-\Gamma V\). As \(V\) has exactly two centered values whose sum is \(h\), the pointwise identity \(V^2=s^2+hV\) holds. Applying the full generator \(L\) to \(YV\), \(Y^2\) and \(Y^2V\), and taking stationary expectations yields
\[
 c:=\mathbb E(YV)=\frac{s^2}{\kappa+\Gamma},\qquad
 \mathbb E(Y^2)=\frac D\kappa+\frac c\kappa,\qquad
 \mathbb E(Y^2V)=\frac{2hc}{2\kappa+\Gamma}.
\]
Indeed,
\[
 L(YV)=-(\kappa+\Gamma)YV+s^2+hV,
\]
\[
 L(Y^2)=-2\kappa Y^2+2YV+2D,
 \qquad L(Y^2V)=-(2\kappa+\Gamma)Y^2V+2YV^2+2DV.
\]

**2. Work decomposition and Poisson equation.** Since the constant-force part of work is the endpoint quantity \(m(X_T-X_0)/D\), it contributes neither the asymptotic mean rate nor the variance rate. The centered-force work obeys
\[
 W_T=\frac{m(X_T-X_0)}D
 +\frac1D\int_0^T\big(V_t^2-\kappa Y_tV_t\big)dt
 +\sqrt{\frac2D}\int_0^TV_t\,dB_t.
\]
Its stationary drift mean is \(\bar w=(s^2-\kappa c)/D=\Gamma s^2/[D(\kappa+\Gamma)]\). Let
\[
 A(y,v)=-\kappa(yv-c)+hv,
 \qquad \phi(y,v)=\frac{A(y,v)}{D(\kappa+\Gamma)}.
\]
A direct calculation gives \(L A=-(\kappa+\Gamma)A\) and hence \(L\phi=-A/D\). The martingale decomposition is therefore
\[
 W_T-\bar wT=\frac{m(X_T-X_0)}D+\phi(Y_0,V_0)-\phi(Y_T,V_T)+M_T,
\]
where \(M_T\) combines the continuous work martingale and the martingale part of \(\phi\). Its Brownian coefficient is
\[
 \sqrt{\frac2D}\,\frac{\Gamma}{\kappa+\Gamma}V_t,
\]
and at an orientation flip \(v\mapsto v'\), its jump is
\[
 \Delta M=\frac{(v'-v)(h-\kappa Y_t)}{D(\kappa+\Gamma)}.
\]

**3. Exact bracket rate.** A flip has \((v'-v)^2=(v_R+v_L)^2\). For the flip rate \(q_v\) in the current state, the pointwise identity
\[
 q_v(v'-v)^2=2\Gamma s^2+\Gamma h v
\]
holds. Consequently the stationary mean predictable bracket rate of \(M\) is
\[
 \begin{aligned}
 \mathcal V={}&\frac{2\Gamma^2s^2}{D(\kappa+\Gamma)^2}\\
 &+\frac{\mathbb E[(2\Gamma s^2+\Gamma hV)(h-\kappa Y)^2]}{D^2(\kappa+\Gamma)^2}\\
 ={}&2\bar w\left(1+\frac{\kappa s^2}{D(\kappa+\Gamma)^2}
 +\frac{h^2}{D(2\kappa+\Gamma)}\right),
 \end{aligned}
\]
where the last equality follows by inserting the three stationary moment identities of Step 1 and \(\mathbb E Y=\mathbb EV=0\).

The stationary endpoint term is uniformly bounded in \(L^2\) as \(T\) varies. The ergodic theorem makes \(\langle M\rangle_T/T\to\mathcal V\) almost surely. Finite moments of every order imply the jump-martingale Lindeberg condition, so the martingale central limit theorem gives \(M_T/\sqrt T\Rightarrow\mathcal N(0,\mathcal V)\); endpoint terms vanish on this scale. Stationary fourth moments and Cauchy–Schwarz show the normalized variance of the endpoint and its covariance with \(M_T\) vanish, hence \(\operatorname{Var}(W_T)/T\to\mathcal V\).

**4. Sharp resonance.** Division by \(\bar w\) gives
\[
 F(\kappa)=2\left[1+\frac{\kappa s^2}{D(\kappa+\Gamma)^2}
 +\frac{h^2}{D(2\kappa+\Gamma)}\right].
\]
Thus
\[
 \frac D2 F'(\kappa)=\frac{s^2(\Gamma-\kappa)}{(\kappa+\Gamma)^3}
 -\frac{2h^2}{(2\kappa+\Gamma)^2}.
\]
It is strictly negative when \(\kappa\ge\Gamma\), except that in the symmetric case it vanishes at \(\kappa=\Gamma\) and is strictly negative to the right. On \(0<\kappa<\Gamma\) set \(t=\kappa/\Gamma\); the derivative's sign is the sign of
\[
 G(t)-\frac{2h^2}{s^2},\qquad
 G(t)=\frac{(1-t)(1+2t)^2}{(1+t)^3}.
\]
Here \(G(0)=1\), \(G(1)=0\), and \(G'(t)=-6t(1+2t)/(1+t)^4<0\) for \(0<t<1\). The initial derivative is positive precisely when \(2h^2<s^2\). Since \(h^2/s^2=(\alpha_R-\alpha_L)^2/(\alpha_R\alpha_L)\), this is equivalent to \(1/2<\alpha_R/\alpha_L<2\). Strict decrease of \(G\) gives uniqueness and strictness of the maximum. At the two boundary ratios, \(F'(\kappa)<0\) for all \(\kappa>0\). As \(F(\kappa)>2\) and \(F(\kappa)\to2\) at large stiffness, this is a complete classification.

## Verification

The standalone `check_entropy_work.py` uses exact OU transitions between exponentially distributed orientation flips, not an Euler time-step discretization. Independent finite-time Monte Carlo checks compare \(\mathbb EW_T/T\) and \(\operatorname{Var}(W_T)/T\) against the theorem for symmetric and asymmetric velocities/rates and several confinement/noise strengths. It also checks the sign-change classification and the interior critical point for ratios inside and outside the sharp interval. The program is numerical corroboration only; the infinite-time statements are proved in Steps 1–4.

## Relationship to prior work

Paoluzzi, Puglisi, and Angelani (2024), Section IV, equation (72), proved the stationary **mean** entropy-production rate for the same asymmetric harmonic run-and-tumble dynamics; after identifying \(\kappa=\mu k\), its value equals \(\bar w\) above. Garcia-Millan and Pruessner (2020/2021) derived symmetric harmonic run-and-tumble stationary entropy production and correlation functions. Neither inspected paper states the long-time active-work variance or its sharp nonmonotone confinement region. Padmanabha et al. (2022/2023) compute current/entropy cumulants in a discrete-state finite-track run-and-tumble process rather than this harmonic continuous-position diffusion. Semeraro et al. (2023) analyze active-work fluctuations for a harmonically trapped **Gaussian Ornstein–Uhlenbeck** driving force, not a two-state force with unequal switching rates; Shankar and Marchetti (2018) compare ABP/AOUP work fluctuations in a free active gas. These analyses share techniques or observables but do not imply the dichotomous asymmetric resonance criterion as stated. More general Markov-additive fluctuation theory supplies methodological ingredients, without giving this evaluated closed-form threshold by itself.

## Limitations

Only the two-state, constant-speed, spatially homogeneous Poisson-tumbling harmonic model with \(D>0\) and \(\kappa>0\) is covered. The \(\kappa\downarrow0\) formula is a one-sided limit along stationary confined processes, not an assertion about a nonexistent stationary position law for a freely drifting particle. The result is for active work, not necessarily the full stochastic entropy production including internal-state conventions and boundary contributions. No large-deviation rate function, finite-time exact distribution, or multidimensional interacting-particle extension is claimed. The statement is a mathematically self-reviewed original candidate, not independently validated or guaranteed globally novel; an unidentified more general active-work fluctuation theorem remains a priority risk.

## References

1. M. Paoluzzi, A. Puglisi, and L. Angelani, *Entropy production of run-and-tumble particles*, arXiv:2404.16955 (first publicly available 2024-04-25), Section IV, Eq. (72). https://arxiv.org/abs/2404.16955
2. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, arXiv:2012.02900, J. Stat. Mech. 063203 (2021). https://arxiv.org/abs/2012.02900
3. P. Padmanabha, D. M. Busiello, A. Maritan, and D. Gupta, *Fluctuations of entropy production of a run-and-tumble particle*, arXiv:2207.12091, Phys. Rev. E 107, 014129 (2023). https://arxiv.org/abs/2207.12091
4. M. Semeraro, G. Gonnella, A. Suma, and M. Zamparo, *Work fluctuations for a harmonically confined Active Ornstein-Uhlenbeck Particle*, arXiv:2302.12535 (2023). https://arxiv.org/abs/2302.12535
5. S. Shankar and M. C. Marchetti, *Hidden entropy production and work fluctuations in an ideal active gas*, arXiv:1804.03099, Phys. Rev. E 98, 020604(R) (2018). https://arxiv.org/abs/1804.03099
