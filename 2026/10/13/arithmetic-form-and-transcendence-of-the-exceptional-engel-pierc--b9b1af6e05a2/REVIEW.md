# Independent mathematical audit

## correctness

PASS

Using the exact Pierce alternating-product normalization and least onset N of consecutive digits, split the sequence into a rational prefix and tail T_m. Beta integration gives T_m=int_0^1 t^(m-1) exp(t-1)dt, T_1=1-e^-1 and integration-by-parts recurrence T_m=1-(m-1)T_(m-1). Induction on derangement recurrence gives T_m=(-1)^(m-1)D_(m-1)+(-1)^m(m-1)!e^-1. The coefficient of e^-1 after attaching any admissible prefix is rational nonzero, so Hermite transcendence implies every exceptional x is transcendental; Ahn Theta maps onto complement C, so all algebraic irrational x are in its image. Independent exact recurrence checks m=1..100 and 45-digit alternating series comparisons m=1..11 corroborate the proof.

## originality

PASS

Ahn introduces topological exceptional set C and establishes countability/density and surjectivity onto complement, without the explicit affine-in-e^-1 parameterization or transcendence of all C. Prior Pierce-expansion papers treat other sequences or isolated numbers, not this complete exceptional set.

## value

PASS

The exceptional set in a new Engel–Pierce homeomorphism has a natural arithmetic question not answered by its topological description: the result evaluates all members explicitly in Q+Q^×e^-1 and excludes every algebraic irrational. The formula and image corollary may be directly reused in digit-expansion and descriptive-topology analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
