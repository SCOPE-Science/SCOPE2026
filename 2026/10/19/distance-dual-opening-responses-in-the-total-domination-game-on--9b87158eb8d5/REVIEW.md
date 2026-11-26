# Independent mathematical audit

## correctness

PASS

Open-neighborhood union is the only needed history: any previously played vertex has no new neighbor, and at any nonterminal state some undominated vertex has a neighbor that can cover it. Thus taking the min/max over strictly increasing dominated sets is exact. I independently solved the equivalent deadline game on uncovered sets by testing whether Dominator can ensure completion in h further moves: at his turn one legal successor must suffice, at Staller's every successor must suffice. The terminal state is successful and a nonempty state with more than 3h uncovered vertices fails. With interleaved Petersen labels and Floyd–Warshall distances, the independent computation checks all 380 distinct ordered opening pairs per graph, each second move's legality and every first move under both conventions. It gives (11,10) and (10,10); by distance 1 through 5 the dodecahedron yields (10,11),(11,11),(10,11),(10,11),(10,10), and the Desargues graph gives (10,10) throughout. The common distance-shell sizes are (1,3,6,6,3,1). Taking the appropriate extremum proves exactly the stated optimal reply sets. The frozen programs use two graph constructions with fixed isomorphisms and have byte-identical recorded outputs. Independent replay: python3 /workspace/branches/independent_game.py. This establishes only the stated two graphs and rules.

## originality

PASS

The closest inspected Resultary findings use closed neighborhoods and give different values and second-response geometry, even on the same graphs. Inspected primary material gives general total-game bounds and exact-results context, not the forced-pair shell table. The distinct comparison is supported to best current knowledge, with explicit limits on external retrieval and on possible coverage under the equivalent hypergraph game.

## value

PASS

Matching distance-shell cardinalities, sizes and degrees make these two canonical graphs a controlled comparison. The exact opening classification shows that those shell sizes do not determine the strategy: one graph distinguishes sharply between distance two and the antipode depending on who starts, while the other is completely indifferent at move two. This is an independently useful exact strategic invariant, not just an isolated optimum or a claim about static total dominating sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
