# Independent mathematical audit

## correctness

PASS

For labelled GP(10,2) on 20 vertices, the source's 20 by 3 neighbor array implements simultaneous Boolean majority, with no ties. Independently reconstructed the entire 2^20-state transition by a Boolean majority expression (not the original indegree-peeling algorithm), classified all 1,048,576 states by direct forward iterates to their first F^2(y)=y state, and recovered entry layers (fixed,two): t=0 (118,19358),1 (4710,351490),2 (14700,344880),3 (27320,105000),4 (61600,33960),5 (60960,5760),6 (15840,0),7 (2880,0). Therefore 118 fixed and 9679 unordered temporal two-cycles, full basins 188128 and 860448; no other periods, sharp uniform 7-step bound (witness state 5608), F^9=F^7. Independently checked GP(10,2) graph isomorphism, enumerated 120 graph automorphisms and their 9 fixed and 145 two-cycle geometric orbit classes, with total orbit coverage 118 and 9679. Fixed configurations exactly those with matching bichromatic cut edges by cubic majority equivalence; complementation pairs 118 into 59. This is an actual exhaustive finite certificate, not extrapolation from samples.

## originality

PASS

Best-of-knowledge: the exact new assertion was compared to its natural aliases, stronger/general results and selected primary literature, as well as the Resultary search. Known foundations are not claimed as new. Sources read and unresolved priority limitations are recorded explicitly. dodeca.

## value

PASS

A complete dynamical census for the natural 3-regular dodecahedral graph separates 118 fixed states from 9679 two-cycle orbits, quantifies every basin/entrance layer, identifies a sharp finite transient and resolves the full spatial symmetry quotient. Such an exact graph-specific benchmark is a motivated, finite but nontrivial invariant, not merely a general-period theorem or an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
