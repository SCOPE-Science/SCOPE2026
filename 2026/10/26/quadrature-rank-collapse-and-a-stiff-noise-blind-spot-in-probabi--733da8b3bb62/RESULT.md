# Quadrature-rank collapse and a stiff-noise blind spot in probabilistic exponential ODE filtering

## Finding

**Theorem (conditioned covariance of quadrature-discretized once-integrated Ornstein–Uhlenbeck filtering).** Fix a positive step \(h\), a damping rate \(a>0\), and a diffusion scale \(\kappa>0\). Use the once-integrated Ornstein–Uhlenbeck prior with linear rate \(L=-a\), a perfectly known initial state, and the noiseless EKL observation of the ODE residual. Approximate the process-noise covariance with any positive quadrature rule consisting of \(m\) distinct lag nodes \(0<s_1<\cdots<s_m<h\), weights \(w_i>0\), and \(\sum_i w_i=h\). Let \(P_m\) be the resulting one-step **filtered position variance**, and let \(P_{\mathrm{exact}}\) use the true process-noise covariance. Then

\[
P_m=\frac{\kappa^2}{a^2}\left(\sum_{i=1}^m w_i e^{-2a s_i}-\frac1h\left(\sum_{i=1}^m w_i e^{-a s_i}\right)^2\right),\qquad
P_{\mathrm{exact}}=\frac{\kappa^2}{a^2}\left(\frac{1-e^{-2ah}}{2a}-\frac{(1-e^{-ah})^2}{a^2h}\right)>0.
\]

In particular, \(P_1=0\) for **every** one-node rule, whereas \(P_m>0\) whenever \(m\ge2\). For the \(m=2\) Gauss–Legendre rule,

\[
P_2=\frac{\kappa^2h}{a^2}e^{-ah}\sinh^2\!\left(\frac{ah}{2\sqrt3}\right)>0.
\]

For every **fixed** \(m\ge2\) and \(h>0\), Gauss–Legendre's smallest lag node \(s_1>0\) and its weight \(w_1\) give the sharp stiff asymptotics, as \(a\to\infty\),

\[
P_m\sim\frac{\kappa^2}{a^2}w_1\left(1-\frac{w_1}{h}\right)e^{-2as_1},\qquad
P_{\mathrm{exact}}\sim\frac{\kappa^2}{2a^3},\qquad \frac{P_m}{P_{\mathrm{exact}}}\longrightarrow0.
\]

The one-node Gauss–Legendre rule is the midpoint rule. When the exact initial state is used, **all** subsequent mesh-point filtered covariances are zero under this rule, not just the first one, for any smooth semilinear right-hand side treated with EKL observations and the same positive step and linear rate.

