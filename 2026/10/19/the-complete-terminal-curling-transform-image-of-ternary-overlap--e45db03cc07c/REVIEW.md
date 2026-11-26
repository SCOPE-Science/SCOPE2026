# Independent mathematical audit

## correctness

PASS

The transform uses the curling number of each nonempty prefix, with no extra initial 1. An overlap has length 2p+1 and period p, and a cube always contains one, so in overlap-free words a suffix square exactly detects curling number 2. If an admissible prefix is extended, all newly introduced forbidden factors on either side end at the new position; this establishes the exact prefix induction including termination. Independently enumerated every labeled candidate using integer symbol masks: compare the low p bits for suffix squares and p+1 bits for suffix overlaps against their p-shifts, on both source and transform as appropriate. Replay: python3 /workspace/reproduction/4.py; see 4.txt. The counts at depths 83,84,85 were 5040,6048,0. The only outputs match the exact stated H with tails 1 and 2, with frequencies 4032 and 2016. In letter order 0,1,2, the only nonempty final branching tuples are (1,1,2), (1,2,1), (2,1,1), each at 672 distinct parents; thus all three letters work at every one of the 2016 extendible parents, and exactly one gives curling digit 2. A separate labeled check recomputing factors and curling numbers directly agreed. These are complete finite enumerations, not probability or extrapolation. The frozen computation logs were inspected as recorded evidence, not relied on for independent confirmation.

## originality

PASS

Best-of-knowledge pass only for the complete image, fibers, common-prefix rigidity and final branching of the stated terminal family. The 84 maximum, the 6048 total, exclusion of length 85 and one of the two outputs were already given by Caveney–Dong–Shallit. A later-dated indexed result gives the same profile plus a finer final-symbol criterion; exact overlap is acknowledged without assuming priority from index dates alone.

## value

PASS

The entire transform image of the natural maximal admissible family is an intrinsic finite invariant: 6048 different inputs yield only two outputs differing at the last position. The fiber sizes and universal three-letter parent branching resolve how terminal square-suffix choices concentrate, information unavailable from a total count. This is useful as a constraint and a benchmark for structural accounts of these rigidity phenomena, without claiming a general theorem at shorter lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
