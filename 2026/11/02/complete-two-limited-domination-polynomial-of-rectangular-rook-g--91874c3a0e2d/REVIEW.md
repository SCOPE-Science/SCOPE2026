# Scientific review

## Correctness — PASS
The claim is a complete set-count formula for \(m,n\ge4\). For a selected grid square, the exact number of omitted neighbors is its omitted row degree plus its omitted column degree, giving the criterion \(r_i+c_j\le2\). The independent dominance criterion excludes simultaneous fully omitted row and column. Every feasible omission pattern is derived by a complete split into the cases with and without a full omitted line; the case split includes equality boundaries and permits coinciding exponents without confusing distinct configurations. Direct independent enumeration of all \(35,717,120\) subsets across four small grid sizes found exact agreement with the formula and the optimizer counts. The symbolic case argument proves the unrestricted result; finite checks are corroboration.

## Originality — PASS (priority provisional)
The closest same-invariant source is Tepeh (2026), Section 4 Proposition 6: it proves the minimum for \(K_{k+2}\square K_{k+2}\), including the known \(4\times4\) case. That result neither counts nor characterizes all feasible sets and does not imply their size distribution. Božović et al. (2026) introduce the notion and give generic bounds and the equivalent regular-graph \((1,t)\) formulation, not this enumerator. Mertens (2024) computes the ordinary rook domination polynomial, which does not encode the added selected-vertex capacity restriction. Equivalent rook/line/Hamming descriptions, near published results, and available mathematical finding records were queried; no stronger covering statement was identified. Search cannot establish historical uniqueness; non-indexed literature remains a residual risk.

## Mathematical value — PASS
The recent limited-domination parameter has already been evaluated at the level of minimum cardinalities for some Cartesian products. A complete all-set enumerator on a canonical two-coordinate Hamming/rook family is a substantially finer, natural invariant: it gives an exact finite structural classification of omission patterns, every cardinality count, and exact extremal multiplicities for all rectangular dimensions. The finite exceptional support shapes and whole-line obstruction expose why the constrained polynomial differs sharply from the known ordinary rook domination polynomial. This is not asserted to generalize to arbitrary graphs or to solve unrestricted parameter complexity.

## Caveats
The special \(4\times4\) minimum was previously known. Historical priority is provisional; independently performed mathematical audit is outstanding. The proof is specific to two-limited domination with both dimensions at least four.

Self-review: passed. Independent audit: not yet performed.
