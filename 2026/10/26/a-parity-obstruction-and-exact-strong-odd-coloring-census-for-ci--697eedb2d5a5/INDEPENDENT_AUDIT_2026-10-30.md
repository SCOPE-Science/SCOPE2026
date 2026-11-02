# Independent mathematical audit

## correctness

PASS

On P_n=C_n □ K2 (n>=3), a proper strong-odd coloring requires each cubic open-neighbor triple to have either one or three distinct colors. Two consecutive vertical columns form q-palette transfer states; q=4 yields 84 states. Direct independent enumeration found each state has exactly one successor and obtained six directed 2-cycles, six 4-cycles and eight 6-cycles. Hence A_n(4)=12·1_{2|n}+24·1_{4|n}+48·1_{6|n}; there are no odd four-palette closed walks, including colorings with fewer colors. Even n>=4 have exactly two optimal bipartition colorings; n=3 has graph square K6 and needs six. Explicit legal 5-color closed walks of lengths 4,5,7 share one initial two-column state and concatenate to every odd n>=5, giving χ_so=5 then; the general 5-palette number is exactly tr(T5^n) with 260 states, checked in given proof and source verifier for n=5,7,9,11. Independent 84-state exhaustive cycle classification is complete for its finite transition system; this is a logically valid finite certificate for arbitrary n because n-length colorings are closed walks. The infinite construction follows from explicit common-based loops, not finite n sampling.

## originality

PASS

Kwon–Park (arXiv:2401.11653) introduce strong odd coloring and general sparse-graph upper bounds; Caro–Petruševski–Škrekovski–Tuza (arXiv:2410.02336v1) give a Cartesian-product bound χ_so(G□H)≤χ_so(G)χ_so(H) and other structural examples. Their accessible primary HTML was inspected for the ordinary cyclic prism exact classification; the general bound does not imply the odd n lower χ_so>=5 or the four-palette 84-state periodicity/census. Ordinary odd colorings, and strong odd crown graphs in Resultary, concern a different invariant or graph. Searches found no same cyclic-prism named-palette table. A differently indexed old exact prism enumeration remains possible, so originality is best knowledge, not a global priority certificate.

## value

PASS

Prisms C_n□K2 are a canonical cubic graph family. The jump χ_so=2 for even n to 5 for odd n, apart from the 6-color triangular prism, is a topological parity obstruction not predicted by degree or product upper bounds. The exact forced 2/4/6 transition periods and tr(T5^n) enumerator offer motivated structural and counting data beyond the chromatic value; the large finite transfer system is completely specified rather than an unexamined output table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
