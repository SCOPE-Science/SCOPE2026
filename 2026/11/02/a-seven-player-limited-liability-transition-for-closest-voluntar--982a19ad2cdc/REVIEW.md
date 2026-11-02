# Scientific review: closest voluntary Shapley payment flows in pair-synergy games

## Correctness — PASS

The statement is limited to \(2\leq n\leq7\), \(a\geq0\), and \(b>0\). The full-entry protocol, Euclidean objective, payments, and nonnegativity requirements are explicitly defined. Symmetry follows from uniqueness of the strictly convex nearest-flow problem. The consent inequalities and objective are independently derived from the payoff sequence, and exact KKT certificates certify each unique global optimum. In the constrained seven-agent phase the binding upper payment constraint, all remaining primal inequalities, nonnegative dual variables, and stationarity are algebraically verified. The squared-distance penalty is obtained by direct substitution, not numerical fitting. The exact-rational checker reconstructs the defining constraints and tests full-state Bellman comparisons. It does not claim finite checking proves any broader cardinality theorem.

## Originality — PASS, with residual publication risk

Lim (2026), arXiv:2609.20421, Section 4.1, Proposition 5 gives the parent quadratic program and three-player special cases. The parent reduction is prior art; the novelty here is its explicit pair-synergy active-set solution through seven players, the first *negative-entrant* optimum, the sharp price-of-nonnegativity threshold, and the exact constrained optimizer and penalty. We inspected that paper's main sections and Appendix A.6. The general population-monotonic allocation-scheme theory of Sprumont (1990) concerns monotonic feasibility and does not specify a Shapley-flow Euclidean projection or these multipliers. Published mathematical findings were searched for aliases including convex TU games, pairwise interaction games, least-squares voluntary payment adjustment, signed-to-nonnegative flows, and active-set thresholds. Nearby hits concerned different power indices or games and did not imply the present theorem. No equivalent statement was identified, but unpublished exact-QP notes and unindexed publications remain a real risk. No uniqueness claim is inferred merely from database partitioning or failed keyword searches.

## Value — PASS

Limited liability (nonnegative payments) is a motivated institutional restriction explicitly treated in the source problem. The theorem identifies the smallest player count within a complete seven-player cutoff where nonnegative-flow and signed-flow *closest implementations* differ, despite the continued existence of nonnegative voluntary implementations. It measures the correction as a sharp real-parameter phase boundary and an exact adjustment-cost penalty. This distinguishes feasibility of voluntary implementation from the geometry of the canonical least-squares solution and gives a reproducible benchmark for restricted cooperative payment design. Only the exact formulas and first-sign transition, not the source's general QP framework, carry the value assessment.

## Closest literature and limitations

Closest: Tongseok Lim, *Stable Allocations, Unstable Payment Paths: The Shapley Value and Voluntary Coalition Formation*, arXiv:2609.20421v1 (2026-09-17), especially Proposition 5 and its examples. Related: Yves Sprumont, *Population Monotonic Allocation Schemes for Cooperative Games with Transferable Utility*, Games and Economic Behavior 2 (1990), 378–394. No universal characterization is asserted for \(n>7\), alternative norms or entry rules, or general convex games. Unindexed equivalent work is possible.

Self-review: passed. Independent audit: not yet performed.
