# Scientific review

## Correctness

PASS. The all-horizons Bellman recursion is justified by the four ordered independent offers. The cone proof checks the odd and even middle boundaries and all small-index exceptions, establishing a single optimal policy for every horizon. The stagewise conditional-quantile coupling handles arbitrary adaptive policies; the exact moment recurrences and a biased-walk exponential moment give the variance expansion and Lyapunov central limit theorem. The standalone checker has 39,497 exact assertions, independently computing the finite absorbing-chain moments.

## Originality

The distinct claim is stochastic-order optimality for whole-cycle coverage. The primary choice-walk source establishes linear-order cover bounds for tori. The fixed-target result cited as [3] in RESULT.md already supplies the one-stage moment formulas, by taking distance one on a cycle with one more vertex than the visited arc. Its optimality result is for the mean and its fluctuation theorem concerns a different limit (a single target at diverging distance). No originality is claimed for the individual stage moments or the exact cover mean. The total variance and Gaussian limit are consequences that quantify the cover policy; the all-tail minimum is the substantive distinction. The comparisons are bounded and do not establish absolute priority.

## Value

PASS. Risk-sensitive cover-time control is a natural strengthening of expectation minimization: one strategy now minimizes every deadline failure probability and all increasing penalties. The sharp \(6n-129/4\) fluctuation variance and Gaussian law quantify reliability at square-root scale; neither follows from knowing the mean alone. The result is a complete structural statement for a fundamental graph family, not a routine numerical improvement.

## Closest literature and limitations

The primary comparisons are Georgakopoulos et al., *The Power of Two Choices for Random Walks*, arXiv:1911.05170 (first posted 2019-11-12), and the fixed-target result [3] in RESULT.md. The cover-time proof is for cycles with two independent with-replacement neighbor offers, not general graphs.

Self-review: passed. Independent audit: not yet performed.
