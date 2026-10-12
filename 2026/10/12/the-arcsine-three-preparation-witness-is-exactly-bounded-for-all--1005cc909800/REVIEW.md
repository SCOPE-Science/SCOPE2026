# Review

## Correctness
PASS. The observable parametrization \(O=aI+b\cdot\sigma\) is exact for every binary qubit POVM, and the contraction condition gives \(\lvert a\rvert+\lVert b\rVert\le1\). Mixed states can be lifted to pure Bloch vectors without changing the two relevant correlations because two measurement Bloch vectors span at most a plane. The arcsine response has spherical gradient norm at most one. The remaining three-point estimate is reduced to a one-variable endpoint inequality, and applying it to both the observables and their negatives yields the absolute-value bound. The displayed projective strategy attains equality.

Risk: derivative formulas at endpoint correlations \(\pm1\) are interpreted by continuity. This causes no gap because the Lipschitz inequality holds on the interior and extends to the compact sphere continuously.

## Originality
PASS. The defining paper, arXiv:1010.5064v1, labels the bound as supported by “strong numerical evidence” and proposes it as a nonlinear qubit witness rather than proving it analytically. The full text of Brunner--Navascués--Vértesi, arXiv:1209.5643, explicitly describes the earlier approach as one whose quantum-witness validity generally had to be tested numerically and develops a different state-discrimination family. Bowles--Quintino--Brunner, arXiv:1311.1525, develops a different determinant witness under an independence assumption. Exact-expression and reformulation searches did not locate an implication-equivalent proof.

Risk: a later proof may be poorly indexed or phrased in a substantially different language. No searched source supplied stronger coverage or an implication that settles this exact five-term arcsine inequality.

## Value
PASS. This resolves an explicit analytic gap in an early prepare-and-measure dimension-witness construction. The result is not a parameter tweak: it upgrades a numerically supported boundary into a sharp theorem for the full qubit model allowed by the source, including mixed preparations and arbitrary binary POVMs. The proof isolates a reusable geometric mechanism—biased qubit observables produce one-Lipschitz arcsine functions on the Bloch sphere—and identifies the exact equality scale.

Self-review: passed. Independent audit: not yet performed.
