# Independent mathematical audit

## correctness

PASS

Algorithm 2 of arXiv:2105.10190v1 supplies the quoted scalar angle and adjacent minimum. Sign alternation makes the numerator magnitude 2G and the denominator 1-G^2 at every transition from t=2, so the minimum agrees with the single-transition angle from t=3 regardless of startup. The cosine and tangent transform inputs are respectively |1-G^2|/(1+G^2) and 2G/|1-G^2|. These are invariant under G->1/G, and on 0<G<1 the first is strictly decreasing and the second strictly increasing; reciprocity gives the other half. G=1 is a continuous extension, not a defined evalution of the printed quotient: the extended coefficients are 1/2 and 1. Equating the inputs and dividing by G^2 gives z^2-2z-4=0 for z=G+1/G>=2. The two positive reciprocal roots and their quoted decimals check; the strict tangent advantage is between the roots, the strict cosine advantage is below the lower or above the upper root, and there is equality at the two roots. The exact direction flip is the same (angle pi) for every amplitude; the paper statistic instead measures an acute angle of slopes. The claim isolates the paper coefficient and does not assert the same output for the public implementation or any full objective trajectory. Frozen verification code was inspected, not executed; an independent root evaluation corroborated the algebra.

## originality

PASS

The checked paper and a subsequent AngularGrad summary provide the recurrence, not the quantitative equal-amplitude two-variant phase diagram. The closest comparators give other angular statistics or different alternating-gradient transfer laws. The bounded searches do not establish first priority. The supported distinction is the exact reciprocal symmetry, reversal in variant ordering, and opposite extremal response at fixed alternating directions for the paper recurrence.

## value

PASS

Equal-magnitude sign alternation is a controlled test of a mechanism described as responding to directions: all consecutive gradients are antiparallel, so amplitude is the only changing input across tests. The exact crossover and extremum analysis shows which of the two published variants damps or amplifies the relative step more, and how the ordering reverses under rescaling. That is useful for interpreting or reproducing the paper rule, beyond one numerical counterexample; it makes no claim of better training or of a defect in an implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
