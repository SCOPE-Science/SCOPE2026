# Scientific review of the common-favorite distributional reduction

## Correctness — PASS

The precise model fixes a common first school for any \(r\) of \(n\) students, independently uniform tails, independently uniform whole rankings of other students, and RSD with unit school capacities. The proof constructs every student's ranking from independent raw labels, proves the exact equivalence between an unenvied allocation and a raw-draw singleton, and handles separately the symmetry argument for \(r=1\) and deletion of repeated common-school draws for \(r\ge2\). The critical nonstandard step is that the adaptively interleaved non-common raw draws remain independent uniforms over the remaining schools and terminate exactly at their last first appearance; this follows from the conditional distribution of each next fresh draw and from allocation of the common school before the final choice. The cited Myers–Wilf result supplies the known singleton pmf and harmonic mean. Replayed exact-rational enumeration confirms all \(810,521\) market/designation cases at sizes \(2,3,4\). Finite checks are corroboration; the proof is uniform in \(n\) and \(r\).

## Originality — PASS, subject to unindexed-literature risk

The full open-access manuscript by Ortega et al., *The Distribution of Envy in Matching Markets*, https://arxiv.org/html/2603.23385v1 , Sections 2–4, assumes independent uniform rankings and gives the expectation \(H_n\) for RSD (Proposition 3), but does not imply a law in which two or more agents have a forced shared favorite. It explicitly identifies correlated preferences as a question. Myers and Wilf, https://arxiv.org/html/math/0304229v1 , Section 4, give the coupon distribution but do not supply the nontrivial correlated-market reduction. Wang, https://arxiv.org/html/2603.24526v1 , uses Mallows-correlated preferences for stable matchings rather than this RSD statistic. Related stochastic-dominance and fixed-profile matching results concern different quantifiers, outcome measures or preference laws. The sharp equality for every \(r\ge2\) is not a consequence of the prior iid expectation or coupon integral without the deletion coupling. Search completeness cannot certify mathematical priority; independent literature validation remains desirable.

## Value — PASS

This supplies a complete exact distribution, not just another harmonic expectation, for a natural non-iid demand bottleneck in school choice. It identifies the precise structural change when a second applicant shares a favorite school and shows the surprising invariance of the entire law as further applicants join that group. All market sizes are covered by one coupling and inherit explicit coupon probability tables, enabling exact predictions of ex-post envy concentration without repeated combinatorial enumeration. This directly addresses the correlated-preferences gap raised by the motivating paper, while remaining carefully scoped to one common-favorite group.

## Boundaries and residual risks

The result does not cover general Mallows correlations, multiple popular schools, school priorities, or deferred acceptance in the modified model. The coupon pmf and harmonic identity are credited, not proposed as original. The most plausible novelty risk is an earlier unindexed distributional coupling for a common forced favorite; the available primary sources and overlapping-metric searches did not establish such coverage. The finite verifier only tests sizes up to four. The universal claim instead rests on the complete analytical coupling.

Self-review: passed. Independent audit: not yet performed.
