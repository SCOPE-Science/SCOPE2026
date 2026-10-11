# Scientific review: sharp graph-metric numerical-index bound

## Correctness — PASS
The edge molecules generate the primal unit ball. Extreme dual graph-Lipschitz potentials have connected tight-edge subgraphs and hence integer vertex heights. The only possible slopes on an edge are \(-1\), \(0\), and \(1\). Nonzero slopes furnish numerical-radius norming pairs; zero slopes admit an explicit decomposition into two norming functions via the reweighted shortest-path potential. The resulting universal operator estimate is \(\|T\|\le2v(T)\). A concrete triangle operator has norm \(1\) and numerical radius \(1/2\), proving sharpness. All edge cases, quantifiers, normalization, and real-scalar restrictions were checked. The exact-rational reproducer provides finite corroboration, not the general proof.

## Originality — PASS, with historical risk
The 2009 foundational tree-metric article does not discuss finite-graph numerical index. The inspected 2023 numerical-index primary manuscript computes only two-dimensional free spaces and its applications to subspaces. The closest published graph-metric result establishes the **criterion for index exactly one**, which does not bound arbitrary nonbipartite indices from below. The published equilateral-family and five-vertex-wheel evaluations provide sharp special cases but not the global graph bound. Full relevant texts and statement-level implications were compared rather than relying only on title searches. Historical terminology outside these sources remains a nonzero bibliographic risk.

## Value — PASS
The exact constant \(1/2\) is a new dimension-independent robustness floor for a whole natural and unbounded class of transportation-cost Banach spaces. It gives a general norm-versus-numerical-radius equivalence for every operator, a substantive counterpart to previously known maximal-index characterizations, and a sharp boundary example. It is not a table lookup or an isolated small-graph computation.

## Limits
Finite, simple, connected, unit-edge graphs and real scalars only. No extension to weighted metrics or complex spaces is proved, nor does the theorem compute individual nonbipartite indices. The standalone checker treats only 48 graphs and does not certify the infinite graph-order quantifier.

Same-model review: passed. Independent audit: not yet performed.
