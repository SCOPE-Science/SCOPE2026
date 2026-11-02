# Review of the coordinate-optimized Golay pair-distance theorem

## Correctness

**PASS.** The assertion applies to all permutations of the 24 coordinates, with a fully specified binary code construction and a single exact achieving ordering. Every cyclic five-coordinate window lies in a weight-eight Golay octad by the \(S(5,8,24)\) design, forcing four consecutive internal octad edges and the bound \(d_{\mathrm{pair}}\le12\). Exhaustive verification of all 4096 codewords of the displayed generator and all 759 octads gives a largest induced-edge count of four, so that ordering has distance at least 12. For other nonzero weights the one-run lower bound excludes a smaller distance. The standalone verifier also independently confirms all 42504 Steiner pentads and the complete pair-distance spectrum. This is a finite exact certificate, not a finite check substituted for an infinite argument.

## Originality

**PASS, subject to historical-priority risk.** Chapman supplies Golay octads and the design but no optimized symbol-pair metric. Cassuto–Blaum and Yaakobi–Bruck–Siegel concern symbol-pair read channels and general bounds; their examined scope does not address maximizing the minimum pair distance of a fixed noncyclic extended Golay code over every coordinate permutation. Chen considers permutation in covering-radius questions, not the present max-min invariant. Searches for Golay, pair metric, coordinate ordering, octads, and equivalent cycle-edge obstructions found no matching theorem; absence from indexed results is not proof against inaccessible prior work. The closest identifiable work uses the same metric but not the same invariant and optimization domain.

## Value

**PASS.** Overlapping-pair read channels are established coding-theoretic models, and coordinate ordering changes the performance of an otherwise fixed code in this metric. The main theorem determines the exact best achievable distance for an exceptional, classical high-symmetry code over its entire permutation orbit. The structural obstruction arising from the Witt five-design and its matching explicit construction are independently meaningful; this is not a routine Hamming-distance restatement or an arbitrary tiny parameter slice.

## Literature and risks

The closest studies are Cassuto–Blaum (2011), Yaakobi–Bruck–Siegel (2016), Chen (2022/2023), and Chapman (1997 survey). The original 2011 publisher source and the full texts of the latter three were inspected to the extent available, with source material identified in the structured audit. An unindexed earlier cycle-layout classification may exist. The universal claim is restricted to the extended binary Golay code under a cyclic pair metric; orbit counts and other read widths are unproved.

Self-review: passed. Independent audit: not yet performed.
