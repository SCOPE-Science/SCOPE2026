# Self-review

## Correctness — PASS

The occupancy lemma is derived from the original neighbor-count condition for every absent cell. Exhausting four row/column-support cases proves the minimum-size lower bounds, and the equality cases are counted without overlap: all-to-all \(2\)-by-\(2\) rectangles, row-pair selections for two-row boards, and columnwise row-surjections on the exceptional small boards. The free-standing verifier enumerates original-definition forts and compares the exact minimum configurations over 26 boards; its second independent exhaustive test checks the occupancy lemma on 10190 subsets. The proof, not finite tests, establishes all-parameter validity.

## Originality — PASS (with residual risks)

Actual published-finding corpus semantic searches under rook-graph, product-of-cliques, and line-graph-of-complete-bipartite aliases yielded nearest fort claims on **complete multipartite base graphs**, which do not cover Cartesian products of cliques. Relevant fort papers by Cameron et al. (2023), Becker et al. (2024), and Brimkov et al. (2025) were examined in relevant sections, including Cartesian-product constructions, graph-family enumerations, and minimum forts of hypercubes. These sources establish the framework but do not state the present all-parameter exact minimum-fort multiplicity theorem for rook graphs. Unindexed or indirectly implied results cannot be ruled out absolutely, and the sources were inspected selectively rather than every page being reread linearly.

## Value — PASS

The family \(K_p\square K_q=L(K_{p,q})\) is a canonical graph product and line graph. Enumerating **all smallest fort obstructions** resolves the bottom layer of its zero-forcing obstruction hypergraph and reveals a nonuniform small-board phase diagram and a quartic-to-quadratic change in the number of optimal certificates. It is not merely an isolated computation or a restatement of the minimum cardinality; it supplies every optimizer and an infinite-family counting law.

## Sources and limitations

Primary comparators: arXiv:2310.17904, arXiv:2404.05963, arXiv:2507.10826. Search absence is not proof of publication priority. The enumeration addresses only the minimum-cardinality layer, not all inclusion-minimal forts or full forcing parameters. Mathematical independent audit is not performed.

Self-review: passed. Independent audit: not yet performed.
