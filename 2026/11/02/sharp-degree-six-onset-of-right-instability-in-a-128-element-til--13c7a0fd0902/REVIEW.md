# Scientific assessment

## Correctness — PASS

The ring and right-evaluation normalization are explicit. A necessary 24-by-24 evaluation-and-parity certificate has determinant \(2^{12}\) and mod-two rank 12; its Smith invariants force every coefficient entry even for all degree-at-most-five null polynomials. The symbolic lower-triangular reduction proves right stability for every entrywise-even null polynomial in arbitrary degree. A degree-six witness is checked on all 128 ring elements and has an explicitly nonzero right multiple. The executable checker independently reconstructs and validates all finite certificates. No numerical approximation, sampling, or extrapolation is used.

## Originality — PASS with historical-priority limitation

Wu (arXiv:2609.01150, Section 5) already constructs this ring and a sextic witness. **Neither its ring nor the sextic existence is a new claim.** The novelty claim is the sharp impossibility of any lower-degree witness, the coefficient-parity obstruction through degree five, and the all-degree right-stability lemma for entrywise-even null coefficients. Wu's full text was compared at the theorem and example level. Havlovec's characteristic-two counterexample (arXiv:2608.13251) and Werner's radical criterion (arXiv:2608.25853) do not establish these statements for Wu's characteristic-four ring. Targeted broader mathematical-record searches did not identify an equivalent result; this is not proof of global priority. A general polynomial-function identity or an earlier unpublished degree analysis could still imply the result.

## Value — PASS

The first degree of failure is a natural structural invariant for a minimal-order finite counterexample to a formerly conjectured two-sidedness property. The theorem replaces an isolated degree-six construction by a sharp threshold, rules out **every** lower degree at once, and explains this cutoff through a coefficient-parity phenomenon that forces right stability in every degree. The exact small integer certificate makes the boundary independently reproducible. The claim is deliberately specific: it does not assert a universal degree threshold or a classification of all rings.

## Research limitations and relationship

The source ring is due to Wu, and prior work already establishes that some null-polynomial right multiple is not null. The result is a low-degree optimality and structural-stability refinement. Historical priority requires further independent literature assessment; correctness does not depend on a novelty search. The symbolic proof covers the entire low-degree class; the exhaustive witness enumeration covers only this finite ring.

Self-review: passed. Independent audit: not yet performed.
