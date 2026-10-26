# A sharp Gaussian-fluctuation threshold for stretched-exponential urn frequencies

## Finding
Let \(Z_\beta=\sum_{j=1}^{\infty}e^{-j^\beta}\) and \(p_j=Z_\beta^{-1}e^{-j^\beta}\), where \(\beta>0\). In the Poissonized infinite-urn scheme, let \(N_j(t)\) be independent \(\operatorname{Poisson}(tp_j)\) counts and define
\[
K_\beta(t)=\sum_{j\ge1}\mathbf 1_{\{N_j(t)>0\}},\qquad V_\beta(t)=\operatorname{Var}K_\beta(t).
\]
Then
\[
\frac{K_\beta(t)-\mathbb E K_\beta(t)}{\sqrt{V_\beta(t)}}\Rightarrow N(0,1)\quad(t\to\infty)
\]
if and only if \(0<\beta<1\). For this regime,
\[
V_\beta(t)\sim\frac{\log 2}{\beta}\left(\log\frac{t}{Z_\beta}\right)^{1/\beta-1}.
\]
At \(\beta=1\), centering by \(\lfloor\log(t/Z_1)\rfloor\) gives phase-indexed integer-valued subsequential limits. For \(\beta>1\), explicit subsequences give a nondegenerate Bernoulli limit after centering, so a full-sequence Gaussian fluctuation limit is impossible.

## Assumptions and scope
The parameter \(\beta\) is fixed and positive. The normalization \(Z_\beta\) is finite, and the urn counts at time \(t\) are independent Poisson random variables with means \(tp_j\). The result concerns this Poissonized model only; it does not assert a de-Poissonization theorem for a fixed number of balls.

## Proof
Put \(L_t=\log(t/Z_\beta)\), \(\lambda_j(t)=tp_j=e^{L_t-j^\beta}\), and \(I_j(t)=\mathbf 1_{\{N_j(t)>0\}}\). Then the \(I_j(t)\) are independent Bernoulli variables with success probabilities \(q_j(t)=1-e^{-\lambda_j(t)}\), and
\[
V_\beta(t)=\sum_{j\ge1}e^{-\lambda_j(t)}(1-e^{-\lambda_j(t)}).
\tag{1}
\]
The sum is finite for every fixed \(t\), since \(\mathbb E K_\beta(t)\le\sum_j\lambda_j(t)=t\).

Suppose \(0<\beta<1\). Define the transition location and width by
\[
x_t=L_t^{1/\beta},\qquad w_t=(\beta x_t^{\beta-1})^{-1}=\frac1\beta L_t^{1/\beta-1}.
\]
Then \(w_t\to\infty\), and for each bounded real \(u\), Taylor expansion gives
\[
\lambda_{\lfloor x_t+w_tu\rfloor}(t)\longrightarrow e^{-u}.
\]
A dominated Riemann-sum argument applied to (1), with the small-\(\lambda\) bound \(e^{-\lambda}(1-e^{-\lambda})\le\lambda\) and the large-\(\lambda\) bound \(e^{-\lambda}(1-e^{-\lambda})\le e^{-\lambda}\), yields
\[
\frac{V_\beta(t)}{w_t}\longrightarrow\int_{-\infty}^{\infty}e^{-e^{-u}}(1-e^{-e^{-u}})\,du
=\int_0^\infty\frac{e^{-v}-e^{-2v}}v\,dv=\log2.
\]
This proves the displayed variance asymptotic. For a Bernoulli variable with parameter \(q\), its third absolute centered moment is \(q(1-q)((1-q)^2+q^2)\le q(1-q)\). Consequently the sum of third absolute centered moments divided by \(V_\beta(t)^{3/2}\) is at most \(V_\beta(t)^{-1/2}\to0\). Lyapunov's condition proves the Gaussian limit for \(0<\beta<1\).

