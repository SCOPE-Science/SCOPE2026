# Scientific review: sharp simplex-volume phase cascade in Euclidean conical frusta

## Correctness — PASS

The theorem follows from five reconstructible steps: determinant convexity moves each unrestricted vertex to a base without reducing the optimum; expansion along height yields a wedge product of two horizontal difference matrices; a sharp singular-value/AM–GM argument bounds each centered group by the regular-simplex determinant and exhibits orthogonal equality; strictly decreasing ratios of the regular-simplex determinant constants give every distinct transition with no skipped split; uniform control of the score tail establishes the fixed-ratio high-dimensional limit. The normalizations in horizontal radius and perpendicular height are explicitly reversible. The proof addresses dimensions \(d\ge2\), the apex case, equal radii, and arbitrary lateral displacement.

The standalone source checker produced `PASS: 486 constructed layer configurations, 5400 random contained simplices, 9 dimension phase lists, and high-dimensional consistency checks.` These are consistency checks, not replacements for the all-dimensional proof. No independent verification is claimed.

## Originality — PASS with residual historical risk

Lassak (2011), *Approximation of convex bodies by inscribed simplices of maximum volume*, DOI 10.1007/s13366-011-0026-x, was read as complete six-page open-access PDF. Its main approximation bound applies to arbitrary convex bodies, and Lemma 2 treats a symmetric double-cone: neither determines the extremal vertex distribution across two unequal-radius parallel spherical bases or the internal phase transitions. The general contained-simplex theorem does not imply the claimed exact numerical formula.

Horváth and Lángi (2014), *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496, was read in full via its lawful arXiv HTML. Its orthogonal joins of regular simplices optimize a \((d+2)\)-vertex polytope on one sphere, not a \((d+1)\)-vertex simplex distributed across two spheres in parallel planes. The common orthogonal-regular extremizer motif is acknowledged; it does not entail the varying-radius transition sequence.

A directly same-body published result, *Universal Santaló and volume-product laws for homothetic frusta* (2026, published identifier 3dbfdaf0b359), was read in full. It computes Santaló centers and polar volume products for general homothetic convex bases, but contains no maximum-contained-simplex theorem and does not imply this sharp determinant envelope.

McKinney (1974), *On maximal simplices inscribed in a central convex set*, DOI 10.1112/S0025579300005763, was checked at the bibliographic and abstract level only; the complete text was unavailable. Its possible coverage of the central-symmetric equal-radius cylinder endpoint remains a historical-priority risk. Such coverage would not automatically subsume the asymmetric \(0<t<1\) phase cascade, but a stronger unforeseen formulation cannot be ruled out without full inspection. Searches of the research index and public literature yielded no directly dominating result, which is evidence of a gap rather than a proof of novelty.

## Mathematical value — PASS

This is a complete natural extremal invariant for all Euclidean conical frusta in all dimensions, including both cone and cylinder boundaries, with a sharp piecewise-monomial formula, all transition locations, and equality structures. The nontrivial strict phase ordering provides a dimension-dependent geometric classification rather than a fixed-size computation. The bounded narrow-base vertex count at each fixed ratio under dimension growth adds a structural asymptotic law useful for extremal simplex and convex-body approximation questions.

## Remaining limitations

One related historical full text was inaccessible. Specialist priority review and independent proof audit remain to be carried out. The formula does not classify every simplex whose vertices touch the ruled side of the frustum, nor the transition scale as the radius ratio approaches one with increasing dimension.

Self-review: passed. Independent audit: not yet performed.
