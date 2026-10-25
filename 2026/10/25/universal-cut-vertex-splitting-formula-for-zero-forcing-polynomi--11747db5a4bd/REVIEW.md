# Review of the cut-vertex splitting theorem

## Correctness

**PASS.** The proof supplies exact definitions for each of the four local polynomials, with disjoint A/B branch types and a separate root-activation flag. The essential monotonicity lemma establishes deterministic passive closure. Distinguishing initially-blue from initially-white roots yields all-A/exactly-one-B, and excludes precisely the nonactivating white-root cases. The resulting polynomial identity has correct coefficients for every size. The independent global enumerator was compared with the local-state enumerator on 1,974 complete rooted graph assemblies and 23 clique-bouquet checks. Exhaustive finite checks are corroboration, not the proof for infinite graph families.

## Originality

**PASS with residual bibliographic uncertainty.** Boyer et al. (arXiv:1801.08910, Section 6, Question 1) explicitly request cut-vertex splitting formulas, but their published decomposition is a disjoint-union product rather than a one-point-union identity. Menon and Singh (DOI:10.1016/j.disc.2025.114516) obtain coefficientwise graph-operation comparisons, not the present exact four-state factorization. German (arXiv:2605.10836) establishes path-extremal inequalities, not exact rooted splitting. Special-family enumerations, including friendship graphs and bridge barbells, do not logically entail the unrestricted formula. Search-based comparisons cannot establish uniqueness; older cut-vertex work on minimum zero-forcing numbers was not fully inspected, and independently published equivalent expressions may exist.

## Mathematical value

**PASS.** The result provides a constructive answer to a precisely posed 2018 structural problem for arbitrary one-vertex separators: the entire zero-forcing polynomial is composed from finite rooted-state data. It applies to graph families containing unrestricted cyclic blocks, not merely paths or cliques, and distinguishes whether activation of the cut vertex is needed. This is a motivated structural theorem, rather than an incremental small-graph census or a restatement of a special-family polynomial.

## Boundaries

The four rooted polynomials can require exponential-time enumeration; no efficient general algorithm or separator-size-two result is claimed. Only the ordinary zero-forcing rule is addressed. Exact duplicate publications remain a bibliographic risk. Independent mathematical audit and validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
