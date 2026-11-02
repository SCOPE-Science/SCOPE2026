# Frozen-bath convergence and a Gaussian observation-window crossover for resetting tracers

## Finding

For the partially reset two-coordinate diffusion defined below, fix a resetting rate \(r>0\), let the bath friction \(\gamma\to\infty\), and begin the dynamics in its unique stationary law \(\pi_\gamma\). Put
\[
k=\frac{r}{1+r},\qquad p=\frac{1}{r(1+r)},\qquad
\Phi(z)=\begin{cases}2(z-1+e^{-z})/z^2,&z>0,\\1,&z=0.\end{cases}
\]
There is **joint stationary weak convergence**
\[
\pi_\gamma(dx,dq)\Longrightarrow
\frac{e^{-q^2/(2/k)}}{\sqrt{2\pi/k}}\,dq\;\nu_q(dx),
\]
where \(\nu_q\) is the exact reset-Ornstein--Uhlenbeck invariant probability conditional on the frozen bath value \(q\):
\[
\nu_q(dx)=\int_0^\infty r e^{-ru}\,
\mathcal N\big(q(1-e^{-u}),1-e^{-2u}\big)(dx)\,du.
\]
The resulting tracer marginal coincides with the previously proposed quasi-static Gaussian mixture; the novelty here is a stationary convergence argument and the accompanying distributional observation-window classification.

For any deterministic \(T_\gamma\to\infty\), define the stationary empirical position average
\[
\overline X_{T_\gamma}=\frac1{T_\gamma}\int_0^{T_\gamma}X_t\,dt.
\]
The complete three-regime limit is:
\[
\begin{array}{ll}
T_\gamma/\gamma\to0:&\overline X_{T_\gamma}\Longrightarrow\mathcal N(0,p),\\[2pt]
T_\gamma/\gamma\to s\in(0,\infty):&\overline X_{T_\gamma}\Longrightarrow\mathcal N(0,p\Phi(ks)),\\[2pt]
T_\gamma/\gamma\to\infty:&\overline X_{T_\gamma}\to0\quad\text{in }L^2.
\end{array}
\]
In the middle regime the second moments converge to \(p\Phi(ks)\). The continuous, strictly decreasing crossover \(\Phi\) tends to \(1\) for short scaled windows and decays as \(2/z\) for large scaled windows. Thus arbitrarily long observation windows can retain an order-one random calibration offset when the bath timescale grows even faster; for every fixed finite bath friction that offset eventually vanishes.

## Assumptions and scope

Let \(W^x,W^q\) be independent standard Brownian motions and \(N_t\) an independent Poisson process of rate \(r>0\). Between reset events,
\[
\begin{aligned}
dX_t&=(Q_t-X_t)\,dt+\sqrt2\,dW_t^x,\\
dQ_t&=\frac{X_t-Q_t}{\gamma}\,dt+\sqrt{\frac2\gamma}\,dW_t^q.
\end{aligned}
\]
At every event of \(N_t\), only \(X_t\) jumps to zero; \(Q_t\) remains continuous. All limits are for a fixed strictly positive \(r\), an initially stationary process, and the positive parameter \(\gamma\to\infty\). The diffusion is on the full real line in both coordinates. The statement does not assert uniform convergence of far spatial tails or any result for a bath-reset protocol.

## Proof

**1. Stationarity and moment bounds.** The generator, acting on smooth test functions, is
\[
\mathcal L_\gamma f=(q-x)f_x+f_{xx}+\gamma^{-1}(x-q)f_q+\gamma^{-1}f_{qq}+r[f(0,q)-f(x,q)].
\]
For \(V(x,q)=x^2+\gamma q^2\), direct calculation gives
\[
\mathcal L_\gamma V=4-rx^2-2(x-q)^2.
\]
The negative quadratic form is strictly coercive for each \(\gamma,r>0\). Together with nondegenerate Gaussian diffusion, this supplies the usual irreducibility and Foster--Lyapunov conditions for a unique stationary law with finite second moments. The centered stationary moments, obtained by setting the generators of \(x^2,xq,q^2\) to zero, are
\[
\begin{aligned}
U_\gamma:=\mathbb E[X^2]&=\frac{2[\gamma(r+1)+1]}{r[\gamma(r+2)+1]},\\
H_\gamma:=\mathbb E[XQ]&=\frac{\gamma(r+2)+2}{r[\gamma(r+2)+1]},\\
V_\gamma:=\mathbb E[Q^2]&=\frac{(r+2)[\gamma(r+1)+1]}{r[\gamma(r+2)+1]}.
\end{aligned}
\]
In particular these moments are uniformly bounded for large \(\gamma\), and \(V_\gamma\to1/k=(r+1)/r\). The stationary mean is zero by the linear first-moment equations. These moment identities already follow from established second-order generator methods; the new argument starts with their uniform bounds.

