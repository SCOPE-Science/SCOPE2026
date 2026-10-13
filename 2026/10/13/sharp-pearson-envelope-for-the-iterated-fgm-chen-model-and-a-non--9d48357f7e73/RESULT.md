# Sharp Pearson envelope for the iterated-FGM Chen model and a nonoptimal published corner

## Finding

Fix \(\theta>0\) and \(\beta>0\). Couple two identically distributed Chen lifetimes through the two-parameter iterated Farlie–Gumbel–Morgenstern (IFGM) copula used by Alawady et al. (2026). Let \(\rho(\gamma,\omega)\) denote their Pearson correlation, with the full admissible copula parameter set \(\Omega\) specified below. Define \(a,b\) from the Chen quantile in the next section. Then \(0<b<a\), and the **entire attainable correlation interval**, including both endpoints, is

\[
\boxed{\quad -a\ \leq\ \rho\ \leq\ -a+2b+\sqrt{(2a-b)^2+3b^2}.\quad}
\]

The lower endpoint is uniquely attained at \((\gamma,\omega)=(-1,0)\). The upper endpoint is uniquely attained at

\[
\gamma_*=-1+\frac{2(2a-b)}{\sqrt{(2a-b)^2+3b^2}},\qquad
\omega_*=\frac{3-\gamma_*+\sqrt{9-6\gamma_*-3\gamma_*^2}}{2}.
\]

In particular, \(0<\gamma_*<1\) and \(\omega_*>1\). Thus the point \((\gamma,\omega)=(1,1)\), called the maximizing corner in Section 3.1 of the 2026 source, **is never a Pearson maximizer for any positive Chen marginal parameters**. Its exact shortfall is

\[
\rho_{\max}-\rho(1,1)
=\sqrt{(2a-b)^2+3b^2}-(2a-b)
=\frac{3b^2}{\sqrt{(2a-b)^2+3b^2}+2a-b}>0.
\]

For the source's emphasized Chen parameters \((\theta,\beta)=(2,1.5)\), numerical quadrature gives \(\rho(1,1)=0.418064606189\ldots\), agreeing with its reported \(0.4181\), but the actual maximum is \(0.442643119199\ldots\), at \((\gamma_*,\omega_*)=(0.914229166194\ldots,1.544677230776\ldots)\). For another of its studied settings, \((\theta,\beta)=(1,1)\), the maximum is \(0.448380652718\ldots\) instead of the corner value \(0.417856529502\ldots\).

## Assumptions and scope

The marginal Chen distribution is

\[
F(x)=1-\exp\{-\theta[\exp(x^\beta)-1]\},\qquad x>0,\quad\theta,\beta>0.
\]

Its quantile is

\[
Q(u)=\left[\log\left(1-\frac{\log(1-u)}{\theta}\right)\right]^{1/\beta},\qquad 0<u<1.
\]

Both margins share precisely this \(F\); they are not assumed independent. The IFGM copula and its density are

\[
C(u,v)=uv[1+\gamma(1-u)(1-v)+\omega uv(1-u)(1-v)],
\]
\[
c(u,v)=1+\gamma(1-2u)(1-2v)+\omega u(2-3u)v(2-3v).
\]

The **full**, not rectangular, admissibility region established in the IFGM literature and reproduced in the source is

\[
\Omega=\left\{(\gamma,\omega):-1\le\gamma\le1,\quad \omega\ge-1-\gamma,\quad
\omega\le U(\gamma)\right\},\qquad
U(\gamma)=\frac{3-\gamma+\sqrt{9-6\gamma-3\gamma^2}}{2}.
\]

Set

\[
\mu=\int_0^1Q(u)\,du,\quad \sigma^2=\int_0^1Q(u)^2\,du-\mu^2,
\]
\[
A=\int_0^1Q(u)(1-2u)\,du,\qquad
B=\int_0^1Q(u)u(2-3u)\,du,\qquad
 a=\frac{A^2}{\sigma^2},\quad b=\frac{B^2}{\sigma^2}.
\]

All these moments are finite for every positive \(\theta,\beta\). The result concerns population Pearson correlation across all valid copulas with *fixed identical Chen margins*. It makes no assertion about maximal correlation after varying the marginal parameters continuously or about correlation with unequal Chen margins.

## Proof

**Step 1: Linear dependence coefficients.** The copula density factorizes its two perturbations into products of one-dimensional functions. Let \(X=Q(U)\) and \(Y=Q(V)\). Integrating the joint density against \(Q(u)Q(v)\), and subtracting the product of marginal means, gives the exact identity

\[
\operatorname{Cov}(X,Y)=\gamma A^2+\omega B^2,
\qquad \rho(\gamma,\omega)=a\gamma+b\omega.
\]

No approximation or assumption about the size of \(\gamma,\omega\) is used in this identity.

**Step 2: Strict coefficient ordering.** Since \(Q\) is strictly increasing and differentiable, integration by parts yields

\[
A=-\int_0^1Q'(u)u(1-u)\,du,
\qquad B=-\int_0^1Q'(u)u^2(1-u)\,du.
\]

