# Cauchy limits for one-step Gaussian-sketched harmonic Ritz values

## Finding

For a real symmetric positive-definite matrix and any fixed non-eigenvector starting direction, the one-step Gaussian-sketched **harmonic** Ritz value has a reciprocal of a translated, rescaled Student law. Consequently, for **every finite sketch dimension**, its absolute moments exist exactly below order one, while its positive and negative first moments are both infinite. More strongly, averages of independent harmonic Ritz values converge in distribution to an explicit **nondegenerate Cauchy law**, rather than to any deterministic value. The exact tail coefficient and the Cauchy location and scale are given below.

These statements contrast with the ordinary one-step Gaussian-sketched Rayleigh--Ritz scalar, which has a finite mean for sketch dimension at least two. The distinction is caused by taking a reciprocal of the sketched harmonic inner product, not by lack of positive definiteness of the original matrix.

## Assumptions and scope

Let \(n\ge2\), let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, let \(b\in\mathbb R^n\setminus\{0\}\) be fixed independently of the sketch, and let \(s\ge1\) be any **finite integer**. Draw \(S\in\mathbb R^{s\times n}\) with mutually independent \(N(0,1/s)\) entries. The one-step sketched harmonic Ritz scalar is
\[
\Theta=\frac{\|SAb\|_2^2}{(SAb)^{\mathsf T}Sb},
\]
provided its denominator is nonzero. Write \(u=Ab\), \(w=b=A^{-1}u\), and set
\[
\alpha=\frac{u^{\mathsf T}w}{\|u\|_2^2}>0,
\qquad
\delta=\left(\frac{\|w\|_2^2}{\|u\|_2^2}-\alpha^2\right)^{1/2}\ge0.
\]
By Cauchy--Schwarz, \(\delta=0\) exactly when \(b\) is an eigenvector of \(A\). All statements below concern exact real arithmetic, fixed data \((A,b)\), and fresh independent Gaussian sketches; they do not cover adaptive choices of \(b\) depending on \(S\).

If \(\delta=0\), then \(\Theta=1/\alpha>0\) almost surely; this is the complete exceptional case. Assume henceforth \(\delta>0\). Then \(\Theta\) is finite and nonzero almost surely, and its reciprocal has the exact representation
\[
R:=\Theta^{-1}\ \overset{d}{=}\ \alpha+\frac{\delta}{\sqrt{s}}T_s,
\qquad T_s\sim\mathrm{Student}(s).
\]
The density of \(R\), written \(f_R\), is strictly positive and smooth on the entire real line. In particular,
\[
f_R(0)=
\frac{\Gamma((s+1)/2)}{\sqrt\pi\,\delta\,\Gamma(s/2)}
\left(1+\frac{\alpha^2}{\delta^2}\right)^{-(s+1)/2}>0.
\]
The following claims hold for every choice of \((A,b,s)\) satisfying these assumptions.

**Exact moment threshold and tails.** For every real \(p>0\),
\[
\mathbb E|\Theta|^p<\infty\quad\Longleftrightarrow\quad 0<p<1.
\]
Moreover \(\mathbb E\Theta_+=\mathbb E(-\Theta)_+=\infty\), so the ordinary signed expectation is undefined. The sharp two-sided tail is
\[
\lim_{t\to\infty}t\Pr\{|\Theta|>t\}=2f_R(0),
\]
and its logarithmically truncated absolute mean satisfies
\[
\lim_{B\to\infty}\frac{\mathbb E[|\Theta|\,\mathbf1_{\{|\Theta|\le B\}}]}{\log B}
=2f_R(0).
\]
The positive and negative tails each have coefficient \(f_R(0)\).

**Nonconcentrating averages.** Let \(\Theta_1,\Theta_2,\ldots\) be independent copies, each generated with the same fixed \((A,b,s)\) and a fresh sketch. The improper integral
\[
m_{\rm PV}=\int_0^\infty\frac{f_R(r)-f_R(-r)}{r}\,dr
\]
is absolutely convergent at both endpoints. Let \(\gamma=\pi f_R(0)>0\). Then
\[
\frac1N\sum_{j=1}^N\Theta_j
\ \xrightarrow[N\to\infty]{\ d\ }\
\operatorname{Cauchy}(m_{\rm PV},\gamma).
\]
Here \(\operatorname{Cauchy}(m,\gamma)\) has characteristic function \(\exp(imt-\gamma|t|)\). Thus repeated sketching and ordinary averaging do not consistently estimate any deterministic harmonic Ritz value at fixed finite \(s\), regardless of how large that finite dimension is.

