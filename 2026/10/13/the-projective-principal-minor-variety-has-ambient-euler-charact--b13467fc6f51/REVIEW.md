# Self-review

## Correctness
PASS. The archival projective principal-minor variety is invariant under the natural \(\operatorname{GL}_2(\mathbb C)^n\)-action. A powers-of-two diagonal one-parameter subgroup has distinct weights on all \(2^n\) tensor-coordinate lines, so those are the only ambient projective fixed points.

For diagonal \(A,B\), the projective principal-minor map becomes the Segre monomial map
\[
\phi(A,B)_I=\prod_{i\in I}a_i\prod_{i\notin I}b_i.
\]
Thus every coordinate fixed point belongs to the variety. The fixed locus therefore has exactly \(2^n\) points. Algebraic \(\mathbb C^*\)-localization and projectivity give \(\chi_{\mathrm{top}}=2^n\), and additivity gives zero compactly supported Euler characteristic for the complement.

The packaged checker independently verifies the weight separation and coordinate-point specializations on broad finite ranges. Those computations are regression evidence only.

## Originality
PASS. Borodin--Rains and Lin--Sturmfels give the same determinantal/principal-minor variety, its symmetry, dimensions, difficult equations, and its first hyperdeterminantal model, but their inspected full texts contain no Euler- or Poincaré-type calculation. Targeted semantic and web searches under both standard names and topological aliases found no covering statement.

A related theorem gives the analogous numerical Euler formula for the symmetric principal-minor subvariety. That does not imply the present theorem for the larger general variety: Euler characteristic is not monotone under inclusion, and the two varieties have different dimensions and defining ideals.

## Value
PASS. The theorem computes a canonical global invariant of a classical difficult projective variety in every dimension. It shows that every nontrivial general principal-minor variety has the full ambient Euler characteristic and that its complement has compactly supported Euler characteristic zero, a structural cancellation not visible from the known dimension, degree, or ideal calculations.

Self-review: passed. Independent audit: not yet performed.
