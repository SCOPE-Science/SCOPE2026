# Self-review

## Correctness — PASS

The invariant joint law exists because on-state residence is recurrent and introduces contraction. Solving the two stationary characteristic-function equations fixes the Gaussian normalization and both rational powers. The Lévy profile \(h(r)=(a+1)e^{-cr}-e^{-dr}\) is everywhere positive. By the canonical class-\(L\) criterion, monotonicity holds exactly when \((a+1)c\ge d\), equivalent to \(\beta(4\mu+\alpha)\ge4\mu^2\). Equality is included. Above and at the boundary, \(q=-h'\) is a legitimate finite-intensity Lévy jump density, and the OU stationary exponent reconstructs the transform. Below it, increasing \(h\) near the origin is a decisive obstruction. A standalone program independently passed 112 finite tests, including exact rational moment recurrence comparisons. Those tests do not replace the proof.

## Originality — PASS, with priority risk

Santra, Das and Nath (2021, arXiv:2104.00609) derive the symmetric-rate physical model's stationary transform. Zhang and Wang (2017, Theorem 2.1(ii), doi:10.1080/03610918.2015.1132321) already give the exact unequal-rate transform in a general Markov-switching Ornstein–Uhlenbeck setting. Therefore the transform is NOT claimed as new. The exact class-\(L\)/ordinary Lévy-driven OU stationary-marginal *phase classification* and explicit positive background jump law were not identified in either inspected text, the relevant distribution-theory review, or targeted published mathematical-record searches. The canonical-density test itself is classical and a recent variance-gamma/Gaussian-jump study applies it in a different family. A major residual risk is that the evaluated transition may be an unrecognized elementary corollary of the older transform and standard self-decomposability criterion. The present review does not constitute an independent priority determination.

## Scientific value — PASS

The phase boundary answers the natural structural question of precisely when a two-rate intermittently driven Brownian trap can be replaced, at stationary one-time marginal level, by a fixed linear harmonic trap and independent Lévy forcing. It separates infinite divisibility, which always holds, from stronger self-decomposability, and provides a complete realizable jump law and a diffusivity-independent physical switching threshold. This is a motivated exact classification, not a nominal reparameterization; its mathematical depth is limited by reliance on known transform and canonical test.

## Closest literature and limitations

The full Fourier-law overlap with Zhang--Wang (2017) is decisive and explicitly conceded. Santra--Das--Nath (2021) motivates the on/off physical setting. The result does not cover arbitrary state-dependent diffusivity or reconstruct temporal correlations. Priority and full correctness still warrant external examination.

Self-review: passed. Independent audit: not yet performed.
