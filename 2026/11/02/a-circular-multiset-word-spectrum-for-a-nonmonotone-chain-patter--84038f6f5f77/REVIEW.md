# Independent mathematical audit

## correctness

PASS

Expand y^c by marking an arbitrary subset with weight t per mark. For either pattern compare suffix and prefix standardizations: shifts 1 and 2 disagree, and shifts 3 and 4 agree. At shift 4 the old maximum is shared as the next minimum and the four new values lie above it. At shift 3 in 12435 the second shared value is the old maximum and all three new letters are larger; in 13245 the two shared positions contain the top two of the latest occurrence. They are the top two of the whole chain inductively (true initially, preserved by either extension). The new rank-2 letter inserts between them, and ranks 4 and 5 append above them. This gives exactly one total order per compatible chain signature. The last value strictly increases along each overlapping gap, excluding a fully closed marked chain. A sole mark has a gap n≥5 back to itself. Cutting at every gap ≥5 gives disjoint chains, possibly touching at gap 5, and singleton uncovered positions, each in a canonical atom. For length n and k atoms, distinguish one of the k atom boundaries in an indexed configuration. This gives a linear ordered tuple of k atoms starting there and a choice of its starting index among n options; conversely these data give the distinguished boundary in the indexed configuration. Therefore the contribution of A^k is multiplied by n/k, even for rotationally periodic words. The singleton-only configurations handle the empty marking and n<5; for a<5 the expression reduces to ze_1/(1−ze_1). Substitution t=y−1 restores ordinary occurrence weights, and coefficient symmetry gives content-permutation stability.

## originality

PASS

The supported distinction is the full indexed cyclic occurrence enumerator resolved by arbitrary repeated-letter content for these two patterns. Linear chain-cluster stability and the logarithmic relation on distinct-entry circular permutations are not new here. No inspected statement covers the arbitrary-content indexed cyclic claim.

## value

PASS

The result resolves all counts by multiplicities and number of occurrences, including wraparound, for explicit nonmonotone patterns. The total-order property makes each connected contribution a single elementary symmetric function rather than a general order enumerator, and the proof isolates exactly the additional condition needed to use cyclic atoms. This yields useful exact distribution and stability information in a domain not handled by distinct-entry circular enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
