# Same-model review

## Correctness

**PASS.** The finding is reduced exactly to a Gaussian numerator independent of a weighted sum of two normalized chi-square variables. The coverage functional \(q\mapsto2\Phi(z\sqrt q)-1\) has a strictly negative second derivative. Pairwise averaging of iid chi-square coefficients proves the upper convex-order bound, and a leave-one-out Jensen argument proves that normalized chi-square means decrease in convex order with their degrees of freedom, yielding the lower bound. The equality and limiting cases follow from the same representation. The accompanying numerical replay checks the reported example but is not used as proof.

## Originality

**PASS.** The closest primary source on Student bridge distributions already contains the exact Behrens--Fisher bridge representation, its endpoint Student distributions, and the balanced Student case; those facts are explicitly treated as prior. The accepted claim is narrower and different: a sharp global minimum/maximum theorem for the central coverage probability over all positive nuisance variance ratios, together with the exact maximizing balance surface and the prediction-powered specialization. Targeted published-finding corpus queries, the own prior ledger, the direct PPI source, the closest full Student-bridge paper, classical Welch--Satterthwaite references, and later non-asymptotic PPI work were compared by implication. No inspected source stated or implied this two-sided convex-order envelope directly.

Residual risk remains because the historical Behrens--Fisher literature is large and a non-surfaced older paper may contain an equivalent extremal coverage statement.

## Value

**PASS.** The result identifies exactly how far the commonly displayed normal-critical-value prediction-powered mean interval can deviate in finite Gaussian samples as the two variance contributions change. It supplies a sharp floor, an attained best case, and the unique variance-balance condition for that best case. The result is useful for interpreting finite-sample calibration and is not merely a recomputation of a known special-case Student law.

## Closest literature and limitations

The prediction-powered source defines the estimator and interval. Richter (2020) supplies the underlying Student-bridge family and special Student cases. Welch and Satterthwaite supply the classical moment-matching approximation, and later PPI work studies other finite-sample effects. The finding assumes two independent Gaussian samples, unbiased sample variances, and a fixed predictor. The lower endpoint is an infimum if both population variances must remain strictly positive.

Same-model review: passed. Independent audit: not yet performed.
