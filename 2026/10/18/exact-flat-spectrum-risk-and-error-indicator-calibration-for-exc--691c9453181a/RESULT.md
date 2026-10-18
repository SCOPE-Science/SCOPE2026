# Exact flat-spectrum risk and error-indicator calibration for exchangeable Nyström traces

## Finding

Let \(n\ge r\ge1\), let \(P\in\mathbb R^{n\times n}\) be an orthogonal projector of rank \(r\), and let \(A=\lambda P\) for \(\lambda>0\). Let \(f:[0,\infty)\to\mathbb R\) be a finite-valued scalar spectral function satisfying \(f(0)=0\), and put \(c=f(\lambda)\ne0\). The operator-monotone functions covered by FlexTrace, including square root and logarithm, are special cases.

Draw independent \(\omega_1,\ldots,\omega_k\sim N(0,I_n)\). For a set \(J\subseteq\{1,\ldots,k\}\), write \(\Omega_J\) for its probe matrix and define the exact-arithmetic Nyström approximation
\[
B_J=A\Omega_J(\Omega_J^{\mathsf T}A\Omega_J)^\dagger(A\Omega_J)^{\mathsf T},\qquad B_\varnothing=0.
\]
Set \(B=B_{\{1,\ldots,k\}}\), \(B_{-i}=B_{\{1,\ldots,k\}\setminus\{i\}}\), and define the **unnormalized Gaussian FlexTrace estimator** (Algorithm 3.1 in the source paper)
\[
H_i=\operatorname{tr}f(B_{-i})+\omega_i^{\mathsf T}[f(B)-f(B_{-i})]\omega_i,
\qquad H=\frac1k\sum_{i=1}^k H_i.
\]
When \(f(x)=x\), this is also the Gaussian XNysTrace estimator, up to the obvious scalar factor on the flat spectrum. The conclusions below concern the displayed unnormalized estimator, **not** the separately recommended normalized-probe version.

**Theorem (complete flat-spectrum second-moment law).** If \(1\le k\le r\) and \(d=r-k+1\), each \(H_i\) has the law \(c(k-1+\chi_d^2)\). For \(i\ne j\) (when \(k\ge2\)),
\[
\operatorname{Var}(H_i)=2dc^2,\qquad
\operatorname{Cov}(H_i,H_j)=\frac{2d}{d+3}c^2,
\qquad \operatorname{Corr}(H_i,H_j)=\frac1{d+3}.
\]
In particular, the estimator is unbiased and its exact mean-square error is
\[
\boxed{\mathbb EH=rc,\qquad
\mathbb E(H-rc)^2=\frac{2d(r+3)}{k(d+3)}c^2.}
\]
For \(k\ge2\), the conventional leave-one-out squared-error indicator
\[
S=\frac1{k(k-1)}\sum_{i=1}^k(H_i-H)^2
\]
satisfies
\[
\boxed{\mathbb ES=\frac{2d(d+2)}{k(d+3)}c^2,
\qquad \frac{\mathbb ES}{\mathbb E(H-rc)^2}=\frac{r-k+3}{r+3}.}
\]
Thus \(\frac{r+3}{r-k+3}S\) is an unbiased squared-risk estimator **within this flat-spectrum model**.

At the rank-saturation budget \(k=r\),
\[
\boxed{\mathbb E(H-rc)^2=\frac{r+3}{2r}c^2,\qquad
\mathbb ES=\frac{3}{2r}c^2\quad(r\ge2).}
\]
Consequently, as \(r\to\infty\) with \(k=r\), the actual absolute squared risk approaches \(c^2/2\), whereas the mean reported squared error tends to zero. For **every** \(k\ge r+1\), one instead has \(H=rc\) almost surely, and \(S=0\) when defined. The full Nyström approximation is already exact at \(k=r\), yet one extra probe removes the leave-one-out randomness altogether.

## Assumptions and scope

All formulas concern exact real arithmetic, independent standard *unnormalized* Gaussian columns, the exact Moore–Penrose pseudoinverse, an orthogonal projector of arbitrary orientation, and a constant nonzero eigenvalue on its image. There is no restriction on the ambient nullspace dimension \(n-r\). The theorem holds simultaneously for every fixed integer \(n\ge r\ge1\) and \(k\ge1\); the posterior indicator is defined only when \(k\ge2\). The formulas depend on \(f\) only through \(f(0)=0\) and the scalar \(c=f(\lambda)\); for the motivating method one may take any nonzero operator-monotone function in its stated class.

## Proof

**Step 1: Exact Nyström geometry.** Write \(W_J=P\Omega_J\) and let \(\Pi_J\) be the Euclidean projector onto its column span. As \(A=\lambda P\), the pseudoinverse formula gives \(B_J=\lambda\Pi_J\), including for a rank-deficient sketch. Thus \(f(B_J)=c\Pi_J\). Every set of \(j\) Gaussian columns has projected rank \(\min(j,r)\) almost surely. If \(k\ge r+1\), both \(\Pi_{\{1,\ldots,k\}}\) and every \(\Pi_{-i}\) equal \(P\); each \(H_i=rc\). Henceforth \(k\le r\).

**Step 2: The individual law.** Each \(\Pi_{-i}\) has rank \(k-1\). The difference \(\Pi-\Pi_{-i}\) projects onto the single new direction obtained by projecting \(P\omega_i\) orthogonally away from the other projected probes. Therefore
\[
\omega_i^{\mathsf T}(\Pi-\Pi_{-i})\omega_i
=\|(P-\Pi_{-i})\omega_i\|_2^2=:X_i.
\]
Conditionally on the other columns, \(P-\Pi_{-i}\) is a deterministic projector of rank \(d=r-k+1\), independent of \(\omega_i\). Hence \(X_i\sim\chi_d^2\) and \(H_i=c[(k-1)+X_i]\). It follows that \(\mathbb EX_i=d\), \(\operatorname{Var}(X_i)=2d\), and \(\mathbb EH=c[(k-1)+d]=rc\).

