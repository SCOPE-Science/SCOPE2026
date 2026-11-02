# Mathematical assessment

## Correctness — PASS

The theorem concerns independent longitude-uniform samples on a fixed spherical small circle with shortest-geodesic edges. The derivation uses exact tangent-vector dot products, the anchored cyclic half-gap density, a bijection with a positive probability simplex with explicitly differentiated Jacobian, and inclusion-exclusion of all failed angle inequalities. At the two critical parameters the proof checks which intersections are present. All integration domains and strict inequalities are specified, and the constants at both quadratic transitions follow from the local density and area of the remaining simplex regions. `check.py` independently evaluates the integration and compares directly computed intrinsic angle events with the theoretical probability; its finite experiments are corroboration, not an infinite proof.

## Originality — PASS (provisional historical priority)

The closest inspected complete primary source is Akopyan–Edelsbrunner–Nikitenko (arXiv:2007.07783, pp. 4–5 and §4.1). Its Euclidean triangles built from sphere-uniform vertices and its conditionally sampled circumcircle are not the independent uniform points on a fixed small circle joined by spherical *geodesics*. The cap-surface sampling in Le (1989) differs as a sampling measure. The Maeda (2008) and Maehara–Martini (2024) works have only abstracts or previews available, so their full results are unresolved priority risks; no assertion of whole-document noncoverage is made. Related arithmetical or combinatorial findings concern different underlying random objects. The earlier fixed-radius hyperbolic-circle law follows a different curvature geometry and its first branch cannot imply the spherical overlap correction or extinction threshold. The reviewed statement is the full piecewise probability law and its two sharp geometric transitions, not merely a formal curvature substitution.

## Mathematical value — PASS

The law classifies all possible radii for a natural spherical geometric sampling problem, including an exact probability beyond the reach of a single-obtuse-angle subtraction. It exhibits two distinct critical phenomena: simultaneous nonacute angles become possible at one radius, and acuteness becomes impossible at a sharp larger radius. The explicitly computable dilogarithm correction, monotonicity, and quadratic onset give structural information of intrinsic geometric interest beyond a routine probability evaluation.

## Remaining limitations

The result applies only to fixed-radius geodesic circles of radius strictly between zero and a hemisphere, boundary-arclength sampling, and intrinsic angles. The complete texts of some broader surveys and older shape-density studies were unavailable, leaving provisional historical priority. The computational tests do not independently certify the mathematical proof.

Self-review: passed. Independent audit: not yet performed.
