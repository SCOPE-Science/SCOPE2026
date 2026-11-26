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

D and Phi count two separate classes of nonempty subsets of [n], as made explicit by the proof and verifier; Phi is not conditioned on membership in D. Each deficit includes the empty subset. All multiples-of-r subsets fail the D condition because r does not divide n, and every failing gcd is at least r. For Phi the corresponding assertions follow from p being the least prime divisor of n. Counting subsets supported on multiples and taking a union bound traps each deficit between 2^floor(n/d) and (n+1) times that lower bound, with d=r or p. This also works at n=2 with r=3 and an empty upper-bound sum. Taking logarithms and accounting for both floors gives the asserted (looser) uniform error; r≥3,p=2 on even n and r=2,p≥3 on odd n give both inequalities for the unscaled ratio. The fibers r=k are the difference of the multiples of L_(k−1) and L_k; a new LCM valuation occurs exactly at a prime power. The least-prime fibers follow from finite inclusion–exclusion. The even tail is bounded by 1/L_K and the tail avoiding all primes through Q by the finite Euler product, which tends to zero by comparison of its reciprocal with the harmonic sum. This justifies taking the infinite limit for bounded continuous h, using uniform continuity on the eventual compact range. Each parity contributes total mass 1/2.

## originality

PASS

The supported distinct claim is the full prime-power/least-prime atomic law for the logarithmic ratio, with quantified localization yielding parity escape. The strongest Resultary comparison substantially overlaps the growth and parity statements but is dated later and gives no limiting distribution. The original question and the checked neighboring results do not provide this classification. In particular a parity sign alone has no control over logarithmic size or empirical atom frequencies.

## value

PASS

The ratio was explicitly posed in the original subset-counting literature, and the result goes beyond sign and unscaled extrema. The logarithmic scale retains the relative exponential rates even when the raw ratio escapes by parity. The full atomic law explains which arithmetic obstructions dominate and assigns their exact frequencies, useful information not supplied by counts or parity alone. The result does not claim the separate summatory questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
