# Scientific review: two-width binary three-mer minimizer rankings

**Correctness — PASS.** The selector-change event has two disjoint alternatives: the former leftmost minimum leaves, or the entering last motif is strictly better. Counting constrained de Bruijn walks yields each exact numerator, and complete enumeration of all 40320 total rankings resolves the 1145 distinct two-width score pairs. Independent direct-bit and transfer-graph implementations reproduce the same two Pareto points (46,759) and (50,750), multiplicities 48 and 32, and a disjoint width-nine optimum. The proof is finite and does not make infinite-family claims.

**Originality — PASS, with residual risk.** The 2018 Marçais–DeBlasio–Kingsford paper already exhaustively calculates single-width minima through window 27; those scalar values are not claimed. Joint use of the **same** ranking across widths is a different quantifier, and the complete two-dimensional Pareto list is not implied by independent scalar minima. Full inspected 2017 and 2018 primary articles do not print this exact joint classification. The 2018 authors may have generated a nonpublic intermediate table containing it; unpublished and inaccessible supplements cannot be ruled out.

**Value — PASS.** Fixed minimizer orderings are commonly reused at different window parameters. This natural joint design problem needs a sharp compatibility/no-common-optimum statement and the entire set of undominated compromises, rather than separate optima that may be mutually incompatible. The exact frontier is complete and immediately identifies two optimal operating choices for both widths.

**Limits and source coverage.** The scope is iid equiprobable binary strings and length-three motifs. The 2016 hitting-set conference work was inspected via its abstract/date record, not full text; it defines a different objective. The model review is not external validation.

Self-review: passed. Independent audit: not yet performed.
