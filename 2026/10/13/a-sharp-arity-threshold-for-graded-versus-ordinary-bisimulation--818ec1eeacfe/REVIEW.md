# Mathematical review: counting versus plain bisimulation compression

## Correctness — PASS

The theorem uses the correct bottom-up set and multiset signatures for the two modal equivalences on finite outward-directed trees. When \(q=2\), child-type support uniquely determines its size-two multiset, proving coincidence at all heights. For \(q\ge3\), the restricted family has precisely \(h+2\) ordinary classes and realizes the graded count recurrence \(g_1=q-1\), \(g_{k+1}=\binom{g_k+q-1}{q}\). Its strictly positive doubly exponential growth exponent is justified by \(g_2^{q-1}>q!\), giving enough disjoint subtree types at residual height \(O(\log h)\). A separate unrestricted graded-type census bounds every quotient by \(O_q(N/\log N)\), and at least \(h+1\) distinct heights bound every ordinary quotient from below. The resulting ratio has matching upper and lower bounds. Finite exhaustive and structured verifier checks agree with the argument; the infinite-height conclusion rests on the proof, not on testing.

## Originality — PASS with residual priority risk

The primary modal-logic papers of Bellas Acosta–Venema and Otto establish the language, bisimulation clauses, and expressive characterization, but the inspected relevant full-text sections do not state the sharp regular-tree arity boundary or the extremal comparison of two quotient cardinalities on the same coloring. Jacobs–Wißmann address minimization algorithms across coalgebra types, not this family-specific separation law. Direct searches for regular trees, set-versus-multiset type spectra, and counting/ordinary quotient gaps did not return an equivalent theorem. A previous ordinary-only complete-tree compression result supplies some background upper-bound methodology but neither the graded constrained-family lower bound nor the simultaneous quotient ratio. An implicit older coalgebraic/tree-minimization antecedent remains possible; the novelty claim is appropriately limited to this combined exact asymptotic tradeoff.

## Value — PASS

Both plain and graded bisimulation are standard finite-state minimization invariants, and their relative quotient size quantifies a concrete expressiveness and state-space compression cost of enabling successor counting. The theorem determines the sharp fixed-arity boundary at two versus three children and the full asymptotic order of the worst-case quotient-ratio penalty, with a construction attaining it at the smallest possible ordinary footprint. This is not merely a count of isolated small instances or a translation of an already-known single-quotient upper bound. The result may inform separation examples and regression benchmarks for modal and coalgebraic minimization, without asserting unverified broader applications.

## Boundaries

Fixed arity, binary coloring, complete finite directed trees and unrestricted graded counting are essential hypotheses. Exact finite-height maximizers and leading constants are not determined. The cited sources were inspected in relevant full-text sections, not presumed exhausted throughout all published literature. The computational checks are reproducibility evidence, not independent review.

Self-review: passed. Independent audit: not yet performed.
