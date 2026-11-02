# Self-review

## Correctness — PASS

For every \(a,b,c>0\), the tetrahedron's centroid is interior. Each edge crosses a generic central plane with probability equal to the angle between its endpoint rays divided by \(\pi\), from an exact two-lune area calculation. There are six edges, with three pairwise angles appearing twice. This proves the arcsine formula, and the section must have either three or four vertices. Pair balancing increases the sum of arcsines because, for two proportions \(x>y\) and the third \(z>0\), \(x(1-x)-y(1-y)=(x-y)z>0\); this controls the derivatives even across the inflection at \(1/2\). The unique regular maximizer, full range, local Taylor coefficient, and uniform boundary cusp follow rigorously. The Gaussian triangle-inequality equivalent is checked pointwise by sign patterns. The executable checker corroborates independently derived formulas and four independent normal-sampling cases; simulation is not used as an infinite proof.

## Originality — PASS, with historical limitation

The spherical-lune crossing probability itself is classical. Feldman--Klain (2008) concerns triangular *orthogonal projections* and arbitrary tetrahedral angle sums, not the Haar **central-sectional** probability as a function of equifacial shape. Kabluchko (2019, arXiv:1905.01533) studies expected angle sums of random simplices, not fixed equifacial centroid sections. Godland--Kabluchko--Zaporozhets (2020, arXiv:2007.02590) derives Gaussian-projection and Grassmann-angle identities, not the strict shape ordering here. A publicly indexed regular-simplex centroid-section vertex-count law covers the equal-axis benchmark but does not, on its stated claim, give the heterogeneous-axis Schur ordering and edge cusp. Closest other indexed equifacial-tetrahedron results concern radius ratios and other invariants. Exact synonym/half-normal, stronger-coverage, and equation-level searches found no directly covering result. A not fully accessible indexed record and any older unindexed specialized inequality leave bibliographic priority provisional; no claim of verified uniqueness in all literature is made.

## Mathematical value — PASS

The probability of a triangular centroid section is a canonical combinatorial statistic of a random plane. Equifacial tetrahedra form a natural three-parameter family that includes the regular tetrahedron but has meaningful anisotropy. The result gives its *complete* normalized shape law, a strict majorization order, a unique sharp regular optimizer, the entire attainable probability interval, and a geometry-independent square-root degeneration exponent. The Schur order is not a direct application of ordinary concavity, since \(\arcsin\sqrt t\) ceases to be concave beyond \(1/2\); the three-part constraint is decisive. The same theorem is a sharp formation-probability comparison for three independent scaled half-normal lengths. This is more than a routine special-case recomputation of the known regular value.

## Limits

Only the stated geometry, zero offset, and Haar orientation are covered. The global best stability constant is not determined. The literature comparison is substantive but not an independent historical-priority certification.

Self-review: passed. Independent audit: not yet performed.
