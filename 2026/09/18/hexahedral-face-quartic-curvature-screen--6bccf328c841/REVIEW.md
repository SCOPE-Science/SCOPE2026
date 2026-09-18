# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The main identities admit direct symbolic and analytic checks.  The chain rule gives h'=P/(4a^2).  If a is constant, direct differentiation gives h''''=-6 b_2^2/a; if a is nonconstant, Euclidean division b=a l+r reduces the only fourth-order contribution to -r^2/(4a), yielding h''''=-6 r^2 a_1^4/a^5.  Hence h'' is concave.  Repeated Rolle arguments give the three-root bound, and concavity of h'' excludes two negative-to-positive stationary crossings.  At P=0, the Schur complement of f_ss=2a gives det Hessian=P'/(2a).  The exact rational example has three feasible stationary roots with curvature signs (-,+,-), so the coefficient-class three-root bound is attained.  The accompanying symbolic artifact verifies all displayed algebraic identities.

The principal edge cases were checked separately.  When P is identically zero, the primary source already proves that perimeter candidates suffice.  Multiple roots are not screened solely by P': the stated rule uses the actual sign change of P, retaining an odd-multiplicity negative-to-positive root and rejecting stationary roots that do not represent a local minimum.  If a vanishes, a strictly smaller interior face minimum is excluded by the source paper's argument, so the screen is applied only where a>0.

## Originality

**PASS, to the best of our knowledge.** The primary source arXiv:2609.19926 was inspected at the theorem and algorithm level.  It derives the quartic P, states that up to four interior roots may be retained, notes that some retained points can be saddles, and explicitly reports that its implementations do not use concavity screening and retain feasible negative-curvature stationary points.  It does not state h''''<=0, the resulting three-root bound, uniqueness of a minimum-capable root, or det Hessian=P'/(2a).

Searches using the source title, hexahedral Jacobian face minimization, quartic stationary points, negative curvature, concavity screening, and synonymous mesh-validity terminology did not identify an earlier statement of these refinements.  The accessible 2017 Johnen-Weill-Remacle paper and the 2022/2023 hex-meshing survey concern Bernstein-coefficient certification/subdivision rather than the new exact face-quartic candidate structure.  No inaccessible paper was identified whose title or available description specifically suggests coverage of the one-minimum theorem.  Because the primary source is very recent, simultaneous or unpublished follow-up work remains a residual originality risk.

## Value

**PASS.** The result changes the exact candidate structure of the new boundary-minimization algorithm: a nominal quartic can have at most three stationary roots on the positive-a interval, and only one can be a face minimum.  The simple-root test P'>0 is an exact Hessian-curvature certificate, while the multiple-root sign rule is also exact.  This reduces the worst-case number of post-root-solve interior jacdet evaluations from four to one per face, while preserving correctness for both boundary-minimum and strict-validity queries.  The quartic root solve remains necessary, so the contribution is a structural and implementation-level simplification rather than a new asymptotic complexity class.

## Limitations

The result does not reduce quartic root-solving degree or establish finite-precision runtime gains.  The explicit three-root sharpness witness belongs to the abstract face-polynomial coefficient class; geometric realization of that particular tuple by an actual trilinear hexahedron is not claimed.  Higher-order finite elements are outside the statement.  Originality is to the best of our knowledge.
