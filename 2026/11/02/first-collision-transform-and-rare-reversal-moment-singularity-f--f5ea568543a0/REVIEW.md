# Scientific review: first-collision transform and rare-reversal singularity

## Correctness — PASS

The physical state reduction is exact before the first meeting: two independent sign-flip clocks of rate \(\alpha\) induce the three-state closing/opening/stalled chain with transition rates \(2\alpha\) and \(\alpha\). The antipodal-folding and first-contact conditions are applied only to the incoming characteristics. Eliminating the stalled state yields \(U''=s(s+4\alpha)U/(4v^2)\); the two boundary conditions determine its unique transform. A first-order expansion gives the exact mean. For the rare-rate limit, an initial flip has probability \(1-e^{-\alpha x/v}\), then enforces a holding time of mean \(1/(2\alpha)\). The full all-order assertion additionally follows from a uniform analytic expansion of the scaled Laplace transform; this is not inferred solely from simulations or weak convergence. The independent verifier passed 30 checks, including direct symbolic generator identities and event-driven simulations.

## Originality — PASS, with residual risk

The collision model, folded gap and stationary behavior are established in Hahn–Guillin–Michel, arXiv:2306.00831. Le Doussal–Majumdar–Schehr, arXiv:1902.06176, already solve encounter statistics on an unbounded line. Guillin–Hahn–Michel, arXiv:2411.13964, Section 4.2, derive a mean time to one specified oriented jamming endpoint, not first collision at either endpoint; this is the closest prior claim and is credited. Grange–Yuan, arXiv:2509.11308, derive conditional mean exit times for a different nonzero-drift three-velocity interval model, explicitly noting higher moments as an extension. In the material inspected, none implies the exact two-particle ring **first-contact transform together with its rare-reversal all-moment singularity**. Targeted semantic searches returned unrelated mathematical findings; no search failure is treated as proof of novelty. Full priority verification against broader Markov-fluid first-passage literature remains a risk.

## Value — PASS

First collision is the kinetic entrance into a jammed configuration, not merely a stationary occupation or post-jamming relaxation observable. The exact formula identifies an observable nonuniform-integrability phenomenon: for almost all low-flip trajectories collision is ballistic, yet rare interrupted trajectories double the limiting expectation, and all moments of order at least two diverge with explicit universal coefficients independent of circumference at leading order. These conclusions separate typical and average aggregation time and are not a straightforward paraphrase of stationary-state identities. The precise first-contact time is useful in interpreting clustering onset and transient rare-event behavior; the claim is intentionally limited to this natural initial condition.

## Nearest prior literature and limitations

The main model source (arXiv:2306.00831, Section II) and the 2024 same-particle mixing study (arXiv:2411.13964, Sections 1.2 and 4.2) were inspected in relevant detail. The latter supplies a neighboring, but not identical, hitting-time computation, so the ordinary backward-equation method is not claimed to be new. The 2019 line-encounter result (arXiv:1902.06176, Section III) gives a different infinite-domain absorption law. The 2025/2026 Grange–Yuan analysis (arXiv:2509.11308, Sections 3–5 and 7) is a broader related velocity model with additional drift but does not directly address this zero-drift, reflected/periodic contact law or its all-order singularity. No generalization to asymmetric rates, thermal noise, three particles, or an entire mixing spectrum is claimed.

Self-review: passed. Independent audit: not yet performed.
