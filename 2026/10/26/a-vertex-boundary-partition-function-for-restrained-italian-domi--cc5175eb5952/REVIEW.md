# Scientific review

## Correctness — PASS

The proof first excludes zero labels at private leaves from the joint zero-neighborhood and Italian defense conditions, then characterizes exactly the admissible zero-core sets by minimum induced degree one. Every positive core/leaf contributes one of two labels, and each zero core contributes either a forced 2-leaf or an independently chosen 1/2-leaf depending on whether it has a positive core neighbor. This yields the full coefficient formula; its minimum exponents and unit leading coefficients give the optimizer census. Path and cycle counts follow from a complete run decomposition with all endpoints and short orders checked. The universal-vertex consequence follows from the boundary being at most one less than the base order. The included Python program independently constructs graph neighborhoods and brute-forces actual label assignments for 80 base graphs, including every graph of order at most four. It separately tests the run-pattern boundary formula for paths through order 18 and cycles through order 18; these finite tests corroborate, rather than establish, the infinite theorems.

## Originality — PASS (qualified by literature-access risk)

The 2020 publicly posted foundational work defines the same restrained Italian function and develops scalar bounds and extremal configurations; it does not state the leaf-corona weight enumerator in the inspected primary text. Later scalar studies discuss ordinary paths/cycles or some corona graphs, while the 2022/2023 restrained *domination polynomial* enumerates vertex sets of a different problem. The directly relevant 2023/2024 article by Abdulhasan and Mojdeh describes scalar results on certain corona graphs in its abstract, but complete text was inaccessible, so special scalar overlap cannot be excluded; no full-document noncoverage claim is made. Indexed searches of equivalent terminology, corona variants, coefficient formulas and predecessor results found no identified polynomial or complete optimal-labeling census that logically implies the stated result. Closest records concerning other domination variants on coronas do not imply it. The original contribution assessed here is the complete weight polynomial with the vertex-boundary correspondence and the optimum-labeling counts for combs/sunlets; prior scalar cases are not asserted to be newly determined.

## Mathematical value — PASS

A natural full weight enumerator is not determined by an optimization number. This result converts restrained Italian functions on a canonical and widely used graph construction into a base-graph induced-minimum-degree and boundary partition function, giving every coefficient and uniquely identifying all minima. It derives exact infinite comb and sunlet optimum censuses with sharp congruence effects (constant/linear/quadratic regimes), along with a structural equality characterization for the universal lower weight bound. These are natural cases and graph properties rather than arbitrary slices of the parameter space.

## Closest literature and limitations

- Samadi, Alishahi, Masoumi and Mojdeh, *Restrained Italian domination in graphs*, arXiv:2009.12209, original preprint dated 2020-09-25: foundational definitions, bounds and extremal graphs; original work credited.
- Volkmann, *Remarks on the restrained Italian domination number in graphs*, DOI:10.22049/CCO.2021.27471.1269: scalar graph-family results, including ordinary paths and cycles, not the optimal-function polynomial on their coronas.
- Velmurugan and Kala, *Restrained domination polynomial of join and corona of graphs*, DOI:10.1142/S179383092250118X: a different, set-based invariant; only the abstract was accessible.
- Abdulhasan and Mojdeh, *Further results on (total) restrained Italian domination*, DOI:10.1142/S1793830923500179: most relevant remaining coverage risk; abstract reports some corona scalar values, full proof and scope unavailable.

The proof excludes zero private leaves and applies to any finite simple base. The specialized counts treat named vertices, not symmetry classes. No complexity statement or independent audit is claimed. Complete priority over inaccessible or unindexed literature is not established.

Self-review: passed. Independent audit: not yet performed.