The covariance collapse can coexist with a provably **nonzero point-estimate error**. For the forced linear initial-value problem \(y'(t)=-ay(t)+t\), \(y(0)=0\), the one-node quadrature-filtered mean at \(t=h\) and the exact solution satisfy

\[
\widehat y_1=\frac h a(1-e^{-ah/2}),\qquad y(h)=\frac h a-\frac{1-e^{-ah}}{a^2},\qquad
\widehat y_1-y(h)=\frac{e^{-ah/2}}{a^2}\bigl(2\sinh(ah/2)-ah\bigr)>0.
\]

The same filter using the **exact** process-noise covariance returns \(y(h)\) as its one-step mean on this forcing example. All preceding expressions extend continuously to \(a=0\), with \(P_{\mathrm{exact}}=\kappa^2h^3/12\), \(P_1=0\), and \(P_2=\kappa^2h^3/12\).

## Assumptions and scope

The prior state is \(Y=(Y^{(0)},Y^{(1)})^\top\), with drift and diffusion input

\[
A=\begin{pmatrix}0&1\\0&-a\end{pmatrix},\qquad B=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Its process-noise covariance over one step is \(\kappa^2Q(h)\), where \(Q(h)=\int_0^h e^{As}BB^\top e^{A^\top s}\,ds\). The EKL observation linearizes the noiseless condition \(Y^{(1)}-(-aY^{(0)}+N(Y^{(0)},t))=0\) with fixed row \(H=(a,1)\). The original correction is the exact Gaussian-conditioning operation, with positive innovation variance. We analyze the mathematical quadrature rule stated in Bosch–Hennig–Tronarp, not floating-point implementation details. The scale \(\kappa\) is fixed and strictly positive. The forced linear example has \(N(y,t)=t\) and deterministic initial derivative \(0\).

For the first-step formulas, the initial covariance is zero. The mesh-point collapse statement uses the same deterministic initial state and subsequent exact noiseless EKL corrections. It does **not** assert collapse for arbitrary positive initial covariance, noisy observations, other prior orders, or non-EKL observation linearizations.

## Proof

**Step 1: Fundamental impulse response.** Matrix exponentiation gives

\[
e^{As}B=v(s):=\begin{pmatrix}(1-e^{-as})/a\\e^{-as}\end{pmatrix},\qquad Hv(s)=1.
\]

The last identity holds exactly at every \(s\ge0\). Hence a quadrature prediction from a certain state has covariance \(\kappa^2Q_m=\kappa^2\sum_i w_iv(s_i)v(s_i)^\top\), with innovation variance \(\kappa^2HQ_mH^\top=\kappa^2h>0\). The Kalman update therefore yields

\[
\Sigma_m=\kappa^2\left(Q_m-\frac{Q_mH^\top HQ_m}{h}\right).
\]

Writing \(b_i=(1-e^{-as_i})/a\), its first diagonal entry is \(\kappa^2\{\sum_iw_ib_i^2-(\sum_iw_ib_i)^2/h\}\), which is the claimed weighted variance formula; the same argument with integrals gives \(P_{\mathrm{exact}}\).

**Step 2: Rank and positivity.** The weighted variance vanishes for one node. With at least two distinct nodes, the map \(s\mapsto(1-e^{-as})/a\) is strictly increasing, so the weighted variance is strictly positive. The exact integral variance is likewise positive for every \(h>0\). A Gauss–Legendre two-node rule has equal weights \(h/2\) and nodes \(h(1\pm1/\sqrt3)/2\); its variance is \(\kappa^2h(b_2-b_1)^2/4\). Substituting their exponential values gives the displayed hyperbolic-sine identity.

**Step 3: Loss of stiffness-uniform covariance accuracy.** In the exact integral formula, with \(h>0\) fixed and \(a\to\infty\), the leading term is \(\kappa^2/(2a^3)\). For a fixed positive Gauss–Legendre rule, \(0<s_1<s_2<\cdots<s_m<h\) and \(0<w_1<h\) if \(m\ge2\). In the weighted exponential variance, the smallest-node contributions to the two terms are respectively \(w_1e^{-2as_1}\) and \(w_1^2e^{-2as_1}/h\); every other term is exponentially smaller. This proves the stated asymptotic equivalent and the vanishing variance ratio. For \(m=1\), the variance is identically zero. The result is a **fixed quadrature-order** assertion; it does not cover rules whose node count grows with stiffness.

**Step 4: Collapse at every mesh point.** The initial covariance is zero. If the current filtered covariance is zero, the next prediction has covariance \(\kappa^2Q_1\), rank one, with the sole range direction \(v(h/2)\). Because \(Hv(h/2)=1\), conditioning on the exact scalar residual removes that range completely, so the next filtered covariance is zero. Induction proves the mesh-point statement. The nonlinear residual changes the conditional mean but not the rank argument because EKL fixes \(H=(a,1)\).

**Step 5: A demonstrably incorrect mean with zero covariance.** On \(y'=-ay+t\), \(y(0)=0\), the initial prior mean is \((0,0)^\top\), and the first predicted mean remains zero. The residual observed at \(t=h\) is \(-h\). The Kalman position gain is \(b(h/2)\) under one-node Gauss quadrature, yielding \(\widehat y_1=hb(h/2)\). The variation-of-constants formula gives the displayed exact value. Their difference is positive since \(2\sinh(z/2)>z\) for \(z>0\). With exact covariance, the gain instead equals \(h^{-1}\int_0^h b(s)\,ds\), whose product with the residual magnitude \(h\) is precisely the exact solution. Thus the deterministic posterior arises in the presence of genuine discretization error.

## Verification

`verify.py` (Python standard library) reconstructs the Gauss–Legendre nodes, process covariance, Gaussian conditioning, and exact forcing solution independently from the closed formulas. It checks quadrature polynomial exactness, the innovation identity, weighted-variance equivalence, positivity for multiple nodes, the two-node formula, the exact-vs-quadrature stiff limits, and zero conditional covariance over repeated one-node steps. Its 2,886 finite assertions pass for the indicated deterministic test grid. For \(a=h=\kappa=1\) it prints \(\widehat y_1=0.3934693402873666\), \(y(h)=0.36787944117144233\), \(P_{\mathrm{exact}}=0.032755957487965615\), \(P_1=0\), and \(P_2=0.0315177113279678\). The infinite and sharp asymptotic claims follow from the proof, not these finite checks.

## Relationship to prior work

Bosch, Hennig and Tronarp [1] introduce the once-integrated Ornstein–Uhlenbeck prior and a Gauss–Legendre square-root process-noise approximation with \(m=q\) nodes (Section 3.2, equations (24)–(25)). Their exact-covariance calculation in Appendix B proves the mean equivalence to an exponential trapezoidal rule for \(q=1\), using the unapproximated integral. The present theorem differentiates that exact calculation from the **one-node instantiation** of their stated quadrature prescription, and quantifies both the zero conditioned covariance and the stiff covariance underresolution for arbitrary fixed node counts. It does not relabel their integral identities as new.

Schmidt, Hennig, Nick and Tronarp [2] study rank-reduced Kalman filtering and acknowledge that limited-rank covariance approximations can cause overconfidence, but their dynamics, observation model, and approximation are different. No formula there was identified that implies the particular Gauss–Legendre filtered variance, its sharp fixed-node stiff asymptotics, or the forced-ODE numerical error. Tronarp et al. [3] supply the broader noiseless-ODE-observation filtering framework, not this quadrature result. The general weighted-variance identity follows standard Gaussian conditioning; the new assessed contribution is its concrete exact structural consequence for this prescribed IOUP quadrature construction.

## Limitations

The result is restricted to one-dimensional, once-integrated IOUP filtering with deterministic initialization, positive diffusion scaling, noiseless EKL conditioning, and the explicitly stated covariance quadrature. Its one-step covariance is a *numerical posterior variance*, not a frequentist squared-error estimator. It does not establish behavior for altered regularization, stochastic observation noise, higher-order priors, posterior calibration routines, or a particular software build. The quantitative stiff asymptotic requires the number of quadrature nodes to stay fixed. The conclusion is a mathematical warning about the stated process-noise discretization, not a claim that all probabilistic exponential solvers or all implementations have zero uncertainty. Publication priority may be affected by equivalent statements in Gaussian-quadrature or low-rank Kalman-filter literature not located in the searches.

## References

[1] N. Bosch, P. Hennig, F. Tronarp, *Probabilistic Exponential Integrators*, arXiv:2305.14978 (first posted 2023-05-24), Sections 2.3, 3.2–3.4 and Appendix B. https://arxiv.org/html/2305.14978v2

[2] J. Schmidt, P. Hennig, J. Nick, F. Tronarp, *The Rank-Reduced Kalman Filter: Approximate Dynamical-Low-Rank Filtering In High Dimensions*, arXiv:2306.07774 (2023), Sections 2–5 and appendices. https://arxiv.org/abs/2306.07774

[3] F. Tronarp, H. Kersting, S. Särkkä, P. Hennig, *Probabilistic Solutions to Ordinary Differential Equations as Non-Linear Bayesian Filtering: A New Perspective*, Statistics and Computing 29 (2019), arXiv:1810.03440. https://arxiv.org/abs/1810.03440
