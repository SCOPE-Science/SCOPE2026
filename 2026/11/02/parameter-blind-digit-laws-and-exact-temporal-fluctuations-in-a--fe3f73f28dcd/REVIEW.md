# Mathematical review

## Correctness — PASS

Both affine maps send each of the six partition cells bijectively onto the same one of two intervals, independent of which map is selected. Exact interval lengths give a common transition matrix. The displayed stationary six-state distribution and interval density are verified by direct multiplication; affine-cylinder conditional uniformity proves the full-process Markov representation rather than just matching one-step marginals. The centered digit indicator satisfies \(P^2g=-Pg/3\). This gives every covariance, a finite geometric variance sum, and a positive asymptotic variance. Irreducibility and the positive self-loop of the finite chain ensure the standard Markov central limit theorem applies. The distinct three-letter conditional laws prove the binary process itself is not first-order Markov. Exact rational checks in `verify.py` agree with every finite algebraic identity; they are not relied on for infinity claims.

## Originality — PASS within inspected sources

Kalle and Maggioni's defining paper [1, §7] supplies the exact maps and the invariant density and one-time digit frequencies; those are not contributions here. Full-text review of the source's example found no all-cylinder parameter-identifiability theorem, covariance recurrence, finite-horizon variance, Gaussian variance coefficient or two-symbol non-Markov witness. The related follow-up [2] supplies broad Markov partition and digit-frequency methods for other random Lüroth families, without these explicit statements. Comparisons against symbol-covariance work for unrelated coded shifts, deterministic expanding maps, and general finite-state theorems reveal useful methods but no covering result for this system. The method is elementary Markov-partition theory, not claimed as a new general method. An unindexed or differently described equivalent symbolic calculation remains possible; the earliest 2018 preprint version was not examined in full.

## Mathematical value — PASS

The original density and \(13/16\) digit-two frequency do not reveal whether a switch probability can be recovered from a whole digit time series. The all-length law rules out that inference categorically for stationary digit-only observations; the explicit negative alternating lag correlation and exact variance quantify the remaining symbolic memory. The different conditional two-step probabilities show a mathematically relevant obstruction to modeling the digits as a two-state chain. These conclusions address natural temporal and statistical questions about this specific bounded-digit system, not an arbitrary finite calculation.

## Closest work and limitations

[1] C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430, §7, first posted 2018; revised 2020. The density, map, and marginal frequencies are already established there.

[2] C. Kalle and M. Maggioni, *On approximation by random Lüroth expansions*, arXiv:2101.01982 (2021), §§4–5. Related partition construction, not the exact six-cell digit-process classification presented here.

General finite-state Markov-chain CLT and piecewise affine Markov partition theory are pre-existing tools. The result is stationary and six-cell-specific, and an independent review remains pending.

Self-review: passed. Independent audit: not yet performed.
