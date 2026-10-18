# Scientific review: monotone sorting-bottleneck relocation

## Correctness

PASS. The result takes the existing almost-sure finite-species sorting-time variational formula as a stated hypothesis and does not claim its proof as new. Each scalar objective has strictly positive second derivative and divergent endpoint values, giving a smooth unique minimizer. The envelope derivative is computed with its normalization \(1/K\) intact; ordered adjacent gaps force the strict pairwise derivative inequalities. The four-species limiting inequalities are proved analytically, and two exact-rational certified enclosures place the unique crossing in \((467/500,187/200)\). The standalone checker verifies the rational inequalities. Numerical root estimates are not part of the proof.

## Originality

PASS, qualified. Maga and Tóth's arXiv:2610.08135v1 establishes the maximum-over-cuts formula, and therefore supplies the necessary starting point, but the inspected text does not state the global no-reentrance theorem or analyze the single four-species bottleneck switch. Relevant inhomogeneous last-passage shape and permutation-invariance literature was also compared: their general shape frameworks do not directly select the maximum among contiguous species cuts under extreme-speed variation. An older, unlocated parametrized-optimization lemma or specialized sorting analysis could imply the same conclusion. The finding is a new structural consequence of an existing formula, not a new exclusion-process limit theorem.

## Value

PASS. Which species boundary determines a multispecies sorting time is a canonical observability question because the limit is a maximum over cuts. No-reentrance prevents repeated bottleneck reversals under one-sided speed tuning. The smallest-gap counterexample and transverse cusp establish a meaningful qualitative change in the bottleneck mechanism and clarify why nearest-neighbor speed gaps alone cannot predict sorting time. The three-species reflection argument proves that the four-species counterexample is minimal, not an arbitrary finite enumeration.

## Closest literature, evidence and limitations

The motivating variational representation is Theorem 1.2 of Maga and Tóth, *Microscopic sorting in a multispecies exclusion process* (arXiv:2610.08135v1, 2026-10-06). The inspected examples and proof do not contain the parameter-ordered derivative inequality or stated four-species phase classification. Emrah–Janjigian–Seppäläinen (arXiv:1908.09319) treats broader inhomogeneous last-passage shapes, and Bates–Emrah–Martin–Seppäläinen–Sorensen (arXiv:2506.12641) concerns LPP permutation invariance; neither inspected statement directly covers this parameter-driven sorting-cut selection. General sensitivity machinery can explain parts of the calculation, so priority is not independently established.

The theorem is for strictly increasing, fixed species speeds and a varying slowest speed; no finite-size cutoff, joint speed variation, or fluctuation result is asserted. Independent research-level assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
