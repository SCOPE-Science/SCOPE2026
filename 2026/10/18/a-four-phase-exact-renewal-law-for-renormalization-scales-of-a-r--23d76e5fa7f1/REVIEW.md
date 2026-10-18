# Scientific review: exact renewal scales in a rhombus piecewise isometry

## Correctness — PASS

The domain is the full-measure set of parameter values in the normalized interval \([0,\sqrt2]\) having an infinite nonboundary itinerary under the Lowenstein–Vivaldi full-branch map \(f\). The object is the canonical induced base-triangle similarity-length hierarchy, not a phase-space orbit. The source's Theorem 1 and branch equations establish the full-step multiplier \(q^{|i|+|j|+2}\) where \(q=\sqrt2-1\). Cylinder-length products prove independence of the \(f\)-digits; pairing gives positive independent exponents with the explicit squared generating function.

The infinite exact hit formula follows from the renewal recurrence and an algebraically checked rational partial-fraction decomposition; the four-phase limits follow from its explicit coefficients. A finite-threshold first-crossing convolution gives complete rational overshoot generating functions, and dominated convergence plus an exact tail sum prove the limiting probability law, including normalization. Hypotheses, denominator cancellations, endpoint conventions and distinction between geometric scale and physical return time have been checked. The standalone exact-arithmetic reproduction reports `VERIFY_OK` on 85 positive levels, 84 paired-digit weights, 25 crossing thresholds and the limiting mass; finite checks supplement, not replace, the infinite proof.

## Originality — PASS, with residual historical uncertainty

Lowenstein–Vivaldi (arXiv:1406.6910, original public version 2014-06-26) already proves the planar rhombus model, the induced five-atom base triangle, its full-branch Lüroth coding and the geometric multiplier. No originality is claimed for those definitions or its renormalizability theorem. Its Sections 4–5 and 11 were read for possible coverage; these do not state the uniform-parameter exact level-hit distribution, four-phase finite-scale correction, or complete overshoot generating functions.

Kesseböhmer–Munday–Stratmann (arXiv:1006.5693, full Section 3) already states a general renewal recurrence and the reciprocal-mean renewal limit for Lüroth sum-level sets. Its generic generating-function identity \(U=1/(1-W)\), once the special increment law is separately supplied, is a clear antecedent to the present calculation; the renewal limit \(1/4\) is not presented as new in isolation. The evaluated rational factorization with nontrivial complex root phases and the exact first-crossing law for the specific geometric PWI hierarchy were not found stated in these sources.

The main residual risk is that the exact finite-scale evaluation might have been derived elsewhere or considered a close explicit corollary of general discrete-renewal theory; absolute priority is not certified. The narrower specific evaluated formula, not an invented new renewal principle, is the claim reviewed here.

## Mathematical value — PASS

In a planar model whose renormalizations can require arbitrarily complex induction itineraries, exact geometric scales form a natural discrete hierarchy. The probability of ever attaining a prescribed fine scale and the amount by which the first crossing skips that scale are intrinsic, interpretable parameter-ensemble invariants. The result gives all-level probabilities rather than only an asymptotic recurrence or generic mean. The four-phase leading correction distinguishes adjacent geometric levels by a stable arithmetic pattern; the exact rational first-crossing functions classify the distribution at every threshold, while the limiting overshoot quantifies unavoidable lattice-scale skipping. These statistics address questions about parameter-space geometry not answered by existence of renormalization, temporal incidence matrices, or general renewal limits.

Scientific limitations remain: only the canonical base-triangle hierarchy, normalized uniform parameter measure, and scale (not actual return times or planar invariant-measure averages) are covered. The finding is not claimed to establish a perturbation theorem, an exceptional-set dimension, or historical independence of all prior literature.

Self-review: passed. Independent audit: not yet performed.
