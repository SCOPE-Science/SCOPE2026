# Exact stationary cloaking and one-lag recovery in an intermittent resetting walk

## Finding

A diffusive/ballistic intermittent searcher can have exactly the stationary spatial law of a purely Brownian resetting particle, regardless of which of the two modes is reselected at reset. The equality is **exactly** restricted to one rate-matching hypersurface, and it conceals rather than removes a strictly ordered family of different temporal correlations.

Here is the precise all-parameter statement. Let \(\alpha,\beta,r,D,v>0\) and \(p\in[0,1]\). Define
\[
B=\beta+r,\qquad \Lambda=\alpha+\beta+r.
\]
Consider the three-mode process in the next section, with its unique stationary law. Let \(\Phi_p(q)=\mathbb E[e^{iqX_0}]\) be its stationary spatial characteristic function. Write \(\Phi_{\mathrm{Br}}(q)=r/(r+Dq^2)\) for Brownian motion of diffusivity \(D\), restarted at the origin at rate \(r\).

Then, for every \(p\in[0,1]\),
\[
\boxed{\ \Phi_p(q)=\Phi_{\mathrm{Br}}(q)\ \text{for all real }q
\quad\Longleftrightarrow\quad v^2=D(\beta+r).\ }
\]
On this and only this hypersurface, every reset-mode mixture \(p\) has the same stationary *position* density,
\[
\boxed{\ f_p(x)=\frac12\sqrt{\frac rD}\,
\exp\!\left(-\sqrt{\frac rD}\,|x|\right),\qquad x\in\mathbb R.\ }
\]
For every \(t\ge0\), the stationary position autocovariance on this hypersurface is nevertheless
\[
\boxed{\ C_p(t)=\mathbb E[X_tX_0]
=e^{-rt}\left[\frac{2D}{r}
+\frac{D}{\beta}\frac{\alpha+(1-p)r}{\Lambda}
\big(1-e^{-\beta t}\big)\right].\ }
\]
Consequently, for each \(t>0\) and \(0\le p_1<p_2\le1\),
\[
C_{p_1}(t)>C_{p_2}(t)>\frac{2D}{r}e^{-rt}
=C_{\mathrm{Br}}(t).
\]
In particular, if \(\alpha,\beta,r,D\) are known, a single ideal nonzero-lag covariance measurement uniquely recovers the unknown reset mixture \(p\):
\[
\boxed{\ p=1+\frac\alpha r-
\frac{\beta\Lambda}{rD}\,
\frac{e^{rt}C_p(t)-2D/r}{1-e^{-\beta t}},\qquad t>0.\ }
\]
Off the matching hypersurface, different values of \(p\) already give different stationary position variances, so the loss of one-time identifiability occurs at exactly this hypersurface.

## Assumptions and scope

The position \(X_t\in\mathbb R\) and mode \(S_t\in\{0,+1,-1\}\) evolve as follows. In mode \(0\), position performs Brownian motion with generator \(D\partial_{xx}\). In modes \(+1\) and \(-1\), it moves deterministically with respective velocities \(+v\) and \(-v\). The transition \(0\to+1\) occurs at rate \(\alpha/2\) and \(0\to-1\) at rate \(\alpha/2\), while each ballistic mode transitions to mode \(0\) at rate \(\beta\).

An independent Poisson clock of rate \(r\) instantaneously resets the position to zero and independently selects a new mode: \(0\) with probability \(p\), or each ballistic direction with probability \((1-p)/2\). Every reset renews the *whole* trajectory. The model has no targets or absorbing boundaries. All expectations in the theorem are taken in the unique stationary regime, not from an isolated fresh start. The sign and orientation symmetry imply \(\mathbb E[X_t]=0\).

The rates \(\alpha,\beta,r,D,v\) are strictly positive throughout; the mixture endpoints \(p=0\) and \(p=1\) are included. No singular zero-rate limits are incorporated into the iff statement.

## Proof

