# Logarithmic rare-Friedman crossover for a mixed two-colour Pólya urn

## Finding

For each integer \(N\ge 1\), run a two-colour Pólya–Friedman urn for exactly \(N\) draws, with an independently selected Friedman rule at each step having probability \(\varepsilon_N\). The rule probability is constant within a run but may vary between runs. Suppose
\[
\varepsilon_N\to0,\qquad \varepsilon_N\log N\to\lambda\in[0,\infty].
\]
With fixed positive initial colour counts \(y_1,y_2\), fixed Pólya addition \(c>0\), and Friedman additions \(a\ge0\) to the drawn colour and \(b>0\) to the opposite colour, let \(Z_N\) be the final proportion of colour 1. Set \(\alpha=y_1/c\) and \(\beta=y_2/c\). Then
\[
Z_N\ \Longrightarrow\ \tfrac12+e^{-2b\lambda/c}(B-\tfrac12),
\qquad B\sim\operatorname{Beta}(\alpha,\beta),
\]
where \(e^{-2b\lambda/c}\) is interpreted as zero for \(\lambda=\infty\). In particular, the zero-window limit is the classical Pólya beta law, the positive finite window is a nondegenerate affine contraction of that law, and the infinite-window limit is the point mass at \(1/2\).

Writing \(d=e^{-2b\lambda/c}\), the limiting first two moments are
\[
\lim_{N\to\infty}\mathbb E Z_N
=\tfrac12+d\left(\frac{\alpha}{\alpha+\beta}-\tfrac12\right),
\qquad
\lim_{N\to\infty}\operatorname{Var}(Z_N)
=d^2\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.
\]
At the critical scale the shape and contraction do not depend on the Friedman same-colour addition \(a\): only the opposite-colour contribution \(b\), the Pólya addition \(c\), and the initial counts remain.

## Assumptions and scope

Choose fixed integers \(y_1,y_2\ge1\), \(a\ge0\), and \(b,c\ge1\). For each \(N\), start independently with \(y_1,y_2\) balls. For steps \(j=1,\ldots,N\), draw one ball uniformly, replace it, and independently choose one of two addition rules: with probability \(1-\varepsilon_N\), add \(c\) balls of the drawn colour; with probability \(\varepsilon_N\), add \(a\) of the drawn colour and \(b\) of the other colour. Allow \(\varepsilon_N=0\) and assume \(0\le\varepsilon_N\le1\). Each row has independent rule choices and independent drawing uniforms. The theorem asserts weak convergence at the end of each row and convergence of bounded moments; it does not assert almost-sure convergence across rows or a quantitative rate.

## Proof

**1. Exact rule-conditioned recursion.** Within a fixed row let \(\xi_j\) be the indicator of the Friedman choice, let \(\eta_j\) indicate that colour 1 is drawn, and put \(T_j=Y^1_j+Y^2_j\), \(Z_j=Y^1_j/T_j\), \(V_j=Z_j-1/2\). Conditional on past compositions and the rule sequence, the colour draw is Bernoulli with parameter \(Z_{j-1}\). The number of added balls depends on the rule but not the colour drawn. Therefore exactly
\[
T_j=T_0+cj+(a+b-c)\sum_{i=1}^j\xi_i,
\]
\[
V_j=\left(1-\frac{2b\xi_j}{T_j}\right)V_{j-1}+M_j,
\quad
M_j=\frac{c(1-\xi_j)+(a-b)\xi_j}{T_j}
(\eta_j-Z_{j-1}).
\]
The entire rule sequence is independent of the fresh drawing uniforms. Conditional on that sequence, \(M_j\) are bounded martingale differences with respect to the uniforms revealed up to step \(j\). With \(m=\min\{c,a+b\}>0\) and \(M=\max\{c,a+b\}\), the pathwise bounds \(mj\le T_j\le T_0+Mj\) hold, and \(|M_j|\le C/j\) for a constant independent of the row.

**2. The noise after a fixed early stage vanishes uniformly.** Select an integer \(K\) with \(m(K+1)>2b\). For all \(j>K\), the factors \(h_j=1-2b\xi_j/T_j\) lie in \([0,1]\). Set \(D_{u,v}=\prod_{j=u+1}^v h_j\). Iterating the exact recursion gives
\[
V_N=D_{K,N}V_K+\sum_{j=K+1}^N D_{j,N}M_j.
\]
Conditional on the entire rule sequence, the coefficients \(D_{j,N}\) are deterministic and bounded by one; the martingale differences are orthogonal in conditional \(L^2\). Hence, uniformly over all \(N>K\) and all rule probabilities,
\[
\mathbb E\left|\sum_{j=K+1}^N D_{j,N}M_j\right|^2
\le C^2\sum_{j>K}j^{-2}\le C_1/K.
\]
Thus all stochastic noise arising after a large fixed early stage can be discarded in \(L^2\), uniformly over the triangular array.

