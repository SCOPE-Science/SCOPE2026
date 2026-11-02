# Review of the one-switch permutation-arch theorem

## Correctness — PASS

The proof establishes the exact shortest-absent length by one-permutation-block embedding and the constant-letter obstruction. An explicit greedy block lemma handles strict rank ascent versus weak descent and gives both directions of the pivot characterization. Independent stars-and-bars counts yield the rank-pair sum; the strict rearrangement inequality identifies unique phase-order extrema; a factorwise strict ratio establishes the balanced split. A unique highest-degree summand proves the asymptotics. `verify.py` independently checks 768 parameter combinations and 1,245,538 candidate subsequences, constructs subsequence sets separately for 56 examples, and checks 12 extrema and 441 balancing examples. These finite checks corroborate the infinite proof, but do not replace it.

## Originality — PASS, subject to disclosed risk

The most relevant primary papers are *Absent Subsequences in Words* (arXiv:2108.13968), *Tight Bounds for the Number of Absent Subsequences* (arXiv:2407.18599) and *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String* (arXiv:2504.21471). Their inspected results supply the general framework, global extremal values or enumerators for a specified input word. They do not state the complete one-switch rank-pivot classification, its arbitrary-second-order sum, strict unique conditional order extrema or the balanced degree-doubling result. Semantic research-record and literature queries identified neighboring subsequence-universality and binary extremal results but no equivalent complete statement. This is best-knowledge originality rather than a formal guarantee; the remaining risk is a hidden exact specialization in broader absent-subsequence literature.

## Value — PASS

The simplest possible nonperiodic change to fully universal permutation arches, one switch of the repeating order, has a completely classifiable forbidden shortest language. The all-parameter result exposes sharp mathematical structure: unique optimizers, a balanced phase optimum, and a change from polynomial degree \(q-1\) to degree \(2q-2\). This directly measures sensitivity of shortest missing-pattern complexity to a single ordering transition, rather than recomputing already tabulated values.

## Scientific boundaries

No conclusion extends to incomplete blocks, arbitrary source words, multiple switches, or independently audited priority. The counting and optimization tools used in the proof are classical.

Self-review: passed. Independent audit: not yet performed.
