# Self-review

## Correctness: PASS

The domain is a one-dimensional symmetric strictly stable Levy flight with fixed interior reset point and independent Poisson reset clocks, \(0<\alpha<2\). The normalization matches the stated characteristic exponent and Levy density. The essential nonstandard premise is the marked one-jump exit law (RESULT.md (1)), which follows from small-time Levy path decomposition and is supported by the 2014 stopped-Levy-bridge analysis. The exact renewal identity (4) was reconstructed from independent failed and successful cycles. The conditional failed-cycle mean bias is \(O(r^{-1})\) after multiplying by \(r\), so the random-index central limit in (8) is centered correctly; its variance remains random and explains the Laplace, rather than Gaussian, marginal. No computation is substituted for the infinite-probability arguments. The standalone `verify.py` stress-tests normalizations, renewal algebra, and Gaussian-exponential mixture constants.

## Originality: PASS (best-knowledge, provisional)

Zbik–Palmowski (2026) determine mean-exit asymptotics, not the marked two-scale limit. Linn–Lawley (2023) already give the marginal exponential first-passage limit, Sunil et al. (2023) the general joint reset-count/time transform, and Figueroa-Lopez–Tankov (2014) the free short-time marked-exit asymptotics. Those are explicitly excluded from the novelty claim. The assessed addition is the **joint** six-variable limit with the \(\sqrt r\) clock-error Gaussian scale mixture, its Laplace marginal, and independence from final-excursion marks. The published generic transform makes the result logically derivable with additional fluctuation analysis; it is an acknowledged priority risk, but no inspected primary source states that joint second-order conclusion.

## Mathematical value: PASS

The natural reset-count estimator \(N_r/r\) has a stochastic correction with a non-Gaussian universal law, even though the conditional error is Gaussian; this is mathematically relevant to uncertainty propagation for high-rate stopping-time observations. Exit side, overshoot, and duration of the final excursion describe practical boundary-crossing behavior absent from mean-only asymptotics. The six-component joint limit distinguishes macroscopic completion time, microlocal final duration, and fluctuations of the observed reset clock. The result is not a mere numerical improvement or a name change.

## Scope and residual risks

All asymptotic parameters except \(r\) are fixed. No uniformity near \(\alpha=2\) or near an interval boundary. Independent historical-priority review is still needed, especially whether a general marked-renewal central limit theorem already subsumes this as a corollary. Finite checks cannot establish infinite limits.

Self-review: passed. Independent audit: not yet performed.
