# A universal mixed-normal error law for shared-shift stratified control variates

## Finding

Consider the one-dimensional, order-two stratified-control-variate quadrature rule defined below. Its **single interpolation shift, shared by every stratum**, changes the asymptotic error distribution even though each stratum has independent residual samples. For every real-valued \(f\in C^2([0,1])\) with
\[
J_f:=\int_0^1\bigl(f''(x)\bigr)^2\,dx>0,
\]
let \(Q_m^{\mathrm{sh}}(f)\) denote the shared-shift rule on \(m\) uniform cells. With \(\Xi\sim\operatorname{Uniform}(0,1)\) and an independent standard normal \(G\),
\[
\bigl(\Xi,m^{5/2}(Q_m^{\mathrm{sh}}(f)-If)\bigr)
\ \Longrightarrow\
\left(\Xi,\sqrt{\frac{J_f V(\Xi)}8}\,G\right),
\quad
V(t):=\frac1{180}+\frac{(t-1/2)^2}{12},\qquad If:=\int_0^1f(x)\,dx.
\]
This limit is **not Gaussian**. Its variance is \(J_f/640\), and after division by its unconditional standard deviation its fourth moment is the universal constant
\[
\frac{3\,\mathbb E[V(\Xi)^2]}{\mathbb E[V(\Xi)]^2}
=\frac{101}{27}>3.
\]
The conclusion is independent of the particular nonaffine \(C^2\) integrand after variance normalization.

Let \(Q_m^{\mathrm{ind}}(f)\) be the otherwise identical rule with a fresh independent interpolation shift in each cell. **For every finite \(m\)** the shared- and independent-shift rules have exactly the same expectation and variance, yet
\[
m^{5/2}(Q_m^{\mathrm{ind}}(f)-If)
\ \Longrightarrow\ N(0,J_f/640),
\]
so the independent-shift version has an ordinary Gaussian limit.

Finally, the residual data already used by the shared-shift rule give an exactly conditionally unbiased variance estimator
\[
\widehat s_m^2:=\frac1{4m^2}\sum_{i=0}^{m-1}
\bigl(R_{i,m}(U_{i1})-R_{i,m}(U_{i2})\bigr)^2,
\qquad
\mathbb E[\widehat s_m^2\mid\Xi]
=\operatorname{Var}(Q_m^{\mathrm{sh}}(f)\mid\Xi).
\]
It obeys \(m^5\widehat s_m^2-J_fV(\Xi)/8\to0\) in probability and restores the Gaussian pivot:
\[
\frac{Q_m^{\mathrm{sh}}(f)-If}{\widehat s_m}\ \Longrightarrow\ N(0,1).
\]
The ratio may be defined arbitrarily when \(\widehat s_m=0\), an event with probability tending to zero.

## Assumptions and scope

For each integer \(m\ge1\), partition \([0,1]\) into \(C_{i,m}=[i/m,(i+1)/m]\), \(i=0,\ldots,m-1\). Draw one \(\Xi\sim\operatorname{Uniform}(0,1)\). In **every** cell use the same local interpolation locations
\[
a(\Xi)=\frac\Xi2,\qquad b(\Xi)=\frac{1+\Xi}{2}.
\]
Let \(g_{i,m}\) be the affine function interpolating \(f\) at \((i+a(\Xi))/m\) and \((i+b(\Xi))/m\); define the local residual on \([0,1]\) by
\[
R_{i,m}(u):=f\left(\frac{i+u}{m}\right)-g_{i,m}\left(\frac{i+u}{m}\right).
\]
Conditionally on \(\Xi\), draw all \(U_{ij}\), \(i=0,\ldots,m-1\), \(j=1,2\), mutually independently from \(\operatorname{Uniform}(0,1)\). Set
\[
Q_m^{\mathrm{sh}}(f)=\frac1m\sum_{i=0}^{m-1}
\left[\int_0^1g_{i,m}\left(\frac{i+u}{m}\right)du
+\frac{R_{i,m}(U_{i1})+R_{i,m}(U_{i2})}{2}\right].
\]
There are two interpolation evaluations and two residual evaluations per cell, hence \(4m\) evaluations of \(f\). For \(Q_m^{\mathrm{ind}}\), replace the common \(\Xi\) by independent uniform shifts \(\Xi_i\) in the interpolation nodes of the respective cells; keep all residual samples independent. No dependence between independent runs or nested meshes is required for the distributional limits. The test functions are \(C^2\), and \(J_f>0\) excludes the affine functions that the rule integrates exactly.

