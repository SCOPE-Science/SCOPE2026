# Review of The generic \(B_4\) unexpected quartic has one ordinary quadruple point

## Correctness
**PASS.** The claim is reduced to an exact witness and an open-condition argument. At \(P=[1:2:4:8]\), the published cone equation becomes a quartic \(f(y_1,y_2,y_3)\) independent of the vertex coordinate. Exact Gröbner bases of the gradient ideal on \(y_1=1\), \(y_2=1\), and \(y_3=1\) are each \([1]\), so the projective base quartic is smooth. The checker independently verifies the 16 base-point incidences and one-dimensional interpolation kernel. Standard cone geometry then gives the unique singular point, and adjunction gives \(E^2=-4\) and discrepancy \(-2\).

Risk: the conclusion is deliberately generic; special vertices can lie on a discriminant and are not classified.

## Originality
**PASS.** The 2018 primary paper states that the general \(B_4\) unexpected quartic is a cone, while the 2021 companion-varieties paper gives its explicit equation and additional common base points. Neither inspected treatment states smoothness of the generic plane-quartic base, the singleton singular locus, the ordinary-quadruple analytic description, or the discrepancy. Targeted database searches for these equivalent formulations and consequences returned no covering result.

Closest literature: the companion-varieties paper is the closest source because it writes the exact family used here; its Section 4.1 studies the cone equation, base points, and companion threefold rather than the singularity type of the cone itself.

Residual risk: a less directly indexed paper or thesis may contain the same local classification. No such source was located in the targeted searches.

## Value
**PASS.** This closes a natural geometric question left implicit by a standard example of higher-dimensional unexpected hypersurfaces: whether the named generic cone acquires singularities along its base directions and how severe its vertex is. The result gives a complete generic singularity description and shows that the vertex is worse than log canonical, a structurally meaningful boundary property rather than a coordinate-only computation.

Same-model review: passed. Independent audit: not yet performed.
