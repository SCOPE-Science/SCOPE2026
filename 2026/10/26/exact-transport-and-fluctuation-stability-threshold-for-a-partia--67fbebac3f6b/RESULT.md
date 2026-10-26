# Exact transport and fluctuation-stability threshold for a partially synchronized nonreciprocal dimer

## Finding

A pair of coupled overdamped Brownian particles with four-state correlated telegraph switching has a sharp, explicitly calculable stationary second-moment threshold, even when its instantaneous dynamics is stable on average. In the partially synchronized family, define \(\delta=1-\chi\in(0,1]\) and
\[
\mathcal D(\delta)=k(k+\lambda\delta)(2k+\lambda)-c^2(2k+\lambda\delta).
\]
For positive \(k,\lambda,c,D_x\), the relative coordinate has a finite stationary second moment if and only if \(\mathcal D(\delta)>0\). The active center-of-mass velocity has the **exact universal normalized correlation**
\[
\frac{\mathbb E[v_t v_0]}{\mathbb E[v_0^2]}=e^{-2(k+\lambda)t},\qquad t\ge0,
\]
regardless of the switching synchronization parameter, whenever that moment is finite. Its amplitude and full center-of-mass mean-square displacement are explicit.

The fluctuation-stability boundary and the point at which synchronization reverses its effect on diffusivity differ: stability requires
\[
c^2<\frac{k(k+\lambda\delta)(2k+\lambda)}{2k+\lambda\delta},
\]
whereas the sign of the diffusivity's derivative with respect to asynchrony \(\delta\) is the sign of \(k(2k+\lambda)-2c^2\). These sharp changes are not inferred from a small-fluctuation expansion.

## Assumptions and scope

Let \(J_t\) be a stationary continuous-time Markov chain with state order \((++),(+-),(--),(-+)\), invariant law \(\pi_j=1/4\), and generator
\[
M=\lambda[(1-\chi)M_{\rm mono}+\chi M_{\rm bi}],
\]
where
\[
M_{\rm mono}=\begin{pmatrix}-2&1&0&1\\1&-2&1&0\\0&1&-2&1\\1&0&1&-2\end{pmatrix},\quad
M_{\rm bi}=\begin{pmatrix}-1&0&1&0\\0&-1&0&1\\1&0&-1&0\end{pmatrix}.
\]
The synchronization parameter lies in \(0\le\chi<1\), so this generator is irreducible. The underlying particle-pair interaction has mean stiffness \(k>0\), telegraphic stiffness amplitude \(c>0\), and independent bare Brownian noise diffusivity \(D_x>0\). Set the sum and difference vectors of the fluctuating couplings to
\[
\phi=(2c,0,-2c,0),\qquad\psi=(0,2c,0,-2c).
\]
With independent standard Brownian motions \(W^y,W^X\) independent of \(J\), consider
\[
\mathrm dy_t=-(2k+\phi_{J_t})y_t\,\mathrm dt+\sqrt{4D_x}\,\mathrm dW^y_t,
\quad
\mathrm dX_t=-\tfrac12\psi_{J_t}y_t\,\mathrm dt+\sqrt{D_x}\,\mathrm dW^X_t.
\]
These formulas fix all normalization conventions. The stationary solution of the first equation is used throughout; the center of mass starts from an arbitrary origin, so only increments matter. Define \(v_t=-\psi_{J_t}y_t/2\). Finite-variance conclusions concern stationary initial data for \((y,J)\); no assertion about a stationary law for \(X\) is made.

## Proof

**1. Stationary existence and second-moment threshold.** The ergodic theorem gives average damping \(\mathbb E_\pi[2k+\phi_J]=2k>0\), hence a unique stationary pathwise solution
\[
y_t=\sqrt{4D_x}\int_{-\infty}^t\exp\!\left(-\int_s^t(2k+\phi_{J_u})\,\mathrm du\right)\,\mathrm dW^y_s.
\]
Define \(Q=2\operatorname{diag}(2k+\phi)-M\). The state-resolved second moments \(g_j=\mathbb E[y^2\mathbf1_{\{J=j\}}]\), when finite, satisfy \(Qg=D_x\mathbf1\). The matrix \(-Q=M-2\operatorname{diag}(2k+\phi)\) is irreducible Metzler. Positivity of the state-resolved Brownian integral implies that \(g\) is finite exactly when its Perron spectral abscissa is negative, equivalently when \(Q\) is a nonsingular \(M\)-matrix. Direct elimination gives
\[
\det Q=64(2k+\lambda)\mathcal D(\delta).
\]
At \(c=0\), \(Q\) is a nonsingular \(M\)-matrix. Increasing \(c\) from zero, \(\mathcal D(\delta)\) has a single positive zero. Irreducibility ensures the principal eigenvalue crosses zero at this first singularity, and the Perron spectral abscissa is monotone nondecreasing in \(c\) by convexity and evenness under the exchange \((++)\leftrightarrow(--)\); therefore the stated strict inequality is both necessary and sufficient. At or beyond equality, the stationary second moment is infinite.

