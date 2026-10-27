# The \(\beta=2\) level-repulsion transition under independent matrix-entry resetting

## Finding

For the stationary two-site tridiagonal Dyson-index matrix with independently reset entries, the small positive eigenvalue-gap density has a **sharp exponent saturation** at \(\beta=2\), with a logarithm at the transition. The stationary simultaneous-reset model, whose two-site gap asymptotic is known, instead saturates at \(\beta=1\). Yet both protocols have exactly the same second moment of the gap. The new assertion is the independent-reset classification and its exact constants; the simultaneous-reset classification is included as an attributed benchmark, not a new theorem.

**Theorem.** Fix \(\beta,D,\mu,r>0\). Let \(\Delta_{\mathrm I}\) be the positive difference of the two ordered eigenvalues of the stationary \(2\times2\) independent-entry-reset matrix described below. Its density \(p_{\mathrm I}\) obeys, as \(s\downarrow0\),

\[
p_{\mathrm I}(s)\sim
\begin{cases}
\displaystyle \frac{2^{1-\beta}\sqrt\pi\,h_0 M_\beta}{\Gamma((\beta+1)/2)}\,s^\beta, &0<\beta<2,\\[6pt]
\displaystyle\frac{2h_0r}{a}\,s^2\log(\ell/s), &\beta=2,\\[6pt]
\displaystyle\frac{2h_0r}{a(\beta-2)}\,s^2, &\beta>2.
\end{cases}
\]

Here \(\ell>0\) is any fixed reference length (its choice does not affect equivalence), \(a=2D/\beta\), \(S^2=D/(\beta\mu)\), \(\alpha=r/(2\mu)\), and the positive finite constants are

\[
M_\beta=\alpha S^{-\beta}\mathrm B(\alpha,1-\beta/2)
\quad(0<\beta<2),\qquad
h_0=\mathbb E\left[\frac{1}{\sqrt{2\pi(S^2(T_1)+S^2(T_2))}}\right],
\]

where \(T_1,T_2\) are independent exponential variables of rate \(r\), and \(S^2(t)=S^2(1-e^{-2\mu t})\). In particular, the small-gap exponent is \(\min\{\beta,2\}\), apart from the logarithmic correction at equality.

Let \(\Delta_{\mathrm S}\) denote the gap under the *same marginal entry dynamics* but with a common Poisson reset clock. In both protocols,

\[
\boxed{\mathbb E[\Delta_{\mathrm I}^{\,2}]
=\mathbb E[\Delta_{\mathrm S}^{\,2}]
=\frac{4D(\beta+1)}{\beta(r+2\mu)}.}
\]

The previously established simultaneous-reset gap law has small-gap exponent \(\min\{\beta,1\}\), logarithmic at \(\beta=1\) [2]. Thus identical second gap moments coexist with different sharp repulsion exponents for every \(\beta\ge1\); at \(\beta=1\), the independent-reset density is asymptotically linear while the simultaneous-reset density has a logarithmic enhancement.

## Assumptions and scope

The \(2\times2\) real symmetric tridiagonal matrix is

\[
H=\begin{pmatrix}X&C\\C&Y\end{pmatrix},\qquad C\ge0,
\qquad \Delta=\sqrt{(X-Y)^2+4C^2}.
\]

At the stationary observation time, each diagonal entry \(X,Y\), conditioned on its most recent reset age \(T\sim\operatorname{Exp}(r)\), is centered Gaussian with variance \(S^2(T)\). The nonnegative off-diagonal entry satisfies \(2C=\sqrt2\,S(T)\,R_\beta\), with \(R_\beta\) a chi variable with \(\beta>0\) degrees of freedom (equivalently, \(R_\beta^2\) has Gamma shape \(\beta/2\) and scale \(2\)). All Gaussian, Gamma, and reset-age variables are mutually independent for the independent-reset model. For the simultaneous-reset model, all three entries share one reset age \(T\) but have conditionally independent Gaussian and Gamma draws. Every reset returns the relevant entry to zero. These are exactly the stationary entry distributions of [1, equations (76), (81), (97)–(101)] for matrix dimension two.

