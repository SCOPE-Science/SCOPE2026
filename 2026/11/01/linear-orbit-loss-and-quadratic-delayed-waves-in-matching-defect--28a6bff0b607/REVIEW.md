# Independent mathematical audit

## correctness

PASS

For K_n with k disjoint deleted edges, n-k>=4, every vertex misses at most its matched partner, and a color-i vertex can be blocked only if the unique successor-color vertex is that partner. At most one color-blocking pair exists in any onto-three-color state. With one/two initial colors, nonmonochromatic states enter consensus at time one except 6k exceptional orientations which enter at time two; three monochromatic states are fixed. An onto state is an immediate three-cycle unless uniquely blocked, in which case 6k(2^{n-2}-1) initial states are selected. If r=0 additional original color-i vertices, all others advance to consensus in two steps (6k states); if r>=1, only the r=1 case paired to a second deleted edge creates a second consecutive blocker, counted by 12k(k-1), then unblocked and in three-cycle. Remaining one-blocker states enter three-cycle at time one and yield 6k(2^{n-2}-2k). The derived disjoint census has exact six rows (0,1):3,(0,3):3^n-3*2^n+3-6k(2^{n-2}-1),(1,1):3*2^n-6-6k,(1,3):6k(2^{n-2}-2k),(2,1):12k,(2,3):12k(k-1). It implies F^5=F^2, primitive 3-cycle Q3=(0,3)/3, consensus basin 3(2^n-1)+6k, and sharp time2 for every k. Independent direct neighbor-update enumeration, without using the blocking classification, exhausted all 3^n states for each admissible n=5..9 and k (14 parameter pairs), reproduced every cell, transient/period and global iterate identity; infinite result rests on blocker proof.

## originality

PASS

Best-of-knowledge PASS for the all-(n,k) matching-defect six-class labelled orbit census and its linear-versus-quadratic response, while the qualitative time-two period-collapse is not claimed as new. Gravner-Lyu-Sivakoff provide finite-graph synchronization criteria/diameter results, but do not count all transient/period classes. The closest exact published complete-multipartite census discovered is for a different binary parity automaton, not three-color successor contact.

## value

PASS

Exact six-class dynamics for a natural near-complete graph family gives a substantive perturbative invariant: k disjoint missing edges cause linear loss of primitive three-cycle orbits, only linear consensus-basin growth, but a quadratic 12k(k-1) delayed oscillation class caused by interaction of distinct defects. The natural matching-size parameter, exhaustive labelled state classification and sharp two-step cutoff make this meaningful beyond a one-off finite simulation or qualitative synchronization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