**2. A vanishing martingale remainder.** With \(\widetilde N_t=N_t-rt\), the exact semimartingale equation is
\[
dX_t=[-(1+r)X_t+Q_t]dt+dM_t,
\qquad dM_t=\sqrt2\,dW_t^x-X_{t-}\,d\widetilde N_t.
\]
Consequently, for every \(u\ge0\),
\[
\frac1\gamma\int_0^{\gamma u}X_tdt
=\frac1{1+r}\int_0^u Q_{\gamma v}dv+R_\gamma(u),\qquad
R_\gamma(u)=\frac{M_{\gamma u}-X_{\gamma u}+X_0}{(1+r)\gamma}.
\]
Since the compensated jump martingale and the Brownian martingale have zero mutual predictable covariation,
\[
\mathbb E[M_{\gamma u}^2]=\gamma u(2+rU_\gamma).
\]
Stationarity also bounds \(\mathbb E[(X_{\gamma u}-X_0)^2]\le4U_\gamma\). Hence for every fixed \(S>0\),
\[
\sup_{0\le u\le S}\mathbb E|R_\gamma(u)|^2=O_{r,S}(\gamma^{-1}).
\]

**3. The stationary bath becomes an Ornstein--Uhlenbeck process.** Rescale \(Q^\gamma_u=Q_{\gamma u}\), and \(B^\gamma_u=\gamma^{-1/2}W^q_{\gamma u}\). Step 2 inserted into the bath equation gives the exact integral relation
\[
Q^\gamma_u=Q^\gamma_0-k\int_0^u Q^\gamma_v\,dv+\sqrt2B^\gamma_u+R_\gamma(u).
\]
The corresponding unperturbed Ornstein--Uhlenbeck solution, using the same initial bath coordinate and the same future Brownian noise, differs from \(Q^\gamma\) by an \(L^2\) quantity tending to zero at each finite scaled time, and in integrated \(L^2\) on compact scaled intervals. The stationary initial bath marginals are tight by Step 1. If a subsequence of them converges weakly to a probability \(\zeta\), stationarity implies that \(\zeta\) is invariant under the Ornstein--Uhlenbeck semigroup of drift \(-kq\) and diffusivity \(\sqrt2\). That semigroup has the unique invariant law \(\mathcal N(0,1/k)\). Thus the entire initial-bath sequence converges to this Gaussian, and \(Q^\gamma\) converges in finite-dimensional distributions, with its compact-interval integrals, to the stationary diffusion
\[
dQ_u=-kQ_u\,du+\sqrt2\,dB_u,\qquad Q_0\sim\mathcal N(0,1/k).
\]
Future Brownian increments are independent of the stationary initial state; no assumption of independent probe excursions is made.

**4. The full joint stationary law.** The moment bound makes \(\{\pi_\gamma\}\) tight. Any weak subsequential limit \(\pi_\infty\) satisfies the stationary martingale-generator identity for
\[
\mathcal L_\infty f=(q-x)f_x+f_{xx}+r[f(0,q)-f(x,q)],
\]
because the two \(q\)-derivative terms in \(\mathcal L_\gamma\) are \(O(\gamma^{-1})\) after integration against compactly supported smooth functions. Disintegrating \(\pi_\infty(dx,dq)\) over its \(q\)-marginal shows that, for almost every \(q\), the conditional \(x\)-law is invariant for the one-dimensional Ornstein--Uhlenbeck diffusion pulled toward \(q\) and reset to zero at rate \(r\). This has a unique invariant law, obtained by conditioning on the time since the last Poisson reset: precisely \(\nu_q\) in the statement. Step 3 identifies the \(q\)-marginal as \(\mathcal N(0,1/k)\). Every subsequential limit is therefore the same stated joint law, proving full weak convergence. This is convergence at fixed spatial scales, not a claim about tails under simultaneous spatial scaling.

**5. Observation windows.** For \(T_\gamma/\gamma\to s\in(0,\infty)\), Step 2 and Step 3 give
\[
\overline X_{T_\gamma}\Longrightarrow
\frac1{(1+r)s}\int_0^s Q_u\,du.
\]
The integral is centered Gaussian. Its variance is
\[
\frac{1}{(1+r)^2s^2}\int_0^s\!\int_0^s\frac{e^{-k|u-v|}}{k}\,du\,dv
=\frac1{r(1+r)}\Phi(ks).
\]
For \(T_\gamma/\gamma\to0\) with \(T_\gamma\to\infty\), the same exact martingale identity gives an error of mean-square order \(O(T_\gamma^{-1})\) between \(\overline X_{T_\gamma}\) and \((1+r)^{-1}T_\gamma^{-1}\int_0^{T_\gamma}Q_tdt\). The bath equation and the uniform second-moment bound imply
\[
\mathbb E|Q_t-Q_0|^2\le C_r[(t/\gamma)^2+t/\gamma].
\]
Its time-average is therefore \(L^2\)-close to \(Q_0\), whose law converges to the Gaussian from Step 3. This proves the first regime.

