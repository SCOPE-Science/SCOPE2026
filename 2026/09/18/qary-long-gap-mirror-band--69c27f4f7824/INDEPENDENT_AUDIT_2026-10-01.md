# Independent audit — Conditional q-ary mirror band for linear-code weight distributions

Audit date: 2026-10-01 (UTC) UTC

Final disposition: **PASSED**

## Correctness — PASS

The proof is self-contained: the long initial gap forces an inclusion-minimal covered word to have weight \(d\); one scalar cancels at least \(\lceil d/(q-1)\rceil\) coordinates, forcing a second minimum-weight word, so any target word would have weight at most \(2d\). The displayed \([5,2,2]_q\) enumerator is also correct.

## Originality — PASS

The positive long-gap theorem was not found in the binary source, coding references, Resultary, or published SCOPE comparisons. A same-day published SCOPE record gives a stronger negative counterexample family, so the small counterexample component is not treated as original; it does not imply the positive theorem.

### equivalent_formulations

The ratio-cancellation theorem is not equivalent to the binary disjoint-support theorem.

Evidence: No positive q-ary long-gap theorem located.

### broader_coverage

No broader theorem found implies the positive band.

Evidence: The same-day record gives stronger negative counterexamples only.

### exact_database_or_table

The accepted positive theorem is not an exact database/table lookup.

Evidence: The negative example is covered by 7d5d46a2a226.

### claim_vs_prior_implication

Prior statements cover ingredients/negative boundary, not the final positive theorem.

Evidence: Neither implies the long-gap q-ary upper band.

## Source inspections


- **A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes** (arXiv:2609.20344): PRIOR_INGREDIENT. Material read: arXiv abstract/theorem description. Evidence: States the binary mirror band and binary disjoint-support mechanism.

- **Nonbinary counterexamples to the literal mirror-vanishing extension** (Resultary 2026/9/18/SCOPE-qary-counterexamples-mirror-vanishing--7d5d46a2a226): COVERS_NEGATIVE_COMPONENT_ONLY. Material read: complete RESULT.md. Evidence: Gives a stronger all-q, all-d negative family and includes the smallest ternary instance.


## Scientific value — PASS

The positive theorem gives a natural alphabet-dependent replacement for a newly proposed binary mirror phenomenon and quantifies the surviving cancellation over larger alphabets.

## Residual risks and limitations


- The binary source is very recent. The negative counterexample component is already covered by a same-day published SCOPE record; acceptance is for the positive long-gap theorem.
