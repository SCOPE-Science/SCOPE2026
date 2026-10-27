# Mathematical review

## Correctness — PASS
The cyclic XOR difference is valid for every circumference, including \(1\) and \(2\). Substitution into the pseudoperiod condition gives exactly forbidden triples `100` and `111`, and the cyclic run argument forces blocks `10` and `110`. Even transition parity is necessary and sufficient for the two binary lifts. Double-counting marked zeros proves the exact integer coefficient \(\frac{2n}{n-t}\binom{n-t}{2t-n}\); the four-state transfer determinant gives the rational generating and zeta functions; Möbius inversion gives the primitive classes. The spectral argument gives the asymptotics. The standalone verifier checks every binary word through circumference \(18\), independent difference constraints through \(14\), matrix traces through \(70\), and Newton sums through \(180\). Finite checks are corroboration, not an infinite proof.

## Originality — PASS, with residual risk
The primary 2022 pseudoperiod paper defines the class and examines the rigid \((1,2)\) case and repetition thresholds for other pairs, including \((1,3)\). It does not provide this precise circular classification, the two-parameter coefficient formula, or primitive periodic-orbit counts. General symbolic-dynamics work supplies determinant methods for finite-state shifts but not these instance-specific coefficients. Searches for pseudoperiodic circular enumerations, alternative transition descriptions, plastic-constant growth, and exact coefficient sequences did not identify explicit coverage. An equivalent computation may nevertheless occur under unrelated terminology or in a preexisting integer-sequence table.

## Mathematical value — PASS
The pair \((1,3)\) is the first nonrigid two-element pseudoperiod with first displacement one; \((1,2)\) permits only eventual constant or alternating behavior. The result classifies *every periodic point* of this natural positive-entropy shift by its transition number, yields a closed all-length binomial law and complete primitive-orbit counts, and determines the entropy by a concrete plastic-constant renewal decomposition. This is a complete natural invariant, not an arbitrary low-length slice, though the transfer-matrix technique itself is standard.

## Closest literature and limitations
J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171, definition and Sections 2 and 5; M. Boyle and S. Schmieding, *Finite Group Extensions of Shifts of Finite Type*, arXiv:1503.02050, general determinant periodic-point framework. The precise enumeration may have an unlocated equivalent formulation. This is confined to a binary periodic-extension condition, not all pseudoperiodic or critical-exponent problems.

Self-review: passed. Independent audit: not yet performed.
