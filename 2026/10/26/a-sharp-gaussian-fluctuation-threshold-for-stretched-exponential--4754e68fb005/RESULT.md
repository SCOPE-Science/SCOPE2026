# A sharp Gaussian-fluctuation threshold for stretched-exponential urn frequencies

## Finding

Fix \(\beta>0\), put \(Z_\beta=\sum_{j\ge1}e^{-j^\beta}\) and \(p_j=Z_\beta^{-1}e^{-j^\beta}\), and let \(N_j(t)\) be independent Poisson random variables with means \(tp_j\). Define the Poissonized occupied-urn count and its variance by
\[
K_\beta(t)=\sum_{j\ge1}\mathbf1_{\{N_j(t)>0\}},\qquad V_\beta(t)=\operatorname{Var} K_\beta(t).
\]
The variance-normalized count converges to a standard Gaussian precisely for \(0<\beta<1\):
\[
\frac{K_\beta(t)-\mathbb E K_\beta(t)}{\sqrt{V_\beta(t)}}\ \Rightarrow\ N(0,1)\quad(t\to\infty)
\qquad\Longleftrightarrow\qquad 0<\beta<1.
\]
In this regime,
\[
V_\beta(t)\sim\frac{\log 2}{\beta}\left(\log\frac{t}{Z_\beta}\right)^{1/\beta-1}.
\]
At \(\beta=1\), logarithmic phase subsequences have discrete integer-valued limits. At \(\beta>1\), there are explicit subsequences with nondegenerate Bernoulli fluctuations: for fixed \(\gamma\in\mathbb R\), with
\[
x_m=m+\frac{\gamma}{\beta m^{\beta-1}},\quad t_m=Z_\beta e^{x_m^\beta},\quad B_\gamma\sim\operatorname{Bernoulli}(1-e^{-e^\gamma}),
\]
the **correctly centered** limit is
\[
\boxed{K_\beta(t_m)-(m-1)\Rightarrow B_\gamma,}
\qquad\text{equivalently}\qquad
\boxed{K_\beta(t_m)-m\Rightarrow B_\gamma-1.}
\]
The integer shift is essential: exactly \(m-1\) lower-index urns, not \(m\), are asymptotically occupied with probability one.

## Assumptions and scope

All statements concern the Poissonized infinite-urn model with fixed positive \(\beta\). The urns are indexed from \(1\), counts are independent with the displayed Poisson means, and all limits let \(t\to\infty\) (or \(m\to\infty\) along the specified subsequence). This theorem does not claim a corresponding de-Poissonization result for fixed sample size, nor a classification of arbitrary index-zero frequency sequences.

## Proof

Write \(L_t=\log(t/Z_\beta)\), \(\lambda_j(t)=e^{L_t-j^\beta}\), and \(I_j(t)=\mathbf1_{\{N_j(t)>0\}}\). Independent Poisson thinning makes the \(I_j(t)\) independent Bernoulli variables with success probabilities \(1-e^{-\lambda_j(t)}\). Thus
\[
V_\beta(t)=\sum_{j\ge1}e^{-\lambda_j(t)}(1-e^{-\lambda_j(t)}).\tag{1}
\]
This is finite for each \(t\), because \(\sum_j\mathbb E I_j(t)\le\sum_jtp_j=t\).

**The Gaussian regime \(0<\beta<1\).** Set \(x_t=L_t^{1/\beta}\) and \(w_t=(\beta x_t^{\beta-1})^{-1}=\beta^{-1}L_t^{1/\beta-1}\). Then \(w_t\to\infty\), and, uniformly for bounded \(u\),
\[
\lambda_{\lfloor x_t+w_tu\rfloor}(t)\to e^{-u}.
\]
Applying a transition-window Riemann sum to (1), with the summand bounded by \(\lambda\) for small \(\lambda\) and by \(e^{-\lambda}\) for large \(\lambda\), yields
\[
\frac{V_\beta(t)}{w_t}\to\int_{-\infty}^{\infty}e^{-e^{-u}}(1-e^{-e^{-u}})\,du
=\int_0^\infty\frac{e^{-v}-e^{-2v}}{v}\,dv=\log2.
\]
The variance therefore diverges with the asserted sharp asymptotic. Each Bernoulli third absolute centered moment is at most its variance; hence the Lyapunov ratio for the independent centered occupancies is at most \(V_\beta(t)^{-1/2}\to0\). The same conclusion follows by finite truncation and an \(L^2\) tail bound. The central limit theorem gives the Gaussian limit.

