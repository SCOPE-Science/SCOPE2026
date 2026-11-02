# Scientific review: Three-translate Crofton conservation

## Correctness — PASS

The line normalization is explicit. Intersections of each translated convex body with a fixed-normal line family correspond to three equal-length offset intervals. Pairwise intersection of the original translates forces the interval ranges to have a common intersection for every normal. Sorting their translations decomposes the covered offsets into five consecutive occupancy blocks, proving the exact \(1,2,3\) lengths \(w_T,w_T,w_K-w_T\) pointwise; Cauchy's perimeter formula then gives the invariant-line result. Independently, three equilateral disk projections lead to exact one-, two- and three-fold intersection measures and complete inclusion–exclusion. The second derivative of the triple-overlap formula at the critical ratio gives the claimed quadratic coefficient. Embedded independent numeric interval enumeration passes across three convex-body shapes and eight disk aspect ratios. It is not relied on as a proof for infinitely many directions.

## Originality — PASS, with residual priority risk

The closest full-text literature directly inspected is Kaiser's 2002 *Line Transversals to Unit Disks* (DOI 10.1007/s00454-002-2821-5) and Heppes' *Transversals in Superdisjoint T(3)-families of Translates* (DOI 10.1007/s00454-010-9292-x, available online 14 September 2010). Their relevant definitions, results and arguments address existence of transversals and combinatorial Helly-type thresholds, not invariant line-measure histograms or fixed-direction equality of exactly-one and exactly-two events. The classical existence boundary for equilateral disks is independently described by Cut-the-Knot and is **not** assigned new priority. Searches on incidence conservation, multi-translate Crofton formulas, and triple-disk random line hit counts found no directly matching prior law. The mechanism uses classical interval inclusion–exclusion and Cauchy's theorem, and an older integral-geometric treatment might contain a logically equivalent formulation; this uncertainty remains explicit.

## Mathematical value — PASS

The equality of *two distinct line-incidence classes* for **all** triples of pairwise intersecting translates of **every** planar convex body is a natural, geometric, shape-independent conservation law, holding separately at each direction. It extracts a measurable translation-triangle invariant from a random-line experiment without requiring common intersection or symmetry. In the complementary disjoint-disk regime, the complete exact distribution resolves the quantitative phase transition from zero to positive triple-hit probability, including its non-smooth second-order onset and exact coefficient. The complete theorem is more than a name change or an arbitrary numerical instance.

## Scope, risks and audit status

The random-line measure is restricted and normalized by conditioning on hitting the union. The general conservation identity does not assert the same behavior for unequal shapes, arbitrary rotations, or four translates. The equilateral formulas apply to all positive ratios but do not classify general center configurations. Historical priority for a potentially equivalent classical Crofton computation is not independently certified.

Self-review: passed. Independent audit: not yet performed.
