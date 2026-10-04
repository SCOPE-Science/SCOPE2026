# Review of “A square-root step-size bias in the balanced implicit SIS invasion threshold”

## Correctness
PASS. The source equations give the exact disease-free linear SDE and the BIM weight. For \\(F_1\\equiv0\\) and \\(F_2(S,I)=\\sigma S/K\\), condition (45) is satisfied because \\(F_2/S=\\sigma/K\\). The BIM linearization is scalar with a positive iid multiplier, so its almost-sure exponent is the expected log multiplier divided by \\(h\\). The half-normal moments and Taylor coefficients were reconstructed independently, with an integrable fourth-derivative domination for the remainder. The sign and threshold expansion follow from strict monotonicity in \\(a\\).

## Originality
PASS. Exact-title, DOI, formula-alias, finite-step Lyapunov-threshold, and dynamics-preserving searches were compared by statement and implication. The 2026 motivating paper proves arbitrary-step invariance and fixed-finite-time mean-square convergence but does not derive this finite-step transverse exponent or its \\(O(\\sqrt h)\\) threshold displacement. The 2019 same-model paper uses the same BIM but leaves quantitative long-time numerical analysis to earlier numerical-method work and does not state this source-specific threshold expansion. Dedicated dynamics-preserving SIS schemes prove threshold behavior for different algorithms rather than implying the present BIM calculation.

## Value
PASS. Disease-free invasion/extinction thresholds are a central long-time qualitative property of epidemic discretizations, and the source explicitly frames its BIM analysis in terms of dynamic consistency. The square-root threshold shift identifies a structural effect of the absolute-value balancing term inside an admissible convergence-class specialization. It cleanly separates fixed-time convergence from exact finite-step preservation of a long-time local threshold and gives the leading correction needed to quantify that distinction.

## Closest literature and limitations
The closest source is the 2026 Schurz–Tosun BIM analysis itself; the 2019 Schurz–Tosun paper supplies the same SIS family and BIM form; Liu–Wang–Dai (2024, arXiv:2308.05287) is the closest retrieved comparison explicitly preserving SIS extinction and persistence for any step size, but it uses a different scheme. The claim is local, linear, specialized, and asymptotic in \\(h\\); it does not address global nonlinear stability.

Same-model review: passed. Independent audit: not yet performed.
