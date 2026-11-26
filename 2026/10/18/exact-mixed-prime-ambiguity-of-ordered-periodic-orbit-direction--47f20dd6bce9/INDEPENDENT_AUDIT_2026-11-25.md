# Independent mathematical audit

## correctness

PASS

For a fixed labeled order and a single cycle, anchoring the least point at phase zero makes a cycle equivalent to its phase assignment. At stage i the nonzero-time entries for the next point are the indicator of A_i translated by its phase; replacing the time-zero entry by zero makes this exact. All extensions yielding the prescribed row form one coset of the translation stabilizer, whose order divides gcd(2p,i). If its order is p at i=p, A_p is the even residues. Invariance by addition of p would send any earlier nonempty subset out of the evens or force any later superset to contain every odd residue. Hence such a path has no size-two branch; other paths have at most p-1 size-two branches. With uniform choice at each node every completed leaf has probability at least 2^{-(p-1)}, proving the upper bound even with dead ends. The adjacent-pair construction has free bits on p-1 links and total flip parity odd. Its p-step iterate flips within each block, while nonmultiples of p give comparisons determined by blocks, proving attainment.

## originality

PASS

The signature, phase reconstruction and a witness family have substantial overlap with adjacent work. The supported distinct claim is the sharp maximum over all signatures for 2p, not composite nonuniqueness or a large explicitly constructed fiber by itself.

## value

PASS

The theorem measures exactly how much a complete ordered observation can fail to identify a cycle in the natural mixed-prime family following the known prime case. It shows that two distinct arithmetic branching mechanisms cannot compound, closing an actual factor-p gap between a natural general bound and attainability. This is useful without a broader classification of interval maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
