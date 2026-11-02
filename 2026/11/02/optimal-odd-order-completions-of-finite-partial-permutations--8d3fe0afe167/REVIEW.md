# Self-review

## Correctness — PASS
All partial injections decompose into vertex-disjoint directed paths and cycles. Existing cycles cannot change; on the original set any completion corresponds bijectively to a permutation of path labels. A completed cycle has odd vertex length exactly when an odd number of its path labels represent odd-size paths. The count with only odd-size paths is the classical odd-cycle count \(c_a\). Reversible insertion of \(b\) labelled even-size paths into the \(a,a+1,\ldots,a+b-1\) slots proves the full formula and generating function. If no odd-size path exists, one fresh vertex supplies exactly one odd-size component, forcing all paths into a single cycle and giving \(b!\) labelled solutions. The checker exhaustively verifies labelled partial injections through size five and one-point minima through size four. No finite computation is used as a replacement for this argument.

## Originality — PASS within inspected evidence
Etedadialiabad--Gao (2026), Lemma 3.12, proves existence of a one-generator completion by closing paths individually after adding vertices. It does not state the one-vertex optimality boundary or counts of all labelled completions. Adin--Hegedűs--Roichman (2025), Section 1, gives the classical all-odd-cycle count \(c_a\), accepted as prior. The new theorem uses that established base but counts completions of *arbitrary prescribed partial maps* and identifies a complete parity-profile reduction. Published mathematical finding searches for path-block insertion, parity-profile completions, and odd-order partial-permutation extensions did not reveal an equivalent statement; the closest retrieved records concern different objects. A more obscure cycle-index restatement could cover the result and remains a declared priority risk.

## Value — PASS
The 2026 motivating problem is explicitly about possible extensions of partial permutations. The theorem answers a quantitatively different and naturally specified question: minimum additional universe size and the exact number of optimal completions. It classifies every finite one-generator instance, proves that a single new vertex always suffices when any extension is possible, and identifies a non-obvious compression of all path lengths to their two parity counts. It thereby strengthens an existence-only construction with exact, reproducible fibres and a generating function; it makes no claim about the unresolved multi-generator extension problem.

## Scope and limitations
Single injective partial self-map, odd-order permutations, labelled ground sets, and first-order extension of the map only. The unrestricted all-odd-cycle count is classical. Exact equivalents in unindexed earlier literature have not been ruled out, and independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
