# Independent mathematical audit

## correctness

PASS

The random choices are independent physical positions. For t>=1 the failure numerator is the sum of plane-mass powers minus twice the sum of rank-one-subspace mass powers plus eight times the zero-mass power: a tuple spanning a plane, a line, the zero space, or the whole space is counted with respective weights 1, 3-2, 7-14+8, 0. In the simplex this is 7*3^t-14. The sum of plane occupancies is 21+4c0. If c0=0 and all occupancies are at most three, they equal three; the incidence Gram matrix 2I+J and total mass seven force every nonzero multiplicity to be one. Any nonsimplex thus has a plane with at least four positions, giving failure numerator at least 4^t > 7*3^t for t>=7. For t=3 through 6, independently enumerated all 3432 nonnegative eight-tuples of total seven (2696 full rank), testing rank via an independent triple of distinct nonzero vector types with nonzero XOR. For each exact subset of physical positions, a surjection from the reads to that subset counts precisely the tuples using all of it. Summing surjection counts over deficient subsets verifies the four baseline numerators, strictness, minima 24,192,1080,5280 and precisely the 42 stated profiles at every deadline. This is different from the frozen subspace dynamic program, which was inspected, not executed. Replay: node /workspace/branches/independent-checks.js (record 3 block). For two or fewer reads spanning is impossible; rank and the tails are invariant under row-basis changes and column permutations.

## originality

PASS

Credit the known probability formula, t=3 optimum, and later general non-strict rank-tail theorem. The distinctive supported contribution is the explicit strict Fano comparison by deadline, in particular the exact second-place gaps and all minimizers at four deadlines; the later non-strict result comes close to the order statement but none of the inspected results determines those gaps. The expectation census has the same second-place geometry for a different objective, not the four pointwise comparisons. Record dates are not used as proof of precedence.

## value

PASS

Single-deadline reliability is a natural objective when the read budget is fixed; expected stopping time does not determine it. The sharp quantitative gaps and identification of every nearest competitor at the first four nontrivial deadlines give a reusable benchmark for the smallest binary projective instance and distinguish the unique optimum from its next-best multiplicity pattern. The cutoff at seven is mathematically motivated by the plane bound, not an arbitrary search horizon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
