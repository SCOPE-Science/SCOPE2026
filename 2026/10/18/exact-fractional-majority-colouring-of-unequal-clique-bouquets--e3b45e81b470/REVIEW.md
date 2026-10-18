# Scientific assessment

## Correctness — PASS
The local capacity bound \(|S\cap(\{h\}\cup C_i)|\le\lfloor s_i/2\rfloor+1\) holds for every majority-stable set, regardless of hub membership. Summing the fractional coverage constraints across each central block yields the stated lower bound. Two explicitly defined and independently sampled distributions give valid majority-stable sets, and weights \(1\) and \(L-1\) cover all vertices with total weight exactly \(L\). The proof treats all sizes \(s_i\ge1\) and numbers of cliques \(t\ge1\). A direct graph/LP checker agrees for all 230 enumerated small profiles; no finite extrapolation is used.

## Originality — PASS, with priority risk
The October 2026 fractional-majority paper gives broad bounds, complexity results and a different sampling construction, not an exact clique-bouquet formula in the inspected portions. The earlier 2019/2021 article develops the fractional relaxation and universal bounds. Related mathematical records concerning majority C-colouring of complete multipartite graphs, strong-majority edge-colouring and ordinary fractional graph colouring are not implication-equivalent. Searches under windmill, friendship, clique-sum and majority-stable terminology disclosed no exact matching theorem. This does not prove exhaustive priority: an uncatalogued general block-gluing result may subsume the statement, and relevant primary manuscripts were inspected by pertinent sections rather than exhaustively line by line.

## Value — PASS
The parameter is a natural fractional analogue of a major directed graph-colouring invariant. The theorem completely classifies it on all one-hub clique bouquets with arbitrary unequal clique sizes. The sharp parity transition and maximum-over-blocks law are structurally informative because the hub's outdegree changes when new cliques are attached, whereas the exact optimum remains governed by a single peripheral clique. The proof supplies an optimal fractional-colouring construction, not just a numerical test.

## Limits
The classification does not extend to general oriented or arbitrary block graphs, and independent validation or decisive bibliographic priority certification has not occurred. The computed checks support the proof but are not evidence for the infinite parameter range.

Self-review: passed. Independent audit: not yet performed.
