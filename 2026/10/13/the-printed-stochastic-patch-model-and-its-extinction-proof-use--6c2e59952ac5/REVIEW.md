# Self-review

## Correctness

PASS. Equations (1.4)-(1.5) print one Brownian motion in both patch equations, whereas the later proofs use two Brownian motions and a sum-of-squares quadratic variation. Recomputing the weighted-total Itô correction gives the sharp independent-noise floor
\[
\frac{\sigma_1^2\sigma_2^2}{\sigma_1^2+\sigma_2^2}
\]
and the sharp common-noise floor
\[
\min\{\sigma_1^2,\sigma_2^2\}.
\]
The exact symmetric witness has logarithmic total-population drift at most \(-1/8\), proving exponential extinction almost surely.

## Originality

PASS. Correlation-dependent stochastic population survival is prior theory. The accepted contribution is source-specific: the printed 2020 model is perfectly correlated, its proofs are independent-noise proofs, and the exact replacement changes the sufficient extinction margin. Exact source and alias searches found no published correction.

## Value

PASS. The paper interprets environmental noise intensity as a driver of extinction and persistence. Correlation is therefore not a cosmetic Brownian label: it changes the quadratic variation and doubles the sharp uniform extinction margin for equal patch noise. The strict witness shows a parameter range that the printed common-noise model certifies extinct but the source's stated threshold does not cover.

## Closest literature and limitations

A related two-patch stochastic diffusion paper explicitly assumes mutually independent Brownian motions. General stochastic patch-population theory treats environmental covariance, including perfectly correlated noise, as structural and capable of changing persistence/extinction behavior.

The result does not determine which noise structure was used in unavailable simulation code and does not claim that every source theorem fails under common noise.

Self-review: passed. Independent audit: not yet performed.
