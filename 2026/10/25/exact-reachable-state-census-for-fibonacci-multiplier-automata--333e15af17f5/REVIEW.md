# Independent mathematical audit

## correctness

PASS

Checked the source transition (a,b,d,e)->(s,t,d+e+b−ma+t−ms,d), the no-adjacent-one constraints, and the [-m,2m−1] window. Zeckendorf last-digit deletion g(z)=floor((z+2)/phi)−1 and irrational rotation delta={(X+2)/phi} produce an exact current difference/preceding-difference formula; density of irrational rotation and breakpoint coincidence counts give each r_m(d), with four endpoint adjustments counted even for m=1. Backward closure under deleting prefix last digits means no admissible pair is silently lost to window rejection, and out-of-window prefixes cannot reach an accepting difference c. Independently BFS-enumerated the entire exact integer state graph and per-d profile for m=1..25, all matched. Source verify_reachable.py independently counts m=1..60 plus numeral samples; its saved log is corroborative, not an infinite proof. Finite tests alone cannot establish the all-m formula.

## originality

PASS

Best of knowledge after current primary-source reading and searches: A 36m² ambient automaton does not force 6m²+6m−4 reachability or its four boundary defects. The 2m² trim minimal single-track divisibility result is neither a bound nor an equality for two-track Y=mX+c.

## value

PASS

Determines exact accessible size of an explicitly standard Zeckendorf multiplier automaton, replacing loose 36m² ambient size with a complete 6m²+6m−4 profile. The nearest published source specifically calls better understanding reachable states an open need; separating reachability from minimization makes the exact invariant meaningful for resource analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