For the last regime, let \(K_\gamma(t)=\mathbb E[X_tX_0]\) under stationarity. Conditional-mean evolution is linear with
\[
B_\gamma=\begin{pmatrix}-(1+r)&1\\\gamma^{-1}&-\gamma^{-1}\end{pmatrix},\quad
K_\gamma(t)=(1,0)e^{tB_\gamma}(U_\gamma,H_\gamma)^{\mathsf T}.
\]
The matrix is Hurwitz and Metzler, so \(K_\gamma(t)\ge0\). Its exact integrated covariance is
\[
\int_0^\infty K_\gamma(t)dt
=\frac{U_\gamma+\gamma H_\gamma}{r}
=\frac2{r^2}+\frac{\gamma^2(r+2)}{r^2[\gamma(r+2)+1]}=O_r(\gamma).
\]
Therefore
\[
\mathbb E[\overline X_T^2]=\frac2{T^2}\int_0^T(T-t)K_\gamma(t)dt
\le\frac2T\int_0^\infty K_\gamma(t)dt,
\]
which tends to zero when \(T_\gamma/\gamma\to\infty\). The same formula also implies the stated middle-regime variance convergence by the exact matrix exponential and bounded convergence. These covariance identities are useful verification tools rather than claimed new independently of previous two-time studies.

## Verification

The standalone file `CHECK.py` performs exact rational Gaussian elimination on the second- and fourth-order stationary generator identities, compares the integrated covariance both through the generator resolvent and its spectral decomposition, numerically integrates the stationary two-time covariance, and checks the predicted slow-bath window variance against finite-parameter approximations. It also compares fourth-order stationary moments with those of the explicit limiting Gaussian mixture. Run with `python3 CHECK.py`; it requires only Python's standard library. Passing finite checks is not a proof of the weak-convergence theorem; the martingale, invariant-measure and tightness arguments above supply that proof.

## Relationship to prior work

Santra and Das, *Resetting in a viscoelastic bath: the bath remembers* (first public preprint March 17, 2026), introduced exactly this model, derived its finite-parameter second-moment equations and proposed the large-bath-timescale tracer marginal as an Ornstein--Uhlenbeck mixture using a quasi-static approximation. Neither that model nor that marginal mixture formula is claimed new here. The present finding supplies a joint invariant-law convergence justification and a distribution-level classification of stationary empirical position averages over growing observation windows.

Biswas, Dubbeldam, Sandev and Pal, *A resetting particle embedded in a viscoelastic bath* (first preprint December 12, 2024), studied two-time correlations through renewal theory with resetting of the full memory-bearing state, whereas the bath coordinate here continues through each tracer reset. Maes and Thiery, *The induced motion of a probe coupled to a bath with random resettings* (2017), reset the bath particles rather than the probe. These are related but structurally different resetting protocols. Previously available exact stationary covariance and asymmetry calculations for the same partially reset model already determine several second-order identities used above; the new statement is the full joint weak limit and the Gaussian distributional window crossover, which do not follow from a covariance function alone.

## Limitations

The theorem assumes a single harmonic bath coordinate, independent thermal noises, instantaneous memory-preserving resets of the tracer only, a fixed positive reset rate, and initially stationary sampling. It does not address nonlinear or multi-relaxation baths, non-Poisson resetting, nonstationary initial transients, sample-quantile error bounds, functional central limit theorems for the full tracer trajectory, or uniform estimates of the far tails as \(\gamma\to\infty\). The limits are ordinary weak convergence and stated second-moment convergence, not a claim of independent external verification or publication priority. For each finite \(\gamma>0\), the long observation-time average converges to zero; the nonzero Gaussian plateau only appears in an order-of-limits regime.

## References

1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1, submitted March 17, 2026. https://arxiv.org/html/2603.17027v1
2. A. Biswas, J. L. A. Dubbeldam, T. Sandev and A. Pal, *A resetting particle embedded in a viscoelastic bath*, arXiv:2412.09260, submitted December 12, 2024; *Chaos* **35**, 031102 (2025). https://arxiv.org/abs/2412.09260
3. C. Maes and T. Thiery, *The induced motion of a probe coupled to a bath with random resettings*, arXiv:1705.07670, submitted May 22, 2017. https://arxiv.org/abs/1705.07670
