# Scientific assessment

## Correctness: PASS

The claim concerns precisely 720 cyclic permutations and 35 Boolean ternary queries. Every seven-query pattern is witnessed, all eight-query supports are excluded by a symmetry-reduced complete finite test with a safe necessary-size pruning inequality, and every path of a full depth-nine tree is witnessed. A depth-ten tree requires 1024 distinct concepts; 720 are available. Checks were replayed from the actual three files in this package. No generalization from finite sampling is involved.

## Originality: PASS, with historical-priority caveat

Direct comparison against the public P39-MATH-G study is particularly informative: it computes the same static invariant through six labels and explicitly leaves the seven-label dimension as an open value between seven and nine. This exact static classification and the distinct adaptive dimension are not implied by that interval, nor by the general VC/Littlestone bounds in Guingona et al. or Malliaris–Moran. The cyclic order representation of García-Colín et al. is equivalent at the level of query semantics but does not itself give the new extremal threshold in its inspected theorems. Older extendability and permutation-shattering papers may contain results not detected by these comparisons; independent historical-priority assessment is still necessary.

## Mathematical value: PASS

The seven-label value resolves an explicitly stated next finite case for the natural family of circular-order ternary queries. The difference between seven static and nine adaptive bits is nontrivial and identifies the first sharp adaptivity advantage, with complete constructive and obstruction certificates. The exact boundary is motivated by the existing incomplete seven-label shattering bounds, not an arbitrarily selected small subproblem.

## Scientific limitations

The proof computes exact finite values only through seven labels. It relies on code whose finite exhaustive logic is explained in the proof and can be independently replayed; a separate implementation or human audit has not been performed. Partial inspection of some historical prior sources leaves residual priority risk.

Self-review: passed. Independent audit: not yet performed.
