# Scientific review

## Correctness — PASS
The stated model preserves active-force variance exactly, and its remaining covariance equations close without approximation. Positive cross-covariance permits forward/backward order comparison. Both envelope paths are explicitly achievable by two-segment rate controls; convex interpolation weighted by the positive state gives every intermediate terminal variance, not merely a bound. The strict finite-time speed-limit gap, large-horizon opposite sign, and uniqueness of extremizing controls follow from the same scalar equations and positive convolution kernel. A standalone standard-library checker repeats the analytic propagator across 125 parameter choices and checks independent numerical propagation for representative settings. Correctness rests on the written argument, not simulation.

## Originality — PASS, qualified best-knowledge
The source by Boriskovsky et al. (arXiv:2610.11831v1) already develops the moment inverse engineering framework, time limits, and prescribed-trajectory optimization. Those are not claimed. The assessed statement concerns *all measurable bounded bath-rate trajectories*, giving the complete terminal-variance interval, its two explicit sharp extremizers, and a globally optimal one-switch finite-time NESS transfer. Related studies of auxiliary-potential and quadratic-cost control do not imply that specific closed interval. Targeted research-record and own-finding searches did not expose an equivalent claim. The most important risk is that the inaccessible full source or its supplement may already contain the same global theorem; abstract comparisons alone cannot establish whole-paper absence.

## Value — PASS
An exact finite-horizon reachable set and global, constructive speed limit answer a natural actuator-constrained state-preparation question without restricting to convenient control ansatz families. The switched-control structure is simple enough for physical implementation in idealized rate-quench settings and quantifies how matching cross-covariance alone can be too fast to match the full Gaussian state. It is a substantive reachability classification rather than a routine stationary moment computation.

## Limits and closest work
The proof covers deterministic measurable correlation-rate control in a fixed harmonic Gaussian model with constant stationary active-force variance. The motivating preprint's full text was inaccessible, so originality remains a qualified best-knowledge judgment pending a full priority review. Smooth-control and thermodynamic-cost optima are outside scope. The mathematical review described here is not independent validation.

Self-review: passed. Independent audit: not yet performed.
