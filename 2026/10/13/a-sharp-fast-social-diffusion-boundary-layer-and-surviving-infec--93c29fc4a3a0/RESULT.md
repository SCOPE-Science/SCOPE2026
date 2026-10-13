# A sharp fast-social-diffusion boundary layer and surviving infection in the Gaussian epidemic model

## Finding

For the four-dimensional Gaussian SfIR epidemic ODE in [1, Eq. (27)], increasing social diffusion to infinity compresses susceptible depletion into a fast initial layer but does **not** instantaneously remove infected people. More precisely, under the assumptions below, with \(K=S_0+I_0\), for every \(0<\delta<T<\infty\) the following convergence is uniform on \([\delta,T]\):

\[
S_D(t)\longrightarrow0,\qquad I_D(t)\longrightarrow K e^{-\gamma t},\qquad R_D(t)\longrightarrow1-K e^{-\gamma t},\qquad
\frac{\overline\beta_D(t)-\beta_0}{\sqrt D}\longrightarrow\sqrt{\frac{\beta_1}{K}}e^{\gamma t/2}.
\]

For every fixed \(t>0\), susceptibility has the sharp logarithmic extinction rate

\[
\lim_{D\to\infty}\frac{1}{\sqrt D}\log\frac{S_D(t)}{S_0}
=-\frac{2\sqrt{\beta_1K}}{\gamma}(1-e^{-\gamma t/2}).
\]

The complete initial layer is the coupled nonlinear limit displayed in the proof. In particular, fixed-time infection approaches a **positive** quantity, contrary to the proposed vanishing-infection scenario in [1, Section 5.1, open problems].

## Assumptions and scope

The population is normalized to one. Fix \(\gamma>0\), \(\beta_1>0\), \(\mu_0\ge0\), and \(\beta_0\ge0\). For each \(D>0\), consider the unique solution of

\[
\begin{aligned}
\dot S&=-(\beta_0+w)SI,\\
\dot I&=(\beta_0+w)SI-\gamma I,\\
\dot R&=\gamma I,\\
\dot w&=2D\beta_1-2\mu_0w-2Iw^2,
\end{aligned}
\]

with \(S(0)=S_0>0\), \(I(0)=I_0>0\), \(R(0)=R_0\ge0\), \(S_0+I_0+R_0=1\), \(w(0)=w_0\ge0\). All data except \(D\) are fixed as \(D\to\infty\), and \(w=\overline\beta-\beta_0\). This is exactly [1, Eq. (27)] with \(N=1\), not the underlying risk-density PDE. The parameter \(K=S_0+I_0=1-R_0\) is strictly positive. The limits hold on compact intervals strictly after time zero; no uniform convergence at time zero is claimed for \(S_D\) or \(I_D\).

## Proof

**1. Positivity, boundedness, and the scaled risk.** The nonnegative simplex is forward invariant, and \(S_D,I_D>0\) at every finite time. The sum \(S_D+I_D+R_D\) is one. The first and third equations make \(S_D\) decreasing and \(R_D\) increasing. On any fixed interval \([0,T]\),

\[
I_D(t)\ge I_0e^{-\gamma T}=:m_T>0,\qquad I_D(t)\le1.
\]

Set \(b_D=w_D/\sqrt D\). Then

\[
\dot b_D=\sqrt D(2\beta_1-2I_Db_D^2)-2\mu_0b_D.
\]

For \(D\ge1\), the scalar comparison at \(b_D=\sqrt{\beta_1/m_T}\) shows

\[
0\le b_D(t)\le B_T:=\max\{w_0,\sqrt{\beta_1/m_T}\},\qquad 0\le t\le T.
\]

In particular the solution exists globally. Also, since \(I_D\le1\), \(\sqrt D\ge1\), and \(b_D\ge0\),

\[
\dot b_D\ge\sqrt D\bigl(2\beta_1-2b_D^2-2\mu_0b_D\bigr).
\]

