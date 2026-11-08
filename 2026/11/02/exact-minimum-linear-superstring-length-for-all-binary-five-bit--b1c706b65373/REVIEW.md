# Independent mathematical audit

## correctness

PASS

Exactly 32 distinct ten-bit squares uu with u in {0,1}^5 must appear in a linear word. Choosing ordered occurrences yields an overlap-weighted Hamiltonian path of all required length-10 squares; conversely every such path constructs a superstring by maximal overlaps. The 8 rotation necklaces (two singleton, six length five) entail q>=7 cross-necklace transitions; cross cost at least 6, within cost at least 1, hence L>=41+5q, excluding q>=9 at L<=81. If q=7, one contiguous block for each necklace; direct internal permutation minima by endpoints (<=5! permutations) and a subset DP over eight blocks gives global minimum 82. At q=8, L<=81 requires equality in every cost: all within-orbit edges are directed one-step rotations and each crossing costs 6; exactly one primitive necklace splits into two directed arcs. All 6*5*4=120 splits were exhaustively decided by a nine-block subset reachability DP, none feasible. The given literal 82-bit witness was independently checked to include each distinct ten-bit square. Reimplemented both DPs independently from the supplied VERIFY.py, obtaining q7=82, 120 q8 splits with zero equality cases, witness length 82 and 32 required squares. This is a finite exhaustive proof conditional on faithfully enumerated partitions and transitions, not extrapolated finite sampling.

## originality

PASS

Best-of-knowledge PASS solely for proving sharpness 82 of a natural finite superstring covering problem; 82 itself as a construction is prior in Au. Primary same-object literature was inspected in detail and yields a 72 lower bound, not exact 82 minimality.

## value

PASS

Finding the exact linear superstring optimum for all 32 natural length-10 squares is a well-motivated finite combinatorial covering invariant, not an arbitrary sample. The gap between existing constructive length 82 and prior lower bound 72 was genuine; the necklace-DP exhaustive proof closes it. An exact finite optimum remains valuable without a formula for other root lengths. Do not advertise the 82-word construction itself as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
