# Scientific review: identifying-code exchange rigidity in the Shrikhande graph

## Correctness — PASS
The size-four lower bound follows from counting distinct nonempty binary observation traces, and the size-five attainment is witnessed by an explicit code and each of the sixteen six-code template families. The complete finite classification follows from 136 explicit incidence-hitting constraints evaluated against all 4,368 five-subsets. A separate, direct trace-based implementation verifies precisely the same 96 sets. Both executable programs verify the 96 exchange adjacencies and their decomposition into sixteen induced six-cycles. Boundary conventions (closed neighborhoods, nonempty traces, unrestricted one-vertex swaps, labels modulo four) are made explicit. The finite proof makes no infinite extrapolation.

## Originality — PASS, with a stated residual risk
The closest prior result, Gravier–Moncel–Semri (2008), concerns identifying codes of clique Cartesian products and gives six as the minimum for the cospectral four-by-four rook graph; it does not classify minimum Shrikhande codes or their exchanges. Gravier–Parreau–Rottey–Storme–Vandomme (2015) develops general methods and bounds for vertex-transitive and strongly regular graphs; the inspected introduction and strongly-regular section do not imply these refined exact Shrikhande statements. Indexed findings on Shrikhande independence complexes, metric bases, independent dominating sets and zero forcing have different object-level admissibility conditions and provide no implication to this closed-neighborhood identifying-code census. Exact and alias-based mathematical-record searches found no covering theorem. No search proves global novelty: alternate terminology, unindexed articles and a Shrikhande-specific paper for which only bibliographic material was accessible remain risks.

## Mathematical value — PASS
A previously established pair of cospectral strongly regular graphs has different optimum identifying-code sizes, making the complete geometry of optimum feasible configurations mathematically motivated rather than an arbitrary count. The sixteen-cycle decomposition gives exact local-mobility and disconnectivity information that a minimum-cardinality statement alone cannot yield. It is a natural complete classification with a precise obstruction to optimum-preserving reconfiguration, and both the result and its finite scope are explicit.

## Validation limits
All numerical conclusions are exhaustively reproducible from two short standalone Python programs; they do not constitute an independent formal proof checker. Independent scientific assessment remains outstanding. An inaccessible possibly relevant source and non-indexed equivalents remain publication-priority uncertainties.

Self-review: passed. Independent audit: not yet performed.
