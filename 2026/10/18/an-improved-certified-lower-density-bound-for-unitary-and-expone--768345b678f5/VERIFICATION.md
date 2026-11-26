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

For a prime power the unitary divisors are 1 and p^e, and the exponential-divisor exponents are the positive divisors of e; multiplicativity gives exactly the specified positive local ratios. The residual atanh series starts at power 33 and its absolute value is bounded by the given geometric majorant. Flooring the resulting lower shifts and flooring each individual nonnegative CRT mass transition both preserve the lower-bound direction. Summed shift >= 0 certifies a finite product >= 1, including possible equality. Enforcing exponents <= 1 for p > 997 preserves the inequality and makes it strict unless n is 997-smooth (a density-zero exception). The infinite CRT limit is uniform: for any Q the fraction of n <= X divisible by some p^2 with p > Q is at most sum_{p>Q}p^-2, independent of X. This gives the Euler-product multiplier; comparison over odd integers gives 1-1/(2*997). An independently written replay computed lower mass 772112456436, total retained rounded mass 999878226389, and shift span [-167406,201533], giving exactly 384705031419237/498500000000000 > 7717/10000. Signed integer capacity follows from mass <= 10^12 at each lower transition, factors <= 996 and at most 16 retained terms for each prime; denominators also fit, and quantities summed are nonnegative. No sampled integer counts enter the proof.

## originality

PASS

This specific lower certificate strictly improves the earlier directly compared lower bounds. The same-day different record supplies an upper bound, not an implication of the lower bound. A later stronger lower result supersedes the numerical endpoint today without establishing prior coverage of the dated finding.

## value

PASS

The density was explicitly posed in prior work. A certified large-prime convolution with a uniform infinite-tail sieve substantially strengthens the six-prime certificate and moves beyond the earlier 77% bracket without relying on numerical counts up to a finite cutoff. The certificate gives a useful reproducible method and an advance at its date, although a subsequent bound further tightens it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
