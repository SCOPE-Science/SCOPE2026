# Independent mathematical audit

## correctness

PASS

The unique hyperelliptic quotient is a genus-zero curve split over the finite field. Its double cover has at most 16 rational points, with equality exactly when all eight fibers split. Over F_7 this condition is F(P) in {1,2,4} at each standard base point. The evaluation vector has coordinate sum zero, and interpolation at seven finite points is bijective; the eighth coordinate is forced. For isomorphisms, the descended PGL_2 map must identify the homogeneous sextics up to a square scalar; conversely this gives a lift. Normalization of the eight points introduces no scaling on degree-six evaluations, since every nonzero field element has sixth power 1. I independently replayed the complete finite calculation with `python3 /tmp/opencode/review04_replay.py`: enumerate exactly the 9*7^5 coefficient vectors with constant and leading coefficients in {1,2,4}, screen the six remaining finite values, and apply polynomial Euclidean gcd with the derivative. This returned 924 split and 588 squarefree distinct evaluation vectors. Closing the given representatives' vectors under x->x+1, x->3x, x->1/x and scalar multiplication by 2 gives disjoint orbits of 84 and 504 covering all 588. The first three transformations generate PGL_2 by affine changes and inversion; the last generates the square scalars. Thus 2*1008/orbit_size gives 24 and 4 rational automorphisms. Independently counting with w^2=-1 over F_49, including the two points at infinity, gave 46 and 44. The degree lists of gcd(f,X^(7^k)-X) at k=1,...,6 were (0,6,0,6,0,6) and (0,0,0,0,0,6), which force the two asserted branch partitions. Newton identities and the reciprocal symmetry yield the stated quartics; different characteristic polynomials exclude F_7-isogeny. All uploaded checker outputs were treated as recorded evidence, not executed. Completeness of the replay is only for the stated field, genus and rational-fiber criterion.

## originality

PASS

The fiber bound, its attainability and the possible Weil polynomials at this trace are not the contribution. The distinct supported claim is the arithmetic isomorphism classification with multiplicities one in each isogeny type, the actual two branches and stabilizers, and the resulting fixed-coordinate orbit census. The inspected isogeny theorem and known small-field census context do not establish these arithmetic multiplicities or the combined refinements. The closest inaccessible early numerical study is a meaningful residual risk, not evidence against coverage or a reason to abstain from a decision.

## value

PASS

The natural extremal problem asks which arithmetic curves attain the canonical double-cover fiber bound, not merely the maximum. Distinguishing one class in each of two Jacobian isogeny types and recording degree-six versus three quadratic branch orbits and the two stabilizer sizes gives useful input for arithmetic tests and cover constructions. The fixed-coordinate count is a consistency consequence and useful census datum, not the reason for valuing the result by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
