# Gaussian spreading–localization trichotomy for scaled-angular Brownian swimmers

## Finding

A planar particle can move at constant positive speed without a trap and nevertheless converge almost surely to a finite random location. This occurs at a sharp threshold in the growth of its rotational diffusivity. The same model has an isotropic Gaussian fluctuation law on **both** sides of the threshold, but the Gaussian variable describes the growing position below it and the shrinking residual displacement above it.

Let \(v>0\), \(\kappa>0\), \(\beta>0\), and define the swimmer by the stochastic equations in the next section. With \(\mathcal N_2(0,cI_2)\) denoting the centered isotropic planar Gaussian distribution of coordinate variance \(c\), the complete limit-law classification is:

\[
\begin{array}{ll}
0<\beta<2:\quad & T^{-(1-\beta/2)}X_T\ \Longrightarrow\ 
\mathcal N_2\!\left(0,\dfrac{v^2}{\kappa\beta(2-\beta)}I_2\right),\\[5pt]
\beta=2:\quad &(\log T)^{-1/2}X_T\ \Longrightarrow\
\mathcal N_2\!\left(0,\dfrac{v^2}{2\kappa}I_2\right),\\[5pt]
\beta>2:\quad &X_T\longrightarrow X_\infty\quad\text{a.s. and in }L^2,\\
& T^{\beta/2-1}(X_\infty-X_T)\ \Longrightarrow\
\mathcal N_2\!\left(0,\dfrac{v^2}{\kappa\beta(\beta-2)}I_2\right).
\end{array}
\]

For \(\beta\le2\), \(\lvert X_T\rvert\to\infty\) **in probability**, hence there is no finite endpoint in probability. This does not assert pathwise monotone escape. For \(\beta>2\), the exact finite terminal mean-square distance is

\[
\mathbb E\lvert X_\infty\rvert^2
=\frac{2v^2}{\beta^2\kappa^{2/\beta}}
\frac{\Gamma(2/\beta)\Gamma(1/\beta)\Gamma(1-2/\beta)}{\Gamma(1-1/\beta)}.
\]

The exact second-moment identity from which this expression follows was previously available; the distinctive claim here is the **almost-sure threshold and the explicit Gaussian limit laws**, including the isotropic Gaussian approach to a nontrivial random endpoint above the threshold.

## Assumptions and scope

Let \(W\) be standard one-dimensional Brownian motion. The initial angle \(\Theta_0\) may be deterministic or independent of \(W\), including uniform on \([0,2\pi)\). Define

\[
\Theta_t=\Theta_0+\int_0^t\sqrt{2\kappa\beta s^{\beta-1}}\,dW_s,
\qquad
X_t=v\int_0^t(\cos\Theta_s,\sin\Theta_s)\,ds\in\mathbb R^2.
\]

All parameters \(v,\kappa,\beta\) are fixed as \(T\to\infty\). There is no translational thermal Brownian noise, stochastic resetting, confining potential, or orientation–position feedback. The angular variance is \(2\kappa t^\beta\); the instantaneous rotational diffusivity is \(\kappa\beta t^{\beta-1}\). For every fixed \(\beta>0\), the angular SDE is well defined at time zero because its squared diffusion coefficient is locally integrable.

The Gaussian limits concern ordinary weak convergence of random vectors, not a finite-time Gaussian law or an assertion that the terminal position is Gaussian. The exact terminal second moment holds for every admissible initial angle because the angular-increment covariance is independent of that angle.

## Proof

**1. Exact covariance and the known second-moment identity.** Represent planar positions by the complex process \(Z_t=X_t^{(1)}+iX_t^{(2)}\), put \(U_t=e^{i\Theta_t}\), and write \(Z_t=v\int_0^t U_s\,ds\). Brownian independent increments give, for \(t\ge s\),

\[
\mathbb E(U_t\overline U_s)=\exp\{-\kappa(t^\beta-s^\beta)\}.
\]

Therefore

\[
M_\beta(T):=\mathbb E\lvert Z_T\rvert^2
=2v^2\int_0^T e^{-\kappa t^\beta}
\left(\int_0^t e^{\kappa s^\beta}\,ds\right)dt.
\tag{1}
\]

This is the exact mean-square formula given by the motivating work, written in its native normalization; it is **not** claimed as new. An endpoint Laplace estimate, or l'Hôpital's rule applied to the inner integral, yields

\[
e^{-\kappa t^\beta}\int_0^t e^{\kappa s^\beta}\,ds
\sim\frac{t^{1-\beta}}{\kappa\beta}.
\tag{2}
\]