**The critical regime \(\beta=1\).** Put \(m_t=\lfloor L_t\rfloor\) and \(\phi_t=L_t-m_t\). Along any sequence with \(\phi_t\to\phi\in[0,1]\), urn \(m_t+k\) has mean \(e^{\phi_t-k}\). Shifting the index and using summability of vacancies for \(k\le0\) and of occupancies for \(k\ge1\), one obtains
\[
K_1(t)-m_t\Rightarrow
Y_\phi:=\sum_{k\le0}(B_k-1)+\sum_{k\ge1}B_k,
\]
where the \(B_k\) are independent Bernoulli variables with parameters \(1-e^{-e^{\phi-k}}\). Both one-sided series are almost surely finite, and the limiting variance is finite and strictly positive. Every such centered limit is integer-valued; after variance standardization it remains discrete, so convergence to a standard Gaussian along all \(t\) is impossible.

**The sparse-transition regime \(\beta>1\).** Fix \(\gamma\in\mathbb R\) and use \(x_m,t_m\) from the finding. Expansion gives \(\lambda_m(t_m)\to e^\gamma\), hence \(I_m(t_m)\Rightarrow B_\gamma\). Furthermore \(\lambda_{m-1}(t_m)\to\infty\) faster than \(\log m\), so
\[
\Pr(\text{one of urns }1,\ldots,m-1\text{ is empty})
\le (m-1)e^{-\lambda_{m-1}(t_m)}\to0.
\]
Since the gaps \((j+1)^\beta-j^\beta\) increase and diverge, the upper tail satisfies
\[
\Pr(\text{an urn }j>m\text{ is occupied})
\le\sum_{j>m}\lambda_j(t_m)
\le\frac{\lambda_{m+1}(t_m)}{1-e^{-((m+2)^\beta-(m+1)^\beta)}}\to0.
\]
Thus the occupied count equals \((m-1)+I_m(t_m)\) with probability tending to one, proving both centered Bernoulli limits in the finding. Along this subsequence \(V_\beta(t_m)\to p_\gamma(1-p_\gamma)>0\), where \(p_\gamma=1-e^{-e^\gamma}\). Consequently the variance-standardized count tends to a non-Gaussian two-point law, excluding a full-sequence Gaussian limit. This proves the if-and-only-if assertion.

## Verification and correction scope

The proof uses the exact Bernoulli variance, a Frullani integral, the Lyapunov criterion and explicit tightness of critical/subcritical index windows. The crucial integer bookkeeping in the last step is \(\sum_{j<m}I_j=m-1\), so a Bernoulli limit requires centering by \(m-1\); centering by \(m\) yields \(B_\gamma-1\). No finite numerical trial is used as proof of the infinite-index assertions.

## Relationship to prior work

Karlin's classical infinite-urn central limit framework and subsequent index-zero occupancy CLTs provide prior general methods; Gaussianity from diverging independent Bernoulli variance is not new. Chebunin and Zuyev (2020/2022) analyze functional occupancy limits under regular variation, while Abebe, Chebunin and Kovalevskii (2026) obtain multivariate/functional results whose displayed theorems assume a positive regular-variation index. The present frequency-counting function has index zero, and the assessed increment is the explicit stretched-exponential three-regime classification, sharp variance constant, phase-indexed boundary limit and tuned Bernoulli obstruction with its correct centering. This comparison does not exclude an equivalent older treatment of geometric frequencies or index-zero occupancy fluctuations.

## Limitations

This theorem is restricted to fixed \(\beta>0\) and independently Poissonized infinite urns. At \(\beta=1\) the limit depends on the fractional logarithmic phase; for \(\beta>1\) the non-Gaussian obstruction is proved along particular subsequences. The conclusions are not automatically transferred to fixed-sample occupancy counts or more general stretched-exponential distributions.

## References

1. B. Abebe, M. Chebunin, A. Kovalevskii, *Limit theorems for a class of random outer measures in infinite urn schemes*, arXiv:2602.13938v1 (2026).
2. M. Chebunin, S. Zuyev, *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*, Journal of Theoretical Probability 35 (2022), 1–19, DOI:10.1007/s10959-020-01053-6.
3. S. Karlin, *Central Limit Theorems for Certain Infinite Urn Schemes*, Indiana University Mathematics Journal 17 (1968), 373–401, DOI:10.1512/iumj.1968.17.17020.
