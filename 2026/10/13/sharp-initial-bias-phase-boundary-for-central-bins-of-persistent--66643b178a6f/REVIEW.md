# Scientific review: biased-start central-bin phase boundary

## Correctness — PASS
The run-composition formula (4) separates odd and even switch counts under a nonstationary initial law. Three factorial/binomial identities yield the exact adjacent-bin difference (1), independently checked against exact-rational Markov recurrences. For \(0<u<1\), symmetric unimodality of the convolution kernel, strengthened by the displayed strict first-difference induction, gives \(C_1>C_2\). The aperiodic lattice local limit theorem for differences of two binomial variables gives \(C_2/C_1\to1\), proving both the strict finite-length inequality at the limiting threshold and necessity from eventual sign reversal. The checker passed 680 rational comparisons; the argument, not the checks, proves the continuum of \(p,\alpha\) and unbounded even lengths.

## Originality — PASS, with residual priority risk
The closest recent full text, Pemmasani (arXiv:2610.06935v1), assumes a fair initial direction and analyzes crossings of the middle bin with the endpoint bins. Its recurrence and run enumeration do not state or imply the nonstationary-start threshold without new coefficient comparisons. Dekking–Kong (arXiv:1102.3613v1) handles arbitrary starts and proves interior log-concavity plus a coarse one-/two-/three-mode classification; neither states the sharp all-even-length boundary \(\alpha+p=3/2\) nor the nontrivial finite-size reversal. A full-text version of Renshaw–Henderson (1981) could not be obtained; its available abstract concerns transition probabilities and limits rather than an all-length modal comparison, but equivalent priority remains possible. Database searches and current claims comparison revealed no asserted dominating result. This is not a claim of exhaustive novelty or independent priority certification.

## Value — PASS
The initial law creates a persistent but size-dependent shift in the central occupation profile. A sharp, parameter-only criterion simultaneously decides a strict probability comparison at **all even sample sizes**, and a nonempty explicit region forces the inequality to reverse between a short and a long walk. This is a structural finite-versus-asymptotic modal boundary, not an arbitrary isolated computation or mere restatement of a known Markov-binomial formula. It is particularly relevant when extrapolating finite correlated-walk modes from long-time approximations.

## Scientific limits and closest literature
This compares only two adjacent central bins; endpoint peaks and other global modes are not classified. The transition kernel must be symmetric and persistent, and no uniform convergence rate is asserted near \(p=1\). Relevant primary sources: Pemmasani (2026), Dekking–Kong (2011), Renshaw–Henderson (1981; full-text unavailable). Exact-rational checks do not establish the infinite theorem by themselves.

Self-review: passed. Independent audit: not yet performed.