Only the single positive spacing between the two eigenvalues is studied. Parameters are fixed during the small-gap limit. Neither a many-level spacing distribution nor a large-matrix limit is asserted.

## Proof

**1. Independent stationary diagonal difference.** Write \(Z=X-Y\) and denote its density by \(h\). Conditional on independent reset ages \(T_1,T_2\), this difference is centered Gaussian with variance \(S^2(T_1)+S^2(T_2)\). Thus

\[
h(z)=\mathbb E\left[\frac{\exp\left(-z^2/[2(S^2(T_1)+S^2(T_2))]\right)}{\sqrt{2\pi(S^2(T_1)+S^2(T_2))}}\right].
\]

Since \(S^2(t)=at+O(t^2)\) as \(t\downarrow0\), the integrand at \(z=0\) is locally bounded by a constant times \((T_1+T_2)^{-1/2}\), integrable over a neighborhood of the origin with respect to the joint age density. Dominated convergence shows that \(h\) is continuous, bounded, even, and \(h(0)=h_0\in(0,\infty)\).

**2. Independent stationary off-diagonal density.** Put \(U=2C\). By the chi density and the age mixture, its density on \((0,\infty)\) is

\[
g_\beta(u)=\frac{2^{1-\beta}}{\Gamma(\beta/2)}u^{\beta-1}
\int_0^\infty re^{-rt}[S(t)]^{-\beta}
\exp\left(-\frac{u^2}{4S^2(t)}\right)\,dt.
\]

For \(0<\beta<2\), the negative moment in this integral is finite. The substitution \(v=e^{-2\mu t}\) gives the displayed \(M_\beta\), and dominated convergence yields

\[
g_\beta(u)\sim \frac{2^{1-\beta}M_\beta}{\Gamma(\beta/2)}u^{\beta-1}.
\]

For \(\beta\ge2\), the integral is controlled by ages \(t=O(u^2)\). Splitting it at a fixed small age, replacing \(S^2(t)=at(1+O(t))\) within the singular part, and substituting \(w=u^2/(4at)\) gives

\[
g_2(u)\sim\frac{r}{a}u\log(\ell/u),\qquad
g_\beta(u)\sim\frac{r}{a(\beta-2)}u\quad(\beta>2).
\]

The stated limits follow from \(\int_0^\infty w^{\beta/2-2}e^{-w}\,dw=\Gamma(\beta/2-1)\) and the logarithmic borderline when \(\beta=2\). The regular (nonzero-age) part is asymptotically negligible for \(\beta>2\), and contributes only to lower logarithmic order for \(\beta=2\).

**3. The radial gap transform.** Since \(Z,U\) are independent and \(U>0\), the polar change of variables \(Z=s\sin\phi\), \(U=s\cos\phi\), with \(-\pi/2<\phi<\pi/2\), gives the exact density identity

\[
p_{\mathrm I}(s)=s\int_{-\pi/2}^{\pi/2}
 h(s\sin\phi)g_\beta(s\cos\phi)\,d\phi.
\]

For \(\beta<2\), the integrable bound \(g_\beta(u)\le C u^{\beta-1}\) for small \(u\) allows dominated convergence after dividing by \(s^\beta\). Evaluating \(\int_{-\pi/2}^{\pi/2}(\cos\phi)^{\beta-1}\,d\phi=\mathrm B(1/2,\beta/2)\) and simplifying Gamma factors gives the first constant. For \(\beta>2\), dividing by \(s^2\) and integrating \(\cos\phi\) produces the third constant. At \(\beta=2\), dividing by \(s^2\log(\ell/s)\) works because the additional \(\cos\phi\log(1/\cos\phi)\) term is integrable; this gives the middle constant. These arguments establish the claimed equivalents, not merely numerical power laws.

