# True-orbit KRR accuracy does not control coupled closure rollout
## Finding
The KRR closure estimate in Theorem 2.1 of Habbershaw--Harlim--Liang requires a stability hypothesis that is not supplied by true-orbit approximation accuracy. The paper defines the learned unresolved map as \(\widetilde{{\Phi}}_y:\mathbb R^{{d_x+d_y}}\to\mathbb R^{{d_y}}\), but assumption (8) is written using powers \((\widetilde{{\Phi}}_y)^n(z_0)\). Those powers are not composable when \(d_x>0\). More importantly, if one repairs (8) in the natural teacher-forced sense by asking only that the KRR predictor be accurate on the true sampled orbit, the conclusion of Theorem 2.1 does not follow.

There is an explicit family using the paper's standard Gaussian kernel. Let \(h=1/m\), \(T=1\), and consider
\[
x'=y,\qquad y'=0,\qquad (x(0),y(0))=(0,1).
\]
The true sampled states are \(z_j=(jh,1)\), \(0\le j\le m\). Train scalar KRR on these centers with constant target \(1\), Gaussian kernel
\[
k_h(z,z')=\exp\!\left(-rac{\|z-z'\|^2}{h^{10}}ight),
\]
which is equation (4) with \(4\varepsilon_h=h^{10}\), and ridge parameter \(\lambda_h=h^5\). If \(A_h=(K_h+\lambda_h I)^{-1}{\bf 1}\), then at every true center
\[
\widetilde{\Phi}_{y,h}(z_j)=1-\lambda_h(A_h)_j=1-h^5+O(h^{10})+o(h^r)
\]
for every fixed \(r>0\). Hence the maximum teacher-forced nodal error is \(O(h^5)\).

