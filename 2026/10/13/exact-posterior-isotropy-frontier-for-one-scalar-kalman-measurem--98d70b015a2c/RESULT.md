# Exact posterior-isotropy frontier for one scalar Kalman measurement

## Finding
Let
\[
P=P^{\mathsf T}\succ0
\]
be a two-dimensional prior covariance with distinct eigenvalues
\[
L>\mu>0.
\]
Take one scalar linear Gaussian measurement
\[
y=h^{\mathsf T}x+\varepsilon,
\qquad
\|h\|_2=1,
\qquad
\operatorname{Var}(\varepsilon)=r>0.
\]
The posterior covariance is
\[
P_h^+
=
\left(P^{-1}+r^{-1}hh^{\mathsf T}\right)^{-1}.
\]

For every fixed \(r\), the posterior spectral condition number is minimized exactly by measuring along the largest-variance prior eigendirection. If
\[
Pu_L=Lu_L,
\qquad
\|u_L\|_2=1,
\]
then
\[
\boxed{h_*=\pm u_L.}
\]

Put
\[
\kappa=\frac{L}{\mu},
\qquad
\eta=\frac{r}{\mu},
\qquad
q=\frac{\kappa\eta}{\kappa+\eta}.
\]
The exact optimum is
\[
\boxed{
\min_{\|h\|_2=1}\kappa_2(P_h^+)
=
\max\!\left\{q,\frac1q\right\}.
}
\]

There is a unique finite noise level at which one scalar measurement makes the posterior exactly isotropic:
\[
\boxed{
r_*=\frac{L\mu}{L-\mu}.
}
\]
At this noise level,
\[
P_{h_*}^+=\mu I.
\]

The condition-number response is therefore nonmonotone in measurement quality. Decreasing \(r\) from infinity down to \(r_*\) improves posterior isotropy. Decreasing \(r\) further makes the posterior increasingly anisotropic, even though the covariance itself continues to decrease in the Loewner order. The exact threshold at which the optimally oriented posterior becomes more ill-conditioned than the prior is
\[
\boxed{
r<\frac{L\mu^2}{L^2-\mu^2}.
}
\]

For
\[
P=\operatorname{diag}(4,1),
\]
the isotropy noise is
\[
r_*=\frac43.
\]
At that value the optimal posterior is \(I\). With the stronger measurement
\[
r=\frac14,
\]
the optimal posterior is instead
\[
P^+=\operatorname{diag}\!\left(\frac4{17},1\right),
\]
so its condition number is
\[
\frac{17}{4}>4,
\]
even though both its trace and determinant are smaller than those of the prior.

## Assumptions and scope
The state is two-dimensional and the prior covariance is real symmetric positive definite with two distinct eigenvalues. The measurement is scalar, linear, and has independent Gaussian noise of positive variance. The measurement vector is normalized in Euclidean norm; changing its magnitude is equivalent to rescaling the noise variance.

The result concerns the condition number of the posterior covariance, which measures anisotropy of the confidence ellipsoid. It is not a claim that a more accurate measurement worsens estimation accuracy. For fixed direction, lowering the noise variance always decreases the posterior covariance in the Loewner order. The finding is precisely that anisotropy and total uncertainty can move in opposite directions.

No dynamic prediction step is included. The theorem describes one Kalman measurement update, or equivalently one linear-Gaussian Bayesian conditioning step.

## Proof
Because inversion preserves the spectral condition number of a positive definite matrix, minimizing
\[
\kappa_2(P_h^+)
\]
is equivalent to minimizing the condition number of the posterior information matrix
\[
S_h=P^{-1}+r^{-1}hh^{\mathsf T}.
\]

For every unit vector \(h\),
\[
\operatorname{tr}S_h
=
\operatorname{tr}P^{-1}+\frac1r,
\]
so the trace is independent of measurement direction.

For a positive two-dimensional matrix with eigenvalues
\[
0<\lambda_-\le\lambda_+,
\]
write
\[
T=\lambda_-+\lambda_+,
\qquad
D=\lambda_-\lambda_+.
\]
At fixed \(T\),
\[
\frac{\lambda_+}{\lambda_-}
=
\frac{T+\sqrt{T^2-4D}}
{T-\sqrt{T^2-4D}}
\]
is strictly decreasing in \(D\). Hence minimizing the condition number of \(S_h\) is equivalent to maximizing its determinant.

The matrix determinant lemma gives
\[
\det S_h
=
\det(P^{-1})
\left(1+\frac{h^{\mathsf T}Ph}{r}\right).
\]
The Rayleigh quotient is maximized exactly at
\[
h=\pm u_L,
\]
because the largest eigenvalue \(L\) is simple. This proves the optimal-direction statement.

