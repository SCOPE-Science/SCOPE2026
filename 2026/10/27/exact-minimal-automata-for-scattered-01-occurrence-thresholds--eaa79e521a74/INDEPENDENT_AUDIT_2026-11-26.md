# Independent mathematical audit

## correctness

PASS

For a prefix with z zeros and p pairs and a suffix with t ones and h internal pairs, the total is p+zt+h by splitting pairs into the three possible locations. The classes p>=k, z=0, and p<k with z>=1 and p+z>=k have residuals all suffixes, the initial language, and suffixes containing a 1, respectively. Otherwise d=k-p-z is positive, 1<=z<=k-d, and acceptance becomes h+z(t-1)>=d. The prefix 01^(k-d-z)0^(z-1) reaches every admissible pair. At t=0 all these levels reject; t=1 tests h>=d; if z>=d all t>=2 are accepted. Distinct levels are separated by 0^d1 at the smaller level, which also separates that level from the initial language. At equal d, use 10^max(d-z_2,0)1 for z_1<z_2 with z_1<d. The empty suffix and the one-letter suffix 1 distinguish the exceptional classes where needed. Summing min(d,k-d) over 1<=d<k yields floor(k^2/4); at k=1 there are only the three reachable exceptions. Inspected RESULT.md, VERIFICATION.md and verify.py. The recorded finite refinement and short-word comparisons were not replayed; they supplement the universal argument. The reported raw-state and direct-test totals also agree with sum_{k=1}^{40}(k^2+2) and 12(2^10-1)(2^7-1), respectively.

## originality

PASS

Best of current knowledge for the exact inclusive-threshold quotient only. The strongest catalogue matches give different exact-equality quotients whose dead class loses the distinction between overshooting k and being below k but unable to hit it exactly. General bounded-count and Parikh-matrix constructions are background, not a minimal threshold classification. The underlying residual variables and several test words are shared with earlier work; no novelty is credited for those in isolation.

## value

PASS

A threshold on an elementary scattered-pair statistic is a natural regular constraint, and a user designing or studying a recognizer needs the exact quotient, not only regularity or an automaton for exact counts. The theorem gives both the optimal uniform state count and a residual classification with explicit witnesses; the inclusive collapse is different from the overshoot behavior of exact equality. Value is confined to this exact binary-pattern invariant, not broader algorithms or pattern families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
