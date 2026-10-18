# Review: a residue-class transition for open-separating codes of clique subdivisions

## Correctness

**PASS.** The proof checks domination and open-neighborhood separation separately and on both sides of the incidence bipartition. Every OD-code selects at least \(n-1\) originals. Selected subdivision vertices correspond to a spanning graph having neither two isolates nor any isolated-edge component; the sole permitted isolate must be among the selected originals. The same characterization with no isolate exactly describes OTD-codes. The counting identities follow from this disjoint decomposition and inclusion-exclusion on isolated components. The minimum formula and optimal multiplicity use the exact maximum of \(\lfloor s/3\rfloor\) tree components of order at least three, with Cayley's tree count. Direct exhaustive testing on 2,131,008 subsets over four graph orders agrees with every coefficient; symbolic checks span nine orders. The finite tests are corroboration, not proof of the unbounded claim.

## Originality

**PASS, with bibliographic risk.** The foundational 2024 Chakraborty–Wagler papers introduce OSD/OD-codes and show that OD and OLD/OTD minima differ by at most one. Their inspected discussion of graph families does not state the clique-subdivision polynomial, its forest bijection, or the residue-class threshold. The 2014 open-neighborhood locating-dominating work concerns the total-domination variant and supplies neither the claimed all-size enumeration nor the OD/OTD dichotomy. Searches under *edge–vertex incidence graph of a clique*, *complete-graph subdivision*, and *central graph of a clique* found no covering published theorem. A broad related dissertation was inaccessible for full-text comparison, and previously unindexed literature may contain equivalent statements. The originality verdict is therefore a reasoned literature comparison, not proof of priority.

## Value

**PASS.** The result provides a natural infinite-family census of two closely related identification codes and a sharp periodic answer to the question of when their minimum cardinalities agree. The bijection to spanning graphs with forbidden one- and two-vertex components explains the polynomial and the residue classes, and also gives exact optimizer multiplicities. This goes beyond computing a generic inequality or a few small instances; the distinction between allowing one empty signature and requiring none creates an actual structural transition.

## Limitations

Only one-subdivisions of complete graphs are addressed. The source literature is not known to be exhaustive, and the inaccessible dissertation leaves uncertainty. Code runs test only finite orders. Independent evaluation is pending.

Self-review: passed. Independent audit: not yet performed.