This is the order-two, one-dimensional specialization of the randomized-interpolation construction in Kunsch's stratified-control-variate framework, with the valid interpolation template \(\{0,1\}\). It does **not** describe its deterministic-interpolation variant.

## Proof

**Step 1: Uniform local interpolation expansion.** Set
\[
\phi_t(u):=(u-t/2)\bigl(u-(1+t)/2\bigr).
\]
Taylor expansion with the uniformly continuous second derivative of \(f\), followed by subtraction of the interpolating affine polynomial, yields
\[
R_{i,m}(u)=\frac{f''(i/m)}{2m^2}\phi_\Xi(u)+o(m^{-2})
\]
uniformly over every cell index \(i\), \(u\in[0,1]\), and \(\Xi\in[0,1]\). The uniformity follows because the interpolation nodes are always separated by exactly \(1/2\) in local coordinates. For \(f(x)=x^2\), this equality is exact without the remainder.

**Step 2: The persistent random variance.** If \(U\) is uniform on \([0,1]\), constants in \(\phi_t(U)=U^2-(t+1/2)U+t(1+t)/4\) do not affect its variance. Direct integration using \(\operatorname{Var}(U)=1/12\), \(\operatorname{Var}(U^2)=4/45\), and \(\operatorname{Cov}(U,U^2)=1/12\) gives
\[
\operatorname{Var}(\phi_t(U))=V(t)=\frac1{180}+\frac{(t-1/2)^2}{12}>0.
\]
Moreover,
\[
\mathbb E[V(\Xi)]=\frac1{80},\qquad
\mathbb E[V(\Xi)^2]=\frac{101}{518400}.
\]
Since the residual estimate in every cell is conditionally unbiased,
\[
\mathbb E[Q_m^{\mathrm{sh}}(f)\mid\Xi]=If,
\quad
\operatorname{Var}(Q_m^{\mathrm{sh}}(f)\mid\Xi)
=\frac1{2m^2}\sum_i\operatorname{Var}_U(R_{i,m}(U)).
\]
The local expansion and the Riemann sum for \((f'')^2\) imply, uniformly in the shift,
\[
m^5\operatorname{Var}(Q_m^{\mathrm{sh}}(f)\mid\Xi)
\longrightarrow\frac{J_fV(\Xi)}8.
\]

**Step 3: Conditional central limit theorem and fourth moment.** Given the shift, the centered contributions of the individual residual samples are independent. In the \(m^{5/2}\)-normalized sum, each is uniformly \(O(m^{-1/2})\); the variance converges to the strictly positive quantity in Step 2. Lindeberg's triangular-array central limit theorem applies conditionally for every fixed shift. Bounded conditional characteristic functions and integration over the uniform shift then give the stated joint and unconditional mixed-normal limit. The same uniform bounds imply convergence of fourth moments, by expanding fourth powers of sums of conditionally independent centered terms; the fourth-cumulant remainder is \(O(1/m)\). Thus the limiting standardized fourth moment equals \(3\mathbb E[V^2]/(\mathbb E V)^2=101/27\). The mixture cannot be Gaussian, since a nondegenerate centered Gaussian has standardized fourth moment \(3\).

**Step 4: Equal variance but different limits.** A cell's conditional quadrature error has mean zero for every interpolation shift. Hence shared-shift errors from distinct cells have zero covariance even unconditionally. Both randomization schemes give the same one-cell marginal distribution, so summing their variances proves exact equality of the finite-\(m\) variances. For independent shifts the individual cell errors are fully independent, and the same bounded triangular-array argument gives a Gaussian limit whose variance is \(J_f\mathbb E[V]/8=J_f/640\). In the common-shift scheme that is only the average conditional variance, not the variance of a single conditional Gaussian limit.