**1. Regeneration and the spatial transform.** Full-state Poisson renewal at rate \(r>0\) gives a unique stationary law by taking the state observed at an independent exponential age after a fresh reset. Finite stationary second moments follow because the displacement up to age \(T\) is bounded in absolute value by the ballistic bound \(vT\) plus a Brownian stochastic integral of quadratic variation at most \(2DT\), with \(\mathbb E[T^2]<\infty\).

For any real Fourier frequency \(q\), put \(z=q^2\). The stationary Fourier transforms of the mode-conditioned spatial measures satisfy
\[
\begin{aligned}
0&=-(r+\alpha+Dz)\widehat f_0
+\beta(\widehat f_++\widehat f_-)+rp,\\
0&=\frac\alpha2\widehat f_0-(r+\beta-ivq)\widehat f_+
+\frac{r(1-p)}2,\\
0&=\frac\alpha2\widehat f_0-(r+\beta+ivq)\widehat f_-
+\frac{r(1-p)}2.
\end{aligned}
\]
The sign convention on the two imaginary terms can be exchanged by interchanging the ballistic labels, without changing the spatial marginal. Eliminating the three unknown transforms gives
\[
\Phi_p(q)=\frac{r\left[B\Lambda+
\left(pv^2+(1-p)DB\right)z\right]}{H(z)},
\qquad
H(z)=(r+\alpha+Dz)(B^2+v^2z)-\alpha\beta B.
\]
For \(z\ge0\),
\[
H(z)=rB\Lambda+\big(DB^2+(r+\alpha)v^2\big)z+Dv^2z^2>0.
\]
This explicit positivity also rules out any singular Fourier denominators on the real line.

**2. The sharp cloaking equivalence.** Subtracting the standard Brownian resetting characteristic function yields the exact factorization
\[
\Phi_p(q)-\frac{r}{r+Dz}
=\frac{r\,[DB-v^2]z\,[\alpha+(1-p)(r+Dz)]}
{H(z)(r+Dz)}.
\]
For any \(q\ne0\), the last factor in the numerator is strictly positive because \(\alpha>0\) and \(0\le p\le1\). Hence equality of the stationary spatial laws is **necessary** only when \(v^2=DB\). Conversely, on that hypersurface,
\[
H(z)=B(r+Dz)(\Lambda+Dz),
\]
and the numerator of \(\Phi_p\) is \(rB(\Lambda+Dz)\); cancellation gives \(\Phi_p(q)=r/(r+Dq^2)\) for every real \(q\). Fourier inversion yields the stated normalized Laplace density.

The same computation shows that off the hypersurface
\[
\Phi_{p_1}(q)-\Phi_{p_2}(q)
=\frac{r(p_1-p_2)(v^2-DB)q^2}{H(q^2)},
\]
which is nonzero for all \(q\ne0\) whenever \(p_1\ne p_2\).

**3. A generator calculation of the temporal covariance.** The stationary mode probabilities are
\[
\pi_0=\frac{\beta+pr}{\Lambda},\qquad
\pi_{\rm ball}=\frac{\alpha+(1-p)r}{\Lambda}.
\]
The generator acting on the signed ballistic mode and its position product gives
\[
\mathcal LS=-(\beta+r)S,
\qquad
\mathcal L(XS)=v\mathbf 1_{\{S\ne0\}}-(\beta+r)XS.
\]
Consequently, stationarity implies
\[
\mathbb E[X_0S_0]=\frac{v\pi_{\rm ball}}{\beta+r}.
\]
The position generator is \(\mathcal LX=vS-rX\). For \(t>0\), writing \(Z(t)=\mathbb E[S_tX_0]\) and \(C_p(t)=\mathbb E[X_tX_0]\), the backward-generator equations become
\[
Z'(t)=-(\beta+r)Z(t),\qquad
C_p'(t)=-rC_p(t)+vZ(t).
\]
On the cloaking hypersurface the stationary spatial variance is \(C_p(0)=2D/r\). Solving this triangular initial-value problem gives the boxed covariance formula. In particular,
\[
C_{p_1}(t)-C_{p_2}(t)
=\frac{Dr(p_2-p_1)}{\beta\Lambda}
 e^{-rt}(1-e^{-\beta t})>0
\]
for \(p_1<p_2\) and \(t>0\). Also \(\pi_{\rm ball}>0\), so every intermittent process has strictly more positive covariance than Brownian resetting at every nonzero lag. Algebraic rearrangement of the covariance formula gives the single-lag reconstruction of \(p\).

