# Scientific review: exact beta-binomial degrees in recursive cographs

## Correctness — PASS
The parent selection and optional true-twin edge give the old-vertex conditional degree increment \((k+q)/n\). The new vertex is a random parent's old degree plus Bernoulli\((q)\). The resulting founder recurrence and the recurrence for the annealed degree histogram agree term by term with the beta-binomial recurrence, respectively for initial parameter pairs \((q,1-q)\) and \((2q,2(1-q))\). The proof treats initial size one, all degrees including zero and maximum, and all integer sizes. The variance formulas and beta weak limits follow from the beta-mixture representation. The embedded exact rational checker independently enumerates finite graph laws and verifies those recurrences; 10,821 assertions passed. Risk: no proof of a joint or quenched degree limit is provided or claimed.

## Originality — PASS, with residual priority risk
The starting graph process, graphon limit, and complete finite labeled-graph probabilities already appear in Féray–Rivera-Lopez (arXiv:2306.04278), including a strong general enumerative result which in principle determines all marginals by summation. Inspection of the available primary text did not identify the collapsed beta-binomial *degree* identities, all-size uniformity, or the founder/typical-vertex parameter-doubling law. Bassino and collaborators (arXiv:1907.08517) prove degree uniformity for uniform random cographs, a different graph law and an asymptotic rather than finite assertion. Scientific searches covering duplicates, cographs, beta-binomial degrees and the full graph formulas found no closer matching claim. A broader, presently unidentified theorem in duplication-graph probability could subsume this marginal calculation; searches do not establish historical uniqueness.

## Value — PASS
A random vertex's degree is a first-order observable for a graphon model; its exact finite law is therefore a natural invariant rather than a specially selected coefficient. The complete law holds for every size and bias, exhibits an exact uniformity at symmetry, and distinguishes old versus typical vertices by a factor-of-two shift in beta shape despite equal means. It sharpens interpretation of existing graphon limits and makes a precise comparison with uniform-cograph asymptotic degree laws. It does not rely on unsupported downstream applications.

## Limitations and literature
The result addresses annealed one-vertex degrees, not a deterministic empirical law. Foundational source: Féray and Rivera-Lopez, arXiv:2306.04278 (June 7, 2023). Closest degree-law comparison: Bassino and collaborators, arXiv:1907.08517 (July 19, 2019). Independent validation has not been performed; unresolved older or wider cloning-model results may affect historical priority.

Self-review: passed. Independent audit: not yet performed.
