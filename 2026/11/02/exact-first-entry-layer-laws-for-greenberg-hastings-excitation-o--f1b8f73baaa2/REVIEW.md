# Review of exact first-entry layers for Greenberg–Hastings dynamics on bridged cliques

## Correctness — PASS
The graph, synchronous update and boundary orders are defined exactly. The six-step first-entry bound follows from the closed 6084-state capped-color transition, which the package computes exhaustively, and the all-size 13-layer coefficient formulas are formal exponential-generating-function identities. The orbit count is also proved by a distinct local successor-color classification. The standalone direct implementation reproduces all coefficients for twelve complete finite graph state spaces, independently of the capped-state proof. No finite sample is substituted for the all-size identity.

## Originality — PASS (qualified)
Gravner, Lyu and Sivakoff's 2016 general irrotationality theorem already supplies the qualitative criterion and, on this graph, the *total* extinction basin. Doba's 2018 maximum-cycle-density theorem supplies the general eventual excitation-rate criterion. Neither inspected primary full text supplies the 13 first-entry layers, the number of bridge-supported three-cycles, their palindromic layer relation or the sharp six-step bound. Accessible published mathematical records and historical claims about related graph families were checked for statement-level implication. Unindexed equivalent enumerations remain a priority risk.

## Mathematical value — PASS
A single intercommunity bridge is a natural finite excitable medium with a bottleneck. Exact time-to-recurrence distributions and orbit counts distinguish finite-time propagation from long-time excitation. The non-obvious mirror law for three-cycle approach times and an exact sharp global arrival bound provide useful quantitative structure beyond the known survival dichotomy.

## Sources and limits
Primary comparisons: Gravner–Lyu–Sivakoff, arXiv:1610.07320 (2016), Theorem 3 and Sections 2 and 4; Doba, DOI:10.25088/ComplexSystems.27.2.101 (2018), Sections 3 and 6–8. Computation uses a finite exact symbolic reduction; the programs, their successful outputs and assumptions are included. No independent external audit or generalization to other excitation thresholds is asserted.

Self-review: passed. Independent audit: not yet performed.
