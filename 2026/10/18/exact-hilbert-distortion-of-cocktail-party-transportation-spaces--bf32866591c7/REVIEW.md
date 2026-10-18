# Scientific review: exact Hilbert distortion of cocktail-party transportation spaces

## Correctness — PASS

The proof defines the graph metric, centered molecule hull and both orthogonal invariant summands. It establishes an exhaustive classification of extreme dual potentials using tight-edge connectivity, reduces every quadratic candidate by convex group averaging, calculates each dual vertex energy exactly, and supplies matching global lower and upper certificates for each integer range. The exceptional dimensions are treated separately; no numerical test is used as proof of the infinite cases. The independent standard-library rational checker passes all dimensions \(2\le k\le8\).

## Originality — PASS, subject to bibliographic limits

Dilworth–Kutzarova–Ostrovskii (arXiv:1807.03814v1) give the graph transportation quotient; Higashitani–Jochemko–Michałek (arXiv:1807.07678v1, Proposition 3.5) already classify the relevant facets; D'Alì–Delucchi–Michałek (arXiv:1910.05193v1) connect these polytopes to finite metrics. None of these inspected contributions optimizes Euclidean distortion for the complete multipartite family with all parts of size two. General Banach–Mazur extremal theory in Grundbacher–Kobos (arXiv:2407.08829v1) supplies bounds but not the formula. Comparisons with available mathematical research records found results for complete bipartite, equilateral and complete-multipartite inradii, none implying the new result for \(k\ge3\). The \(k=2\) four-cycle value is a previously known boundary check. Unindexed equivalents remain possible.

## Mathematical value — PASS

The result computes a natural isomorphic Banach-space invariant for an infinite family of non-tree metric spaces, identifies the unique invariant ellipsoid shape in all dimensions, and proves a sharp low-dimensional symmetry-breaking cutoff. The proof yields exact optimality rather than an upper bound or numerical exploration. It makes the specific factor \(\sqrt{k}\) and the six-vertex exception available to future comparisons of metric-derived norms.

## Limitations

Only equal two-vertex parts, real scalars and unit graph edges are proved; uniqueness is claimed among invariant optimal forms rather than all forms. The finite checker verifies the stated cases but cannot replace the all-dimensional argument. Bibliographic completeness and independent external review remain unresolved.

Self-review: passed. Independent audit: not yet performed.
