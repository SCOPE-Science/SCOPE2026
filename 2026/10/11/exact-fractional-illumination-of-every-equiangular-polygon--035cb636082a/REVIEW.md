# Review

## Correctness
**PASS.** At each vertex of an equiangular \(n\)-gon the illuminating directions form an open arc of length
\[
\pi-\frac{2\pi}{n},
\]
and the arc centers are equally spaced by \(2\pi/n\). Therefore any direction illuminates at most
\[
r_n=\left\lfloor\frac{n-1}{2}\right\rfloor
\]
vertices. Summing the \(n\) vertex constraints gives the lower bound \(n/r_n\). For the upper bound, one direction is chosen in the common intersection for each cyclic block of \(r_n\) consecutive vertices and assigned weight \(1/r_n\); every vertex belongs to exactly \(r_n\) blocks. A convex-combination argument shows that vertex illumination constraints dominate the edge-interior constraints. Equality in the double-counting chain also proves the stated rigidity. The bundled checker independently verifies the cyclic incidence pattern through \(n=500\).

## Originality
**PASS, with an elementary-cyclic-system residual risk.** The defining 2009 paper was materially inspected through the definition, the fractional-transversal reformulation, and the proof of its regular-pentagon proposition. It proves only
\[
i^*(P_5)\ge\frac52
\]
for that example, not equality or an all-\(n\) polygon formula. A modern full-text treatment of fractional illumination was also inspected and contains no polygon or pentagon specialization. Searches using regular polygon, equiangular polygon, cyclic interval, pentagon, and both parity formulas did not locate an implication-equivalent result. General fractional-covering theory gives the linear-programming language but does not itself identify the geometric cyclic system or its parity-sensitive rank.

## Value
**PASS.** The regular pentagon is the explicit nontrivial polygonal example singled out in the paper introducing fractional illumination, so closing its lower bound and extending it to the entire equiangular class is motivated by the source rather than an arbitrary computation. The theorem gives an exact normal-fan invariant for every number of sides, an explicit optimal measure, equality rigidity, and a parity-sensitive approach to the smooth-body value \(2\).

Same-model review: passed. Independent audit: not yet performed.
