# Scientific review

## Correctness — PASS

All conditional signs have independent multiplier histories; the resulting two-block likelihood reproduces the exact finite Markov evolution. Uniform Taylor expansion and the triangular-array central limit theorem give a lognormal likelihood limit, and bounded continuity yields the total-variation Gaussian profile. Every phase has a constructive dimension subsequence. Elementary chi-squared and Hellinger estimates establish the cutoff window. The numerical checker returns 1366 exact-rational/deterministic assertions, supportive rather than a substitute for the limiting argument. A limitation is that the result is for fixed \(0<a<1\).

## Originality — PASS, with priority risk

Judd–Esposito, arXiv:2610.10860v1, Lemma 5.2 and its Appendix A proof, provides a bound for early times and the one-block exact formula at multiples of the register length. Its Lemma 5.4 *already proves* equality of worst-case and average distance at every time; this equality is expressly excluded from the new contribution. The new claim is the evaluated two-block profile at partial-block times and the nonconstant log-periodic Gaussian cutoff family. Levin–Tankala (arXiv:2109.05387) concerns a different XOR shift-register process. General Bernoulli-product normal approximations may imply the Gaussian sublemma; they do not, without the model's partial-block structure, give the phase law. Exact earlier applications to this process could still cover the result, and no claim of exhaustive priority is made.

## Mathematical value — PASS

The main source uses this exact chain to calibrate statistical impossibility through average mixing times. A phase-free Gaussian approximation at its expected cutoff location is mathematically false; the proved family identifies how the discrete register length stores a fraction-of-block phase, causing different asymptotic mixing levels along dimension subsequences. This distinction directly informs threshold calibration, not just a numerically larger constant. It is more than a routine evaluation at a fixed index: it classifies all subsequential profiles and proves their genuine separation.

Self-review: passed. Independent audit: not yet performed.
