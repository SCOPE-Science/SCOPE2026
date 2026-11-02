# Scientific review: fractional BDF3 coefficient signs

## Correctness

**PASS.** The theorem specifies the analytic power-series branch, order range, positive timestep scaling and all integer indices. Differentiating the cubic symbol gives the three-term coefficient recurrence. The first three signs are explicit, with a strictly positive quadratic for the third. For indices 4–21, 18 exact rational Bernstein coefficient checks prove strict positivity of the rescaled negative weights; four further checks initialize a rigorous invariant interval for adjacent ratios. The interval is preserved for all indices 22 onward by the explicit corner inequalities displayed in the proof. Independent generalized-binomial coefficient comparisons check the algebraic implementation. Finite exact computation is not being substituted for the infinite induction.

## Originality

**PASS on inspected evidence, with residual risk.** Lubich (1986) provides the third-order fractional multistep generator; Jin–Li–Zhou (2017) provide higher-order derivative quadrature and correction analysis; Karaa (2024) establishes positivity of convolution quadratic forms, not pointwise BDF3 derivative coefficient signs. Examination of their relevant generating-function definitions, proofs and reported results did not locate the all-index BDF3 coefficient sign frontier at \(\alpha=7/18\). The contribution is narrower than the pre-existing full scheme and is not simply the second-order coefficient threshold. A specialist article containing an equivalent inequality but not surfaced by the searches remains possible.

## Mathematical value

**PASS.** A sharp necessary-and-sufficient nonpositive-history-weight condition is a naturally motivated kernel invariant for sign-based stability or monotonicity arguments in fractional stepping. The order-dependent exception and its exact boundary can affect whether coefficientwise monotonicity tools are available. The result is an exact classification for a standard third-order convolution symbol, not an arbitrary finite slice or unsupported numerical observation. It does not independently certify positivity of numerical solutions.

## Closest literature and limitations

The generator comes from C. Lubich, *Discretized Fractional Calculus*, DOI 10.1137/0517050. Higher-order derivative and correction schemes are treated by B. Jin, B. Li and Z. Zhou, DOI 10.1137/17M1118816. S. Karaa, DOI 10.5802/crmath.669, establishes a different quadratic-form notion of convolution positivity and explicitly treats BDF2 weights. Only the uncorrected derivative coefficients and \(0<\alpha<1\) are within scope. Independent validation and a specialist exhaustive novelty review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
