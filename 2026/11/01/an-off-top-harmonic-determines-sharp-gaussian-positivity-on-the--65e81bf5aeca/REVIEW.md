# Scientific review

## Correctness

**PASS (self-review).** The five powered-distance eigenbranches follow from the explicitly stated intersection array, Boolean inclusion filtration and polynomial recurrence. The analytic derivative bound makes the fourth branch strictly increasing on all nonnegative exponents. The exact rational-power certificate verifies opposite signs at \(71/200\) and \(89/250\) and strictly negative values for each competing nonconstant branch throughout that bracket; this combines with the classical Schoenberg theorem and fractional-power closure to prove the claimed sharp all-bandwidth Gaussian positivity and the endpoint nullity \(165\). The standalone checker independently reconstructs all 462 graph vertices, BFS distances, intersection identities, and representative full spectra. Numerical diagonalizations do not replace the exact sign certificate or analytic argument.

## Originality

**PASS under bounded source access.** Murugan's 2011 generalized-roundness work gives the first-singular-distance-power characterization for vertex-transitive graphs. Aalipour et al. (2015), Section 3.2, provide the odd-graph distance formula and general Johnson/Kneser eigenspace machinery. Neither inspected primary treatment establishes the exact \(KG(11,5)\) crossing, the rigorous four-competitor ordering, or the non-top \(j=4\) endpoint nullity. The closest accessible earlier harmonic bridge concerns the top odd-graph harmonic (\(j=5\) here) and a different smaller graph; it does not supply this result. Search failure is not a novelty proof, and an equivalent specialized computation in older literature remains possible.

## Mathematical value

**PASS.** Universal Gaussian positivity and squared-Euclidean rank are canonical invariants of a finite metric, and \(O_6\) is a standard, highly symmetric odd graph. The theorem identifies a genuine off-top mode obstruction and the exact sharp kernel exponent rather than just a finite numerical eigenvalue. Its endpoint embedding dimension \(296\) and spectral mechanism may inform larger odd-graph comparisons. The scope is one graph, not an all-order classification.

## Sources and limitations

Primary scientific sources inspected: M. K. Murugan, *Generalized roundness of vertex transitive graphs* (arXiv:1112.5657, Sections 2–4), and G. Aalipour et al., *On the distance spectra of graphs* (arXiv:1509.01196, especially Section 3.2, Theorems 3.9–3.10). The crucial root and sign comparisons are certified inside `check_odd6.py`, while the full mathematical argument is in `RESULT.md`. The result has not undergone independent review.

Self-review: passed. Independent audit: not yet performed.
