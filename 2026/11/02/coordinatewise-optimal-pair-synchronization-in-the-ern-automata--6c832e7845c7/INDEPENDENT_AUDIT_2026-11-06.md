# Independent mathematical audit

## correctness

PASS

Take unordered pairs of distinct cyclic states and height h their minimal cyclic separation, with antipodal orientation fixed at n even. Compute two potential coordinates (A,B), piecewise A=h(n-1)-i/B=h or A=(m-1)n-i/B=m. All transitions satisfy A−A(after a)≤1 and B(after a)=B, while A(after b)≥A and B−B(after b)≤1; direct inspection of both wrap cases and the n=2,3 boundaries shows R=A+B has exactly one outgoing rank-decreasing letter at every pair. The displayed word a^(n−1−i)b(a^(n−1)b)^(h−1), or antipodal adjustment, reaches singleton using precisely A a-letters and B b-letters. Thus all positive weighted costs are lower-bounded componentwise and uniquely attained; R-values partition 1,…,C(n,2) into consecutive height blocks. Independent pair-transition and 3-cost reverse-Dijkstra verification checked all pairs for n=2…18; universal proof is the one-step transition analysis, not finite Dijkstra.

## originality

PASS

Best-of-knowledge PASS for simultaneous coordinatewise Parikh-minimization and unique merging word for every pair/all positive letter costs, plus full multiplicity-one shortest-distance spectrum. Classical Černý reset lengths, random-input pair graphs, and general rank-deficiency profiles are prior. A random-input analysis explicitly draws the same pair automaton, which is a realistic source for implicit shortest-path arguments but its results do not state or logically force all-cost coordinatewise uniqueness.

## value

PASS

The canonical difficult synchronizing automaton has a natural pair automaton used in synchronization algorithms. A closed-form unique all-weight optimal word for EVERY pair and exact non-repeating distance spectrum are useful combinatorial structure, not an arbitrary small-instance enumeration. The proof gives a sharp all-n family and componentwise lower bounds stronger than an ordinary shortest reset length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
