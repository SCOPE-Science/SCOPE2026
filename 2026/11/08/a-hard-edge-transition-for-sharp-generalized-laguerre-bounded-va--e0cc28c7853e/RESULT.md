# A hard-edge transition for sharp generalized Laguerre bounded-variation coefficients

## Finding

Let \(\alpha>-1\), \(n\ge1\), and \(L_n^{(\alpha)}\) denote the generalized Laguerre polynomial in the standard normalization \(L_n^{(\alpha)}(0)=\binom{n+\alpha}{n}\). Define
\[
F_{n,\alpha}(x)=\int_0^x t^\alpha e^{-t}L_n^{(\alpha)}(t)\,dt,\qquad
M_{n,\alpha}=\max_{x\ge0}|F_{n,\alpha}(x)|.
\]
For every complex-valued bounded-variation function \(f\) on \([0,\infty)\),
\[
\left|\int_0^\infty f(x)x^\alpha e^{-x}L_n^{(\alpha)}(x)\,dx\right|
\le M_{n,\alpha}\operatorname{Var}_{[0,\infty)}(f).
\]
The constant is exactly sharp: a Heaviside jump at a maximizing location realizes equality.

Write the ordered, strictly positive roots of \(L_n^{(\alpha)}\) as \(x_{n,1}<\cdots<x_{n,n}\). There is a *finite-degree global classification*:

- If \(-1<\alpha\le-1/2\), the first root \(x_{n,1}\) uniquely maximizes \(|F_{n,\alpha}|\); successive critical-point absolute heights strictly decrease.
- If \(\alpha>-1/2\), every maximizing root is one of the closest roots immediately below/above \(x_\ast=\alpha+1/2\) (one candidate if the comparison point falls outside the root range or is itself a root).

The asymptotic sharp coefficient norm exhibits a hard-edge/bulk transition. Write \(j_{\alpha,1}\) for the first positive zero of the Bessel function \(J_\alpha\). For \(-1<\alpha\le-1/2\),
\[
\lim_{n\to\infty} nM_{n,\alpha}=
\left(\frac{j_{\alpha,1}}2\right)^{\alpha+1}
\left|J_{\alpha+1}(j_{\alpha,1})\right|,
\qquad
\lim_{n\to\infty}nx_{n,1}=\frac{j_{\alpha,1}^2}{4}.
\]
For \(\alpha>-1/2\),
\[
\lim_{n\to\infty}n^{3/4-\alpha/2}M_{n,\alpha}
=\frac{e^{-(\alpha+1/2)/2}(\alpha+1/2)^{\alpha/2+1/4}}{\sqrt\pi},
\]
and all maximizing locations converge to \(\alpha+1/2\). At \(\alpha=-1/2\), the first constant equals \(1/\sqrt\pi\). The statement is for each fixed parameter \(\alpha\), not a double limit where the parameter also varies with \(n\).

## Assumptions and scope

The weight is exactly \(x^\alpha e^{-x}\) on the positive half-line. Here \(\alpha>-1\) ensures integrability at the origin, and \(n\ge1\) ensures the Laguerre polynomial has zero weighted mean. The variation is ordinary total variation on \([0,\infty)\), including any interior jumps; every such function is bounded. The generalized Laguerre basis has not been orthonormalized. For the conventional expansion coefficient with prefactor \(n!/\Gamma(n+\alpha+1)\), multiply the sharp constants above by that factor.

## Proof

**1. Exact primitive and differential equation.** The differentiation identity for generalized Laguerre polynomials, or integration of the Rodrigues formula, gives
\[
F_{n,\alpha}(x)=\frac{x^{\alpha+1}e^{-x}}{n}L_{n-1}^{(\alpha+1)}(x).
\]
Consequently \(F_{n,\alpha}(0)=F_{n,\alpha}(\infty)=0\) and
\[
F_{n,\alpha}'=x^\alpha e^{-x}L_n^{(\alpha)},\qquad
F_{n,\alpha}''+\left(1-\frac\alpha x\right)F_{n,\alpha}'
+\frac nxF_{n,\alpha}=0.
\]
For a bounded-variation \(f\), Stieltjes integration by parts (first for step functions, then for the variation measure) yields
\[
\int_0^\infty f\,dF_{n,\alpha}=-\int_{(0,\infty)}F_{n,\alpha}\,df.
\]
The boundary terms vanish, proving the inequality. Taking \(f\) to jump from \(0\) to \(1\) at a global maximizing point produces \(-F_{n,\alpha}(x)\) and proves sharpness.

**2. Global envelope and exact finite-degree localization.** Define, for \(x>0\),
\[
E_{n,\alpha}(x)=F_{n,\alpha}(x)^2+\frac{x}{n}F_{n,\alpha}'(x)^2.
\]
Differentiating and using the displayed differential equation produces the *exact Sonin identity*
\[
E_{n,\alpha}'(x)=\frac{2\alpha+1-2x}{n}F_{n,\alpha}'(x)^2.
\]
The derivative is strictly negative (apart from isolated roots) for \(-1<\alpha\le-1/2\), and changes sign once, at \(x_\ast=\alpha+1/2\), for \(\alpha>-1/2\). At each critical point of \(F_{n,\alpha}\), namely a zero of \(L_n^{(\alpha)}\), the envelope is precisely \(F_{n,\alpha}^2\). Because the primitive vanishes at both boundaries, its global absolute maximum occurs at such a root. The envelope's strict monotonicity on each side proves the complete finite-degree assertions, including uniqueness in the first-root regime. In the bulk regime, the candidate roots are the immediate neighbors of the turning point.

