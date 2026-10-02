# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS**. At stationarity the containing renewal interval is size-biased and the inspection location is uniform, so the age and residual pair is a uniform split of that interval. The first, second and mixed powered moments follow directly. The resulting correlation depends on the interarrival law only through one positive moment ratio, which lies in the interval from zero to one by Cauchy–Schwarz, with equality at one exactly for deterministic interarrivals. The correlation is strictly decreasing in this ratio. A two-point size-biased interval law realizes every interior ratio and can approach zero, and inverse size-biasing returns a valid positive two-point interarrival law. This proves the endpoint and attainability claims as well as the exponential zero-correlation benchmark.
- Originality: **PASS**. The stationary Schur-constant representation and the ordinary first-power correlation are prior theory, but the inspected sources did not state the all-positive-power exact correlation envelope, endpoint/extremizer classification, two-point attainability result, or high-power collapse.
- Scientific value: **PASS**. The theorem gives a complete distribution-free identification region for a natural dependence statistic across every positive power, with exact extremizers, attainability, a sign threshold and a high-power limit. This is a motivated complete classification rather than a raw moment computation.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`. Earlier review evidence is preserved in `AUDIT.json` without being relabeled as fresh independent evidence.
