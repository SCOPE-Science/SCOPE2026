---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For an atom 2k/3, the sole integer at distance strictly less than 2/3 is the nearest integer; if W_infty were strictly below 2/3 there would be a coupling below that radius and its target law would be the nearest-rounded law. Its indices 1,2,3 have preimages {1,2}, {3}, {4,5}. With N=3n, the unnormalized masses are N(N+1)/2, N(N-1)(N-2)/6, and N(N-1)(N-2)(N-3)(N+1)/120. Their defect a_1 a_3-a_2^2 is N^2(N-1)(N-2)/720 times [3(N-3)(N+1)^2-20(N-1)(N-2)]. On substituting N=3n the bracket is 81(n-2)^3+279(n-2)^2+279(n-2)+41, strictly positive for n>=2. By Newton's inequalities every Poisson-binomial law is log-concave, also with deterministic Bernoulli summands (which shift or leave unchanged the nontrivial sequence). Independently overlaid the two cumulative quantile distributions at n=2 using 64 equal mass units, obtaining the displayed table and maximum displacement 2/3. At n=1 the rounded PGF is (1+6z+z^2)/8, with Bernoulli probabilities (1+1/sqrt(2))/2 and (1-1/sqrt(2))/2, and a positive atom at 2/3 already requires distance at least 1/3. This proves a sharp uniform lower bound, not the exact distance at all n>=2. The shipped checker was inspected; the infinite argument is symbolic.

## originality

PASS

The six-trial and three-trial optima are known, not credited as new. The distinct supported claim is the all-size, nearest-rounding obstruction, yielding a positive uniform lower bound on this subsequence. The closest inspected general approximations and floor obstructions do not imply it. The published supplement remains an identified bibliographic risk.

## value

PASS

The target family comes from an established transport question. The bound excludes a whole band of better radii uniformly in trial count for the specified scaling and subsequence. The forced-law idea and one fixed mass index give a transparent obstruction without classifying all Poisson-binomial approximants. The known six-trial attainment certifies the optimal uniform constant, while neither that case nor the elementary geometric floor alone supplies the all-size result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
