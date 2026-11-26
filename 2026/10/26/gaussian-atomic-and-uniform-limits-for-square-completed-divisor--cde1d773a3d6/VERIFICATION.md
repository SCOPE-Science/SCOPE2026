---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On a full block the sampling weight is (2m−1)/T², and conditional on m the shift is the uniform grid of mesh 1/(2m−1). The weighted bounded-Lipschitz grid error is O(1/T) even after multiplication by bounded statistics of m. Divisor factorization gives log D(m²)=log(3/2)ω(m)+H(m). Fixed bounded valuation patterns are congruence conditions; CRT gives their weighted geometric probabilities. For Erdős–Kac in a fixed class, truncate at T^(1/log log T) excluding primes dividing the modulus: CRT gives each fixed joint moment the independent-prime main term with total error T^(−1+o(1)), and the omitted primes have conditional mean O_q(1+log log log T) by Mertens and summing the counting errors. For each fixed lower-scale endpoint tT, the same normalized Gaussian law holds since replacing log log T by log log(tT) is negligible; partial summation gives it under the root weight. Thus the normalized ω is asymptotically independent of each finite valuation vector, not just marginally Gaussian. The weighted expectation of the discarded correction above B is bounded by 2 sum_(p>B)1/[p(p−1)]. This makes the correction tight, permits the finite-prime product limit and Slutsky replacement, and implies almost-sure finite support in primes in the model. The remaining incomplete block has O(1/T) mass. The zero and smallest positive atoms follow respectively from all valuations ≤1 and exactly one valuation equal to 2. A fresh rational enclosure (/workspace/branches/7b2beb61-f14c-4930-ace9-73fec79f60fd/atom_certificate.py) bounds the latter probability between 0.2007556808 and 0.2007562888, sufficient for the displayed rounding; it is a numerical check, not the limiting-law proof. The uploaded checker was inspected, not executed.

## originality

PASS

The supported distinct claim is the mutually independent Gaussian bulk, discrete prime-power correction and uniform within-block phase for this sampling, with explicit atoms of the correction. The weighted Gaussian marginal and additive correction framework overlap with known general theorems. The closest matching-statistic records compute summatory means; these neither imply weak joint convergence nor condition the Gaussian law on prime-power patterns. I found no equivalent joint statement in the inspected claims. This does not certify priority or assess the cited mean formulas.

## value

PASS

The Gaussian scale alone loses both the repeated-prime correction and the distance to the next square. The joint limit recovers both at their natural scales, showing precisely that neither carries limiting information about the Gaussian fluctuation, and gives concrete masses for the correction's most prominent starting atoms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
