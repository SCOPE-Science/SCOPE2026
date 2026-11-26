# Logarithmic rare-Friedman crossover for a mixed two-colour Pólya urn

## Finding

The logarithmic rare-rule crossover persists when the two rules add **unequal** total numbers of balls. Let the Pólya rule add \(c\) balls of the drawn colour, and the Friedman rule add \(a\) balls of that colour and \(b\) of the opposite colour, where \(a+b\ne c\). In a row of \(N\) draws, use the Friedman rule independently with probability \(\varepsilon_N\) per draw. Assume \(\varepsilon_N\to0\) and \(\varepsilon_N\log N\to\lambda\in[0,\infty]\). If \(Z^{(N)}_N\) is the final proportion of colour 1, then
\[
Z^{(N)}_N\Rightarrow\tfrac12+d(B-\tfrac12),\qquad
B\sim\operatorname{Beta}(y_1/c,y_2/c),\qquad d=e^{-2b\lambda/c},
\]
with \(d=0\) for \(\lambda=\infty\). In particular, the random total does not change the limiting contraction coefficient. Writing \(\alpha=y_1/c\), \(\beta=y_2/c\), the limiting mean is \(1/2+d(\alpha/(\alpha+\beta)-1/2)\) and the limiting variance is \(d^2\alpha\beta/[(\alpha+\beta)^2(\alpha+\beta+1)]\).

## Assumptions and scope

The initial counts \(y_1,y_2\) are fixed positive integers; \(a\ge0\), \(b,c\ge1\) are fixed integers, and \(a+b\ne c\). Draw a ball uniformly and replace it before adding balls. Rule indicators within each row are independent Bernoulli variables of parameter \(\varepsilon_N\in[0,1]\), independent of all drawing uniforms. The two rules add different numbers in total, but for a given rule the total increment does not depend on the colour drawn. The conclusion concerns the endpoint distribution and bounded moments, not an almost-sure limit across rows.

## Proof

Within a row let \(\xi_j\) indicate the Friedman rule, \(I_j\) indicate the drawing of colour 1, and \(R_j=\sum_{i=1}^j\xi_i\). Use \(T_j\) for total size, \(Z_j\) for the proportion of colour 1, \(V_j=Z_j-1/2\), and \(\delta=a+b-c\). Then
\[
T_j=y_1+y_2+cj+\delta R_j,\qquad
V_j=\left(1-2b\xi_j/T_j\right)V_{j-1}+M_j,\qquad
M_j=\frac{c(1-\xi_j)+(a-b)\xi_j}{T_j}(I_j-Z_{j-1}).
\]
Indeed the addition to colour 1 is \(cI_j\) or \(b+(a-b)I_j\), respectively. Condition on the entire rule sequence. The denominators are then deterministic and \(M_j\) are martingale differences for the filtration of drawing uniforms. With \(m=\min(c,a+b)>0\), \(M=\max(c,a+b)\), we have \(mj\le T_j\le T_0+Mj\), so \(|M_j|\le C/j\) with a constant independent of the row.

Choose a fixed \(K\) with \(m(K+1)>2b\) and write \(D_{u,v}=\prod_{j=u+1}^v(1-2b\xi_j/T_j)\) for \(v\ge u\ge K\). All its factors belong to \((0,1]\). Iterating the recursion gives
\[
V_N=D_{K,N}V_K+\sum_{j=K+1}^N D_{j,N}M_j.
\]
The coefficients in the sum are deterministic conditional on the rules. Orthogonality and the bound on \(M_j\) give an unconditional squared \(L^2\) error bound \(C^2\sum_{j>K}j^{-2}\le C^2/K\), uniform in \(N>K\).

For finite \(\lambda\), the weighted Bernoulli sum \(\sum_{j=K+1}^N\xi_j/j\) has mean tending to \(\lambda\) and variance at most \(\varepsilon_N\sum_{j>K}j^{-2}\to0\). To handle the random totals, use
\[
\left|T_j^{-1}-(cj)^{-1}\right|\le\frac{T_0+|\delta|R_j}{cmj^2},\qquad
\mathbb E[\xi_j R_j]=\varepsilon_N+(j-1)\varepsilon_N^2.
\]
The expected absolute error after weighting by \(\xi_j\) and summing is \(O(\varepsilon_N+\varepsilon_N^2\log N)=o(1)\). Thus \(\sum_{j>K}\xi_j/T_j\to\lambda/c\) in probability, with all sums ending at \(N\). The expected sum of \((\xi_j/T_j)^2\) is at most \(m^{-2}\varepsilon_N\sum_{j>K}j^{-2}\to0\). Expanding the log factors, with a uniform quadratic remainder since \(2b/[m(K+1)]<1\), gives \(D_{K,N}\to d\) in probability. If \(\lambda=\infty\), the weighted Bernoulli sum instead diverges in probability by the same variance bound. Now \(T_j\le(T_0+M)j\) makes \(\sum_{j>K}\xi_j/T_j\) diverge in probability, and \(1-x\le e^{-x}\) gives \(D_{K,N}\to0\). No finite-window error bound in \(\varepsilon_N^2\log N\) is needed for this case.

Couple each row and a pure Pólya urn using identical drawing uniforms. At the fixed time \(K\) the proportions agree except on an event of probability at most \(K\varepsilon_N\). By product convergence in probability and boundedness, \(D_{K,N}V_K\) thus converges in distribution to \(d(Z^{\mathrm P}_K-1/2)\). For each bounded Lipschitz test function the remaining innovation sum changes its expectation by at most the Lipschitz constant times \(C/\sqrt K\). The classical pure Pólya proportion converges to the stated Beta random variable; sending \(K\) to infinity proves the endpoint claim. Proportions are bounded in \([0,1]\), so the first two moments converge. The stated formulas follow from the Beta mean and variance.

## Verification

The proof controls the random denominator, its dependence on the rule at the same step, and the conditional drawing noise. The finite exact transition and moment checks in `checker.py` are supplementary; the attached `checker_output.txt` reports `ALL_ASSERTIONS_PASSED 3439`. The numerical large-row diagnostics in that output are for the balanced comparison model, not direct numerical tests of the unequal-total limit.

## Relationship to prior work and limitations

The endpoint law in the equal-total setting is not claimed as new. *Logarithmic-time Dirichlet crossover in vanishing Pólya–Friedman urns* proves a stronger coupled path limit with more colours when both rules add the same total and the same-colour Friedman addition is positive. Its two-colour specialization implies the same endpoint formula and both limiting regimes there. The difference here is the unequal total: the denominator is random and correlated with the damping indicator. The finite-window comparison uses \(\mathbb E[\xi_j R_j]\), not deterministic balance or a substitution of the mean replacement matrix. The result is only for the two-colour endpoint and gives no rate or process limit. Shi, Yin and Miao treat fixed mixture probabilities in the same two-rule family; fixed positive probabilities do not yield the triangular window here. Alves and Rosales give fixed-positive-probability equalization in their mixture model. This comparison does not establish exhaustive historical priority.

## References

1. *Logarithmic-time Dirichlet crossover in vanishing Pólya–Friedman urns*, [Resultary record](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-logarithmic-time-dirichlet-crossover-in-vanishing-p-lya-friedman--f9652b484b0a).
2. J. Shi, Q. Yin, and Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, [arXiv:2605.26669v1](https://arxiv.org/html/2605.26669v1).
3. R. Alves and R. A. Rosales, *Friedman vs Pólya*, [arXiv:2502.16768v2](https://arxiv.org/html/2502.16768v2).
