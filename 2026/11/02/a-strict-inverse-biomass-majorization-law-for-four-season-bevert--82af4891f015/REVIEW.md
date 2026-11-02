# Scientific assessment: four-season inverse-biomass majorization

## Correctness — PASS

For all real \(r>1\) and \(0<L<H\), the exact reciprocal change of variables linearizes the Beverton–Holt recurrence and gives a unique globally attractive four-season cycle. The four inverse-biomass coordinates are a common affine scaling of pairwise sums of \(1,r,r^2,r^3\). Sorting these sums gives the three strictly positive grouped-minus-alternating majorization gaps \(\delta(r^2-r)/(r^4-1)\), \(\delta(r-1)^2/(r^4-1)\), and \(\delta(r^2-r)/(r^4-1)\). The equal full sum and strict convexity of reciprocation prove the mean comparison, while extremal inversion gives the opposed trough and crest comparisons. The six schedules are classified up to rotation. A standalone rational implementation independently verifies 41,615 assertions on 640 parameter triples. The proof, rather than these samples, establishes the universal result. No physical or stochastic model beyond the stated scalar recurrence is claimed.

## Originality — PASS within inspected evidence, with residual priority risk

The source equation, stable cycle and general periodic average formulas are established; see AlSharawi–Rhouma (2010), especially Example 3.4 and Theorem 3.5, and Yang–Sacker with Haskell (2013), Theorems 2.1–2.2 and Appendix C. The 2010 paper explicitly notes some mean changes under seasonal permutations and derives period-four maximum-harvest thresholds; the 2013 paper provides a general mean-versus-capacity formula. The proposed contribution is instead a strict inverse-biomass majorization comparison of all four coordinates, and the parameter-uniform mean-versus-trough tradeoff under two-valued permutations. The broader formulas allow special-case evaluation and thus present a priority/derivativeness risk; they were inspected for, but did not state, the comparison theorem. Later harvesting-quota permutation work concerns a different parameter and geometric mean. Full papers on related resonance and later quota permutations remained inaccessible, which limits the priority conclusion. Searches of relevant mathematical research records and accessible previously recorded claims found no matching statement; absence from those searches cannot prove novelty.

## Value — PASS

A seasonal management objective of maximizing average standing biomass conflicts rigorously with the objective of protecting the minimum standing biomass, even when the same two capacities occur at exactly the same frequency. The new convex-order statement captures a complete family of nonlinear penalties on reciprocal biomass, and the four-season arrangement is the first nontrivial cyclic comparison with two copies of each of two capacities. This gives an interpretable, parameter-uniform benchmark for comparing deterministic seasonal environmental sequences. It is not a prediction of population extinction, sustainable catch, or field outcomes.

## Closest work and limits

AlSharawi–Rhouma (2010), DOI 10.1155/2010/215875, was inspected as full OA technical text, including its comparisons. Yang–Sacker (2013), DOI 10.1080/10236198.2012.726988, was inspected as a 19-page full text, including the four-period appendix. Abstract-only comparisons were made for Allen–Kocic (2013), DOI 10.1080/10236198.2013.854779, and Al-Ghassani–AlSharawi (2020), DOI 10.1016/j.amc.2019.124905; technical coverage remains a residual risk. The theorem excludes heterogeneous growth, harvest, finite-sample observations, noise, and periods other than the two-valued four-season design.

Self-review: passed. Independent audit: not yet performed.
