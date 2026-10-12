# Self-review

## Correctness
**PASS.** The descendant definition reduces the finite problem to avoiding \(972\) forbidden triples on the \(27\) words. The bundled exhaustive verifier finds no valid ten-word code and exactly \(12\) nine-word codes, then directly rechecks every equality case. It separately verifies all pair-coordinate projections, enumerates all Latin squares of order \(3\), compares the two complete censuses, and exhausts all \(1296\) natural isometries. The finite proof makes no asymptotic extrapolation.

## Originality
**PASS.** The classical sharp bound \(C(3,q,\{1,2\})\le q^2\) and Latin-square constructions are prior work and are not claimed as new. The checked equivalent formulation, sharp-bound sources, exact-parameter searches, and Latin-square/IPP literature did not state or imply the surviving classification: every ternary equality case is Latin-square derived, there are exactly \(12\), and they form one natural-isometry orbit with stabilizer \(108\). The strongest residual risk is an obscure unindexed small-parameter census.

## Value
**PASS.** Equality cases of a sharp classical bound are a natural object. The result turns existence into a complete rigidity statement at the first nonbinary sharp parameter and gives exact labeled and quotient-level counts. This is more informative than recomputing the already-known maximum.

## Closest literature and limitations
The closest prior result is Bazrafshan's sharp \(q^2\) bound for three-row type-\(\{1,2\}\) separating hash families together with optimal Latin-square constructions. Staddon–Stinson–Wei supplies the exact frameproof/SHF equivalence, and Shangguan–Ge later restates the sharp regime. Batra–Singh is a plausible Latin-square neighbor but constructs stronger 2-IPP codes for different parameters. None of the inspected texts supplies the ternary equality census. The result is finite and does not classify general alphabet sizes.

Self-review: passed. Independent audit: not yet performed.
