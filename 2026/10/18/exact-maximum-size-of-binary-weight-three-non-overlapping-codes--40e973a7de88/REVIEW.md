# Review of the weight-three synchronization-code theorem

## Correctness — PASS
The orbit upper bound follows because a codeword cannot be a proper power and two different codewords cannot be rotations of one another. The only nonprimitive weight-three words are triple repetitions when the length is divisible by three. The explicit construction is cross-bifix-free by comparing the number of ones in each nonzero-starting suffix against the corresponding prefix. Its exact count agrees with the primitive-orbit count in each residue class modulo three. The included Python standard-library checker independently exhausts all ordered overlaps and primitive orbits for lengths 3 through 30; the symbolic proof covers all lengths.

## Originality — PASS for the stated claim against inspected prior literature
Directly relevant publications on binary Dyck constructions, generalized non-overlapping codes, non-expandable families, and later unrestricted/balanced-code optimization were checked at the level of their definitions, constructions and main theorem statements. None of the inspected claims gives both the binary weight-three exact optimum for every length and an explicit overlap-free transversal of all primitive weight-three rotation classes. In particular, a known cyclic-orbit upper bound does not imply its attainability. A prior enumeration of unbordered shifts in weight-three words concerns single-word borders rather than compatibility among different words. Literature indexing and alternate terminology remain residual originality risks; no assertion of exhaustive worldwide novelty is made.

## Value — PASS
The parameter is a natural fixed-composition synchronization capacity: a code's weight-three constraint fixes a sparse symbol budget, while cross-bifix freedom prevents ambiguity from partial concatenations. The result determines its exact capacity for all block lengths and exhibits saturation of the strongest simple cyclic-orbit upper bound, rather than merely estimating the asymptotic rate or a small numerical instance. The explicit construction is elementary to generate. No claims about noise resilience or uniqueness of extremizers are made.

Self-review: passed. Independent audit: not yet performed.
