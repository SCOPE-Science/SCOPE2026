# Scientific review

## Correctness

PASS. The shortest-absence length and forbidden-pair description follow from the greedy subsequence embedding through full two-symbol blocks. The two-coordinate recurrence matches, after a translation by \(1\) in each coordinate, the ordinary distinct-subsequence endpoint recurrence. Complementation by \(J\) and Cayley–Hamilton establish the coupled integer equations, and a solved inhomogeneous logarithmic recurrence gives the absolutely convergent growth constant. Checks cover all \(510\) binary inputs through length \(8\) and Thue–Morse iterates through length \(512\); correctness for all words relies on the proof, not those finite checks.

## Originality

PASS, with explicit residual risk. Kosche et al. (2021), Theorem 3.5 and Lemma 3.16, provide a general local characterization and concatenation rule for shortest absent subsequences, so the forbidden-pair description is not independently claimed as new. Flaxman–Harrow–Sorkin (2004) give extremal, not fixed-word dyadic, counts for distinct subsequences. The assessed contribution is the **exact cross-invariant equality** between absence after complementary-pair substitution and distinct-subsequence counts before substitution, and its **closed nonlinear Thue–Morse specialization including the limit base**. The publicly indexed nearest results on binary subsequence-universality distributions and Fibonacci extremizers address other quantifiers. A presentation under automata or scattering terminology remains possible; exhaustive priority is not asserted.

## Value

PASS. An apparent enumeration of exponentially long shortest-absence dictionaries collapses to a second-order integer recurrence, and its double-exponential behavior has an explicit limiting base. The bridge also lets algorithms for distinct-subsequence enumeration solve a different extremal-obstruction problem exactly. Both invariants are canonical and their relationship is mathematically motivated, beyond a finite table or renaming.

## Limitations and references

The argument is specific to binary complementary-pair substitution and complete Thue–Morse iterates. It does not count embedding multiplicities or generic morphic words. Sources materially compared: Flaxman–Harrow–Sorkin, *Electronic Journal of Combinatorics* 11 (2004), R8; Collins, arXiv:1310.7288; Kosche–Koß–Manea–Siemer, arXiv:2108.13968, §§2–3; Leroy–Rigo–Stipulanti, *Discrete Mathematics* (2017), §§1, 7–8. Generic SAS characterization is a known predecessor and remains a possible route to an alternative derivation.

Self-review: passed. Independent audit: not yet performed.