**Contrast.** The ordinary sketched one-dimensional Rayleigh--Ritz scalar
\[
\Lambda=\frac{(Sb)^{\mathsf T}SAb}{\|Sb\|_2^2}
\]
has a translated-scaled Student law of the same degrees \(s\). For \(s\ge2\), \(\mathbb E|\Lambda|<\infty\) and \(\mathbb E\Lambda=b^{\mathsf T}Ab/\|b\|_2^2\). This contrast is a comparison, not a claim of novelty about the classical Student distribution.

## Proof

**1. Exact reciprocal law.** Put \(v=(w-\alpha u)/(\delta\|u\|_2)\). The definitions give \(v^{\mathsf T}u=0\) and \(\|v\|_2=1\), and \(w=\alpha u+\delta\|u\|_2v\). Orthogonal Gaussian projections imply that \(g=\sqrt s\,Su/\|u\|_2\) and \(h=\sqrt s\,Sv\) are independent standard normal vectors in \(\mathbb R^s\). Consequently,
\[
R=\frac{(Su)^{\mathsf T}Sw}{\|Su\|_2^2}
=\alpha+\delta\frac{g^{\mathsf T}h}{\|g\|_2^2}.
\]
Conditioned on \(g\ne0\), the scalar \(g^{\mathsf T}h/\|g\|_2\) is standard normal, with conditional law independent of \(g\). Also \(\|g\|_2^2\sim\chi_s^2\). Thus the last ratio is a standard normal divided by \(\sqrt{\chi_s^2}\), which equals \(T_s/\sqrt s\) in law. The Gaussian sketch denominator vanishes exactly when \(R=0\), an event of probability zero because the Student density is continuous.

**2. Tail and moment laws.** Since the Student density is smooth and positive, \(f_R(r)=f_R(0)+O(|r|)\) near zero. For \(t>0\),
\[
\Pr\{|\Theta|>t\}=\Pr\{|R|<1/t\}
=\int_{-1/t}^{1/t}f_R(r)\,dr
=\frac{2f_R(0)}{t}+O(t^{-2}).
\]
One-sided integrals give the separate constants \(f_R(0)\). Because \(\mathbb E|\Theta|^p=\int_{\mathbb R}|r|^{-p}f_R(r)\,dr\), integrability at \(r=0\) holds precisely for \(p<1\), and the tails of the integral away from zero are harmless for \(p>0\). Both positive and negative first moments diverge separately. Finally, either integrating the tail or integrating \(|r|^{-1}f_R(r)\) over \(1/B\le|r|\) yields the claimed exact logarithmic coefficient.

**3. Cauchy limit.** For \(x\ne0\), the density of \(\Theta\) is \(g(x)=f_R(1/x)/x^2\). Smoothness of \(f_R\) near zero gives
\[
g(x)=\frac{f_R(0)}{x^2}+O(|x|^{-3})
\quad\text{as }|x|\to\infty,
\]
and \(g(x)-g(-x)=O(x^{-3})\) as \(x\to+\infty\). Therefore \(x[g(x)-g(-x)]\) is integrable on \((0,\infty)\): at infinity by the preceding estimate, and near zero since \(g\) is a probability density (indeed the Student density implies \(g(x)=O(|x|^{s-1})\) there). Symmetrization and dominated convergence give
\[
\frac{\mathbb E\sin(t\Theta)}{t}
\longrightarrow\int_0^\infty x[g(x)-g(-x)]\,dx
=m_{\rm PV}.
\]
For the real part, subtract \(f_R(0)/x^2\) on both sufficiently far tails and use the integrable remainder; the classical integral \(\int_{\mathbb R}(1-\cos(tx))/x^2\,dx=\pi|t|\) yields
\[
1-\mathbb E\cos(t\Theta)=\pi f_R(0)|t|+o(|t|).
\]
Thus the characteristic function \(\varphi(t)\) obeys \(\varphi(t)=1+im_{\rm PV}t-\pi f_R(0)|t|+o(|t|)\). Independence implies \(\varphi(t/N)^N\to\exp(im_{\rm PV}t-\gamma|t|)\), and the continuity theorem yields the stated Cauchy weak limit. Its scale is strictly positive, precluding convergence of the averages in probability to any constant.

