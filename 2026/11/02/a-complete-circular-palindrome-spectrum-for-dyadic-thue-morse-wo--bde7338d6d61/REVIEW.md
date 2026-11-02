# Scientific review

## Correctness
**PASS.** The proof reduces every even-length circular factor to one of two explicit injective substituted forms. The absence of a cyclic three-letter constant run implies the absence of length-five palindromes, ruling out all odd palindromes of length at least five. Characterizing palindrome versus antipalindrome preimages proves both lengthwise recurrences. The sole overlap of antipalindromic images is the two length-two factors; that exceptional subtraction is proved rather than inferred. Summing the recurrences gives two exact parity-dependent closed formulas. Direct factor enumeration independently confirms each recurrence through rank nine; it is not used as an infinite proof.

## Originality
**PASS, subject to historical-priority uncertainty.** The exact object is the set of distinct circular factors of each *fixed finite Thue–Morse iterate* of length at most one period, not the ordinary factor language of the infinite Thue–Morse word. The closest primary results concern the latter's palindromic and antipalindromic complexity (Allouche–Baake–Cassaigne–Damanik; Peltomäki; Blondin-Massé et al.). Simpson establishes general bounds for circular palindromes but an accessible summary supplies no exact finite Thue–Morse classification; full text could not be inspected. None of the material actually reviewed implies the two parity-oscillating total formulas or the complete circular lengthwise recurrences. An undiscovered source or theorem could still cover the claim.

## Mathematical value
**PASS.** Circular closure changes the palindrome language because factors may wrap across the boundary. The result settles a natural complete length-spectrum problem for an important classical automatic-word family, detects an unexpected alternating density, and demonstrates a reusable two-parity morphism technique. It is not a collection of ad hoc finite numerical observations.

## Reproducibility and limitations
`checker.py` performs independent direct enumeration at ranks one through nine and checks both full recurrence profiles. The general theorem is supported by the written induction, not numerical extrapolation. The theorem assumes full dyadic iterates over the stated binary alphabet, one traversal maximum. Simpson's full paper and an exhaustive priority audit were not available; no independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
