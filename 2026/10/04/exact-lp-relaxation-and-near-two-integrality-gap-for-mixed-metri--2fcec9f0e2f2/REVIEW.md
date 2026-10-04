# Review of Exact LP relaxation and near-two integrality gap for mixed metric dimension of double fans

## Correctness
PASS. Every pair of vertices of a double fan is realized as an exact mixed resolving neighborhood, and all singleton resolving neighborhoods are classified explicitly from incident vertex-edge pairs. Since every other resolving neighborhood has at least two vertices, these constraints exactly generate the continuous relaxation. The resulting optimization reduces, for \(n\ge4\), to two forced unit coordinates plus the fractional vertex-cover polytope of \(K_n\), giving the unique half-vector and optimum \(\frac{n+4}2\). The included checker reconstructs all original mixed-distance constraints and independently confirms the optimum and coordinatewise uniqueness for \(2\le n\le20\).

## Originality
PASS. The foundational source supplies a binary integer program but does not study its continuous relaxation. The 2023 max-mixed-dimension paper concerns the integer parameter and, among other results, already covers the small graph \(F_{2,2}=K_4-e\). The 2024 double-fan paper studies the integer dimension. Searches for fractional mixed metric dimension, LP relaxations, fractional mixed resolving sets, integrality gaps, and double-fan optimization returned no equivalent continuous-relaxation theorem. The integer formulas are explicitly excluded from the novelty basis.

## Value
PASS. The relaxation is canonical because it is obtained directly from the published integer-program formulation. The result gives the complete optimizer, not merely a numerical bound, and exhibits a natural family whose integrality ratio tends to two. This supplies a concrete benchmark for mixed-metric integer programming and clarifies how much the basic LP can underestimate the combinatorial optimum.

Same-model review: passed. Independent audit: not yet performed.
