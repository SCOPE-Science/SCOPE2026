# Independent audit — 2026-10-01

## Final scientific disposition

**PASSED**

## Correctness (C): PASS

Independent reconstruction from the shift matrix gives zero 4-cycles, rank(HX)=rank(HZ)=186, CSS orthogonality, and k=28. Independent singular-value computation gives s2≈2.72800676, consistent with the exact 2.70<s2≤2.73 inertia certificates. An independent meet-in-the-middle syndrome enumeration excludes base codewords of weight at most 7 and verifies the given weight-8 word. The listed weight-7 support has zero syndrome for both checks and lies outside both relevant row spaces, so d≤7. The inequality \(9/s_2^2<100/81<3/2\) follows in the correct direction from s2>2.70.

## Originality (O): PASS

The primary finite-length lifted-product literature gives general design constraints and different example matrices, and the foundational lifted-product literature gives the construction. Searches found no prior occurrence of this exact lift-16 shift matrix, its (400,28) ranks, spectral interval, distance-8 base certificate, or the stated weight-7 logical. The result is not a formal consequence of the design theorems without solving this instance.

The comparison included equivalent formulations, broader coverage, exact-instance searches, and direct implication from prior theorems.

## Value (V): PASS

The exact instance is motivated by finite-length quasi-cyclic lifted-product code design. Its weight-7 logical and the certified failure of a specific spectral transfer route give a concrete diagnostic at the same scale as published finite-length design examples, while the claim is carefully limited to this route and instance.

## Sources inspected

- https://arxiv.org/abs/2503.07567
- https://doi.org/10.1109/TIT.2021.3119384
- https://arxiv.org/abs/2502.20297

## Residual risks

- No quantum lower bound is proved, and exact-instance literature searches cannot rule out an unindexed private computation; neither risk changes the stated finite certificate.
