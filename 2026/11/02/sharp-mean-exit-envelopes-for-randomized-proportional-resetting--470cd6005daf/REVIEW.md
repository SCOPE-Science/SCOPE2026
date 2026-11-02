# Scientific review

## Correctness — PASS
The killed jump-diffusion has a finite mean symmetric exit time, verified by a uniform non-reset Brownian exit chance. The unique bounded backward solution is the absolutely convergent even-power series, obtained by coefficient matching and the absorbing endpoint conditions. Jensen and the inequality \(0\le U^j\le U\) for \(U=A^2\in[0,1]\) give the sharp coefficient comparisons. Equality and strictness follow from the second nontrivial moment coefficient. The stationary quadratic moment identity, weak-rate coefficient and fast-rate cosh-product asymptotics have been checked independently of the numerical BVP. The accompanying program passed 93 numerical verification checks; finite-dimensional numerical agreement is not the proof.

## Originality — PASS, qualified
The closest primary source, Biroli et al. (2024), treats first passage to one target under a deterministic multiplier, and includes a power-series recurrence. Pal and Prasad (2019) treat two absorbing endpoints under fixed-location restarting. Méndez et al. (2024) treat independent random reset positions, and Pierce (2022) treats fixed rescaling and stationary laws. The precise new statement is the complete **factor-distribution extremal classification** for symmetric exit at fixed second-moment retention, including equality cases, identical stationary variance and exponential fast-reset separation. The recurrence and fixed-location/full-reset limits are acknowledged prior techniques. No stronger published statement covering this full comparison was located in the checks described in AUDIT.json. Remaining risk: a more general monotonicity principle for stochastic jump kernels may imply the result without presenting it in this language; priority has not been independently certified.

## Mathematical value — PASS
At fixed \(\mathbb E[A^2]\), all protocols have the same stationary variance, making that constraint physically natural rather than an arbitrary parameter slice. Yet their exit times differ sharply, with a rigorous minimum under occasional complete resets and a maximum under deterministic partial resets. The result supplies exact quantitative envelopes, uniqueness of the two protocols, and an exponentially large protocol-design distinction in the fast-reset regime. This is a motivated absorption-versus-stationarity comparison, not a reparameterization of the fixed-multiplier one-target formula.

## Limits
The theorem concerns symmetric mean exit only. It does not certify full first-passage distribution ordering, asymmetric target optimization, or priority across inaccessible literature.

Self-review: passed. Independent audit: not yet performed.
