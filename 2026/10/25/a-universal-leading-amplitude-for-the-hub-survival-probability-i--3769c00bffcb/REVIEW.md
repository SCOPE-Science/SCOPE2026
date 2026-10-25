# Self-review

## Correctness — PASS
The random-arrival process is uniquely defined, and all rates are positive. Parity forces central occupancy on odd rims. First-edge conditioning for the even rim, and then for the resulting path, rigorously yields the recurrence with denominator \(2(1+\lambda)m-1\). A coefficient comparison derives the stated Riccati equation; substitution gives the specified entire hypergeometric denominator. Its strictly negative nonconstant Taylor coefficients imply a unique simple positive dominant zero, and singularity analysis gives the amplitude \(2\) and an exponentially smaller remainder. Strict decay-rate monotonicity follows coefficientwise. The packaged independent full-state exact-rational calculation matched the analytic recursion for all sampled instances, and coefficient checks matched the hypergeometric representation. Finite tests do not prove the infinite theorem.

## Originality — PASS relative to the inspected sources, with residual uncertainty
Krapivsky's Section IV-B of arXiv:2009.08609 supplies the full perfect-packing generating function and leading pole residue for a homogeneous open path with no competing spoke traps (the present \(a=1\) boundary recursion). The positive-spoke-rate wheel survival law is not covered by that claim: its event, recurrence denominators, and hypergeometric parameter vary with \(\lambda>0\). The full arXiv:1210.8098 text addresses interacting adsorbed dimers on surfaces, not a finite-wheel hub survival event. Pippenger's 1989 paper and Dyer–Frieze's 1991 paper were consulted through available abstracts/catalog metadata; the former is a meaningful residual risk because a sufficiently general graph-adsorption theorem might subsume this result, even though no equivalent evaluated wheel formula was identified. Research-record searches of the title, aliases, mathematical recurrence, and hub-survival observable did not identify a matching claim. No global priority is asserted.

## Mathematical value — PASS
The central vacancy event is a natural physically defined local rare event on a heterogeneous substrate. The proof determines its complete finite-size rate dependence and extracts a non-obvious amplitude that is independent of the rate contrast, while the exponential decay rate depends strictly on it. The exact weighted-path Riccati/hypergeometric mechanism gives a structural explanation and a quantitative asymptotic law, beyond renaming a homogeneous recurrence.

## Limitations and risks
Only the final central-vacancy event on a finite wheel is classified; correlated site observables and arbitrary graphs are outside scope. Independent scientific audit and exhaustive priority verification are outstanding. The 1989 full text was inaccessible, and a stronger older generalized weighted RSA theorem may exist. The 2020 one-dimensional unweighted result must not be represented as original to this finding.

Self-review: passed. Independent audit: not yet performed.
