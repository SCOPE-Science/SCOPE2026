# Independent mathematical audit

## correctness

PASS

The canonical embedding of a smooth plane quartic identifies abstract isomorphism with projective equivalence; over F2 there is no residual equation scaling. The coordinate group has order (8-1)(8-2)(8-4)=168, and swap, cyclic permutation and elementary shear generate it by elementary row operations. Geometric singularity is equivalent to the quartic and all its first derivatives having a common geometric zero in one of the three affine charts, so the computation must test the chart ideals for 1; in characteristic two the equation itself must be retained in these tests. For genus three, the first three projective point counts give the three Newton coefficients and the functional equation supplies the remaining ones. A smooth quartic has no line component, so its restriction is nonzero; being a square is exactly vanishing of the two odd mixed coefficients. A rational effective degree-two contact divisor with exactly one distinct rational point must be twice that point; zero or two rational points give the other two types. Independently reproduced the exhaustive 32767-form, 279-orbit computation, the 78 smooth classes of combined size 10920, counts over F2/F4/F8 and all 546 line restrictions, matching every bundled CSV row. The five double fibers have first coefficient triples (-1,0,2), (-1,1,0), (0,0,0), (0,0,3), (0,1,3); exactly the second and fourth split, hence 73 Weil and 75 joint values. For masks 4249 and 4469 the unique bitangent restrictions are Y^4 at Z=0 and (Y^2+YZ+Z^2)^2 at X=0; at 4347 and 4415 they are Y^4 at Z=0 and (Z^2+YZ)^2 at X+Y=0. The first-degree-through-third counts are (2,6,11) and (3,5,18) for the two pairs, respectively; independent degree-four-through-six checks gave (26,22,87) and (17,33,86). This is finite exhaustion at F2, not a claim for larger fields. Frozen replay entry points are verify_census.py then verify_independent.py in the record folder (Python/SymPy); the uploaded scripts were inspected, not executed. The reported independent run's complete source was not archived in the review delivery.

## originality

PASS

The supported distinct contribution is the full zeta/contact alignment, particularly the two equal-zeta, equal-bitangent-count pairs with different splitting. The 78-class census and the earlier alignment with the base-field point count are not new. A class catalogue keyed by projective orbit makes a join possible, but no second matching full-zeta table furnishing that join was established in the inspected sources. One published equal-zeta pair is a different fiber and does not distinguish contact signatures. The assessment does not establish priority of the bare zeta distribution.

## value

PASS

The contact divisor is a natural refinement of the rational bitangent count; the Weil numerator records arithmetic point counts but not their placement along bitangents. The two verified fixed-count collisions prove that the refinement captures information missing from both coarser measurements, while the full census specifies exactly when it improves this invariant over F2. This is more than a recomputation of the known contact marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
