# Same-model review

## Correctness

**PASS.** The proof reduces the final claim to an exact count. A loop-chain in \(\mathrm M_n\) has \(n-1\) required forward labels. Parity isolation permits at most two loop labels at any vertex, because three loops force a same-parity pair and swapping that pair leaves the matrix-unit product unchanged. Thus \(2m-1-(n-1)\le2n\), giving \(n\ge\lceil2m/3\rceil\). The focal construction reaches equality and its full-text proof supplies the needed parity-isolation property.

## Originality

**PASS.** The focal source was compared at statement and proof level. It states the finite level, constructs the loop-chain encoding, and explicitly says that the level is not claimed globally optimal, but it does not state the converse lower bound for all encodings of that same type. Eight published-finding corpus queries and targeted web searches covered the source identifier, the exact level, parity-preserving reorderings, matrix-unit paths, loop-chain aliases, and method-optimality language. No implication-equivalent record was found. The closest path-chain published-finding corpus hit concerns a different homological digraph problem.

Residual risk remains that this elementary combinatorial observation may exist as folklore or under unrelated path-ordering terminology.

## Value

**PASS.** The lower bound answers a natural methodological question raised by the source's explicit non-optimality caveat. It proves that the source's \(2/3\) matrix-size ratio cannot be improved by simply packing more loop factors into the same single-entry path extraction. Any improvement of the finite level must use a genuinely different encoding or argument. The claim is therefore a sharp structural limitation of the motivating proof mechanism.

The special Schatten-space level-\(2\) theorem is not in conflict: it shows only that other structures can do better in a narrower ambient setting.

Same-model review: passed. Independent audit: not yet performed.
