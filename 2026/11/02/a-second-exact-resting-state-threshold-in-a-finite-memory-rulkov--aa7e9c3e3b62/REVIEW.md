# Self-review

## Correctness — PASS

The equilibrium census uses the exact negative fast branch and the finite-window sigmoid, not the paper's approximate mean-voltage response. The characteristic polynomial follows from the full memory-shift Jacobian. For fast multiplier above one, a signed quadratic comparison produces real eigenvalues outside the unit circle, including explicit small-update bounds. Below one, analytic root continuation shows all roots enter the disk. At the degenerate fast multiplier one, Puiseux expansions through order \(\mu\) give a strictly negative radial drift for every finite memory length. The boundary case is therefore proved, not extrapolated from numerics. Symbolic and finite eigenvalue checks reproduced the calculations. No global stability or fixed finite-\(\mu\) threshold is inferred.

## Originality — PASS under examined literature

The 2026 motivating paper was inspected in its full accessible HTML, especially its equations (1)–(8) and regime discussion in §§3.1–3.3. It already uses the scalar intersection \(\sigma=\tanh(\kappa\sigma)\) as a mean-voltage heuristic and reports stable neuronal *regimes*. That is not equivalent to a full delayed-map Jacobian classification of stationary points: a stable spiking regime need not contain a stable fixed point. The exact degree-\(m+2\) polynomial, the threshold \(\kappa_*\), and boundary-inclusive complex-pair stability are not found in the inspected text. A related 2021 Rulkov discrete-memristor paper is available only at abstract level; its dynamical description differs and cannot be certified as not covering any possible reduction. The published mathematical-record comparisons found fixed-parameter Rulkov moment and two-cycle results, not an equivalent finite-memory equilibrium stability theorem. Absence in searches is not independent proof of historical novelty.

## Mathematical value — PASS

The two thresholds answer a motivated and natural question raised by the source's distinct silent, spiking, and bursting regimes: when does there actually exist an exponentially attracting *time-independent* rest state of the full lagged map? The answer is not given by the mean-feedback pitchfork at \(\kappa=1\), and the critical endpoint requires a singular double-root analysis. The result is exact for arbitrary finite memory length, supplies a complete weak-slow-gain stationary-point classification, and distinguishes a dynamical resting state from statistically stationary oscillatory activity. It neither claims a global attractor theorem nor treats narrow numerical sampling as sufficient evidence.

## Closest sources and residual limitations

The closest primary source is Moreno–Nieto–Sanjuán, arXiv:2601.12139, full HTML §§2–4 (read); the older Liu–Wei memristive Rulkov article arXiv:2112.02738 and Guo–Bai–Zhang's 2026 coupled-neuron article were inspected at abstract/metadata level only. Model differences support, but do not independently certify, the priority comparison. A separate human review of broader neuronal-map literature is still needed. All conclusions concern local fixed-point behavior at sufficiently small positive slow-update gain.

Self-review: passed. Independent audit: not yet performed.
