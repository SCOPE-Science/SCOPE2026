# The scaling constant of the Shannon entropy–exceedance crossover for uniform spacings

## Finding

Let \(m\ge2\) be any integer, and let \((X_1,\ldots,X_m)\) be the spacings of \(m-1\) independent uniform points of \([0,1]\), including the two boundary spacings. Write \(H_m=-\sum_{i=1}^m X_i\log X_i\) for Shannon spacing entropy and \(N_m(t)=\sum_{i=1}^m\mathbf1\{X_i>t\}\) for the exceedance count. Let \(t_m\in(0,1)\) denote the unique covariance crossover threshold (see the finite-sample lemma below). The entropy-specific result is that, for each fixed \(c>0\),

\[
\lim_{m\to\infty}\operatorname{Cov}(H_m,N_m(c/m))=F(c),\qquad m t_m\longrightarrow c_*=1.700321026132689\ldots,
\]

where \(c_*\) is the unique positive zero of

\[
F(c)=e^{-c}[(c+1)(2-\gamma-\log c)-2]-E_1(c),\qquad E_1(c)=\int_c^\infty\frac{e^{-u}}u\,du,
\]

and \(\gamma\) is Euler's constant. The limiting covariance is positive for \(0<c<c_*\) and negative for \(c>c_*\). The crossover is at about \(1.70\) times the mean spacing instead of \(2\) times the mean spacing as for Greenwood's quadratic concentration statistic. For example, for the threshold \(1.8/m\), the concentration score \(\log m-H_m\) has positive covariance with the count, while the quadratic score has negative covariance with the count, for all sufficiently large \(m\).

## Assumptions and scope

All logarithms are natural, and the convention \(0\log0=0\) is used. The joint spacing distribution is \(\operatorname{Dirichlet}(1,\ldots,1)\), so every spacing is positive almost surely and their sum is one. A threshold \(t\) is deterministic; statements hold for every integer \(m\ge2\) and every real \(t\in(0,1)\). The asymptotic assertion concerns \(m\to\infty\) in this same family. No independence of \(H_m\) and \(N_m(t_m)\) is asserted.

## Proof

**Conditional mean.** Let \(\mathsf H_m=\sum_{j=1}^m1/j\), \(\mu_m=\mathsf H_m-1\), and \(a_{m-1}=\mathsf H_{m-1}-1\). The entropy mean of a uniform Dirichlet vector of length \(m\) is \(\mu_m\), as follows from the beta marginal or differentiating its moments. Given \(X_1=x\), the normalized residual vector has an independent uniform Dirichlet law with \(m-1\) coordinates. Therefore

\[
q_m(x):=\mathbb E[H_m\mid X_1=x]=-x\log x-(1-x)\log(1-x)+(1-x)a_{m-1}.
\]

The centered function \(g_m(x)=q_m(x)-\mu_m\) satisfies \(g_m(0)=-1/m<0\), \(g_m(1)=-\mu_m<0\), and

\[
g_m''(x)=-\frac1x-\frac1{1-x}<0\qquad(0<x<1).
\]

Since the beta marginal density is \(f_m(x)=(m-1)(1-x)^{m-2}\), the tower property gives \(\int_0^1g_m(x)f_m(x)\,dx=0\). Strict concavity, negative endpoints, and zero mean imply that \(g_m\) is positive somewhere and has exactly two interior roots \(a_m<b_m\); its sign is negative on the two outer intervals and positive between the roots.

**Finite-sample crossover lemma.** By exchangeability and the conditional-mean identity,

\[
C_m(t):=\operatorname{Cov}(H_m,N_m(t))
=m(m-1)\int_t^1 g_m(x)(1-x)^{m-2}\,dx,
\]

