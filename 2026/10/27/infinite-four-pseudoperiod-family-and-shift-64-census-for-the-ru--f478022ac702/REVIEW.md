# Independent mathematical audit

## correctness

PASS

The binary-pair recurrence gives r(4t)=r(4t+1)=r(t) and complementary symbols at 4t+2 and 4t+3. For Q=8m, at n=4t or n=4t+1 with t even, shift 1 matches; at n=4t+1 with t odd, shifts Q and Q+1 are complementary, as they are at n=4t+2; at n=4t+3 the complementary shifts are Q−1 and Q. This covers every n and m≥1. The published factor-closure induction is valid: any length-65 image window uses at most 33 source letters and hence lies in the image of a length-65 source factor. Separately, /workspace/branches/independent-3.py, given the path to the frozen census.tsv, computed all eight reachable adjacent parity-symbol state pairs, generated all windows from successive length-64 blocks using the binary concatenation rule, and found 512 binary factors. Every length-65 window fits within such a pair of blocks. Enumerating all 4-subsets of mismatching shifts excluded exactly 635352 of 635376 candidates, leaving precisely the 24 TSV rows, including seven members of the infinite family and the unique tuple through shift five. This exhausts the infinite-word condition within the cutoff, not the unbounded shift problem.

## originality

PASS

The independently supported contributions are the explicit unbounded arithmetic family and the exhaustive binary shift-64 census, not four-pseudoperiodicity itself or the known witness (2,3,4,5). No available evidence examined covers the two contributions.

## value

PASS

The residue argument gives infinitely many explicit minimal-cardinality witnesses, a structural feature not shown by the known one-off witness. The complete census at a binary block scale adds exact short witnesses outside this family, measures the family's coverage of the bounded regime, and gives concrete tests for a future full classification. The family, not the cutoff alone, provides the unbounded contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
