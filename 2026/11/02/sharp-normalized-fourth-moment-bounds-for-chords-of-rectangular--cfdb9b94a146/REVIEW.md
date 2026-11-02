# Scientific review of rectangular-box surface chord dispersion

## Correctness — PASS
The exact statement concerns two independent points sampled with normalized **surface area** from all six faces of a full-dimensional rectangular box in three-dimensional Euclidean space. The conditional face law has probabilities \(p_i=abc/(a_i(ab+bc+ca))\), and yields the second and fourth mixed coordinate moments used in the proof. The fourth chord-moment identity follows from independence and central symmetry without assuming independence of coordinates in the unconditional surface law.

The two final inequalities are reduced to homogeneous polynomial identities with positive integer coefficients. The upper certificate has 15 positive monomials. For the lower certificate the ordered half-length substitution \(a=w+v+u,b=w+v,c=w\) has 39 nonzero, all-positive monomials, and equality requires \(u=v=0\). The singular-limit leading terms and a continuity argument establish exact sharpness and full attainability. The verifier regenerated these identities exactly; five rational face-pair integrals separately checked the moment formulas. Its seeded simulations are only auxiliary.

## Originality — PASS, provisional historical priority
The 1999 Mathai–Moschopoulos–Pederzoli article treats cube distances and selected face-pair schemes, not an explicit all-aspect-ratio sharp optimization according to its accessible publisher abstract. Its complete text could not be accessed, leaving an acknowledged historical-priority risk. The dated 2013 Tong–Ahmadi–Pan preprint treats **planar polygon-interior** sampling and transformations from line chords to point distances; accessible substantive sections use a different probability space. Fixed-cube face-to-face calculations on MathWorld are also distinguished from normalized moments for the full boundary of an arbitrary cuboid.

The closest identified published geometric comparison concerns the fourth-moment ratio for **planar parallelogram boundaries**; its one-dimensional boundary measure and its fourth-moment amplification comparison do not cover three-dimensional cuboid surfaces. General convex-body interior pair-distance inequalities and directional orthotope-shadow moment formulas also use different sampling models/observables. Searches used box/cuboid/orthotope, surface/boundary/faces, chord/line picking, normalized fourth moment and coefficient-of-variation variants; no inspected claim implies both present sharp constants and the cube equality rigidity. This is a best-knowledge originality assessment, not an independent historical certification.

## Mathematical value — PASS
The ratio \(\mathbb E[D^4]/(\mathbb E[D^2])^2\) measures dispersion of squared distances and is insensitive to scale. Unlike evaluation of one fixed-cube moment, the theorem completely determines its shape range over every positive rectangular-box aspect ratio, proves a unique minimizer, and gives a geometrically interpretable unattained extremum in a rod-like degeneration. The exact coefficients require a genuine global positivity argument, not just differentiating along one aspect-ratio line. This supplies a sharp benchmark for surface-sampled spatial distances.

## Limitations and closest literature
The finding does not recover the three half-lengths from one statistic, estimate finite-sample errors, address nonrectangular parallelepipeds, or extend the statement to arbitrary dimension. Full-text access to the 1999 cube-distance article was unavailable; hidden stronger results remain a residual priority risk. This same review verifies mathematical details and accessible overlap evidence only, not independent publication priority.

Self-review: passed. Independent audit: not yet performed.
