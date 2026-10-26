# Scientific review

## Correctness (C): PASS

The proof defines the error channel and distinct outcomes without ambiguity. Comparing only the previous four windows is justified by disjoint changed-position supports, giving an exact length-nine local score. The 256-state, 512-edge dynamic program is derived from this local score; its componentwise identity at lengths 12 and 18, verified by a standalone complete integer calculation, propagates to all longer lengths by max-plus homogeneity. Finite base cases and the six-periodic sharpness construction establish both inequalities. The certificate relies on reproducible code, not on a finite experiment misrepresented as an infinite proof. Residual risk is a shared implementation or specification mistake; the checker separately enumerates direct error balls for all short binary words to mitigate it.

## Originality (O): PASS, with residual risk

The closest primary text is Chen–Milenkovic, arXiv:2610.15701v1 (2026-10-11), inspected in its accessible HTML material concerning the channel definition, cyclic-permutation lower bounds, and general upper bounds. It does not state the exact window-five maximum nor imply the six-step extremal identity. Previously established radius-one results for a window of length four address a different parameter and do not entail the five-window result. Retrieved discussions of ordinary burst errors, pair-symbol codes, and limited permutation covers concern different error operations or different invariants. No inspected source yielded a stronger statement covering the claimed exact formula. Unindexed equivalent work remains a residual possibility.

## Value (V): PASS

The theorem gives a sharp, uniform finite-block volume for an entire natural channel model introduced in coding work on cyclic nanopore ambiguities, with a six-step arithmetic structure and an explicit periodic family of maximizing centers. Precise ball-volume bounds can be used when assessing sphere-covering and packing arguments; no particular optimal-code theorem is claimed. The all-length closed form and exact extremal witness are not implied by the source's general loose window bound or by the previously available four-window instance.

## Independent status and limitations

The statement is exact only for binary words, one five-symbol cyclic permutation, and no wraparound. The max-plus identity is computer-assisted and requires replay of the supplied checker. Originality search is nonexhaustive. No external specialist or independent verification has been performed.

Self-review: passed. Independent audit: not yet performed.
