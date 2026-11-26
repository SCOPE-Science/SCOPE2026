# Independent mathematical audit

## correctness

PASS

On a projective chart normalized by a nonzero coordinate of the remaining columns B, the permanent is exactly u^T A(B)v: a permutation chooses ordered distinct rows for u,v. At the all-ones B, A=(n-2)!(J-I) is invertible, with eigenvalues (n-1)(n-2)! and -(n-2)!. On the determinant-open chart, w=A(B)v has a regular inverse. The equation becomes sum u_i w_i, whose full Jacobian ideal is (u,w), including scheme structure; the equation itself belongs to the ideal. Thus the open transverse cone has dimension 2n-1 and multiplicity two, and the zero-column space is a whole irreducible component since it is the entire singular locus on an ambient open meeting it densely. There are exactly n(n-1) distinct spaces of the specified types (not necessarily all components); even for n=3 the surviving coordinate positions distinguish row and column spaces. The codimension in the ambient projective space is 2n. The Hessian determinant is (-1)^n(det A)^2, so the degree-n(n-2) divisor is det A, not the full determinant divisor; no squarefreeness or degeneracy classification follows. Inspected checker.py, checker_output.txt and VERIFICATION.md. The retained 42 expansion and six determinant checks are finite; they were not rerun and are not required for the algebraic proof. The checker uses int.bit_count, so Python 3.10+ rather than the advertised 3.8+ is appropriate for replay.

## originality

PASS

Credit prior singular containment, the complementary-permanent Jacobian/Hessian and the rank-drop criterion. The supported distinct contribution is the explicit algebraic trivialization of the entire hypersurface on the determinant-open projective charts, not the computation of the transverse tangent form at a point. The component and divisor statements are geometric consequences or close to consequences of known calculations, not independent priority claims.

## value

PASS

A uniform regular coordinate chart on every such stratum gives usable geometric information beyond a tangent-space dimension, including the full reduced Jacobian scheme where the chart applies and an explicit boundary of applicability. This is a structural lemma about classical singular strata, without claiming to solve the global component or codimension problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
