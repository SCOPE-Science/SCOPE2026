# Scientific review

## Correctness — PASS

The structural equivalence has an explicit proof in both directions: a white cycle cannot have a first forced edge; a nonempty white graph without isolated complete-graph vertices prevents any initial force; and an isolated vertex together with a white-tree leaf supplies a unique-neighbor force that can be repeated. The component recurrence follows by choosing the labeled tree containing a fixed label, and isolate inclusion–exclusion gives the exact polynomial. Formal exponential assembly counts isolated-component inclusion exactly. The maximum-edge case of a forest with an isolate is a tree on \(n-1\) labels and one separate vertex, so Cayley's formula proves the minimum multiplicity. Direct ordinary forcing and independent cycle/isolated-degree tests agree on 33,866 exhaustively checked initial sets at \(2\le n\le6\) and 20,480 deterministically sampled larger instances. The recurrence independently reproduces all small exact coefficients and the Cayley count through \(n=16\). The infinite claim rests on the proof, not on the finite tests. No unresolved correctness premise remains in the stated domain.

## Originality — PASS, with residual literature risk

The zero-forcing polynomial was introduced in arXiv:1801.08910; no triangular/Johnson/line-complete-graph enumeration occurs in its inspected relevant material. arXiv:2302.07757 proves the minimum **number** for Johnson graphs and constructs witnesses, but does not enumerate all forcing sets. arXiv:1508.07357 addresses a different, positive zero-forcing variant for the same graph, not the ordinary polynomial. The 2024 paper DOI:10.1007/s12190-024-02064-w addresses maximum failed-set size, not the full successful-set distribution in the accessible abstract; its full text could not be retrieved without interactive authorization. Searches for structural aliases, isolated-vertex forest complements, all-set polynomial, and minimum multiplicities found no equivalent claim in the checked sources. A hidden equivalence or uninspected result remains possible; search absence is not mathematical proof of priority. The scalar minimum \(\binom n2-n+2\), Cayley's tree count, and unlabeled forest recurrence are not claimed as original.

## Value — PASS

A complete and natural all-set classification is stronger than a single known forcing number. It gives every coefficient for an infinite classical graph family, a reproducible recurrence and formal generating function, and an exact number of minimum forcing sets via a transparent combinatorial correspondence. The latter multiplicity is not implied by knowing the minimum number alone. This is a substantive graph-enumeration result, though not a claim of broader results for every Johnson graph.

## Residual risks and limits

The full paper DOI:10.1007/s12190-024-02064-w was inaccessible under noninteractive access, so the comparison uses its abstract only. Classical forest enumerations do not alone identify the zero-forcing sets, but could appear implicitly in another paper. The small-instance calculations support but do not replace the infinite proof.

Self-review: passed. Independent audit: not yet performed.
