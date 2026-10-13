# A bounded Lambert-W VaR surrogate for a heavy-tailed log-adjusted Fréchet model

## Finding

For the log-adjusted polynomial Fréchet (LAPFr) model of Aljadani (2025), the Lambert-W expression displayed as Eq. (13), explicitly described there as an approximate high-confidence value-at-risk (VaR) formula, has the *opposite* asymptotic regime: it is relatively accurate at confidence levels tending to zero, but **cannot** be a high-confidence quantile approximation. At any fixed admissible parameters, it remains bounded as the nominal confidence level tends to one, although the true VaR diverges. Its limiting actual coverage lies strictly between \(\log 2\) and \(\log(1+\log 2)/\log 2 = 0.7597073881389085\ldots\). The latter bound is sharp over the model's positive generator parameter. Thus the proposed high-confidence surrogate can asymptotically deliver **less than 76% actual coverage** at nominal confidence tending to 100%. This is an exact characterization of Eq. (13), not a claim about implementations that numerically invert the original CDF.

## Assumptions and scope

Fix real parameters \(\alpha>0\), \(\theta>0\), and \(\beta>0\). For \(x>0\), set
\[
g(x)=\exp\!\left[-(\alpha/x)^\theta\right],\qquad
F(x)=\frac{\log(1+g(x))\exp[\beta(g(x)-1)]}{\log 2}.
\]
This is Eq. (3) of the source, with its normalization made explicit. Define the true quantile \(Q(q)=F^{-1}(q)\) for \(0<q<1\). The source's Eq. (13), obtained by replacing \(\log(1+g)\) by \(g\), is
\[
\widetilde Q(q)=\alpha\left[-\log z_\beta(q)\right]^{-1/\theta},\quad
z_\beta(q)=\frac{W_0(\beta q e^\beta\log 2)}{\beta},
\]
where \(W_0\) is the principal real Lambert-W branch. The arguments below involve exact real arithmetic and the full parameter domain above. No lower-tail or high-confidence approximation is *assumed* in the proof.

## Proof

**Step 1: exact achieved coverage and strict underestimation.** The function \(g:(0,\infty)\to(0,1)\) is strictly increasing and onto. The generator \(h_\beta(t)=\log(1+t)e^{\beta(t-1)}/\log 2\) is strictly increasing from zero to one on \(0<t<1\). The surrogate equation is \(z_\beta(q)e^{\beta(z_\beta(q)-1)}=q\log 2\); hence \(z_\beta(q)\in(0,1)\) and substitution into the exact CDF gives
\[
\boxed{F(\widetilde Q(q))=q\,\frac{\log(1+z_\beta(q))}{z_\beta(q)}<q.}
\]
Since \(\log(1+t)<t\) for all \(t>0\), strict monotonicity of \(F\) gives \(\widetilde Q(q)<Q(q)\) for every \(q\in(0,1)\). No numerical error or parameter fitting is involved.

