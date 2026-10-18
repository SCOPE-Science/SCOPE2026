# Spectrally sharp small-ball constants for independent tensorized Gaussian probes

## Finding
Let \(M\in\mathbb R^{m\times n}\) be nonzero, of rank \(r\), and let \(\ell\ge1\) be an integer. For independent standard real Gaussian vector pairs \((u_j,v_j)\), put \(X_j=u_j^{\mathsf T}Mv_j\) and
\[
Q_\ell=\frac{\sqrt\ell\,\|M\|_F}{(\sum_{j=1}^{\ell}X_j^2)^{1/2}}.
\]
For fixed \(M\) and \(\ell\), the large-distortion probability has the following **exact leading laws** as \(\tau\to\infty\):

* If \(r=1\),
\[
\Pr\{Q_\ell>\tau\}\sim
\frac{\ell^{\ell/2}}{\pi^{\ell/2}\Gamma(1+\ell/2)}
\frac{(\log\tau)^\ell}{\tau^\ell}.
\]
* If \(r\ge2\) and the nonzero singular values are \(s_1,\dots,s_r\), define
\[
f_M(0)=\frac1\pi\int_0^\infty\prod_{j=1}^r
(1+s_j^2t^2)^{-1/2}\,dt,\qquad
V_\ell=\frac{\pi^{\ell/2}}{\Gamma(1+\ell/2)}.
\]
Then
\[
\Pr\{Q_\ell>\tau\}\sim
V_\ell\ell^{\ell/2}
\bigl(\|M\|_F f_M(0)\bigr)^\ell\tau^{-\ell}.
\]
For every \(r\ge1\) and every real \(p>0\),
\[
\mathbb E Q_\ell^p<\infty\quad\Longleftrightarrow\quad p<\ell.
\]
In particular, two independent tensor probes are necessary and sufficient for a finite mean distortion ratio; three are necessary and sufficient for a finite second moment (and hence finite variance). These are conclusions about the validation ratio, not the convergence of the approximation algorithm.

For fixed \(r\ge2\), the leading coefficient in the second display, among all matrices of rank \(r\) and fixed Frobenius norm, is uniquely minimized when the \(r\) nonzero singular values are equal. Its exact minimum is
\[
C_{\ell,r}^{\min}=V_\ell\ell^{\ell/2}
\left[\frac{\sqrt r\,\Gamma((r-1)/2)}{2\sqrt\pi\,\Gamma(r/2)}\right]^\ell.
\]
For every finite \(r\), this is strictly larger than the corresponding full independent Gaussian-probe leading coefficient
\[
C_\ell^{\mathrm{full}}=
V_\ell\left(\frac{\ell}{2\pi}\right)^{\ell/2};
\]
the ratio tends to one as \(r\to\infty\) through equal-singular-value matrices. At rank two and two probes the minimum tensorized coefficient is exactly \(\pi\), versus one for full Gaussian probes. The result supplies exact fixed-matrix asymptotics, not a uniform approximation over matrices with arbitrarily small nonzero singular values.

## Assumptions and scope
Here \(m,n\ge1\), \(1\le r\le\min(m,n)\), and each \(u_j\in\mathbb R^m\), \(v_j\in\mathbb R^n\) has independent standard normal coordinates. All vectors for distinct \(j\) are mutually independent. The same assertion applies to a *separable, fixed* real matrix-valued residual \(h(z)=\phi(z)M\), for a nonzero \(\phi\in L^2(\Omega)\): its tensor-probed \(L^2\) norm ratio is precisely \(Q_\ell\) when each sample is divided by \(\sqrt\ell\). The residual must be selected independently of the validation probes. Notably, every such separable residual has operator stable rank one in the spatial-variable decomposition regardless of the ordinary matrix rank \(r\), so a stable-rank-one guarantee cannot itself distinguish the two logarithmic regimes. The statements concern Euclidean/Frobenius norm and exact real Gaussian tests, not complex Gaussian tests or the error of an approximation itself fitted with the same probes.

