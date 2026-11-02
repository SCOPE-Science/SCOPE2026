# Scientific review: circular composition-deck reconstruction

## Correctness — PASS

The statement concerns exactly the full multiset of weights of all cyclic windows at each length, modulo dihedral equivalence. A complementary-window identity reconstructs the long rows from the short rows and total weight. The finite claim checks all \(2^n\) words at every length through fifteen by a canonical-dihedral-orbit census; the orbit coverage check, Burnside count, two independent window-histogram implementations and explicit exact collision-fiber comparisons are included in the standalone verifier. It returns `VERIFY_OK`. The four non-complementary length-fifteen pairs are checked against all rotations, reversals and complements. The arbitrary-multiplier claim follows from the proved periodic-window identity, not the finite replay.

The exhaustive certificate is finite, and no general formula for all larger lengths or third-party proof certification is claimed. All code and proof dependencies are contained in the package.

## Originality — PASS, qualified

The closest inspected sources are Badkobeh–Fici–Kroon–Lipták (2012), on *existence* of jumbled factors rather than multiplicity profiles; Acharya–Das–Milenkovic–Orlitsky–Pan (2014), on composition multisets of *linear* strings; and Ota–Manada (2024), on *ordered* circular factor frequencies and minimal absent words. Neither changing linear words to circles nor discarding the order of letters within each observed factor preserves the previously proved reconstruction theorems. The finite six-pair classification, the complement-only phenomenon through length fourteen, the intrinsic threshold at fifteen and the infinite periodic witness are not asserted by their inspected statements.

Searches for circular equicomposability, Parikh-window histograms, homometric necklace ambiguity, and the displayed exceptional words were also compared with accessible published result records and the accessible prior claim archive. The nearest separately published two-multispectrum result uses ordered adjacent-pair counts and does not imply the all-length cyclic window-weight observation. A search that does not find a match is not a uniqueness proof; unindexed historical sources, an inaccessible specialized treatment, and the uninspected remainder of the later reconstruction paper leave a priority risk.

## Value — PASS

The problem is the information content of an idealized circular polymer-mass observation: for each fragment length the multiset of composition counts is available, but neither fragment origin nor symbol order is known. The result gives a sharp *first intrinsic* nonidentifiability length, every exceptional bracelet pair through that threshold, a surprising recovery at length thirteen, an exact small-block zero-error code capacity, and infinitely many genuinely ambiguous lengths. This is a natural reconstruction boundary and complete finite classification, not a routine additional table row or an arbitrary imposed slice.

## Limits and closest literature

Finite coverage ends at length fifteen. The observation assumes error-free complete cyclic fragment multiplicities; no noise robustness, general-alphabet extension or full large-length classification follows. The closest primary papers are arXiv:1206.2523 (first public 2012-06-12), arXiv:1403.2439 (first public 2014-03-10), and DOI:10.1587/transfun.2023TAP0015 (2024). All originality comparisons are provisional pending independent historical verification.

Self-review: passed. Independent audit: not yet performed.
