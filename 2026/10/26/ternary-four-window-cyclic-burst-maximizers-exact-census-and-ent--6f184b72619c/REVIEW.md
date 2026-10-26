# Scientific review: ternary four-window cyclic-burst maximizers

## Correctness
PASS. The ball consists of the unchanged word and at most three outputs per four-window. The period-six witness attains the bound, with six local contexts that can be checked exhaustively. Because a nontrivial permutation must change at least two positions, an appended window can collide only with its two immediate predecessors, giving a rigorous six-symbol-local transition rule. The complete 21-state canonical graph follows by exhaustive enumeration of the 243 five-letter words and their three extensions. Exact integer matrix calculations establish both the recurrence and generating function, with an independent direct output-set census through length nine. The finite checks are used to verify a finite transition graph and algebraic identities, not to infer an infinite conclusion without a proof.

## Originality
PASS, subject to stated residual risk. The closest primary source is Chen–Milenkovic, arXiv:2610.15701v1, particularly its binary-model scope and Sections III–V; it analyzes cyclic-permutation redundancy and constructions, not a ternary four-window extremizer-language census. Published binary four-window and nonbinary three-window computations have different hypotheses and do not imply this ternary classification. A separate paper on fixed-length burst Levenshtein balls permits replacement with unrelated inserted symbols, a larger and structurally different channel. Searches by model, parameter, synonyms and rational-enumeration claims found no equivalent; negative search alone does not prove uniqueness.

## Value
PASS. The exactly-four-position cyclic-permutation channel is explicitly motivated by four-base sensing windows. The smallest alphabet that can attain the simple full three-output-per-window bound at all lengths is nontrivial because windows necessarily repeat symbols over three letters. The classification of *all* maximum-ambiguity ternary inputs, its finite-state structure, rational census and exponential scarcity distinguish a complete natural family rather than an arbitrary fixed-length numerical case. The contribution does not claim a coding-rate improvement.

## Sources and limitations
Closest full text: Chen and Milenkovic, arXiv:2610.15701v1 (2026-10-11), Introduction and Sections III–V, VII–VIII; directly inspected as accessible HTML. Distinct-channel comparator: Xi, Sun and Ge, arXiv:2506.07817v1 (2025-06-09), abstract and model. Residual risks are unpublished or unindexed equivalent equality cases and independent validation not yet undertaken. The result is restricted to maximizers for the exact four-window model.

Self-review: passed. Independent audit: not yet performed.
