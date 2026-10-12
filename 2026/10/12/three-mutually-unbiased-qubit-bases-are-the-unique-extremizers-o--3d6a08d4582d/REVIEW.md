# Review

## Correctness
PASS. The Bloch parametrization is exact for rank-one qubit projective measurements. The function \(H(s)=h((1+\sqrt s)/2)\) has the explicit strictly negative second derivative displayed in RESULT.md. This proves both exact MUB extrema. The global upper comparison uses the exact sign average \(\frac18\sum_\varepsilon\|A^{-1}\varepsilon/\sqrt3\|^2=\frac13\operatorname{tr}((AA^T)^{-1})\) and the arithmetic-harmonic mean inequality; singular triples are handled separately. Equality conditions are tracked at every strict step.

## Originality
PASS. arXiv:1506.07709 explicitly reports numerical exploration of arbitrary triples of qubit measurements and states the general MUB extremality as Conjecture 1; it gives the tight MUB endpoint values but does not prove the global Shannon comparison. Searches using the source identifier, qubit/MUB/certainty aliases, Bloch-axis formulations, the exact endpoint constant, and the octahedral-POVM reformulation found no implication-equivalent result. The closest fixed-POVM entropy literature does not optimize over arbitrary triples of projective bases.

## Value
PASS. This settles the complete first nontrivial instance of a published entropic certainty/uncertainty conjecture, including both directions and rigid equality cases, for every triple of qubit projective measurements rather than a one-parameter or numerical family. The proof also isolates a reusable three-vector balancing lemma behind the certainty half.

## Closest literature and limitations
The defining 2015 paper supplies the conjecture and exact MUB endpoint values. Sánchez-Ruiz supplies complete-MUB certainty bounds, and the highly symmetric POVM literature treats the fixed octahedral measurement. None of those inspected sources gives the all-triples extremal comparison proved here. The theorem does not extend the claim to higher dimensions or to the separate variance conjecture.

Self-review: passed. Independent audit: not yet performed.
