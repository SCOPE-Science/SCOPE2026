# Scientific review

## Correctness — PASS
The invariant follows because a forbidden value cannot cross its own coordinate via adjacent swaps without landing on it. All signatures are realized by the ordered-block canonical words. Each bubble-sort inversion is checked separately across blocks and within both constrained blocks, establishing a legal path of length at most \(\binom n2\) to a representative and the component bound. Two independently implemented exact finite checks cover all forbidden masks through \(n=7\) and \(n=8\), respectively. The proof, rather than these finite enumerations, establishes the unbounded parameter claim.

## Originality — PASS, with residual risk
Compared the exact constraint and allowed transitions with Baril–Vajnovszki (2004), Vajnovszki (2010), and Clark (2013), as well as related full-permutahedron and crown-graph formulations. Earlier Gray codes allow nonadjacent transpositions or rotation operations, unlike the present adjacent-swap induced graph; graph derangements concern existence, not this metric. No inspected source implies the general component formula. Residual risk: an older theorem on permutations with forbidden positions or adjacent swaps may already imply it, perhaps under a poset/linear-extension formulation. A failed search is not a uniqueness certificate.

## Mathematical value — PASS
The exact exponential disconnection law holds for every subset of forbidden diagonal positions, describes all components by an explicit invariant, and supplies constructive paths and a uniform diameter bound. It explains structurally why generating derangements with a more permissive swap operation differs from feasible adjacent exchanges, not merely furnishing a small numeric example.

## Limits
The general upper bound is not asserted sharp and the individual component size distributions are not determined. Independent external scientific review has not occurred.

Self-review: passed. Independent audit: not yet performed.
