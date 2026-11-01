# Scientific assessment: unequal-radius spherical-lens John ellipsoid

## Correctness — PASS

The theorem covers every integer dimension \(d\ge2\), radius ratio \(0<q<1\), and separation \(0\le L<1+q\). The nested-ball case is immediate. In the other cases, substitution into the squared distance to each of the two ball centers gives a nonpositive quadratic-square identity for active sphere contacts and a strictly concave endpoint inequality for a screened pole. The one-pole scalar equation is strictly increasing in its parameter. The two-latitude scalar equation is strictly decreasing on its specified interval; the derivative is an explicitly negative rational function with a strictly positive polynomial factor. This establishes existence and uniqueness and covers both transition endpoints. The normalized contact distributions have mean zero and second moment \(I_d/d\), satisfying John's global optimality criterion for arbitrary inscribed ellipsoids. The accompanying implementation checked 675 separate parameter cases by analytic maximization of quadratic boundary-distance polynomials. The analytic proof, not the finite tests, establishes the theorem.

## Originality — PASS, with residual historical-priority risk

The closest inspected full text is Güler–Gürtuna (arXiv:0709.0707), whose general extremal-ellipsoid theorem provides the global optimality tool and whose worked cases concern slabs, truncated cones, and cylinders. Uhler–Wright (*Packing Ellipsoids with Overlap*) describes an optimization formulation for ellipsoid overlaps rather than an exact two-ball lens contact diagram. Kahan's relevant treatment studies *circumscribing* ellipsoids, not the maximal inscribed one, and the inspected portion principally concerns concentric data. Prior equal-radius spherical lenses possess reflection symmetry, whereas the present unequal-radius case exhibits a sharp radius screening boundary and a nontrivial phase change. None of the inspected results establishes the stated all-dimensional formulas or the exact \(q=1/d\) threshold. This is a best-knowledge originality assessment, not proof against every historical source. Generic semidefinite representability does not alone imply the stated exact formulas; undocumented specializations in prior numerical optimization work remain a risk.

## Mathematical value — PASS

Intersections of two balls provide a canonical nonsmooth family for testing geometric approximation and contact certificates. The result goes beyond routine application of John's theorem: it explicitly determines the optimizer and every contact orbit, including the unexpected fact that for radius ratio at most \(1/d\), one sphere contacts at a pole for all nontrivial separations, however thin the lens becomes. For larger ratios it determines the exact geometric phase threshold and a universal product rule for normalized contact latitudes. This is a complete, natural classification of a small-parameter convex-geometric family, with an exact constructive global-optimality witness and reproducible scalar solution.

## Scope, evidence, and remaining limitations

The theorem excludes equal radii, tangent or disjoint balls, and lenses defined by more than two balls. The cited comparator full texts cover related but not identical geometric objectives, and an older explicit solution in a different terminology remains possible. The 675 numerical cases only check concrete instances, with the universal claim resting on algebraic identities and John's criterion. Independent historical-priority verification and independent scientific audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
