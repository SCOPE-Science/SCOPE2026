# Scientific review

## Correctness — PASS

For the exact directed mutual-visibility definition (every ordered selected pair has an unobstructed shortest directed path), three selected vertices in one cycle fibre are impossible: the unique directed geodesic between an appropriate first and third selected point must traverse the middle one. There are four first-coordinate fibres, giving the universal upper bound eight. A shortest path in the product is exactly a monotone walk in a finite rectangle, making the included Boolean reachability recurrence equivalent to the original visibility condition. All 2,946 reduced candidates of size at least six at width four and all 2,490 reduced eight-vertex candidates at width five were exhaustively rejected by the recurrence and independent direct breadth-first search. The three explicit configurations attain five, seven, and eight. The width-six witness lifts to every greater width by inserting empty columns along the single directed wrap-around, preserving each witnessing geodesic. Therefore the stated exact formula follows for all integers \(n\ge4\).

## Originality — PASS, qualified

The full directed-visibility study of Stojanović (arXiv:2602.03267, first 3 February 2026) defines this invariant and proves the directed single-cycle value but does not treat Cartesian products. The two most relevant product papers—Cicerone, Di Stefano and Klavžar (arXiv:2112.13024) and Korže and Vesel (2024, DOI 10.1007/s00025-024-02139-x)—work with undirected graphs. Korže and Vesel's Proposition 3.9 yields \(\mu(C_4\square C_n)=12\) from width eight onward, a different and strictly larger number than the claimed directed value eight. Targeted research-record, terminology, and primary-literature searches did not identify a theorem that implies this directed classification. The earlier undirected product formulas do not transfer because directed shortest-path intervals and the ordered-pair requirement are different. Historical priority is provisional; searches cannot exclude equivalent older terminology.

## Mathematical value — PASS

The finding resolves a natural first bounded-width toroidal family for a directed invariant newly introduced in the motivating 2026 work. The sharp width-six threshold, universal fibre obstruction, and empty-column extension give a structural rather than solely tabular answer. The precise four-vertex contrast with a published undirected torus theorem exhibits a substantive orientation effect on pairwise unobstructed shortest-route capacity.

## Closest literature and limits

Primary directed definition and directed-cycle bound: Stojanović, arXiv:2602.03267. Closest same-underlying-graph result: Korže–Vesel, Results in Mathematics 79 (2024), Proposition 3.9 (undirected, not covering). Other undirected product framework: Cicerone–Di Stefano–Klavžar, arXiv:2112.13024. Independent priority checking remains incomplete. The proof does not classify arbitrary orientations or cycle-product widths other than four in one factor.

Self-review: passed. Independent audit: not yet performed.
