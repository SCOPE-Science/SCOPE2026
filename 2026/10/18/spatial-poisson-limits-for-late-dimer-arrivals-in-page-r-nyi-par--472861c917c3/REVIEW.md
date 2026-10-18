# Scientific review: spatial Poisson limits for late dimer arrivals

## Correctness — PASS

The exact finite one-edge integral follows from a one-sided vacancy recursion for independent uniform arrival times; its Taylor remainder supplies a uniform \(O(n^{-1})\) count-mean estimate. The finite-range truncation error is bounded by the probability of a strictly decreasing priority chain, at most \(2/(L+2)!\). For \(L=\lceil\log n\rceil\), dependency-graph Chen–Stein bounds prove the threshold-count error \(O(\log n/n)\), and mixed factorial moments give the stated spatial and temporal Poisson-process convergence. Every step holds for all integers \(n\ge2\) where the finite identity is asserted, and for sufficiently large \(n\) where a limit or error rate is asserted. Exact finite enumeration independently confirms the vacancy identities, edge probabilities and causal-path implication; it does not establish the infinite limit on its own.

## Originality — PASS, with residual historical risk

De Smedt, Godrèche and Luck (arXiv:cond-mat/0202465), Section 5, explicitly apply their Gumbel jamming-time prediction to the same dimer process, so neither the scalar Gumbel law nor its \(e^{-2}\) constant is claimed as novel. Gerin (arXiv:1411.8002), especially Theorem 5 and Lemma 8, has the relevant time-density and locality inputs, but does not state joint marked spatial Poisson convergence, the exact finite individual-edge law, or the quantitative count approximation. Penrose–Sudbury (arXiv:math/0503519) study general deposition and normal approximation; Purvis et al. (2015) study near-jamming coverage/availability scaling. The contribution is the spatially resolved, multitime extreme-process theorem and finite error rate, not established scalar extremal behavior. Possible implicit derivations in other adsorption papers remain a priority risk; semantic similarity searches alone do not prove absence.

## Value — PASS

The last successful depositions are a natural observable of slow jamming. A scalar last-time distribution does not determine where the last few dimers land, how many nearly simultaneous late arrivals remain or whether their locations decouple. The theorem gives that complete rare-event field, exact finite rates per edge and a quantitative approximation for finite paths, permitting spatial late-stage calibration. This is substantially more informative than restating an already-known Gumbel limit.

## Limits and external status

The model has rate-one independent edge clocks and nearest-neighbor dimers on a path. No longer-car, nonuniform-clock or irregular-graph extension is asserted, and spatial convergence is not total variation. The review is not an independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
