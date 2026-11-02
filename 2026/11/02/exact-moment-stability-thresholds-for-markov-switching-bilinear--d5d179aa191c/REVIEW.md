# Scientific review

## Correctness — PASS

The stated object is Algorithm 1's discrete feedback update on stationary two-state Markov-switching bilinear games with common saddle and equal feedback gains. The proof first reconstructs the update as conformal matrices and then obtains an exact scalar product formula for every orbit. Markov occupation frequencies give the almost-sure exponent, without silently replacing this by a moment assertion. For arbitrary real positive moment order, a strictly positive two-by-two transfer matrix computes each finite-time moment exactly. The Perron root and the rank-one derivative prove the unique critical switching threshold, and the hyperbolic-sine formula proves its strict increase in moment order. The explicit rational example and the endpoints are checked algebraically. A standalone script reproduces 711 symbolic and numerical consistency checks. The code does not constitute proof of the infinite-time classifications; those follow from occupation laws, Perron–Frobenius theory, and the proven monotonicity.

## Originality — PASS, with residual priority risk

The motivating primary text introduces the fixed controller and a separate continuous-time local stability analysis; it does not give the exact Markov sign-switching all-order moment phase diagram. General Markov jump linear-system spectral criteria, specifically Ling and Deng (2012), already encompass mean-square spectral tests and their broader theoretical mechanism; these are explicitly treated as prior art. Tai (2026) establishes general moment/covariance spectral criteria for additively forced Markov-affine recurrences and illustrates the broader Lyapunov-versus-variance distinction. No finding has been identified in the checked indexed research records or the accessible prior ledger with the same controlled algorithm, explicit parameter-dependent almost-sure region, entire ordered family of exact moment thresholds, and simultaneous stable-second/unstable-fourth-moment example. That is a best-knowledge claim, not proof of uniqueness or independently adjudicated priority. The possibility of an unindexed earlier Markov-products specialization remains.

## Mathematical value — PASS

The exact thresholds distinguish sampling-independent signs from anti-persistent interaction changes and reveal that reliable convergence of typical controlled game trajectories is not enough to control their expected squared error or higher-order tail risk. The continuous, strictly increasing moment hierarchy is a structural result useful for specifying which moment-based guarantees a time-varying feedback design could support. The exact rational example places decay and growth of different moments on opposite sides of a single switching frequency. This is more informative than a generic application of a spectral-radius test, while making no claim about general nonlinear adversarial training.

## Limitations and closest literature

Relevant primary works: Luo, Chen and Zhu, arXiv:2610.12915; Ling and Deng, DOI:10.1155/2012/642480; Tai, arXiv:2607.09994. The theorem assumes symmetric stationary two-state sign switching, scalar bilinear coupling, equal gains, fixed steps and no additive noise. General Markov jump-system theory supplies the spectral machinery; the new proposed contribution is the explicit method-specific full phase diagram. Priority requires independent scholarly review.

Self-review: passed. Independent audit: not yet performed.