## Proof
**1. Reduction to one scalar bilinear form.** An SVD and orthogonal invariance give
\[
X_j\stackrel{d}=\sum_{k=1}^{r}s_kG_{jk}H_{jk},
\]
where every \(G_{jk}\) and \(H_{jk}\) is standard normal and all are independent. Conditioning on the \(G_{jk}\) yields the scalar characteristic function
\[
\varphi_M(t)=\mathbb E e^{itX_1}
=\prod_{k=1}^{r}(1+s_k^2t^2)^{-1/2}.
\]
The denominator of \(Q_\ell\) is positive almost surely: the nontrivial scalar bilinear form has a continuous distribution away from the origin, with no atom at zero.

**2. Nondegenerate rank.** If \(r\ge2\), \(\varphi_M\in L^1(\mathbb R)\), by its \(O(|t|^{-r})\) decay. Fourier inversion therefore produces a bounded continuous scalar density \(f_M\), with the strictly positive origin value displayed above. Independence gives the joint density \(\prod_{j=1}^{\ell}f_M(x_j)\). The event \(Q_\ell>\tau\) is the ball
\[
\sum_{j=1}^{\ell}x_j^2<\frac{\ell\|M\|_F^2}{\tau^2}.
\]
Rescale this ball to unit radius and apply continuity and dominated convergence. Its volume is \(V_\ell\), producing exactly the claimed \(\tau^{-\ell}\) constant.

**3. Rank one, including the logarithmic coefficient.** Write \(s=\|M\|_F\). The product of two independent standard Gaussians has density \(K_0(|x|)/(\pi)\), where \(K_0\) is the modified Bessel function, so \(X_1\) has density \(K_0(|x|/s)/(\pi s)\). The classical origin expansion is
\[
K_0(z)=\log(1/z)+O(1),\qquad z\downarrow0.
\]
Set \(a=\sqrt\ell s/\tau\), and substitute \(x_j=ay_j\) in the ball integral. For almost every \(y\) in the unit ball, each density divided by \(\log\tau\) tends to \((\pi s)^{-1}\). The uniform bound \(K_0(a|y_j|/s)\le C(\log\tau+1+|\log|y_j||)\) for sufficiently large \(\tau\), together with integrability of \(\prod_j(1+|\log|y_j||)\) over the unit ball, permits dominated convergence. Multiplication by \(a^\ell\) and \(V_\ell\) gives the stated exact \(\tau^{-\ell}(\log\tau)^\ell\) coefficient. The singular density, rather than insufficient independence across probes, is responsible for the logarithms.

**4. Moment boundary.** The tail-integral identity
\[
\mathbb E Q_\ell^p=p\int_0^\infty \tau^{p-1}\Pr\{Q_\ell>\tau\}\,d\tau
\]
holds for every \(p>0\). At infinity the integrand is asymptotic to a positive constant times \(\tau^{p-\ell-1}\) for \(r\ge2\), or the same times \((\log\tau)^\ell\) for \(r=1\). Both are integrable precisely when \(p<\ell\). The integral near zero is finite because the probability is at most one.

**5. Sharp spectral minimization and dense comparison.** Fix \(\sum s_k^2=F^2\), and put \(w_k=s_k^2/F^2\), so \(\sum w_k=1\). After normalizing \(t\) by \(F\), the normalized origin density is
\[
Ff_M(0)=\frac1\pi\int_0^\infty\prod_{k=1}^{r}(1+w_kt^2)^{-1/2}\,dt.
\]
Strict concavity of \(w\mapsto\log(1+wt^2)\), for every \(t>0\), gives
\[
\sum_{k=1}^{r}\log(1+w_kt^2)
\le r\log(1+t^2/r),
\]
with equality precisely at \(w_k=1/r\) for all \(k\). Thus the origin density, and hence the full leading constant, is uniquely smallest for a flat positive spectrum. At flat rank, Euler's beta integral evaluates
\[
Ff_M(0)=\frac{\sqrt r\,\Gamma((r-1)/2)}{2\sqrt\pi\,\Gamma(r/2)}.
\]
Separately, the elementary bound \(\log(1+u)<u\) for \(u>0\) gives the strict pointwise inequality
\[
\prod_{k=1}^r(1+w_kt^2)^{-1/2}>e^{-t^2/2},\qquad t>0.
\]
Integrating proves \(Ff_M(0)>1/\sqrt{2\pi}\), the origin density of a unit normal variable, and gives the claimed strict comparison with full Gaussian probes. Stirling's gamma-ratio asymptotic gives convergence to the full-Gaussian constant as \(r\to\infty\) through flat spectra.

