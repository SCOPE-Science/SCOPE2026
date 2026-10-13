# Self-review

## Correctness
PASS. For every zero-zero edge \(a_i b_j\) with \(i\ne j\), its neighborhood union omits exactly \(a_j\) and \(b_i\), so feasibility is exactly \(W-x_j-y_i\ge2\). A failure therefore requires \(x_j+y_i\ge W-1\), which is impossible for \(W\ge6\). The remaining six weights are exhausted by the displayed pair-pattern table, with both directions checked: every listed pattern has a violating edge, and every violating edge forces one listed pattern. Subtracting these counts from the full ternary-label polynomial yields the formula. Exhaustive direct enumeration for \(3\le n\le6\) independently agrees with every coefficient and with the minimum-function classification.

## Originality
PASS. The 2025 initiating paper defines the exact invariant but its inspected full article treats paths, cycles, trees, and bipartite complexity, with no crown, complete-bipartite, polynomial, or enumerator result. Targeted published-finding corpus searches under the invariant name, abbreviation, crown/matching-deleted aliases, complete bipartite graphs, and weight-enumerator terminology found no covering theorem. The closest indexed results are an ordinary Roman \(\{2\}\) enumerator on complete multipartite graphs and a restrained-domination profile of crown graphs; neither implies the edge-based crown enumerator.

## Value
PASS. The result classifies every feasible labeling by weight for a canonical regular bipartite family under a recently introduced NP-hard invariant, rather than only evaluating one minimum. The structural reduction shows that deleting one perfect matching from \(K_{n,n}\) creates exactly a degree-five low-weight defect polynomial while every labeling of weight at least six remains feasible. This supplies a reusable benchmark and sharply separates the new edge-based invariant from its stronger vertexwise Roman \(\{2\}\) analogue.

## Closest literature and limitations
The closest primary source is Almulhim–Mondal, *Vertex–Edge Roman {2}-Domination* (2025), DOI 10.3390/math13132169. It introduces the invariant but does not treat crown graphs or all-function enumeration. The closest indexed all-function result concerns ordinary Roman \(\{2\}\) domination on complete multipartite graphs, a stronger vertexwise condition on a different graph class. An unindexed equivalent formulation remains a residual literature risk.

Self-review: passed. Independent audit: not yet performed.
