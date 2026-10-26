# Scientific review

## Correctness — PASS

The greedy-arch criterion is a known characterization and is also justified in the proof. The prefix deficit \(q(k-r)-s\) has both a disjoint-arch lower bound and a matching explicit completion. The zero-slack branch skips exactly the infeasible letters; the positive-slack branch includes all possible symbols. The iterative DFS visits every feasible prefix in lexicographic order. Along the two root-to-leaf path fragments separating consecutive outputs, the number of fresh missing-list allocations times their \(O(q)\) cost is \(O(n)\), completing the variable-alphabet bound. The supplied independent direct enumeration comparisons cover 128 small parameter instances, and long-word/large-alphabet edge tests check additional boundary behavior.

## Originality — PASS, with risk

Adamson (2023) proves \(O(nq)\) delay and asks explicitly for \(O(n)\). The present method achieves that bound uniformly in \(q\), without expensive initialization. Adamson–Gawrychowski–Manea (2024) proves stronger succinct-output delay for explicit directed graphs and prefix-closed regular languages, but does not provide a linear-size alphabet-dependent graph for this variable-alphabet, fixed-length acceptance problem; the ordinary full-subset arch DFA has exponential \(q\) states. Adamson et al. (2023) treat general regular-language universality; the 2024 absent-subsequence paper enumerates a different set of objects. An overlooked implicit-automaton translation or previously published specialized linear-delay enumerator is a residual novelty risk.

## Value — PASS

The result directly answers an explicit research question in formal-language enumeration and obtains the information-theoretically optimal delay for writing each full word. It improves the known bound by a variable alphabet-size factor, while removing the previous dynamic-programming preprocessing. The proof gives a simple, reusable structural technique for enumerating words subject to greedy-arch completion constraints, rather than a narrow numerical improvement.

## Scope and limitations

The claim is explicit lexicographic output, not ranking/unranking or succinct constant-time output. Proof assumes constant-time arithmetic on \(O(\log(n+q))\)-bit indices; the finite checker does not independently establish asymptotic bounds.

Self-review: passed. Independent audit: not yet performed.
