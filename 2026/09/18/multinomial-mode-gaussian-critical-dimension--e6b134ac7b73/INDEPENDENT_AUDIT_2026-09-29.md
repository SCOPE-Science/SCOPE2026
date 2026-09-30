# Independent Audit — 2026/09/18/multinomial-mode-gaussian-critical-dimension--e6b134ac7b73

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d7dd70aada69655d0ee9f60396aec40ad90b2155`
- Disposition: **PASSED**

## Correctness

**PASS** — The growing-dimension Stirling calculation is correct. Modal offsets lie in [-1,1], so the shifted-Gamma expansion is uniform in the lattice phase while N/m tends to infinity. Summing the denominator remainders gives O_K(m^(K+2)/N^(K+1)). At k=1, A_2(theta)=1/6+theta(1-theta), and its phase-dependent term cancels exactly with the Gaussian Mahalanobis exponent, leaving -(m^2-1)/(12N). Every subsequent term is smaller by a factor O(m/N), establishing the e^(-c/12) critical profile and the iff m=o(sqrt(N)) relative-accuracy criterion. The K-term correction scale follows by balancing m^(K+2)/N^(K+1). For the unit-cell correction, Sigma_m^{-1}=m(I+11^T) gives a vanishing linear term and a quadratic limit c(1+Z^2)/24, whose Laplace transform is e^(-c/24)(1+c/12)^(-1/2). Direct exact log-factorial evaluations at several large (N,m) pairs match the leading critical exponent to numerical precision.

## Originality

**PASS** — Elezović's expansion is formulated for a fixed multinomial probability vector, and Ouimet's precise local limit theorem likewise treats finite dimension with constants depending on the dimension/probability data. The audited result instead lets the equiprobable category count grow and extracts exact phase-uniform dimension transition laws, an all-orders correction hierarchy, and a critical unit-cell profile. Classical central-multinomial Stirling expansions contain the divisible-N first correction, but they do not by themselves supply the arbitrary lattice-phase hierarchy and Gaussian-cell limit stated here. Targeted searches found no pre-record theorem with these critical profiles.

## Scientific value

**PASS** — The theorem identifies the exact square-root dimension threshold where a standard Gaussian local approximation ceases to be relatively accurate, quantifies the missing factor, and shows how successive explicit corrections push the allowable dimension toward N. The continuity-correction calculation is particularly useful because it shows that the usual unit cube cancels the first small-c distortion but still has a nontrivial critical error. These are informative finite-dimensional transition laws rather than merely another fixed-d expansion.

## Sources

- Multinomial probabilities near the mode: integer modes and the complete local expansion (Neven Elezović): https://arxiv.org/abs/2609.20229 — Fixed-probability-vector complete local expansion and exact multinomial mode characterization.
- A precise local limit theorem for the multinomial distribution and some applications (Frédéric Ouimet): https://arxiv.org/abs/2001.08512 — Prior precise multinomial local limit theorem in fixed dimension; discusses normal comparison and finely tuned continuity corrections.

## Limitations

- Only the equiprobable multinomial and modal lattice points are covered.
- The regime requires m=o(N), excluding sparse occupancy with bounded expected counts.
- No global total-variation, Le Cam, or convex-set approximation threshold is claimed.
- The standard unit cube is analyzed; optimized lattice cells could have different critical behavior.

## Independent exact check

```json
{
  "implementation": "direct lgamma evaluation of exact modal mass versus Gaussian density",
  "cases": [
    {
      "N": 1000000,
      "m": 1000,
      "log_ratio": -0.0833332471202084,
      "leading": -0.08333325
    },
    {
      "N": 1000000,
      "m": 2000,
      "log_ratio": -0.3333332060201428,
      "leading": -0.33333325
    },
    {
      "N": 2000000,
      "m": 1000,
      "log_ratio": -0.04166662534044008,
      "leading": -0.041666625
    },
    {
      "N": 10000000,
      "m": 2000,
      "log_ratio": -0.0333333265298279,
      "leading": -0.033333325
    }
  ],
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; no needed source remained inaccessible, so Oxford Download was not required.
