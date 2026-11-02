# Self-review

## Correctness — PASS

The stated index periods and fiber counts refer to complete periods, with separate formulas for \(p=2\), \(p=3\), and \(p\ge5\). Algebraic expansion of the four dyadic branches gives four 2-adic isometries with output scales \(4,2,4,2\), proving the observed fivefold fibers without a finite extrapolation. Each of the three 3-adic branches is an isometry, yielding exactly three indices per target. At odd primes at least five, Hensel uniqueness handles regular roots, a local quadratic analytic coordinate handles singular roots, and the conic collision count proves the prime-field image-size formula. Chinese remaindering proves the general claim. Direct exhaustive checks of \(205113\) fibers in \(55\) prime-power levels and \(27\) composite levels were consistent with every formula.

## Originality — PASS (with residual priority risk)

The general odd-prime cubic value-set formula is a special case of earlier Dickson-polynomial theory; this component by itself is not claimed new. Similarly, Ahmed (2019, Proposition 3.1) gives the exact least periods. Leyendekkers--Shannon (2011) tabulate tetrahedral behavior modulo three and four, and Sun (2013) provides criteria for cubic roots modulo a prime. The combined **all-modulus exact fiber distribution**, especially the uniform \(3\)-adic and nonuniform \(2\)-adic towers, is not stated or implied by the inspected full texts. Bremser--Gomez-Calderon (1991) address Dickson values over Galois rings, with some preimage formulas; the full text was unavailable and might cover part of the odd-prime calculation. These limitations constrain the priority claim; they are not concealed.

## Mathematical value — PASS

Tetrahedral numbers form a canonical integer-valued cubic. Determining exactly which residues occur is weaker than determining how frequently every target is reached. The theorem provides a complete multiplicative all-modulus answer, reveals the exceptional \(2\)-adic fivefold classes and the uniform \(3\)-adic branches, identifies all singular lifting contributions, and gives the exact number of representable residues for every modulus. These are natural arithmetic invariants useful in congruence constraints and additive questions about figurate numbers, rather than an arbitrary bounded computation.

## Sources and limits

See `RESULT.md` references and the `AUDIT.json` source-by-source comparisons. The proof depends on classical Hensel and finite-field collision results; independently formulated arguments are included. The automated finite check is corroboration, not proof. The 1991 specialist paper remains a literature access risk.

Self-review: passed. Independent audit: not yet performed.
