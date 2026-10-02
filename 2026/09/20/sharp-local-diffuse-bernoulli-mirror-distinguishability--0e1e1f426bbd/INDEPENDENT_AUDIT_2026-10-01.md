# Independent scientific audit — SCOPE-20260920-0e1e1f426bbd

Audited at: 2026-10-01T21:06:11.107600Z

Disposition: **repaired**

## Correctness — PASS

For the repaired claim, let \(S_n=\sum_i\operatorname{atanh}(a_{n,i})\varepsilon_i\) under the positive mirror law. Its mean is \(v+o(1)\), variance is \(v+o(1)\), and the largest centered summand tends to zero when \(\max_i a_{n,i}\to0\), so Lindeberg gives \(S_n\Rightarrow N(v,v)\). The likelihood-ratio sign identity then gives \(\tau_n\to2\Phi(\sqrt v)-1\). Also \(\log\prod_i(1-a_{n,i}^2)\to-v\), so \(\Delta_n\to\sqrt{1-e^{-v}}\). For \(t=\sqrt v\), differentiating \(I(t)/\sqrt{1-e^{-t^2}}\) reduces strict monotonicity to \(2\sinh(t^2/2)>tI(t)\), which follows from \(2\sinh(t^2/2)>t^2\) and \(I(t)<t\).

### Correctness sources

- repaired RESULT.md proof
- assigned artifacts/verify_mirror_tv.py
- published 2026-09-19 weak-signal mirror record
- Smirnov arXiv:2609.19222 abstract

### Correctness risks

- The artifact numerically illustrates homogeneous convergence but is not the proof.
- The primary Smirnov full text was not available through the current access route; its abstract and the earlier published comparison were inspected.

## Originality — PASS

The original record overclaimed local weak-signal results already published on 2026-09-19. The repaired claim removes those covered statements and retains only the fixed-positive-signal diffuse limit and its strictly increasing efficiency curve. Resultary searches for that curve returned the repaired record and the earlier weak-signal record; the earlier theorem assumes total squared signal tending to zero and does not contain the fixed \(v\in(0,\infty)\) curve. The accessible Smirnov primary abstract states constant-factor Bernoulli-product bounds but not this asymptotic profile.

### Equivalent formulations

The repaired theorem is not equivalent to the local result because \(v\) remains bounded away from zero.

### Broader coverage

Those ingredients motivate but do not already state the exact finite-signal mirror efficiency curve and its global monotonic interpolation.

### Exact database or table

Absence is supporting evidence only; the decisive comparison is with the earlier same-object weak-signal theorem.

### Claim versus prior implication

Although the proof uses standard CLT/LAN tools, the source-specific closed profile and strict monotonicity are additional statements rather than a restatement of the local theorem.

### Sources inspected

- Sharp weak-signal profiles for mirror Bernoulli products — published record 2026/09/19/sharp-weak-signal-mirror-bernoulli-profiles--80bd8eba23bd. PARTIAL_COVERAGE: It covers the original record's Theorems 1-2, which are removed by repair, but not the fixed-positive-signal curve.
- TV between Bernoulli products, up to constants — https://arxiv.org/abs/2609.19222. INACCESSIBLE_PLAUSIBLE_SOURCE: The accessible statement gives constant-factor upper/lower bounds, not the repaired finite-signal curve; full-text noncoverage is not asserted.

### Checked sources

- published SCOPE 2026/09/19/sharp-weak-signal-mirror-bernoulli-profiles--80bd8eba23bd
- https://arxiv.org/abs/2609.19222
- https://arxiv.org/abs/2602.21828
- Resultary semantic search

### Residual risks

- The unavailable full text of Smirnov's very recent preprint could contain a related asymptotic not visible in the abstract.
- Older binary-experiment/LAN literature could contain an equivalent formula in different notation; no source-specific mirror formulation was located.

## Value — PASS

After removing the covered local theorem, the fixed-positive-signal curve remains a natural quantitative invariant of the mirror experiment: it gives the complete diffuse efficiency interpolation from \(\sqrt{2/\pi}\) to one and proves the interpolation is strictly monotone. This directly sharpens interpretation of a motivated recent comparison, rather than selecting an arbitrary parameter slice.

### Value sources

- published 2026-09-19 weak-signal mirror theorem
- Smirnov arXiv:2609.19222

### Value risks

- The derivation uses standard LAN machinery, so its value is the exact source-specific profile rather than a new central-limit theorem.

## Limitations

- The repaired theorem requires \(\max_i a_{n,i}\to0\) and \(\sum_i a_{n,i}^2\to v\in(0,\infty)\).
- It does not re-claim the already-published weak-signal interval or diffuse local constant.
- No quantitative convergence rate is proved.
- The globally optimal all-signal comparison constant is not determined.
