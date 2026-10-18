# Scientific review

## Correctness — PASS

At a constructed first-success state, conjugacy gives \(\operatorname{Beta}(\alpha+1,\beta+f_m)\) and the strict one-step ratio \(m(\alpha+1)/(m(\alpha+1)+\delta_m)<1\). The alternative policy uses the next-success posterior ratio, not future information, and its exact reward is computed by conditioning on the first later success; the terminal-event weight is constant in that success time. The positive-part sum and the asymptotic Riemann integral yield a strictly positive limiting conditional advantage. A Gamma-ratio calculation converts this to an unconditional polynomial lower bound. Exact rational checks replicate the finite identity for seven distinct parameter settings. The checker is not used to justify the uniform or asymptotic conclusions.

## Originality — PASS, with residual priority risk

The closest 2026 source (Ano, arXiv:2610.10237, Section 3.4) supplies the posterior formulas, myopic criterion, dynamic program, and two illustrative finite counterexamples; it does not state that strict suboptimality occurs for **every** Beta prior at unbounded horizons or quantify its unavoidable Bayesian-regret lower bound. The 2009 full Bayesian recursion of Bruss–Louchard can numerically solve each finite problem but does not itself state the present uniform parameter theorem. Paindaveine's unknown-fixed-parameter frequentist plug-in problem and Gnedin–Derbazi's random-observation-time prior are not equivalent to this conditional-Beta setting. Searches of relevant published research records and primary literature did not identify the exact theorem. The possibility of an earlier general optimal-stopping comparison theorem implying it remains a priority risk; no independent audit has been performed.

## Mathematical value — PASS

The exact failure of a locally favorable Bayesian last-success stopping decision for **every** proper Beta prior is a structurally meaningful obstruction to extending one-step monotone stopping theory. The construction is explicit at infinitely many horizons, yields a nonvanishing conditional advantage, and quantifies a positive polynomial-scale unconditional regret without solving the whole dynamic program. This generalizes isolated counterexamples and reveals a mechanism—posterior updating after further successes—that cannot be detected from the first one-step comparison.

## Closest literature and limitations

Ano 2026, Section 3.4, and Bruss–Louchard 2009, Section 6, are closest by model and mathematical implication. The theorem concerns a specially constructed infinite subsequence of horizons and a lower bound, not a characterization of all horizons, all priors, the globally optimal policy, or the exact regret. Independent priority evaluation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
