# Independent mathematical audit

## correctness

PASS

The complete two-coordinate update is diagonal with iid K_n~Bin(q,1/2), factors 1−αK_n/q and 1−α(q−K_n)/q. A coordinate is killed only at the integer count j=q/α; every such count occurs eventually a.s. and is absorbing. The two killing counts are disjoint unless 2j=q, giving the exact survival law and mean 3/(2p_j) or 1/p_j. Conditional risk multiplies by 1−α+α²(q+1)/(4q), independent of the error coordinates. For q4 α4, p=1/4, Eτ=6 and risk 2^n. At α=19/5, no factor is zero; exact weighted product of |1−αk/q| equals 6972041972007/64000000000000000<1 whereas risk=137/80>1; the strong law and norm comparison give the almost-sure exponent, with continuity furnishing an open interval. Independent rational arithmetic rechecked the exact product and risk and inspected check.py; finite checks are not the SLLN proof.

## originality

PASS

Best-of-knowledge, after comparing the actual theorem and its implications to retrieved Resultary records and the named published primary material. Prior mean-square upper bounds imply nothing about almost-sure finite absorption under α=q/j when the bound grows. The new claims concern exact hitting and robust typical-versus-second-moment separation, not the already-known recurrence alone. Residual priority/access risks are explicitly retained.

## value

PASS

The method is a real parallel optimization update; the extreme gap between finite-time almost-sure exact solution and diverging expected squared error, plus robust nonresonant separation, gives a precise caution about interpreting mean-square convergence and relaxation in randomized algorithms. The transparent orthogonal two-row witness is substantively motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
