# Scientific review

## Correctness — PASS

The claimed object is finite: the \(35\) three-subsets of a seven-set, with disjointness adjacency. The exact distance/intersection rule has four distinct values. The two independent cardinality checkers exhaust all \(52{,}360\) potential four-vertex resolving sets and all \(324{,}632\) potential five-vertex resolving sets, returning zero and \(149{,}184\), respectively. Smaller bases are excluded by monotonicity. Two distinct complete exchange implementations agree on \(6{,}331{,}500\) edges, connectedness, degree bounds, and degree sum. Two independent \(S_7\)-generator orbit computations yield \(48\) orbits; breadth-first search visits the entire exchange graph from each representative, yielding eccentricity \(5\) on \(146{,}160\) bases and \(6\) on \(3{,}024\). Separate shortest-path computations verify two explicit pairs at distance six. No extrapolation beyond the named finite graphs is used.

## Originality — PASS with residual literature risk

Bailey et al. (arXiv:1203.2660, pp. 2–4, 12, 15–16, 19) give the distance correspondence for Odd and Johnson graphs, the Fano resolving construction and general bounds. Their results do not count all five-bases or constrain exchange paths. Peng et al. (DOI:10.1166/jctn.2016.4951) give the exact minimum size five, which is acknowledged as prior work; their accessible abstract does not assert the present optimal-set count or exchange geometry. Additional targeted mathematical-record and scholarly searches by the terms Odd graph, \(KG(7,3)\), \(J(7,3)\), resolving set, metric base, \(149{,}184\), and exchange graph found no covering result. The closest database results on edge bases of crown and half graphs concern different objects and do not imply this census. The 2016 original full text was inaccessible, so the remaining possibility of a recorded but unindexed enumeration is explicitly retained. Equivalence to the Johnson formulation is fully accounted for.

## Mathematical value — PASS

The natural question is not re-establishing the known metric dimension but determining the flexibility of *all* optimal landmark configurations in the canonical next Odd graph after the Petersen graph. The complete orbit and exchange results show that the optimal choices, despite \(48\) symmetry types, are all connected by at most six replacements, with an exceptional \(3{,}024\)-configuration eccentricity class. This yields an exact optimal-configuration landscape with a potentially useful robustness bound, not an arbitrary numerical slice or a repackaged metric-dimension calculation.

## Remaining limitations

The statement is finite. The diameter uses exhaustive breadth-first searches from exactly one representative of each rigorously generated symmetry orbit; independently implemented tests cover enumeration, edge count, connectedness and two diameter witnesses but do not rerun all 48 representative breadth-first searches independently. The 2016 article remains accessible only by abstract and bibliographic material, not full content.

Self-review: passed. Independent audit: not yet performed.
