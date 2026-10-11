# Scientific review: integral homotopy type of the Desargues independence complex

## Correctness — PASS

The claimed graph is explicitly defined as \(GP(10,3)\), and an independent bipartite-Kneser construction checks a concrete graph isomorphism. Exhaustive enumeration produces 6212 faces including the empty face, with size distribution \((1,20,160,660,1510,1924,1320,480,115,20,2)\). The complete 3103-pair matching leaves one critical dimension-four face and five critical dimension-five faces in the augmented poset; removing the empty face gives exactly one additional critical vertex. Directed acyclicity was verified on all 30380 cover incidences. Signed integral elimination yields a zero five-to-four Morse boundary, with explicit unit-coefficient substitutions. The resulting CW complex has a four-sphere skeleton; \(\pi_4(S^4)\cong\mathbb Z\) makes each zero-degree five-cell attachment nullhomotopic. Independently computed mod-two boundary ranks agree with the claimed integral homotopy type. An internal reproducibility check is not an independent audit.

## Originality — PASS with residual bibliographic risk

The closest exact-graph publication located is Kumar–Singh–Verma, arXiv:2105.06144v1, which calculates the linear strand of the edge ideal of \(H(5,2)\). Those graded syzygy ranks do not calculate the ordinary independence complex's full integral homotopy type. Barmak's arXiv:1007.0418v1, Theorem 3.4, proves a general suspension property; Tsukuda's 2017 Corollary 5.3 refines the incidence interpretation but gives no graph-specific wedge multiplicities. Nilakantan–Shukla's arXiv:1709.04789v1 applies to a different bipartite graph family: its relevant three-regular instances contain four-cycles, whereas the Desargues graph has girth six. The closest indexed Desargues calculation treats its *matching* complex, that is the independence complex of the line graph, not the present object. Indexed-result queries checked the Desargues, \(GP(10,3)\), \(H(5,2)\), Levi-graph, graph-complement-clique, Petersen-cover and sphere-wedge formulations, without identifying a stronger covering statement. This negative search result alone is not a novelty proof; an unindexed equivalent calculation remains possible.

## Value — PASS

The Desargues graph is a canonical distance-transitive cubic incidence graph with twenty vertices and thirty edges. Its dimension-nine independence complex has nonzero reduced integral homology in precisely dimensions four and five, and an exact wedge decomposition is strictly more informative than homology groups, a suspension theorem, the independence polynomial, or edge-ideal regularity. The explicit full-face discrete-Morse certificate resolves integral attaching maps and torsion, making this a motivated exact invariant of a natural object rather than an arbitrary parameter slice. The result makes no unsupported claim of a general theorem for all generalized Petersen graphs.

## Limits

This is a single finite graph, not a family classification or equivariant result. The primary computation is finite but exhaustive and checked; its complete source code is included. Independent scientific auditing and exhaustive indexing of all possible literature are not claimed.

Same-model review: passed. Independent audit: not yet performed.
