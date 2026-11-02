# Scientific review

## Correctness

PASS. The infinite-range VC dimension follows from geodesic obstruction and leaf witnesses; the unbounded online lower bound is an explicit product of three balanced threshold searches. The finite online upper bounds are exhaustive: at each version space, all coordinates and both outcome branches are considered by a complete inductive recurrence, with cardinality pruning only when mathematically necessary. Two independent concept enumerations and two different state representations yield identical values through twelve arm lengths; the root profile further checks all initial queries for the critical case. Limits: no extrapolation of exact online numbers to longer spiders; no external independent validation.

## Originality

PASS under accessible comparisons, with a genuine historical-priority caveat. The 2013 Munaro paper and earlier graph-VC literature address static shattering, which is not presented as new. Dossou-Olory 2019 counts connected induced subgraphs rather than computing online query complexity. Krishna et al. 2023 address discrepancy, a different optimization problem. Ghazi et al. 2021 give general closure bounds, not the exact finite spider cutoff. Actual semantic research-record searches and comparisons to accessible earlier claims identified no stronger/equivalent result. Search non-detection alone does not establish priority; an alternative range-query or online mistake-bound formulation could predate this observation.

## Mathematical value

PASS. The invariant is the natural worst-case adaptive shattering depth of all connected vertex ranges in a fixed branching tree. The exact first two-bit gap at twelve arm edges is a motivated threshold in the tension between concept entropy and query geometry, not an arbitrary extra table cell. The all-size constant-VC/unbounded-online contrast explains why static subtree shattering cannot predict its adaptive behavior. A stronger general formula is not asserted.

## Closest literature and limitations

See RESULT.md references and AUDIT.json for the inspected sources, equivalent-formulation and broader-coverage comparisons, and residual risks. The finite upper obstruction is computer-assisted and awaits independent validation.

Self-review: passed. Independent audit: not yet performed.
