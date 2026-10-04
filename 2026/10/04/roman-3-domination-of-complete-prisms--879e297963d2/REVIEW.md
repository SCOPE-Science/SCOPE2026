# Review of Roman \(\{3\}\)-domination of complete prisms

## Correctness
PASS. Writing \(\alpha\) and \(\beta\) for the two clique-layer label sums, the defining condition at \(a_i\) with label at most \(1\) is exactly \(\alpha+f(b_i)\ge3\), and symmetrically on the other layer. If one layer has sum at most \(2\), all but at most one matched coordinate in the opposite layer must carry enough weight to force the sharp lower bounds. Equality gives the exceptional \(n=4\) and \(n=5\) patterns. For \(n\ge6\), weight \(6\) forces both layer sums to equal \(3\), after which every composition is automatically feasible. Direct exhaustive checks for \(n=4,5\) and an independent exact aggregate dynamic program through \(n=60\) agree with the value, classification, and counts.

## Originality
PASS. The 2020 bounds paper gives general degree-based inequalities for the same invariant; targeted searches of its inspected full text found no Cartesian product, prism, or \(K_n\square K_2\) treatment. The 2023 small/large-value paper characterizes the extreme values \(3\), order minus one, and order and develops tree bounds, but its inspected full text likewise contains no complete-prism formula. Targeted web and published-results searches for the Roman \(\{3\}\) or double Italian domination of \(K_n\square K_2\), complete prisms, and prism graphs did not locate an equivalent statement or the minimum-function enumeration.

## Value
PASS. Cartesian products with a two-vertex factor are a standard graph construction, and the complete prism is a highly symmetric family not covered by the known complete multipartite formulas. The theorem gives more than a scalar value: it identifies the exact stabilization threshold, completely classifies the exceptional transition cases, and gives a closed formula for every optimum from \(n\ge6\). The square stars-and-bars count reflects an exact decoupling of the two clique layers at optimum.

Same-model review: passed. Independent audit: not yet performed.