Thus for \(0<\beta<2\),
\(M_\beta(T)\sim 2v^2T^{2-\beta}/[\kappa\beta(2-\beta)]\); at \(\beta=2\), \(M_2(T)\sim(v^2/\kappa)\log T\); and for \(\beta>2\),

\[
M_\beta(\infty)-M_\beta(T)
\sim\frac{2v^2}{\kappa\beta(\beta-2)}T^{2-\beta}.
\tag{3}
\]

For \(\beta>2\), substitute \(s=tq\) in (1), integrate \(t\in(0,\infty)\), then substitute \(z=q^\beta\). Tonelli's theorem applies because the integrand is nonnegative. The resulting beta integral converges exactly when \(\beta>2\) and gives the displayed Gamma-function formula. These moment consequences are already implied by (1); the distributional and almost-sure assertions require the additional arguments below.

**2. An exact martingale decomposition.** Itô's formula yields

\[
dU_t=-\kappa\beta t^{\beta-1}U_t\,dt
+i\sqrt{2\kappa\beta t^{\beta-1}}U_t\,dW_t.
\]

For \(t\ge1\), put \(f(t)=t^{1-\beta}/(\kappa\beta)\). Integration by parts gives the exact pathwise identity

\[
\begin{split}
v\int_1^T U_t\,dt={}&v f(1)U_1-v f(T)U_T
+v\int_1^T f'(t)U_t\,dt\\
&+iv\sqrt{\frac{2}{\kappa\beta}}
\int_1^T t^{(1-\beta)/2}U_t\,dW_t.
\end{split}
\tag{4}
\]

The first three terms on the right have absolute value at most \(C(1+T^{(1-\beta)_+})\), and therefore vanish after division by \(T^{1-\beta/2}\) for every \(0<\beta<2\), or by \(\sqrt{\log T}\) at \(\beta=2\). The finite initial integral \(v\int_0^1U_t\,dt\) also disappears under these normalizations.

