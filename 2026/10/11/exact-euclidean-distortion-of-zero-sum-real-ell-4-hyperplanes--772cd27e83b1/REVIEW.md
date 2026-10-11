# Scientific review of an exact Euclidean distortion formula

## Correctness
**PASS.** The center-subtracted quartic polynomial is invariant under all coordinate permutations and of degree four, so Riener's half-degree principle (Theorem 1.3 of arXiv:1001.4464) reduces each sharp inequality to two-valued test vectors. Exact calculation yields \(Q_k=n/[k(n-k)]-3/n\), with extrema at \(k=1\) and the nearest integer to \(n/2\). Averaging an arbitrary feasible distortion ellipsoid is legitimate because its inner containment inequalities are affine in its positive-definite matrix and its outer containment inequalities have a linear matrix inequality representation. Invariant matrices restrict to scalar Euclidean forms on the zero-sum hyperplane. The proof treats every real vector and every linear isomorphism, not just finite samples. The standalone symbolic checker verifies the algebra and is not presented as a universal proof.

## Originality
**PASS, subject to bibliographic uncertainty.** Riener (arXiv:1001.4464, full text, Theorem 1.3 and proof) supplies a general symmetry reduction, not the Banach--Mazur distance. Grundbacher--Kobos (arXiv:2603.18268, full text, Theorem 1.1 and Section 2) treats direct \(\ell_p\)-sums, whereas the zero-sum hyperplane is a linear constraint coupling all coordinates. Existing exact planar Banach--Mazur records describe specific two-dimensional norms and do not imply a uniform codimension-one formula with distinct parity regimes. Targeted theorem- and parameter-level searches found no covering statement. Historical subspace literature not fully indexed or accessible remains a residual risk; no search failure is taken as mathematical proof of novelty.

## Value
**PASS.** The zero-sum subspace is the canonical standard representation of coordinate permutations and a natural codimension-one subspace of the classical real \(\ell_4\) space. The exact Euclidean distortion in *every* dimension, including a sharp odd/even split, an exceptional Hilbertian two-dimensional member, and the optimal asymptotic constant, is a natural complete geometric invariant rather than an arbitrary finite example. The averaging step certifies the invariant under all changes of coordinates, not merely the inherited Euclidean coordinates.

## Sources, boundaries, and risk
Primary theorem: Cordian Riener, *On the degree and half degree principle for symmetric polynomials*, arXiv:1001.4464 (2010), Theorem 1.3. Closest modern Banach--Mazur coverage: Florian Grundbacher and Tomasz Kobos, *Exact Banach--Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268 (2026), Theorem 1.1, whose direct-sum assumption does not cover this constrained hyperplane. Other exact planar distances likewise do not supply an all-dimensional formula. No uniqueness of optimizers is claimed, and independent bibliographic and mathematical verification is not completed.

Same-model review: passed. Independent audit: not yet performed.
