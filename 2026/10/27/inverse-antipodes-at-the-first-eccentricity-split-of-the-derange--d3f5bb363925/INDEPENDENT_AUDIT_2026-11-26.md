# Independent mathematical audit

## correctness

PASS

An image swap that leaves both moved positions fixed-point-free gives exactly one edge in the simple graph, equivalently an alternating four-cycle flip of a perfect matching of the crown graph. The independent all-roots BFS rebuilt the vertices and edges from this rule and reached all vertices for n=4,5,6. It found vertex/edge counts 9/12, 44/120, 265/1260, and unordered distance histograms (12,18,6), (120,300,360,166), (1260,5310,11490,12100,4800,20). G_4 and G_5 have constant eccentricities 3 and 4, respectively. In G_6 exactly the 40 type-(3,3) vertices have eccentricity 6 and each has only its inverse in that shell; all 225 others have eccentricity 5. Replay: python3 /workspace/branches/1bca7efc-9c1f-442c-ae3a-925674b099c9/independent_derangement_metrics.py --min-n 4 --max-n 6. The supplied representative labels also have a valid exact certificate design: a zero root, edgewise unit variation and descending neighbors imply both distance bounds; conjugation is a graph automorphism and transports each cycle-type row and inversion. The four-step unrestricted geodesic obstruction is sound: each first transposition in such a geodesic must split a relative three-cycle, but swapping within either original three-cycle makes a fixed point, and parity excludes distance five. The proof of uniqueness and of the split is exhaustive for these orders, not for n≥7.

## originality

PASS

The supported distinct result is the complete finite eccentricity split, unique inverse partners and pair-distance census in the first three connected orders considered. The graph and its matching-switch/Markov-chain formulations are known. The closest checked same-graph sources concern local closed walks or spectral/mixing estimates, while the available Jain description concerns spanning walks. Later indexed exact inverse-distance results cover a portion of the n=6 result or a different graph order, not the full frozen result. This is a bounded best-of-knowledge comparison, not a priority claim.

## value

PASS

The orders are not an arbitrary sample: they give the first nonconstant eccentricity among the connected orders compared. Identifying the precise cycle type and a unique inverse partner explains which obstruction appears at that cutoff; the unrestricted transposition distance misses it. This is a useful exact benchmark for conjectures or algorithms on derangement switches and perfect-matching reconfiguration, without extrapolating the phenomenon to all orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