Now let \(\beta=1\), set \(m_t=\lfloor L_t\rfloor\), and write \(\phi_t=L_t-m_t\). Along any sequence with \(\phi_t\to\phi\in[0,1]\), the urn at index \(m_t+k\) has mean \(\lambda_{m_t+k}(t)=e^{\phi_t-k}\). Thus the centered count \(K_1(t)-m_t\) converges in distribution to
\[
Y_\phi=\sum_{k\le0}(B_k-1)+\sum_{k\ge1}B_k,
\]
where the \(B_k\) are independent Bernoulli variables with parameters \(1-e^{-e^{\phi-k}}\). The sum is almost surely well-defined: the probabilities of a vacancy for \(k\le0\) and of an occupied urn for \(k\ge1\) are summable. Its variance is finite and positive. Hence each phase limit is discrete and non-Gaussian, ruling out a full-sequence Gaussian limit at \(\beta=1\).

Finally suppose \(\beta>1\). For fixed \(\gamma\in\mathbb R\), let
\[
x_m=m+\frac{\gamma}{\beta m^{\beta-1}},\qquad t_m=Z_\beta e^{x_m^\beta}.
\]
Then \(\lambda_m(t_m)\to e^\gamma\). For every \(j<m\), \(\lambda_j(t_m)\ge\lambda_{m-1}(t_m)\to\infty\) so rapidly that the probability any such urn is empty tends to zero. For \(j>m\), the sum \(\sum_{j>m}\lambda_j(t_m)\to0\), because the successive ratios are bounded by \(e^{-((m+2)^\beta-(m+1)^\beta)}\to0\). Therefore
\[
K_\beta(t_m)-m\Rightarrow B_\gamma,\qquad B_\gamma\sim\operatorname{Bernoulli}(1-e^{-e^\gamma}).
\]
The variance converges to the positive Bernoulli variance, so the centered, variance-normalized subsequence converges to a two-point law, not a standard normal law. This proves the claimed sharp boundary.

## Verification
Equation (1) follows directly from independent Poisson occupancies. The variance constant is the Frullani integral \(\int_0^\infty(e^{-v}-e^{-2v})v^{-1}\,dv=\log2\). The Gaussian regime uses Lyapunov's condition; the two boundary regimes are established by explicit subsequential distributional limits. No finite experiment is used as an infinite proof.

## Relationship to prior work
Abebe, Chebunin, and Kovalevskii study central and functional limit theorems for infinite-urn random outer measures. Their stated Poissonized central limit theorem uses a regular-variation index \(\theta\in(0,1)\), and their functional theorem uses \(\theta\in(0,1]\). For the present family, the counting function satisfies \(\#\{j:p_j\ge x^{-1}\}\sim(\log(x/Z_\beta))^{1/\beta}\), which has regular-variation index zero. The same paper notes that earlier work treats a subclass of this index-zero regime. The contribution here is the explicit transition at \(\beta=1\), including the phase-indexed and Bernoulli subsequential limits when Gaussian fluctuations fail.

## Limitations
The theorem is for Poissonized counts only. It does not establish a corresponding fixed-sample-size limit, and it does not classify all slowly varying occupancy-frequency sequences. At \(\beta=1\), the subsequential law depends on the fractional part of \(\log(t/Z_1)\); for \(\beta>1\), the stated obstruction is along tuned subsequences.

## References
1. B. Abebe, M. Chebunin, and A. Kovalevskii, “Limit theorems for a class of random outer measures in infinite urn schemes,” arXiv:2602.13938v1, first posted 15 February 2026.
2. M. Chebunin and S. Zuyev, “Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models,” *Journal of Theoretical Probability* 35 (2022), 1–19; first published online 23 November 2020. DOI: 10.1007/s10959-020-01053-6.
3. S. Karlin, “Central Limit Theorems for Certain Infinite Urn Schemes,” *Indiana University Mathematics Journal* 17(4) (1968), 373–401. DOI: 10.1512/iumj.1968.17.17020.