**3. The logarithmic damping product.** First suppose \(\lambda<\infty\). Let \(R_j=\sum_{i=1}^j\xi_i\). Using the exact total and its deterministic bounds,
\[
\left|T_j^{-1}-(cj)^{-1}\right|
\le\frac{T_0+|a+b-c|R_j}{cmj^2}.
\]
Because \(\mathbb E[\xi_jR_j]=\varepsilon_N+(j-1)\varepsilon_N^2\),
\[
\mathbb E\sum_{j>K}\xi_j\left|T_j^{-1}-(cj)^{-1}\right|
=O\bigl(\varepsilon_N+\varepsilon_N^2\log N\bigr)=o(1).
\]
Also independence of the rule indicators implies
\[
\mathbb E\sum_{j=K+1}^N\frac{\xi_j}{j}
=\varepsilon_N\sum_{j=K+1}^N j^{-1}\to\lambda,
\quad
\operatorname{Var}\left(\sum_{j=K+1}^N\frac{\xi_j}{j}\right)
\le\varepsilon_N\sum_{j>K}j^{-2}\to0.
\]
Consequently \(\sum_{j>K}\xi_j/T_j\to\lambda/c\) in probability. Moreover,
\[
\mathbb E\sum_{j>K}(\xi_j/T_j)^2
\le m^{-2}\varepsilon_N\sum_{j>K}j^{-2}\to0.
\]
Since all \(2b/T_j<1\) for \(j>K\), the standard bound \(|\log(1-t)+t|\le C_Kt^2\) applies uniformly to these factors, with \(C_K<\infty\). Therefore
\[
\log D_{K,N}=-2b\sum_{j>K}\frac{\xi_j}{T_j}+o_{\mathbb P}(1)
\ \xrightarrow{\mathbb P}\ -2b\lambda/c,
\]
and \(D_{K,N}\to e^{-2b\lambda/c}\) in probability.

For \(\lambda=\infty\), the upper bound on \(T_j\) gives
\[
\sum_{j>K}\frac{\xi_j}{T_j}
\ge\frac{1}{T_0+M}\sum_{j>K}\frac{\xi_j}{j}.
\]
The sum on the right has mean \(\varepsilon_N\log N+O(\varepsilon_N)\to\infty\) and variance bounded by \(\varepsilon_N\sum j^{-2}\to0\); hence it diverges in probability. From \(1-t\le e^{-t}\), \(D_{K,N}\le\exp(-2b\sum_{j>K}\xi_j/T_j)\to0\) in probability. Both cases yield \(D_{K,N}\to d\), for every fixed sufficiently large \(K\).

**4. Recover the early Pólya randomness.** Couple each mixed row to a pure Pólya urn using the same colour-drawing uniforms. In the first \(K\) steps they agree whenever no Friedman rule is chosen, an event whose complement has probability at most \(K\varepsilon_N\to0\). Thus, for every fixed \(K\), \(V_K^{(N)}\) converges in probability (in this coupling) to \(V_K^{\mathrm P}=Z_K^{\mathrm P}-1/2\). The classical \(c\)-addition two-colour Pólya urn proportion is a bounded martingale converging in \(L^2\) to \(B\sim\operatorname{Beta}(y_1/c,y_2/c)\).

For fixed large \(K\), the decomposition of Step 2, the convergence of Step 3, and Slutsky's theorem show that the final row variable differs in probability, up to an \(L^2\) error bounded by \(C_1/K\), from \(d V_K^{\mathrm P}\). Letting \(K\to\infty\), and using bounded-Lipschitz test functions and \(L^2\) convergence of the Pólya martingale, proves \(V_N\Rightarrow d(B-1/2)\). Translation gives the stated law. Uniform boundedness of proportions allows convergence of their first and second moments and yields the displayed mean and variance.

## Verification

The standalone Python file `checker.py` checks exact finite-state transitions for several urn parameter sets using rational arithmetic and compares independently evaluated conditional drift, second moments, and mass preservation. It also checks the separate balanced-urn moment recurrence against exact distribution enumeration and evaluates finite-size triangular-array moments as a numerical diagnostic. Its attached output reports `ALL_ASSERTIONS_PASSED 3439`. These checks do not prove the weak limit: the four-step analytical argument above establishes it for all admissible parameters and sequences.

## Relationship to prior work

Shi, Yin and Miao (arXiv:2605.26669v1, May 26, 2026) formulate the same two-rule urn and establish fixed-rule-probability central limit results. Alves and Rosales (arXiv:2502.16768) prove that any *fixed positive* mixture probability leads almost surely to a balanced limit. The classical Pólya urn supplies the beta law at zero mixture probability. The new statement treats a distinct two-parameter limit in which the mixture probability itself goes to zero with the row length, and identifies the intermediate nondegenerate distribution at the critical logarithmic scale.

Crimaldi, Louis and Minelli (arXiv:2102.06287) study time-dependent random diagonal reinforcements and associated random limits and fluctuations. Gao and Aguech (2023) treat dynamic opposite-reinforcement rules with a time-dependent addition scale. Their different replacement structures and fixed-asymptotic schemes do not yield the precise triangular rare-rule crossover by direct specialization. Relevant general stochastic-approximation or perturbation theory could nevertheless imply the statement indirectly; exhaustive historical priority is not asserted.

## Limitations

The two colours, fixed positive initial counts, positive Pólya addition, strictly positive opposite-colour Friedman addition, and rowwise independent random replacement rules are essential hypotheses of the proof as presented. The result is a distributional limit and moment limit, not a total-variation theorem, an almost-sure coupling across rows, or a convergence-rate result. The formula is not extended to more than two colours or time-varying rule probabilities within each row. Independent review and comprehensive historical-priority assessment have not been performed.

## References

1. J. Shi, Q. Yin, and Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669v1 (May 26, 2026). https://arxiv.org/html/2605.26669v1
2. R. Alves and R. A. Rosales, *Friedman vs Pólya*, arXiv:2502.16768 (February 24, 2025). https://arxiv.org/pdf/2502.16768
3. I. Crimaldi, P.-Y. Louis, and I. G. Minelli, *Urn models with random multiple drawing and random addition*, arXiv:2102.06287 (February 11, 2021). https://arxiv.org/pdf/2102.06287
4. S. Gao and R. Aguech, *Multiple-drawing dynamic Friedman urns with opposite-reinforcement*, *Probability in the Engineering and Informational Sciences* (2023). https://www.cambridge.org/core/journals/probability-in-the-engineering-and-informational-sciences/article/multipledrawing-dynamic-friedman-urns-with-oppositereinforcement/F59521C7894E49AE1B060398EDC803B3
