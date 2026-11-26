# Independent mathematical audit

## correctness

PASS

A column contains at most one zero and at least two mutually adjacent positive vertices, so the ordinary and total outer-independent Roman feasible sets agree, not merely their minima. For z zeros and t twos, z≤n and z≤3t, giving saving z−t≤floor(2n/3). With k=ceil(n/3), the path centers have gaps two or three and endpoints within one step (the singleton path is direct). For a cycle n≥4, 2k≤n≤3k realizes the requisite two/three gaps. Properly color the centers with at most three defender rows; for a three-gap use both its different boundary rows, for a two-gap the preceding defender's row. At each center at most two row values are forbidden for its zero, including its defender row; this verifies global zero independence and domination. On C3 one two cannot defend three independent zeros, as the two neighboring columns themselves are adjacent; the listed two-zero witness attains 3m−1. At n=3q, z−t=2q and the two inequalities force z=3q and t=q, so the q defended three-column neighborhoods are disjoint and cover the columns. The path has one phase, a cycle of length at least six has three; center zeros are independently chosen off the defender row in each block (no restriction across middle-column zeros). Adjacent defender rows must differ. Path coloring multiplication and the trace of (J−I)^q for the cycle give the two claimed counts, including q=2 on the cycle. Bounded direct graph enumeration over all 3^9 labelings each of K3×P3 and K3×C3 gave (minimum,count)=(7,6) and (8,108), respectively; the second is an exceptional-case count, not a claimed formula. Frozen CHECKER.py was inspected, not run. Neither finite diagnostic is used for the general proof.

## originality

PASS

This passes for the stated full-family comparison and the main all-minimizer rigidity/count refinement, not as a novelty claim for already-known scalar cases. The record expressly credits width-three minima and the complete-factor cases. Exact further coverage for the C3 exceptional scalar case in a catalogue rook-graph polynomial does not cover the divisible-by-three cylinder claims, which start at C6, or the path multiplicities. The strongest similar catalogue count located imposes independence on the opposite label support and is a different problem.

## value

PASS

Covering-capacity saturation determines every optimum on a natural family of products and turns their exact labeled enumeration into ordinary row colorings, including the distinct cyclic phases and parity term. This structural description is useful beyond a minimum-weight table and beyond the routine totality observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
