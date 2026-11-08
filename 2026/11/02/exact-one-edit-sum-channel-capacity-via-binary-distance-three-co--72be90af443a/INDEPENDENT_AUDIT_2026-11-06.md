# Independent mathematical audit

## correctness

PASS

With ordered row identities and visible lengths, an insertion/deletion collision of two distinct input sums cannot occur: length pattern fixes which row was edited, and the other ell rows uniquely determine all ell+1. Unedited outputs have even column parity and one-substitution outputs have a single odd column. Two input sums have column distance w+(w mod 2), so their radius-one substitution balls intersect exactly when they differ in a single data column by Hamming weight 1 or 2. Each fixed-all-but-one-column section is a classical distance-three code, giving at most A_2(ell,3) times 2^{ell(n−1)}. A row-parity check in an optimal classical code attains it, and equality forces every coordinate section optimal. Independently enumerated complete SID balls and compared all pairs for ell=1..3,n=1..2, exactly matching the criterion. For ell=8 the witness of 20 words is distance-three; optimality 20 is borrowed from published code classification, not proved by local checker. Exact formula holds all ell,n>=1 but not two edits, unlabeled rows or unknown A_2 values.

## originality

PASS

The lower parity construction and A_2(8,3)=20 are not new; Abboud–Yaakobi introduced the same channel and near-optimal substitution construction. The matching all-parameter converse and section rigidity are additional to the accessible primary statements, with uninspected full paper remaining a qualified risk.

## value

PASS

The exact capacity of a natural row-parity edit channel reduces to classical Hamming distance-three packing with a tight converse, and every optimum has a nontrivial necessary sectional property. It sharpens previously near-optimal constructions and yields the concrete ell=8 gain. This is substantive coding structure rather than a renamed table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