**Step 3: Exact cross-covariance.** Fix \(i\ne j\) and condition on the remaining \(k-2\) Gaussian columns. In the orthogonal complement of their projected span *inside* \(\operatorname{range}(P)\), the dimension is \(q=r-k+2=d+1\). The two distinguished residual columns are independent standard Gaussian vectors \(a,b\in\mathbb R^q\). The two residual energies are exactly
\[
X_i=\|a\|_2^2\left(1-\frac{(a^{\mathsf T}b)^2}{\|a\|_2^2\|b\|_2^2}\right),\qquad
X_j=\|b\|_2^2\left(1-\frac{(a^{\mathsf T}b)^2}{\|a\|_2^2\|b\|_2^2}\right).
\]
The squared cosine \(U=(a^{\mathsf T}b)^2/(\|a\|_2^2\|b\|_2^2)\) has the \(\operatorname{Beta}(1/2,(q-1)/2)\) distribution. By rotational symmetry, or by elementary moments of the uniform sphere, \(\mathbb EU=1/q\), \(\mathbb EU^2=3/[q(q+2)]\). The independent squared Gaussian radii are \(\chi_q^2\), each of mean \(q\), and they are independent of \(U\). Thus
\[
\mathbb EX_iX_j=q^2\left(1-\frac2q+\frac3{q(q+2)}\right)
=\frac{(d+1)d(d+2)}{d+3}.
\]
Subtracting \(\mathbb EX_i\mathbb EX_j=d^2\) gives \(\operatorname{Cov}(X_i,X_j)=2d/(d+3)\), independent of the conditioned columns. This proves the claimed pair covariance and correlation.

**Step 4: Risk and error-indicator calibration.** Exchangeability, the individual variance, and the pair covariance give
\[
\operatorname{Var}(H)=\frac{c^2}{k}\left[2d+(k-1)\frac{2d}{d+3}\right]
=\frac{2d(k+d+2)}{k(d+3)}c^2
=\frac{2d(r+3)}{k(d+3)}c^2.
\]
For \(k\ge2\), expand the centered sample variance and apply the same covariance identities:
\[
\mathbb ES=\frac{c^2}{k}\left[2d-\frac{2d}{d+3}\right]
=\frac{2d(d+2)}{k(d+3)}c^2.
\]
The ratio and the rank-saturation and one-extra-probe consequences follow by substitution. This proves all assertions.

## Verification

Run `python3 check_flat_trace.py` from the directory containing this document. The included standalone program uses exact rational arithmetic to reconstruct Gaussian angular-moment identities, all stated second-moment identities over a finite rectangular grid of ranks and budgets, and numerous rational orthogonal-projector instances. Separately, seeded direct Gaussian-vector tests recompute the leave-one-out residuals and compare measured risks and posterior indicators to the formulas. A successful execution reports **13,545 checks**. These computations are consistency checks, not substitutes for Step 3's all-dimension analytic argument.

## Relationship to prior work

Madhavan, Alexanderian and Saibaba's 2026 *FlexTrace* introduces precisely the function-Nyström leave-one-out estimator in Algorithm 3.1 and provides general bias/MSE bounds, but the inspected estimator and theory statements do not furnish this flat-spectrum pair-covariance and risk-calibration formula. Epperly, Tropp and Webber introduced Gaussian XNysTrace and the squared-error indicator in their 2023 preprint/2024 journal paper; their Proposition 2 expresses the indicator-to-risk ratio using the (unspecified) correlation of basic estimates. The calculation \(\operatorname{Corr}(H_i,H_j)=1/(d+3)\), and the resulting explicit calibration and rank-saturation laws, are the additional statements here. Their recommended normalized-probe variant must not be confused with the unnormalized Gaussian estimator: for a full-rank identity multiple in its natural dimension, normalizing the held-out residual eliminates the displayed Gaussian-length fluctuations. Hallman's 2025 *Two Variations on the XTrace Algorithm* studies rotation averaging and a larger deflation space for XTrace rather than these exact Nyström covariance and calibration identities.

## Limitations

This is an exact flat-spectrum benchmark, **not** a worst-case theorem for arbitrary spectral distributions. It makes no claim of novelty for Nyström approximation, leave-one-out trace estimation, Gaussian spherical moments, the general covariance decomposition, or posterior-error normalization. Its formulas do not apply unchanged to spherical/renormalized probes, Rademacher probes, finite-precision algebra, or nonconstant nonzero spectra. A corrected indicator is unbiased for squared risk in expectation; it need not concentrate around the error in any single run. Unindexed earlier specializations of the exchangeable trace variance remain a bibliographic risk.

## References

1. M. Madhavan, A. Alexanderian and A. K. Saibaba, *FlexTrace: Exchangeable Randomized Trace Estimation for Matrix Functions*, arXiv:2603.05721v1 (public 2026-03-05), especially Algorithm 3.1 and Theorems 3.2–3.5. https://arxiv.org/abs/2603.05721
2. E. N. Epperly, J. A. Tropp and R. J. Webber, *XTrace: Making the most of every sample in stochastic trace estimation*, arXiv:2301.07825 (2023); SIAM Journal on Matrix Analysis and Applications **45** (2024), 1–23, especially equations (8), (9), (16), Proposition 2 and the Gaussian XNysTrace variance argument. https://arxiv.org/abs/2301.07825
3. E. Hallman, *Two Variations on the XTrace Algorithm*, arXiv:2512.02316v1 (public 2025-12-02), especially Section 1 and its description of normalized XTrace. https://arxiv.org/abs/2512.02316
