# Scientific review

## Correctness

PASS. The all-horizons Bellman recursion is justified by the four ordered independent offers. The cone proof checks the odd and even middle boundaries and all small-index exceptions, establishing a single optimal policy for every horizon. The stagewise conditional-quantile coupling handles arbitrary adaptive policies; the exact moment recurrences and a biased-walk exponential moment give the variance expansion and Lyapunov central limit theorem. The standalone checker has 39,497 exact assertions, independently computing the finite absorbing-chain moments.

## Originality

PASS, qualified. The primary 2019/2021/2022 choice-walk source establishes linear-order cover bounds for tori and general dynamic programming, not a stochastic-order-optimal policy or cycle-cover fluctuation law. The previously available exact expected cycle cover time is explicitly excluded from the originality claim. A mean minimum is strictly weaker than minimization of all cover-time tails. No equivalent stronger theorem emerged in the checked indexed claims or literature searches. Priority relative to less discoverable treatments of risk-sensitive controlled walks remains a residual risk.

## Value

PASS. Risk-sensitive cover-time control is a natural strengthening of expectation minimization: one strategy now minimizes every deadline failure probability and all increasing penalties. The sharp \(6n-129/4\) fluctuation variance and Gaussian law quantify reliability at square-root scale; neither follows from knowing the mean alone. The result is a complete structural statement for a fundamental graph family, not a routine numerical improvement.

## Closest literature and limitations

The primary comparison is Georgakopoulos et al., *The Power of Two Choices for Random Walks*, arXiv:1911.05170, first public 2019-11-12, and the earlier ITCS version. The relevant primary full text (torus bounds and controlled-chain formulation) was inspected. This proof is for cycles with two independent with-replacement neighbor offers, not general graphs; independent priority verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
