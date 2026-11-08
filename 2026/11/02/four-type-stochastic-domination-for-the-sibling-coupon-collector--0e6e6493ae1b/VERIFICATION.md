---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For four independent positive coupon probabilities, Poissonized last-arrival conditioning gives exact G_p(z)=z Σ_k∫p_k e^(−p_k t)∏_{i≠k}(1−e^(−p_i t)+(z−1)p_i t e^(−p_i t))dt. Expanding at z=1 produces middle tail T=P(U≥3)=6Σ A_i/(1−p_i)^3−6Σ A_i−48∏p_i. After sorting unnormalized weights as r,r+v,r+v+w,r+v+w+z, multiplying 47/144−T by positive 144 S^4 Q yields a degree-16 integer polynomial. Independently regenerated all 955 nonzero coefficients by a fresh arbitrary-precision polynomial map, compared all against the actual 955-row source certificate.tsv; every coefficient exactly agreed and was strictly positive (minimum 47), with explicit positive r^14 v²,r^14 w²,r^14 z² terms. This proves P(U≥3)≤47/144 strict off uniform for the whole continuous simplex. U≥1 is certain; Long left-PGF order yields U≥2 via z↓0; U=4=24∏p_i≤3/32 by AM–GM. The exact uniform PMF (97,97,67,27)/288 sums to one, giving full ordinary stochastic domination.

## originality

PASS

Best-of-knowledge original four-type *ordinary* stochastic order against uniform, especially the middle tail k=3. Long already proves PGF and binomial-moment extremality and, together with AM–GM, the other threshold comparisons; these are credited. The accessible full Long manuscript could not be inspected, so an undiscovered appendix for the four-type ordinary order remains a priority risk, but the independent new exact 955-coefficient proof supplies the missing implication and motivates best-of-knowledge pass.

## value

PASS

A genuinely nontrivial first-order stochastic dominance theorem at four types, sharply separating ordinary upper-tail order from expectation, PGF and binomial-moment extremality. The complete 955-term positive polynomial settles a natural missing interior tail and an exact uniform extremizer, not just an arbitrary finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