For completeness, the same generator identities imply the variance at general parameters,
\[
\operatorname{Var}_p(X)=\frac2r
\left[D\pi_0+\frac{v^2}{\beta+r}\pi_{\rm ball}\right].
\]
Its derivative with respect to the mixing probability is
\[
\frac{\partial}{\partial p}\operatorname{Var}_p(X)
=\frac{2[DB-v^2]}{B\Lambda}.
\]
Thus the stationary *variance alone* identifies \(p\) if the other parameters are known and the cloaking condition fails; exactly at the cloaking condition, every stationary spatial moment loses its dependence on \(p\), while the lag covariance restores it.

## Verification

The accompanying `CHECK.py` verifies the Fourier-elimination identities and positivity-relevant factorizations symbolically, checks the stationary-moment and covariance ODE identities, and performs 225 independent comparisons against the uneliminated three-state Fourier linear system and a separate matrix-exponential evolution of the covariance variables. It was executed using Python with SymPy, NumPy and SciPy and all assertions passed. The analytic positivity and iff arguments above, rather than the finite numerical checks, establish the infinite-parameter conclusions.

To reproduce, execute `python CHECK.py` in the directory containing the file. No external datasets or source-paper files are required.

## Relationship to prior work

Flaquer-Galmés, Campos and Méndez [1] introduced precisely the diffusive/ballistic intermittent walker and computed its Fourier-Laplace propagators, stationary positional distributions under purely diffusive versus ballistic restart, mean-squared displacement, and first-arrival statistics. Their formulas supply the established resolvent machinery used here. They describe the reset-mode dependence generically, but do not provide the sharp static cloaking condition, the continuum of reset mixtures, or the stationary all-lag covariance-order and single-lag recovery theorem. This work does not claim a new process or a new basic renewal identity.

Evans and Majumdar [2] proved reset-orientation independence of the stationary marginal for a *different*, always-ballistic run-and-tumble process, obtaining a Laplace law over its full parameter range. That result is not the conditional diffusive-versus-ballistic mode equality proved here and does not supply the observed covariance fan. Kumar, Sadekar and Basu [3] studied resetting protocols for the distinct two-dimensional rotational-diffusion active Brownian model, including limiting marginal distributions; their claims also do not imply the three-mode sharp equivalence. Pure Brownian resetting and its Laplace stationary law are classical [4].

## Limitations

The equality is for a *one-time spatial marginal*, not equality of the stationary joint phase-position law, path law, hitting-time law, or full temporal statistics. In fact, the covariance formulas rigorously show path-law inequivalence. Recovery of \(p\) presumes exact knowledge of the other model parameters and ideal stationary covariance; neither finite-data statistical efficiency nor measurement noise robustness is established. The argument assumes symmetric ballistic directions, independent exponential switching and complete resetting of both position and mode. No extension to non-Poisson switching, correlated resets, higher-dimensional directional processes, spatially dependent rates, or absorbing targets is proved. Mathematical priority beyond the directly inspected papers remains subject to independent literature assessment; the stationary transform in [1] already gives the algebraic starting point.

## References

1. R. Flaquer-Galmés, D. Campos, and V. Méndez, *Intermittent random walks under stochastic resetting*, arXiv:2401.16849 (initially public 30 January 2024), *Phys. Rev. E* **109**, 034103 (2024), https://arxiv.org/abs/2401.16849. In particular Sections II, III.1–III.2 and Appendix A.
2. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, arXiv:1808.06450 (2018), https://arxiv.org/abs/1808.06450. In particular Sections 3.1 and 6.
3. V. Kumar, O. Sadekar, and U. Basu, *Active Brownian Motion in two dimensions under stochastic resetting*, arXiv:2008.03294 (2020), https://arxiv.org/abs/2008.03294. In particular Sections II and IV.2.
4. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, arXiv:1102.2704 (2011), https://arxiv.org/abs/1102.2704.
