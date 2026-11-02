# Scientific review

## Correctness — PASS

For each coalition \(C\), the welfare contribution is exactly \(2W(C)/|C|\). Removing nonpositive disconnected components cannot reduce welfare. The central nonstandard lemma replaces every connected path or cycle coalition of size at least four by a positive-weight matching and singletons: alternating edge classes give the path/even-cycle inequality; rotational averaging of the \((q-1)/2\)-edge matchings gives the odd-cycle inequality. The resulting connected tiles of sizes at most three are completely enumerated by the path prefix recurrence and six nonoverlapping cycle cases, including a separate triangle case. Unrestricted exact-rational set-partition checks on 2,209 connected instances and 580 disconnected instances passed, as did the two sharpness tests. These are corroboration, not the infinite proof.

## Originality — PASS (best-knowledge; priority risk remains)

The closely matching Hanaka–Ikeyama–Ono preprint gives a magnitude-dependent weighted treewidth algorithm, not a signed-valuations strongly linear path/cycle result. Bilò et al.'s short-coalition lemma is explicitly limited to unweighted trees; Bazgan–Casel–Cazals' degree-two remark concerns unweighted density; Aziz et al.'s weighted result is an approximation algorithm. Material sections of these primary sources and the comparisons in AUDIT.json were examined. An equivalent weighted path/cycle theorem in a differently named graph-partitioning or coalition-optimization source could still exist.

## Mathematical value — PASS

The three-vertex structural reduction is a useful exact boundary: negative friendships and arbitrary numerical magnitudes do not increase the required size of connected optimum groups on maximum-degree-two networks. A simple weight-independent exact linear-time algorithm follows for an infinite family of heterogeneous signed coalition games, substantially more specialized than the known pseudopolynomial weighted bounded-treewidth method. The positive three-path and degree-three claw show the precise changes in structural behavior.

## Scope and limitations

The claim concerns symmetric real edge valuations and utilitarian welfare only. It guarantees at least one canonical optimizer, not all optimizers or their count. Complexity is arithmetic operation count; representation/bit complexity is not asserted. No independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
