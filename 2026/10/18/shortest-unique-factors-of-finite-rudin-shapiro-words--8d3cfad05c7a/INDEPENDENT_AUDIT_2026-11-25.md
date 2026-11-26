# Independent mathematical audit

## correctness

PASS

Appending a binary zero preserves adjacent-11 parity, and appending one toggles it iff the parent index is odd. Applying the resulting pair rule three times yields the four aligned 8-blocks; independent enumeration confirmed 56 distinct 8-windows with disjoint start phases and 104 possible length-14 windows across parity-alternating block triples, each present at least six times in the first 1024 bits. Any shorter factor can be extended to the right in the infinite word, including at a finite prefix boundary, giving enough embedded repetitions. For length k≥15 the child start parity is recognized by the first eight symbols, and its residue mod 8 also gives the first parent index parity needed to decode a partial pair. The touched parent factor has length ceil(k/2) for even starts and floor(k/2)+1 for odd starts, both at least eight. All copies of a parent factor therefore have the same parent start parity, and each yields a matching child occurrence, fitting inside the finite prefix even when an endpoint pair is only partially used. This is a bijection, not just an inequality of multiplicities. An independent suffix-neighbor longest-common-prefix scan gives minimum 18 and starts 175,191,207,223,367,383,399,415 at n=9; n=10–12 give 34,66,130 with the stated starts. Below 2ℓ_n−2 both parent lengths are less than ℓ_n; at equality, only odd starts can come from a parent singleton of length ℓ_n, and each such start lifts by p↦2p+1. The finite certificates plus this induction prove the length and complete eight-start classification for all n≥9.

## originality

PASS

No inspected work supplies the all-order shortest singleton length and full set of starts for these dyadic Rudin–Shapiro prefixes. The closest same-sequence records solve another occurrence question, bound finite minimal absence, or optimize hitting sets; exact global shortest-unique algorithms and occurrence-preserving methods are not themselves a classification of this family.

## value

PASS

The first factor length that distinguishes even one position of an explicitly structured finite word is a natural substring invariant. Here the exact scale, bounded number eight, and locations give a complete benchmark for shortest-unique-factor procedures on an infinite family. The synchronization argument explains the stable positional pattern rather than merely listing individual computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
