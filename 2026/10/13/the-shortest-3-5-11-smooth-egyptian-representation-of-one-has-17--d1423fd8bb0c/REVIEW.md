# Independent mathematical audit

## correctness

PASS

The first 14 distinct admissible reciprocals give at most 243508/245025 < 1. If a 15-term solution omits any of the first 13 denominators, its largest possible sum is attained by dropping 99 from the 15 largest reciprocals and adding 1/135; the resulting 1224041/1225125 is below 1. The forced first 13 terms leave 322/22275. With x<y, 1/x+1/y<2/x forces x<22275/161<139. An independent exact exponent sieve through 138 (not just the bundled script's 135) gives only 121, 125, 135 greater than 99; exact substitution gives 245025/1517, 111375/719, 22275/157 for y, none integral. The size bound is on x only and excludes arbitrarily large y by solving its equation, so no denominator cap is presumed. Multiplying by the odd common denominator forces odd length and excludes 16. Independent rational addition verifies the distinct 17-denominator witness sums to 1, and factorization verifies its support. The frozen checker was inspected, not executed.

## originality

PASS

The exact assertion is T_17(3,5,11)>0 and T_k(3,5,11)=0 for k<17, with no denominator cap. No equivalent claim or stronger implying theorem was found among the inspected sources. This is not a claim to have established priority exhaustively.

## value

PASS

The threshold is the first nonzero count in the standard restricted-Egyptian-fraction problem for the next admissible prime after 7 in a family with only three admissible primes p>5. Feasibility does not quantify the minimum; the universal lower bound plus exact witness supplies a natural benchmark for constrained enumeration, not a numerical result at an arbitrary search cap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
