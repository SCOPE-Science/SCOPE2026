# Review

## Correctness — PASS

For independent atomless observations, the twenty-four consecutive four-pattern indicators are 3-dependent and have uniform marginal probability \(1/24\). Exact joint pattern enumeration for lags 0–3 gives the rational limiting covariance \(\Gamma\). An 18-by-18 principal determinant is nonzero modulo the prime 1000003, giving a characteristic-zero rank lower bound of 18. Exact multiplication confirms six linearly independent nullspace vectors arising from the sum constraint and the five endpoint-coboundary balances, giving the upper bound. The exact finite telescoping formula, positive variance outside this kernel, and an ordinary bounded 3-dependent central limit theorem complete the proof. The extracted standalone checker also verifies 2304 finite covariance entries at orders 4–7, but those examples are not a substitute for the general proof.

## Originality — PASS, with residual priority risk

The stated claim is the **complete** nullspace of the 24-by-24 consecutive length-four covariance limit, not the familiar indicator overlap calculation or the length-three problem. Janson's constrained-pattern theory (arXiv:2106.09401, Remark 14.2) explicitly leaves degenerate linear-combination classification open. Bandt (2023, doi:10.1063/5.0132602) develops the complete length-three covariance contrasts and only two selected length-four contrasts, and calls fuller length-four analysis a next step. Crane–DeSalvo (arXiv:1509.07941) treats pattern occurrence/avoidance, while Janson–Nakamura–Zeilberger (arXiv:1312.3955) treats nonconsecutive subsequences. The full 2022 Weiß–Ruiz Marín–Keller–Matilla-García test paper and complete 2007 Bandt–Shiha text were not inspected; an implicit equivalent there remains possible. Searches cannot certify global priority.

## Mathematical value — PASS

Twenty-four local order-pattern counts are widely used as a joint multivariate summary. The theorem identifies precisely why their asymptotic covariance is singular, resolves its rank, classifies all bounded-variance contrasts, and supplies the correct number of Gaussian fluctuation directions for statistical calibration. The 18-dimensional positivity statement is nontrivial; it does not follow just from knowing five stationarity-balance relations.

## Scientific limitations

The result is uniform-i.i.d. specific and confined to consecutive length-four windows. It does not determine the full eigenvalue list or any finite-sample chi-square distribution. All claims here have undergone only an internal mathematical review; historical priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
