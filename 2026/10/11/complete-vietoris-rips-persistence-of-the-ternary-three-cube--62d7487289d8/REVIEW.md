# Scientific review — complete Vietoris–Rips persistence of the ternary three-cube

## Correctness — PASS

The underlying 27-point metric and all threshold conventions are explicit. At scale one, all 27 coordinate triangles have free edges and collapse to a connected graph of first Betti number 28. At scale two, the flag condition is identical to independence for the triple categorical product; direct integer-bit enumeration produces 5,949 faces. The exact face-poset matching has 2,951 pairs with one critical vertex and 46 critical 3-faces. All 27,189 codimension-one incidences are checked for directed cycles, making the discrete-Morse wedge conclusion a complete finite proof rather than an extrapolation. Independent mod-two chain ranks agree. At scale three, the full simplex completes the proof and barcode. The built-in algorithm and Python execution are the relevant reproducibility assumptions.

## Originality — PASS

A closely relevant full-text source, Antolín Camarena–Carnero Bravo (2023), proves the case with a factor of order two (Proposition 25) and states the arbitrary-three-factor classification as Conjecture 26. The three equal factors of order three fall outside the proved theorem and yield the predicted 46 three-spheres. Goyal–Shukla–Singh (2019) treat two factors, whereas Adams–Frick–Virk (2022) provide a general Rips framework without this finite computation. The closest prior investigations of other Hamming-space topology involve different constructions and do not imply this barcode. Residual risk: an unindexed later proof or equivalent formulation in the theory of intersecting families may cover this fixed case; no global uniqueness claim is warranted.

## Value — PASS

This is the first uniform-alphabet, no-factor-two test of a specifically published topological conjecture. The exact 46-sphere homotopy type is stronger than a numerical Betti calculation, and the full integral persistence classification connects the conjectural combinatorial model to natural metric topology. The result is deliberately confined to a motivated finite benchmark; no general-alphabet conjecture is claimed.

## Closest literature and limitations

The closest explicit statement is Conjecture 26 of arXiv:2307.12401. Its Proposition 25 does not subsume this case; nor does the two-factor theorem in arXiv:1905.06926. The method is an exhaustive, reproducible proof for a fixed 27-vertex complex, not a symbolic theorem for all alphabet sizes. Related variants using intrinsic Čech complexes have different face sets and different homology. Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