## Verification
Running `python verify.py` with `scipy>=1.10` evaluates finite instances of the Fourier integral against exact beta formulas for ranks two through eight; checks the flat-spectrum coefficient for one through six probes, strict spectral imbalance comparisons, the full-Gaussian density inequality, and three diminishing radii each in the exact rank-two Laplace disk integral and rank-one product-normal integrals. It prints `PASS: 38 scalar density, constant, and small-ball checks`. These numerical checks do not establish the universal asymptotics; the argument above does.

For an exact rank-two witness, let \(M=I_2\). A scalar probe has the unit-scale Laplace distribution, with density \(\tfrac12e^{-|x|}\). For two probes \(\ell=2\), \(\Pr\{Q_2>\tau\}\sim\pi\tau^{-2}\); the non-tensorized Gaussian comparator is \(\sim\tau^{-2}\). For rank one and two probes, the law is instead \(\sim(2/\pi)\tau^{-2}(\log\tau)^2\).

## Relationship to prior work
Güttel, Kressner, and Vandereycken introduced multiple tensorized probes for matrix-function sketching. Their 2022 preprint, Section 3.3 and Theorem 3.4, treats one tensor probe and explicitly leaves improved multi-probe bounds open; the present theorem treats only a separable real fixed residual, not their general function-valued sketchAAA approximation. Bujanović and Kressner (2020, Theorems 2.2 and 3.1) gave useful nonasymptotic rank-one norm- and trace-estimation bounds, but do not identify the above fixed-rank leading constants or their spectral minimizers.

Shao and Nakatsukasa (2026, Lemma 2.4, Remark 2.5, and Theorem 2.7) already identify the qualitative disappearance of the logarithm for two nonzero singular values. Their block observable \(\|\Omega_L^{\mathsf T}M\Omega_R\|_F\) has shared left/right factors across its entries and has a different dependence structure from independent bilinear probes. They provide big-O bounds, not the constants, inverse-moment classification, or spectrum-constrained minimization in this theorem. Hu and Paouris (2024) give general small-ball estimates for projections of simple random tensors, not the fixed-matrix multi-probe asymptotics here. Known product-normal and Gaussian Fourier identities are used as mathematical ingredients, not claimed as new.

## Limitations
The statement is an exact asymptotic at fixed matrix, fixed rank, and fixed probe count; it contains no uniform error estimate as singular values tend to zero and no finite-\(\tau\) minimax ordering. The statistics of fully crossed left/right block probes can be different, and this theorem neither settles their full small-ball law nor handles complex Gaussian probes. It does not claim that sketchAAA with probes reused for fitting attains the same bound. The logarithmic rank-one phenomenon itself and the elementary product-normal density are prior knowledge; the contribution is the complete leading-constant, singular-spectrum, and moment classification for independent multi-probe norm validation.

## References
1. S. Güttel, D. Kressner, and B. Vandereycken, *Randomized sketching of nonlinear eigenvalue problems*, arXiv:2211.12175 (first posted 2022-11-22), Section 3.3, Theorem 3.4; https://arxiv.org/abs/2211.12175.
2. Z. Bujanović and D. Kressner, *Norm and trace estimation with random rank-one vectors*, arXiv:2004.06433 (2020), Theorems 2.2 and 3.1; https://arxiv.org/abs/2004.06433.
3. N. Shao and Y. Nakatsukasa, *Convergence analysis of a nonlinear eigensolver based on rational approximation of the resolvent*, arXiv:2607.10377 (2026), Lemma 2.4, Remark 2.5, Theorem 2.7; https://arxiv.org/abs/2607.10377.
4. F. Hu and G. Paouris, *Small Ball Probabilities for Simple Random Tensors*, arXiv:2403.20192 (2024), Theorem 1.1; https://arxiv.org/abs/2403.20192.