**Step 2: saturation and a universal sharp coverage interval.** The increasing surrogate root converges to the unique \(z_\beta\in(0,1)\) satisfying
\[
\log z_\beta+\beta(z_\beta-1)=\log(\log 2).
\]
The left-hand side at \(z=\log 2\) is less than its right-hand side, and at \(z=1\) it is greater; therefore \(\log 2<z_\beta<1\). Consequently
\[
\widetilde Q(q)\longrightarrow \alpha[-\log z_\beta]^{-1/\theta}<\infty,
\quad F(\widetilde Q(q))\longrightarrow c_\beta:=\frac{\log(1+z_\beta)}{z_\beta}.
\]
The ratio \(r(z)=\log(1+z)/z\) is strictly decreasing on \((0,1]\): indeed \(z^2r'(z)=z/(1+z)-\log(1+z)<0\). Hence
\[
\boxed{\log 2<c_\beta<\frac{\log(1+\log 2)}{\log 2}=0.7597073881389085\ldots.}
\]
Implicit differentiation yields \(dz_\beta/d\beta=(1-z_\beta)/(1/z_\beta+\beta)>0\). As \(\beta\downarrow0\), \(z_\beta\to\log2\); as \(\beta\to\infty\), \(z_\beta\to1\). The bounds are therefore sharp, but neither is attained for finite \(\beta>0\). This failure is uniform in \(\alpha\) and \(\theta\).

**Step 3: divergence of true VaR and its rate.** Differentiating \(h_\beta\) at its right endpoint gives
\[
h_\beta'(1)=K_\beta:=\beta+\frac{1}{2\log2}>0.
\]
Since \(1-g(x)\sim(\alpha/x)^\theta\) as \(x\to\infty\),
\[
1-F(x)\sim K_\beta(\alpha/x)^\theta,
\qquad Q(q)\sim\alpha\left(\frac{K_\beta}{1-q}\right)^{1/\theta} \quad(q\uparrow1).
\]
Therefore
\[
\boxed{\frac{\widetilde Q(q)}{Q(q)}\sim\left[\frac{1-q}{K_\beta(-\log z_\beta)}\right]^{1/\theta}\longrightarrow0.}
\]
In contrast, as \(q\downarrow0\), both the exact root \(h_\beta^{-1}(q)\) and the surrogate root \(z_\beta(q)\) are asymptotic to \(q e^\beta\log2\). Their negative logarithms are asymptotic, so \(\widetilde Q(q)/Q(q)\to1\). Thus replacing \(\log(1+g)\) by \(g\) is legitimate only in the *lower* baseline-CDF regime \(g\to0\), not in the high-VaR regime \(g\to1\).

**Step 4: exact repair.** For each \(0<q<1\), determine the unique \(t\in(0,1)\) solving
\[
\frac{\log(1+t)e^{\beta(t-1)}}{\log2}=q,
\]
for example by bisection with endpoints zero and one. Then \(Q(q)=\alpha[-\log t]^{-1/\theta}\) is the exact VaR. This repair uses the same LAPFr model and needs no parameter modification.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently solves the exact and Lambert-surrogate scalar equations by monotone bisection, checks the coverage identity, and evaluates a representative extreme-level comparison. With \(\alpha=\theta=\beta=1\) and nominal \(q=0.99\), the surrogate is \(\widetilde Q=5.0654970551\ldots\), its actual CDF coverage is \(0.7227998524\ldots\), and the exact quantile is \(Q=171.0287464965\ldots\). An apparent 99% risk threshold thus corresponds to approximately 72.28% model coverage if Eq. (13) itself is used. This calculation illustrates, but is not the proof of, the universal result.

Reproduction: from the directory containing this document and `verify.py`, run `python3 verify.py`. No network access, source PDF, private data, or nonstandard packages are required.

## Relationship to prior work

The source's Section 3.1 (pp. 27022–27023) derives Eq. (13) by the replacement \(\log(1+g)\approx g\), calls it an approximation, but explicitly describes it as valid for high confidence levels such as \(q\ge0.90\). The source simultaneously notes that \(g\to1\) in the far upper tail. The present result respects the source's qualification that Eq. (13) is an approximation: it proves that this particular approximation is not asymptotically valid in its *claimed* high-confidence regime, supplies exact actual-coverage and divergence formulae, and identifies the opposite lower-confidence regime where relative accuracy does hold. A related 2025 log-exponentiated polynomial family article explicitly advocates numerical CDF inversion but concerns a different generator and does not provide this source-specific coverage envelope. Basic monotone inversion and the Lambert-W identity are established tools, not claimed as new.

## Limitations

No statement is made that the full LAPFr distribution is invalid, that the published empirical values were necessarily computed from Eq. (13), or that a correctly implemented numerical inverse suffers this error. The theorem covers the printed Eq. (13) interpreted as a VaR surrogate for the stated distribution, at all \(\alpha,\theta,\beta>0\). It proves mathematical undercoverage and asymptotics, not a statistical sampling-error bound or a numerical-optimization result. Priority over unindexed corrections cannot be certified by a literature search alone.

## References

1. A. Aljadani (2025), *A new log-adjusted polynomial Fréchet model for heavy-tailed PORT-VaR analysis and one-step-ahead-VaR forecasting in finance and economics*, AIMS Mathematics **10**(11), 27016–27043, DOI:10.3934/math.20251187, especially Eqs. (1)–(3), (13) and Section 3.1. Publisher full-text PDF: https://www.aimspress.com/aimspress-data/math/2025/11/PDF/math-10-11-1187.pdf
2. A. M. AboAlkhair, G. G. Hamedani, N. A. Ahmed, M. Ibrahim, M. A. Zayed, H. M. Yousof (2025), *A New G Family: Properties, Characterizations, Different Estimation Methods and PORT-VaR Analysis for U.K. Insurance Claims and U.S. House Prices Data Sets*, Mathematics **13**(19), 3097, DOI:10.3390/math13193097, Section 2.2 (numerical quantile inversion). https://doi.org/10.3390/math13193097
