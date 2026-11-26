# Independent mathematical audit

## correctness

PASS

The simple-cycle hypothesis n >= 3 makes the two adjacent columns distinct. Each column has at most two selected vertices by independence on C5. An empty column forces both adjacent columns to contain every row; a singleton at row r forces both adjacent columns to contain the adjacent rows r+2 and r-2. Both are impossible. Write each independent pair uniquely as {t-1,t+1}; disjoint adjacent pairs have centers differing by +1 or -1 modulo 5. The unselected rows t+2 and t-2 each require a neighbor from the adjacent column with the corresponding center t+1 or t-1. Thus the two neighboring centers are opposite steps from t, and every consecutive increment is the same. Closure is equivalent to 5 dividing n. Conversely, this recurrence supplies the required outside neighbors, including two within the column at t; the first center and first step distinguish the ten labelled sets. The official 2016 paper uses matching graph and kernel definitions. An independent exact witness check, `python3 /workspace/branches/replay_2_3.py`, verifies the ten distinct C5 x C10 sets, each with 20 selected vertices of inside-degree zero and 30 outside vertices of inside-degree 2 or 4. The all-n conclusion is analytic, not extrapolated from this check. Inspected the two frozen checker sources without executing them.

## originality

PASS

The unequal-order family and exact ten-pattern classification for the fixed first factor are distinct on the evidence inspected. The 2016 theorem purports to give broader coverage, but its claimed necessity actually excludes the verified new examples. The equal-order case is credited rather than treated as a new count.

## value

PASS

C5 is the smallest odd cycle that permits nontrivial two-element independent columns; the local necessity proves an all-length rigidity statement, not merely a short-grid check. The explicit family overturns a printed general existence criterion while replacing it on this factor by an exact classification and count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