**4. Equal second moments under both reset protocols.** Conditional on any reset age, the diagonal second moment is \(S^2(T)\), and the off-diagonal second moment is \(\beta S^2(T)/2\). Since \(\Delta^2=(X-Y)^2+4C^2\) and the two diagonal entries have zero means even with a shared age, in either reset protocol

\[
\mathbb E\Delta^2=2(\beta+1)\mathbb E[S^2(T)]
=2(\beta+1)\frac{D}{\beta\mu}\frac{2\mu}{r+2\mu},
\]

which simplifies to the stated common value.

**5. Prior simultaneous-reset comparison.** Sharing one age causes \(Z\) and \(U\) to combine conditionally into a single chi variable with \(\beta+1\) degrees of freedom, so \(\Delta_{\mathrm S}\mid T\) has law \(\sqrt2 S(T)R_{\beta+1}\). Its stationary density and the \(\beta=1\) small-gap saturation are explicitly derived in [2, equations (39)–(40), (68)–(70)]; they are *not* original here. The independent-reset density instead depends on the separate convolution \(h\) and on the singular mixture \(g_\beta\), leading to the distinct \(\beta=2\) threshold.

## Verification

The supplied standalone `verify_gap.py` evaluates the stationary chi-mixture integral through incomplete Gamma functions, the exact angular spectral-density integral, and the second-moment identity from independent Monte Carlo samples. Under Python with NumPy, SciPy, and mpmath installed, run `python verify_gap.py`. The recorded execution passed 97 assertion groups. The numerical results corroborate the formulas for multiple Dyson indices; the all-parameter proof is the analytic argument above, not the finite tests.

## Relationship to prior work

Akemann, Majumdar and Päßler [1] introduce the matrix process, prove the independent-entry stationary laws, and explain that even its stationary eigenvalue density is difficult; the entries and their Gamma/Gaussian mixtures are **prior results**, not new constructions. Their examples focus on numerical average eigenvalue densities at larger matrix dimensions, not the exact small-gap law in the two-site independent-reset process.

Biroli, Majumdar and Schehr [2] establish **the complete simultaneous-reset two-particle gap distribution and its small-gap trichotomy**, including the exponent \(\min\{\beta,1\}\) and the logarithm at \(\beta=1\). These are fully attributed. The present theorem isolates a different reset protocol and proves its distinct exponent saturation at \(\beta=2\), the corresponding sharp coefficients, and the shared second-moment contrast. The non-reset tridiagonal beta ensemble is due to Dumitriu and Edelman [3].

## Limitations

The result is for the minimal nontrivial matrix dimension two, stationary independent Poisson entry clocks with a common rate, positive harmonic restoring strength, and the specified Gaussian/CIR entry dynamics. It does not determine the full independent-reset eigenvalue joint density at general dimension, nearest-neighbor bulk spacing as dimension tends to infinity, transient dynamics, or arbitrary non-Poisson reset distributions. Although the eigenvalue gap is exactly computable from the previously known entry law, extracting the phase boundary requires a singular-limit calculation. The possibility of a broader previously published statement that implies the independent-reset asymptotics cannot be excluded without independent priority review.

## References

[1] G. Akemann, S. N. Majumdar, and P. Päßler, *A tridiagonal matrix-valued process with stochastic resetting for arbitrary Dyson index \(\beta>0\)*, arXiv:2605.26945v1 (first posted 26 May 2026), especially Sections 5–6 and equations (76), (81), (97)–(101). https://arxiv.org/abs/2605.26945

[2] M. Biroli, S. N. Majumdar, and G. Schehr, *Resetting Dyson Brownian motion*, arXiv:2503.14733v1 (18 March 2025), especially equations (39)–(40), (68)–(70). https://arxiv.org/abs/2503.14733

[3] I. Dumitriu and A. Edelman, *Matrix models for beta ensembles*, Journal of Mathematical Physics 43 (2002), 5830–5847, https://doi.org/10.1063/1.1507823.