**Step 5: Feasible conditional studentization.** For two independent residual values from one cell,
\[
\mathbb E[(R_{i,m}(U_{i1})-R_{i,m}(U_{i2}))^2\mid\Xi]
=2\operatorname{Var}_U(R_{i,m}(U)).
\]
This gives the displayed exact conditional unbiasedness identity. The local Taylor expansion shows
\[
m^5\widehat s_m^2
=\frac1{16m}\sum_i\bigl(f''(i/m)\bigr)^2
\bigl(\phi_\Xi(U_{i1})-\phi_\Xi(U_{i2})\bigr)^2+o_{\mathbb P}(1).
\]
Its conditional expectation tends to \(J_fV(\Xi)/8\) and its conditional variance tends to zero at rate \(O(1/m)\), using boundedness of \(f''\) and \(\phi_t\). Conditional Slutsky and integration over shifts yield the standard-normal studentized limit.

## Verification

Run `python verify.py` with dependencies in `requirements.txt`. The checker symbolically reconstructs the interpolation residual, the exact \(V(t)\), its first two shift moments, the sharp \(101/27\) fourth-moment coefficient, the quadratic benchmark's exact conditional variance for all positive cell counts, the paired-residual variance identity, and polynomial consistency checks. It also performs independent finite-size sanity checks. The machine checks are finite or symbolic; the general \(C^2\) convergence theorem is proved by the uniform Taylor expansion and conditional triangular-array arguments above.

As an interpretable confidence-level calculation, an ordinary Gaussian interval based on the *unconditional* asymptotic variance has limiting coverage
\[
\int_0^1\left[2\Phi\left(\frac{\Phi^{-1}(0.975)}{\sqrt{80V(t)}}\right)-1\right]dt
\approx0.9446368,
\]
not \(0.95\). By contrast, the conditionally studentized interval is asymptotically calibrated at every fixed continuous normal quantile. The numerical integral is supplementary, not part of the proof of non-Gaussianity.

## Relationship to prior work

Kunsch (arXiv:2309.09059v1, September 16, 2023), Section 2, equation (19), defines stratified control variates and expressly shares the interpolation shift across all subcubes; Remark 2.8 allows the randomized interpolation version even for smooth inputs. Its main results establish probabilistic error rates and confidence-width bounds, not the exact conditional limiting variance, mixed-normal distribution, universal fourth moment, or same-variance contrast between shared and independent cell shifts.

Chopin and Gerber (arXiv:2210.01554v1, October 4, 2022), Section 2.7 and Theorem 2, prove a Gaussian central limit theorem for a *different* high-order cubically stratified estimator with locally computed derivative-control information. Their normal limit is not an implication about the shared random interpolation phase in the present rule.

Nakayama and Tuffin (DOI:10.1145/3643847, author-hosted preprint, pages 1–3 and Sections 2–4) discuss failures of naive normal calibration for randomized quasi-Monte Carlo with fixed numbers of randomizations, and derive conditions for Gaussian confidence intervals in that framework. This supports the importance of the phenomenon, but their randomized lattice/digital schemes and CLT conditions do not specify the present interpolation-based rule or imply its explicit universal mixing law and within-cell variance estimator. Gaussian scale mixtures and conditional CLT arguments themselves are classical, not claimed as novel.

## Limitations

The result is exact for the stated one-dimensional, order-two randomized-interpolation algorithm with one common shift and two independent residual evaluations per cell. It is not a claim about Kunsch's deterministic-interpolation version, about all possible interpolation templates, about low-regularity inputs, or about higher spatial dimensions. For affine inputs \(J_f=0\) and there is no nontrivial normalized error distribution. The optimal choice of interpolation nodes, computational overhead of alternative randomization, and finite-sample coverage guarantees are not established. A general common-random-environment mixture principle is known; the specific SCV law, its universal sharp moment, and its conditional calibration formula constitute the assessed result. Publication-priority comparisons are bounded by the sources listed below; no independent scientific audit is asserted.

## References

1. R. J. Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals*, arXiv:2309.09059v1 (publicly submitted September 16, 2023); full text: https://arxiv.org/html/2309.09059v2 .
2. N. Chopin and M. Gerber, *Higher-order stochastic integration through cubic stratification*, arXiv:2210.01554v1 (October 4, 2022); full text: https://arxiv.org/abs/2210.01554 .
3. M. K. Nakayama and B. Tuffin, *Sufficient Conditions for Central Limit Theorems and Confidence Intervals for Randomized Quasi-Monte Carlo Methods*, ACM Transactions on Modeling and Computer Simulation 34(3), Article 13 (May 16, 2024), DOI:10.1145/3643847; author-preprint: https://web.njit.edu/~marvin/rqmcclt-tomacs-r2.pdf .
