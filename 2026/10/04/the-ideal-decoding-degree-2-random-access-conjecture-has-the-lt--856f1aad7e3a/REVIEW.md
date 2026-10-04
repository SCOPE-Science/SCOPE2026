# Review

## Correctness

PASS. The recovery criterion is exact in the large-multiplicity process: a target is recovered if its sampled edge component contains a direct mark, a simple cycle, or a repeated pair support, and is not recovered when its component is an unmarked simple tree. The converse for a tree is witnessed by an explicit nonzero dual vector constructed recursively along the tree. Independent Poisson processes then give the exact finite-\(k\) tree-component survival formula. Fixed-size terms converge to the rooted-tree series, large component sizes are suppressed by the no-mark factor, and the whole survival curve is dominated by the target's no-direct-mark probability \(e^{-ar}\). The rooted-tree equation and integration by parts give the claimed integral. The packaged verifier checks the integrated finite-\(k\) expression and the KKT optimum from actual package paths.

Risks checked: repeated sampling of the same physical edge column is excluded only after the stated inner \(x\to\infty\) limit; repeated pair supports with distinct columns remain in the model and are correctly treated as recoverable. Finite experiments are not used as an all-\(k\) proof.

## Originality

PASS. The closest 2026 source explicitly states the claimed equality of ideal and degree-\(2\) peeling ratios/expectations as a conjecture rather than a theorem. The recovery-complete source supplies the finite graph construction and leaves unequal vertex/edge probability optimization as future work. Exact-phrase, numerical-constant, support-distribution, random-graph, and implication searches found no intervening source proving the conjecture. A separate 2026 random-access paper provides finite-parameter algorithms and small-\(k\) bounds but not this asymptotic recovery-complete limit.

Residual risk: an equivalent marked-random-graph argument may occur under different terminology in a source not surfaced by the searches.

## Value

PASS. This closes an explicit recent conjecture connecting two active random-access constructions and identifies the exact asymptotic performance of the best weight-\(1\)/weight-\(2\) tuning under ideal decoding. The result is structurally informative: it explains why cycle recovery, although strictly stronger than peeling at finite size, does not change the first-order limit once a positive density of direct marks is present. It also converts the earlier finite-\(k\) optimization problem into the same one-dimensional strictly convex objective already solved on the LT side.

Same-model review: passed. Independent audit: not yet performed.
