# Self-review

## Correctness — PASS

The domain is a two-hub metric tree with integer \(d\ge2\) and arbitrary real \(t>0\). Its nodal Gram matrix has a positive-definite \(2\times2\) Schur complement, and the row formulas for the inverse are explicit in \(U,V>0\). Every edgewise evaluation kernel is affine; integrating its absolute value gives an exact, attained leaf and hub evaluation norm. The strict leaf/hub comparison is expressed as a positive \(21\)-term polynomial certificate in \((d-2,t)\). The derivative of the exact leaf norm has a degree-seven numerator with at most one positive root by a coefficient-sign argument and Descartes' rule, and the \(7/3\) boundary is controlled by a quartic with one sign change. Both identities are independently checked symbolically and the assembled matrix calculation is independently replayed at 35 parameter pairs. There is no extrapolation from a finite experiment to a universal conclusion: the all-parameter proof is in `RESULT.md`. The elementary interval and sign conventions are defined there, including vertex atoms (absent), finite vs. unattained limits, and the strict interior inequality.

## Originality — PASS (qualified)

The closest existing exact star calculation has one central branching vertex and establishes the sharp \(7/3\) star-family envelope, but cannot imply the present two-hub bridge-dependent norm. The present result in fact violates that envelope once \(d\ge9\) and the bridge is sufficiently long. Kayumov's dated 2004 exposition examines interval L-splines; the actually inspected Oswald 2006 article studies planar triangulations, not one-dimensional metric trees; and Boman 2006 provides general weighted finite-element estimates rather than an identified exact double-star formula. Searches of indexed scientific claims for double-star, spline orthogonal projector and branch-length resonance returned no covering mathematical statement; these failed retrievals do **not** establish uniqueness. The unresolved possibility of a previously published equivalent double-star calculation, and the unavailable full text of Boman, are recorded in `AUDIT.json`.

## Value — PASS

The question is motivated by a natural first departure from one-vertex metric stars: two branching junctions connected by a tunable edge. An exact norm and all norming locations are determined for every degree and bridge length. The fact that the star-family sharp supremum \(7/3\) is crossed precisely with nine pendant edges per hub and that the norm then has a unique interior maximum is a substantive shape-instability phenomenon, not a renaming or parameter substitution. The first-order bridge asymptotic independently locates the sharp integer threshold. Applications to unrestricted graph topologies or nonuniform leaf weights are not asserted.

## Coverage and limits

References include the 2004 Kayumov interval-spline synopsis, the full accessible HTML of Oswald's 2006 arXiv article, and the Boman 2006 bibliographic abstract. Exact previously recorded star results were used solely to exclude a covered case; no old result was re-audited. No independent referee, external theorem prover or cross-implementation certification has been performed.

Self-review: passed. Independent audit: not yet performed.
