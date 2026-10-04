# Review: Exact binary length-nine optimum for two magnitude-one sticky deletions

## Correctness — PASS
The final claim is a finite packing equality. The lower certificate lists \(120\) length-nine words and the replay reconstructs every channel ball directly from maximal runs, checking pairwise disjointness. The upper certificate is a nonnegative rational weighting of received words with total weight \(120\); exact `Fraction` arithmetic checks all \(512\) source balls have weight at least \(1\). The disjoint-ball double-counting argument then gives the upper bound. No numerical tolerance, incomplete enumeration, or solver status is used in the proof.

Risk: the only normalization subtlety is that the source paper's Definition 6 says “at most” \(t\) affected run coordinates, while a later shorthand for an error-ball codomain is terser. The finding therefore states its channel explicitly and proves exactly that at-most interpretation.

## Originality — PASS
The primary full text defines the channel and proves general coding constructions, but the inspected results do not state this exact \(n=9,t=2,\ell=1\) optimum. Exact-value and alias searches for the value \(120\), the length-nine parameter, two affected runs, limited-magnitude sticky deletion, weighted sphere packing, and related repetition-error language returned no statement implying the claim. The nearest published-finding records concern ordinary deletion codes or asymptotic multi-deletion constructions, which do not dominate this restricted run-error channel.

Risk: a finite computation in an unindexed source could still coincide with the result; failed searches are not treated as a proof of novelty.

## Value — PASS
The maximum code cardinality is the central finite packing invariant of the channel introduced in the primary paper, rather than an arbitrary statistic. The exact value supplies a small-parameter benchmark for a model motivated by storage and sequencing, and the matching fractional certificate shows that a weighted sphere-packing method is sharp at this natural first moderate binary instance with two independently affected runs.

Same-model review: passed. Independent audit: not yet performed.
