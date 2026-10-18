# Mathematical review

## Correctness

**PASS.** Both exact-arithmetic checkers reproduce the 178365 long-root-anchored five-point configurations. They obtain cardinalities 8855, 42504, 69828, 46552, 10626 for zero through four short roots, and sharp doubled-coordinate determinants 192 for all-long and \(128\sqrt2\) for mixed types. The maxima of the two middle mixed classes are only \(128+32\sqrt2\), smaller than \(128\sqrt2\). All 42504 pure-long five-subsets have been checked, with 48 maximal ones and no two sharing four vertices. An orthogonal block-Hadamard matrix maps pure-long to equal-length pure-short configurations; the latter split into signed-permutation orbit sizes 16,16,16. Convexity of the determinant in each vertex and four-face nonincidence exclude non-generator maximizers, while the two inclusion arguments transfer the critical maximum to all positive scales. The code is an exhaustive finite certificate, not a substitute for the geometric reduction.

## Originality

**PASS under inspected evidence, with historical-priority risk.** The closest published 24-cell result determines the pure-long simplex spectrum and its 48 maximizing simplices, which are explicitly attributed rather than claimed as new. The classical type-\(F_4\) sources construct the two root sets, not the mixed-simplex extremum. Existing sphere-constrained optimal-simplex results do not determine the root-set mixed determinant threshold, the 96-fold equality at equal length, or the scale transition. The critical strict mixed-root gap is the essential additional claim; none of the inspected full texts covers it. An unindexed root-system or disphenoidal-288-cell table remains a residual priority risk.

## Mathematical value

**PASS.** The 48-root convex-hull deformation interpolates between two congruent but differently oriented regular 24-cells. The result gives a sharp continuous extremal law, complete equality and orbit classification, and a strict mixed-configuration barrier at the geometric equal-length transition. The phenomenon is an intrinsic discrete geometric optimization problem, rather than an arbitrary slice, a textbook deduction, or a recomputation of the known single-24-cell answer.

## Reproducibility and limitations

Execute `python3 verify.py` and compile/run `verify.cpp` with a C++17 compiler. Both independently implement exact determinant expansion; the supplied proof explains the reduction to the finite search and its implications. The statement is restricted to the specified root configuration, and an independent scientific audit has not been performed. Priority against inaccessible classical sources cannot be established definitively.

Self-review: passed. Independent audit: not yet performed.
