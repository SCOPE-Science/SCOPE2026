# Review

## Correctness

The factor-cover argument reduces every length-\(2^k\) factor to a legal adjacent substitution-block pair and an offset. The exact \(T_k,G_k\) recurrence is derived from the two halves of each substitution image. The even/odd matrices follow by induction from \(k=2,3\), and their legal-pair maxima are unique. The separate argmax-set recurrence proves the stated offset formula. The accompanying script checks the recurrence implementation through \(k=20\), but finite checks are not the infinite proof.

## Originality

The closest full-text source, arXiv:1606.06935, gives the maximum sign-sum function and constructs maximizing factors, but the inspected proof does not classify the distinct maximizing factor words as unique at dyadic lengths. Related work on automatic-word properties, string attractors, initial nonrepetitive complexity, and 2-binomial factor classes treats different invariants. An older 1985 extremal-property source was available only through its abstract and metadata; its full-text coverage remains a residual risk. Search failure is not taken as proof of novelty.

## Value

Uniqueness of the extremal factor word is a natural structural refinement of the known maximum sign-sum function: the value alone does not identify the word or its block-boundary location. The dyadic lengths are intrinsic to the constant-length substitution, and the exact offset formula is an all-\(k\) statement rather than a finite sample.

Self-review: passed. Independent audit: not yet performed.
