# Scientific review

**Correctness (PASS).** The proof reduces the published nonlinear randomized row update exactly to a sign-reset recursion, derives its almost-sure logarithmic rate using iid sign transitions, proves the critical oscillation via iid geometric return cycles, and computes its full moment spectrum with a positive two-state matrix. The positive-moment frontier follows from Perron–Frobenius theory and convexity. The executable checks confirm the finite algebra but are not mistaken for infinite-time proof.

**Originality (PASS, with risk).** The source paper gives the general GAVE algorithm and sufficient convergence bounds, while the present theorem determines sharp sampling bias thresholds, boundary oscillation, a complete moment spectrum and a non-uniformly-integrable fair-sampling martingale on an explicit GAVE specialization. Comparisons against source Sections 4 and 5.3, related linear Kaczmarz literature, accessible earlier mathematical findings and targeted indexed searches did not identify a covering statement. Classical random-product machinery is expressly prior art; an equivalent instance in specialized Markov-additive or absolute-value-equation literature remains possible.

**Value (PASS).** This supplies an exact, structurally motivated warning that adjusting sampling probabilities can flip an almost-surely convergent nonlinear randomized solver into almost-sure divergence, and that even fair sampling does not control expected first or second absolute error. The square-root small-step sampling-tolerance scale and the sharp critical fluctuations make the phenomenon quantitative, beyond a routine fixed-parameter example.

**Limitations.** The theorem applies to a two-row, one-unknown, exactly solved GAVE under independent sampling, not to general nonsquare nonlinear systems. The general source convergence guarantees are sufficient, and no claim of contradiction is made. Originality is assessed only against actually inspected evidence and not independently certified.

Self-review: passed. Independent audit: not yet performed.