with \(C_m(0)=C_m(1)=0\) and \(C_m'(t)=-m f_m(t)g_m(t)\). Thus \(C_m\) increases from zero up to \(a_m\), strictly decreases between \(a_m\) and \(b_m\), and increases from \(b_m\) to zero. In particular \(C_m(a_m)>0\) and \(C_m(b_m)<0\), so there is exactly one zero \(t_m\in(a_m,b_m)\), with positive covariance below \(t_m\) and negative covariance above \(t_m\). For \(m=2\), \(N_2(1/2)=1\) almost surely because exactly one of the two continuously distributed spacings exceeds \(1/2\); uniqueness yields \(t_2=1/2\).

**Limit of the threshold.** Fix \(u>0\). The conditional-mean formula gives

\[
m g_m(u/m)=u(\log m-\log u-a_{m-1})-(m-u)\log(1-u/m)-1
\longrightarrow \phi(u):=u(2-\gamma-\log u)-1.
\]

Changing variables in the covariance formula gives

\[
C_m(c/m)=\frac{m-1}{m}\int_c^m[m g_m(u/m)](1-u/m)^{m-2}\,du
\longrightarrow \int_c^\infty\phi(u)e^{-u}\,du=:F(c)
\]

for each fixed \(c>0\). For completeness, if \(m\ge4\), then \((1-u/m)^{m-2}\le e^{-u/2}\) and \(-(m-u)\log(1-u/m)\le u\). The quantity \(\log m-a_{m-1}\) is uniformly bounded. Consequently, for \(u\ge c\) the integrand is bounded in absolute value by a fixed multiple of \(e^{-u/2}(1+u+u|\log u|)\), which is integrable. Dominated convergence justifies the limit.

The function \(\phi\) is strictly concave on \((0,\infty)\) because \(\phi''(u)=-1/u\). Its endpoint values satisfy \(\phi(0+)=-1\), \(\phi(1)=1-\gamma>0\), and \(\phi(u)\to-\infty\). It therefore has exactly two positive roots and sign sequence negative, positive, negative. Also \(F(0+)=\mathbb E[\phi(U)]=0\) for \(U\sim\operatorname{Exp}(1)\), as follows from \(\mathbb E U=1\) and \(\mathbb E[U\log U]=1-\gamma\). Because \(F'(c)=-e^{-c}\phi(c)\) and \(F(c)\to0\) at infinity, the same three-phase derivative argument as above shows that \(F\) has exactly one positive zero \(c_*\), with \(F(c)>0\) below it and \(F(c)<0\) above it. Integration by parts yields the displayed expression in terms of \(E_1\). For arbitrary fixed \(c_-<c_*<c_+\) with \(c_->0\), the pointwise covariance limits imply \(C_m(c_-/m)>0\) and \(C_m(c_+/m)<0\) for all sufficiently large \(m\). Uniqueness places \(m t_m\) between \(c_-\) and \(c_+\), hence \(m t_m\to c_*\).

## Verification

The accompanying standalone `verify_entropy.py` evaluates the exact beta integral, checks its sign on both sides of the unique numerical root for numerous sample sizes, compares finite thresholds to the asymptotic expression, and independently simulates Dirichlet vectors using normalized exponential draws. The supplied `requirements.txt` specifies numerical dependencies. The script is corroboration only: the infinite-range uniqueness and asymptotic assertions follow from the analytic argument above.

## Relationship to prior work

Slud (1978) analyzes Shannon partition entropy and maximum-spacing asymptotics. Bieniek and Szynal (2008) derive exact partition-entropy moments and convergence properties. Their inspected passages address marginal entropy quantities rather than the explicit limiting mixed covariance \(F\). Joint spacing limit theory provides a possible alternative route to a mixed covariance; here it is obtained directly from the finite beta integrals.

The [universal one-switch covariance law for large spacings and convex spacing tests](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-universal-one-switch-covariance-law-for-large-spacings-and-con--8cec2684e10a/RESULT.md) proves the finite switch for strictly convex \(C^1\) summands. Its conditional-simplex proof also applies to \(f(x)=x\log x\) with \(f(0)=0\): near \(t=0\) the coordinates of \(t e_1+(1-t)Y\) are bounded below by \(Y_j/2\), so the differentiated integrands are dominated by a constant plus \(\sum_j|\log Y_j|\), which is integrable. Negating the statistic gives the finite entropy switch. That switch is used here as a lemma, not as a separate contribution. The cited law gives an asymptotic correlation for the quadratic score, not the entropy-specific \(F\) or its zero. The exact quadratic crossover \(2/(m+2)\) also appears in the [Greenwood–exceedance covariance result](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-sharp-greenwood-exceedance-covariance-crossover-for-dirichlet--178c0a43180a/RESULT.md).

## Limitations

The asymptotic formula concerns uniform spacings and deterministic thresholds \(c/m\) with fixed \(c>0\). It does not extend here to general Dirichlet parameters, nonuniform point sampling, or other entropy functionals. The comparison with older specialist spacing literature is not exhaustive, and an equivalent earlier formulation may exist. Numerical checks do not constitute a proof of any infinite statement. A zero covariance does not imply independence.

## References

1. E. V. Slud (1978), "Entropy and Maximal Spacings for Random Partitions," *Z. Wahrscheinlichkeitstheorie verw. Gebiete* **41**, 341–352. DOI: 10.1007/BF00533604.
2. M. Bieniek and D. Szynal (2008), "On entropies for random partitions of the unit segment," *Kybernetika* **44**(1), 75–94. https://www.kybernetika.cz/content/2008/1/75/paper.pdf.
3. G. R. Shorack and J. A. Wellner (1986), *Empirical Processes with Applications to Statistics*, Wiley, chapters on uniform spacings (general background).
