# Scientific review: minimal unique factors of weight-two binary words

## Correctness

PASS. The result explicitly defines overlapping occurrence counts, allows zero-length gaps, and correctly covers the shortest word `11`. Every minimal unique factor contains zero, one or two ones. Unique all-zero factors require a unique longest positive zero run; one-one factors have exactly two possible shortest distinguishing flanks, with an important exclusion when the flank itself is a unique zero run; a two-one minimal unique factor can only be the entire two-one core. The resulting four disjoint types imply the sharp inequality and equality criterion. The one-, two-, and four-factor classes have explicit disjoint gap parametrizations; the remaining three-factor class is obtained by subtraction from all weak compositions. The resulting rational functions sum exactly to the weak-composition series. The standalone verifier matched actual MUS factor sets for 8436 triples with zero-gap sum at most 35, and checked all four series through degree 35; the mathematical proof, not this finite check, establishes the infinite claim.

## Originality

PASS under the stated evidence and residual historical risk. The 2011 originating paper defines minimum unique substrings and discusses repeat duality and generic algorithms; the available material did not establish this constrained family's exact four-factor list or rational distribution, but its full text could not be read. The 2016 open-access full text gives a general run-count bound \(2m-1\), its Lemma 8 handles the unique-run subcase, and its focus is run-length algorithmic processing. It does not contain the weight-two enumeration or sharp four-factor bound. The related 2019 sliding-window literature addresses updates under window shifts, not this full fixed-weight census in the inspected material. Research-record and literature queries for minimal/"minimum" unique substrings, sparse two-marker words, exact weight-two generating functions, and aliases did not reveal this specific result. An unindexed equivalent specialization remains possible; search absence alone is not uniqueness evidence.

## Value

PASS. MUSs are a fundamental preprocessing object for shortest-unique-substring indexing. For sparse texts with only two informative markers and an arbitrarily long background, the formula describes every minimal identifier without expanding the word, gives a sharp **constant four** even though the word length is unbounded, and counts exactly how many such strings have each possible local-uniqueness complexity. The limiting one-third extremal density and four rational generating functions give structural and enumerative information not supplied by generic algorithms or coarse run bounds. This is a complete natural sparse-family classification, not an arbitrary finite sample or a renaming of the general bound.

## Closest literature and limitations

L. Ilie and W. F. Smyth (2011), DOI 10.3233/FI-2011-536: foundational definition and algorithms; publisher text inspected, full text unavailable. T. Mieno et al. (2016), DOI 10.4230/LIPIcs.MFCS.2016.69: full primary text inspected, especially Lemmas 7 and 8. T. Mieno et al. (2019), arXiv:1909.02804: sliding-window MUS and minimal-absent-factor setting, with limited primary material inspected. The theorem is only for exact contiguous occurrences in two-one binary words; it does not cover general weights, other alphabets, or pointwise shortest-unique-substring multiplicities. Independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
