# Exact covariance and diagnostic undercalibration for Gaussian exchangeable traces on flat spectra

## Finding
Let \(n\geq2\), \(1\leq k\leq n+1\), \(\lambda>0\), and let \(f\) be any operator-monotone function on the nonnegative real axis satisfying \(f(0)=0\) and \(c:=f(\lambda)>0\). Apply the **unnormalized Gaussian FLEXTRACE** estimator of Madhavan, Alexanderian, and Saibaba to \(A=\lambda I_n\), with \(k\) independent standard-normal probes. Let \(X_i\) denote its leave-one-out contributions and \(H=k^{-1}\sum_i X_i\).

For \(1\leq k\leq n\), set \(d=n-k+1\). Then
\[
\mathbb E H=nc,\qquad
\operatorname{Var}(H)=\frac{2c^2d(n+3)}{k(d+3)}.
\]
For distinct probe indices, whenever \(k\geq2\),
\[
\operatorname{Var}(X_i)=2c^2d,\qquad
\operatorname{Cov}(X_i,X_j)=\frac{2c^2d}{d+3},\qquad
\operatorname{Corr}(X_i,X_j)=\frac1{d+3}.
\]
For the natural leave-one-out dispersion diagnostic, previously used for exchangeable trace estimators,
\[
S^2:=\frac1{k(k-1)}\sum_{i=1}^k(X_i-H)^2\quad(2\leq k\leq n),
\]
one has the exact identity
\[
\mathbb E S^2=\frac{2c^2d(d+2)}{k(d+3)},\qquad
\frac{\mathbb E(H-nc)^2}{\mathbb E S^2}
=\frac{n+3}{n-k+3}.
\]
Thus multiplying \(S^2\) by \((n+3)/(n-k+3)\) gives an unbiased **mean-squared-error diagnostic on this specified flat-spectrum family**, not a universal calibration. At \(k=n\),
\[
\operatorname{Var}(H)=c^2\frac{n+3}{2n},\qquad
\mathbb E S^2=\frac{3c^2}{2n}.
\]
In contrast, at \(k=n+1\), every leave-one-out Nyström approximation is already exact and \(H=nc\) almost surely.

For any fixed \(0<\gamma<1\) along integers with \(k/n\to\gamma\), the variance approaches \(2c^2/\gamma\) while the ratio of true to reported expected squared error approaches \(1/(1-\gamma)\). For fixed integer \(s\geq0\) and \(k=n-s\),
\[
\operatorname{Var}(H)\to\frac{2c^2(s+1)}{s+4},\qquad
\mathbb E S^2\sim\frac{2c^2(s+1)(s+3)}{(s+4)n}.
\]
This is an exact near-rank-threshold calibration collapse for the unnormalized estimator. It does **not** imply a nonvanishing relative trace error, because the target \(nc\) grows with \(n\).

## Assumptions and scope
The input is the real matrix \(A=\lambda I_n\), and every entry of \(\Omega=[\omega_1,\ldots,\omega_k]\in\mathbb R^{n\times k}\) is independent \(N(0,1)\). All operations are in exact arithmetic. For an index set \(J\), define
\[
N_J=A\Omega_J(\Omega_J^{\mathsf T}A\Omega_J)^\dagger\Omega_J^{\mathsf T}A,
\]
where \(\dagger\) means the Moore–Penrose inverse, and let \(N=N_{\{1,\ldots,k\}}\), \(N_{-i}=N_{\{1,\ldots,k\}\setminus\{i\}}\). The investigated estimator is precisely
\[
X_i=\operatorname{tr}f(N_{-i})+
\omega_i^{\mathsf T}\bigl(f(N)-f(N_{-i})\bigr)\omega_i.
\]
The diagnostic \(S^2\) is defined only for \(k\geq2\). The theorem concerns this raw Gaussian version, not the residual-normalized version of earlier exchangeable estimators. Nothing is claimed for nonconstant spectra, nonsymmetric inputs, finite precision, arbitrary functions with \(f(0)\ne0\), or general trace-estimator error bars.

## Proof
**Projector reduction.** Since \(A=\lambda I_n\), every Nyström approximation is \(N_J=\lambda P_J\), where \(P_J\) is the orthogonal projector onto the span of the selected Gaussian columns. From \(f(0)=0\), \(f(\lambda P_J)=cP_J\). For \(k\leq n\), the columns are linearly independent almost surely. Put \(P_{-i}=P_{\{1,\ldots,k\}\setminus\{i\}}\) and
\[
R_i=\left\|(I-P_{-i})\omega_i\right\|_2^2.
\]
The rank-one difference \(P-P_{-i}\) projects onto the residual direction of \(\omega_i\). Therefore
\[
X_i=c\bigl[(k-1)+R_i\bigr].
\]
Conditional on all columns except \(i\), the complement of the other columns' span has dimension \(d=n-k+1\) and is independent of \(\omega_i\). Consequently \(R_i\sim\chi_d^2\), so \(\mathbb ER_i=d\), \(\operatorname{Var}R_i=2d\), and \(\mathbb EX_i=nc\).

