# Same-model review

## Correctness

PASS. Ghomi's one-direction theorem gives three reflection planes with normals \(e_1,e_2,e_3\). Translating to the centroid makes them linear. The first two reflections compose to the exact \(z\)-rotation
\[
\begin{pmatrix}
-7/25&-24/25&0\\
24/25&-7/25&0\\
0&0&1
\end{pmatrix}.
\]
Its half-angle has cosine \(3/5\); the root-of-unity algebraic-integer argument proves the angle is an irrational multiple of \(\pi\), so its powers are dense in the axial circle. The third reflection maps the \(z\)-axis to the \(y\)-axis. Closedness of the symmetry group and the Euler-angle decomposition then force \(SO(3)\)-invariance and hence a ball. For any two prescribed directions, a nonround spheroid about an axis perpendicular to both is symmetric across both required normal planes, so the curvature comparisons hold with equality.

## Originality

PASS. The focal source is one-directional and does not state a finite test count. The closest inspected 2026 symmetry paper studies sequences of axes or hyperplanes and does not state a three-direction curvature-order test or its minimality. Targeted semantic searches covered the source ID, finite directions, sphere forcing, irrational-reflection generation, and the universal two-direction spheroid obstruction without locating an equivalent statement.

Residual risk: the reflection-group step is classical, so an older observation may exist under different terminology. The originality assessment is therefore for the combined sharp curvature-test theorem, not for the abstract group fact by itself.

## Value

PASS. Determining the minimum number of directional tests is the natural finite-data completion of a new one-direction symmetry theorem. The answer is exact, constructive, and sharp: one explicit triple forces a sphere, while every pair admits a smooth strictly convex nonround counterexample. This provides a reusable finite rigidity criterion rather than a routine corollary for a single special body.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Mohammad Ghomi, *Mean Curvatures and Symmetry of Convex Hypersurfaces*, arXiv:2608.28410v1. The closest broader symmetry comparison is Alfonseca-Cubero, Cordier, Morales-Amaya, and Verdusco Hernández, *Characterizations of generalized convex bodies of revolution*, DOI:10.4153/S0008439526102215.

The result is restricted to \(\mathbb R^3\), gives one sufficient triple rather than a classification of all triples, and does not claim a higher-dimensional minimum.
