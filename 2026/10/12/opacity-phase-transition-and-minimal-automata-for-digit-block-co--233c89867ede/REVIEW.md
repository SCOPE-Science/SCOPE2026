# Scientific review

## Correctness — PASS
For every base and nonempty pattern, the explicit prefix-matching automaton handles overlapping occurrences and the unpadded representation, including the output at zero for the one-letter zero-pattern. The period-based separator lemma constructs every state, and completing suffixes distinguish distinct prefix memories. Binary alphabet transitions enter each state under one digit when pattern length is at least two; larger alphabets admit conflicting two-step paths. The one-symbol binary boundary has shortest conflicting path length two or three. Applying Allouche–Yao [2, Theorems 1–2] proves the displayed opacity and state formulas without relying on numerical extrapolation. The embedded program checks 1,368 distinct patterns, 846,900 direct outputs, minimization, reachability, and graph conflicts.

## Originality — PASS, with residual risk
Abram, Hu, and Li [1] define the family and establish generation, non-pure morphicity, and suffix-memory separation (Lemma 12), which are credited. Allouche and Yao [2] introduce opacity, its universal intrinsic graph criterion, and several concrete classical examples (notably the binary one-pattern and 11-pattern). The exact full parameter-family opacity diagram, the zero singleton boundary, and uniform minimal state size are not statements of either inspected full preprint. Related published searches and mathematical record comparisons found no stronger covering classification; unindexed prior derivations remain possible.

## Value — PASS
The result completely settles a natural structural invariant of the whole block-counting family and exhibits a sharp distinction between binary and all higher bases. It also supplies the precise intrinsic state complexity, which is useful when separating automaticity, morphicity, and prefix-distortion behavior. It is not an arbitrary finite slice or an extrapolation from small examples.

## Limits
Only the prefix-distance opacity of [2], modulo-the-base counts, individual fixed blocks, and ordinary unpadded numerals are covered. In particular, quadratic opacity and sums of pattern counts are not classified. Computation is a consistency test and not a substitute for the symbolic proof. The claimed absence of covering literature is subject to indexing and publication limitations.

## Primary references
[1] A. Abram, Y. Hu, and S. Li, arXiv:2304.14595v1, 2023-04-28.

[2] J.-P. Allouche and J.-Y. Yao, arXiv:2404.13601v1, 2024-04-21.

Self-review: passed. Independent audit: not yet performed.