**The nontrivial covariance.** Fix distinct \(i,j\), and condition on the other \(k-2\) Gaussian columns. Their orthogonal complement has dimension \(m=n-k+2=d+1\geq2\). The projections \(u,v\) of \(\omega_i,\omega_j\) into that complement are independent standard Gaussian vectors in \(\mathbb R^m\), and
\[
R_i=\|u\|_2^2\sin^2\theta,\qquad
R_j=\|v\|_2^2\sin^2\theta,
\]
where \(\theta\) is their mutual angle. The two radial squared norms are independent of the angular directions and have means \(m\). The squared cosine is \(\operatorname{Beta}(1/2,(m-1)/2)\). Hence
\[
\mathbb E\sin^4\theta=
\frac{(m-1)(m+1)}{m(m+2)},\quad
\mathbb E(R_iR_j)=\frac{m(m^2-1)}{m+2}.
\]
The conditional joint law is independent of the conditioned columns. Subtracting \((m-1)^2=d^2\) gives the exact pair covariance
\[
\operatorname{Cov}(R_i,R_j)=\frac{2(m-1)}{m+2}=\frac{2d}{d+3}.
\]
This argument includes \(k=2\), where no other columns are conditioned upon.

**Averaging and diagnostic.** Exchangeability now gives
\[
\operatorname{Var}H=\frac{c^2}{k^2}
\bigl(k\cdot2d+k(k-1)\cdot\tfrac{2d}{d+3}\bigr)
=\frac{2c^2d(n+3)}{k(d+3)}.
\]
The identity \(\mathbb E\sum_i(X_i-H)^2=(k-1)(\operatorname{Var}X_i-\operatorname{Cov}(X_i,X_j))\) gives
\[
\mathbb ES^2=\frac{\operatorname{Var}X_i-\operatorname{Cov}(X_i,X_j)}k
=\frac{2c^2d(d+2)}{k(d+3)}.
\]
The ratio and its asymptotic limits follow by algebra. For \(k=1\), the same projector reduction and chi-square law yield \(\operatorname{Var}H=2nc^2\), agreeing with the displayed variance formula; no empirical dispersion proxy is defined. For \(k=n+1\), deleting any column leaves \(n\) linearly independent Gaussian columns almost surely, so both \(N\) and every \(N_{-i}\) equal \(A\); therefore \(X_i=nc\) identically.

## Verification
Run `python verify.py` with Python 3.10+ and NumPy. It checks the rational beta-moment/covariance identities across \(3,240\) integer parameter pairs, directly compares projector/Nyström FLEXTRACE contributions against residual formulas in \(528\) independent finite matrix instances (including \(k=n+1\)), and performs \(750,000\) Gaussian pair-moment draws. Finite tests support the algebra; the proof above establishes statements for every admissible dimension, positive scale, and probe count. The script reports independent counters and fails on discrepancies.

## Relationship to prior work
Madhavan, Alexanderian, and Saibaba (arXiv:2603.05721v1, 5 March 2026) define the unnormalized FLEXTRACE estimator in their Algorithm 3.1, prove general bias and mean-squared-error bounds, and explain why sample exchangeability matters. Epperly, Tropp, and Webber (arXiv:2301.07825, Sections 1.2, 3.1, 5.3, 5.6) previously introduced XNysTrace, the corresponding leave-one-out dispersion diagnostic, a general covariance-based diagnostic relation, and a residual-normalization option. Those constructions and their general relations are **prior results**, not claimed as new.

The specific contribution here is an exact \(n,k\)-dependent evaluation of the joint Gaussian leave-one-out covariance **on the isotropic matrix-function model**, and therefore the full sharp calibration ratio, sampling-rank edge law, and finite-spectrum transition. The earlier general error identity does not itself evaluate the angular covariance on this family. The previously published normalization of residual vectors makes the flat-spectrum estimator exact, so the diagnostic problem shown here pertains to the explicitly unnormalized method.

## Limitations
This is a complete classification only for constant nonzero spectral level and Gaussian probes in exact arithmetic. At \(k=n\) the absolute mean-squared error stays bounded away from zero, but the squared *relative* error tends to zero since \(\operatorname{tr}f(A)=nc\). Existing residual normalization already removes this phenomenon on flat spectra; the result motivates that choice rather than claiming a new universal correction. The distinction between the mean of \(S^2\) and any particular realized \(S^2\) is essential: no samplewise or tail guarantee is proved. Literature uniqueness is not established; exact versions of the angular moment calculation may occur in other contexts.

## References
- M. Madhavan, A. Alexanderian, A. K. Saibaba, *FlexTrace: Exchangeable Randomized Trace Estimation for Matrix Functions*, arXiv:2603.05721v1 (first posted 2026-03-05), especially Algorithm 3.1 and Theorems 3.3–3.5. https://arxiv.org/abs/2603.05721
- E. N. Epperly, J. A. Tropp, R. J. Webber, *XTrace: Making the most of every sample in stochastic trace estimation*, arXiv:2301.07825 (first posted 2023-01-19); published in SIAM J. Matrix Anal. Appl. 45 (2024), 1–23. Sections 2.2–2.3, 3.1, 5.3, and 5.6. https://arxiv.org/abs/2301.07825
