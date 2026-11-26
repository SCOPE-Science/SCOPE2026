# Independent mathematical audit

## correctness

PASS

Matched the submitted primary paper's definitions and both rule conditions. Averaging all shifts gives the same circular matrix as averaging distinct conjugates since each distinct conjugate has the same multiplicity. To exhaust the words, canonicalize all 3^n words by the least rotation and retain those containing all three letters. Group by the six exact rational scattered-subword counts. To exhaust moves, test every rotation, every split of the n−4 unmarked letters between x and y, both orientations and both choices of α where applicable. Connected components then resolve completeness on every class. The independent bounded reproduction (python3 census.py --max-n 6, separate from the frozen package) was run after a timed n≤3 slice; it compared direct counts and letter-matrix products, enumerated the rule edges and checked every pair in the nontrivial classes. Full-support counts are 0,0,2,9,30,91. There are no nontrivial classes through n=4. At n=5 the sole pair is {aacbc,abacc}: for example rotate to acbca and use CE₁ with x empty and y=b to reach cabac, a rotation of abacc. At n=6 eight classes contain seventeen words; five classes are connected. The other classes are {aabcbc,ababcc}, {aacbcb,abaccb}, {abacbc,abcacb,abcbac}, with fractional tails (7/3,7/3,13/6), (5/3,5/3,5/6), (2,2,4/3) respectively, all with counts (2,2,2). The reproduction checks all seven words have no legal move in either direction, even to their own rotation class. Read the frozen certificate and script without executing them. The frozen pair test reuses the move generator and the frozen degree test discards self-rotations; the independent bidirectional replay supplies the stronger isolation check. The conclusion is bounded to n≤6 and full support.

## originality

PASS

The published rules and the fact of incompleteness are prior work. The inspected primary presentation gives a length-8 failure, not the first full-support cutoff or the complete length-6 census. No compared record supplies those results. This is a bounded literature assessment, with the primary evidence coming from the open submitted version and the closest indexed records compared at statement level.

## value

PASS

The earliest failure of a proposed rule system is a natural exact boundary, particularly when the literature exhibited only a longer example. Full support removes separate binary degeneracies, and all seven short isolated obstructions identify precisely where new moves would first be needed. The complete short-length cutoff is useful independently of any general replacement rule system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
