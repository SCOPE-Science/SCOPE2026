# Independent mathematical audit

## correctness

PASS

PASS. The 24 cube darts (b,i), b∈{0,...,7}, i=0,1,2, define 36 edges, degree 3, matching a truncated-cube skeleton. Independent reimplementation in /mnt/data/scope08_cube_recheck.py reproduced the complete 26,440 nonempty simplices and f=(24,240,1296,4092,7632,8056,4272,828), the greedy acyclic 13,211 matching pairs, critical counts one 0, five 5, twelve 6, and all 143,760 oriented Hasse incidences topologically sorted. The source signed-gradient Morse differential 5×12 has two identical nonzero rows, rank one, a unit entry -1; the precise nonzero entries at (1-based) rows 4,5 columns 5,6=-1 and column9=+1 were reconstructed from signed boundary recurrence. Therefore one 5/6 cell cancellation leaves four 5-cells and eleven 6-cells and, by π5(wedge S5)=Z^4, every remaining degree-zero 6-attachment is null. This proves an integral homotopy wedge rather than just finite-field Betti counts. Only the 24-vertex graph is covered.

## originality

PASS

PASS on bounded full-text comparison. Barmak proves general star-cluster/suspension and claw-free connectivity criteria, none evaluates this cubic graph (which has a triangle at every vertex); Goyal–Shukla–Singh treats other graph families and alterations. A public Rips complex of the same truncated cube has an unrelated definition and degree 2/3 wedge, not the independence complex; truncated octahedron independence complex is a different graph and invariant. No stronger coverage or table yielding exactly (4,11) was found.

## value

PASS

PASS. The truncated cube is a canonical Archimedean 3-regular polyhedral graph, and its mixed-dimensional integral homotopy decomposition is a natural complete invariant not determined by Euler characteristic, Betti numbers or generic connectivity bounds. The unimodular signed attaching-map calculation is material rather than a cheap numerical recomputation; no claim of a broad family theorem is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
