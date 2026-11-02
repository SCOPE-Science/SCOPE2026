# Independent mathematical audit

## correctness

PASS

From the frozen RESULT.md the concatenation identity R(2^en+b)=R(n) xor R(b) xor ((n mod2)*topbit(b)) gives all Myhill–Nerode residuals F_{q,s,t}. Nonultimate periodicity plus its implications for any nonzero translation establish all distinct q and s,t triples are inequivalent. At e>=B+3 the q=0 or1 classes stabilize: the RS values differ at 4j+2 and 4j+3, so every five-consecutive-integers window realizes both. Counting dyadic levels yields 4m+2; c=0 and short shifts checked. Independently wrote BFS of arithmetic residual transitions and direct short-interval formulas for c=0..1023, matching complete state sets, and verified 13 dyadic shifts; inspected source checker.py and checker_output.txt (2048 claimed earlier checks). Finite tests support the symbolic all-offset proof, not extrapolated.

## originality

PASS

Best of knowledge after current primary-source reading and searches: The known bound on shifted automata and N(0)=4 do not determine minimal N(c); Thue–Morse has no adjacent-11 parity statistic.

## value

PASS

Minimal DFAO state complexity of a well-studied automatic sequence under translations is a natural exact invariant. A uniform explicit O(log c) arithmetic count plus precise dyadic growth measures the cost of shifting a nontrivial neighbor-interaction sequence, beyond standard automaticity or unminimized carry constructions. Natural parameter all offsets; neither ad hoc slice nor known four-state unshifted table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
