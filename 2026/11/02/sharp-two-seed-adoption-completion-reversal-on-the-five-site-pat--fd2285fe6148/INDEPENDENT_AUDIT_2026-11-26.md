# Independent mathematical audit

## correctness

PASS

An independent exact reproduction sums over every complete adoption order. The probability of an order is the product of the selected hazards divided by the total hazards; conditional on that order the mean of the dimensionless waiting-time sum is the sum of reciprocal total hazards, because the minimum exponential time is independent of the winning clock. The resulting symbolic aT values agree with the six frozen rational expressions, and exact polynomial sign checks show each excluded pair is worse than both {1,4} and {1,5} for every x>0. Reflection ties {1,4} with {2,5}. The remaining difference a(T15−T14) has numerator x(4x²−11x−8) over a strictly positive denominator, giving one positive zero (11+√249)/8 and exactly the specified three-way tie. Checking every pair on P3 and P4 proves strict endpoint optimality; on P2 both vertices are already seeded. This is for positive finite hazards and the expected all-adopted hitting time. Independent replay: python3 /workspace/reproduction/5.py (SymPy); passed for every pair on P2–P5 using exact arithmetic. The uploaded script was read, not executed: it uses an occupied-set recurrence, exact symbolic identities and finite rational spot checks.

## originality

PASS

No originality is credited for the discrete Bass hazard, exponential-race expectation equations, or the general idea of optimized seeding on paths. The closest verified same-hazard literature treats unseeded adoption probabilities and expected adoption levels, and the closest two-seed path classification optimizes expected final reach under independent bond transmission. Neither gives the exact completion-time crossover with two seeds or its smallest path order. Earlier advertising and seeding work could not all be inspected in full; that limits priority exclusion but is not itself adverse evidence.

## value

PASS

Placement matters here only through speed, since positive innovation makes eventual full adoption certain. The exact minimum-size counterexample to a rate-independent endpoint placement rule, including the location of the switch and all optimal pairs at equality, gives a motivated benchmark for time-to-coverage optimization. The narrow P5 result is useful because minimality and the whole positive parameter range are proven, not merely because the state space was exhaustively evaluated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
