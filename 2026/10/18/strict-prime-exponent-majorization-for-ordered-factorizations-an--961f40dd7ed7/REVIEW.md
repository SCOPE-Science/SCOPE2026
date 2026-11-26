# Independent mathematical audit

## correctness

PASS

The frozen assumptions only require exactly one representation of integers in the interval and omit the exclusion of extra sums. Under that literal condition, n=6 and m=2 admit infinitely many tuples: ({0,1,2,M},{0,3}) works for every M>=6. The asserted finite formula is false on that reading, even though the standard term suggests the intended exact sumset. The complete replacement RESULT.md explicitly requires a bijective addition map onto the interval, hence no extra sums and product of cardinalities n. This matches the primary source of the Stirling transform, now checked on the corrected claim. For example, at n=6 the size-two part is {0,d}, and its translates by the size-three part must partition [0,5]. Along residue classes modulo d the partition requires even chain lengths, forcing d=1 or 3. Each gives one tiling and either part order, in agreement with 2c_2(6)=4. For the proof, ordered factorizations are exponent rows with no zero column, giving the stated inclusion–exclusion, including c_1=1. Conditioning on outsider-prime assignments leaves mandatory slots for the two selected primes. Degree profiles of their slot generating functions are products of complete homogeneous functions; in two variables the one-step coefficient gain is the Schur coefficient of (a-1,b+1), nonnegative by Pieri. If more than a+b slots are mandatory, both monomial counts are zero. For strictness, occupy min(h,S) slots with the outsider units. With zero or one mandatory slot use two positive degrees a-1,b+1; with q>=2 mandatory slots balance a+b over them, giving largest degree at most ceil((a+b)/2)<=a-1. This makes the profile dominated by the two-row shape and gives a positive Kostka coefficient. The positive Stirling transform transfers strictness since its j=m coefficient is m!. Repeated balancing decreases the sum of squares until the balanced profile; reversing transfers from any non-spike profile concentrates it and strictly decreases all counts. For strict support splitting, use any old allocation in which the prime to be split appears in two slots, possible for h<=k. The greedy split is injective by merging the slots' prime exponents; a distinct split exists because both new exponents are positive and the old exponent has at least two positive slot capacities, permitting a unit transfer from a used slot to a distinct slot with spare capacity. This proves strictness at every stated h; it does not extend strictness to length one or to j,m>k. The uploaded checker was inspected without execution and applies an algebraic transform; its finite checks cannot repair the definition or establish the universal proof.

## originality

PASS

Reassessed for exact interval sum systems. The distinct claim is strict balancing and the matching extremizers simultaneously at every individual factorization length, with consequences for higher-part systems. The aggregate and two-part cases, the transform, and the binomial enumeration are credited as known, including the aggregate priority clarification in the replacement.

## value

PASS

For the corrected exact interval problem, the coefficientwise theorem gives a genuine distributional comparison hidden by the known total count: any fixed nontrivial length, and any higher-part system counted by the positive transform, exhibits the same strict spike-to-balanced ordering. At varying support it also gives a strict ordering under splitting, with common extremizers. The balancing and extremum classification apply to a natural family of counting problems and not merely to a table recalculation or the already known two-part case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
