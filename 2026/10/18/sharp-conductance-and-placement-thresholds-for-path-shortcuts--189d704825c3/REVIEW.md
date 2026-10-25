# Independent mathematical audit

## correctness

PASS

For a unit path the third eigenvalue Λ=2−2cos(2pi/n) is the rank-one interlacing upper ceiling for a single nonnegative chord Laplacian. An edge vector b not orthogonal to the second nonconstant cosine mode u_2 admits a mean-zero combination of u_1,u_2 killed by b with Rayleigh quotient strictly <Λ (using b·u_1≠0), so saturation forces i+j=n−1. Reversal then separates the unchanged even sector (least positive Λ) and odd sector A=(L−ΛI)|odd with one strictly negative eigenvalue. Schur inertia gives A+wbb^T PSD iff 1+w b^TA^{-1}b<=0. The explicitly checked piecewise sine/cosine Green solution has b^TA^{-1}b=−sin((2i+1)2pi/n)/sin(2pi/n); hence the exact strict-positive sine and sharp w threshold, including equality. Maximizing sine over admissible odd r=2i+1 yields delta_n nearest-odd formula, n4 endpoint, w1 optimizer set and asymptotic 2pi/n+O(n^-3). Independently built each augmented path Laplacian and checked all chord choices for n4..14 by dense eigenvalues; no finite SVD can establish the all-n theorem.

## originality

PASS

Exact saturation equality, minimal conductance and complete optimizer family are not merely the rank-one interlacing ceiling or known generic Fiedler-vector heuristics. The full 2003 unicyclic extremal source was inaccessible, creating a concrete but not automatic originality failure risk.

## value

PASS

A path with one shortcut is a canonical constrained network-design/consensus problem. Interlacing alone yields a ceiling but not whether it is reachable; the theorem solves exactly the minimum link conductance, every saturated location at all positive conductances, and the family of n-dependent unit-link ties, with a sharp 2pi/n strength scale. These are motivated design quantities, not arbitrary numerology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