All boundary terms vanish: \(Q(u)\) grows only as a positive power of \(\log[-\log(1-u)]\) when \(u\uparrow1\), and vanishes at \(u\downarrow0\). The strict inequality \(0<u<1\) and \(Q'(u)>0\) give \(0<|B|<|A|\). Since \(\sigma^2>0\), it follows that \(0<b<a\).

**Step 3: Sharp minimum.** As \(\omega\ge-1-\gamma\) and \(b>0\),

\[
\rho=a\gamma+b\omega\ge-b+(a-b)\gamma\ge-a,
\]

with equality only at \((\gamma,\omega)=(-1,0)\). This is an admissible copula.

**Step 4: Sharp maximum.** Since \(b>0\), every maximum has \(\omega=U(\gamma)\). Set \(t=1+\gamma\in[0,2]\). Using \(9-6\gamma-3\gamma^2=12-3t^2\) gives

\[
a\gamma+bU(\gamma)
=-a+2b+\left(a-\frac b2\right)t+\frac{\sqrt3\,b}{2}\sqrt{4-t^2}.
\]

The last two terms are the scalar product of the vector \(\bigl(a-b/2,\sqrt3 b/2\bigr)\) with a point on the upper semicircle of radius \(2\). Because \(a>b>0\), both coefficients are strictly positive; Cauchy–Schwarz has equality at exactly one point of this semicircle, namely

\[
t_*=\frac{2(2a-b)}{\sqrt{(2a-b)^2+3b^2}}\in(1,2).
\]

Substitution gives the stated sharp upper value and the unique maximizing copula parameters. Since \(\Omega\) is convex and \(\rho\) is affine in its parameters, every value between the extrema is attained. The strict positive corner shortfall follows from \(b>0\) by rationalizing the square-root difference.

## Verification

A reproducibility script, `check.py`, evaluates the defining Chen-quantile integrals under the substitution \(u=1-e^{-y}\), then checks the analytic extremum, feasibility, uniqueness locally and the numerical comparisons for two parameter choices. Run from the directory containing that script with `python3 check.py` (standard library only); its successful terminal line is `CHECK_OK`.

For \((\theta,\beta)=(2,1.5)\), higher-precision independent quadrature (55-decimal-digit arithmetic) yielded

\[
a=0.3222022088524795167\ldots,\qquad
b=0.0958623973370279477\ldots.
\]

The corresponding \(\rho(1,1)=0.4180646061895074645\ldots\), \(\rho_{\max}=0.4426431191991010677\ldots\), and gain \(0.0245785130095936032\ldots\). The standard-library reproducibility checker uses finite quadrature with intentionally looser numerical tolerances; the general extremal identities are proved analytically, not by numerical sampling.

## Relationship to prior work

Huang and Kotz (1984) established the underlying IFGM parameter region and studied maximum correlations for general margins, including the classical uniform example. Those general ingredients are acknowledged as prior art. Chandra et al. (2024) and James et al. (2023/2025 posting) analyze IFGM correlation and reliability with Rayleigh and Lindley margins, respectively. None of the inspected relevant portions supplies the corrected Chen-specific statement addressed here.

The 2026 IFGM–Chen source, Section 3.1, explicitly treats the valid corner \((1,1)\) as giving the maximum Pearson correlation and reports approximately \(0.4181\) for \((\theta,\beta)=(2,1.5)\). The present result makes the **source-specific correction**, derives the precise globally optimizing parameter pair, and shows that the corner is strictly suboptimal for *every* nondegenerate Chen marginal. The source correctly recognizes a non-corner optimum for Kendall's tau in its separate Section 3.2; that calculation does not establish the Pearson maximum.

## Limitations

The original 1984 paper's publisher full text could not be obtained during this literature comparison; only its abstract and accessible technical-report metadata were available. It may contain a broader general optimization argument, so no priority is asserted for the generic semicircle-support calculation or the IFGM admissibility region. The identified numerical and interpretive correction concerns the later, specifically Chen-marginal study. Other Chen parameter combinations, unequal margins, alternative copulas and inferential procedures are outside the claim. The displayed decimal values are numerical quadrature approximations; no machine-checked interval-arithmetic certificate is claimed.

## References

1. M. A. Alawady et al., "Bivariate Chen distribution based on iterated FGM copula: Properties and applications," *AIMS Mathematics* **11** (2026), 5379–5408, DOI: 10.3934/math.2026222; primary MSC 60B12; published 03 March 2026.
2. J. S. Huang and S. Kotz, "Correlation structure in iterated Farlie–Gumbel–Morgenstern distributions," *Biometrika* **71** (1984), 633–636, DOI: 10.1093/biomet/71.3.633; abstract and Stanford technical-report record SOL ONR 340 inspected.
3. N. Chandra, A. James, F. Domma and H. Rehman, "Bivariate iterated Farlie–Gumbel–Morgenstern stress–strength reliability model for Rayleigh margins: Properties and estimation," *Statistical Theory and Related Fields* **8** (2024), 315–334, DOI: 10.1080/24754269.2024.2398987.
4. A. James, N. Chandra and F. Domma, "Reliability Estimation of Dependence Structure System For Huang-Kotz Iterated FGM With Lindley Marginal," *Statistica* **83** (2023), 183–212, DOI: 10.6092/issn.1973-2201/18225; publisher page posted 2025.
