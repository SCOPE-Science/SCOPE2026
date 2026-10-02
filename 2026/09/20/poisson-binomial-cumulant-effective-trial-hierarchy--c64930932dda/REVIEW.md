# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS**. Variance-weighting converts the third cumulant to a weighted mean and gives the third-moment effective count. Weighted variance proves the comparison with the fourth-cumulant participation count, and Cauchy–Schwarz bounds that count by the number of active Bernoulli variables with the stated equality cases. Convex packing of Bernoulli variances gives the sharp fourth-cumulant endpoint, and the Lyapunov identity is termwise. The exact-rational verifier checks 66,429 grid vectors as corroboration.
- Originality: **PASS**. Peköz et al. already define the third-moment-matched real binomial trial count that equals the present third-cumulant count, but the inspected sources do not give the fourth-cumulant participation count, the chain between the two counts and active trial number, the equality classification, or the sharp fixed-variance envelopes.
- Scientific value: **PASS**. The theorem ties a pre-existing third-moment effective trial count to a fourth-cumulant participation count and the active trial number, with exact equality cases and sharp low-moment envelopes. This is a natural reusable structural diagnostic for Poisson-binomial laws.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`. Earlier same-model evidence is preserved in `AUDIT.json` and is not relabeled as independent evidence.
