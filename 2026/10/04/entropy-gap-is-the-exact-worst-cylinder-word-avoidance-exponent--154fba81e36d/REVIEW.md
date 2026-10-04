# Review

## Correctness
PASS. The proof reduces the statement to two constant-factor sandwiches. The avoidance language is factorial, its word counts are submultiplicative, and its entropy is the survivor-shift entropy. Entropy minimality makes the survivor entropy strictly smaller whenever the survivor is nonempty. The empty word realizes the global avoidance ratio inside the follower and predecessor suprema, while bi-balancedness gives the matching uniform upper bound. For the measure statement, the invariant Gibbs inequality applied to the disjoint cylinders \([uw]_0\) and \([wu]_{-n}\) gives the stated bounds. The empty-survivor case is separately resolved by compactness.

## Originality
PASS with a stated folklore risk. The closest source, Hong--Kim arXiv:2609.33476v1, proves only the qualitative one-hit conclusion in Lemma 4.9, although its proof supplies the avoidance-language entropy gap. Earlier open-system work already identifies a global entropy-difference escape rate for irreducible shifts of finite type with Parry measure, so that global fact is excluded from the novelty claim. The searched finite-type, Markov-measure, conditional-escape, entropy-perturbation, and single-pattern literature did not yield the constant-factor worst-follower/predecessor sandwich or the exact worst arbitrary-cylinder Gibbs conditional exponent in the entropy-minimal bi-balanced setting.

## Value
PASS. Lemma 4.9 is the quantitative bottleneck used to force uniform returns in the motivating fresh work. Replacing eventual existence of one good extension by an exact exponential law gives a natural recurrence scale, namely the entropy cost \(\Delta_v=h(X)-h(Y_v)\), simultaneously for combinatorial extensions and Gibbs conditional probabilities. The statement also applies to the paper's entropy-minimal bi-balanced regime without assuming synchronization, so it is relevant to the structural boundary emphasized there.

## Closest literature and limitations
The global entropy-gap escape formula is classical for important finite-type/Parry settings and is not claimed as new. The theorem does not count occurrences crossing the history/block boundary, does not prove synchronization, and does not assert mixing or a hitting-time limit law. An unindexed folklore version of the short constant-factor argument remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
