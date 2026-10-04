# Sharp weak-identification experiment for exponential-tilt response shift
## Finding
Consider the separable response-shift component of the synthetic regression model in Choi (2026). Let \(V\sim\mathrm{Unif}[-1,1]\), let \(Z=\operatorname{sign}(Y)\in\{-1,+1\}\), and write
\[
\pi_\eta(v)=\Pr(Z=+1\mid V=v)=\operatorname{logit}^{-1}(d_\eta+3\eta v),
\]
where \(d_\eta\) is chosen so that \(\mathbb E\pi_\eta(V)=p\in(0,1)\) is fixed. Tilt responses by \(e^{bZ}\). If \(Q^V_{b,\eta}\) is the resulting target marginal of \(V\) and
\[
q_b=\frac{pe^b}{(1-p)e^{-b}+pe^b},
\]
then, relative to the uniform law \(\mu\),
\[
\frac{dQ^V_{b,\eta}}{d\mu}(v)
=1+\frac{(q_b-p)(\pi_\eta(v)-p)}{p(1-p)}.
\]
This identity is exact.

As \(\eta\downarrow0\), for fixed \(b_0,b_1\),
\[
D_{\mathrm{KL}}(Q^V_{b_0,\eta}\|Q^V_{b_1,\eta})
=\frac32(q_{b_0}-q_{b_1})^2\eta^2+O(\eta^3).
\]
The one-observation Fisher information for \(b\) is
\[
I_b(\eta)=12q_b^2(1-q_b)^2\eta^2+O(\eta^3),
\]
and the target mean obeys
\[
\mathbb E_{Q^V_{b,\eta}}V=(q_b-p)\eta+O(\eta^2).
\]

For fixed \(b_0\ne b_1\), let \(m\) independent target inputs be observed and let \(\eta_m\downarrow0\). Put \(\Delta_q=q_{b_0}-q_{b_1}\). If \(m\eta_m^2\to\lambda\in(0,\infty)\), then under \(b_0\)
\[
\log\frac{d(Q^V_{b_0,\eta_m})^{\otimes m}}{d(Q^V_{b_1,\eta_m})^{\otimes m}}
\Rightarrow
N\!\left(\frac32\Delta_q^2\lambda,3\Delta_q^2\lambda\right),
\]
with the mean negated under \(b_1\). Therefore
\[
d_{\mathrm{TV}}\!\left((Q^V_{b_0,\eta_m})^{\otimes m},(Q^V_{b_1,\eta_m})^{\otimes m}\right)
\longrightarrow
2\Phi\!\left(\frac{|\Delta_q|\sqrt{3\lambda}}{2}\right)-1.
\]
In particular, \(m\eta_m^2\to0\) gives asymptotic indistinguishability, whereas \(m\eta_m^2\to\infty\) permits consistent discrimination by the sample mean of \(V\). Thus \(m\eta^2\) is the sharp weak-identification information scale for the response tilt in this model.

## Assumptions and scope
The source law is treated as known. The theorem isolates the response coefficient \(b\); the independent input-only tilt in Choi's separable family factors out of the \(V\)-marginal and does not affect the calculation. The source mode mass \(p\) is held fixed as \(\eta\) varies exactly as in the paper's sensitivity design. The asymptotics concern \(\eta\downarrow0\), fixed distinct \(b_0,b_1\), and an increasing target-input sample size \(m\).

The theorem does not analyze source-model estimation, regularization, numerical optimization, conformal coverage, or the larger interaction family that Choi shows can be nonidentified. It is a local statistical-experiment calculation for the identifiable separable response-shift direction.

## Proof
Let
\[
Z_b=(1-p)e^{-b}+pe^b.
\]
Conditioning on \(V=v\), the response tilt changes the target \(V\)-density relative to \(\mu\) by
\[
r_{b,\eta}(v)=\frac{(1-\pi_\eta(v))e^{-b}+\pi_\eta(v)e^b}{Z_b}.
\]
Since \(q_b=pe^b/Z_b\), also \(e^b/Z_b=q_b/p\) and \(e^{-b}/Z_b=(1-q_b)/(1-p)\). Algebra gives
\[
r_{b,\eta}(v)=1+(q_b-p)s_\eta(v),
\qquad
s_\eta(v)=\frac{\pi_\eta(v)-p}{p(1-p)}.
\]
Because \(\mathbb E_\mu\pi_\eta(V)=p\), one has \(\mathbb E_\mu s_\eta(V)=0\) exactly.

