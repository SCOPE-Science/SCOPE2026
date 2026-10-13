# Self-review

## Correctness
**PASS.** The claim is reconstructed from the descendant-code definition. Failure of strong \(\overline{2}\)-separability is converted exactly into containment of a generated forbidden set; inclusion minimization yields \(891\) four-word obstructions. A complete normalized search proves maximum size \(10\) and finds exactly \(20\) maxima containing \(000\). Word transitivity expands these to \(54\) labeled maxima and independently gives the incidence check \(20\cdot27=54\cdot10\). Every maximum is then replayed directly against the original coalition-intersection definition, and the full order-\(1296\) Hamming-isometry orbit and profiles are recomputed.

Risk: the extremal proof is finite and computational, but the complete standard-library verifier regenerates the obstruction system and the search from definitions rather than relying on a stored list or solver log.

## Originality
**PASS.** The foundational full text studies the same strongly \(\overline{2}\)-separable length-three objects and provides a construction that gives \(9\) words for \(q=3\), but it does not give a finite exact optimum or equality census. A later broader bound specializes to \(12\), and its main new length-three equivalence concerns coalition parameter \(3\). Exact-parameter and numerical-invariant searches found no implication-equivalent result for \(10\), \(54\), or the single-orbit classification.

Risk: an obscure or unindexed historical small-parameter enumeration may remain undiscovered.

## Value
**PASS.** The result closes a natural \(9\)-to-\(12\) gap at the first ternary alphabet size in the length-three SSC problem emphasized by the original construction. The complete extremizer census shows that the optimum has a unique Hamming-isometry type, which is stronger and more reusable than a single improved construction.

Self-review: passed. Independent audit: not yet performed.
