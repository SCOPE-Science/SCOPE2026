# Independent mathematical audit

## correctness

PASS

A vertex is a word with none of the eight proper borders. Edges encode both directions of each permitted overlap test, so exactly the maximal cliques are the inclusion-maximal codes. Length-one overlaps separate the two orientations 0…1 and 1…0, exchanged by complementation or reversal. Independently, repro/review5.py builds the incompatibility graph by prefix and suffix classes. It enumerates independent dominating sets in the first orientation: an undominated vertex must be covered by at least one neighbor or itself, and branching on the first chosen such vertex partitions all extensions. It gives 148 vertices, 3080 compatible edges, and labeled frequencies 1:4, 4:12, 5:20, 6:48, 7:200, 8:588, 9:1712, 10:5056, 11:13520, 12:23136, 13:16832, 14:1152. Reverse complement is the only nonidentity group element that can fix a nonempty code; its action had no fixed set in the first orientation, hence none in either. The 62280 codes yield 15570 orbits. The independent canonical catalog and the frozen gzip payload both give 7338080 bytes and SHA-256 ebacd3ecd51b08c10b05e462a3496200ca3261b0840a0a3351910af91436ecd3. The frozen Python and C++ sources were inspected, not run; some checks described as assertions in the prose are printed diagnostics in those sources, but were actually checked in the independent reproduction.

## originality

PASS

Credit the known optimum and the already indexed 1152-code maximum layer. The distinct supported result is the all-cardinality maximal-code distribution and free action on the entire census, beyond that layer and the published construction families.

## value

PASS

Length nine is a natural exceptional binary benchmark from the maximum-code literature. The census answers a different saturation question: a greedy insertion process may already be stuck at size one, never stops at sizes two or three, and can stop at every size from four to the optimum. The exact multiplicities and symmetry action provide a deduplicated reference for this full finite class, not an arbitrary sample or rerun of the maximum layer alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
