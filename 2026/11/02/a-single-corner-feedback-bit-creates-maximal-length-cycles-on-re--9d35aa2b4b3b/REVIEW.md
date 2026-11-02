# Self-review

## Correctness — PASS

The claimed characteristic polynomial follows from an explicit path continuant, the binary tensor binomial theorem, a complete list of corner-return moments, and the matrix determinant lemma. The unperturbed operator is nilpotent by Frobenius, and the polynomial's unit factor is squarefree because its derivative is a pure monomial coprime to its nonzero constant term. The Fitting decomposition therefore provides exactly the claimed dimension of recurrent configurations and the fixed-iterate gcd formula over every finite characteristic-two field. The two Mersenne-prime special cases have separate exact irreducibility and arithmetic certificates, checked by an executable standalone verifier; a direct grid simulator checks the small cycle. Finite tests are corroboration, not substitutes for the proof.

## Originality — PASS, with historical-priority risk

Martin–Odlyzko–Wolfram (1984), Sections 4D and 4F, analyzes additive multidimensional and boundary-controlled automata but gives general polynomial techniques, not the present single-corner calculation for a null-boundary Mersenne rectangle. Ciandrini et al. (arXiv:0809.1526, Section II) analyzes directed random Boolean XOR networks and does not supply this rectangular characteristic polynomial. Temiz–Sah–Akın (2019), Sections 3–5, gives rule matrices and reversibility/rank conditions for two other hybrid diamond/cross families, not this characteristic and periodic-basin census. A related prior result for **square** grids with one corner feedback bit has only a one-dimensional periodic subspace, and its parameters do not include the present proper rectangles. The new formula is not a wording variant of these results. The computationally motivated primitive length \(2^{31}-1\) remains subject to unindexed equivalence risk and an inaccessible more recent paper on permutation XOR automata with different connections.

## Mathematical value — PASS

A single altered update bit on a natural zero-boundary grid converts universal finite-time extinction into a growing, explicitly counted invertible recurrent sector. On a 93-site rectangle it produces one period-\(2147483647\) orbit that attracts a fraction \(1-2^{-31}\) of all initial binary states, a sharp and nontrivial distinction from the unmodified dynamics. The result gives a structural all-parameter polynomial formula, not just a finite example or a minor numeric improvement.

## Scope and limitations

Only rectangles of width three and lengths \(2^b-1\), \(b\ge3\), are classified; finite characteristic-two fields are allowed. The two maximal-length polynomial cases are \(b=3\) and \(b=5\), not all \(b\). No complete nonperiodic transient-time census is asserted, and no external independent audit has been undertaken. The existing square-grid formula is prior work, not part of the new claim.

Self-review: passed. Independent audit: not yet performed.