**4. Ordinary sketched Rayleigh--Ritz contrast.** Interchanging the roles of \(u\) and \(w\) in Step 1 shows that \(\Lambda\) is a positive deterministic center plus a scaled Student \(T_s\), or a constant in the eigenvector case. The Student law has a finite first absolute moment for \(s>1\), and its centered part has mean zero. Hence \(\mathbb E\Lambda=b^{\mathsf T}Ab/\|b\|_2^2\) for all \(s\ge2\).

## Verification

Execute `python verify.py` after installing NumPy and SciPy. The included standalone script passed **1,562** algebraic, Gaussian-sketch, Student-CDF, exact angle-witness, Pareto-tail, and Cauchy-average checks. It uses fixed pseudorandom seeds for Monte Carlo comparisons and numerical integration of the Cauchy centering integral. The analytical steps above prove the infinite-dimensional quantifiers over allowable matrices and sketch widths; finite tests do not replace those steps.

For illustration, on a two-eigenvalue matrix with condition number \(10\), and a fixed input realizing the extreme-eigenvalue Kantorovich angle, \(s=16\) gives a negative harmonic Ritz probability of approximately \(0.0062777\), yet the Cauchy scale of independent-sketch averages is approximately \(0.062941\) and does not vanish when the number of averaged sketches increases. This finite-\(s\) statement is compatible with stronger concentration as the sketch dimension itself increases.

## Relationship to prior work

Güttel, Liu and Nyman (first public version July 11, 2026), Section 5.3, equation (23), express reciprocals of sketched harmonic Ritz values using the sketched bilinear form \((Sx)^{\mathsf T}SA^{-1}x/\|Sx\|_2^2\) and supply a sufficient embedding condition for their positivity. Their theorem concerns convergence under adequate embeddings and does not provide this fixed-input Gaussian reciprocal distribution, moment threshold, asymptotic heavy-tail coefficient, or nonconcentrating repeated-sketch Cauchy limit. The published experiments in that work use a sparse sign sketch; Gaussian sketches are separately discussed as a possible embedding family.

Nakatsukasa and Tropp develop sketched Rayleigh--Ritz theory and accuracy under subspace embeddings, a related but different projection. Simoncini and Wang study stabilization of sketched Krylov recurrences and spectral location. The Student and chi-square identities used in this proof are classical, as is the Cauchy domain-of-attraction principle; the claim here is their exact application to the defined sketched harmonic Ritz observable and its resulting moment/averaging obstruction. No claim is made about broader random-ratio theory being new.

## Limitations

The result covers only one-step real Gaussian sketched harmonic extraction with deterministic SPD input and exact arithmetic. It does not apply as stated to complex, sparse-sign, orthogonal, or adaptive sketches, to multiple Ritz values, or to the global convergence of a restarted algorithm. Infinite expected magnitude is an unconditional population statement and does not imply that any individual finite-precision run must become large. Conditional subspace-embedding events can suppress the denominator singularity. For each fixed finite \(s\) the averaging limit is nondegenerate; the theorem does not assert interchange of the sketch-dimension and replication limits. Historical mathematical priority remains subject to independent literature verification.

## References

1. S. Güttel, J. Liu, L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354v1, first submitted 2026-07-11, especially Sections 2.2, 5.3 and equation (23). https://arxiv.org/abs/2607.10354
2. Y. Nakatsukasa, J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113 (2021), later SIAM Journal on Matrix Analysis and Applications 45 (2024), 1183--1214. https://arxiv.org/abs/2111.00113
3. V. Simoncini, Y. Wang, *Stabilized Krylov Subspace Recurrences via Randomized Sketching*, Numerical Linear Algebra with Applications (2025). https://doi.org/10.1002/nla.70022
4. Classical Student \(t\), chi-square, Gaussian orthogonal projection, and characteristic-function continuity identities, as stated and derived where used in the proof.
