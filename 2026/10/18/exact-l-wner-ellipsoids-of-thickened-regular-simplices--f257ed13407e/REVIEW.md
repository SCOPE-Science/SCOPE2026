# Self-review

## Correctness — PASS

The proof explicitly defines the ambient and intrinsic dimensions, fixes the vertex normalization, and covers every real scale including zero. Exact support functions give the nonnegative factorization \(\frac{s}{t}(p-t)^2\) for all orientations. All contact points are determined via equality normals; a finite, explicitly normalized simplex-and-signed-basis contact set has zero mean and covariance \(I_n/n\). Averaging arbitrary competing ellipsoid containment inequalities and applying AM–GM proves global volume minimality and rigidity without assuming competitors inherit symmetry. Implicit differentiation proves the stated strictly concave growth law. Exact rational checks in `verify.py` passed but are not substituted for the proof.

## Originality — PASS, with residual historical risk

The starting 2005 algorithmic work on the convex hull of ellipsoids includes the input class but states approximation algorithms, not an explicit closed-form solution for rounded higher-dimensional regular simplices; full text was unavailable for inspection. The inspected 2007 paper solves truncated ellipsoidal cone/cylinder sections, not ball-parallel simplices. General Löwner contact criteria and the lower-rank two-ball special case are acknowledged. Searches for regular-simplex offsets, thickened simplices, and covering ellipsoids did not reveal a stronger exact formula, but unsuccessful searches are not proof of historical priority. A hidden earlier equivalent remains possible.

## Value — PASS

A unit-ball parallel body of a regular simplex is a canonical smoothly rounded convex body. The theorem solves its unrestricted extremal enclosing ellipsoid in all permitted intrinsic/ambient dimensions and all nonnegative simplex scales, identifies the complete positive-scale contact locus and a scale-independent dimensional splitting law, and establishes strict logarithmic concavity of the optimal volume. This is a natural structural classification, not a numerical or arbitrary-parameter table.

## Limits

Unequal balls, irregular center configurations, and non-Euclidean offsets are not covered. Independent verification and absolute historical-priority certification have not been carried out.

Self-review: passed. Independent audit: not yet performed.