Nevertheless, the first coupled prediction is \(\widehat y_1=1-h^5+o(h^5)\). With linear interpolation of \(y\) and the trapezoidal/Heun update for \(x'=y\),
\[
\widehat x_1=rac h2(1+\widehat y_1)=h-O(h^6).
\]
Thus \(\widehat z_1=(\widehat x_1,\widehat y_1)\) lies a distance \(h^5(1+o(1))\) from the true center \(z_1\). At precisely that distance the self-kernel satisfies
\[
k_h(\widehat z_1,z_1)\longrightarrow e^{-1},
\]
while all kernels against the other centers are super-polynomially small. Since \((A_h)_1\to1\), the next coupled prediction obeys
\[
\widehat y_2\longrightarrow e^{-1}.
\]
The resolved error after two steps is therefore
\[
2h-\widehat x_2
=rac h2igl(3-2\widehat y_1-\widehat y_2igr)
\sim rac{1-e^{-1}}2h.
\]
For interpolation degree \(p=1\) and a globally second-order resolved update \(q=2\), the right side of the claimed estimate under the teacher-forced repair is only \(O(h^5+h^2+h^2)=O(h^2)\). No constant independent of \(h\) can make that rate valid.

## Assumptions and scope
The finding concerns the theoretical statement and proof of Theorem 2.1 in arXiv:2610.02564v1. It does not claim that the paper's rollout-aware hyperparameter selection fails empirically, and it does not claim that Theorem 2.1 is false under a stronger hypothesis that directly bounds the actual coupled values \(\widehat y_n\). Indeed, that stronger hypothesis supplies exactly the estimate needed in equation (29).

The counterexample uses the standard Gaussian RBF kernel explicitly allowed and tested by the source, a globally Lipschitz two-dimensional ODE, degree-one stable interpolation, and a second-order endpoint method for the resolved equation. The bandwidth and ridge parameter tend to zero while the number of true-orbit centers tends to infinity.

## Proof
Write \(K_h=I+E_h\). Distinct centers are separated by at least \(h\), so every off-diagonal kernel entry is at most \(e^{-h^{-8}}\). Hence
\[
\|E_h\|_\infty\le 2m e^{-h^{-8}}=o(h^r)
\]
for every fixed \(r>0\). A Neumann-series estimate for \((K_h+h^5I)^{-1}\) gives, uniformly in \(j\),
\[
(A_h)_j=1+O(h^5)+o(h^r).
\]
Because \((K_h+h^5I)A_h={\bf1}\), one has exactly
\[
\widetilde{\Phi}_{y,h}(z_j)=(K_hA_h)_j=1-h^5(A_h)_j,
\]
which proves the \(O(h^5)\) teacher-forced error.

Set \(d_h=1-\widehat y_1=h^5(A_h)_0=h^5(1+o(1))\). The first resolved step gives \(\widehat x_1=h-hd_h/2\), so
\[
\|\widehat z_1-z_1\|^2=d_h^2\left(1+rac{h^2}{4}ight)=h^{10}(1+o(1)).
\]
Therefore the kernel contribution of \(z_1\) tends to \(e^{-1}\). For \(j\ne1\), the horizontal distance from \(\widehat z_1\) to \(z_j\) is at least \(h/2\) for all sufficiently small \(h\), so those kernel terms are bounded by \(e^{-1/(4h^8)}\). Since the coefficients stay uniformly bounded and \((A_h)_1\to1\), it follows that \(\widehat y_2\to e^{-1}\).

Finally, the endpoint/trapezoidal update is
\[
\widehat x_2=rac h2(1+\widehat y_1)+rac h2(\widehat y_1+\widehat y_2).
\]
Subtracting from \(x_2=2h\) yields the displayed asymptotic \((1-e^{-1})h/2\). This contradicts an \(O(h^2)\) rate under teacher-forced KRR error \(O(h^5)\).

## Verification
The argument uses exact kernel identities and asymptotic bounds, not a finite numerical experiment. The crucial checks are: center separation \(h\); super-polynomial decay of off-center Gaussian kernels; the exact KRR identity \(K_hA_h={\bf1}-h^5A_h\); the first-step displacement \(d_h\sim h^5\); the resulting self-kernel limit \(e^{-1}\); and the exact two-step resolved-error formula.

The source's own types were checked: equation (3) defines \(\widetilde{\Phi}_y\) with input dimension \(d_x+d_y\) and output dimension \(d_y\), equation (7) evaluates it on the coupled predicted state, equation (8) writes iterates of that non-self-map, and Appendix B uses (8) to bound the actual coupled nodal errors in equation (29).

## Relationship to prior work
Habbershaw--Harlim--Liang use rollout-aware validation in practice, so the paper is already empirically sensitive to autonomous rollout behavior. Song--Huang--Harlim likewise select KRR hyperparameters using errors from iterated predictions rather than only one-step loss. Those procedures do not supply the missing theorem hypothesis.

Li--Wan study the general phenomenon that small one-step model error can diverge under autonomous rollout and obtain rollout bounds only with domain-wide incremental-stability or Lipschitz control. That broader stability theory motivates the needed repair but does not state the source-specific type defect, the failed implication from teacher-forced KRR accuracy to equation (29), or the explicit Gaussian-KRR construction above.

## Limitations
The finding does not rule out a corrected theorem in which \(\delta\) is defined to be the maximum actual coupled-rollout error \(\max_n\|\widehat y_n-y_n\|\). Nor does it determine the weakest possible stability condition. A uniform Lipschitz bound for \(\widetilde{\Phi}_y\) on a tube around the true and predicted trajectories is one sufficient route, but sharper localized conditions may exist.

The counterexample addresses the standard RBF kernel. It does not assert that diffusion-map kernels necessarily exhibit the same narrow-band instability for the source's validated hyperparameters.

## References
1. E. Habbershaw, J. Harlim, S. Liang, *Learning Closure of Dynamical Systems with Kernel Ridge Regression*, arXiv:2610.02564v1, 2026.
2. Q. Li, M. Wan, *Stability-Regularized Residual Neural ODEs: From Rollout-Error Contraction Diagnostics to a Train-Time Method for Robust Long-Horizon Forecasting*, Mathematics 14(15):2850, 2026, DOI:10.3390/math14152850.
3. J. Song, D. Huang, J. Harlim, *Learning solution operator of dynamical systems with diffusion maps kernel ridge regression*, arXiv:2512.17203v2, 2025.
