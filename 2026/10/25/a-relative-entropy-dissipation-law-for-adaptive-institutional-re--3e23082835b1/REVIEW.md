# Scientific review

## Correctness (C): PASS

The exact differential identity follows from the two Bernoulli relative-entropy derivatives, the source equation \(d=\delta a_*S_N(x_*)\), and the linear negative-feedback factor \(-(1+u)(x-x_*)\). The strict sign is certified by \(S'_N(x)\le-1\) when \(N\ge2\), and the entropies blow up on every face of the open rectangle. The invariant-set argument isolates the sole possible omega limit at the interior coexistence equilibrium for arbitrary \(\epsilon>0\). The integrated equality and bound follow by integration and convergence. The accompanying script checked the algebra exactly in 6,048 rational instances; it is not the proof.

## Originality (O): PASS, with residual priority uncertainty

The primary 2023 paper [1] contains the model, interior equilibrium and local Jacobian stability, plus phase portraits for selected speeds. Its full HTML manuscript, including the appendix, was inspected. It does not present the weighted entropy function, exact dissipation, arbitrary-speed global interior attraction proof, or time-integrated cooperation deviation bound. The related collective-risk feedback game [2] has a different, generally nonmonotone payoff and admits Hopf cycles; its results neither cover nor contradict this monotone-kernel theorem. Published-record and literature searches using the model name, equivalent entropy wording and nonlinear feedback aliases found no direct implication. General monotone negative-feedback or evolutionary-game Lyapunov literature could contain a broader theorem that subsumes this result, so priority is not independently certified.

## Value (V): PASS

The motivating work's numerically observed coexistence stability becomes an exact global theorem throughout its interior parameter regime without a slow-fast separation, and the construction yields a finite upper bound on the accumulated squared cooperation error. This establishes that persistent oscillations require a mechanism beyond the source's positive bounded reward and monotonically decreasing incentive kernel, a substantive contrast with feedback games where cyclic behavior occurs. The result is not merely a local Jacobian calculation or a selected-parameter plot.

## Closest literature and limitations

[1] Hua–Liu, arXiv:2308.09530v1 (2023), Secs. 3–5 and Appendix: model, fixed-point classification and local stability. [2] Liu–Chen–Szolnoki, eLife 12:e82954 (2023), Eq. (5) and Appendix: a nonmonotone feedback payoff with possible limit cycles. Only deterministic interior coexistence, positive bounds and the precise source equations are covered. Other general feedback-system stability theorems are an unresolved priority risk.

Self-review: passed. Independent audit: not yet performed.
