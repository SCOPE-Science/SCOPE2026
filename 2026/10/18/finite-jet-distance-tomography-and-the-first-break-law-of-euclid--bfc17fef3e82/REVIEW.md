# Scientific review

## Correctness — PASS

The hypotheses are explicit: dimension \(d\ge3\), positive side lengths, independent volume-uniform interior points, and Euclidean distance. The difference vector has the product triangular density \(V^{-1}\prod_i(1-|z_i|/a_i)_+\). On balls of radius not exceeding the shortest side, expanding this density and applying the stated ball-monomial beta integral gives every coefficient of the exact short-distance polynomial. The leading coefficient determines volume, the next \(d-1\) give elementary symmetric functions of reciprocal lengths, and their product is the reciprocal volume; Vieta recovers the positive lengths. Perturbing the penultimate symmetric coefficient at a polynomial with simple positive roots supplies the generic \(d-1\)-coefficient obstruction. Immediately beyond the shortest side, the excluded axial caps are disjoint and the leading beta integral gives the positive \(\varepsilon^{(d+3)/2}\) term, including repeated shortest sides.

The supplied checker reproduces the inverse in dimensions two through five, computes independent planar numerical quadratures, checks cap asymptotics in dimensions two through four, and compares three-dimensional and four-dimensional Monte Carlo distance laws with the formula. These experiments are corroboration, not infinite-dimensional certification. The published theorem covers dimensions at least three.

## Originality — PASS relative to inspected sources

Bäsel (arXiv:1208.6228, §§1–4) provides a planar forward distance distribution, explicitly including rectangle-related prior work; Pure et al. (arXiv:1903.07757, §1 and framework sections) treat arbitrary planar polygon forward distance laws. The 1990 rectangle and 1999 cube papers were identified but their full primary texts were not accessible; no whole-document negative conclusion is drawn from their abstracts. Holmin–Kurlberg–Månsson (arXiv:1702.08096) recover box side lengths from discontinuities of a *random-line free-path* distribution, a different sampling measure and observable. Wang (arXiv:2610.01916, §1–2) develops general pair-distance/covariogram methodology and a first-order small-range law, which does not state this exact degree-\(2d\) orthotope polynomial, optimal \(d\)-coefficient inverse, or multiplicity-sensitive first-break expansion. The relevant published database records about planar polygon pair distances, hyperplane-shadow tomography of boxes, and gauge-distance bounds were compared at the level of their statements; none establishes the combined theorem.

**Priority risk:** The covariance/overlap identity and planar special cases are classical. An equivalent inverse or breakpoint result might appear under older box chord/covariogram terminology, particularly in the unavailable full 1990 or 1999 source. Novelty here is assessed only for the explicitly defined, all-dimensional pair-distance local-jet inverse and sharp first-break law, not for the convolution identity itself. No historical uniqueness or independent certification is claimed.

## Mathematical value — PASS

The observable is a canonical Euclidean distance between two random interior points. Its exact local \(d\)-coefficient jet recovers all orthotope edge lengths and the ambient scale, sharply improves on the need for an entire global distribution, and has a complete positive-root feasibility test. The shortest side reappears independently as the first nonpolynomial radius threshold with a multiplicity-sensitive explicit exponent and coefficient. These are natural inverse-geometric and distributional invariants; generic minimality is proved, rather than inferred from parameter counting.

## Limitations

The reconstruction assumes an orthotope model and population measurements. Finite-sample stability, noise robustness, and classification among arbitrary convex bodies are not proved. A full historical-priority review remains necessary, and the reviewer here is not independent.

Self-review: passed. Independent audit: not yet performed.
