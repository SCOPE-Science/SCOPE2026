# Scientific review

## Correctness — PASS

The precise domain is the two-observation scalar, identity-budget, positive-definite-weight oracle. The proof reduces every causal policy to its three second moments, invokes the sharp Cauchy–Schwarz equality, and solves a strictly concave scalar maximization without a missing feasibility implication. The change of regime occurs exactly when its unconstrained ellipse maximizer crosses the physical boundary at zero initial excitation. The one-step gain, budget, and value branches agree at the transition. The singular dual calculation is separately derived; the exact quadratic-surd witness and parameter-grid verifier both pass. The proof establishes all quantified formulas without relying on grid exhaustiveness.

## Originality — PASS (residual risk recorded)

The motivating source [1] already states the **qualitative** mechanism: a singular Riccati control curvature can permit additional excitation when regular feedback does not saturate the budget. This general insight is not claimed as new. Neither its Section 4 nor its feasibility appendix gives the closed-form scalar boundary, frozen gain, initial energy law, exact value, or feedback-only gap. The present claim is those exact connected sharp invariants, not a rebranding of the general duality framework. Task-optimal exploration [2] and conditional-gradient Markov-chain design [3] use other criteria or objects. There remains a genuine possibility of an equivalent phase law implicit in older scalar constrained LQ or active-experiment-design work; literature-search negatives are not proof of novelty, and independent review is outstanding.

## Mathematical value — PASS

The precisely motivated gap is when a linear covariance oracle can or cannot be saturated by its regular Riccati family. The classification gives a parameter-dependent exact threshold, shows the feedback gain stops responding to increasing budget beyond it, and calculates an unavoidable positive value loss for pure homogeneous state feedback. These are natural finite-horizon structural invariants, not arbitrary sample counts or routine numerical recomputations. The result is limited to the scalar two-step problem, and does not imply a general algorithmic bound for full Frank–Wolfe outer iterations.

## Sources and limitations

[1] Bencherki, Lee, Matni, and Rantzer, *Optimal input design via Frank–Wolfe*, arXiv:2609.08751, Sections 2–4; Remark 2; Appendix Lemma 4 and proof of Lemma 3. [2] Wagenmaker, Simchowitz, and Jamieson, *Task-Optimal Exploration in Linear Dynamical Systems*, PMLR 139 (2021). [3] Mutný, Janik, and Krause, *Active Exploration via Experiment Design in Markov Chains*, PMLR 206 (2023). The result applies to exact arithmetic and the specified LMO, not the nonlinear inverse-covariance outer objective. Unexamined equivalences in prior specialized scalar LQ literature remain a risk.

Self-review: passed. Independent audit: not yet performed.
