# Scientific review

## Correctness (C): PASS

The proof reconstructs the quantifiers for every integer \(k\ge2\) and every positive norm-one \(f\in C([0,1])\). A function with orthogonal norm-one summands has \(k\) ordered peaks equal to one and exact separating zeros, so any approximation error majorizes the alternating witness objective. Conversely, an arbitrary witness of error \(\delta\) produces a continuous approximant through the clipping envelopes \(L=(f-\delta)_+\) and \(U=\min(f+\delta,1)\); its separator zeros split it into exactly \(k\) summands of norm one. Compactness proves closure; \(f(t)=t\) gives an unattained distance of \(1/2\); uniform continuity proves the all-\(k\) limiting law. The strictly subhalf vertex-transfer argument gives the rational finite formula. The standalone checker passed 940 rational finite test cases. No finite test substitutes for the general proof; the stated claims do not include rates of convergence or noncommutative extensions.

## Originality (O): PASS, best-knowledge

Taghavi, arXiv:2610.15167 (Theorem 3.2 and full proof), establishes qualitative closure and an exact zero-set criterion for the **two-summand** locus; his Theorem 3.1 and earlier arXiv:1301.3129 treat distance from the algebra identity. The current claim is a different, strictly quantitative all-input and all-summand distance problem, with a nearest-point obstruction and a limit invariant. Biswas et al., doi:10.1007/s41468-023-00126-9, characterize persistence critical pairings and variation on 1D maps; their inspected main theorem does not compute constrained norm-one orthogonal-summand distances or nearest points. Targeted published research-record queries and checks of the accessible prior same-slot claims, including source ID, alternate vocabulary, and implication comparisons, produced no covering statement. Failure of search is not a novelty proof: unindexed nonlinear approximation/persistence formulations remain the principal originality risk.

## Mathematical value (V): PASS

Normalized orthogonal positive sums are a canonical nonlinear object in \(C^*\)-algebra geometry. Exact distance from an arbitrary positive norm-one input, a complete nearest-point criterion, and the failure of proximinality despite norm closedness provide substantive metric structure beyond the initiating qualitative theorems. The all-\(k\) limit \(\max\{1/2,\min f\}\) shows a sharp complexity transition, and the finite rational formula permits exact reproducible computations for piecewise-affine data. The result is not a precomputed table or a consequence of just changing notation.

## Closest sources and limits

The nearest primary source is A. Taghavi, *On the set of orthogonal positive sums in a \(C^*\)-algebra* (arXiv:2610.15167, submitted 2026-10-10). Its closedness theorem is acknowledged. Earlier A. Taghavi, arXiv:1301.3129, and Biswas et al., doi:10.1007/s41468-023-00126-9, were compared for distinct metrics and related persistence interpretations. The statement is restricted to the interval algebra, positive unit-sphere inputs, and the indicated finite-dimensional discretization. Independent correctness and publication-priority checks are not claimed.

Self-review: passed. Independent audit: not yet performed.
