# Scientific review: stationary aliasing with hidden temporal distinction

## Correctness — PASS

The three-mode Markov generators and renewal mechanism are specified completely. The Fourier stationary system gives a strictly positive common denominator for all real frequencies; subtracting its two stationary solutions shows that the positional distributions coincide if and only if the ballistic speed obeys the stated balance. At this balance, factorization gives the symmetric Laplace characteristic function. Stationary mode fractions and position–heading correlations follow from exact generator balances. Conditioning on zero or at least one reset during a lag supplies an exact two-time covariance, whose positive difference and integrated discrepancy follow algebraically. The six-dimensional independent matrix-semigroup and Fourier checks in `CHECK.py` passed 622 assertions. No unproved limit theorem or numerical extrapolation is used to establish the result.

## Originality — PASS, with residual priority risk

The main prior paper, Flaquer-Galmés, Campos, and Méndez, Physical Review E 109, 034103 (2024), derives the same switching dynamics and both stationary spatial distributions. Its equations (29)–(30) already imply the tuned stationary spatial coincidence after specialization; that coincidence alone is therefore not credited as an original theorem. However, its full paper focuses on stationary one-time distributions, mean-square displacement, and first-arrival statistics, and contains no two-time stationary position covariance or strict all-lag comparison between the two resetting protocols. The assessed original content is the if-and-only-if spatial aliasing coupled to rigorously distinct all-lag and integrated temporal correlations. Related switching-framework work (Santra, Olsen, Gupta, Soft Matter 2024) and intermittent-activity correlation work (Datta, Beta, Großmann, Physical Review Research 2024) do not establish the simultaneous exact distinction in this reset-renewed three-state model. A broader regenerative switching theory or uninspected treatment may contain an equivalent calculation; independent priority review remains outstanding.

## Value — PASS

The model's established dependence on the phase chosen at resetting motivates asking whether that phase can be inferred from stationary observations. The theorem supplies a complete and unexpected obstruction: even the *entire* stationary position law can become identical across physically different protocols, not merely a low-order moment. It then gives a concrete experimental/mathematical discriminator that succeeds at every nonzero lag, with a sharp integrated consequence for time-averaged measurement variance. The result addresses observability of hidden transport mechanisms, not an arbitrary parameter slice or a small numerical improvement.

## Scope and evidence boundaries

All rates and diffusion parameters are strictly positive, ballistic direction choice is symmetric, resets renew both location and mode, and the motion is one-dimensional. The primary 2024 article already covers the single-time transform framework. Full text of one related switching paper was not independently retrieved; its indexed model/sections were assessed without claiming whole-document absence. Unknown equivalent results in the broader hidden Markov and resetting literature remain a priority risk. Numerical verification supplements but does not replace the exact algebraic proof.

Self-review: passed. Independent audit: not yet performed.
