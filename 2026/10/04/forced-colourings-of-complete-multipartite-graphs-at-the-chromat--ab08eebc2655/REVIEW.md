# Same-model scientific review

## Correctness
PASS. A proper colouring with exactly \(r\) colours on a complete \(r\)-partite graph necessarily assigns one colour to each part. This makes the forcing threshold transparent: with at most \(r-2\) seeded parts no vertex can initially see \(r-1\) neighbour colours, whereas with at least \(r-1\) seeded parts the unique missing part, if any, forces immediately and then all remaining vertices force. The product formulas then follow by independently choosing a nonempty seeded subset in each seeded part. The probability expression uses the exact per-vertex weights \(p\) for a prescribed colour and \(1-rp\) for being uncoloured. Exhaustive enumeration through order six independently agrees with the characterization and formulas.

## Originality
PASS, subject to the stated residual literature risk. The closest primary source, arXiv:2609.17108v1, proves the two-colour formula for bipartite graphs but does not state a complete-multipartite result for three or more chromatic colours. Targeted semantic and web searches under equivalent formulations did not locate a stronger theorem or exact table covering the claim. The closest indexed exact forced-colouring result treats maximum-degree-two graphs for three colours, a different graph class. A prior internal finding on complete bipartite graphs uses three available colours; its graph/palette regime is disjoint from the present \(r\ge3\), \(\lambda=r\) theorem.

## Value
PASS. The initiating paper proves that evaluating the forced-colouring function is generally computationally hard for fixed palettes of at least three colours. The theorem isolates a broad classical dense family where the full forcing-set structure, the complete domain-size enumerator, the probability polynomial, and the minimum forcing-domain size all admit closed forms. It also extends the structural mechanism behind the known minimal-palette bipartite case to every complete multipartite chromatic palette of size at least three.

## Closest literature and limitations
Farr's 2026 paper is the closest source: its Theorem 7 handles bipartite graphs with two colours, which is the formal \(r=2\) boundary specialization of the formula here. Farr and Morgan's earlier graph-polynomial work introduced the partial-colouring polynomial framework but was not found to contain this complete-multipartite theorem. The classical forcing chromatic number concerns unique completion from a precolouring rather than the iterative local forcing polynomial. The case of more available colours than partite sets remains open here, and terminology not surfaced by the searches is a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
