# Same-model review

## Correctness
**PASS.** The proof correctly uses an ergodic invariant probability \(\mu\) equivalent to Lebesgue measure. For each \(d_N=c+(1-c)/(N+1)\), the fixed hole \((a,d_N)\) has positive \(\mu\)-measure, so almost every orbit enters it and \(S_f(a,d_N)\) is \(\mu\)-null. Equivalence, specifically \(\operatorname{{Leb}}\ll\mu\), transfers this to Lebesgue nullity. The symbolic part is the general self-survival/realization argument appearing in the focal source: it yields the countable-cover inclusion of the parameter pullback by fixed-hole survivor sets. The conclusion then follows from countable subadditivity and the source's Corollary 3.

A critical normalization check was made: assuming only \(\mu\ll\operatorname{{Leb}}\) would not justify the needed implication from \(\mu\)-null to Lebesgue-null, so the final theorem explicitly assumes equivalence.

## Originality
**PASS.** The focal paper leaves the decreasing-Lorenz entropy theorem conditional on \((P)\) and verifies \((P)\) only for one two-slope piecewise-linear family. The closest earlier theorem, Sun--Li--Ding (2024), gives the invariant-measure criterion for increasing expansive Lorenz maps. The increasing theorem does not imply the decreasing result because the decreasing class uses alternating order and the negative-doubling address map. Glendinning--Hege (2026) addresses chaos/dimension transition boundaries rather than the pullback-null implication.


Residual risks are an unindexed equivalent theorem under different terminology or a future revision of the very recent focal preprint.

## Value
**PASS.** Condition \((P)\) is the explicit extra metric hypothesis blocking the focal source's general decreasing-map entropy conclusion. Replacing it with the standard and interpretable condition of an ergodic invariant probability equivalent to Lebesgue measure is a meaningful structural extension, not a parameter renaming or a finite recomputation. It also clarifies exactly which direction of absolute continuity is needed.

## Closest literature and limitations
The closest literature is the 2024 increasing-Lorenz devil-staircase theorem and the 2026 focal decreasing-Lorenz paper. The finding is conditional: it does not prove that arbitrary decreasing Lorenz maps possess an equivalent ergodic invariant probability, and it does not establish a general Hausdorff-dimension transfer.

Same-model review: passed. Independent audit: not yet performed.