Set \(d_0=\operatorname{logit}(p)\). The defining equation for \(d_\eta\) has strictly positive derivative in \(d\), so the implicit-function theorem gives a smooth local solution. Symmetry of \(V\) gives \(d_\eta=d_{-\eta}\), hence \(d'_0=0\). Uniform Taylor expansion of the logistic function therefore yields
\[
\pi_\eta(v)-p=3p(1-p)\eta v+O(\eta^2),
\qquad
s_\eta(v)=3\eta v+O(\eta^2)
\]
uniformly for \(v\in[-1,1]\). Thus
\[
\mathbb E_\mu s_\eta(V)^2=3\eta^2+O(\eta^3),
\qquad
\mathbb E_\mu[V s_\eta(V)]=\eta+O(\eta^2).
\]
The second identity immediately gives the asserted target mean.

For \(c_j=q_{b_j}-p\), expand
\[
(1+c_0s)\{\log(1+c_0s)-\log(1+c_1s)\}
=(c_0-c_1)s+\frac12(c_0-c_1)^2s^2+O(s^3).
\]
The linear term integrates to zero because \(\mathbb E_\mu s_\eta=0\). Since \(s_\eta=O(\eta)\) uniformly, the KL expansion follows.

For Fisher information, \(q'_b=2q_b(1-q_b)\) and
\[
\partial_b\log r_{b,\eta}(v)
=\frac{q'_b s_\eta(v)}{1+(q_b-p)s_\eta(v)}.
\]
Integrating its square under density \(r_{b,\eta}\,d\mu\), and using the second-moment expansion above, gives
\[
I_b(\eta)=q_b'^2\{3\eta^2+O(\eta^3)\}
=12q_b^2(1-q_b)^2\eta^2+O(\eta^3).
\]

For the triangular experiment, the one-observation log likelihood ratio is
\[
\ell_\eta(V)=\log\frac{1+c_0s_\eta(V)}{1+c_1s_\eta(V)}.
\]
Under \(Q^V_{b_0,\eta}\), the preceding expansion gives
\[
\mathbb E\ell_\eta=\frac32\Delta_q^2\eta^2+O(\eta^3),
\qquad
\operatorname{Var}(\ell_\eta)=3\Delta_q^2\eta^2+O(\eta^3).
\]
Moreover \(|\ell_\eta-\mathbb E\ell_\eta|=O(\eta)\) uniformly, so the Lindeberg condition is automatic. If \(m\eta_m^2\to\lambda\in(0,\infty)\), the triangular-array central limit theorem yields the stated Gaussian limit. Under \(b_1\), the mean is the negative reverse KL with the same leading variance. The Neyman--Pearson threshold at log likelihood ratio zero then gives limiting sum of the two simple-hypothesis errors
\[
2\Phi\!\left(-\frac{|\Delta_q|\sqrt{3\lambda}}{2}\right),
\]
which is equivalent to the stated total-variation limit.

If \(m\eta_m^2\to0\), product KL tends to zero and Pinsker's inequality gives total variation tending to zero. If \(m\eta_m^2\to\infty\), the two target means differ by \(\Delta_q\eta_m+O(\eta_m^2)\); since \(V\in[-1,1]\), a midpoint sample-mean test is consistent by Hoeffding's inequality.

## Verification
The standalone script `verify.py` numerically solves the fixed-mode-mass equation for \(d_\eta\) using the paper's source value
\[
p=\frac{\log(1+e)-\log(1+e^{-5})}{6},
\]
and deterministic quadrature. For decreasing \(\eta\), it checks convergence of the scaled KL divergence, Fisher information, and target mean to the analytic constants. The script returned `VERIFY_OK` from the packaged path. These numerical checks support the coefficient algebra; they are not used as a substitute for the asymptotic proof.

## Relationship to prior work
Choi (2026) proves that the separable response coefficient is identified for every \(\eta>0\) in this regression design, becomes unidentified at \(\eta=0\), and reports severe finite-sample deterioration as \(\eta\) decreases. The paper explicitly states that it does not derive a general regression estimation rate. The result here quantifies that paper's concrete weak-signal ladder: the information per target input is quadratic in \(\eta\), with explicit KL and Fisher constants, and the full fixed-alternative testing experiment has a nontrivial Gaussian limit exactly on the \(m\eta^2\) scale.

Garg et al. (2020) give fixed-model label-shift estimation bounds controlled by likelihood curvature/minimum eigenvalues and discuss loss of information under coarse calibration. Those results establish a broad connection between weak curvature and estimation error, but do not give this triangular weak-signal experiment, its \(m\eta^2\) phase boundary, or the constants above for Choi's logistic gate. Lee, Ma, and Zhao (2023/2024) develop large-sample semiparametric theory under label shift; their fixed-identification theory is relevant context, but the checked abstract and accessible records do not state the present vanishing-signal experiment.

## Limitations
The result concerns a deliberately isolated, correctly specified binary-mode subexperiment with known source law. It does not establish a rate for Choi's implemented ExTRA estimator, whose source gate and normalizer are themselves estimated, and it does not convert the information boundary into a conformal-coverage theorem. General weak-identification and label-shift theory could contain equivalent consequences under different notation; targeted searches and the primary comparisons below did not locate this exact statement, so that remains the principal originality risk.

## References
1. S. Choi, “Conformal Prediction under Exponential-Tilt Joint Shift,” arXiv:2609.30886v1, first public 2026-09-25.
2. S. Garg, Y. Wu, S. Balakrishnan, and Z. C. Lipton, “A Unified View of Label Shift Estimation,” NeurIPS 2020, arXiv:2003.07554.
3. S.-H. Lee, Y. Ma, and J. Zhao, “Doubly Flexible Estimation under Label Shift,” arXiv:2307.04250; Journal of the American Statistical Association.
