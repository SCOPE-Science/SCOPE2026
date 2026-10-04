# Review

## Correctness
PASS. The proof separates the source construction into its binary and multi-outcome constraints, derives the general fallback lower bound \(W\ge3-2/L\), and checks an explicit rational parameter choice. The global 342-bit exclusion uses only inequalities valid for every admissible member of the stated family. The delicate numerical comparisons are exact rational/integer comparisons reproduced by `verify.py`, not floating-point evidence.

## Originality
PASS. The primary preprint gives 357 bits, explicitly says its numerical parameters are not optimized, and leaves the balance of covering size and truncation length unoptimized. It does not state a 343-bit parameter choice, the generalized multi-outcome constraint \(\varepsilon<\eta(3-2/L)\), or the family-wide impossibility of certifying 342 bits. Targeted searches for the paper identifier combined with “343 bits,” optimized qutrit simulation, covering radius, and truncation length found no equivalent claim. Earlier exact-simulation work did not provide a finite qutrit upper bound, while prior beyond-qubit protocols were approximate.

## Value
PASS. The classical message alphabet is the central resource in the qutrit simulation problem. Reducing the explicit worst-case guarantee from 357 to 343 bits shrinks the certified alphabet by more than four orders of magnitude, and the accompanying family-optimality result distinguishes a genuine limitation of this proof architecture from a merely untuned parameter choice. The result is a natural finite resource cutoff, not an arbitrary numerical slice.

## Closest literature and limitations
The closest source is arXiv:2609.04182v1 itself: its Remark D.5 supplies the parameterized binary fallback ingredients and explicitly leaves the communication optimization open, while its multi-outcome proof is written only for the fixed numerical choice. arXiv:2603.01255 gives lower bounds for restricted qutrit prepare-and-measure scenarios and predates the finite upper bound. Scientific Reports 16, 21297 (2026) gives approximate higher-dimensional simulation protocols, not exact finite qutrit simulation. The 343-bit optimum proved here is restricted to the source’s parameterized covering/truncation family and the universal cover estimate; it does not determine the unrestricted optimum.

Same-model review: passed. Independent audit: not yet performed.
