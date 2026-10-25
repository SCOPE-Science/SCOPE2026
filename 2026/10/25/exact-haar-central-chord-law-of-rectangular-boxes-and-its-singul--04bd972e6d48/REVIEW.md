# Scientific review: exact Haar central-chord distribution for rectangular boxes

## Correctness — PASS

The probability law is a complete all-parameter identity for every three-dimensional box with strictly positive half-lengths. The chord formula \(L=2\min_i a_i/|U_i|\) follows directly from the defining inequalities of the box. Union probabilities of three absolute-coordinate spherical caps truncate at the pair level for \(x<2R\), since \(\sum_i(2a_i/x)^2>1\). Their pair areas follow from the explicitly normalized two-coordinate spherical density and an elementary one-dimensional integral, with a direct endpoint and derivative identity for the arctangent formula. A shrinking two-cap intersection yields a \(3/2\)-power onset with a positive coefficient. The terminal event is exactly a shrinking triangle in squared-coordinate Dirichlet space, giving the quadratic tail with its normalization. The proof treats endpoints, vanishing intersections, unequal and equal side lengths, and coincident thresholds.

The actual standalone `verify.py` is dependency-free. It was executed from the new package and completed seeded checks for three boxes, pair quadrature and asymptotic coefficients with output `VERIFY_OK`. The finite checks only corroborate, and do not replace, the proof for all real parameters. The big-O bounds are local with the box dimensions fixed.

## Originality — PASS (historical-priority risk retained)

The most closely related modern motivating work [1] studies high-probability bounds for diameters of random sections but does not provide this exact three-dimensional all-aspect-ratio centered-line CDF or its sharp face-diagonal and terminal expansions. Its arXiv first-submission date is independently established as 2026-09-21. Coleman's complete available 1969 paper [2] computes explicit cube secant laws under four random sampling protocols, each with a randomized point or offset, not Haar-uniform lines constrained to pass through the fixed center. The 1981 *Intercept lengths of random probes through boxes* [3] is a plausible title-level comparator; its abstract was accessible, but full-text confirmation was not obtained, and this uncertainty is disclosed rather than silently treated as a negative result.

The complete inspected mathematical records on the Haar hexagon probability of central **plane sections** [4], the directional width distribution of cubes [5], and central chords of **planar regular polygons** [6] differ in dimension or whether the random statistic is an intersection or a projection. Neither their complete results nor the accessible historical claims about center-constrained planar parallelogram mean chords imply the all-aspect-ratio three-dimensional probability law. Targeted queries also searched the exact CDF, spherical cap overlap, chord alias, and endpoint asymptotic formulations. Absence from search results alone is not asserted to prove novelty. The remaining possibility of a classical stereological formula for the fixed-center sampling model is a real residual risk.

## Mathematical value — PASS

A complete analytic law for a natural and reproducible stochastic geometric observation of every three-dimensional orthotope is a motivated exact benchmark for random-section diameter bounds and for distinctions among stereological random-line models. The three independent half-lengths cannot be removed by Euclidean symmetry. The support, each pairwise face-diagonal threshold, its noninteger \(3/2\) onset, and the sharp terminal quadratic coefficient provide a structural classification across arbitrary aspect ratios. None is an arbitrary isolated numerical slice or a mere cube-table recomputation. The proof uses the geometry of spherical cap overlap and the Dirichlet corner, explaining why these exponents arise.

## Closest literature and limitations

[1] Guédon–Litvak–Tatarko–Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131 (2026-09-21).

[2] R. Coleman, *Random paths through convex bodies*, *Journal of Applied Probability* **6** (1969), 430–441, DOI 10.1017/S0021900200032939. Available full text read for its sampling definitions and cube calculations.

[3] R. Coleman, *Intercept lengths of random probes through boxes*, *Journal of Applied Probability* **18** (1981), 276–282, DOI 10.2307/3213189; complete text was unavailable. Its relationship to fixed-center Haar lines is unverified.

[4–6] Published mathematical research records titled *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, *Exact directional width law of the cube and its first spherical-cap transition*, and *Parity-resolved central-chord laws for regular polygons*. Their complete RESULT texts were read and compared by the section dimension, random variable, and claimed result.

The proof is confined to Haar-directions through a fixed center for Euclidean three-dimensional orthotopes; it does not address offset-invariant secants, arbitrary oblique parallelepipeds, higher-dimensional cap intersections or global uniqueness of the mathematical observation. The cited 1981 comparator and unindexed earlier stereology are the remaining originality risks.

Self-review: passed. Independent audit: not yet performed.
