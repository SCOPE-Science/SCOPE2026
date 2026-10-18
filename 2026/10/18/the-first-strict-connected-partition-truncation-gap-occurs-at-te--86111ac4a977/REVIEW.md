# Scientific assessment

**Correctness — PASS.** Recursive unordered rooted-tree codes enumerate all rooted isomorphism classes by child multisets; center canonicalization then enumerates all free trees. Complete enumeration of every spanning forest, corroborated by two distinct component algorithms using exact integers, gives rank-layer collision counts. At order ten there are exactly \(106\) free trees, one colliding unordered pair at rank five, and no pair at rank six; the explicit pair has differing diameters and a rank-six partition witness. The complete checks and mathematical completeness argument are in `RESULT.md` and `verify.py`.

**Originality — PASS, with residual literature risk.** Awan (2026), Section 4, defines this exact invariant and proves the general half-order lower bound, illustrating the order-five case. The inspected text does not determine the first strictness or ten-vertex collision. Zeng (2026) reconstructs weighted proper-tree cores using other, fuller invariant data and gives cut-partition calculations, not this truncation threshold. Searches for the exact numerical boundary and equivalent descriptions, along with comparisons against relevant published research records, did not identify a stronger covering result. An unindexed table or supplementary computation remains possible.

**Value — PASS.** The result answers a natural sharpness question for a specifically defined reconstruction-depth invariant, identifies the first order at which the recently proved lower bound fails to be exact, and completely classifies the obstruction as one pair. Its two members even have different diameters, illustrating which structural information can be hidden from low-rank connected partitions. This exact first cutoff is useful without a claim about all larger trees.

**Limitations.** No statement is made for orders beyond ten; neither the general tree-isomorphism conjecture nor completeness of all external literature has been established. Computational exhaustiveness rests on the included verifiable finite generator and independent counting recurrences.

Self-review: passed. Independent audit: not yet performed.
