# Scientific review

**Correctness (C): PASS.** The upper bound follows because a positive response leaves at most \(h+1\) ancestor hypotheses; the lower bound follows from the chain threshold subproblem. In a full branching tree, the off-spine queries shatter the positive ancestor chain, and a sibling subtree supplies the full negative branch. This proves matching sharpness inductively for all heights, including separately checked base cases. The laminarity argument bounds VC dimension. Finite certificates and exact recurrences in the reproducibility files independently verify small cases, but are not the infinite proof.

**Originality (O): PASS, with residual historical-priority risk.** Published-record searches for tree cone, principal descendant, ancestor relation, thicket rank, laminar and Littlestone equivalents did not identify this height-law classification. Material readings of Malliaris–Moran's general dimension theory and Walker's full tree-dimension paper, including its main results, reveal related definitions and bounds but not a formula for the node-indexed principal descendant-cone concept class. Walker's leaf-family embedded tree dimension is a different parameter. The familiar information bound and laminar VC bound are prior tools, not claimed as new.

**Value (V): PASS.** The result isolates height rather than node count as a sharp, nearly exact online-complexity invariant on a natural family of hierarchical Boolean classifiers. It determines the two optimal extremal regimes for every height, complete regular trees at all parameters, and a uniform VC-two versus unbounded Littlestone separation. This is a motivated structural classification, not a numerical slice or renaming.

Limits: No exact invariant for each individual irregular tree, no uniqueness of extremizers, and no independent audit or comprehensive publication-priority certification. References: Malliaris–Moran, arXiv:2108.05569 (2021); Walker, arXiv:2203.12211 (2022).

Self-review: passed. Independent audit: not yet performed.