**3. Singular/hard-edge regime.** Classical Mehler–Heine asymptotics, locally uniformly for \(u>0\), give
\[
n^{-\alpha}L_n^{(\alpha)}(u/n)
\longrightarrow u^{-\alpha/2}J_\alpha(2\sqrt u),
\]
and the primitive identity consequently implies
\[
nF_{n,\alpha}(u/n)
\longrightarrow u^{(\alpha+1)/2}J_{\alpha+1}(2\sqrt u).
\]
Since \(n x_{n,1}\to j_{\alpha,1}^2/4\), and the *finite-degree global maximum is exactly at the first root* throughout \(\alpha\le-1/2\), evaluation there proves both limits in this regime. Substituting \(j_{-1/2,1}=\pi/2\) and the elementary half-integer Bessel formula yields \(1/\sqrt\pi\) at the transition.

**4. Bulk regime.** For each fixed \(\alpha>-1/2\), fixed-point generalized Laguerre Plancherel–Rotach asymptotics, uniformly on compact positive \(x\)-intervals, give quadrature-phase leading terms
\[
F_{n,\alpha}(x)=\frac{n^{\alpha/2-3/4}e^{-x/2}x^{\alpha/2+1/4}}{\sqrt\pi}
\bigl(\sin\vartheta_n(x)+o(1)\bigr),
\]
\[
\sqrt{x/n}\,F_{n,\alpha}'(x)
=\frac{n^{\alpha/2-3/4}e^{-x/2}x^{\alpha/2+1/4}}{\sqrt\pi}
\bigl(\cos\vartheta_n(x)+o(1)\bigr).
\]
Here the phase \(\vartheta_n(x)=2\sqrt{nx}-\alpha\pi/2-\pi/4\) is compatible with the standard formula up to a harmless phase shift; only the relative quarter-period is used. Hence
\[
n^{3/2-\alpha}E_{n,\alpha}(x)
\longrightarrow \frac{e^{-x}x^{\alpha+1/2}}\pi
\]
uniformly near \(x_\ast=\alpha+1/2>0\). The exact envelope identity gives \(\sup_{x>0}E_{n,\alpha}(x)=E_{n,\alpha}(x_\ast)\), which bounds all \(|F_{n,\alpha}(x)|\) from above. Consecutive zeros of \(L_n^{(\alpha)}\) around the positive fixed point \(x_\ast\) have spacing \(O(n^{-1/2})\) by the same compact-uniform Plancherel–Rotach formula, so some root \(z_n=x_\ast+O(n^{-1/2})\) satisfies \(F_{n,\alpha}'(z_n)=0\) and thus \(F_{n,\alpha}(z_n)^2=E_{n,\alpha}(z_n)\). The uniform envelope limit yields the matching lower bound. Finally, for any fixed \(\varepsilon>0\), the exact monotonicity of \(E\) gives a strict gap outside \((x_\ast-\varepsilon,x_\ast+\varepsilon)\) from its maximum for large \(n\); therefore all global maximizing roots tend to \(x_\ast\).

## Verification

The standalone `CHECK.py` checks the primitive ODE, the exact envelope derivative, the root-selection rules over multiple degrees and parameters, and representative scaled asymptotic constants against Bessel/elementary formulas. A successful execution prints `GENERALIZED_LAGUERRE_BV_CHECKS_PASSED 655`. These are finite numerical corroborations, **not** a proof of the infinite statement; the proof depends on the exact identities and classical locally uniform special-function asymptotics.

## Relationship to prior work

Zhang, Liu and Xiang study coefficient asymptotics for prescribed algebraic and logarithmic singularities, including generalized Laguerre expansions. That fixed-singularity analysis motivates the question of *optimizing the jump location* and does not itself provide a sharp operator norm over all bounded-variation functions, its finite-degree maximizer, or the parameter-dependent hard-edge transition. The classical Mehler–Heine and Plancherel–Rotach formulas, the Rodrigues identity, and the generic variation-by-primitive inequality are known ingredients, not presented here as novel. Previous analysis of the ordinary case \(\alpha=0\) gives a special case of the bulk constant; the contribution here is the full \(\alpha>-1\) classification, particularly the singular regime. Sluchak's later preprint describes sharp primitive inequalities for several orthogonal systems, including ordinary Laguerre polynomials, in its abstract; the full text was not accessible for detailed comparison, so any possible overlap remains a stated literature risk.

## Limitations

No claim is made for arbitrary varying parameters \(\alpha=\alpha(n)\), for other Laguerre normalizations without conversion, or for best constants in smoother function classes. The result gives leading asymptotics rather than a uniform error term. The bibliography comparison is not a certificate of publication priority; an unindexed equivalent theorem remains possible. No independent audit has been performed.

## References

- Y. Zhang, G. Liu, and S. Xiang, *Optimal asymptotic analyses on Laguerre and Hermite orthogonal approximation for functions of algebraic and logarithmic regularities*, arXiv:2604.17752v1, first posted 2026-04-20; https://arxiv.org/abs/2604.17752 .
- NIST Digital Library of Mathematical Functions, §18.15(iv), generalized Laguerre asymptotics, https://dlmf.nist.gov/18.15#iv , and §18.11 for Mehler–Heine limits.
- V. Sluchak, *Bounds for Orthogonal Expansion Coefficients via Weighted Primitives*, arXiv:2611.04067v1, https://arxiv.org/abs/2611.04067 (abstract inspected; full text not inspected).