**2. Explicit moments.** The involution interchanging the second and fourth states, together with the moment equations, yields \(g_2=g_4=h\) with
\[
h=\frac{D_x[(k+\lambda\delta)(2k+\lambda)-2c^2]}{4\mathcal D(\delta)}.
\]
Only the second and fourth states have nonzero \(\psi\), hence
\[
\mathbb E[v_0^2]=\frac14\sum_j\psi_j^2g_j=2c^2h.
\]

**3. Universal two-time persistence and transport.** Direct multiplication gives \(M\psi=-2\lambda\psi\) and \(\operatorname{diag}(2k+\phi)\psi=2k\psi\). For the stationary mixed process, conditional expectation solves the backward linear equation for the observable \(f(y,j)=\psi_jy\), yielding
\[
\mathbb E[v_t\mid y_0,J_0]=e^{-2(k+\lambda)t}v_0.
\]
Thus \(\mathbb E[v_t v_0]=2c^2h e^{-2(k+\lambda)t}\). The Brownian increment \(W^X_t-W^X_0\) is independent of \((y,J)\), and \(\mathbb E[v_t]=0\). Integration of the covariance yields, for every \(t\ge0\),
\[
\operatorname{Var}(X_t-X_0)=D_xt+\frac{2c^2h}{k+\lambda}t-\frac{c^2h}{(k+\lambda)^2}(1-e^{-2(k+\lambda)t}),
\]
so \(D_{\rm eff}=D_x/2+c^2h/(k+\lambda)\). In the non-finite regime, irreducibility makes the conditional stationary variance infinite in every state; on a positive-probability event with no switch in one of the states \((+-),(-+)\), the integrated active drift contains a nonzero multiple of the initial \(y\), proving infinite center-of-mass increment variance for every \(t>0\).

**4. Exact synchronization-response transition.** Differentiation at fixed \(k,\lambda,c,D_x\) gives
\[
\frac{\mathrm dh}{\mathrm d\delta}=\frac{D_x\lambda c^2[k(2k+\lambda)-2c^2]}{4\mathcal D(\delta)^2}.
\]
Its sign is constant across every stable parameter interval. At \(c^2=k(2k+\lambda)/2\), one obtains exactly \(h=D_x/(2k)\), for all \(\delta>0\). The critical squared amplitude increases strictly from \(k(2k+\lambda)/2\) at \(\delta\downarrow0\) to \(k(k+\lambda)\) at \(\delta=1\). For amplitudes strictly between these two levels, the unique admissible stability boundary occurs at
\[
\delta_* =\frac{2kc^2-k^2(2k+\lambda)}{\lambda[k(2k+\lambda)-c^2]}\in(0,1),
\]
and the stationary second moment is finite exactly when \(\delta>\delta_*\). This is a sharp stabilization-by-asynchrony effect.

## Verification

The bundled standard-library Python checker `checks/verify.py` rebuilds the four-state matrices with exact rational arithmetic and confirms \(Qg=D_x\mathbf1\), \(\det Q=64(2k+\lambda)\mathcal D\), the closed-form \(h\), and the exact eigenvector relations at multiple stable parameter values. It separately calculates finite-lag matrix exponentials and checks their active-velocity covariances against the exponential law, followed by the time-integrated mean-square displacement. In particular, \(k=1\), \(\lambda=2\), \(c=3/2\) yields \(\delta_*=1/7\) exactly. Finite checks support but do not replace the parameter-uniform arguments above.

## Relationship to prior work

Cocconi, Alston and Bertrand (2023, arXiv:2304.07738) introduced correlated mono- and bi-directional switching for this interacting dimer, but analyzed the fully synchronized \(\chi=1\) sector explicitly; that endpoint is reducible, and its stationary sector cannot simply be equated with \(\chi\uparrow1\) through irreducible chains. Alston, Cocconi and Bertrand (2022, arXiv:2202.02630) gave a general finite-state switching Ornstein–Uhlenbeck moment system; the present explicit correlated four-state threshold, active-velocity eigenmode, full transport law and synchronization-response reversal are derived separately. Lindskog and Majumder (2019, arXiv:1904.01474) treated broad regime-switching diffusion behavior without this particular nonreciprocal transport phase portrait.

## Limitations

The result concerns this exactly specified Gaussian-noise linear dimer and an irreducible four-state switching family, not arbitrary nonreciprocal interactions. It characterizes finite second moments, not a full tail exponent or stationary distributions. For \(\chi=1\), the generator becomes reducible and the present joint-invariant-law statements are intentionally not asserted. The absence of a found equivalent result is not a proof that no unindexed derivation exists; independent scientific review has not been performed.

## References

- Cocconi, Alston, and Bertrand, *Active bound states arise from transiently nonreciprocal pair interactions* (2023), arXiv:2304.07738, https://arxiv.org/abs/2304.07738 .
- Alston, Cocconi, and Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials* (2022), arXiv:2202.02630, https://arxiv.org/abs/2202.02630 .
- Lindskog and Majumder, *Exact long time behavior of some regime switching stochastic processes* (2019), arXiv:1904.01474, https://arxiv.org/abs/1904.01474 .
