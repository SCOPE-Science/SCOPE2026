# Unique pair-missing Dean extremizer at length \(58\)
## Finding
Use the alphabet \(\{0,1,2,3\}\) with inverse pairs \(0\leftrightarrow2\) and \(1\leftrightarrow3\). A Dean word is a reduced square-free word: it has no adjacent inverse letters and no nonempty square factor.

Among Dean words avoiding the length-two factor \(\mathtt{10}\), there is exactly one word of the published maximum length \(58\):
\[
\mathtt{3230123032301232123032301230321230123212303230123212301232}.
\]
It contains each of the other seven possible length-two Dean factors and misses only \(\mathtt{10}\).

Consequently, among all Dean words of length \(58\) that miss at least one possible length-two Dean factor, there are exactly eight words. They form one orbit under the eight alphabet permutations that preserve the inverse relation, and each of the eight words misses exactly one of
\[
\mathtt{01},\mathtt{03},\mathtt{10},\mathtt{12},
\mathtt{21},\mathtt{23},\mathtt{30},\mathtt{32}.
\]

## Assumptions and scope
A word is reduced when no adjacent pair is one of \(\mathtt{02},\mathtt{20},\mathtt{13},\mathtt{31}\). Square-freeness also excludes equal adjacent letters, so the eight displayed pairs are precisely the possible factors of length two in a Dean word.

The primary source already proves the sharp scalar statement that a Dean word avoiding \(\mathtt{10}\) has length at most \(58\), gives the displayed length-\(58\) witness, and deduces by symmetry that every Dean word of length at least \(59\) contains all possible reduced length-two factors. The new claim is the equality classification at length \(58\): uniqueness for the fixed missing pair and the resulting eight-word global orbit.

## Proof
Fix the forbidden factor \(\mathtt{10}\). The class of Dean words avoiding \(\mathtt{10}\) is factorial, so exhaustive prefix extension is complete.

When a letter is appended to a valid prefix, a newly created failure must occur at the new final position. Reducedness is checked against the inverse of the preceding letter, avoidance of \(\mathtt{10}\) is checked on the final pair, and square-freeness is checked by testing every even suffix for equality of its two halves.

The complete numbers of valid prefixes at lengths \(0\) through \(59\) are
\[
1,4,7,12,15,20,27,36,37,40,49,58,62,68,79,82,76,74,81,86,95,98,113,112,104,100,102,88,84,80,85,78,80,84,89,80,83,78,80,78,82,84,89,86,73,54,47,42,37,26,21,18,15,10,7,6,6,4,1,0.
\]
In particular, there is exactly one survivor at length \(58\) and none at length \(59\). The unique survivor is the displayed word. A direct scan of all its length-two factors shows that \(\mathtt{10}\) is the only possible Dean pair it misses.

For the global statement, let \(G\) be the group of alphabet permutations commuting with inversion. There are exactly eight such permutations. Their action is transitive on the eight possible length-two Dean factors. If a length-\(58\) Dean word misses a pair \(p\), some element of \(G\) maps \(p\) to \(\mathtt{10}\); the relabeled word must therefore be the unique fixed-pair extremizer above. Hence every pair-missing length-\(58\) Dean word is a symmetry image of the witness. The eight images are distinct because the witness misses exactly one pair and the eight images miss eight different pairs.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier uses two enumeration engines. The first applies only newly created suffix tests. The second independently rescans every candidate prefix for all inverse-adjacent pairs, every occurrence of \(\mathtt{10}\), and every square factor. Their complete survivor sets agree at every length through \(59\).

The verifier then checks the unique length-\(58\) word directly, reconstructs the eight inversion-preserving alphabet permutations, verifies their transitivity on the eight possible pairs, and checks that the eight symmetry images are distinct and each misses exactly one possible pair.

## Relationship to prior work
Badkobeh, Harju, Ochem, and Rosenfeld state that a computer search finds the longest Dean word avoiding \(\mathtt{10}\) to have length \(58\), and they print the same witness. They then use the alphabet symmetries preserving reduced words to prove that every Dean word of length at least \(59\) contains all length-two Dean factors.

The source does not state that the printed fixed-pair extremizer is unique, does not enumerate all length-\(58\) words missing a pair, and does not state that the equality set is one eight-element symmetry orbit. Exact-string searches for the witness and searches for “unique”, “equality cases”, and “missing pair” located the source but no published equality classification.

A separate result in the same source concerns absent factors of length three and critical exponent; it does not imply the length-two equality classification here.

## Limitations
The result classifies only the boundary case for missing length-two factors. It does not classify Dean words of length \(58\) that contain all eight possible pairs, nor does it alter the published threshold \(59\).

The original authors necessarily used a computer search to establish the maximum \(58\), so unpublished search logs could contain the same uniqueness information. No such published or indexed equality classification was located.

## References
1. G. Badkobeh, T. Harju, P. Ochem, and M. Rosenfeld, “Avoiding Square-Free Words on Free Groups,” arXiv:2104.06837v1, first public version 2021-04-14; Theoretical Computer Science 922 (2022), 206–217, DOI 10.1016/j.tcs.2022.04.025.