When \(\beta>2\), \(f(T)\to0\) and \(\int_1^\infty\lvert f'(t)\rvert\,dt<\infty\). The last term in (4) is an \(L^2\)-bounded martingale because \(\int_1^\infty t^{1-\beta}dt<\infty\); it converges almost surely and in \(L^2\). The deterministic terms converge too. Hence \(Z_T\to Z_\infty\) almost surely and in \(L^2\). Subtracting (4) from its infinite-time limit gives

\[
Z_\infty-Z_T=iv\sqrt{\frac{2}{\kappa\beta}}
\int_T^\infty t^{(1-\beta)/2}U_t\,dW_t+R_T,
\qquad
\lvert R_T\rvert\le\frac{2v}{\kappa\beta}T^{1-\beta}.
\tag{5}
\]

In particular, \(T^{\beta/2-1}R_T\to0\) deterministically.

**3. An explicit isotropization estimate.** The real and imaginary parts of the martingale in (4) have instantaneous covariance matrix proportional to

\[
t^{1-\beta}
\begin{pmatrix}
\sin^2\Theta_t&-\sin\Theta_t\cos\Theta_t\\
-\sin\Theta_t\cos\Theta_t&\cos^2\Theta_t
\end{pmatrix}dt.
\]

All departures from half the identity are linear combinations of \(\cos(2\Theta_t)\) and \(\sin(2\Theta_t)\). Set \(u=t^\beta\) and \(p=2/\beta-2\). Then

\[
t^{1-\beta}dt=\frac1\beta u^pdu,
\qquad
\mathbb E e^{2i(\Theta_{u^{1/\beta}}-\Theta_{w^{1/\beta}})}
=e^{-4\kappa\lvert u-w\rvert}.
\]

Young's convolution inequality therefore gives, for any interval \(I\subset[1,\infty)\) on which the integrals exist,

\[
\mathbb E\left\lvert\int_Iu^p e^{2i\Theta_{u^{1/\beta}}}du\right\rvert^2
\le\frac1{2\kappa}\int_Iu^{2p}du.
\tag{6}
\]

For \(\beta<2\), \(p>-1\), so the ratio of the right side of (6) to \((\int_1^{T^\beta}u^pdu)^2\) tends to zero. This remains true at \(\beta=2\), where \(p=-1\) and the denominator grows as \((\log T)^2\) while the numerator stays bounded. For \(\beta>2\), \(p<-1\); taking \(I=[T^\beta,\infty)\), the same ratio is \(O(T^{-\beta})\). Consequently the appropriately normalized martingale quadratic-covariation matrix converges in probability to a scalar multiple of \(I_2\) in all three regimes.

**4. Gaussian limits and sharp threshold.** For \(0<\beta<2\), the normalized martingale in (4) has limiting coordinate quadratic variation

\[
\frac{v^2}{\kappa\beta}
T^{\beta-2}\int_1^Tt^{1-\beta}dt
\longrightarrow\frac{v^2}{\kappa\beta(2-\beta)}.
\]

At \(\beta=2\), divide by \(\log T\) instead, obtaining \(v^2/(2\kappa)\). The continuous-martingale central limit theorem applies, because the jumps vanish identically and step 3 supplies deterministic limiting quadratic covariations. The negligible remainder in step 2 proves the first two displayed vector limits.

For \(\beta>2\), normalize the martingale tail in (5) by \(T^{\beta/2-1}\). Its limiting coordinate quadratic variation is

\[
\frac{v^2}{\kappa\beta}T^{\beta-2}
\int_T^\infty t^{1-\beta}dt
=\frac{v^2}{\kappa\beta(\beta-2)}.
\]

For rigor at the infinite upper endpoint, first integrate over \([T,LT]\) with fixed \(L>1\), apply the same continuous-martingale limit theorem and the estimate (6), then let \(L\to\infty\). The omitted tail has uniformly bounded normalized mean-square size proportional to \(L^{2-\beta}\). Equation (5) supplies the negligible remainder. This proves the last Gaussian limit.

Finally, when \(\beta\le2\), the unscaled normalization diverges to infinity. Since the normalized position converges to a nondegenerate Gaussian with no atom at the origin, for every fixed \(R>0\), \(\mathbb P(\lvert X_T\rvert\le R)\to0\). Therefore there is no finite position limit in probability. Together with almost-sure convergence above \(\beta=2\), this proves the sharp classification.

## Verification

The accompanying `verify.py` uses independent numerical integration of the stable second-moment differential equation, direct quadrature of its time-kernel, and numerical quadrature of the Gamma/Beta terminal-moment identity. It also tests finite-time angular increment covariances and asymptotic moment normalizations. Run:

```bash
python verify.py
```

The reproduced execution passed 64 finite numerical and exact-identity diagnostics. The infinite-time convergence and Gaussian statements are proved in the argument above, **not** inferred from those finite tests.

## Relationship to prior work

Sevilla, Valdés-Gómez, and Torres-Carbajal (2024) introduced the precise time-inhomogeneous angular diffusion model, derived its exact mean-square integral (their equations (20)–(21)), and studied anomalous transport and fourth-order statistics primarily at \(0<\beta<2\). In particular, (1), the MSD power law below the critical exponent, and the Gamma/Beta evaluation of the same known integral are not separately claimed as original. The present theorem addresses pathwise convergence and Gaussian normalized laws of the full position and terminal residual, which cannot be deduced from second moments alone.

Gómez-Solano and Sevilla (2020) considered **fractional** angular Brownian motion with stationary-increment long-memory noise; it has different angular increments and long-time diffusive motion. Fernandez-Rodriguez and coauthors (2019) achieved active-particle localization through spatial feedback control of rotational diffusivity; that mechanism is different from the unconfined, deterministic power-law acceleration and Gaussian endpoint-tail limit here.

## Limitations

This analysis concerns the free, constant-speed, purely propulsion-driven model. Any nonzero independent translational Brownian diffusivity destroys almost-sure spatial convergence, and resetting or confinement changes the result. The asymptotic Gaussian law at \(\beta>2\) is for the **residual** \(X_\infty-X_T\); it does not assert that \(X_\infty\) itself is Gaussian. The ordinary model-specific conclusion may be subsumed by a sufficiently general unlocated theorem on additive functionals of time-inhomogeneous Markov processes; publication priority has not been independently established. No empirical estimation guarantee or independent scientific audit is asserted.

## References

1. F. J. Sevilla, A. Valdés-Gómez, and A. Torres-Carbajal, *Anomalous diffusion of scaled Brownian tracers*, arXiv:2401.03127v1 (first public preprint 2024-01-06); *Physical Review E* 110, 014113 (2024). https://arxiv.org/html/2401.03127 ; https://doi.org/10.1103/PhysRevE.110.014113
2. J. R. Gómez-Solano and F. J. Sevilla, *Active particles with fractional rotational Brownian motion*, arXiv:2001.04015 (2020). https://arxiv.org/abs/2001.04015
3. M. A. Fernandez-Rodriguez and collaborators, *Feedback-Controlled Active Brownian Colloids with Space-Dependent Rotational Dynamics*, arXiv:1911.02291 (2019). https://arxiv.org/abs/1911.02291
