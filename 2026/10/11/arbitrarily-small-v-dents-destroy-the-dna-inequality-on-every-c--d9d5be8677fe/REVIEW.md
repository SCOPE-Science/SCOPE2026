# Same-model review

## Correctness
**PASS.** A \(C^2\) convex Jordan curve has a point of positive curvature \(\kappa\). In tangent graph coordinates, replacing the arc between \(x=-t\) and \(x=t\) by the V through \(X_t=(0,\kappa t^2)\) creates exactly one reflex turn of magnitude \(\kappa t+o(t)\). Because the signed total turn remains \(2\pi\), the total absolute curvature becomes \(2\pi+2\kappa t+o(t)\). The removed arc and replacement V have lengths differing only by \(O(t^3)\), so the dented cell's average curvature is \(2\pi/p+(2\kappa/p)t+o(t)\). The removed cap has depth \(O(t^2)\). A homothetic contraction by \(Mt^2\) about a fixed interior point has inward clearance at least \(Mrt^2\), so for fixed \(M\) large enough it lies inside the dented cell. Its average curvature is \(2\pi/p+O(t^2)\), which is strictly smaller for small \(t\). The proof does not use finite computation to infer an infinite statement.

## Originality
**PASS.** Larson's materially inspected Section 9 is the closest source. It explicitly says that an extension of the polygonal dent theorem would imply failure of the DNA inequality for arbitrarily small dents of smooth convex curves and describes that corollary as apparently approachable, but does not prove it. The present theorem supplies a direct proof for every \(C^2\) convex curve and gives quantitative asymptotics for both the dented cell and the interior competitor. Targeted searches under DNA-inequality, average-total-curvature, smooth-dent, V-notch, and Larson-corollary formulations returned no statement implying this theorem. The residual risk is an unindexed or differently worded later observation.

## Value
**PASS.** The claim resolves a specific published smooth-boundary corollary left open in the principal nonconvex DNA-inequality paper. It establishes a sharp scale separation that explains the instability: a dent of geometric depth \(O(t^2)\) causes an order-\(t\) curvature penalty, while an admissible interior homothetic competitor pays only order \(t^2\). This is a structural boundary phenomenon for a classical convex-geometric inequality, not a recomputation or arbitrary finite slice.

## Closest literature and limitations
Larson's paper is decisive: Theorem 8.1 treats polygonal edge dents, while Section 9 explicitly proposes the smooth-convex small-dent consequence without proving it. Lagarias--Richardson establishes the convex-cell inequality, and Tabachnikov's full exposition concerns the convex setting and classical special cases. The new theorem is existential for a canonical V-dent family and does not prove Larson's full piecewise-smooth classification or claim that every small dent fails. The full Lagarias--Richardson article was not accessible from the current author-PDF link, so only its published abstract and its role as documented in the inspected primary sources were used for the coverage comparison.

Same-model review: passed. Independent audit: not yet performed.
