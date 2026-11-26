# Independent mathematical audit

## correctness

PASS

Published Definition 1 uses the same variable and witness in both terms. For an internal arrow its justification set consists of the pairs with exponent difference equal to the displacement modulo the cycle length; for an external arrow it is empty. CRT gives the gcd test, since every integer difference has a nonnegative exponent-pair representative. For a fixed source the nonempty target sets are disjoint, so a nonempty intersection is maximal. Except in the singleton algebra (where the trivial clause gives the unique proportion), no justification is universal. The trivial clause admits two external arrows but does not mix external and internal arrows. Exchange and simultaneous reversal preserve the test. Each residue modulo gcd(n_i,n_j) has n_i²/gcd(n_i,n_j) internal arrows on cycle i, giving the stated ordered count. Equal cycle lengths give the specified equivalence classes; unequal lengths n_i>n_j let the zero arrow on the shorter cycle relate to both displacement 0 and displacement gcd(n_i,n_j) on the longer cycle, which are not related to each other. This gives the three-point minimum. A hand count gives 251 for (2,3) and 96 for (2,2). The supplied verifier's lcm reduction is exact as a representation of justification sets; the script was inspected, not run, and its expected output is not an independent log.

## originality

PASS

The published monounary semantics and transitivity question predate the result. The closest inspected distinct indexed contribution treats idempotent maps and overlaps precisely on identity permutations. The arbitrary-cycle classification, coupled count and equal-length characterization were not established by the compared sources.

## value

PASS

The gcd rule replaces a term-set maximization by a single compatibility test, determines the ordered count, and characterizes when a natural analogue of transitivity holds in the finite bijective subclass of a published problem. The contribution is the complete classification rather than the tiny obstruction in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
