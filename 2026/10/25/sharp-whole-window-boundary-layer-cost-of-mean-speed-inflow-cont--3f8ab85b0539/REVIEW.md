# Self-review of the full-window boundary-layer law

## Correctness — PASS
The cost is a quadratic loss in a single control time after changing observation time to time of injection. Completing the conditional square gives the exact excess functional. The two eligible-time strips have widths \(O(\varepsilon)\), conditional delay deviations \(O(\varepsilon)\), and exact limiting integrals \(1/6\) and \(1/12\) on each side for the ordinary and clipped proxies. The full interior contributes only \(O(\varepsilon^4)\). Exact rational coefficient checks and full finite-width midpoint calculations corroborate, but do not substitute for, the proof. The condition \(T>2/\mu\) ensures the strips do not overlap for sufficiently small uncertainty.

## Originality — PASS with disclosed residual risk
Göttlich–Schillinger (arXiv:2609.01291) establish the stochastic conditional-expectation optimum and a mean-velocity interior approximation bound; the inspected full text does not supply either new whole-window leading constant. Earlier transport-inflow papers arXiv:2111.09674 and DOI 10.1002/oca.2689 have uncertain demand or chance constraints, not this finite observation window with random speed. Four scientific comparison families and direct record searches did not identify equivalent or stronger coverage. Related classical boundary-layer theory and the inaccessible source-code repository remain originality risks; absence of a search hit alone is not a proof of uniqueness.

## Value — PASS
The finite-horizon boundary creates a quantitatively different approximation regime: the complete-horizon cost is \(\Theta(\operatorname{Var}(V)^{3/2})\) even though the interior cost is \(O(\operatorname{Var}(V)^2)\). The sharp positive constants and exact factor-two improvement under clipping are relevant to deciding whether a mean-speed control can be used over the actual observation window. The statement is a motivated exact boundary classification, not a general guarantee for arbitrary demands or velocity laws.

## Limits
All assumptions and the precise sense of whole-horizon extension are in RESULT.md. An independent audit has not been performed. The associated source code and potentially unindexed equivalent classical asymptotics were not fully inspected.

Self-review: passed. Independent audit: not yet performed.