In the eigenbasis of \(P\), use \(h=u_L\). Then
\[
P=\operatorname{diag}(L,\mu)
\]
and
\[
P_{h}^+
=
\operatorname{diag}\!\left(
\frac{Lr}{L+r},
\mu
\right).
\]
After dividing the first eigenvalue by \(\mu\), its ratio to the second is
\[
q
=
\frac{Lr}{\mu(L+r)}
=
\frac{\kappa\eta}{\kappa+\eta}.
\]
Therefore
\[
\kappa_2(P_h^+)
=
\max\!\left\{q,\frac1q\right\}.
\]

The function \(q(\eta)\) is strictly increasing from zero to \(\kappa\). Thus the condition-number envelope has a unique minimum when
\[
q=1.
\]
Solving gives
\[
\eta_*=\frac{\kappa}{\kappa-1}
\]
and hence
\[
r_*=\mu\eta_*
=
\frac{L\mu}{L-\mu}.
\]
At that value the two posterior eigenvalues are both \(\mu\).

On the strong-measurement side, the posterior is more ill-conditioned than the prior exactly when
\[
\frac1q>\kappa.
\]
Solving this strict inequality yields
\[
r<\frac{L\mu^2}{L^2-\mu^2}.
\]
Finally, as \(r\downarrow0\), the measured-direction posterior variance tends to zero while the orthogonal variance remains \(\mu\), so the condition number diverges. In one dimension there is only one covariance eigenvalue, so dimension two is minimal for this anisotropy reversal.

## Verification
The embedded `verify.py` checks the exact rational example
\[
P=\operatorname{diag}(4,1).
\]
It verifies that
\[
r_*=\frac43
\]
produces posterior covariance \(I\), and that
\[
r=\frac14
\]
produces
\[
P^+=\operatorname{diag}\!\left(\frac4{17},1\right)
\]
with condition number \(17/4\).

The checker also verifies the exact prior-worsening threshold
\[
\frac{L\mu^2}{L^2-\mu^2}=\frac4{15}
\]
for this example, so \(r=1/4\) lies strictly in the overmeasurement regime.

Finite replay is corroborative only. The all-parameter direction optimum, isotropy frontier, and reversal threshold are proved analytically.

## Relationship to prior work
Optimal sensor design for Kalman filtering is classical. Oshman's discrete-time sensor-selection strategy uses spectral factors of the error covariance and favors a measurement subsystem that supplies information along the state-space direction associated with the largest current estimation error. That conceptual preference for the largest-error direction is treated as prior work here.

Belabbas gives a full geometric treatment of optimal Kalman sensor design in continuous time. The inspected full text optimizes trace-based mean-square error under a fixed sensing norm and characterizes extremal sensor subspaces through Riccati geometry. It does not formulate the one-update posterior condition-number objective used here.

Tzoumas, Jadbabaie, and Pappas study finite-horizon Kalman sensor placement under minimum-mean-square-error and log-determinant objectives. Those objectives quantify total error or confidence-ellipsoid volume rather than its anisotropy.

Wolkowicz studies condition-number-optimal symmetric rank-one updates in a quasi-Newton secant setting. This is relevant matrix-analysis background because a Kalman information update is also rank one. The inspected material does not justify claiming the largest-eigenvector direction itself as new. The contribution asserted here is the complete fixed-noise two-dimensional Kalman posterior law, including the unique exact isotropy noise and the sharp regime in which a more accurate scalar measurement makes the optimally oriented posterior more ill-conditioned than the prior.

## Limitations
The complete formula is two-dimensional. In higher dimensions a single rank-one information update cannot generally make the full posterior isotropic, and fixed-trace determinant maximization no longer by itself characterizes condition-number minimization.

The measurement vector is allowed to vary continuously over the unit circle. Discrete sensor libraries can prevent attainment of the principal prior direction.

The condition number is a scale-free anisotropy criterion. Trace, determinant, maximum eigenvalue, and application-specific weighted risks can prefer different designs or interpret stronger measurements differently.

The 1974 paper “Optimum measurements for estimation” is a plausible older source for closely related sensor-direction calculations; its full body was not available through the inspected route and remains an originality risk. The rank-one conditioning literature is another residual risk for an algebraically equivalent matrix statement outside Kalman terminology.

## References
1. Y. Oshman, “Optimal Sensor Selection Strategy for Discrete-Time State Estimators,” IEEE Transactions on Aerospace and Electronic Systems 30 (1994), 307–314. DOI 10.1109/7.272256.
2. M.-A. Belabbas, “Geometric methods for optimal sensor design,” arXiv:1503.05968v1, submitted 2015-03-19.
3. V. Tzoumas, A. Jadbabaie, and G. J. Pappas, “Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms,” arXiv:1509.08146v1, submitted 2015-09-27.
4. H. Wolkowicz, “Measures for Symmetric Rank-One Updates,” Mathematics of Operations Research 19 (1994), 815–830. DOI 10.1287/moor.19.4.815.
5. E. F. Costa and A. Astolfi, “Characterization of Exponential Divergence of the Kalman Filter for Time-Varying Systems,” SIAM Journal on Control and Optimization 48 (2009), 2917–2944. DOI 10.1137/080717055.
