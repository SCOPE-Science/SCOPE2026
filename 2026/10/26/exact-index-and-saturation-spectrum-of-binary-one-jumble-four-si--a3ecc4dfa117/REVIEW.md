# Scientific review of the binary one-jumble four-Simon quotient

## Correctness — PASS
The theorem is an infinite exact quotient result. Its critical steps are: recovering capped Parikh counts from short constant patterns; reducing order dependence to six balanced length-four patterns; converting one-jumble membership to shared ordinary length-three subsequences with balanced length-four subsequences; intersecting six explicitly enumerated obstruction sets; proving two singleton types require a symbol count of exactly two; and constructing all remaining signature types. Distinct capped Parikh cells are distinguishable, yielding the 66 count and the fixed-length 31-class saturation. The supplied direct checker verified 66 distinct witnesses and every binary word up to length twelve (8191 words), but these finite tests are not relied upon for the universal claim.

## Originality — PASS within examined sources
The primary October 2026 paper [1] defines precisely the relation and derives an index only in the parameter regime where the allowed jumbling number equals one less than the maximum pattern length. That index formula does not cover this nonextremal one-jumble four-pattern case. The June 2025 foundational paper [2] shows general finite index but no exact count here. Classical Simon congruence [3] has no allowed jumbling. The examined primary material, semantic record searches, and comparisons with nearby subsequence-universality and multispectrum calculations did not locate an equivalent or stronger result. Unindexed or differently stated prior work remains a priority risk.

## Value — PASS
This is a natural first order-sensitive binary one-jumble quotient, not an arbitrarily chosen partial census. A complete missing-pattern classification produces a global exact index, a simple all-length fixed-size spectrum and a sharp saturation threshold. The result quantifies exactly how much information short, partially reordered subsequences retain. It does not claim broader alphabet or higher-jumble generalization.

## Reproducibility, assumptions, and residual limitations
The packaged `check.py` and `WITNESSES.tsv` require Python 3 standard library only. The checker explicitly computes one-jumble pattern signatures from the LCS/deletion definition and checks every short word, independently of the proof's structural class enumeration. Infinite completeness comes from the case split and explicit representatives in RESULT.md. The source study does not exhaust every possible unindexed historical priority source, and independent scientific validation is still outstanding.

Self-review: passed. Independent audit: not yet performed.
