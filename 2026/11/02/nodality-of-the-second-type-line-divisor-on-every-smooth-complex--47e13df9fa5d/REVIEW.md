# Self-review

## Correctness — PASS

The proof uses an arbitrary smooth complex cubic threefold and an arbitrary triple line. Smoothness makes the two-dimensional pencil of normal binary quadratics basepoint-free; the uniqueness of the tangent plane and smoothness justify the coordinate normalization to \(s^2u+t^2v\). The triple-plane condition forces both \(s w^2\) and \(t w^2\) terms to vanish and leaves a nonzero \(k w^3\) term. The Fano chart has invertible Jacobian in its other four normal coordinates, so those coordinates start in order three. Taking the determinant of the three restricted normal derivatives then gives a universal quadratic jet \(-6kef\); its Hessian determinant is \(-36k^2\ne0\). This is a formal ordinary node. The published singular-support theorem covers all remaining points; the Fitting-ideal consequence is the standard local Jacobian computation. The exact standalone checker independently verifies the key coefficient identities for arbitrary symbolic cubic coefficients. These are symbolic identities rather than numerical experiments.

## Originality — PASS, with residual risk

The closest primary article is Bockondas–Boissière, *Triple lines on a cubic threefold*, first posted 2022-01-21 (arXiv:2201.08884), equation (2), Theorem 6, and especially Remark 9 (published 2023, p. 755), which explicitly states the universal nodality question remains open. Their result identifies the *support* of singularities, but does not imply the nondegenerate quadratic tangent cone needed for nodality. Lahoz–Naranjo–Rojas (arXiv:2106.08683) give the class and general-member results, not universal nodality; Bockondas–Bossoto (arXiv:2309.08124) study particular lines and Eckardt configurations without the universal local ring. Work on cubic fourfolds addresses another dimension. Searches against accessible research records and prior claims found no stronger covering assertion. Older incomplete records and possible unindexed earlier arguments are genuine residual risks, not a novelty proof.

## Mathematical value — PASS

The result answers an explicitly stated geometric question about a classical divisor on every smooth cubic threefold, including special reducible cases. The upgrade from singular support to node-type singularities determines local multiplicity, \(\delta\)-invariant, Tjurina number, and reducedness of the intrinsic singular subscheme. The associated genus formula is a consequential, not substituted, corollary. This is substantially beyond a known-support restatement or a special-parameter calculation.

## Boundaries and verification

No assertion is made over arbitrary positive characteristic or about every possible count of triple lines. The exact symbolic checker certifies the universal algebraic identities; the basis-normalization and formal-geometry steps are established in the proof. No independent external mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
