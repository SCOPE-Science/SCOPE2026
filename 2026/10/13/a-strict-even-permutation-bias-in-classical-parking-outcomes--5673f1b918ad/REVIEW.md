# Scientific review: even-parity bias of classical parking outcomes

## Correctness — PASS

The statement concerns the parity of the permutation of cars by occupied space, rather than the inversion statistic of the original preference list. Conditioning on the final car's occupied position yields a genuine bijection: earlier cars split into independent left/right parking functions, the last preference has exactly as many possibilities as its final position, and the cross-block sign is a Gaussian-binomial subset sum evaluated at \(q=-1\). This proves the signed recurrence including the boundary cases \(n=1\) and empty blocks.

Separating even and odd indices gives \(O=E^2+2zEE'\) and \(E'=E^3+8zE^2E'+4z^2E^2E''\) as *formal* series. Positivity follows by coefficient induction, since the coefficient determining the next even value uses earlier nonnegative values and includes a strictly positive \(E^3\) contribution. The odd values follow by positive convolution. A standalone exact-arithmetic checker returned 209 passing assertions, including direct enumeration of preference lists and an independent full-permutation weight comparison. Computation corroborates, but does not replace, the all-size proof.

## Originality — PASS, with stated risk

The closest direct predecessor is Pinsky, arXiv:2404.11529, Theorem 1, which gives the weight of each individual outcome permutation. This general formula permits a factorial-sized alternating sum but supplies neither the sign of that sum for arbitrary size nor its closed convolution or positive formal differential equation. The present claim is therefore not simply a quoted special case or restatement of that theorem. Pinsky's construction is explicitly credited.

Paguyo–Yin, arXiv:2502.07110, studies cycles of the preference map, not outcome-permutation sign. Celano et al., arXiv:2508.11587, studies inversion counts of preference words, not of permutations defined by the final parking arrangement. Searches for parity, sign, outcome-permutation inversion, signed enumerations, the initial integer values, and the displayed differential identity did not reveal a covering result. This is evidence of a literature gap, not proof of universal priority; an unindexed equivalent formula or a consequence of an overlooked symmetric-function specialization remains possible.

## Value — PASS

A permutation sampled uniformly has perfectly balanced even and odd parity when there are at least two labels. The parking-induced distribution is highly nonuniform, but whether all-size sign cancellation yields exact balance, one-sided bias, or a sign change is not resolved by its individual-atom formula. The theorem proves a strict universal direction, gives a constructive exact enumeration, and explains that direction through a positive formal equation despite substantial cancellation in the original alternating sum. The parity contrast is an intrinsic coarse statistic of the induced probability law, not an arbitrary parameter slice, and positivity is an infinite-family structural fact.

## Limitations and closest sources

The result gives no limiting size or asymptotic expansion for the normalized parity bias, and it is specific to classical uniform sampling over successful preference lists. Full inversion-generating polynomials, weighted preferences, and alternative parking disciplines remain open here. The proof requires the elementary Gaussian-binomial \(q=-1\) specialization; the checker verifies many finite instances but is not an independent proof of infinite correctness.

Primary materials: R. G. Pinsky, arXiv:2404.11529 (Theorem 1 and proof); J. E. Paguyo and M. Yin, arXiv:2502.07110 (model, abstract, cycle theorems); K. Celano et al., arXiv:2508.11587 (definition of the separate preference-word inversion statistic and Theorem 1.1).

Self-review: passed. Independent audit: not yet performed.
