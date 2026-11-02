# Self-review

## Correctness — PASS

The central-section probability model specifies a right equilateral triangular prism with base circumradius one, positive half-height \(h\), and an unoriented Haar-uniform normal. A generic section's corners are precisely the prism edges with opposite signs at their endpoints. Exhaustive enumeration of its nine edges on the full azimuthal fundamental sector yields the complete four-interval sign table. The normal's absolute vertical coordinate is uniform on \([0,1]\); exact integration produces all three formulas, including their normalization. Differentiation identifies a strictly monotone stationary equation, proving the global unique maximum. Taylor expansions justify both limiting regimes.

The standalone `verify_prism.py` recomputes section side counts from all nine original edges for an equal-area spherical grid. Its largest discrepancy over six tested heights is below \(0.000551\); it checks a 12-digit stationary root and leading asymptotic constants. These calculations are corroborative and are not used to prove any continuum statement.

## Originality — PASS under the documented best-knowledge scope

Hibi–Li's 2014 full text classifies vertex-preserving separating hyperplanes (in particular for cube and poset polytopes); generic central prism cuts creating edge-intersection vertices are outside their theorem's hypotheses. Earlier stereology, especially Voss (1982), is a substantive near neighbor. Voss's abstract advertises exact frequencies for unspecified families of polyhedra and an integral-geometric method; the whole 1982 paper was inaccessible, so it is not claimed to exclude the present formulas. Ohser–Mücklich (1995) study random-offset sections of randomly situated regular-prism populations for inverse stereological recovery, without identifying the present fixed-center optimal pentagonal probability in accessible material. Known fixed-center calculations for boxes and pentagonal prisms have different face graphs and do not imply the present triple law or its sharp optimizer by specialization. Search and comparison details and unresolved access risks are recorded in AUDIT.json. Independent historical-priority verification remains outstanding.

## Value — PASS

A triangular prism is the simplest prism with a genuine five-sided generic central section, and the possible intersection types form a natural complete three-element classification. The theorem gives the **entire** Haar side-count distribution for all aspect ratios and solves the nontrivial shape optimization of pentagonal-section probability uniquely. The optimizer is not the equilateral-edged prism; the thin-prism behavior distinguishes a quadratic triangular probability from a linear pentagonal probability. These are substantive, directly interpretable facts about a canonical stereological family, not an arbitrary numerical slice or routine isolated substitution.

## Limits and material source risk

The result does not concern offset-random planes, oblique or irregular prisms, nonuniform orientations, or section areas. Voss (1982) remains a genuine overlap risk because the accessible abstract does not identify which simple polyhedra receive analytical formulas and the full text could not be read. Ohser–Mücklich (1995) was available at abstract level. No claim of independent scientific certification is made.

Self-review: passed. Independent audit: not yet performed.
