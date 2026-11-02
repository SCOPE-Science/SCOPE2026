# Self-review

**Correctness — PASS.** The exact joint mixed moment is reconstructed by marking an \(r\)-cycle and deleting it. Differentiating the weighted derangement insertion recurrence gives a contraction recurrence for consecutive mean-cycle increments, proving the sign order and boundary inequalities at every finite size. Analytic asymptotics of the singular generating function prove the parameter-dependent critical fraction and the full signed macroscopic covariance limit. The standalone Python checker passed 5,658 exact assertions and 51,024 weighted derangement enumerations; finite enumeration is not the infinite proof.

**Originality — PASS, with historical-priority risk.** The exact factorial moments and expected total cycle counts in da Silva, Jamshidpey and Tavaré (arXiv:2006.04840, Sections 2.1–2.3) already imply individual covariance values; these known input formulas are not claimed as original. The proposed contribution is their complete simultaneous sign ordering, unique weak transition, explicit \(\theta\)-dependent macroscopic crossover, and signed profile. Relevant full-text sections in arXiv:2211.13831 and arXiv:2104.12019 were also examined, and actual research-record queries did not find a covering sign theorem. An implicit earlier derivation is still possible.

**Value — PASS.** The sharp transition separates cycle-length classes that increase versus decrease with the global component count, uniformly across Ewens parameters. Its nontrivial scale \(1-e^{-1/\theta}\) and quantitative signed profile provide a meaningful dependence characterization of a well-studied combinatorial probability model.

**Limits and risks.** Length \(n-1\) is impossible, exact zero covariance at an interior boundary is not excluded, \(n=2,3\) are degenerate, and the asymptotic regime fixes \(\theta\) and a positive cycle fraction. Covariance is not independence. Prior full factorial-moment formulas are stronger at raw data level, so novelty is confined to the sign and phase structure and remains subject to independent priority review.

Self-review: passed. Independent audit: not yet performed.
