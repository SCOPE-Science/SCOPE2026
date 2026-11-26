# Independent mathematical audit

## correctness

PASS

The repaired claim treats the natural maximum-line-triple stratum without A3. For one smooth conic and five lines, the smooth-branch ADE list and Bézout give tau=20+t+e+r, with t tangents, e on-conic line crossings and r off-conic line triples. The two triples share exactly one line. Putting it at infinity identifies their four residual crossings with the corners of a 2-by-2 grid. The shared line is secant by absence of A3 and because both centers lie off the conic. Tangents among the grid lines can only occur at a corner and cannot share it. With e<=2, t+e<=4; e=4 also gives t+e=4 since every grid line is secant. With e=3 there are two secants and at most two tangents, so equality requires both remaining lines tangent. Permute the corners by reversing coordinates so the omitted corner is (1,1); the equation is A u(u-1)+Buv+D v(v-1)=0 with AD nonzero. One-variable restrictions on u=1 and v=1 give B=D and B=A, completing classification. Homogenization by u=-y/x and v=-z/x recovers the stated f. Its smoothness, tangent locations, transverse nodes and complete multiplicity budget give the reported basket. Exact integer Saito identities suffice for freeness; independently recovering the degree-three kernel gives dimension 2 and a nonzero determinant quotient -147/40 for a different basis (python /workspace/independent_checks.py 3). The τ=27 stratum bound and uniqueness do not rely on the cited unrestricted upper bound.

## originality

PASS

The repaired claim establishes projective rigidity of the equality case for the two-line-only-triple/no-tacnode stratum. It explicitly credits the known unrestricted optimum and free attainment. None of the exact prior witnesses considered belongs to the equality stratum or has the reported basket, and the closest inspected grid reduction concerns a different incidence pattern. The distinct contribution is the stratum classification, not the number 27 or exponents (3,3).

## value

PASS

The five-line skeleton is singled out by attaining the maximum number of line-only triple points. The absence of isolated tangency asks whether every tangency can be absorbed into a triple point at the known optimum. The repair answers both the realization and projective-moduli question for this geometric stratum: no family remains and both tangencies are forced. This is stronger than an extra example or an unmotivated selection of a numerical basket, and distinguishes the contribution from the already-known numerical extremum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
