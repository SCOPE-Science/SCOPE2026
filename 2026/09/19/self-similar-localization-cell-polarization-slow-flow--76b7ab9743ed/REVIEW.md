# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The argument begins with the exact representation formula and monotonicity of the multiplier proved in arXiv:2609.20609v1. After normalizing the signal deficit by `H=(g_max-g)/g_max`, the source equation reduces exactly to

\[
u=[u_0+\Phi-(t+\Phi)H]_+,
\qquad \Phi(t)=\int_0^t g_{\max}(\alpha-\alpha_*)\,ds.
\]

Defining `sigma=Phi/(t+Phi)` therefore introduces no approximation. The two positivity-set inclusions in the record follow directly from boundedness and nonnegativity of `u_0`. They squeeze the conserved mass between `(t+Phi)G(sigma)` and that same quantity plus a term bounded by the measure of a shrinking signal sublevel set. Since the source proves `alpha(t) -> alpha_*`, one has `Phi=o(t)`, and finite isolated maxima make the residual sublevel measure vanish. This proves the central identity `t G(sigma) -> 1` without differentiating an asymptotic formula.

For `G(s) ~ C s^q`, ordinary asymptotic inversion yields the threshold and integrated-multiplier powers. The pointwise multiplier rate is justified by monotonicity: forward and backward difference quotients squeeze the monotone function `phi=Phi'` and give the regular-variation derivative constant `1-1/q`. For homogeneous maxima, the source already establishes `G(s) ~ C s^(1+2/m)`. The local similarity profile then follows from dividing the exact representation by `Phi` and using `ell^m=sigma`. The support-area coefficient is checked by the exact homogeneous identity `int(1-v)_+ = [m/(m+2)] |{v<1}|` in two dimensions. The Morse constants follow from a linear change of variables in the quadratic form.

The compact verification artifact checks all exponent and coefficient identities symbolically. It is supporting reproducibility evidence, not independent validation.

## Originality

**PASS, to the best of our knowledge, with a narrow source-specific claim.** The representation formula, monotonicity of `alpha`, concentration on signal maxima, the limiting-measure characterization, the small-threshold expansion of `G`, and the weights of asymptotically homogeneous maxima are prior results in arXiv:2609.20609v1 and are explicitly excluded from the novelty claim.

The source was inspected at the theorem and proof level in Sections 3.1 and 4. It states qualitative convergence `alpha(t) downarrow alpha_*`, subsequential limit-measure formulas, and the static small-threshold law for `G`; it does not state the full-time clock `t G(sigma(t)) -> 1`, the resulting explicit time decay/growth rates, or the local dynamic similarity profile. Searches within the full text found no source statement of a localization rate or a `t^(-1/4)` dynamic width.

The closely related stationary paper arXiv:2605.03553v1 was inspected. It analyzes the stationary small-mass obstacle problem and obtains different blow-up scales (including the Morse width `mass^(1/6)`), not the large-time zero-diffusion slow flow studied here. The 2023 qualitative paper on the model focuses on support continuity and jumps, and arXiv:2402.03034v1 focuses on interface continuity and small-time oscillations under axisymmetry. None of these inspected sources supplies the localization clock or the dynamic exponents in this record.

External searches used the exact source identifier and title together with `self-similar`, `large-time`, `localization rate`, `free boundary`, `cell polarization`, and `t^{-1/4}`, as well as searches for the earlier papers in the same model family. No public source-specific correction, comment, or earlier equivalent theorem was located. Repository searches by source identifier and claim terminology found no prior SCOPE record covering the result.

Residual originality risk remains because the key proof combines two ingredients already present in the source—the exact positive-part representation and the small-threshold asymptotics of `G`—and general regular-variation inversion is standard. An unindexed note could therefore contain the same sharpening. No inaccessible paper was identified as a particularly close source-specific candidate likely to overturn the claim.

## Value

**PASS.** The source characterizes where mass ultimately concentrates but leaves the physical localization clock implicit. The new identity converts signal sublevel geometry directly into time: it determines the multiplier gap, peak height, support area, spatial width, and a full local similarity profile. The generic Morse case gives explicit, experimentally interpretable exponents and Hessian-dependent constants. The result also cleanly separates the dynamic slow-flow scale from the distinct stationary small-mass scale studied in arXiv:2605.03553.

## Limitations

The result is restricted to the `D=infinity` zero-membrane-diffusion slow-time limit system of Section 3.1 in arXiv:2609.20609v1. It does not establish the same rates for the original parabolic problem, for finite cytosolic diffusion, or for time-dependent signals. Explicit power laws require isolated maxima with regular homogeneous asymptotics; oscillatory threshold geometries from the source fall outside that corollary. No quantitative rate of convergence to the local similarity profile is claimed. The originality assessment is not independent validation.
