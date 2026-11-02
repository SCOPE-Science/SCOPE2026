# Scientific review: complete size spectrum of reverse-complement-closed length-three non-overlapping codes

## Correctness — PASS

The statement fixes a labeled alphabet of \(2h\) letters, a fixed-point-free involution, word length exactly three, all ordered prefix/suffix comparisons (including a word against itself), and reverse-complement closure. The proof identifies the actual first-letter set \(A\), the complementary last-letter set, and the unused letters. For each fixed allowed \(A\), independent two-word middle-unused orbits contribute \((1+x^2)^{a^2(h-a)}\). Middle-used orbits correspond to oriented edges of a simple graph; a loop or opposite edge orientations are precisely the conflicts, while different first letters on the same directed edge are compatible. The factor for each vertex pair is \(2(1+x^2)^a-1\). Binomial inversion removes duplicate counts caused by allowing unused first letters, giving the stated polynomial.

The previously known top-degree coefficient and maximum are correctly recovered. For \(h=1\), the only codebook is empty. Direct independently implemented compatibility-clique enumeration agrees at alphabet sizes \(2,4,6\), counting every codebook (not just optima). A second program expands the formula through \(h=9\) and constructs maximum-code witnesses. Both actual scripts were executed and returned `VERIFY_OK` and `CROSSCHECK_OK`. These finite checks do not replace the all-parameter proof.

## Originality — PASS for the full all-size polynomial only

**Crucial known coverage:** Fimmel et al. (2023), Proposition 5.9, already proves the maximum size \(h^2(h-1)\), the number \(2^{h+\binom h2}\) of maxima, and their complementary partition description for all even alphabets. These are explicitly acknowledged as known consistency checks, not new results. Fimmel, Michel and Strüngmann (2017), Theorem 3.16/Table 2, already enumerates the four-letter reverse-complement closed codebooks of sizes two and four (12 and 8). The four-letter spectrum is therefore entirely known. These prior results do not state the exact **entire nonmaximal size distribution for arbitrary \(h\)**. In particular, the 2023 extremal proposition does not imply the six-letter intermediate coefficients 60, 726, 3072, 6276, 7344, 5256, 2304, and 576 numerically, and the general subset extension must handle codebooks admitting multiple maximal extensions. The new theorem explicitly gives this full polynomial through an allowed-first-set inversion.

Blackburn (2013) gives unrestricted length-three extrema; Stanovnik, Moškon and Mraz (2024) study unrestricted maximum constructions. Published indexed findings on length-five and length-six non-overlapping codes do not imply the all-size reverse-complement length-three spectrum. Comparison of claims, rather than just titles, found no same polynomial. Historical priority is not independently certified: unindexed tables or a sufficiently strong general generating-function result may contain it implicitly. The primary 2023 paper's complete Section 5.3 and the 2017 paper's Section 3.3 were inspected, rather than relying on abstracts alone.

## Value — PASS

The exact cardinality spectrum \(H_h(x)\) counts *all* feasible symmetric codebooks at each size, giving enumeration of random-codebook configurations, moments and tails under size-weighting, and showing how nonmaximal designs proliferate. Knowing only the optimal code size and its multiplicity cannot recover these intermediate counts. The full spectrum is a natural enumeration question in constrained self-synchronizing code design: it covers all even alphabet sizes with a nontrivial inclusion–exclusion mechanism to avoid overcounting subcodes. This is a substantive structural extension of the previously known extremal theory, not an arbitrarily chosen numerical slice. It does not assert better codes or a new extremal bound.

## Closest sources and limitations

- S. R. Blackburn, *Non-overlapping codes* (arXiv:1303.1026), §4, Theorem 7: unrestricted maximum; first posted 5 March 2013.
- E. Fimmel, C. J. Michel and L. Strüngmann, *Strong Comma-Free Codes in Genetic Information* (2017), Theorem 3.16/Table 2: already establishes all nonempty four-letter symmetric counts.
- E. Fimmel et al., *Diletter and triletter comma-free codes over finite alphabets* (Australas. J. Combin. 86, 2023), Theorem 5.3 and Proposition 5.9: the closest and strongest source, establishing all symmetric extrema and structural maximal descriptions but not this all-size polynomial.
- L. Stanovnik et al., *In search of maximum non-overlapping codes* (2024): general unrestricted extremal context.

Residual scientific limitations: only length-three words, even alphabet, fixed-point-free complement; no classification of codes modulo relabeling or formula for general lengths. Residual originality risk: an unindexed all-size self-complementary enumeration or an unstated but immediate specialization of a more general enumerator. The evidence supports best-knowledge originality, not independently established priority.

Self-review: passed. Independent audit: not yet performed.
