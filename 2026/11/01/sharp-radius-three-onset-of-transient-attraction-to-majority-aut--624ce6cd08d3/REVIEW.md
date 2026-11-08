# Independent mathematical audit

## correctness

PASS

For synchronous strict majority on n>=2r+1 distinct sites, the 2022 Nakar–Ron complete periodic-word templates for r=1,2 are 01 at r=1 and 0011,001101,001011 at r=2 (01 at r=2 is fixed). Independently constructed complete phase-window directed graphs for each target give a single recurrent simple cycle of 2,4,6,6 phase states, proving unique preimages for all repeated target lengths. At r=3, direct 7-site majority checks give F(Y)=Z,F(Z)=Y,F(P)=Y for Y=0011001110,Z=1000111001,P=1001011001. The independent graph for target Y has one cyclic SCC with 17 vertices and 18 edges, two phase-zero states (41,49), and exact 10-step return matrix [[1,1],[1,1]], so trace(M^m)=2^m. Direct enumeration of all 2^10 and 2^20 states gave exactly 2 and 4 predecessors, confirming but not replacing infinite transfer result. Complement and 5-site rotation give equal count for Z. Only the companion is periodic, so 2(2^m-1) transient one-step entrances. Both r<=2 exclusion and r=3 witness establish sharp radius.

## originality

PASS

The Tosic–Agha 2004 Lemma 5 explicitly asserts no incoming transient into any threshold-automaton cycle, which the exhibited ten-cell majority counterexample refutes. The 2022 Nakar–Ron classification covers periodic templates, not their exact nonperiodic preimage counts. The novel bounded radius threshold and exact exponential one-shell multiplicity are meaningful departures, not a renaming of the periodic-word classification.

## value

PASS

A constructive correction to a published universal dynamical assertion together with a sharp interaction-radius threshold and exponential entrance count gives a natural exact dynamical basin statistic. It is a substantive structural counterexample and classification, not a tiny isolated simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
