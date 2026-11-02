# Scientific review: exact cyclic Rule-73 image enumerator

## Correctness — PASS

The finding counts distinct indexed one-step outputs, not labelled predecessor walks. The four-vertex overlap-graph construction is exact for all periodic ring lengths, including one and two. Its reachable Boolean-relation automaton has exactly 735 states. The standalone verifier evaluates the full 735-component exact integer identity \(\sum_{j=0}^{34}q_jT^{40-j}h=0\). Because the identity holds as a vector, applying any further nonnegative power of \(T\) extends the recurrence to **all** lengths. The proposed logarithmic-derivative generating function has the same degree-34 denominator, numerator degree at most 39, and matching first 40 coefficients. Literal independent forward enumeration through length 14 covers the small-boundary cases. The checker was executed successfully and printed `VERIFY_OK`.

## Originality — PASS, with historical-priority qualifications

Jen (1989) derives general finite-window predecessor recurrences and classifies Rule 73; the accessible text does not state this exact same-period image counting function. Wolfram (2002) studies walls and localized dynamics of Rule 73. The available Elementary CA Zoo source reports finite cyclic-ring orphan censuses, not an all-length expression. Kang (2013) studies a different, long-distance Rule-73 sampling model. The explicit bit-complement conjugacy with Rule 109 was included in alias comparisons. Searches for the exact early coefficient vector, all-length Rule-73/Rule-109 image laws, and a corresponding rational generating function found no equivalent or logically stronger covered claim. That bounded evidence is not proof of historical uniqueness; older unindexed monographs, unpublished results, and the inaccessible client-side table remain risks.

## Value — PASS

An exact infinite family of one-step reachability counts is a natural structural invariant for a classical complex elementary cellular automaton, with direct significance to how its finite periodic state space is compressed. The explicit factored rational function and the all-length recurrence certificate give information unavailable from finitely many enumerated rings. The question and its precise counting observable arise from standard inverse-image dynamics, not from a selected arbitrary parameter slice.

## Closest sources and scientific limitations

The closest relevant sources are Erica Jen, *Enumeration of Preimages in Cellular Automata* (1989); Stephen Wolfram, *A New Kind of Science* (2002), page 699; and the finite-size *Elementary CA Zoo* Garden-of-Eden census. The result does not identify every predecessor, classify iterated images, or certify any numerical growth constant. The recurrence is a reproducible finite computation and formal proof, not an independently verified analytical decomposition of every Boolean-relation state.

Self-review: passed. Independent audit: not yet performed.
