# Same-model review

## Correctness
PASS. The fixed-step Malitsky--Pock iteration reduces exactly to the displayed two-state matrix. Its discriminant is \((\sigma^2-4r(1-r))/(1+\sigma)^2\). Below the repeated-root boundary, the spectral radius is \(\sqrt{(1-r)/(1+\sigma)}\) and strictly decreases. Above it, direct differentiation of the larger real root is strictly positive. The conversion from \(\sigma_*\) to \(\beta_*\) follows from \(r=\sigma^2a^2/\beta\). The checker independently reconstructs and tests these formulas numerically.

## Originality
PASS with a residual literature risk. The primary 2016 paper identifies \(\beta\) as the primal/dual ratio and supplies the fixed-step ceiling, but does not state a rate-optimal ratio. Fercoq's 2024 quadratic PDHG work explicitly makes spectral-radius minimization the tuning objective and gives the general quadratic iteration matrix; the inspected material does not state this scalar closed form, its critical discriminant boundary, or the corresponding Malitsky--Pock ratio. Targeted published-finding searches for those equivalent formulations returned no implication-equivalent result. The closest published finding found concerns a different forward-reflected-backward method whose optimum also occurs at eigenvalue coalescence; it does not imply the present PDHG matrix calculation.

## Value
PASS. The result resolves a parameter that the source deliberately leaves free with a sharp, closed calibration law on the simplest nontrivial least-squares mode. It also separates three regimes—conjugate, repeated, and real roots—and identifies the exact transition as the unique rate optimum. This supplies a transparent benchmark for primal/dual ratio heuristics and spectral-radius adaptation, while explicitly delimiting the multi-mode problem that remains.

## Closest literature and limitations
The closest later literature is Fercoq's spectral-radius-based PDHG step adaptation for quadratic problems. It motivates the same tuning objective at much greater generality but uses spectral-radius estimation rather than the scalar analytic minimizer recorded here. The claim is limited to one singular mode, constant steps, \(\theta=1\), and asymptotic spectral radius.

Same-model review: passed. Independent audit: not yet performed.