Let \(z' =2\beta_1-2z^2-2\mu_0z\), \(z(0)=0\). Comparison and \(b_D(0)=w_0/\sqrt D\ge0\) give \(b_D(t)\ge z(\sqrt D t)\). The function \(z\) is strictly increasing towards the positive root of its quadratic; put \(c=z(1)>0\). Then \(b_D(t)\ge c\) for \(t\ge D^{-1/2}\).

**2. The instantaneous susceptible layer.** For \(D^{-1/2}\le t\le T\), using \(\beta_0\ge0\) and the preceding lower bounds,

\[
S_D(t)\le S_0\exp[-m_Tc(\sqrt Dt-1)].
\]

Consequently \(S_D\to0\) uniformly on every \([\delta,T]\) with \(\delta>0\), and for each fixed \(t>0\).

**3. Exact removal convolution.** The first two equations imply \(\dot I_D+\gamma I_D=-\dot S_D\). Integration by parts gives the exact identity

\[
I_D(t)=K e^{-\gamma t}-S_D(t)+\gamma\int_0^t e^{-\gamma(t-u)}S_D(u)\,du.
\]

Since \(0\le S_D(u)\le S_0\), and since \(S_D(u)\to0\) for each \(u>0\), dominated convergence makes the integral vanish for every fixed \(t>0\). In fact, for any \(\eta>0\), the integral is uniformly bounded on \([0,T]\) by \(\gamma S_0\eta+\gamma T S_D(\eta)\); taking the diffusion limit followed by \(\eta\downarrow0\) proves uniform convergence of the integral. It follows that \(I_D(t)\to K e^{-\gamma t}\) uniformly on \([\delta,T]\). Conservation yields the corresponding limit for \(R_D\).

**4. Fast Riccati equilibrium away from time zero.** Write \(i_*(t)=K e^{-\gamma t}\) and \(h(t)=\sqrt{\beta_1/i_*(t)}\). On any \([\delta/2,T]\), the bounds from step 1 and the convergence from step 3 imply \(I_D\to i_*\) uniformly, with the latter bounded away from zero. For sufficiently small \(\varepsilon>0\), the vector field for \(b_D-h\) at the barriers \(b_D=h-\varepsilon\) and \(b_D=h+\varepsilon\) has respectively positive and negative sign of magnitude at least \(c_\varepsilon\sqrt D\) for large \(D\), because

\[
2\beta_1-2i_*(h-\varepsilon)^2>0,
\quad 2\beta_1-2i_*(h+\varepsilon)^2<0
\]

uniformly there. The terms \(-2\mu_0 b_D\) and \(-h'\) remain bounded. Since \(b_D\) is uniformly bounded, it enters this moving tube within \(O(D^{-1/2})\) after \(\delta/2\), and the barrier signs prevent exit. Thus \(b_D\to h\) uniformly on \([\delta,T]\) for each \(\delta>0\).

**5. Sharp logarithmic susceptible rate.** Since \(S_D>0\), integrate the exact logarithmic derivative:

\[
\frac1{\sqrt D}\log\frac{S_D(t)}{S_0}
=-\int_0^t b_D(u)I_D(u)\,du
-\frac{\beta_0}{\sqrt D}\int_0^t I_D(u)\,du.
\]

The products in the first integral are bounded by \(B_T\) and converge for every \(u>0\) to \(\sqrt{\beta_1i_*(u)}\). Dominated convergence gives

\[
-\int_0^t\sqrt{\beta_1K}\,e^{-\gamma u/2}\,du
=-\frac{2\sqrt{\beta_1K}}\gamma(1-e^{-\gamma t/2}),
\]

proving the exact coefficient.

**6. Initial layer and matching.** On \(\tau=\sqrt D t\), define \(s_D(\tau)=S_D(\tau/\sqrt D)\), \(i_D(\tau)=I_D(\tau/\sqrt D)\), and \(q_D(\tau)=b_D(\tau/\sqrt D)\). Their equations are

\[
\begin{aligned}
s_D'&=-q_Ds_Di_D-\frac{\beta_0}{\sqrt D}s_Di_D,\\
i_D'&=q_Ds_Di_D+\frac{\beta_0}{\sqrt D}s_Di_D-\frac{\gamma}{\sqrt D}i_D,\\
q_D'&=2\beta_1-2i_Dq_D^2-\frac{2\mu_0}{\sqrt D}q_D.
\end{aligned}
\]

Their initial data converge to \((S_0,I_0,0)\). Standard continuous dependence for locally Lipschitz ODEs, using the already established finite-time bounds on the scaled fields, proves compact-\(\tau\) convergence to the unique system

\[
\mathcal S'=-\mathcal B\mathcal S\mathcal I,
\qquad\mathcal I'=\mathcal B\mathcal S\mathcal I,
\qquad\mathcal B'=2\beta_1-2\mathcal I\mathcal B^2,
\qquad(\mathcal S,\mathcal I,\mathcal B)(0)=(S_0,I_0,0).
\]

Here \(\mathcal S+\mathcal I=K\), \(\mathcal I\ge I_0\), and \(\mathcal B\) has a positive lower bound after unit time by the same Riccati comparison. Thus \(\mathcal S(\tau)\to0\) exponentially, \(\mathcal I(\tau)\to K\). Scalar Riccati comparison about the limiting positive equilibrium then gives \(\mathcal B(\tau)\to\sqrt{\beta_1/K}\). This matches the positive-time outer solution at its right-hand endpoint. \(\square\)

## Verification

The independent algebraic checks are: direct differentiation of the removal convolution in step 3; substitution of \(b_D=w_D/\sqrt D\) in the risk equation; and direct integration of the log-susceptibility law in step 5. The accompanying `check_sfir_fastdiff.py` numerically integrates the exact original ODE with an implicit stiff solver at three increasing diffusion strengths and compares its fixed-time observables against the three proven limit formulas. These finite numerical checks are diagnostic only and do not replace the analytic comparison and compactness steps.

## Relationship to prior work

Berestycki, Desjardins, Weitz, and Oury [1, Section 4.3] derive precisely the four-dimensional Gaussian ODE analyzed here. Their Section 5.1 states the large-social-diffusion asymptotic for the ODE and PDE as an open problem and proposes zero infection at each fixed positive time. The present result solves the **ODE** case, supplies a fast-scale initial-layer mechanism and a sharp logarithmic coefficient, and shows that the proposed infection limit is not correct when the initial infectious seed is fixed and positive. Their large-\(t\) results, including the zero-drift case, do not imply this \(D\to\infty\) fixed-time limit. Dimarco, Perthame, Toscani, and Zanella [2] develop a distinct kinetic social-contact model with Gamma-type rather than this Gaussian risk closure; their fast-relaxation kinetic scaling does not entail the four-ODE diffusion asymptotic stated here.

## Limitations

No limit is established for the full Fokker--Planck PDE, for the higher-order Gaussian hierarchy, or for data depending on the diffusion strength. Uniformity fails through initial time for susceptible and infected fractions. The result takes the large-diffusion limit **before** any large-time limit; no joint two-parameter limit or uniform-in-infinite-time estimate is asserted. Existing general singular-perturbation principles could yield related or more abstract statements; novelty of the exact model-specific coefficient and fast-layer classification is judged against inspected sources, not guaranteed by absence from search results. Numerical simulations do not certify the infinite-diffusion limit.

## References

[1] H. Berestycki, B. Desjardins, J. S. Weitz, and J.-M. Oury, *Epidemic modeling with heterogeneity and social diffusion*, Journal of Mathematical Biology 86 (2023), article 60, DOI: 10.1007/s00285-022-01861-w. Complete article at https://link.springer.com/article/10.1007/s00285-022-01861-w, especially Eq. (27), Section 5.1 and Section 7.

[2] G. Dimarco, B. Perthame, G. Toscani, and M. Zanella, *Kinetic models for epidemic dynamics with social heterogeneity*, Journal of Mathematical Biology 83 (2021), article 4, DOI: 10.1007/s00285-021-01630-1. Complete article at https://link.springer.com/article/10.1007/s00285-021-01630-1, especially Sections 2--4.
