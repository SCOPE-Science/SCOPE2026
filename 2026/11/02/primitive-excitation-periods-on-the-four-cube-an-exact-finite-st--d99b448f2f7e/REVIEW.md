# Independent mathematical audit

## correctness

PASS

The exact 3-state threshold-one synchronous update on the labelled hypercube Q_d is represented by one base-3 digit per vertex. For every state, a single-outgoing-arc DFS on the finite functional digraph identifies each cycle exactly once. Independent vertex-wise and bit-set successors implement the same rule (color-1 set N(A)\(A∪B), color-2 set A); all 3^(2^d) states are exhausted for 1<=d<=4, not sampled. Independently compiled and executed a separate exhaustive 43,046,721-state Q4 C++ enumerator: periods/orbits exactly (1:1),(3:292616),(4:13190),(10:1344), agreeing with package data. The package basin routine correctly back-propagates first-periodic-entry times, yielding period basins 592641,16535592,25166232,752256 and maximum entry time 11. Smaller Q1,Q2,Q3 checks establish dimension boundary; 10-row explicit period-ten witness validates positive existence. No assertion for d>=5.

## originality

PASS

Best-of-knowledge the exact labelled Q4 primitive-cycle and basin census is not implied by published extinction/persistence classification; Gravner–Lyu–Sivakoff Theorem 3 discriminates extinction via circulation but does not count cycles, while Doba supplies a ten-cycle on another graph. Durrett–Steif studies periodic square-lattice long-time behavior, not the exact Q4 43M-state census.

## value

PASS

The labelled four-cube is a canonical finite periodic square-grid Greenberg–Hastings system; its full primitive period spectrum and sharp first appearance of 10-cycles are natural finite dynamical invariants. A complete independently replayable finite census gives a meaningful exact benchmark, including basins and transient length, beyond a mere single small witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
